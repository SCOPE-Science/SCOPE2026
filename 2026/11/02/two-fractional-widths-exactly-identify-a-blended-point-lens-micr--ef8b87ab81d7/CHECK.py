#!/usr/bin/env python3
"""Reproducible finite checks for the exact two-width microlensing theorem.

The global uniqueness statement rests on the analytic monotone-ratio proof
in RESULT.md, not on finite numerical tests.
Uses Python's standard library only; run with: python3 CHECK.py
"""
from decimal import Decimal as D, getcontext
from itertools import product

getcontext().prec = 75
ZERO, ONE, TWO = D(0), D(1), D(2)


def q(y):
    """Squared impact parameter at excess magnification y>0."""
    assert y > 0
    return TWO * ((ONE + y) / (y * (y + TWO)).sqrt() - ONE)


def magnification(u):
    return (u*u + TWO) / (u * (u*u + D(4)).sqrt())


def width2(alpha, y):
    return q(alpha*y) - q(y)


def ratio(alpha, beta, y):
    return width2(alpha, y) / width2(beta, y)


def inverse(alpha, beta, peak, ra, wb):
    """Return (u0, tE, blend) from peak, squared width ratio, short width."""
    lo = peak
    assert ra + D("1e-55") >= ratio(alpha, beta, lo)
    if ra < ratio(alpha,beta,lo):
        ra = ratio(alpha,beta,lo)
    hi = lo * TWO
    while ratio(alpha, beta, hi) <= ra:
        hi *= TWO
        if hi > D('1e25'):
            raise ValueError('Cannot bracket the ratio')
    for _ in range(235):
        mid = (lo + hi) / TWO
        if ratio(alpha, beta, mid) < ra:
            lo = mid
        else:
            hi = mid
    y = (lo+hi)/TWO
    return q(y).sqrt(), wb / width2(beta,y).sqrt(), peak / y


def close(x, y, rel=D('1e-34')):
    assert abs(x-y) <= rel * max(ONE, abs(x), abs(y)), (x,y)


def run():
    count = 0
    params = [(D(1)/D(4), D(1)/D(2)), (D(1)/D(3), D(2)/D(3)),
              (D(1)/D(5), D(1)/D(3))]
    mag = [D('0.015'), D('0.08'), D('0.3'), D(1), D(3), D(15)]
    blends = [D('0.1'), D('0.25'), D('0.5'), D(1)]
    scales = [D('0.5'), D('1.5'), D(4)]
    for alpha,beta in params:
        lower = ((ONE/alpha).sqrt()-ONE)/((ONE/beta).sqrt()-ONE)
        upper = ((ONE/alpha)**2-ONE)/((ONE/beta)**2-ONE)
        for y in mag:
            r=ratio(alpha,beta,y)
            assert lower < r < upper
            count += 2
        # Finite monotonicity stress-test, not the proof.
        grid=[D('0.001'),D('0.005'),D('0.02'),D('0.1'),D('0.5'),D(1),D(3),D(10),D(100)]
        rs=[ratio(alpha,beta,y) for y in grid]
        assert all(x<z for x,z in zip(rs,rs[1:]))
        count += 1
        for y,f,tE in product(mag, blends, scales):
            u=q(y).sqrt()
            obs=f*y
            wa=tE*width2(alpha,y).sqrt()
            wb=tE*width2(beta,y).sqrt()
            R=ratio(alpha,beta,y)
            close(R,(wa/wb)**2,D("1e-65"))
            assert R + D("1e-55") >= ratio(alpha,beta,obs)
            count += 1
            u2,tE2,f2=inverse(alpha,beta,obs,R,wb)
            close(u2,u)
            close(tE2,tE)
            close(f2,f)
            count += 3
            # Direct forward light-curve check at both level crossings.
            for frac,width in [(alpha,wa),(beta,wb)]:
                ulevel=(u*u+(width/tE)**2).sqrt()
                close(f*(magnification(ulevel)-ONE),frac*obs)
                count += 1
    # Simple reproducible illustrative case.
    a,b = D(1)/D(4), D(1)/D(2)
    y=ONE
    u=q(y).sqrt()
    wa=TWO*width2(a,y).sqrt()
    wb=TWO*width2(b,y).sqrt()
    R=(wa/wb)**2
    close(R, D('2.738661863533376051502778808196088378427'),D('1e-39'))
    count += 1
    print('checks_passed=',count)
    print('example_u0=',u)
    print('example_peak_excess=',D(1)/D(2))
    print('example_wa=',wa)
    print('example_wb=',wb)
    print('example_squared_ratio=',R)
    print('example_unblended_lower_ratio=',ratio(a,b,D(1)/D(2)))
    print('global_theorem_proof=analytic_in_RESULT.md')

if __name__ == '__main__':
    run()
