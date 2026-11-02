#!/usr/bin/env python3
"""Numerical/exact finite checks for harmonic-weight quorum asymptotics.

This program checks finite identities and convergence diagnostics.  It does not
establish the asymptotic theorem, whose proof is analytical.
"""
from fractions import Fraction
from itertools import product
from math import exp, expm1, sqrt

GAMMA = 0.577215664901532860606512090082402431
assertions = 0


def insist(predicate, message):
    global assertions
    if not predicate:
        raise AssertionError(message)
    assertions += 1


# Independently enumerate small weighted Bernoulli populations.
for n in range(2, 8):
    weights = [Fraction(1, k) for k in range(1, n + 1)]
    q = [Fraction(2 * k + 1, 3 * k + 4) for k in range(1, n + 1)]
    mean = sum((weights[j] * q[j] for j in range(n)), Fraction(0))
    var = sum((weights[j] ** 2 * q[j] * (1 - q[j]) for j in range(n)), Fraction(0))
    enum_mean = Fraction(0)
    enum_second = Fraction(0)
    mass = Fraction(0)
    for bits in product((0, 1), repeat=n):
        prob = Fraction(1)
        for j, bit in enumerate(bits):
            prob *= q[j] if bit else 1 - q[j]
        score = sum((weights[j] for j in range(n) if bits[j]), Fraction(0))
        mass += prob
        enum_mean += prob * score
        enum_second += prob * score ** 2
    insist(mass == 1, 'probability mass')
    insist(mean == enum_mean, 'independent mean')
    insist(var == enum_second - enum_mean ** 2, 'independent variance')


def stat(n, theta):
    inv = [1.0 / i for i in range(1, n + 1)]
    H = sum(inv)

    def s(A):
        return sum((-expm1(-A * r)) * r for r in inv)

    c = exp((theta - 2.0) * GAMMA)
    z = c * n ** theta
    lo = max(0.0, z / 3)
    hi = z * 3
    insist(s(lo) < theta * H < s(hi), 'root bracket')
    for _ in range(44):
        mid = (lo + hi) / 2
        if s(mid) < theta * H:
            lo = mid
        else:
            hi = mid
    A = (lo + hi) / 2
    insist(abs(s(A) - theta * H) < 3e-10, 'root residual')
    derivative = sum(exp(-A * r) * r * r for r in inv)
    variance = sum(exp(-A * r) * (-expm1(-A * r)) * r * r for r in inv)
    insist(0 < variance < derivative, 'probability variance bounds')
    insist(0 < A * variance < 1, 'scaled variance range')
    insist(0 < A * derivative < 2, 'scaled derivative range')
    delta = (A - z) / (c * c * n ** (2 * theta - 1))
    insist(0 < delta < 2.0, 'positive finite population shift')
    return A, z, c, delta, A * variance, A * derivative, (A - z) / n ** (theta / 2)


for n in (3000, 30000, 100000):
    for theta in (0.5, 2 / 3, 0.75):
        A, z, c, ratio, Av, Ad, shift = stat(n, theta)
        print('n=%d theta=%.6f root=%.8f c=%.8f shift=%.7f correction_ratio=%.7f A_variance=%.7f A_derivative=%.7f' %
              (n, theta, A, c, shift, ratio, Av, Ad))

print('PASS %d finite/computational assertions' % assertions)
