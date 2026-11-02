"""Exact finite sanity checks for dual vertices of block-equilateral metrics.

No external packages required. The quarter-grid enumerates *all* vertices
for the test parameters: a connected tight graph fixes every coordinate
as a sum of quarter-integer edge lengths from the basepoint.
"""
from itertools import product
from math import prod

PROFILES = [
    ((2, 1), (1, 3)),
    ((3, 1), (3, 1)),
    ((2, 2), (1, 3)),
    ((3, 2), (1, 2)),
    ((2, 1, 1), (1, 2, 3)),
    ((2, 2, 1), (1, 3, 2)),
    ((3, 1, 1), (3, 2, 1)),
    ((2, 2, 2), (1, 2, 3)),
    ((3, 3), (1, 3)),
    ((1, 1, 1), (1, 3, 2)),
]
# Each distance is scaled by four; low cluster i has internal length ticks[i].

def exact_vertices(sizes, ticks):
    n = sum(sizes)
    clusters = tuple(i for i, m in enumerate(sizes) for _ in range(m))
    d = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                d[i][j] = ticks[clusters[i]] if clusters[i] == clusters[j] else 4
    edges = [(i, j, d[i][j]) for i in range(n) for j in range(i + 1, n)]
    vertices = set()
    for tail in product(range(-4, 5), repeat=n - 1):
        f = (0,) + tail
        parent = list(range(n))
        def root(v):
            while v != parent[v]:
                v = parent[v]
            return v
        valid = True
        for i, j, length in edges:
            delta = abs(f[i] - f[j])
            if delta > length:
                valid = False
                break
            if delta == length:
                ri, rj = root(i), root(j)
                parent[ri] = rj
        if valid and len({root(i) for i in range(n)}) == 1:
            vertices.add(f)
    return vertices


def predicted_vertices(sizes, ticks):
    values = []
    for high_low in product((0, 1), repeat=len(sizes)):
        if min(high_low) == max(high_low):
            continue
        states = []
        for m, tick, high in zip(sizes, ticks, high_low):
            anchor = 4 if high else 0
            other = 4 - tick if high else tick
            local = tuple(tuple(anchor if (mask >> j) & 1 else other for j in range(m))
                          for mask in range(1, 1 << m))
            states.append(local)
        for parts in product(*states):
            f = tuple(x for part in parts for x in part)
            values.append(tuple(x - f[0] for x in f))
    assert len(values) == len(set(values))
    return set(values)


def run():
    count = 0
    for sizes, ticks in PROFILES:
        actual = exact_vertices(sizes, ticks)
        predicted = predicted_vertices(sizes, ticks)
        expected = ((1 << len(sizes)) - 2) * prod((1 << m) - 1 for m in sizes)
        assert len(predicted) == expected
        assert actual == predicted, (sizes, ticks, len(actual), len(predicted),
                                      sorted(actual - predicted)[:3], sorted(predicted - actual)[:3])
        print('PASS', sizes, ticks, len(actual))
        count += 1
    print('ALL_EXACT_CASES_PASS:', count)

if __name__ == '__main__':
    run()
