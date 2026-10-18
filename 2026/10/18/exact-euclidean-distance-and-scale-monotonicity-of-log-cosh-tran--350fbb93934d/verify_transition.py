#!/usr/bin/env python3
"""Finite numerical regression for the exact log-cosh transition-body profile."""
import math, random

def G(s):
    if not s > 0: raise ValueError('positive argument required')
    return s + math.log1p(math.sqrt(-math.expm1(-2*s)))

def ratio(n,s):
    return G(s)/(math.sqrt(n)*G(s/n))

def f(x):
    return math.log(math.cosh(x)) if abs(x) < 20 else abs(x)-math.log(2)+math.log1p(math.exp(-2*abs(x)))

def checks():
    rng=random.Random(1307)
    for n in range(2,9):
        for s in (0.001,0.01,0.05,0.2,1,3,20,100):
            rin=math.sqrt(n)*G(s/n)
            rout=G(s)
            assert rin<=rout+1e-9, (n,s,rin,rout)
            assert 1-1e-11<=ratio(n,s)<=math.sqrt(n)+1e-11
            assert abs(n*f(rin/math.sqrt(n))-s)<1e-9
            assert abs(f(rout)-s)<1e-9
            for k in range(100):
                v=[rng.gauss(0,1) for _ in range(n)]; mag=math.sqrt(sum(z*z for z in v));v=[z/mag for z in v]
                assert sum(f(rin*z) for z in v)<=s+1e-10
                assert sum(f(rout*z) for z in v)>=s-1e-10
        arr=[ratio(n,s) for s in (0.001,0.01,0.05,0.2,1,3,20,100)]
        assert all(arr[j+1]>arr[j] for j in range(len(arr)-1)),arr
    print('LOGCOSH_PARALLELOTOPE_SHARP_PROFILE_REGRESSIONS_OK')

if __name__=='__main__': checks()
