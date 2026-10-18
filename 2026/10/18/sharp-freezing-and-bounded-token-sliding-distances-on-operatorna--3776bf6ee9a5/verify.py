#!/usr/bin/env python3
"""Finite checks for the Kneser-pair sliding theorem; standard-library only.

All states are sets of two-subsets of {0,...,n-1}.  This script separately
builds independent sets from the adjacency predicate and slide edges from
the removed/replacement pair condition, then tests structural distance claims.
"""
from itertools import combinations
from collections import Counter, deque


def independent_sets(n, k):
    edges = tuple(combinations(range(n), 2))
    out = []
    for idxs in combinations(range(len(edges)), k):
        if all(set(edges[i]) & set(edges[j]) for i, j in combinations(idxs, 2)):
            out.append(idxs)
    return edges, out


def slide_graph(edges, states):
    idx = {s: i for i, s in enumerate(states)}
    full = [frozenset(e) for e in edges]
    graph = []
    for state in states:
        ns = set()
        for old in state:
            others = tuple(e for e in state if e != old)
            for new in range(len(edges)):
                if new in state or not full[old].isdisjoint(full[new]):
                    continue
                if not all(full[new] & full[keep] for keep in others):
                    continue
                nbr = tuple(sorted(others + (new,)))
                ns.add(idx[nbr])
        graph.append(ns)
    assert all(i in graph[j] for i, ns in enumerate(graph) for j in ns)
    return graph


def bfs(graph, source):
    dist = [-1] * len(graph)
    dist[source] = 0
    Q = deque([source])
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                Q.append(v)
    return dist


def classify(edges, state):
    pairs = tuple(frozenset(edges[i]) for i in state)
    support = frozenset().union(*pairs)
    if len(support) == 3:
        assert all(sum(x in p for p in pairs) == 2 for x in support)
        return 'T', support
    assert len(support) == 4
    center = next(x for x in support if all(x in p for p in pairs))
    return 'S', (center, support - {center})


def adjacent_triangles(typ):
    t, data = typ
    if t == 'T':
        return (data,)
    center, leaves = data
    return tuple(frozenset((center, *pair)) for pair in combinations(sorted(leaves), 2))


def expected_three_distance(left, right):
    if left == right:
        return 0
    t, u = left[0], right[0]
    m = max(len(a & b) for a in adjacent_triangles(left)
            for b in adjacent_triangles(right))
    return 2 * (3 - m) + (t == 'S') + (u == 'S')


def check(n):
    summary = {'n': n}
    for k in (2, 3):
        edges, states = independent_sets(n, k)
        graph = slide_graph(edges, states)
        ecc = []
        types = [classify(edges, s) for s in states] if k == 3 else None
        for i, s in enumerate(states):
            ds = bfs(graph, i)
            assert -1 not in ds, (n, k, 'disconnected')
            if k == 3:
                for j, d in enumerate(ds):
                    assert d == expected_three_distance(types[i], types[j]), (n, k, i, j, d)
            ecc.append(max(ds))
        if k == 2:
            assert len(states) == n * (n - 1) * (n - 2) // 2
            assert set(map(len, graph)) == {2 * (n - 3)}
            assert set(ecc) == {4}
        else:
            assert len(states) == n * (n - 1) * (n - 2) * (n - 3) // 6 + n * (n - 1) * (n - 2) // 6
            assert Counter(t for t, v in types) == {'T': n * (n - 1) * (n - 2) // 6,
                                                      'S': n * (n - 1) * (n - 2) * (n - 3) // 6}
            assert all(len(graph[i]) == (3 if typ[0] == 'S' else 3 * (n - 3))
                       for i, typ in enumerate(types))
            Tecc = set(ecc[i] for i, typ in enumerate(types) if typ[0] == 'T')
            Secc = set(ecc[i] for i, typ in enumerate(types) if typ[0] == 'S')
            assert Tecc == {4 if n == 5 else 6 if n == 6 else 7}
            assert Secc == {4 if n == 5 else 5 if n == 6 else 7 if n == 7 else 8}
        summary['k' + str(k)] = {'states': len(states), 'edges': sum(map(len, graph)) // 2,
                                'eccentricities': dict(Counter(ecc))}
    if n <= 7:
        for k in range(4, n):
            edges, states = independent_sets(n, k)
            assert len(states) == n * len(tuple(combinations(range(n - 1), k)))
            assert all(len(g) == 0 for g in slide_graph(edges, states))
        summary['frozen_checked_through'] = n - 1
    return summary


def main():
    # Independent enumeration of pairwise-intersecting edge families, direct
    # adjacency generation, exact BFS, and a separate incidence-metric test.
    for n in range(5, 10):
        print(check(n), flush=True)
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    main()
