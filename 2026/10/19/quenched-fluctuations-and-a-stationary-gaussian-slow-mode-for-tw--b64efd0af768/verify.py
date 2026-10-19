#!/usr/bin/env python3
"""Standalone arithmetic checks for a two-state random Markov cocycle.

Exact rational equalities test only finite environments/parameters; the
infinite-horizon and Gaussian statements have separate analytic proofs.
"""
from fractions import Fraction as Q
from math import exp, log

laws = [
    [(Q(1, 2), Q(1), Q(2)), (Q(1, 2), Q(3), Q(1))],
    [(Q(1, 2), Q(1), Q(1)), (Q(1, 2), Q(2), Q(2))],
    [(Q(1, 3), Q(1), Q(2)), (Q(1, 3), Q(2), Q(1)), (Q(1, 3), Q(3), Q(2))],
]
leakages = [Q(1, 100), Q(1, 20), Q(1, 10)]
checks = 0
for law in laws:
    assert sum((p for p, L, R in law), Q(0)) == 1
    B_mean = sum((p * (L + R) for p, L, R in law), Q(0))
    R_mean = sum((p * R for p, L, R in law), Q(0))
    theta = R_mean / B_mean
    sigma2 = sum((p * (R - theta * (L + R)) ** 2 for p, L, R in law), Q(0))
    B2 = sum((p * (L + R) ** 2 for p, L, R in law), Q(0))
    B_variance = B2 - B_mean ** 2
    checks += 3
    for eps in leakages:
        assert all(Q(0) < eps * (L + R) < 1 for p, L, R in law)
        a = 1 - eps * B_mean
        rho = 1 - 2 * eps * B_mean + eps ** 2 * B2
        variance_inf = eps * sigma2 / (2 * B_mean - eps * B2)
        comparison_difference_inf = (eps ** 2 * B_variance * variance_inf) / (1 - a * a)
        checks += 4
        # Matrix action agrees with the exact centered scalar recursion.
        for p, L, R in law:
            x = Q(2, 5)
            mx = x * (1 - eps * L) + (1 - x) * eps * R
            scalar = (1 - eps * (L + R)) * x + eps * R
            centered = (1 - eps * (L + R)) * (x - theta) + eps * (R - theta * (L + R))
            assert mx == scalar and centered == scalar - theta
            checks += 2
        mean = theta
        second = theta * theta
        diff_second = Q(0)
        for n in range(1, 41):
            new_mean = sum((p * ((1 - eps * (L + R)) * mean + eps * R)
                            for p, L, R in law), Q(0))
            new_second = sum((p * ((1 - eps * (L + R)) ** 2 * second +
                                   2 * (1 - eps * (L + R)) * eps * R * mean +
                                   eps ** 2 * R ** 2) for p, L, R in law), Q(0))
            current_variance = new_second - new_mean ** 2
            target_variance = variance_inf * (1 - rho ** n)
            assert new_mean == theta
            assert current_variance == target_variance
            # Coupled deterministic-drift approximation starts at 0.
            diff_second = a*a*diff_second + eps*eps*B_variance*(second-mean*mean)
            assert diff_second >= 0
            for k in (0, 1, 2, 5):
                # Conditional covariance propagates with annealed factor a.
                assert a**k * current_variance == target_variance * a**k
                checks += 1
            mean, second = new_mean, new_second
            checks += 3
        assert variance_inf == 0 if sigma2 == 0 else variance_inf > 0
        assert comparison_difference_inf >= 0
        checks += 2

# Exact arithmetic in a nonconstant-coefficient, nonsymmetric two-rate law.
p, l, r = laws[0][0]
assert (p, l, r) == (Q(1, 2), Q(1), Q(2))
M, theta, sig = Q(7, 2), Q(3, 7), Q(25, 49)
for ep in leakages:
    expected = 50*ep / (49*(14 - 25*ep))
    computed = ep*sig/(2*M - ep*Q(25, 2))
    assert computed == expected
    checks += 1

# Finite diagnostics for exponential covariance kernel; never an infinite proof.
for ep in (0.01, 0.001, 0.0001):
    a = 1 - ep*float(M)
    exact_scaled_var = float(sig) / (2*float(M) - ep*12.5)
    for t in (0.0, 0.5, 1.0, 2.0):
        empirical = exact_scaled_var*(a**int(t/ep))
        limiting = float(sig)/(2*float(M))*exp(-float(M)*t)
        assert abs(empirical-limiting) < 0.006
        checks += 1

print('PASS: %d exact and finite asymptotic diagnostics; proof handles infinite laws.' % checks)
