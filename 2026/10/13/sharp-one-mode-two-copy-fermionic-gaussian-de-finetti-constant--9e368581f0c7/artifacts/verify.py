#!/usr/bin/env python3
from fractions import Fraction


def l1_from_bernoulli(p, h):
    corr = [
        (p+h)*(p-h),
        (1-p-h)*(1-p+h),
        (p+h)*(1-p+h),
        (1-p-h)*(p-h),
    ]
    prod = [p*p, (1-p)*(1-p), p*(1-p), (1-p)*p]
    return sum(abs(x-y) for x, y in zip(corr, prod))

for n in range(2, 65):
    sharp = Fraction(2, n) + Fraction(2, n*n)
    # Exact equality corners in sector coordinates u,v = +/-1.
    for u, v in [(Fraction(1), Fraction(-1)), (Fraction(-1), Fraction(1))]:
        a = (u + (n-1)*v) / n
        y = (u-v) / n
        p = (1+a) / 2
        h = y / 2
        assert l1_from_bernoulli(p, h) == sharp

    # Deterministic rational grid inside the exchangeability square.
    for iu in range(-10, 11):
        for iv in range(-10, 11):
            u = Fraction(iu, 10)
            v = Fraction(iv, 10)
            a = (u + (n-1)*v) / n
            y = (u-v) / n
            p = (1+a) / 2
            h = y / 2
            # The exact four-entry formula is independent of p.
            got = l1_from_bernoulli(p, h)
            formula = 2*abs(h) + 2*h*h
            assert got == formula
            assert got <= sharp

print('VERIFY_OK')
