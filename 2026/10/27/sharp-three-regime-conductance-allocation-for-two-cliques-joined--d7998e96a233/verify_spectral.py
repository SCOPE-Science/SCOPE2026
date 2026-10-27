#!/usr/bin/env python3
"""Numerical checks of the partial-matching clique allocation formulas.

Requires numpy. This is not a substitute for the all-parameter proof.
"""
import math
import numpy as np


def optimum(k, m):
    assert k >= 2 and m >= 1
    n = k + m
    threshold = 1 + math.sqrt(k / (2 * (k + 1)))
    r = k / m
    t = 1.5 if r <= 1.5 else r if r < threshold else threshold
    a = max(0.0, 1 - m * t / k) / k
    b = (n * t - k) / (2 * k * (t - 1))
    c = t / k
    d = 0.0
    cost = k * (k - 1) * a + k * b + 2 * k * m * c + m * (m - 1) * d
    scalar = n / 2 + 2 * m * t + m / (2 * (t - 1)) + (k - 1) * max(0.0, 1 - m * t / k)
    return a, b, c, d, cost, scalar, t


def laplacian(k, m, a, b, c, d):
    n = k + m
    matrix = np.zeros((2 * n, 2 * n))

    def edge(i, j, w):
        matrix[i, i] += w
        matrix[j, j] += w
        matrix[i, j] -= w
        matrix[j, i] -= w

    for side in (0, 1):
        offset = side * n
        for i in range(n):
            for j in range(i + 1, n):
                weight = a if j < k else d if i >= k else c
                edge(offset + i, offset + j, weight)
    for i in range(k):
        edge(i, n + i, b)
    return matrix


def run():
    total = 0
    for k in range(2, 14):
        for m in range(1, 14):
            a, b, c, d, budget, scalar, t = optimum(k, m)
            L = laplacian(k, m, a, b, c, d)
            vals = np.linalg.eigvalsh(L)
            assert abs(vals[0]) < 1e-10, (k, m, vals[0])
            assert abs(vals[1] - 1) < 1e-9, (k, m, vals[1])
            assert abs(budget - scalar) < 1e-9, (k, m, budget, scalar)
            assert abs(np.trace(L) / 2 - budget) < 1e-9
            for ds in (-0.1, -0.01, 0.01, 0.1):
                z = t + ds
                if z <= 1:
                    continue
                fz = (k + m) / 2 + 2 * m * z + m / (2 * (z - 1)) + (k - 1) * max(0.0, 1 - m * z / k)
                assert fz + 1e-10 >= scalar, (k, m, z, fz, scalar)
            total += 1
    print(f'REPLAY_OK: {total} graph-size pairs; spectral gap, cost, trace, scalar perturbations')


if __name__ == '__main__':
    run()
