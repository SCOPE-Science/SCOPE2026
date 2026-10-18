#!/usr/bin/env python3
"""Reproduce finite coefficient, commutativity, and counting tests for the stated spherical shifts.
The infinite-dimensional statements require the analytic argument in RESULT.md.
"""
from fractions import Fraction
from math import comb, factorial, gamma
from itertools import product


def grades(d, k):
    if d == 1:
        yield (k,)
    else:
        for a in range(k + 1):
            for tail in grades(d - 1, k - a):
                yield (a,) + tail


def coeffs(d, k, profile):
    D_k = comb(k + d - 1, d - 1)
    D_next = comb(k + d, d - 1)
    b_k = profile(k)
    u2 = b_k / D_next
    b_prev = profile(k - 1) if k > 0 else Fraction(0)
    for alpha in grades(d, k):
        outgoing = sum(u2 * Fraction(alpha[j] + 1, k + 1) for j in range(d))
        incoming = Fraction(0)
        if k:
            u_prev2 = b_prev / D_k
            incoming = sum(u_prev2 * Fraction(alpha[j], k) for j in range(d))
        assert outgoing - incoming == (b_k - b_prev) / D_k
        assert outgoing == b_k / D_k
        assert incoming == b_prev / D_k
        # Commuting squares: equality of the squared positive path weights.
        for j in range(d):
            for ell in range(j + 1, d):
                alpha_j = alpha[j]
                alpha_ell = alpha[ell]
                u_next2 = profile(k + 1) / comb(k + d + 1, d - 1)
                left = (u2 * Fraction(alpha_j + 1, k + 1)
                        * u_next2 * Fraction(alpha_ell + 1, k + 2))
                right = (u2 * Fraction(alpha_ell + 1, k + 1)
                         * u_next2 * Fraction(alpha_j + 1, k + 2))
                assert left == right


def bounded_profile(k):
    return Fraction(2) - Fraction(1, k + 1)


def linear_profile(k):
    return Fraction(k + 1)


def constant_profile(k):
    return Fraction(3)


checks = 0
for d in (2, 3, 4):
    for fn in (bounded_profile, linear_profile, constant_profile):
        for k in range(10):
            coeffs(d, k, fn)
            checks += 1

# Trace of the sum of self-commutators over grades <= N telescopes to b_N.
for d in (2, 3, 4):
    for fn in (bounded_profile, linear_profile, constant_profile):
        for N in range(15):
            grade_trace = sum(
                (comb(k + d - 1, d - 1)
                 * ((fn(k) - (fn(k - 1) if k else 0)) / comb(k + d - 1, d - 1)))
                for k in range(N + 1)
            )
            assert grade_trace == fn(N)
            checks += 1

# For b_k=d and dimensions 2, 3, count exact coordinate singular values.
for d, M_values, tolerance in ((2, (10, 20, 30), .002),
                               (3, (10, 20, 30), .006)):
    q = 2 * d / (d - 1)
    gamma_moment = gamma(1 + d/(d-1)) * gamma(d) / gamma(d + d/(d-1))
    predicted = (d * factorial(d-1))**(d/(d-1)) * gamma_moment / factorial(d)
    for M in M_values:
        count = 0
        k = 0
        while True:
            D_next = comb(k + d, d - 1)
            if d * M*M <= D_next:
                break
            for alpha_j in range(k + 1):
                if d * M*M*(alpha_j + 1) > D_next * (k + 1):
                    multiplicity = comb(k-alpha_j + d-2, d-2)
                    count += multiplicity
            k += 1
        observed = count / M**q
        assert abs(observed/predicted - 1) < tolerance, (d, M, observed, predicted)
        checks += 1

print(f"SPHERICAL_SUM_DEFECT_SPECTRAL_FINITE_CHECKS_OK assertionsets={checks}")
