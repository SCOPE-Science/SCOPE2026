#!/usr/bin/env python3
"""Exhaustive verification of a minimal well-covered packing-coloring separation.

No third-party dependencies. Enumerates all unlabeled graphs through five
vertices, tests every candidate coloring using shortest-path distances, and
checks the greedy coloring directly from its vertex order.
"""
from itertools import permutations, product
from collections import deque

WITNESS_EDGES = ((0, 4), (1, 2), (1, 3), (2, 3), (3, 4))


def edge_pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def graph_from_mask(n, mask):
    out = [set() for _ in range(n)]
    for j, (u, v) in enumerate(edge_pairs(n)):
        if mask & (1 << j):
            out[u].add(v)
            out[v].add(u)
    return out


def all_unlabeled(n):
    pairs = edge_pairs(n)
    index = {e: j for j, e in enumerate(pairs)}
    mappings = []
    for p in permutations(range(n)):
        mappings.append([index[tuple(sorted((p[u], p[v])))] for u, v in pairs])
    seen = set()
    for mask in range(1 << len(pairs)):
        if mask in seen:
            continue
        orbit = set()
        for map_bits in mappings:
            renamed = sum(((mask >> t) & 1) << j for j, t in enumerate(map_bits))
            orbit.add(renamed)
        seen.update(orbit)
        yield graph_from_mask(n, mask)


def distances(adj):
    n = len(adj)
    d = [[n + 1] * n for _ in range(n)]
    for s in range(n):
        d[s][s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if d[s][w] > d[s][v] + 1:
                    d[s][w] = d[s][v] + 1
                    q.append(w)
    return d


def maximal_independent_sets(adj):
    n = len(adj)
    out = []
    for mask in range(1, 1 << n):
        chosen = [i for i in range(n) if mask >> i & 1]
        if any(v in adj[u] for k, u in enumerate(chosen) for v in chosen[k + 1:]):
            continue
        if all((mask >> w & 1) or any(w in adj[u] for u in chosen) for w in range(n)):
            out.append(chosen)
    return out


def packing_color(cols, d):
    return all(cols[u] != cols[v] or d[u][v] > cols[u]
               for u in range(len(cols)) for v in range(u + 1, len(cols)))


def greedy_color(cols, d):
    return packing_color(cols, d) and all(
        any(cols[u] == j and d[u][v] <= j for u in range(len(cols)))
        for v, i in enumerate(cols) for j in range(1, i))


def first_fit(adj, order):
    d = distances(adj)
    n = len(adj)
    colors = [0] * n
    for v in order:
        for c in range(1, n + 1):
            if all(colors[u] != c or d[v][u] > c for u in range(n)):
                colors[v] = c
                break
    return tuple(colors)


def exact_numbers(adj):
    n = len(adj)
    d = distances(adj)
    chi = n + 1
    gamma = 0
    packing_witness = None
    greedy_witness = None
    for cols in product(range(1, n + 1), repeat=n):
        high = max(cols)
        if high >= chi and high <= gamma:
            continue
        if not packing_color(cols, d):
            continue
        if high < chi:
            chi, packing_witness = high, cols
        if high > gamma and greedy_color(cols, d):
            gamma, greedy_witness = high, cols
    return chi, gamma, packing_witness, greedy_witness


def clique_tail(m):
    """Clique 0,...,m-1, pendant path 0--m--(m+1)."""
    n = m + 2
    adj = [set() for _ in range(n)]
    for u in range(m):
        for v in range(u + 1, m):
            adj[u].add(v)
            adj[v].add(u)
    adj[0].add(m)
    adj[m].add(0)
    adj[m].add(m + 1)
    adj[m + 1].add(m)
    return adj


def family_witnesses(m):
    n = m + 2
    adj = clique_tail(m)
    # b=2, a=1 are distinct clique vertices other than 0.
    coloring = [0] * n
    coloring[1], coloring[m] = 1, 1
    coloring[2], coloring[m + 1] = 2, 2
    for k, v in enumerate([0] + list(range(3, m)), 3):
        coloring[v] = k
    greedy_order = [m + 1, 1, 2, 0, m] + list(range(3, m))
    return tuple(coloring), greedy_order


def main():
    graph_counts = []
    well_counts = []
    gap = []
    for n in range(1, 6):
        ng = nw = 0
        for adj in all_unlabeled(n):
            ng += 1
            maximal = maximal_independent_sets(adj)
            well = len(set(map(len, maximal))) == 1
            if not well:
                continue
            nw += 1
            chi, gamma, low, high = exact_numbers(adj)
            if gamma > chi:
                edges = [(i, j) for i in range(n) for j in sorted(adj[i]) if i < j]
                gap.append((n, edges, chi, gamma))
                assert packing_color(low, distances(adj))
                assert greedy_color(high, distances(adj))
        graph_counts.append(ng)
        well_counts.append(nw)
    assert graph_counts == [1, 2, 4, 11, 34], graph_counts
    assert well_counts == [1, 2, 3, 7, 14], well_counts
    assert len(gap) == 1 and gap[0][0] == 5 and gap[0][2:] == (3, 4), gap

    fixed = [set() for _ in range(5)]
    for u, v in WITNESS_EDGES:
        fixed[u].add(v)
        fixed[v].add(u)
    witness_sets = maximal_independent_sets(fixed)
    assert len(witness_sets) == 5 and {len(s) for s in witness_sets} == {2}
    assert set(map(frozenset, witness_sets)) == {
        frozenset(s) for s in ((0, 1), (0, 2), (0, 3), (1, 4), (2, 4))}
    assert exact_numbers(fixed)[:2] == (3, 4)
    assert first_fit(fixed, (0, 1, 2, 3, 4)) == (1, 1, 2, 3, 4)
    assert packing_color((2, 1, 2, 3, 1), distances(fixed))
    # Check that the unique five-vertex gap graph has exactly the same edges up to relabeling.
    gap_edges = set(map(frozenset, gap[0][1]))
    target = set(map(frozenset, WITNESS_EDGES))
    assert any({frozenset((p[i], p[j])) for e in gap_edges for i, j in [tuple(e)]} == target
               for p in permutations(range(5)))
    # A second check tests arbitrarily parametrized witness construction,
    # including the exact small instances by full assignment enumeration.
    for m in range(3, 11):
        adj = clique_tail(m)
        near, order = family_witnesses(m)
        assert packing_color(near, distances(adj)) and max(near) == m
        greedy = first_fit(adj, order)
        assert max(greedy) == m + 1
        assert len({len(s) for s in maximal_independent_sets(adj)}) == 1
        assert {len(s) for s in maximal_independent_sets(adj)} == {2}
        if m <= 5:
            chi, gamma, *_ = exact_numbers(adj)
            assert (chi, gamma) == (m, m + 1), (m, chi, gamma)
    print('VERIFICATION_OK unlabeled_graph_counts=' + ','.join(map(str, graph_counts))
          + ' well_covered_counts=' + ','.join(map(str, well_counts))
          + ' unique_gap=(n=5,chi=3,Gamma=4)')
    print('WITNESS_FIRST_FIT=(1,1,2,3,4) PACKING_3=(2,1,2,3,1)')
    print('FAMILY_OK brute_orders=3..5 direct_witness_orders=3..10')


if __name__ == '__main__':
    main()
