#!/usr/bin/env python3
"""Exact arithmetic checks for three-term cubic LCM quotient and high 7-adic overlap."""
from math import gcd, lcm


def quotient(m, n):
    a, b, c = ((n+j)**3 + 2*m for j in range(3))
    return a*b*c // lcm(a, b, c)


def expression(m, n):
    u, v = 108*m*m+1, 27*m*m+16
    return ((2 if n % 2 == 0 else 1) * gcd(2*n+6*m+1, u)
            * gcd(2*n+6*m+3, u) * gcd(4*n+4+3*m, v))


def factorization(n):
    d, factors = 2, {}
    while d*d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def valuation(x, p):
    result = 0
    while x % p == 0:
        result += 1
        x //= p
    return result


def run():
    checks = 0
    for m in range(1, 100, 2):
        u, v = 108*m*m+1, 27*m*m+16
        assert gcd(u, v) == (7 if m % 7 in (3, 4) else 1)
        for n in range(180):
            assert quotient(m, n) == expression(m, n), (m, n)
            checks += 1
    print('PASS direct arithmetic comparisons:', checks)
    for m in (1, 3, 5, 7, 9):
        u, v = 108*m*m+1, 27*m*m+16
        period = 2*lcm(u, v)
        for p, e in factorization(period).items():
            q = p**e
            vals = [valuation(expression(m, n), p) for n in range(q)]
            assert any(vals[i] != vals[(i+1) % q] for i in range(q))
            if e > 1:
                smaller = q//p
                assert any(vals[i] != vals[(i+smaller) % q] for i in range(q))
        print('PASS local periods: m=', m, ', least period=', period, sep='')

    # Regression for a tempting but false shortcut: when 7 | gcd(U,V),
    # both moduli need not have 7-adic exponent one.
    expected = {11: (1, 2), 17: (4, 1), 81: (2, 1), 87: (1, 2)}
    for m, pair in expected.items():
        u, v = 108*m*m+1, 27*m*m+16
        e, d = valuation(u, 7), valuation(v, 7)
        assert (e, d) == pair and gcd(u, v) == 7
        q = 7**max(e, d)
        vals = [valuation(expression(m, n), 7) for n in range(q)]
        shift = q//7
        assert any(vals[i] != vals[(i+shift) % q] for i in range(q))
        for n in range(700):
            assert quotient(m, n) == expression(m, n), (m, n)
        print('PASS high-7-power overlap: m=', m, ', exponents=', pair,
              ', forced local period=', q, sep='')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
