#!/usr/bin/env python3
import math


def solve_y(kappa):
    target = 1.0 + math.log(kappa)
    def f(y):
        return y - math.log(y) - target
    lo = 1.0
    hi = max(2.0, target + math.log(max(target, 1.0)) + 5.0)
    while f(hi) <= 0.0:
        hi *= 2.0
    for _ in range(220):
        mid = (lo + hi) / 2.0
        if f(mid) > 0.0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0


def g(kappa, theta):
    return 1.0 - ((theta - 1.0) / (kappa * theta)) ** theta


def theta_small(q):
    return 1.0/q + 2.0/3.0 + q/12.0 - 2.0*q*q/135.0


def m_small(q):
    inv_e = math.exp(-1.0)
    return 1.0 - inv_e + inv_e*q - inv_e*q*q/6.0 - 5.0*inv_e*q**3/36.0


def close(a, b, tol):
    if abs(a-b) > tol * max(1.0, abs(a), abs(b)):
        raise AssertionError((a, b, tol))


for kappa in [1.000001, 1.0001, 1.001, 1.01, 1.1, 2.0, 10.0, 1.0e6]:
    y = solve_y(kappa)
    theta = y/(y-1.0)
    m = 1.0 - math.exp(-y)
    close(y - math.log(y), 1.0 + math.log(kappa), 2e-14)
    x = 1.0/y
    close(1.0 - 1.0/x - math.log(x/kappa), 0.0, 5e-13)
    close(g(kappa, theta), m, 4e-14)
    close(1.0-m, 1.0/(math.e*kappa*y), 4e-14)
    # The minimizer is strict; use multiplicative perturbations that stay above one.
    for factor in [0.999, 1.001]:
        t = 1.0 + (theta-1.0)*factor
        if not g(kappa, t) > m - 2e-14:
            raise AssertionError(('local_min', kappa, factor, g(kappa,t), m))

# Error-order stress tests in the critical regime.
for q in [0.02, 0.01, 0.005]:
    kappa = math.exp(q*q/2.0)
    y = solve_y(kappa)
    theta = y/(y-1.0)
    m = 1.0-math.exp(-y)
    rt = abs(theta-theta_small(q))/(q**3)
    rm = abs(m-m_small(q))/(q**4)
    if not (rt < 0.01 and rm < 0.2):
        raise AssertionError(('critical_remainder', q, rt, rm))

# Large-kappa scaling stress test.
for kappa in [1e3, 1e6, 1e12]:
    y = solve_y(kappa)
    L = math.log(kappa)
    scale = (1.0-(1.0-math.exp(-y))) * math.e * kappa * L
    # The ratio tends to one from below because L/y -> 1.
    if not (0.5 < scale < 1.01):
        raise AssertionError(('large_kappa', kappa, scale))

print('VERIFY_OK')
