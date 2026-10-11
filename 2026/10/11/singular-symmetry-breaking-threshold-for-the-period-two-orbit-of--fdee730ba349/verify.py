#!/usr/bin/env python3
"""Finite numerical and exact-rational checks for a replicator-map two-cycle theorem.

Python 3.9+ standard library. These diagnostics cannot establish the
universal uniqueness theorem or the singular asymptotic limit.
"""
from math import exp, log, log1p, isclose
from fractions import Fraction as F


def cycle_data(z, b):
    """Parametrize the nontrivial cycle by logarithmic lower endpoint z."""
    x = exp(-z)
    y = 2*b-x
    assert 0 < x < b < y < 1
    a = (z + log1p(-x) + log(y) - log1p(-y))/(b-x)
    lx = 1-a*x*(1-x)
    ly = 1-a*y*(1-y)
    return a, x, y, lx*ly


def at_a(a_target,b):
    lo = -log(b)+1e-3
    hi = 35.0 if b == 0.5 else 400.0
    assert cycle_data(lo,b)[0] < a_target < cycle_data(hi,b)[0]
    for _ in range(120):
        z=(lo+hi)/2
        if cycle_data(z,b)[0]<a_target:
            lo=z
        else:
            hi=z
    return cycle_data((lo+hi)/2,b)


def flip(b):
    lo=-log(b)+1e-3
    hi=250.0
    assert cycle_data(lo,b)[3]>-1>cycle_data(hi,b)[3]
    for _ in range(120):
        z=(lo+hi)/2
        if cycle_data(z,b)[3]>-1:
            lo=z
        else:
            hi=z
    return cycle_data((lo+hi)/2,b)


def f(a,b,x):
    return x/(x+(1-x)*exp(a*(x-b)))


def run():
    count=0
    for num in range(2,40):
        for den in range(40,90,7):
            x=F(num,den+40)
            y=F(num+1,den+40)
            a=F(13,3)
            qx=x*(1-x); qy=y*(1-y)
            lam=(1-a*qx)*(1-a*qy)
            assert 1-lam==a*(qx+qy-a*qx*qy)
            count +=1
    for delta in (0.1,0.05,0.02,0.01,0.005):
        b=0.5-delta
        acrit,xcrit,ycrit,mult=flip(b)
        a0=2/(b*(1-b))
        leading=1/(delta*(1-2*delta))
        assert acrit>a0
        assert abs(mult+1)<1e-10
        assert 0.5/delta<acrit<2/delta
        assert abs(acrit/leading-1)<0.2
        count+=4
        for t in (.8, 1.,1.2):
            a,x,y,L=at_a(acrit*t,b)
            assert isclose(a,acrit*t,rel_tol=1e-12)
            assert isclose(f(a,b,x),y,rel_tol=1e-11)
            assert isclose(f(a,b,y),x,rel_tol=1e-11,abs_tol=1e-70)
            assert L<1
            if t<1: assert -1<L<1
            if t>1: assert L< -1
            if t==1: assert abs(L+1)<1e-10
            count+=5
        if delta<=.05:
            assert abs(acrit-leading)<2/(delta**2)*exp(-1/(40*delta))
            count+=1
        print(f'delta={delta:.3g}; critical a={acrit:.15g}; leading={leading:.15g}; difference={acrit-leading:.3g}')
    for a in (8.1,9.,12.,20.,50.,100.):
        A,x,y,L=at_a(a,.5)
        assert isclose(x+y,1.,abs_tol=1e-14)
        assert 0<=L<1
        assert isclose(L,(1-a*x*(1-x))**2,abs_tol=1e-12)
        count+=3
    print('VERIFY_OK; exact-rational and finite numerical checks:',count)
if __name__=='__main__':run()
