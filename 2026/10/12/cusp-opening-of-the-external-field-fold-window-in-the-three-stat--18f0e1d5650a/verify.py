#!/usr/bin/env python3
from fractions import Fraction
import math

def exact_checks(k):
    assert k >= 2
    xc = Fraction(k + 1, k - 1)
    b0 = xc * xc
    theta2 = Fraction((k - 1) ** 2, k * k + 6 * k + 1)
    b_from_theta = (1 + theta2) / (2 * theta2)
    assert b_from_theta == b0

    A = Fraction((k - 1) ** 4, 4 * k * (k + 1) ** 2)
    B = -Fraction((k - 1) ** 4, 2 * k * k * (k + 1) ** 2)
    assert -2 * A / B == k

    ac = xc ** (-(k + 1))
    direct_ac = Fraction(1, 1) / xc * ((1 + xc) / (b0 + xc)) ** k
    assert ac == direct_ac
    return xc, b0, A, B, ac

def constants(k):
    N = k * k + 6 * k + 1
    theta_c = (k - 1) / math.sqrt(N)
    lambda_c = 2.0 * ((k + 1) / math.sqrt(N)) ** (k + 1)
    K = lambda_c * (N ** 2.25) / (3.0 * (k + 1) ** 2 * math.sqrt(k * (k - 1)))
    return theta_c, lambda_c, K

def fold_gap(k, theta):
    b = (1.0 + theta * theta) / (2.0 * theta * theta)
    b0 = ((k + 1) / (k - 1)) ** 2
    D = (b - 1.0) * (k - 1) ** 2 * (b - b0)
    if D <= 0.0:
        raise ValueError("theta must be below theta_c")
    root = math.sqrt(D)
    x1 = ((b - 1.0) * (k - 1) - 2.0 - root) / 2.0
    x2 = ((b - 1.0) * (k - 1) - 2.0 + root) / 2.0
    def a_of(x):
        return (1.0 / x) * ((1.0 + x) / (b + x)) ** k
    a1, a2 = a_of(x1), a_of(x2)
    assert a1 < a2
    lam1 = 2.0 * theta ** (k + 1) / a2
    lam2 = 2.0 * theta ** (k + 1) / a1
    return lam2 - lam1

for k in range(2, 101):
    exact_checks(k)

# Independent binary-tree specialization.
theta2, lambda2, K2 = constants(2)
assert abs(lambda2 - (54.0 * math.sqrt(17.0) / 289.0)) < 2e-15
assert abs(K2 - (math.sqrt(2.0) * 17.0 ** 0.75)) < 2e-14

worst = 0.0
details = []
for k in (2, 3, 4, 10, 25, 50):
    theta_c, lambda_c, K = constants(k)
    delta = 1e-6
    gap = fold_gap(k, theta_c - delta)
    ratio = gap / (K * delta ** 1.5)
    err = abs(ratio - 1.0)
    worst = max(worst, err)
    details.append((k, ratio))
assert worst < 5e-5

print("VERIFY_OK exact_k=2..100 asymptotic_cases=6 worst_relative=%.3e" % worst)
for k, ratio in details:
    print("k=%d ratio=%.12f" % (k, ratio))
