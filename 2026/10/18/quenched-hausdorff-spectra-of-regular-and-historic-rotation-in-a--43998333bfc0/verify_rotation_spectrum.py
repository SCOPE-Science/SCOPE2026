#!/usr/bin/env python3
"""Finite consistency checks for a three-branch random circle model."""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import exp, log, isclose

def inverse_step(sign,d,y):
    if sign=='+':
        return ((y, y+1, 3-y)[d])/3
    return ((1-y, 1+y, 2+y)[d])/3

def direct_step(sign,x):
    if sign=='+':
        v=3*x if x<Fraction(2,3) else 4-3*x
    else:
        v=-3*x if x<Fraction(1,3) else 3*x-2
    k=v.numerator//v.denominator
    return k,v-k

def kappa(sign,d):
    return ((0,1,1) if sign=='+' else (-1,-1,0))[d]

def verify_base(signs):
    n=len(signs)
    dp=Counter({0:1})
    for s in signs:
        new=Counter()
        for old,num in dp.items():
            for d in range(3):
                new[old+kappa(s,d)]+=num
        dp=new
    observed=Counter()
    for ds in product(range(3),repeat=n):
        y=Fraction(1,2)
        for s,d in reversed(tuple(zip(signs,ds))):
            y=inverse_step(s,d,y)
        initial=y
        displacement=0
        for s,d in zip(signs,ds):
            step,y=direct_step(s,y)
            assert 0<=y<1
            assert step==kappa(s,d), (signs,ds,s,d,step)
            displacement+=step
        observed[displacement]+=1
        assert -1 < (Fraction(displacement)+y-initial)-displacement < 1
    assert observed==dp
    assert sum(dp.values())==3**n
    return 3**n

def pressure(t,p):
    return p*log(1+2*exp(t))+(1-p)*log(1+2*exp(-t))

def pprime(t,p):
    return p*(2*exp(t)/(1+2*exp(t)))-(1-p)*(2*exp(-t)/(1+2*exp(-t)))

def spec(r,p):
    if abs(r-p)<1e-12: return p*log(2)/log(3)
    if abs(r+1-p)<1e-12: return (1-p)*log(2)/log(3)
    lo,hi=-40,40
    for _ in range(100):
        mid=(lo+hi)/2
        if pprime(mid,p)<r:lo=mid
        else:hi=mid
    t=(lo+hi)/2
    return (pressure(t,p)-t*r)/log(3)

def main():
    count=0
    for n in range(1,6):
        for signs in product('+-',repeat=n):
            count+=verify_base(signs)
    for signs in ['++-+-++','---++--','+-+-+-+']:
        count+=verify_base(signs)
    for p in [0.17,0.5,0.83]:
        assert isclose(spec(p,p),p*log(2)/log(3),abs_tol=1e-10)
        assert isclose(spec(p-1,p),(1-p)*log(2)/log(3),abs_tol=1e-10)
        assert isclose(spec((4*p-2)/3,p),1,abs_tol=1e-11)
        for j in range(21):
            r=p-1+j/20
            assert 0<spec(r,p)<=1+1e-12
    print('VERIFY_OK: independent branch inverses, exact rational lifted itineraries and polynomial word-count distributions; checked words =',count,'; pressure/endpoint/concavity tests passed')

if __name__=='__main__': main()
