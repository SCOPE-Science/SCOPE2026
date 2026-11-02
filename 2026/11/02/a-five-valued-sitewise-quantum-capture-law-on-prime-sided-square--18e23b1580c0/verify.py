#!/usr/bin/env python3
"""Finite-grid checks for the exact corner-absorption site law.

Requires Python 3, NumPy and SciPy.  Runs in finite dimension only:
these comparisons support but do not establish the all-prime theorem.
"""
import math
from collections import defaultdict
import numpy as np
from scipy.linalg import expm

PRIMES = (3, 5, 7, 11, 13, 17, 19, 23)


def expected_probability(p, x, y):
    n = p - 1
    if x == y and x in (1, n):
        return 1.0
    if x == y:
        return 1.0 - 5.0 / (6 * p)
    if (x - y) % 2:
        return 0.5
    if abs(x - y) == 2:
        return 0.5 - 5.0 / (6 * p)
    return 0.5 - 1.0 / p


def spectral_capture(p):
    n = p - 1
    indexes = np.arange(1, p)
    eig = 2 * np.cos(np.pi * indexes / p)
    sine = np.sqrt(2 / p) * np.sin(np.pi * np.outer(indexes, indexes) / p)
    # Each column of basis is a Cartesian product of normalized path eigenmodes.
    basis = np.kron(sine, sine)
    trap_weights = basis[0, :]
    groups = defaultdict(list)
    for j in range(n):
        for k in range(n):
            groups[round(float(eig[j] + eig[k]), 10)].append((j, k))
    expected_groups = (n * n + 2) // 2
    assert len(groups) == expected_groups, (p, len(groups), expected_groups)
    capture = np.zeros(n * n)
    for members in groups.values():
        cols = np.array([j * n + k for j, k in members], dtype=int)
        a = trap_weights[cols]
        bright_projection = basis[:, cols] @ a
        capture += bright_projection * bright_projection / np.dot(a, a)
    expected = np.array([
        expected_probability(p, x, y)
        for x in range(1, p) for y in range(1, p)
    ])
    error = float(np.max(np.abs(capture - expected)))
    assert error < 1e-10, (p, error)
    assert abs(np.sum(capture) - expected_groups) < 1e-9
    # The five classes form a partition; some are empty for small p.
    class_counts = (
        2, n - 2, n * n // 2, 2 * (n - 2), n * n // 2 - 3 * n + 4
    )
    assert sum(class_counts) == n * n and min(class_counts) >= 0
    return error, len(groups), class_counts


def direct_loss_check(p, kappa, time):
    n = p - 1
    a = np.diag(np.ones(n - 1), 1)
    a = a + a.T
    h = (np.kron(a, np.eye(n)) + np.kron(np.eye(n), a)).astype(complex)
    h[0, 0] -= 1j * kappa
    # Each column is an independently initialized site state.
    propagator = expm(-1j * h * time)
    capture = 1.0 - np.sum(np.abs(propagator) ** 2, axis=0).real
    target = np.array([
        expected_probability(p, x, y)
        for x in range(1, p) for y in range(1, p)
    ])
    return float(np.max(np.abs(capture - target)))


def main():
    total_sites = 0
    max_error = 0.0
    for p in PRIMES:
        error, bright_dimension, counts = spectral_capture(p)
        total_sites += (p - 1) ** 2
        max_error = max(max_error, error)
        print(f"p={p}: {bright_dimension} active eigenvalues, "
              f"{(p-1)**2} site probabilities, max error {error:.3e}, "
              f"class sizes {counts}")
    print(f"SPECTRAL CHECKS PASS: {total_sites} site probabilities; "
          f"max discrepancy {max_error:.3e}")
    for p, kappa, time, bound in ((3, 0.75, 800, 1e-9),
                                  (5, 0.75, 800, 1e-9),
                                  (7, 0.75, 10000, 1e-8)):
        discrepancy = direct_loss_check(p, kappa, time)
        assert discrepancy < bound, (p, discrepancy, bound)
        print(f"NON-HERMITIAN CHECK PASS: p={p}, kappa={kappa}, "
              f"time={time}, max residual {discrepancy:.3e}")
    print("ALL CHECKS PASSED")


if __name__ == '__main__':
    main()
