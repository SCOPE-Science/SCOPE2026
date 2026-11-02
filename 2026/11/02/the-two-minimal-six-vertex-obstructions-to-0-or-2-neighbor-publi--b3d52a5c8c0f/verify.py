#!/usr/bin/env python3
"""Exact enumeration of 0-or-2-neighbor equilibrium obstructions through six vertices.
Requires only Python >= 3.8. All graphs are finite, simple, undirected and labeled.
"""
from collections import Counter
from itertools import combinations, permutations


def edges(n):
    return tuple(combinations(range(n), 2))


def adjacency(n, edge_mask):
    adj = [0] * n
    for j, (a, b) in enumerate(edges(n)):
        if (edge_mask >> j) & 1:
            adj[a] |= 1 << b
            adj[b] |= 1 << a
    return adj


def is_connected(adj):
    n = len(adj)
    reached = 1
    while True:
        expanded = reached
        for v in range(n):
            if reached & (1 << v):
                expanded |= adj[v]
        if expanded == reached:
            return reached == (1 << n) - 1
        reached = expanded


def equilibria(adj):
    n = len(adj)
    for strategy in range(1 << n):
        if all(((strategy >> v) & 1) == int((adj[v] & strategy).bit_count() in (0, 2))
               for v in range(n)):
            yield strategy


def canonical_edge_mask(adj):
    n = len(adj)
    basis = edges(n)
    return min(sum((1 << j) for j, (u, v) in enumerate(basis)
                   if (adj[perm[u]] >> perm[v]) & 1)
               for perm in permutations(range(n)))


def graph_from_edge_list(n, pairs):
    adj = [0] * n
    for u, v in pairs:
        assert 0 <= u < v < n
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def main():
    ref_a = graph_from_edge_list(6, [
        (0, 1), (0, 2), (0, 4), (0, 5),
        (1, 2), (2, 3), (2, 5), (3, 4)])
    ref_b = graph_from_edge_list(6, [
        (0, 1), (0, 2), (0, 4), (0, 5), (1, 2),
        (1, 3), (1, 4), (3, 4), (4, 5)])
    assert is_connected(ref_a) and is_connected(ref_b)
    assert not list(equilibria(ref_a)) and not list(equilibria(ref_b))
    ca, cb = canonical_edge_mask(ref_a), canonical_edge_mask(ref_b)
    assert ca != cb
    summary = {}
    bad_six = Counter()
    for n in range(1, 7):
        connected = no_equilibrium = 0
        for gm in range(1 << len(edges(n))):
            adj = adjacency(n, gm)
            if not is_connected(adj):
                continue
            connected += 1
            if next(equilibria(adj), None) is None:
                no_equilibrium += 1
                if n == 6:
                    bad_six[canonical_edge_mask(adj)] += 1
        summary[n] = (connected, no_equilibrium)
    expected = {1:(1, 0), 2:(1,0), 3:(4,0), 4:(38,0), 5:(728,0), 6:(26704,300)}
    assert summary == expected, (summary,expected)
    assert bad_six == Counter({ca:180, cb:120}), (bad_six,ca,cb)
    print('VERIFIED: exhaustive labeled connected graphs with 1..6 vertices')
    print('n: (connected graphs, non-equilibrium graphs)')
    for n in range(1,7):
        print(n, summary[n])
    print('Canonical six-vertex obstruction masks:',dict(sorted(bad_six.items())))
    print('VERIFIED: exactly two isomorphism classes, with 180 and 120 labelings')

if __name__ == '__main__':
    main()
