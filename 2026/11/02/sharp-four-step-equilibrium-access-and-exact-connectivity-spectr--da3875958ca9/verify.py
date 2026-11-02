#!/usr/bin/env python3
"""Exact finite verification for three-player strict binary best-response graphs.

Every strict playerwise action preference at each fixed opponent profile
is one directed edge of the ordinary three-cube. All 2**12 orientations
are enumerated once, and all profile-to-equilibrium distances are exact.
"""
from collections import Counter, deque
from itertools import combinations


def edges(dim):
    """List each undirected hypercube edge once in canonical order."""
    return [(v, v ^ (1 << i)) for v in range(1 << dim)
            for i in range(dim) if not (v & (1 << i))]


def graph(dim, mask):
    """Bit 1 orients the canonical edge upward, bit 0 downward."""
    vertices = 1 << dim
    adj = [[] for _ in range(vertices)]
    for j, (u, v) in enumerate(edges(dim)):
        start, end = (u, v) if ((mask >> j) & 1) else (v, u)
        adj[start].append(end)
    return adj


def distances_to_set(adj, terminals):
    """Exact multi-source shortest distance in the reverse digraph."""
    rev = [[] for _ in adj]
    for u, nbrs in enumerate(adj):
        for v in nbrs:
            rev[v].append(u)
    dist = [None] * len(adj)
    queue = deque(terminals)
    for t in terminals:
        dist[t] = 0
    while queue:
        v = queue.popleft()
        for u in rev[v]:
            if dist[u] is None:
                dist[u] = dist[v] + 1
                queue.append(u)
    return dist


def floyd_distances(adj):
    """Independent all-pairs directed shortest paths by dynamic programming."""
    n = len(adj)
    infinity = n + 1
    d = [[0 if i == j else (1 if j in adj[i] else infinity)
          for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                candidate = d[i][k] + d[k][j]
                if candidate < d[i][j]:
                    d[i][j] = candidate
    return d


def classify(dim):
    totals = Counter()
    by_distance = Counter()
    by_equilibrium_count = Counter()
    examples = {}
    for mask in range(1 << len(edges(dim))):
        adj = graph(dim, mask)
        sinks = [v for v in range(1 << dim) if not adj[v]]
        if not sinks:
            totals['no_equilibrium'] += 1
            continue
        totals['with_equilibrium'] += 1
        by_equilibrium_count[len(sinks)] += 1
        d = distances_to_set(adj, sinks)
        if any(x is None for x in d):
            totals['not_weakly_acyclic'] += 1
            continue
        matrix = floyd_distances(adj)
        assert all(d[v] == min(matrix[v][s] for s in sinks) for v in range(1 << dim))
        depth = max(d)
        by_distance[depth] += 1
        examples.setdefault(depth, mask)
        b1 = all(all(x is not None for v, x in enumerate(distances_to_set(adj, [s]))
                     if v not in sinks) for s in sinks)
        b2 = all(all(matrix[v][s] < len(adj) + 1 for v in range(1 << dim)
                     if v not in sinks) for s in sinks)
        assert b1 == b2
        if b1:
            totals['connected'] += 1
    return totals, by_distance, by_equilibrium_count, examples


def count_with_equilibrium_by_inclusion_exclusion():
    e = edges(3)
    independent = Counter()
    for k in range(1, 9):
        for S in combinations(range(8), k):
            if all((u not in S or v not in S) for u, v in e):
                independent[k] += 1
    assert independent == {1: 8, 2: 16, 3: 8, 4: 2}, independent
    return sum((-1) ** (k+1) * c * (1 << (12 - 3*k))
               for k, c in independent.items())


def witness_check():
    """Explicit ordered arcs, distinct from bit-mask enumeration."""
    arcs = ((0, 2), (0, 4), (1, 0), (2, 3), (3, 1),
            (5, 4), (5, 1), (6, 4), (6, 2), (7, 6),
            (7, 5), (7, 3))
    e = {frozenset(p) for p in edges(3)}
    assert {frozenset(p) for p in arcs} == e
    adj = [[] for _ in range(8)]
    for u, v in arcs:
        adj[u].append(v)
    assert [v for v in range(8) if not adj[v]] == [4]
    d = distances_to_set(adj, [4])
    assert d[2] == 4 and max(d) == 4, d
    assert [2, 3, 1, 0, 4] == [2, adj[2][0], adj[3][0], adj[1][0], 4]
    return d


def main():
    t2, d2, _, _ = classify(2)
    assert t2 == {'no_equilibrium': 2, 'with_equilibrium': 14, 'connected': 14}, t2
    assert d2 == {1: 2, 2: 12}, d2
    t3, d3, n3, _ = classify(3)
    assert t3 == {'no_equilibrium': 962, 'with_equilibrium': 3134,
                  'connected': 2492}, t3
    assert d3 == {1: 258, 2: 644, 3: 1512, 4: 720}, d3
    assert n3 == {1: 2232, 2: 844, 3: 56, 4: 2}, n3
    assert sum(d3.values()) == t3['with_equilibrium']
    assert count_with_equilibrium_by_inclusion_exclusion() == t3['with_equilibrium']
    print('VERIFY_OK')
    print('two-player: ', dict(t2), 'worst-case-distance-counts', dict(d2))
    print('three-player:', dict(t3), 'worst-case-distance-counts', dict(d3),
          'number-of-equilibria-counts', dict(n3))
    print('sharp witness distances:', witness_check())


if __name__ == '__main__':
    main()
