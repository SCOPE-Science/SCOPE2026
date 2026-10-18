#!/usr/bin/env python3
"""Exact finite-group tests of a positive injective convolution Lipschitz filter.

This is a finite-dimensional diagnostic, not a proof for infinite compact groups.
Only the Python standard library is required.
"""
from fractions import Fraction as F
from collections import deque
from itertools import permutations


def test_group(elements, identity, mul, generators, label):
    N = len(elements)
    ids = list(elements)
    inv = {}
    for g in ids:
        inv[g] = next(h for h in ids if mul(g, h) == identity and mul(h, g) == identity)
    distance = {identity: 0}
    queue = deque([identity])
    while queue:
        h = queue.popleft()
        for s in generators:
            y = mul(s, h)
            if y not in distance:
                distance[y] = distance[h] + 1
                queue.append(y)
    assert len(distance) == N

    # Right invariance of d(g,h)=word_length(g*h^{-1}).
    d = lambda g, h: distance[mul(g, inv[h])]
    for g in ids:
        for h in ids:
            for t in ids:
                assert d(mul(g, t), mul(h, t)) == d(g, h)

    def bump(radius):
        raw = {g: max(F(0), F(1) - F(distance[g], radius)) for g in ids}
        total = sum(raw.values())
        assert total > 0
        return {g: N * raw[g] / total for g in ids}

    us = [bump(r) for r in (2, 3, 1)]
    weights = (F(3, 7), F(2, 7), F(2, 7))

    def correlation(u, g):
        return sum(u[mul(g, b)] * u[b] for b in ids) / N

    k = {g: sum(w * correlation(u, g) for w, u in zip(weights, us)) for g in ids}
    assert all(k[g] >= 0 for g in ids)
    assert sum(k.values()) == N
    L = max(abs(k[g] - k[h]) / d(g, h) for g in ids for h in ids if g != h)

    def Q(f, g):
        return sum(k[a] * f[mul(inv[a], g)] for a in ids) / N

    # Matrix of the convolution operator; exact Gaussian elimination.
    A = [[k[mul(g, inv[h])] / N for h in ids] for g in ids]
    B = [row[:] for row in A]
    det = F(1)
    for j in range(N):
        pivot = next((i for i in range(j, N) if B[i][j] != 0), None)
        assert pivot is not None
        if pivot != j:
            B[j], B[pivot] = B[pivot], B[j]
            det = -det
        x = B[j][j]
        det *= x
        for i in range(j+1, N):
            scale = B[i][j] / x
            for t in range(j, N):
                B[i][t] -= scale * B[j][t]
    assert det != 0

    f = {g: F((3 * i + 2) % 11, 11) for i, g in enumerate(ids)}
    for g in ids:
        assert Q({h: F(1) for h in ids}, g) == 1
        assert Q(f, g) >= 0
        for h in ids:
            assert abs(Q(f, g) - Q(f, h)) <= L * max(abs(v) for v in f.values()) * d(g, h)
        for a in ids:
            # The shift is R_a f(h)=f(h*a).
            shifted = {h: f[mul(h, a)] for h in ids}
            assert Q(shifted, g) == Q(f, mul(g, a))
    print(label, 'order', N, 'determinant', det, 'kernel_Lip', L, 'PASS')


def cyclic(n):
    test_group(list(range(n)), 0, lambda a, b: (a + b) % n, [1, n-1], f'C{n}')


def symmetric_three():
    elems = list(permutations(range(3)))
    e = (0, 1, 2)
    def mul(a, b):
        return tuple(a[b[i]] for i in range(3))
    s = (1, 0, 2)
    t = (1, 2, 0)
    test_group(elems, e, mul, [s, t, (2, 0, 1)], 'S3')


if __name__ == '__main__':
    cyclic(5)
    symmetric_three()
    print('Exact finite group tests PASS; infinite-group proof is analytic.')
