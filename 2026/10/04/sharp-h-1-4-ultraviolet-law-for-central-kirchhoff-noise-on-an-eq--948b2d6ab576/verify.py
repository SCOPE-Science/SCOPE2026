#!/usr/bin/env python3
import math


def truncated_energy(N, ell, t, alpha, M):
    # The zero mode has eigenvalue zero and center value 1/sqrt(N*ell).
    total = t / (N * ell)
    for n in range(1, M + 1):
        lam = (n * math.pi / ell) ** 2
        total += ((1.0 + lam) ** (2.0 * alpha) / (N * ell * lam)) * (1.0 - math.exp(-2.0 * lam * t))
    return total


def check_critical(N, ell, t):
    c = 1.0 / (N * math.pi)
    m1, m2 = 20000, 40000
    s1 = truncated_energy(N, ell, t, 0.25, m1)
    s2 = truncated_energy(N, ell, t, 0.25, m2)
    slope = (s2 - s1) / math.log(m2 / m1)
    assert abs(slope - c) <= 2.0e-5 * max(1.0, c)
    r1 = s1 - c * math.log(m1)
    r2 = s2 - c * math.log(m2)
    assert abs(r2 - r1) < 2.0e-5


def check_supercritical(N, ell, t, alpha):
    assert alpha > 0.25
    exponent = 4.0 * alpha - 1.0
    coeff = (math.pi ** (4.0 * alpha - 2.0) * ell ** (1.0 - 4.0 * alpha)) / (N * exponent)
    m = 60000
    ratio = truncated_energy(N, ell, t, alpha, m) / (m ** exponent)
    assert abs(ratio / coeff - 1.0) < 0.03


def check_subcritical(N, ell, t, alpha):
    assert alpha < 0.25
    a = truncated_energy(N, ell, t, alpha, 20000)
    b = truncated_energy(N, ell, t, alpha, 40000)
    assert 0.0 <= b - a < 3.0e-3


for args in [(3, 1.7, 0.4), (7, 0.8, 0.05)]:
    check_critical(*args)
check_supercritical(5, 1.3, 0.2, 0.40)
check_subcritical(4, 0.9, 0.3, 0.10)
print('VERIFY_OK')
