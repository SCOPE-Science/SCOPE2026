#!/usr/bin/env python3
"""Standalone arithmetic checks for the positive opinion/leadership equilibrium theorem.

Uses Python standard library only. The algebraic proof for arbitrary networks is
in RESULT.md; these computations are finite consistency checks, not that proof.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
getcontext().prec = 65
D = Decimal


def check_identity():
    cases = 0
    for rho in [Fraction(1, 500), Fraction(1, 3), Fraction(2), Fraction(17)]:
        for r in [Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(1)]:
            for s in [Fraction(1, 10), Fraction(1, 3), Fraction(1, 2), Fraction(9, 10)]:
                a = r + (r-s)**3/(rho*r*r)
                if a <= 0:
                    continue
                left = rho*r**3 + (r-s)**2*(r+2*s)
                A = 3*s*(r-s)**2
                B = rho*a*r*r
                assert left == A+B, (rho, r, s)
                assert Fraction(0) <= A/(A+B) < 1
                gprime = 1 + (r-s)**2*(r+2*s)/(rho*r**3)
                assert gprime > 0
                cases += 1
    return cases


def phi(s, a, rho):
    lo, hi = sorted((s, a))
    for _ in range(190):
        r = (lo+hi)/2
        value = r+(r-s)**3/(rho*r*r)
        if value < a:
            lo = r
        else:
            hi = r
    return (lo+hi)/2


def T(u, a, W, rho):
    return [phi(sum(w*v for w,v in zip(row,u)), ai, rho) for row,ai in zip(W,a)]


def ldist(a,b):
    return max(abs((u/v).ln()) for u,v in zip(a,b))


def model_checks():
    W = [
        [D(0), D('0.5'), D('0.5'), D(0)],
        [D('0.25'), D(0), D('0.5'), D('0.25')],
        [D('0.25')]*4,
        [D(0),D(0),D(1),D(0)],
    ]
    for row in W:
        assert sum(row) == 1
    a = [D('0.2'),D('0.4'),D('0.6'),D('0.8')]
    b = [D('0.2'),D('0.5'),D('0.6'),D('0.8')]
    for rho in [D('0.03'),D('0.6'),D('11')]:
        lower, upper = min(a), max(a)
        Amax = 3*upper*(upper-lower)**2
        q = Amax/(Amax+rho*lower**3)
        assert 0<=q<1
        u=[D('0.8')]*4
        v=[D('0.2')]*4
        for k in range(3):
            Tu, Tv = T(u,a,W,rho),T(v,a,W,rho)
            assert ldist(Tu,Tv) <= q*ldist(u,v) + D('1e-45')
            u,v=Tu,Tv
        def solve(data):
            t=[D('0.5')]*4
            for _ in range(1500):
                nxt=T(t,data,W,rho)
                if max(abs(x-y) for x,y in zip(t,nxt))<D('1e-46'):
                    return nxt
                t=nxt
            raise AssertionError('iteration did not meet numerical tolerance')
        x=solve(a)
        xb=solve(b)
        assert all(lo -D('1e-40') <= v <= hi+D('1e-40') for v,lo,hi in zip(x, [min(a)]*4,[max(a)]*4))
        assert all(xx<=yy+D('1e-43') for xx,yy in zip(x,xb))
        for i,row in enumerate(W):
            s=sum(w*t for w,t in zip(row,x))
            d=x[i]-s
            y=rho*x[i]**2/(rho*x[i]**2+d*d)
            assert 0<y<=1
            assert abs(d**3+rho*x[i]**2*(x[i]-a[i]))<D('1e-43')
            assert abs(-(1-y)*d-y*(x[i]-a[i]))<D('1e-43')
            assert abs(rho*(1-y)*x[i]**2-y*d*d)<D('1e-43')
    return 3


def boundary_checks():
    # With W=I, all coordinate equations reduce to x_i=a_i, y_i=1;
    # a zero-opinion/zero-leadership state also exists outside the positive sector.
    a=[D('0.1'),D('0.9')]
    W=[[D(1),D(0)],[D(0),D(1)]]
    for rho in [D('0.000001'), D(1), D('1000000')]:
        assert T(a,a,W,rho)==a
    return 3

if __name__ == '__main__':
    n=check_identity()
    ncases=model_checks()
    b=boundary_checks()
    print(f'VERIFY_OK: {n} exact rational scalar identities; {ncases} finite-network parameter tests; {b} reducible boundary cases')
