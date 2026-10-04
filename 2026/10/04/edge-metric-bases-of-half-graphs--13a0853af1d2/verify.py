#!/usr/bin/env python3
from itertools import combinations, product
from collections import deque


def half_graph(p):
    vertices = [('a', i) for i in range(1, p + 1)] + [('b', j) for j in range(1, p + 1)]
    edges = [(('a', i), ('b', j)) for i in range(1, p + 1) for j in range(1, i + 1)]
    adjacency = {v: set() for v in vertices}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    distances = {}
    for start in vertices:
        d = {start: 0}
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if v not in d:
                    d[v] = d[u] + 1
                    queue.append(v)
        distances[start] = d
    return vertices, edges, distances


def resolves(edges, distances, landmarks):
    codes = []
    for u, v in edges:
        code = tuple(min(distances[s][u], distances[s][v]) for s in landmarks)
        codes.append(code)
    return len(codes) == len(set(codes))


def is_transversal(p, subset):
    chosen = set(subset)
    return all(((('a', r) in chosen) + (('b', r + 1) in chosen)) == 1 for r in range(1, p))


subset_checks = 0
basis_checks = 0
transversal_checks = 0
for p in range(2, 10):
    vertices, edges, distances = half_graph(p)
    # It suffices to rule out size p-2: a smaller resolving set could be extended to this size.
    for subset in combinations(vertices, p - 2):
        subset_checks += 1
        assert not resolves(edges, distances, subset), (p, subset, 'unexpected smaller generator')
    good = []
    for subset in combinations(vertices, p - 1):
        subset_checks += 1
        observed = resolves(edges, distances, subset)
        expected = is_transversal(p, subset)
        basis_checks += 1
        assert observed == expected, (p, subset, observed, expected)
        if observed:
            good.append(subset)
    assert len(good) == 2 ** (p - 1), (p, len(good))
    pairs = [(('a', r), ('b', r + 1)) for r in range(1, p)]
    for bits in product((0, 1), repeat=p - 1):
        subset = tuple(pairs[r][bits[r]] for r in range(p - 1))
        transversal_checks += 1
        assert resolves(edges, distances, subset), (p, subset, 'transversal failed')
print(f'VERIFY_OK p_range=2..9 subset_checks={subset_checks} basis_checks={basis_checks} transversal_checks={transversal_checks} max_order=18')
