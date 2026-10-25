"""Exact finite checks for the cubic-moment geometry of minimal-state isotropic laws.

Run: python3 verify.py
The proof of the all-dimensional formulas is analytic; finite checks are not proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import sqrt, exp
import cmath

checks = 0


def ck(test, msg):
    global checks
    if not test:
        raise AssertionError(msg)
    checks += 1


def h2(p):
    return (1 - 2 * p) ** 2 / (p * (1 - p))


def tensor_energy(p):
    n = len(p)
    G = [[(1 / p[i] - 1) if i == j else F(-1) for j in range(n)] for i in range(n)]
    raw = sum((p[i] * p[j] * G[i][j] ** 3 for i in range(n) for j in range(n)), F(0))
    formula = sum((1 / x for x in p), F(0)) - 3 * n + 2
    ck(raw == formula, 'Gram-cubic moment contraction')
    ck(formula >= (n - 1) * (n - 2), 'isotropic baseline')
    chi = sum(((F(1, n) - x) ** 2 / x for x in p), F(0))
    ck(formula == (n - 1) * (n - 2) + n * n * chi, 'chi-square remainder')
    for i in range(n):
        ck(sum((p[j] * G[i][j] for j in range(n)), F(0)) == 0, 'mean and Gram')
    for i in range(n):
        for k in range(n):
            ck(sum((p[j] * G[i][j] * G[k][j] for j in range(n)), F(0)) == G[i][k], 'Gram isometry')
    return formula


def test(p):
    n = len(p)
    q = min(p)
    energy = tensor_energy(p)
    spec_sq = h2(q)
    for k in range(1, n):
        for I in combinations(range(n), k):
            w = sum((p[i] for i in I), F(0))
            ck(h2(w) <= spec_sq, 'all two-level stationary values bounded by minimum mass')
    for i in range(n):
        ck(h2(p[i]) <= spec_sq, 'atom directions bounded')
    low = 1 / q + F((n - 1) ** 2) / (1 - q) - 3 * n + 2
    high = (n - 1) / q + 1 / (1 - (n - 1) * q) - 3 * n + 2
    ck(low <= energy <= high, 'two-norm envelope')
    return energy


# Rational samples, including exact equality classes and nonuniform extremal profiles.
for d in range(2, 8):
    n = d + 1
    for t in range(0, 7):
        q = F(1, n + t)
        balanced = [q] + [(1 - q) / d] * d
        concentrated = [q] * d + [1 - d * q]
        e_bal = test(balanced)
        e_con = test(concentrated)
        low = 1 / q + F(d * d) / (1 - q) - 3 * n + 2
        high = d / q + 1 / (1 - d * q) - 3 * n + 2
        ck(e_bal == low, 'lower envelope attained')
        ck(e_con == high, 'upper envelope attained')
        if t:
            ck(high > low, 'strictly distinct nonuniform ends')
        for r in (F(1, 5), F(2, 5), F(3, 5), F(4, 5)):
            mixed = [(1 - r) * balanced[i] + r * concentrated[i] for i in range(n)]
            test(mixed)

# Verify fixed-mass spectral norm by a deterministic 2-D angular grid.
import math
for p in ((.1, .3, .6), (.2, .2, .6), (1/3, 1/3, 1/3), (.05, .24, .71)):
    import numpy as np
    v = np.array(p)
    w, _, _ = np.linalg.svd(np.eye(3) - np.outer(np.sqrt(v), np.sqrt(v)))
    atoms = (w[:, :2] / np.sqrt(v)[:, None])
    bound = abs(1 - 2 * v.min()) / math.sqrt(v.min() * (1 - v.min()))
    attained = 0.0
    for j in range(4096):
        angle = 2 * math.pi * j / 4096
        a = np.array([math.cos(angle), math.sin(angle)])
        got = abs(np.dot(v, (atoms @ a) ** 3))
        ck(got <= bound + 1e-10, 'two-dimensional spectral grid')
        attained = max(attained, got)
    ck(abs(bound - attained) < 2e-5, 'spectral maximizer approximated by dense grid')

# Check the normalized characteristic-function weak limit for two-point projections.
for d, q in ((2, .2), (3, .1), (5, 1/6)):
    mu3 = (1 - 2 * q) / sqrt(q * (1 - q))
    upper = sqrt((1 - q) / q)
    lower = -sqrt(q / (1 - q))
    tau = 1.0
    target = -exp(-tau / 2) * tau * mu3 / 6
    for N in (1000, 4000, 16000):
        h = tau / N
        cf = q * cmath.exp(1j * sqrt(h) * upper) + (1 - q) * cmath.exp(1j * sqrt(h) * lower)
        got = (cf ** N).imag / sqrt(h)
        ck(abs(got - target) < .03, 'weak Fourier coefficient')

print('PASS:', checks, 'exact-rational identities or deterministic numeric checks')
