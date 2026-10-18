#!/usr/bin/env python3
"""Exact rational checks for an algebraic positive-integer pgf family.

Reproduce with: python3 check_coefficients.py
The infinite assertions in the accompanying proof are analytic, not inferred
from the finite calculations here.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext


def series(theta, nmax):
    """Compute [z^n] (sqrt((1+c(z^2+2z))/(1-d(z^2+2z)))-1)."""
    theta = F(theta)
    c, d = (4*theta-1)/3, (1-theta)/3
    q = [F(0)] * (nmax+1)
    f = [F(0)] * (nmax+1)
    q[0] = f[0] = F(1)
    for n in range(1, nmax+1):
        q[n] = 2*d*q[n-1] + (d*q[n-2] if n>=2 else F(0))
        if n == 1:
            q[n] += 2*c
        if n == 2:
            q[n] += c
        f[n] = (q[n] - sum((f[j]*f[n-j] for j in range(1,n)), F(0)))/2
    # Check direct algebraic identity (1-d t)F^2=1+c t coefficientwise.
    sq = [sum((f[j]*f[n-j] for j in range(n+1)), F(0)) for n in range(nmax+1)]
    for n in range(nmax+1):
        lhs = sq[n]- (2*d*sq[n-1] if n>=1 else F(0)) - (d*sq[n-2] if n>=2 else F(0))
        rhs = F(1) if n==0 else (2*c if n==1 else (c if n==2 else F(0)))
        assert lhs == rhs
    assert f[1] == theta
    return f[1:]


def main():
    checks = 0
    for t in [F(1,10),F(1,4),F(1,3),F(2,5),F(1,2)]:
        z = series(t, 120)
        assert all(v>0 for v in z)
        checks += len(z)
    bad = series(F(11,20), 100)
    neg = [i+1 for i,v in enumerate(bad) if v<0]
    assert len(neg)>0 and neg[0] == 39
    checks += len(bad)
    with localcontext() as ctx:
        ctx.prec = 55
        lo = Decimal('1.68133064')
        hi = Decimal('1.68133065')
        poly = lambda x: x*x*x + 2*x*x - 5*x - 2
        assert poly(lo)<0<poly(hi)
        t_lo = (1+3/(hi*hi))/4
        t_hi = (1+3/(lo*lo))/4
        assert Decimal('0.51531084')<t_lo<t_hi<Decimal('0.51531086')
        checks += 4
        print('Critical parameter rigorously bracketed:', t_lo, t_hi)
    print('Exact algebraic/finite-coefficient assertions:', checks)
    print('First negative coefficient at theta=11/20:', neg[0])
    print('PASS')


if __name__ == '__main__':
    main()
