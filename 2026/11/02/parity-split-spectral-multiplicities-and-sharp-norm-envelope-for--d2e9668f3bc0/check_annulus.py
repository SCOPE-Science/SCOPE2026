"""Standalone exact-arithmetic supplementary checks for a weighted annular Hardy multiplier.
Run: python3 check_annulus.py
These finite checks do not replace the universal analytic proof.
"""
from fractions import Fraction as F
from math import isclose


def lam(q, b, n):
    Q = q*q
    t = b*Q**(n-1)
    return (1-Q)**2*t/((1+t)*(1+Q*t))


def weight_sq(q, b, n):
    Q = q*q
    return (1+b*Q**(n+1))/(1+b*Q**n)


count = 0
for q in (F(1, 2), F(1, 3), F(2, 3), F(3, 5)):
    Q = q*q
    low = (1-Q)**2/(2*(1+Q))
    high = (1-q)**2
    assert low <= high
    for k in range(-5, 6):
        b = q**k
        ev = {n: lam(q, b, n) for n in range(-18, 19)}
        for n, e in ev.items():
            assert e == weight_sq(q, b, n)-weight_sq(q, b, n-1)
            assert e > 0
            assert lam(q, b*Q, n) == lam(q, b, n+1)
            assert e == lam(q, b, 1-k-n)
            count += 4
        for n, en in ev.items():
            for m, em in ev.items():
                if n != m and en == em:
                    assert n+m == 1-k
                count += 1
        assert max(ev.values()) == (high if k%2 else low)
        count += 1
        if k%2:
            assert all(ev[-(k-1)//2] >= x for x in ev.values())
    for b in (F(7, 10), F(11, 7), F(13, 23), F(1, 17), F(77, 3)):
        ev = [lam(q, b, n) for n in range(-15, 16)]
        assert len(set(ev)) == len(ev), (q, b)
        assert low < max(ev) < high, (q, b)
        count += 2
        for n in range(-10, 11):
            assert lam(q, b*Q, n) == lam(q, b, n+1)
            count += 1
    for b in (F(1, 7), F(2, 1), F(19, 13)):
        partial = sum((lam(q, b, n) for n in range(-90, 91)), F(0))
        assert abs(float(partial-(1-Q))) < 1e-12
        count += 1
print('PASS:', count, 'exact rational checks and tail comparisons')
