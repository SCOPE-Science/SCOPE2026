#!/usr/bin/env python3
"""Exact-rational checks for the quadratic Lorentz hyperplane projection law."""
from fractions import Fraction as F
from itertools import product


def predicted(n, t):
    assert n >= 3 and 0 <= t <= 1
    if t <= F(1, n-1):
        return F(4*(n-1), n*n) * (n-1+t) / (1+(n-1)*t)
    return 1 + F(n-1, n*n)*(1-t)**2/t


def nsquare(v, t):
    return t*sum(z*z for z in v)+(1-t)*max(abs(z) for z in v)**2


def ratio(v, t):
    z=sum(v, F(0))/len(v)
    y=[x-z for x in v]
    return nsquare(y,t)/nsquare(v,t)


def reduced(n, t, a):
    assert F(0) <= a <= F(n-2,n)
    u=1+t+2*(1-t)*a+(1-t+F(2*n,n-2)*t)*a*a
    v=1+t+F(n*n,n-2)*t*a*a-max(F(0),n*t*a-(1-t))**2/(1+(n-1)*t)
    return u/v


def run():
    witness_cases=0
    grid_cases=0
    for n in range(3,9):
        for t in [F(0),F(1,20),F(1,n-1),F(1,3),F(1,2),F(4,5),F(1)]:
            lam=predicted(n,t)
            a=F(1) if t<=F(1,n-1) else (n-1)*t
            v=[a]+[F(-1)]*(n-1)
            assert ratio(v,t)==lam,(n,t,'equality witness')
            assert reduced(n,t,F(n-2,n))==lam,(n,t,'scalar endpoint')
            witness_cases+=1
            for k in range(31):
                aa=F(n-2,n)*F(k,30)
                assert reduced(n,t,aa)<=lam,(n,t,'scalar grid')
            if n<=5:
                for coords in product(range(-2,3), repeat=n):
                    if any(coords):
                        v=list(map(F,coords))
                        assert ratio(v,t)<=lam,(n,t,'integer grid',coords)
                        grid_cases+=1
    print('PASS exact equality cases:',witness_cases)
    print('PASS finite vector grid checks:',grid_cases)
    print('PASS scalar rational grids and endpoints')

if __name__=='__main__':
    run()
