#!/usr/bin/env python3
"""Exact small-index checks for a normalized divisor-power coefficient identity.

The infinite limiting distribution and its dimension are proved analytically;
these finite checks are consistency tests only.
"""
from fractions import Fraction


def divisors(n):
    out = []
    for d in range(1, n + 1):
        if n % d == 0:
            out.append(d)
    return out


def isprime(n):
    return n >= 2 and all(n % p for p in range(2, int(n**0.5) + 1))


def check(k, ell, cap):
    count = 0
    for n in range(1, cap + 1):
        divs = divisors(n)
        sig_k = sum(d**k for d in divs)
        sig_l = sum(d**ell for d in divs)
        c = (1 + n**ell)*sig_k - (1 + n**k)*sig_l
        w = sum(Fraction(1, d**k) - Fraction(1, d**ell) for d in divs)
        lhs = Fraction(c, n**(k+ell))
        correction = Fraction(sig_k - sig_l, n**(k+ell))
        assert lhs == w + correction, (k, ell, n, lhs, w, correction)
        assert c >= 0
        if n >= 2:
            assert (c == 0) == isprime(n)
        assert w >= 0
        count += 1
    return count


def verify_monotone(k, ell):
    # The proof treats every real x>=2; these exact rational checks
    # only test the prime-local monotonicity at sampled prime values.
    prime_vals = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    a = Fraction(1)
    b = Fraction(1)
    for p in [2, 5, 11]:
        a *= 1 + Fraction(1, p**k)
        b *= 1 + Fraction(1, p**ell)
    assert a >= b
    values = [a*(1+Fraction(1, p**k)) - b*(1+Fraction(1, p**ell)) for p in prime_vals]
    assert all(values[i] > values[i+1] for i in range(len(values)-1))
    return len(values)-1


def main():
    ncheck = 0
    mcheck = 0
    for k, ell in ((3, 5), (3, 7), (5, 7)):
        ncheck += check(k, ell, 1000)
        mcheck += verify_monotone(k, ell)
    print(f'VERIFY_OK exact_coefficients={ncheck} monotonic_pairs={mcheck}')

if __name__ == '__main__':
    main()
