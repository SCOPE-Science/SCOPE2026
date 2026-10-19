#!/usr/bin/env python3
"""Finite reproducibility checks for the thin-strip linked-twist bound.

The infinite-parameter theorem rests on the accompanying analytical proof,
not on finite tests or numerical estimates.
"""
from fractions import Fraction as Q
import math


def mat(p, a, b):
    return ((Q(1), Q(a)/p), (Q(b)/p, Q(1)+Q(a*b)/(p*p)))


def apply(m, v):
    return (m[0][0]*v[0]+m[0][1]*v[1],
            m[1][0]*v[0]+m[1][1]*v[1])


def analytical_enclosure(p):
    low=p/(2-p)*max(math.log(1+1/p**2+1/(1+p)),
                       4*math.log(1/p)-2-math.log(1+p))
    high=2*p/(2-p)*math.log(1+1/p**2)
    return low,high


def exact_checks():
    n=0
    for den in (2, 3, 4, 5, 7, 10, 25, 50):
        for num in range(1,den):
            p=Q(num,den)
            assert (2-p)/p == 2/p-1
            L=Q(1)+1/(p*p)+1/(1+p)
            for a in (1,2,3,5,9):
                for b in (1,2,4,7):
                    m=mat(p,a,b)
                    for u,v in ((Q(0),Q(1)), (Q(1),Q(1)/p),
                                (Q(1),Q(2)/p), (Q(2),Q(9)/p)):
                        w=apply(m,(u,v))
                        assert w[1]>=w[0]/p
                        assert (w[0]+w[1])/(u+v)>=L
                        assert (w[0]+w[1])/(u+v)>=Q(a*b)/(p*p*(1+p))
                        assert m[0][0]+m[1][0] <= (1+Q(a)/p)*(1+Q(b)/p)
                        assert m[0][1]+m[1][1] <= (1+Q(a)/p)*(1+Q(b)/p)
                        n+=1
            low,high=analytical_enclosure(float(p))
            assert 0 < low <= high
    return n


def orbit_exponent(p, iterations=50000):
    # Deterministic typical-orbit diagnostic, not rigorous ergodic sampling.
    x,y=0.372183741,p*0.183726452
    u,v=1.0,1.0
    s=0.0
    for _ in range(iterations):
        if y<p:
            x=(x+y/p)%1
            u+=v/p
        if x<p:
            y=(y+x/p)%1
            v+=u/p
        scale=max(abs(u),abs(v))
        u/=scale
        v/=scale
        s+=math.log(scale)
    return s/iterations


def main():
    n=exact_checks()
    print('EXACT_RATIONAL_CHECKS_OK',n)
    for p in (.02,.05,.1,.2,.5,.8):
        low,high=analytical_enclosure(p)
        estimate=orbit_exponent(p)
        print('PARAMETER',p,'BOUND',round(low,8),round(high,8),
              'SIMULATED_EXPONENT',round(estimate,8))
        # The final result is analytic; the assertion below tests the implementation.
        assert low-0.01 < estimate < high+0.01
    print('FINITE_DIAGNOSTICS_OK')


if __name__=='__main__':
    main()
