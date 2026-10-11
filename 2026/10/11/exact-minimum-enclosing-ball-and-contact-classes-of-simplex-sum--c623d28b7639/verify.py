"""Exact rational checks for the minimum enclosing ball of a simplex-sum stellohedron.

Run with Python 3 (standard library only): python verify.py
This finite verification complements, but does not replace, the all-dimension proof.
"""
from fractions import Fraction
from itertools import permutations
from random import Random


def parameters(k):
    assert k >= 1
    N = (1 << k) - 1
    leaf = Fraction(2 * N + 1, 3 * (k + 1))
    hub = N - k * leaf
    radius2 = Fraction(k * (2 * N + 1) ** 2, 9 * (k + 1))
    return N, hub, leaf, radius2


def canonical(k, r):
    return (2 ** (k - r) - 1,) + tuple(2 ** (k - j) for j in range(1, r + 1)) + (0,) * (k - r)


def norm2(v, hub, leaf):
    return (v[0] - hub) ** 2 + sum((z - leaf) ** 2 for z in v[1:])


def simplex_sum_support_vertex(k, heights):
    v = [0] * (k + 1)
    for mask in range(1, 1 << k):
        indices = [0] + [j + 1 for j in range(k) if mask & (1 << j)]
        best = max(indices, key=lambda j: heights[j])
        v[best] += 1
    return tuple(v)


rank_cases = 0
for k in range(1, 81):
    N, hub, leaf, radius2 = parameters(k)
    assert N > hub > 0 and leaf > 0 and hub + k * leaf == N
    assert hub - leaf == Fraction(N - 1, 3)
    for r in range(k + 1):
        v = canonical(k, r)
        a = 1 << (k - r)
        clearance = Fraction(2 * ((1 << k) - a) * (a - 1), 3)
        assert norm2(v, hub, leaf) + clearance == radius2
        assert (clearance == 0) == (r in (0, k))
        rank_cases += 1
    alpha = hub / N
    assert 0 < alpha < 1
    # Contact barycenter: alpha*(N,0,...,0) + (1-alpha)*average(all k! rank-k vertices).
    assert alpha * N == hub
    assert (1 - alpha) * Fraction(N, k) == leaf

vertex_cases = 0
contact_vertices = 0
for k in range(1, 9):
    N, hub, leaf, radius2 = parameters(k)
    seen = set()
    for r in range(k + 1):
        for order in permutations(range(k), r):
            v = [0] * (k + 1)
            v[0] = 2 ** (k-r) - 1
            for j, index in enumerate(order, 1):
                v[index + 1] = 2 ** (k-j)
            v = tuple(v)
            assert v not in seen
            seen.add(v)
            z = norm2(v, hub, leaf)
            assert z <= radius2
            assert (z == radius2) == (r == 0 or r == k)
            vertex_cases += 1
            contact_vertices += int(z == radius2)
    assert len(seen) == sum(__import__('math').factorial(k)//__import__('math').factorial(k-r) for r in range(k+1))

rng = Random(2026)
support_cases = 0
for k in range(1, 7):
    for _ in range(100):
        heights = list(rng.sample(range(-30000, 30001), k+1))
        v = simplex_sum_support_vertex(k, heights)
        leaves = sorted(range(1, k+1), key=lambda i: -heights[i])
        r = sum(heights[i] > heights[0] for i in leaves)
        expected = [0] * (k+1)
        expected[0] = 2 ** (k-r) - 1
        for j, i in enumerate(leaves[:r], 1):
            expected[i] = 2 ** (k-j)
        assert v == tuple(expected)
        support_cases += 1

print('PASS: 80 all-rank algebraic cases sets; {} exact rank identities'.format(rank_cases))
print('PASS: {} explicit vertices; {} contacts'.format(vertex_cases,contact_vertices))
print('PASS: {} independent simplex-sum support computations'.format(support_cases))
print('Limit: only the written algebraic proof establishes every k >= 1.')
