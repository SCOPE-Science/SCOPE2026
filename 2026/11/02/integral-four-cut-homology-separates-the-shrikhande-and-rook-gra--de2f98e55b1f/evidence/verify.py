#!/usr/bin/env python3
"""Exact integral verification of the ordinary four-cut homology pair.
Python 3 standard library only. This program builds the Alexander dual
and verifies a complete acyclic matching and integer Morse differentials.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
import hashlib
import json

N = 16
V = tuple(range(N))


def graphs():
    coords = tuple((a, b) for a in range(4) for b in range(4))
    steps = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    ans = {}
    for name in ('Shrikhande', 'Rook'):
        adj = [set() for _ in V]
        for u, (a, b) in enumerate(coords):
            for v, (c, d) in enumerate(coords):
                if u == v:
                    continue
                if name == 'Shrikhande':
                    edge = ((c-a) % 4, (d-b) % 4) in steps
                else:
                    edge = a == c or b == d
                if edge:
                    adj[u].add(v)
        for u in V:
            assert len(adj[u]) == 6 and u not in adj[u]
            for v in V:
                if u != v:
                    assert (v in adj[u]) == (u in adj[v])
                    assert len(adj[u] & adj[v]) == (2 if v in adj[u] else 2)
        ans[name] = adj
    return ans


def connected4(adj, tup):
    allowed = set(tup)
    seen = {tup[0]}
    queue = [tup[0]]
    for u in queue:
        for v in adj[u]:
            if v in allowed and v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen) == 4


def faces_of_dual(adj):
    connected = {
        sum(1 << v for v in tup)
        for tup in combinations(V, 4) if connected4(adj, tup)
    }
    valid = bytearray(1 << N)
    valid[0] = 1
    faces = defaultdict(list)
    for mask in range(1, 1 << N):
        size = mask.bit_count()
        if size < 4:
            accept = True
        elif size == 4:
            accept = mask in connected
        else:
            accept = all(valid[mask ^ (1 << v)] for v in V if mask >> v & 1)
        if accept:
            valid[mask] = 1
            faces[size-1].append(mask)
    assert len(connected) + (1820 - len(connected)) == 1820
    # Independent direct criterion for every possible subset, without
    # trusting the recursive enumerator.
    disconnected = tuple(
        sum(1 << v for v in tup)
        for tup in combinations(V, 4) if not connected4(adj, tup)
    )
    for mask in range(1 << N):
        if mask.bit_count() < 4:
            direct = True
        else:
            direct = not any((mask & bad) == bad for bad in disconnected)
        assert direct == bool(valid[mask])
    return faces, len(connected), len(disconnected)


def oriented_boundary(face):
    pos = 0
    for vertex in V:
        if face & (1 << vertex):
            yield face ^ (1 << vertex), (1 if pos % 2 == 0 else -1)
            pos += 1


def matching_and_acyclicity(faces):
    cells = set(c for layer in faces.values() for c in layer)
    unmatched = set(cells)
    pairs = []
    for vertex in V:
        for lower in sorted(unmatched, key=lambda c: (c.bit_count(), c)):
            upper = lower | (1 << vertex)
            if not (lower & (1 << vertex)) and lower in unmatched and upper in unmatched:
                pairs.append((lower, upper))
                unmatched.remove(lower)
                unmatched.remove(upper)
    matched_lower = dict(pairs)
    indeg = {c: 0 for c in cells}
    forward = defaultdict(list)
    num_incidences = 0
    for upper in cells:
        for lower, sign in oriented_boundary(upper):
            if not lower:
                continue
            assert lower in cells and sign in (-1, 1)
            num_incidences += 1
            # Match edges point upward, every other face edge downward.
            source, target = ((lower, upper) if matched_lower.get(lower) == upper
                              else (upper, lower))
            forward[source].append(target)
            indeg[target] += 1
    queue = deque(c for c in cells if indeg[c] == 0)
    visited = 0
    while queue:
        source = queue.popleft()
        visited += 1
        for target in forward[source]:
            indeg[target] -= 1
            if not indeg[target]:
                queue.append(target)
    assert visited == len(cells), 'Matching has a directed cycle'
    return unmatched, pairs, num_incidences


def signed_morse_matrices(faces, critical, pairs):
    lower_upper = dict(pairs)
    upper_lower = {high: low for low, high in pairs}
    from functools import lru_cache

    @lru_cache(None)
    def eliminate(c):
        if c in critical:
            return {c: 1}
        if c in upper_lower:
            return {}
        high = lower_upper[c]
        terms = {}
        pivot = None
        for face, sign in oriented_boundary(high):
            if face == c:
                pivot = sign
            else:
                for crit, coeff in eliminate(face).items():
                    terms[crit] = terms.get(crit, 0) - sign * coeff
        assert pivot in (-1, 1)
        return {crit: pivot * coeff for crit, coeff in terms.items() if coeff}

    crit = {
        dim: sorted(c for c in critical if c.bit_count() == dim + 1)
        for dim in range(7)
    }
    boundaries = {}
    for dim in range(1, 7):
        cols = []
        for c in crit[dim]:
            terms = {}
            for face, sign in oriented_boundary(c):
                for target, coeff in eliminate(face).items():
                    terms[target] = terms.get(target, 0) + sign * coeff
            cols.append({target: coeff for target, coeff in terms.items() if coeff})
        boundaries[dim] = cols
    # Check cellular boundary-square zero without relying on ranks.
    for dim in range(2, 7):
        mid_cols = dict(zip(crit[dim-1], boundaries[dim-1]))
        for col in boundaries[dim]:
            composite = {}
            for mid, coeff in col.items():
                for row, val in mid_cols[mid].items():
                    composite[row] = composite.get(row, 0) + coeff*val
            assert not any(composite.values()), 'Morse boundary does not square to zero'
    return crit, boundaries


def unit_pivot_smith(matrix):
    """Unimodular row and column elimination, no rational arithmetic.

    If all nonzero pivots are units and the residual block is zero,
    the integer Smith invariant factors are all one, with this rank.
    """
    a = [row[:] for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    r = 0
    while r < min(m, n):
        pivot = next(((i, j) for i in range(r, m)
                      for j in range(r, n) if abs(a[i][j]) == 1), None)
        if pivot is None:
            break
        i, j = pivot
        a[i], a[r] = a[r], a[i]
        for row in a:
            row[j], row[r] = row[r], row[j]
        sign = a[r][r]
        for i in range(r+1, m):
            factor = a[i][r] // sign
            if factor:
                for j in range(r, n):
                    a[i][j] -= factor*a[r][j]
        for j in range(r+1, n):
            factor = a[r][j] // sign
            if factor:
                for i in range(r, m):
                    a[i][j] -= factor*a[i][r]
        assert a[r][r] in (-1, 1)
        assert all(a[i][r] == 0 for i in range(r+1, m))
        assert all(a[r][j] == 0 for j in range(r+1, n))
        r += 1
    assert all(a[i][j] == 0 for i in range(r, m) for j in range(r, n)), \
        'A nonunit Smith block remains'
    return r


def rank_mod_two_original(faces):
    """Independent bitset row reduction on original signed boundary mod 2."""
    ranks = {}
    for d in range(1, 7):
        rows = {f: i for i, f in enumerate(faces[d-1])}
        basis = {}
        for c in faces[d]:
            v = 0
            for row, _ in oriented_boundary(c):
                v ^= (1 << rows[row])
            while v:
                j = v.bit_length()-1
                if j in basis:
                    v ^= basis[j]
                else:
                    basis[j] = v
                    break
        ranks[d] = len(basis)
    return ranks


def main():
    results = {}
    for name, adj in graphs().items():
        faces, connected_count, disconnected_count = faces_of_dual(adj)
        critical, pairs, incidence_count = matching_and_acyclicity(faces)
        crit, matrices = signed_morse_matrices(faces, critical, pairs)
        ranks = {}
        for d in range(1, 7):
            matrix = [[col.get(face, 0) for col in matrices[d]]
                      for face in crit[d-1]]
            ranks[d] = unit_pivot_smith(matrix)
        betti = {}
        for d in range(1, 7):
            v = len(crit[d]) - ranks.get(d, 0) - ranks.get(d+1, 0)
            if v:
                assert v > 0
                betti[d] = v
        mod_ranks = rank_mod_two_original(faces)
        for d in range(1, 7):
            v = len(faces[d]) - mod_ranks.get(d, 0) - mod_ranks.get(d+1, 0)
            assert v == betti.get(d, 0)
        # Graphs have a full 2-skeleton, so the dual is connected.
        assert len(faces[0]) == 16 and len(faces[1]) == 120
        delta = {13-d: v for d, v in betti.items()}
        assert all(dim in (9, 10, 11) for dim in delta)
        results[name] = {
            'connected_four_sets': connected_count,
            'disconnected_four_sets': disconnected_count,
            'dual_faces_by_dimension': [len(faces[d]) for d in range(6)],
            'all_nonempty_dual_faces': sum(len(faces[d]) for d in range(6)),
            'pairs': len(pairs),
            'hasse_incidences': incidence_count,
            'critical_cells': {str(d): len(crit[d]) for d in range(6) if crit[d]},
            'unit_smith_ranks': {str(d): ranks[d] for d in range(2, 6)},
            'original_boundary_ranks_mod_2': {str(d): mod_ranks[d] for d in range(1, 6)},
            'dual_integral_reduced_betti': {str(k): v for k,v in sorted(betti.items())},
            'cut_integral_reduced_betti': {str(k): v for k,v in sorted(delta.items())},
        }
    assert results['Shrikhande']['cut_integral_reduced_betti'] == {'9': 12, '10': 2, '11': 65}
    assert results['Rook']['cut_integral_reduced_betti'] == {'10': 21, '11': 96}
    print(json.dumps(results, sort_keys=True, separators=(',', ':')))
    print('SHRIKHANDE_ROOK_ORDINARY_4CUT_INTEGRAL_HOMOLOGY_OK')

if __name__ == '__main__':
    main()
