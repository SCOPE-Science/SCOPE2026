#!/usr/bin/env python3
"""Exact rational checks for odd-prime denominator saturation.

No nonstandard packages or external data are required.
"""
from fractions import Fraction
from math import comb


def vp(n, p):
    assert n > 0 and p >= 3
    s = 0
    while n % p == 0:
        n //= p
        s += 1
    return s


def rational_mod_p(x, p):
    assert x.denominator % p != 0
    return x.numerator * pow(x.denominator, -1, p) % p


def main():
    cases = 0
    terms = 0
    # All shifts are tested for each of these finite prime-power rows.
    for p, m in [(3, 1), (3, 2), (3, 3), (3, 4),
                 (5, 1), (5, 2), (5, 3),
                 (7, 1), (7, 2),
                 (11, 1), (11, 2),
                 (13, 1), (13, 2)]:
        q = p ** m
        n = q - 1
        coeffs = [comb(n, k) for k in range(q)]
        assert all(c % p != 0 for c in coeffs)
        for r in range(1, q):
            total = sum((Fraction(coeffs[k] * k, k + r)
                         for k in range(1, q)), Fraction())
            s = vp(r, p)
            assert vp(total.denominator, p) - vp(total.numerator, p) == m - s
            normalized = total * p ** (m - s)
            expected = (-((q-r)//p**s) if (q-r) & 1 else (q-r)//p**s) % p
            assert rational_mod_p(normalized, p) == expected
            B = comb(n + r, r)
            assert B % total.denominator == 0
            assert vp(B, p) == vp(total.denominator, p)
            assert vp((q-r), p) == s
            cases += 1
            terms += n
    print("VERIFY_OK cases=%d direct_terms=%d prime_power_rows=13" % (cases, terms))


if __name__ == "__main__":
    main()
