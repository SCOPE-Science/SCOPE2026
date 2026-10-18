#!/usr/bin/env python3
"""Reproduce finite coefficient identities and numerical checks for a Gaussian-smoothed Poisson law.
No finite computation is used as a proof of the stated infinite identities.
"""
from fractions import Fraction
from math import factorial, exp, expm1, log, isclose


def a(n):
    return Fraction(2, factorial(n+2))


def coefficient_ratio(n):
    num = sum(a(j)*a(n+2-j) for j in range(1,n+2))
    den = (n+1)*a(n+2)
    return num/den


def exact_ratio(n):
    return Fraction(2*(2**(n+6)-(n+6)**2-(n+6)-2), (n+1)*(n+5)*(n+6))


def m(x):
    if abs(x) < 1.5:
        return sum(2*x**k/factorial(k+2) for k in range(70))
    return 2*(expm1(x)-x)/(x*x)


def dm(x):
    if abs(x) < 1.5:
        return sum(2*k*x**(k-1)/factorial(k+2) for k in range(1,35))
    ex = exp(x)
    return 2*((ex-1)*x-2*(ex-1-x))/x**3


def ratio(x):
    u=m(x)-1
    d=x*dm(x)-u
    return u*u/d


def objective(x,r):
    if x == 0:
        return 1/(3*(r+1))
    return (m(x)-1)/(x*(r+m(x)))


def solve(r):
    if r <= Fraction(1,3):
        return 0.,objective(0,r)
    lo,hi=0.0005,2.
    while ratio(hi)<r+1:
        hi=2*hi
    for _ in range(100):
        mid=(lo+hi)/2
        if ratio(mid) < r+1:lo=mid
        else:hi=mid
    x=(lo+hi)/2
    return x,objective(x,r)


def run():
    tests=0
    for n in range(0,101):
        assert coefficient_ratio(n)==exact_ratio(n)
        tests+=1
    for n in range(100):
        assert exact_ratio(n+1)>exact_ratio(n)
        tests+=1
    assert exact_ratio(0)==Fraction(4,3);tests+=1
    for r in [0,0.01,0.1,0.2,1/3]:
        x,c=solve(r)
        assert x==0 and isclose(c,1/(3*(1+r)),rel_tol=1e-12)
        tests+=1
        for y in [0.00001,0.01,0.1,0.3,1,3,10,30]:
            assert objective(y,r)<=c+1e-10,(r,y,objective(y,r),c)
            tests+=1
    for r in [0.34,0.5,1.,2.,5.,10.,100.,1000.,1e6,1e12,1e20,1e40]:
        x,c=solve(r)
        assert x>0 and c>1/(3*(1+r))
        tests+=1
        assert isclose(ratio(x),r+1,rel_tol=1e-10)
        tests+=1
        for y in [0.,x*.1,x*.5,x*.9,x*1.1,x*2,x*3]:
            assert objective(y,r)<=c+1e-9,(r,y,x,objective(y,r),c)
            tests+=1
    vals=[]
    for L in [10.,20.,40.,80.,120.,200.]:
        r=exp(L)
        x,c=solve(r)
        center=L+3*log(L)-log(2)
        vals.append((L,x-center,1/c-center-1))
        assert abs(x-center)<3
        assert abs(1/c-center-1)<4
        tests+=2
    print(f'PASS {tests} checks: exact coefficient ratios, monotonicity, endpoint/interior optimizer, and high-noise numerical consistency')
    print('L, optimizer residual, inverse-scale residual:')
    for v in vals:print(*['%.8f'%x for x in v])
if __name__=='__main__':run()
