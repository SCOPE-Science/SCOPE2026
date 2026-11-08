#!/usr/bin/env python3
"""Standalone exhaustive checks for a preference-stable colouring theorem.

No dependencies outside the Python standard library.
"""
from itertools import permutations, product

VERTICES = (0, 1, 2, 3, 4)  # u, v, x, y, z
BASE_EDGES = tuple((a, b) for a in (0, 1) for b in (2, 3, 4)) + ((2, 3),)
ORDERS = tuple(permutations((0, 1, 2)))
PROPER = tuple(c for c in product(range(3), repeat=5)
               if all(c[a] != c[b] for a, b in BASE_EDGES))
assert len(PROPER) == 12


def envy_arcs(assignment, preference):
    ranks = tuple(tuple(p.index(i) for i in range(3)) for p in preference)
    arcs = set()
    for a, b in BASE_EDGES:
        if ranks[a][assignment[b]] < ranks[a][assignment[a]]:
            arcs.add((a, b))
        if ranks[b][assignment[a]] < ranks[b][assignment[b]]:
            arcs.add((b, a))
    return arcs


def is_acyclic_dfs(arcs):
    adj = [[] for _ in VERTICES]
    for a, b in arcs:
        adj[a].append(b)
    mark = [0] * 5

    def visit(v):
        mark[v] = 1
        for w in adj[v]:
            if mark[w] == 1:
                return False
            if mark[w] == 0 and not visit(w):
                return False
        mark[v] = 2
        return True

    return all(mark[v] != 0 or visit(v) for v in VERTICES)


def is_acyclic_closure(arcs):
    reach = [0] * 5
    for a, b in arcs:
        reach[a] |= 1 << b
    for k in VERTICES:
        for i in VERTICES:
            if reach[i] & (1 << k):
                reach[i] |= reach[k]
    return not any(reach[i] & (1 << i) for i in VERTICES)


def has_mutual_pair(arcs):
    return any((a, b) in arcs and (b, a) in arcs for a, b in BASE_EDGES)


def count_with(method):
    no_stable = always_mutual = longer_cycle_needed = 0
    hist = [0] * 13
    for profile in product(ORDERS, repeat=5):
        successful = 0
        pair_free = False
        for assignment in PROPER:
            arcs = envy_arcs(assignment, profile)
            if not has_mutual_pair(arcs):
                pair_free = True
            if method(arcs):
                successful += 1
        hist[successful] += 1
        if successful == 0:
            no_stable += 1
            if pair_free:
                longer_cycle_needed += 1
            else:
                always_mutual += 1
    return no_stable, always_mutual, longer_cycle_needed, tuple(hist)


def family_edges(m, r):
    n = 2 * m + r
    total = n + 2
    edges = [(u, b) for u in (0, 1) for b in range(2, total)]
    edges += [(2 + 2 * j, 3 + 2 * j) for j in range(m)]
    return total, tuple(edges)


def orientation_bound(m, r):
    total, edges = family_edges(m, r)
    n = total - 2
    if n <= 2:
        # All edges from {u,v} to the other side; pair edge left-to-right.
        arrows = [(u, b) for u, b in edges if u in (0, 1)]
        arrows += [(u, b) for u, b in edges if u not in (0, 1)]
    else:
        # All B-A edges point to A; pair edges left-to-right.
        arrows = [(b, u) if u in (0, 1) else (u, b) for u, b in edges]
    reach = [set((v,)) for v in range(total)]
    for _ in range(total):
        for a, b in arrows:
            reach[a] |= reach[b]
    return max(map(len, reach))


def prove_obstruction():
    # Rankings top-to-bottom, using 0/1/2 for colors 1/2/3.
    profile = ((2, 1, 0), (0, 1, 2), (1, 0, 2),
               (0, 2, 1), (2, 0, 1))
    for assignment in PROPER:
        assert has_mutual_pair(envy_arcs(assignment, profile)), assignment
    return len(PROPER)


def main():
    assert prove_obstruction() == 12
    assert len(ORDERS) ** 5 == 7776
    a = count_with(is_acyclic_dfs)
    b = count_with(is_acyclic_closure)
    assert a == b, (a, b)
    assert a[:3] == (624, 576, 48), a
    assert sum(a[3]) == 7776
    assert a[3][0] == 624
    for m in range(0, 5):
        for r in range(0, 9):
            n = 2 * m + r
            if n == 0:
                continue
            bound = orientation_bound(m, r)
            assert bound <= (2 if n == 1 else 3 if (m == 0 or n == 2) else 4), (m, r, bound)
    print('OBSTRUCTION_ALL_12_PROPER_COLOURINGS_MUTUALLY_BLOCKED_OK')
    print('TWO_INDEPENDENT_EXHAUSTIVE_7776_PROFILE_ALGORITHMS_OK')
    print('NO_STABLE_3', a[0], 'ALWAYS_MUTUAL', a[1], 'LONGER_CYCLE_ONLY', a[2])
    print('EXPLICIT_REACHABILITY_ORIENTATIONS_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
