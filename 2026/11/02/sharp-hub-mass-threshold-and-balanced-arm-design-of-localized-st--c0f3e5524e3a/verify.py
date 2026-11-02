#!/usr/bin/env python3
"""Independent finite-matrix checks of star-chain band-edge design formulas.

Not a proof for arbitrary arm lengths or central mass.
Run: python3 verify.py
Requires numpy and scipy.
"""
import itertools
from fractions import Fraction
import math
import numpy as np
from scipy.linalg import eigh


def matrix(arms, mu):
    n = 1 + sum(arms)
    L = np.zeros((n, n))
    masses = np.ones(n)
    masses[0] = mu
    j = 1
    for arm in arms:
        prev = 0
        for _ in range(arm):
            L[prev, prev] += 1
            L[j, j] += 1
            L[prev, j] -= 1
            L[j, prev] -= 1
            prev = j
            j += 1
    return L, np.diag(masses)


def threshold(arms):
    return sum((Fraction(L, 2 * L + 1) for L in arms), Fraction(0))


def balanced(q, total):
    a, r = divmod(total, q)
    return (a,) * (q - r) + (a + 1,) * r


def extreme(q, total):
    return (total - q + 1,) + (1,) * (q - 1)


def tail_factor(length, eig):
    r = (eig - 2 - math.sqrt(eig * (eig - 4))) / 2
    return (r - r**(2*length)) / (1 - r**(2*length + 1))


count = {'band_edge': 0, 'one_above': 0, 'balance': 0, 'root': 0, 'limit': 0}
for q in range(3, 7):
    for total in range(q, q + 9):
        partitions = [t for t in itertools.combinations_with_replacement(range(1, total - q + 2), q) if sum(t) == total]
        ths = [threshold(p) for p in partitions]
        tb = threshold(balanced(q, total))
        te = threshold(extreme(q, total))
        assert min(ths) == te and max(ths) == tb
        assert sum(t == te for t in ths) >= 1
        assert sum(t == tb for t in ths) >= 1
        count['balance'] += 1
        for p in partitions:
            t = float(threshold(p))
            mu_list = [0.31, max(0.1, t - 0.04), t, t + 0.04, 1.3, q / 2 + 0.1]
            for mu in mu_list:
                L, M = matrix(p, mu)
                vals = eigh(L, M, eigvals_only=True)
                num = int(np.sum(vals > 4 + 1.e-8))
                expected = int(mu < t - 1.e-9)
                assert num == expected, (p, mu, vals, expected)
                assert num <= 1
                count['one_above'] += 1
                if abs(mu - t) < 1.e-10:
                    assert abs(vals[-1] - 4) < 2e-9
                    count['band_edge'] += 1
                if num:
                    lam = float(vals[-1])
                    residual = q - mu * lam + sum(tail_factor(a, lam) for a in p)
                    assert abs(residual) < 1e-7, (p, mu, lam, residual)
                    count['root'] += 1
            # The top mode is ordered by balancing, on the above-band side.
            mu = min(0.35, t / 2)
            lam = float(eigh(*matrix(p, mu), eigvals_only=True)[-1])
            lam_bal = float(eigh(*matrix(balanced(q, total), mu), eigvals_only=True)[-1])
            lam_ext = float(eigh(*matrix(extreme(q, total), mu), eigvals_only=True)[-1])
            assert lam_ext - 1e-10 <= lam <= lam_bal + 1e-10
            count['balance'] += 1
for q, mu in [(3, 1.0), (4, 0.9), (5, 1.15), (7, 0.5)]:
    top_limit = q*q / (mu * (q - mu))
    prev = 4.0
    for arm in (2, 3, 5, 9, 15, 25):
        eig = float(eigh(*matrix((arm,) * q, mu), eigvals_only=True)[-1])
        assert eig >= prev - 1e-9
        assert eig < top_limit + 1e-9
        prev = eig
        count['limit'] += 1
    assert top_limit - prev < 0.05
print('PASS finite matrix diagnostics:', count)
