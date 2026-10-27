#!/usr/bin/env python3
"""Reproducible finite checks for annular Gaussian concentration eigenvalues.

This checker tests exact coefficient identities and selected numerical instances.
The global spectral staircase and asymptotics require the accompanying proof.
"""
from fractions import Fraction
from math import comb, exp, factorial


def H(k, N, x):
    return sum(x ** r / factorial(r) for r in range(k + 1, k + N + 1))


def Hprime(k, N, x):
    return sum(x ** (r - 1) / factorial(r - 1) for r in range(k + 1, k + N + 1))


def crossing_polynomial(k, N, s, a):
    return exp(s) * H(k, N, a) - H(k, N, a + s)


def root(k, N, s):
    lo, hi = 0.0, max(2.0, k + N + s)
    assert crossing_polynomial(k, N, s, lo) < 0.0
    while crossing_polynomial(k, N, s, hi) <= 0.0:
        hi *= 2.0
    for _ in range(90):
        mid = (lo + hi) / 2
        if crossing_polynomial(k, N, s, mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def E(j, x):
    return sum(x ** r / factorial(r) for r in range(j + 1))


def eigenvalue(j, a, s):
    return exp(-a) * E(j, a) - exp(-a - s) * E(j, a + s)


def check_coefficients():
    count = 0
    for s in (Fraction(1, 3), Fraction(1), Fraction(5, 2)):
        for k in range(7):
            for N in range(1, 6):
                # Coefficients of H(a+s): exact binomial expansion.
                for m in range(k + N + 1):
                    lhs = sum(Fraction(comb(r, m), factorial(r)) * s ** (r - m)
                              for r in range(max(k + 1, m), k + N + 1))
                    rhs = sum(s ** (r - m) / (factorial(m) * factorial(r - m))
                              for r in range(max(k + 1, m), k + N + 1))
                    assert lhs == rhs
                    if m >= k + 1:
                        partial = sum(s ** r / factorial(r)
                                      for r in range(k + N - m + 1))
                        assert rhs == partial / factorial(m)
                    else:
                        assert rhs > 0  # The P-polynomial coefficient is negative.
                    count += 1
    return count


def check_spectra():
    count = 0
    for s in (0.5, 1.0, 3.0, 7.0):
        for N in (1, 2, 3, 5):
            thresholds = [root(k, N, s) for k in range(7)]
            assert all(0 < thresholds[k] < thresholds[k + 1]
                       for k in range(6))
            for k in range(7):
                a = thresholds[k]
                # The crossing polynomial has positive derivative at its root.
                derivative = exp(s) * Hprime(k, N, a) - Hprime(k, N, a + s)
                assert derivative > 0
                # At the crossing, the two endpoint modes agree.
                assert abs(eigenvalue(k, a, s) - eigenvalue(k + N, a, s)) < 3e-12
                count += 1
            for k in range(7):
                a = thresholds[0] / 2 if k == 0 else (thresholds[k - 1] + thresholds[k]) / 2
                vals = [eigenvalue(j, a, s) for j in range(50)]
                winners = set(sorted(range(50), key=lambda j: vals[j], reverse=True)[:N])
                assert winners == set(range(k, k + N)), (s, N, k, a, winners)
                count += 1
    return count


def check_asymptotics():
    count = 0
    for s in (0.5, 2.0, 5.0):
        for N in (1, 3, 5):
            k = 100
            a = root(k, N, s)
            predicted = (k + (N + 1) / 2 - s / 2
                         + (s * s / 12 - (N * N - 1) / 24) / k)
            assert abs(a - predicted) < 0.003, (s, N, a, predicted)
            count += 1
    for k in (0, 1, 2):
        for N in (1, 2, 4):
            s = 40.0
            a = root(k, N, s)
            predicted = ((factorial(k + 1) / factorial(k + N))
                         ** (1 / (k + 1)) * s ** ((k + N) / (k + 1))
                         * exp(-s / (k + 1)))
            # Extreme underflow/cancellation is avoided by the polynomial root.
            assert abs(a / predicted - 1) < 0.3, (k, N, a, predicted)
            count += 1
    return count


if __name__ == '__main__':
    n0 = check_coefficients()
    n1 = check_spectra()
    n2 = check_asymptotics()
    print(f'CHECK_OK: {n0} exact coefficients, {n1} spectral tests, {n2} asymptotic tests')
