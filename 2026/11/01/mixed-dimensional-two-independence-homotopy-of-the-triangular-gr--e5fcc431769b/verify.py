"""Exact finite verification for the higher-independence complexes of T_5,T_6,T_7.

Run with Python 3.10+; only the standard library is used.
The integer coefficients and the simplicial orientations are reconstructed here.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import json


def bits(x):
    while x:
        b = x & -x
        x -= b
        yield b.bit_length() - 1


def make_graph(n):
    edges = list(combinations(range(n), 2))
    adj = []
    for i, e in enumerate(edges):
        adj.append(sum(1 << j for j, f in enumerate(edges)
                       if i != j and (e[0] in f or e[1] in f)))
    return edges, adj


def good_degrees(mask, adj):
    for i in bits(mask):
        if (mask & adj[i]).bit_count() > 1:
            return False
    return True


def good_components(mask, adj):
    remaining = mask
    while remaining:
        start = remaining & -remaining
        stack = start
        seen = 0
        while stack:
            bit = stack & -stack
            stack -= bit
            if seen & bit:
                continue
            seen |= bit
            i = bit.bit_length() - 1
            stack |= (adj[i] & mask) & ~seen
        if seen.bit_count() > 2:
            return False
        remaining &= ~seen
    return True


def faces_of(n):
    edges, adj = make_graph(n)
    # The ambient enumeration is exhaustive: exactly 2^binom(n,2) masks.
    faces = []
    for m in range(1, 1 << len(edges)):
        a = good_degrees(m, adj)
        b = good_components(m, adj)
        assert a == b, (n, m)
        if a:
            faces.append(m)
    return edges, adj, faces


def signed_boundary(mask):
    return {mask ^ (1 << i): (-1 if k % 2 else 1)
            for k, i in enumerate(bits(mask))}


def match_faces(faces, nv):
    unmatched = set(faces)
    pairs = []
    for vertex in range(nv):
        bit = 1 << vertex
        for lower in faces:
            if lower not in unmatched or (lower & bit):
                continue
            upper = lower | bit
            if upper in unmatched:
                pairs.append((lower, upper))
                unmatched.remove(lower)
                unmatched.remove(upper)
    return pairs, sorted(unmatched)


def directed_acyclic(faces, pairs):
    fs = set(faces)
    matched = set(pairs)
    arrows = defaultdict(list)
    indeg = {f: 0 for f in faces}
    covering = 0
    for upper in faces:
        if upper.bit_count() == 1:
            continue
        for i in bits(upper):
            lower = upper ^ (1 << i)
            assert lower in fs
            if (lower, upper) in matched:
                src, dst = lower, upper
            else:
                src, dst = upper, lower
            arrows[src].append(dst)
            indeg[dst] += 1
            covering += 1
    queue = deque(sorted(f for f in faces if indeg[f] == 0))
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in arrows[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                queue.append(y)
    assert visited == len(faces)
    return covering


def recursive_morse_matrix(pairs, critical):
    upward = {lo: hi for lo, hi in pairs}
    crit = set(critical)

    @lru_cache(None)
    def projection(face):
        if face not in upward:
            return {face: 1} if face in crit else {}
        upper = upward[face]
        bd = signed_boundary(upper)
        pivot = bd.pop(face)
        assert abs(pivot) == 1
        out = Counter()
        for lower, coeff in bd.items():
            for endpoint, value in projection(lower).items():
                out[endpoint] -= coeff * pivot * value
        return {k: v for k, v in out.items() if v}

    maps = {}
    for d in range(1, max(c.bit_count() - 1 for c in critical) + 1):
        maps[d] = {}
        for cell in critical:
            if cell.bit_count() != d + 1:
                continue
            out = Counter()
            for lower, coeff in signed_boundary(cell).items():
                for endpoint, value in projection(lower).items():
                    out[endpoint] += coeff * value
            maps[d][cell] = {k: v for k, v in out.items() if v}
    return maps


def cancellation_morse_matrix(faces, pairs):
    """Independent, exact Schur-complement cancellation over the integers."""
    maximum = max(f.bit_count() - 1 for f in faces)
    maps = {d: {f: signed_boundary(f) for f in faces
                if f.bit_count() == d + 1}
            for d in range(1, maximum + 1)}
    grouped = defaultdict(list)
    for lo, hi in pairs:
        grouped[hi.bit_count() - 1].append((lo, hi))
    for d in sorted(grouped, reverse=True):
        for lower, upper in grouped[d]:
            pivot_col = maps[d][upper]
            pivot = pivot_col[lower]
            assert abs(pivot) == 1, (d, lower, upper, pivot)
            for c, col in list(maps[d].items()):
                if c == upper:
                    continue
                a = col.get(lower, 0)
                if not a:
                    continue
                t = a // pivot
                for row, coeff in pivot_col.items():
                    new = col.get(row, 0) - t * coeff
                    if new:
                        col[row] = new
                    else:
                        col.pop(row, None)
            del maps[d][upper]
            if d + 1 in maps:
                for col in maps[d + 1].values():
                    col.pop(upper, None)
            if d - 1 in maps:
                maps[d - 1].pop(lower, None)
    return maps


def determinant(matrix):
    """Fraction-free Bareiss determinant with exact integer arithmetic."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [list(map(int, row)) for row in matrix]
    sign, denom = 1, 1
    for k in range(n - 1):
        j = next((i for i in range(k, n) if a[i][k]), None)
        if j is None:
            return 0
        if j != k:
            a[k], a[j] = a[j], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * p - a[i][k] * a[k][j]
                assert num % denom == 0
                a[i][j] = num // denom
            a[i][k] = 0
        denom = p
    return sign * a[n - 1][n - 1]


def unimodular_minor(maps, critical):
    rows = sorted(f for f in critical if f.bit_count() == 3)
    cols = sorted(f for f in critical if f.bit_count() == 4)
    if not rows:
        return None
    # Deterministic independent column selection by Gaussian elimination over F_2.
    pivots, selected = {}, []
    for j, cell in enumerate(cols):
        v = sum(1 << i for i, row in enumerate(rows)
                if maps[3][cell].get(row, 0) % 2)
        while v:
            i = v.bit_length() - 1
            if i not in pivots:
                pivots[i] = v
                selected.append(j)
                break
            v ^= pivots[i]
        if len(selected) == len(rows):
            break
    if len(selected) != len(rows):
        return {"rank_mod2": len(selected)}
    minor = [[maps[3][cols[j]].get(row, 0) for j in selected]
             for row in rows]
    return {"rank_mod2": len(rows), "selected_column_indices": selected,
            "determinant": determinant(minor), "matrix": minor}


def run(n):
    edges, adj, faces = faces_of(n)
    face_set = set(faces)
    facet_counts = Counter()
    for face in faces:
        if all((face | (1 << i)) not in face_set
               for i in range(len(edges)) if not ((face >> i) & 1)):
            facet_counts[face.bit_count() - 1] += 1
    pairs, critical = match_faces(faces, len(edges))
    incidence_count = directed_acyclic(faces, pairs)
    recursive = recursive_morse_matrix(pairs, critical)
    cancellation = cancellation_morse_matrix(faces, pairs)
    assert all(recursive[d] == cancellation[d] for d in recursive)
    assert all(not col for d, col in cancellation.items() if d not in recursive)
    result = {
        "n": n,
        "face_vector": [sum(f.bit_count() == k for f in faces)
                        for k in range(1, max(f.bit_count() for f in faces)+1)],
        "total_nonempty_faces": len(faces),
        "hasse_incidences": incidence_count,
        "matched_pairs": len(pairs),
        "facet_vector": [facet_counts.get(i, 0)
                         for i in range(max(facet_counts) + 1)],
        "critical_vector": [sum(f.bit_count() == k for f in critical)
                            for k in range(1, max(f.bit_count() for f in critical)+1)],
        "morse_nonzero_boundary_entries":
            {str(d): sum(len(col) for col in cols.values())
             for d, cols in recursive.items()},
    }
    if n == 7:
        result["degree_three_to_two_minor"] = unimodular_minor(recursive, critical)
    return result


def main():
    expected = {
        5: {"face_vector": [10,45,30], "matched_pairs":39,
            "critical_vector": [1,6], "hasse_incidences": 180,
            "facet_vector": [0,0,30]},
        6: {"face_vector": [15,105,195,90], "matched_pairs":185,
            "critical_vector": [1,0,24,10], "hasse_incidences": 1155,
            "facet_vector": [0,0,15,90]},
        7: {"face_vector": [21,210,735,945], "matched_pairs":747,
            "critical_vector": [1,0,8,408], "hasse_incidences": 6405,
            "facet_vector": [0,0,0,945]},
    }
    for n in (5,6,7):
        out = run(n)
        for key, val in expected[n].items():
            assert out[key] == val, (n, key, out[key], val)
        if n == 6:
            assert all(x == 0 for x in out['morse_nonzero_boundary_entries'].values())
        if n == 7:
            assert out['degree_three_to_two_minor']['determinant'] in (-1,1)
        print(json.dumps(out,sort_keys=True,separators=(',',':')))
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    main()
