#!/usr/bin/env python3
"""Exact integer certificates for sharp primitive-necklace root-ratio thresholds.
Run with Python 3 standard library; no external data or numerical tolerance.
"""
from fractions import Fraction as Q
from math import isqrt


def divisors(n):
    return [d for d in range(1, isqrt(n) + 1) if n % d == 0 for d in ([d] if d * d == n else [d, n // d])]


def mobius(n):
    v = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            v = -v
        p += 1
    return -v if n > 1 else v


def necklace(n, q):
    numerator = sum(mobius(d) * q ** (n // d) for d in divisors(n))
    assert numerator > 0 and numerator % n == 0
    return numerator // n


def delta_sign(n, q):
    # sign of g_{n+2}-2g_{n+1}+g_n; all exponents integral.
    a, b, c = (necklace(n + j, q) for j in range(3))
    lhs = a ** ((n + 1) * (n + 2)) * c ** (n * (n + 1))
    rhs = b ** (2 * n * (n + 2))
    return (lhs > rhs) - (lhs < rhs)


def run():
    thresholds = {2: 14, 3: 8, 4: 6, 5: 6, 6: 4, 7: 4, 8: 4}
    cases = 0
    for q, cutoff in thresholds.items():
        for n in range(cutoff, 23):
            assert delta_sign(n, q) == -1, (q, n)
            cases += 1
        assert delta_sign(cutoff - 1, q) == 1, (q, cutoff-1)
    assert cases == 115
    # Independent Möbius inversion check of all short finite-field counts.
    inversion_cases = 0
    for q in range(2, 9):
        for n in range(1, 25):
            assert sum(d * necklace(d, q) for d in divisors(n)) == q ** n
            inversion_cases += 1
    # Pure exact-rational certificates used by the analytic proof.
    assert 4**15 > 3**10 * 5**6
    assert 6**10 * 4**15 > 5**24
    assert Q(1, 1024) > Q(2, 2187)
    assert Q(3, 15625) > Q(29, 164864)
    assert Q(541, 216000) > Q(1, 400) > Q(41, 23205)
    assert Q(56, 81) + Q(263, 240) > Q(89, 50)
    assert Q(8, 9) ** 3 > Q(1, 3)
    assert Q(25, 26) ** 6 > Q(1, 2)
    print('VERIFY_OK finite_suffix=115 exact_witnesses=7 inversion_cases=%d' % inversion_cases)
    print('CHECK_OK analytic_rational_inequalities=8')


if __name__ == '__main__':
    run()
