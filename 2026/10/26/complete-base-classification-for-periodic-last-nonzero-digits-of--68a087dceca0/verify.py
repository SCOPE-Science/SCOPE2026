#!/usr/bin/env python3
"""Reproduce arithmetic witnesses for the last-nonzero-digit periodicity theorem.

The proof is symbolic; the finite tests below check witness construction,
modular evaluation, and selected positive-period cases independently.
"""
from math import gcd


def prime_divisors(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        ans.append(n)
    return ans


def last_nonzero(x, b):
    assert x > 0 and b >= 2
    while x % b == 0:
        x //= b
    return x % b


def build_witness(b, period):
    ps = prime_divisors(b)
    assert len(ps) >= 2 and period >= 1
    p, q = ps[:2]
    coprime_part = period
    for r in ps:
        while coprime_part % r == 0:
            coprime_part //= r
    supported_part = period // coprime_part
    k = 1
    n = b
    while n % supported_part:
        n *= b
        k += 1
    modulus = q * coprime_part
    assert gcd(modulus, p) == 1
    j = -pow(modulus, -1, p) % p
    u = 1 + modulus * j
    assert u > 1 and u % p == 0 and u % q == 1 and u % coprime_part == 1 % coprime_part
    m = n * u
    assert (m - n) % period == 0
    assert n == b**k and (n % b == 0)
    if n <= 150:
        assert last_nonzero(n**n, b) == 1
    a = pow(u, m, b)
    assert a % q != 0 and a % p == 0 and a != 1
    if m <= 500:
        assert last_nonzero(m**m, b) == a
    return k, u, n, m, a


def main():
    bases = [6, 10, 12, 14, 15, 18, 20, 21, 24, 30, 36, 40,
             45, 50, 60, 72, 75, 98, 100, 108, 120, 210]
    periods = [1, 2, 3, 4, 5, 6, 7, 11, 12, 18, 20, 36, 60, 72, 100, 840]
    w = 0
    for b in bases:
        for t in periods:
            build_witness(b, t)
            w += 1
    direct = 0
    for b in [6, 10, 12, 18, 20, 30, 45]:
        for t in range(1, 21):
            _, _, n, m, a = build_witness(b, t)
            if m <= 500:
                assert last_nonzero(m**m, b) == a
                direct += 1
    period_checks = 0
    for b in (2, 4, 16, 256):
        for n in range(1, 129):
            assert last_nonzero(n**n, b) == last_nonzero((n+b)**(n+b), b)
            period_checks += 1
    print('VERIFY_OK', 'mixed_prime_period_witnesses', w,
          'direct_witness_evaluations', direct,
          'prime_power_positive_period_cases', period_checks)


if __name__ == '__main__':
    main()
