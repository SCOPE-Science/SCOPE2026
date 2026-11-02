#!/usr/bin/env python3
"""Finite independent check of independent resolving bases in clique-path graphs.

Uses only graph adjacency and BFS, not the theoretical distance formula.
All vertices and all independent landmark sets up to first feasible size
are enumerated in each tested case; these finite checks do not prove
universality of the formulas.
"""
from collections import deque
from itertools import combinations, product
from math import comb, factorial


def distances(length, colors):
    vertices = list(product(range(length), range(colors)))
    neighbors = [[] for _ in vertices]
    for a, (x, c) in enumerate(vertices):
        for b, (y, d) in enumerate(vertices):
            if a != b and ((x == y and c != d) or (c == d and abs(x-y) == 1)):
                neighbors[a].append(b)
    matrix = []
    for v in range(len(vertices)):
        ds = [-1] * len(vertices)
        ds[v] = 0
        queue = deque([v])
        while queue:
            u = queue.popleft()
            for w in neighbors[u]:
                if ds[w] == -1:
                    ds[w] = ds[u] + 1
                    queue.append(w)
        assert all(a >= 0 for a in ds)
        matrix.append(ds)
    return vertices, neighbors, matrix


def expected(length, colors):
    if colors == 2:
        return (None, 0) if length == 2 else (2, 2)
    if colors == 3:
        return (None, 0) if length < 3 else (3, 12 * comb(length, 3))
    return (None, 0) if length < colors - 1 else (colors - 1, factorial(colors) * comb(length, colors - 1))


def test(length, colors):
    vs, neigh, ds = distances(length, colors)
    indexes = {p: i for i, p in enumerate(vs)}
    candidates = 0
    for size in range(1, length + 1):
        total = 0
        for levels in combinations(range(length), size):
            for chosen_colors in product(range(colors), repeat=size):
                ids = tuple(indexes[(x, c)] for x, c in zip(levels, chosen_colors))
                # Check independence using original adjacency, not tuple shortcuts.
                selected = set(ids)
                if any(selected.intersection(neigh[v]) for v in ids):
                    continue
                candidates += 1
                codes = [tuple(ds[v][s] for s in ids) for v in range(len(vs))]
                if len(set(codes)) == len(vs):
                    total += 1
        if total:
            got = (size, total)
            break
    else:
        got = (None, 0)
    want = expected(length, colors)
    assert got == want, (length, colors, got, want)
    print(f'PASS L={length} q={colors} minimum={got[0]} bases={got[1]} independent_cases={candidates}', flush=True)
    return candidates


if __name__ == '__main__':
    total = 0
    cases = [(l, q) for q, hi in [(2, 8), (3, 7), (4, 6), (5, 6), (6, 6)]
             for l in range(2, hi + 1)]
    for length, colors in cases:
        total += test(length, colors)
    print(f'ALL PASS: {len(cases)} graphs; {total} independently constructed landmark sets tested.')
