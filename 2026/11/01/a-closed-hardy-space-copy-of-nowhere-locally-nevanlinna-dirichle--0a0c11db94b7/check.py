#!/usr/bin/env python3
"""Finite consistency checks for an odd-index Dirichlet block and a prime-separated norm.

No numerical check here proves asymptotic or infinite-dimensional assertions.
"""
import math
import numpy as np

def odd_formula(X, s):
    z = np.arange(1, X + 1, dtype=float)
    all_sum = np.sum(z ** (-s))
    h = np.arange(1, X // 2 + 1, dtype=float)
    return all_sum - 2 ** (-s) * np.sum(h ** (-s))

# Exact combinatorial parity identity (subject to floating-point precision).
for X in [5, 18, 137, 1024, 4097]:
    for t in [0.0, 0.3, 1.0, 2.0]:
        s = 0.5 + 1 / math.log(max(X, 4)) + 1j * t
        odds = np.arange(1, X + 1, 2, dtype=float)
        direct = np.sum(odds ** (-s))
        assert abs(direct - odd_formula(X, s)) < 1e-9

# Euler summation error is bounded at these sample points; no claim of
# universal T or X follows from these finitely many checks.
for X in [10000, 20000, 60000]:
    for t in [0, 0.5, 1, 2, 4]:
        s = 0.5 + 1 / math.log(X) + 1j * t
        B = odd_formula(X, s)
        leading = X ** (1 - s) / (2 * (1 - s))
        assert abs(B - leading) < 4.0

# The finite-variable factorization is a direct consequence of products
# on independent probability spaces, here sampled numerically.
angles = np.linspace(0, 2 * np.pi, 64, endpoint=False)
z = np.exp(1j * angles)
A = 1 + 0.7 * z + 0.2 * z**2  # a disk/prime-2 factor
B = 0.3 + 1.1 * z - 0.4 * z**3  # an odd-prime-coordinate factor
for p in [1.5, 1.75, 1.95]:
    lhs = np.mean(np.abs(B[:, None] * A[None, :])**p)
    rhs = np.mean(np.abs(B)**p) * np.mean(np.abs(A)**p)
    assert abs(lhs - rhs) < 1e-12
print('CHECK_OK: odd block identity, sample Euler remainder, prime-coordinate product')
