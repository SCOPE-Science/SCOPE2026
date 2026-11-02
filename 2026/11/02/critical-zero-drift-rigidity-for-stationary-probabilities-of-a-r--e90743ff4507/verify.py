#!/usr/bin/env python3
"""Supplementary numerical and rational checks of critical random-interval model."""
from decimal import Decimal, localcontext
from fractions import Fraction


def critical_gamma():
    with localcontext() as ctx:
        ctx.prec = 75
        two = Decimal(2)
        def q(v):
            return two * (two.ln() - 1) - v * (v.ln() - 1)
        lo, hi = Decimal('0.2'), Decimal('0.4')
        assert q(lo) < 0 < q(hi)
        for _ in range(300):
            mid = (lo + hi)/2
            if q(mid) < 0:
                lo = mid
            else:
                hi = mid
        gamma = (lo + hi)/2
        assert Decimal('0.26258') < gamma < Decimal('0.26259')
        mean_log = q(gamma)/(two-gamma)
        assert abs(mean_log) < Decimal('1e-65')
        return gamma


def step(x, b):
    return b*x if x <= Fraction(1,2) else 2*x-1


def verify_reachability():
    total = 0
    # A finite diagnostic; the proof covers uncountably many x via generic b.
    for den in range(2,50):
        for num in range(1,den//2+1):
            x=Fraction(num,den)
            witness = False
            for b in (Fraction(7,4), Fraction(13,8), Fraction(8,5), Fraction(5,3)):
                y=x
                for n in range(1,160):
                    y=step(y,b)
                    if Fraction(1,2) < y < 1:
                        witness=True
                        break
                    if y>=1:
                        break
                if witness:
                    break
            assert witness, (num,den)
            total += 1
    assert step(Fraction(0),Fraction(3,2)) == 0
    assert step(Fraction(1),Fraction(3,2)) == 1
    return total

if __name__=='__main__':
    gamma=critical_gamma()
    checks=verify_reachability()
    print('gamma',gamma)
    print('rational-reachability-tests',checks)
    print('VERIFY_OK')
