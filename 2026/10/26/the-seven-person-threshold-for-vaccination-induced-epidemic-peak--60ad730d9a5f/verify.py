#!/usr/bin/env python3
"""Exact finite checks for a seven-vertex static-network SIR peak example."""
from collections import Counter
from math import comb
import random

N = 7
SEED = 0
VACCINATED = 2
# Vertices: seed=0, two first-generation contacts=1,2,
# second-generation intermediate=3, three eventual targets=4,5,6.
EDGES = ((0, 1), (0, 2), (1, 3), (2, 4), (3, 4), (3, 5), (3, 6))


def distances(n, edges, vaccinated=None):
    """Directed shortest-path lengths, with an optional deleted vertex."""
    d = [-1] * n
    d[SEED] = 0
    queue = [SEED]
    neighbours = [[] for _ in range(n)]
    for a, b in edges:
        if a != vaccinated and b != vaccinated:
            neighbours[a].append(b)
    for a in queue:
        for b in neighbours[a]:
            if d[b] == -1:
                d[b] = d[a] + 1
                queue.append(b)
    return d


def peak(n, edges, vaccinated=None):
    d = distances(n, edges, vaccinated)
    return max(d.count(t) for t in range(max(d) + 1))


def seven_vertex_census():
    assert peak(N, EDGES) == 2
    assert peak(N, EDGES, VACCINATED) == 3
    expected = {
        0: {-1: 0, 0: 1, 1: 0},
        1: {-1: 0, 0: 7, 1: 0},
        2: {-1: 1, 0: 20, 1: 0},
        3: {-1: 5, 0: 30, 1: 0},
        4: {-1: 10, 0: 25, 1: 0},
        5: {-1: 7, 0: 14, 1: 0},
        6: {-1: 1, 0: 6, 1: 0},
        7: {-1: 0, 0: 0, 1: 1},
    }
    counts = Counter()
    for mask in range(1 << len(EDGES)):
        active = [edge for i, edge in enumerate(EDGES) if mask & (1 << i)]
        k = mask.bit_count()
        delta = peak(N, active, VACCINATED) - peak(N, active)
        counts[(k, delta)] += 1
    for k, row in expected.items():
        for delta, count in row.items():
            assert counts[(k, delta)] == count, (k, delta)
        assert sum(row.values()) == comb(7, k)
    assert sum(counts.values()) == 128
    # Expand sum_{k,delta} count*delta*p^k*(1-p)^(7-k).
    coeff = [0] * 8
    for (k, delta), count in counts.items():
        for j in range(7 - k + 1):
            coeff[k + j] += count * delta * (-1) ** j * comb(7 - k, j)
    # p^2 * (p^5 - 2*p^4 + 3*p^3 - 1)
    assert coeff == [0, 0, -1, 0, 0, 3, -2, 1], coeff
    def poly(p):
        return p**5 - 2*p**4 + 3*p**3 - 1
    a, b = 0.0, 1.0
    for _ in range(70):
        m = (a + b) / 2
        if poly(m) > 0:
            b = m
        else:
            a = m
    assert 0.78783366030 < (a + b) / 2 < 0.78783366031
    print('seven-vertex census: 128/128, polynomial coefficients:', coeff)
    print('unique-threshold numerical bracket:', a, b)


def stress_test_small_graphs():
    rng = random.Random(20261023)
    checks = 0
    for n in range(2, 7):
        possible = [(a, b) for a in range(n) for b in range(n) if a != b]
        for _ in range(4000):
            edges = [e for e in possible if rng.randrange(2)]
            v = rng.randrange(1, n)
            assert peak(n, edges, v) <= peak(n, edges)
            checks += 1
    print('small directed graph checks:', checks)


if __name__ == '__main__':
    seven_vertex_census()
    stress_test_small_graphs()
    print('VERIFY_OK')
