"""Numerical cross-checks for the clique-with-two-vertex-tail spectral-gap formula.

Usage: python verify.py  (requires Python 3 and numpy).
Tests are finite illustrations, not a replacement for the all-parameter proof.
"""
import math
import numpy as np


def calculate(k):
    assert isinstance(k, int) and k >= 2
    n = k + 3
    d = 1.0 if k <= 3 else math.sqrt((k + 1) / (2 * k))
    t = 1 - d * d
    target = (k * (8 + 6 * d) + 6 + k * k * t) / n
    a = 3 * (d + 1) / (n * d)
    c = 0.0 if k <= 3 else (k * d - 3) / (k * n * d)
    b = (2 * k * d + 3 * (k + 1)) / n
    e = (k * d + 2 * k + 3) / n
    assert min(a, b, c, e) >= 0
    weights = np.zeros((n, n), dtype=float)
    for i in range(k):
        weights[i, k] = weights[k, i] = a
        for j in range(i + 1, k):
            weights[i, j] = weights[j, i] = c
    weights[k, k + 1] = weights[k + 1, k] = b
    weights[k + 1, k + 2] = weights[k + 2, k + 1] = e
    budget = np.triu(weights).sum()
    L = np.diag(weights.sum(axis=1)) - weights
    eigen = np.linalg.eigvalsh(L)

    M = np.diag([k * a, b, e]) - np.array([
        [3 * k, 2 * k, k],
        [2 * k, 2 * k + 2, k + 1],
        [k, k + 1, k + 2],
    ], dtype=float) / n
    expected_multiplicity = 1 if k == 2 else k
    return target, budget, eigen, M, d, expected_multiplicity


def main():
    for k in range(2, 61):
        target, budget, eigen, M, d, multiplicity = calculate(k)
        assert abs(target - budget) < 1e-10, (k, target, budget)
        assert abs(eigen[0]) < 1e-10, (k, eigen[0])
        assert abs(eigen[1] - 1) < 1e-10, (k, eigen[1])
        assert np.sum(np.abs(eigen - 1) < 1e-8) == multiplicity, k
        assert abs(np.linalg.norm(M @ np.array([d, 1, 1]))) < 1e-10, k
        assert np.linalg.eigvalsh(M).min() > -1e-10, k
        if k <= 3:
            assert abs(d - 1) < 1e-12
        else:
            assert d < 1
    print('PASS: 59 cases (k = 2..60); budget, gap, multiplicity, and PSD checks.')


if __name__ == '__main__':
    main()
