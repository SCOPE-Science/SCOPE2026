#!/usr/bin/env python3
"""Exact finite verification of the first three higher-independence complexes
of the explicitly specified eleven-vertex Herschel graph.

Python 3, standard library only. Checks face enumeration in two independent ways,
full directed Hasse acyclicity, integral algebraic Morse cancellation, and
independent mod-two simplicial homology. No statistical sampling.
"""
from collections import Counter, defaultdict, deque
import json

N = 11
EDGES = (
    (0, 5), (0, 6), (0, 9), (0, 10),
    (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 7), (2, 8), (2, 9), (2, 10),
    (3, 5), (3, 7), (3, 9),
    (4, 6), (4, 8), (4, 10),
)
ORDERS = {
    1: (6, 5, 8, 2, 7, 1, 4, 10, 9, 3, 0),
    2: (10, 5, 4, 2, 8, 6, 0, 1, 7, 3, 9),
    3: (4, 2, 3, 0, 10, 6, 9, 5, 8, 7, 1),
}
EXPECTED_CRITICAL = {1: {2: 2}, 2: {3: 10}, 3: {4: 3, 5: 1}}
EXPECTED_FACE_COUNTS = {1: 124, 2: 346, 3: 658}
EXPECTED_HASSE_INCIDENCES = {1: 349, 2: 1150, 3: 2536}


def neighbors():
    nb = [0] * N
    for x, y in EDGES:
        assert 0 <= x < y < N
        nb[x] |= 1 << y
        nb[y] |= 1 << x
    return tuple(nb)


def independent_graph_construction():
    ed = set()
    for t, (x, y) in enumerate(((0, 1), (0, 1), (1, 2), (1, 2),
                                  (2, 0), (2, 0))):
        z = 5 + t
        for a in (x, y, 3 + (t % 2)):
            ed.add(tuple(sorted((a, z))))
    assert ed == set(EDGES)
    assert len(ed) == 18
    assert [sum(i in e for e in ed) for i in range(N)] == [4, 4, 4, 3, 3] + [3] * 6


def connected(mask, nb):
    if mask == 0:
        return False
    found = mask & -mask
    pending = found
    while pending:
        b = pending & -pending
        pending ^= b
        extension = nb[b.bit_length() - 1] & mask & ~found
        found |= extension
        pending |= extension
    return found == mask


def component_size_test(mask, r, nb):
    remaining = mask
    while remaining:
        seed = remaining & -remaining
        seen = seed
        pending = seed
        while pending:
            b = pending & -pending
            pending ^= b
            extension = nb[b.bit_length() - 1] & mask & ~seen
            seen |= extension
            pending |= extension
        if seen.bit_count() > r:
            return False
        remaining &= ~seen
    return True


def faces_by_forbidden_connected_sets(r, nb):
    forbidden = [x for x in range(1 << N)
                 if x.bit_count() == r + 1 and connected(x, nb)]
    return {x for x in range(1 << N)
            if all((x & f) != f for f in forbidden)}, len(forbidden)


def face_set(r, nb):
    a = {x for x in range(1 << N) if component_size_test(x, r, nb)}
    b, nf = faces_by_forbidden_connected_sets(r, nb)
    assert a == b, 'independent face tests disagree'
    assert len(a) == EXPECTED_FACE_COUNTS[r]
    return a, nf


def element_matching(fs, order):
    unmatched = set(fs)
    pairs = []
    for vertex in order:
        bit = 1 << vertex
        for lower in sorted(unmatched):
            if lower & bit:
                continue
            upper = lower | bit
            if upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    assert len(unmatched) + 2 * len(pairs) == len(fs)
    assert all(upper == (lower | (1 << v))
               for lower, upper in pairs
               for v in range(N) if upper & (1 << v) and not lower & (1 << v))
    return pairs, unmatched


def hasse_acyclicity(fs, pairs):
    reversed_edges = set(pairs)
    assert len(reversed_edges) == len(pairs)
    indeg = {x: 0 for x in fs}
    successor = defaultdict(list)
    incidences = 0
    for upper in fs:
        sub = upper
        while sub:
            bit = sub & -sub
            lower = upper ^ bit
            assert lower in fs
            if (lower, upper) in reversed_edges:
                u, v = lower, upper
            else:
                u, v = upper, lower
            successor[u].append(v)
            indeg[v] += 1
            incidences += 1
            sub ^= bit
    queue = deque(x for x, degree in indeg.items() if degree == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in successor[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    assert visited == len(fs), 'directed Hasse cycle exists'
    return incidences


def signed_boundary(mask):
    out = {}
    i = 0
    sub = mask
    while sub:
        bit = sub & -sub
        out[mask ^ bit] = 1 if i % 2 == 0 else -1
        i += 1
        sub ^= bit
    return out


def integral_morse_boundary(fs, pairs):
    # Elementary unit-pivot cancellation in the augmented chain complex.
    # The Schur-complement update is exact over Z, not floating point.
    d = {x: signed_boundary(x) for x in fs}
    active = set(fs)
    pivots = []
    for lower, upper in pairs:
        assert lower in active and upper in active
        coefficient = d[upper].get(lower, 0)
        assert abs(coefficient) == 1, ('nonunit pivot', lower, upper, coefficient)
        pivots.append(coefficient)
        for x in list(active):
            if x == upper or x.bit_count() != upper.bit_count():
                continue
            a = d[x].get(lower, 0)
            if not a:
                continue
            for row, c in d[upper].items():
                updated = d[x].get(row, 0) - a * coefficient * c
                if updated:
                    d[x][row] = updated
                else:
                    d[x].pop(row, None)
        active.remove(lower)
        active.remove(upper)
        del d[lower]
        del d[upper]
        for x in active:
            d[x].pop(lower, None)
            d[x].pop(upper, None)
    assert all(row in active for b in d.values() for row in b)
    assert all(not b for b in d.values()), 'nonzero integral Morse differential'
    return {x: d[x] for x in sorted(active)}, Counter(pivots)


def gf2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)


def mod2_homology(fs):
    grouped = defaultdict(list)
    for x in fs:
        grouped[x.bit_count() - 1].append(x)
    for group in grouped.values():
        group.sort()
    ranks = {}
    betti = {}
    for dim in sorted(grouped):
        if dim == -1:
            continue
        row_index = {mask: j for j, mask in enumerate(grouped[dim - 1])}
        cols = []
        for upper in grouped[dim]:
            bitcol = 0
            for face in signed_boundary(upper):
                bitcol ^= 1 << row_index[face]
            cols.append(bitcol)
        ranks[dim] = gf2_rank(cols)
    for dim in sorted(grouped):
        if dim >= 0:
            betti[dim] = len(grouped[dim]) - ranks[dim] - ranks.get(dim + 1, 0)
    return {d: m for d, m in betti.items() if m}, ranks


def main():
    independent_graph_construction()
    nb = neighbors()
    assert all((nb[i] >> j) & 1 == (nb[j] >> i) & 1
               for i in range(N) for j in range(N))
    results = {}
    previous = set()
    for r in (1, 2, 3):
        fs, number_forbidden = face_set(r, nb)
        assert previous <= fs
        previous = fs
        pairs, crit = element_matching(fs, ORDERS[r])
        crit_counts = dict(Counter(x.bit_count() - 1 for x in crit))
        assert crit_counts == EXPECTED_CRITICAL[r], (r, crit_counts)
        ninc = hasse_acyclicity(fs, pairs)
        assert ninc == EXPECTED_HASSE_INCIDENCES[r], (r, ninc)
        reduced, signs = integral_morse_boundary(fs, pairs)
        assert set(reduced) == crit
        betti, ranks = mod2_homology(fs)
        assert betti == EXPECTED_CRITICAL[r], (r, betti)
        dimension_counts = dict(sorted(Counter(x.bit_count() - 1 for x in fs).items()))
        red_euler = sum((-1)**(x.bit_count() - 1) for x in fs)
        assert red_euler == sum((-1)**d * c for d, c in crit_counts.items())
        results[str(r)] = {
            'augmented_faces': len(fs),
            'forbidden_connected_sets_of_size_r_plus_1': number_forbidden,
            'face_counts_by_dimension': dimension_counts,
            'matched_pairs': len(pairs),
            'Hasse_incidences': ninc,
            'critical_cells_by_dimension': crit_counts,
            'critical_masks': sorted(crit),
            'integral_Morse_boundary_nonzero_entries': sum(len(x) for x in reduced.values()),
            'integral_unit_pivot_signs': dict(signs),
            'reduced_Euler_characteristic': red_euler,
            'independent_mod2_reduced_Betti': betti,
            'independent_mod2_boundary_ranks': ranks,
        }
    print(json.dumps(results, ensure_ascii=False, sort_keys=True, separators=(',', ':')))
    print('HERSCHEL_HIGHER_INDEPENDENCE_1_2_3_INTEGRAL_OK')


if __name__ == '__main__':
    main()
