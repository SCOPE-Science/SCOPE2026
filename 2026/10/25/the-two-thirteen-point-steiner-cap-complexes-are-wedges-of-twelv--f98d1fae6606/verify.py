#!/usr/bin/env python3
"""Integral discrete-Morse certificates for both 13-point Steiner cap complexes.

Python 3 standard library only. All faces and incidences are reconstructed here.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations

POINTS = range(13)
BASES = ((0, 1, 4), (0, 2, 7))
OUT = ((0, 1, 4), (0, 2, 7), (1, 7, 9), (2, 4, 9))
IN = ((0, 1, 7), (0, 2, 4), (1, 4, 9), (2, 7, 9))
ORDERS = {
    "cyclic": (11, 1, 2, 10, 0, 8, 5, 4, 7, 12, 3, 9, 6),
    "switched": (4, 0, 9, 2, 3, 11, 5, 7, 1, 10, 6, 8, 12),
}
EXPECTED = {
    "cyclic": {
        "counts": (13, 78, 260, 455, 312, 39),
        "facets": {4: 117, 5: 39}, "pasch": 13,
        "critical": {0: 1, 3: 4, 4: 16}, "pairs": 568,
        "hasse": 4550, "unit_columns": (0, 1, 2, 5), "beta4": 12,
        "rank": (12, 66, 194, 261, 39),
        "crit3": (45, 293, 1298, 1794),
        "crit4": (121, 244, 425, 569, 968, 976, 4216, 4305,
                  4497, 4552, 4645, 4652, 4657, 4677, 4696, 4808),
    },
    "switched": {
        "counts": (13, 78, 260, 455, 312, 34),
        "facets": {4: 132, 5: 34}, "pasch": 8,
        "critical": {0: 1, 3: 2, 4: 19}, "pairs": 565,
        "hasse": 4520, "unit_columns": (0, 1), "beta4": 17,
        "rank": (12, 66, 194, 261, 34),
        "crit3": (165, 389),
        "crit4": (234, 482, 488, 1378, 1610, 1858, 2218, 2246,
                  2250, 4456, 4552, 4650, 5260, 5506, 5512,
                  6434, 7240, 7264, 7456),
    },
}


def mask(triple):
    return sum(1 << x for x in triple)


def make_designs():
    cyclic = {tuple(sorted(((x + s) % 13 for x in t)))
              for t in BASES for s in POINTS}
    removed = {tuple(sorted(t)) for t in OUT}
    added = {tuple(sorted(t)) for t in IN}
    assert removed <= cyclic and len(cyclic) == 26
    switched = (cyclic - removed) | added
    for design in (cyclic, switched):
        pair_counts = Counter(tuple(sorted(pair))
                              for triple in design
                              for pair in combinations(triple, 2))
        assert len(design) == 26 and len(pair_counts) == 78
        assert all(multiplicity == 1 for multiplicity in pair_counts.values())
    return {"cyclic": sorted(cyclic), "switched": sorted(switched)}


def pasch_count(design):
    count = 0
    for four in combinations(design, 4):
        degrees = Counter(x for triple in four for x in triple)
        if len(degrees) == 6 and set(degrees.values()) == {2}:
            count += 1
    return count


def complex_faces(design):
    blocked = [mask(t) for t in design]
    return {m for m in range(1 << 13)
            if not any((m & b) == b for b in blocked)}


def facet_counts(faces):
    facets = Counter()
    for m in faces:
        if not m:
            continue
        if all((m | (1 << i)) not in faces
               for i in POINTS if not (m & (1 << i))):
            facets[m.bit_count() - 1] += 1
    return dict(facets)


def toggle_matching(faces, order):
    remaining = set(faces) - {0}
    pairs = []
    assert set(order) == set(POINTS)
    for v in order:
        bit = 1 << v
        for m in sorted(remaining, key=lambda x: (x.bit_count(), x)):
            if m not in remaining or (m & bit):
                continue
            upper = m | bit
            if upper in remaining:
                remaining.remove(m)
                remaining.remove(upper)
                pairs.append((m, upper))
    assert len(remaining) + 2 * len(pairs) == len(faces) - 1
    return remaining, pairs


def acyclicity(faces, pairs):
    nodes = sorted(faces - {0})
    inverse = set(pairs)
    nexts = {m: [] for m in nodes}
    indegree = {m: 0 for m in nodes}
    edge_count = 0
    for upper in nodes:
        bits = [i for i in POINTS if upper & (1 << i)]
        for i in bits:
            lower = upper ^ (1 << i)
            if lower == 0:
                continue
            source, target = ((lower, upper) if (lower, upper) in inverse
                              else (upper, lower))
            nexts[source].append(target)
            indegree[target] += 1
            edge_count += 1
    q = deque(m for m in nodes if indegree[m] == 0)
    processed = 0
    while q:
        m = q.popleft()
        processed += 1
        for v in nexts[m]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    assert processed == len(nodes), (processed, len(nodes))
    return edge_count, processed


def boundary(mask_):
    bits = [v for v in POINTS if mask_ & (1 << v)]
    return tuple((mask_ ^ (1 << v), (1 if j % 2 == 0 else -1))
                 for j, v in enumerate(bits))


def morse_matrix(critical, pairs):
    crit3 = tuple(sorted(c for c in critical if c.bit_count() == 4))
    crit4 = tuple(sorted(c for c in critical if c.bit_count() == 5))
    crit3set = set(crit3)
    up = {lower: upper for lower, upper in pairs
          if lower.bit_count() == 4 and upper.bit_count() == 5}

    @lru_cache(maxsize=None)
    def project(simplex):
        if simplex in crit3set:
            return {simplex: 1}
        if simplex not in up:
            return {}
        other = up[simplex]
        coefficient = dict(boundary(other))[simplex]
        out = defaultdict(int)
        for facet, sign in boundary(other):
            if facet != simplex:
                for c, value in project(facet).items():
                    out[c] -= coefficient * sign * value
        return {c: value for c, value in out.items() if value}

    pos = {c: i for i, c in enumerate(crit3)}
    matrix = [[0] * len(crit4) for _ in crit3]
    for col, upper in enumerate(crit4):
        for facet, sign in boundary(upper):
            for c, value in project(facet).items():
                matrix[pos[c]][col] += sign * value
    return crit3, crit4, matrix


def determinant(matrix):
    size = len(matrix)
    result = 0
    for perm in permutations(range(size)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(size) for j in range(i + 1, size))
        prod = (-1) ** inversions
        for i, col in enumerate(perm):
            prod *= matrix[i][col]
        result += prod
    return result


def mod2_boundary_ranks(faces):
    by_dim = {d: sorted(m for m in faces if m.bit_count() == d + 1)
              for d in range(6)}
    ranks = []
    for d in range(1, 6):
        row_number = {m: j for j, m in enumerate(by_dim[d - 1])}
        pivots = {}
        for upper in by_dim[d]:
            col = 0
            for lower, _ in boundary(upper):
                col ^= 1 << row_number[lower]
            while col:
                leading = col.bit_length() - 1
                if leading not in pivots:
                    pivots[leading] = col
                    break
                col ^= pivots[leading]
        ranks.append(len(pivots))
    return tuple(ranks)


def run():
    designs = make_designs()
    for name in ("cyclic", "switched"):
        expected = EXPECTED[name]
        design = designs[name]
        assert pasch_count(design) == expected["pasch"]
        faces = complex_faces(design)
        counts = tuple(sum(m.bit_count() == d + 1 for m in faces)
                       for d in range(6))
        assert counts == expected["counts"]
        assert facet_counts(faces) == expected["facets"]
        assert mod2_boundary_ranks(faces) == expected["rank"]
        critical, pairs = toggle_matching(faces, ORDERS[name])
        assert len(pairs) == expected["pairs"]
        assert Counter(c.bit_count() - 1 for c in critical) == expected["critical"]
        edges, checked = acyclicity(faces, pairs)
        assert edges == expected["hasse"]
        c3, c4, boundary4 = morse_matrix(critical, pairs)
        assert c3 == expected["crit3"]
        assert c4 == expected["crit4"]
        columns = expected["unit_columns"]
        minor = [[row[j] for j in columns] for row in boundary4]
        assert determinant(minor) == 1, (name, minor)
        assert len(c4) - len(c3) == expected["beta4"]
        assert expected["beta4"] == 25 - expected["pasch"]
        print(f"{name}: 26 blocks, Pasch={expected['pasch']}, "
              f"nonempty faces={len(faces)-1}, f-vector={counts}")
        print(f"{name}: matched_pairs={len(pairs)}, "
              f"critical={expected['critical']}, "
              f"acyclic_vertices={checked}, incidence_arcs={edges}")
        print(f"{name}: integral degree-four-to-three Morse boundary "
              f"{len(c3)}x{len(c4)}; unit minor cols={columns}, det=1")
        print(f"{name}: reduced H4=Z^{expected['beta4']}; "
              "other reduced integral homology=0")
    cyclic_faces = complex_faces(designs["cyclic"])
    for k in range(1, 13):
        assert not any(m and all(bool(m & (1 << v)) ==
                bool(m & (1 << ((v + k) % 13))) for v in POINTS)
                for m in cyclic_faces)
    print("cyclic C13 action: character 12 at identity, -1 elsewhere")
    print("VERIFY_OK")


if __name__ == "__main__":
    run()
