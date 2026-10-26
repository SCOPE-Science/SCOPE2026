#!/usr/bin/env python3
"""Finite diagnostic checks for a sharp quasi-Schatten Schur-mask formula.

Only Python standard-library functions are required; finite tests are not a
substitute for the proof of the operator-ideal result.
"""
import cmath
import math
import random


def sharp_constant(p):
    def derivative(k):
        g = (1 - 3*k*k)/(k*(1 + 3*k*k))
        h = ((1+k)**(p-1) - (1-k)**(p-1))/((1+k)**p+(1-k)**p)
        return g+h
    if p == 1:
        k = 1/math.sqrt(3)
    else:
        lo, hi = 1e-12, 1/math.sqrt(3)
        for _ in range(100):
            mid = (lo+hi)/2
            if derivative(mid) > 0:
                lo = mid
            else:
                hi = mid
        k = (lo+hi)/2
    u = 4*k*k/(1+3*k*k)
    a = (math.sqrt(u*(4-3*u))+u)/2
    b = (math.sqrt(u*(4-3*u))-u)/2
    return (a**p+b**p)**(1/p), u


def sv_formula(s,t):
    tau = s+t-s*t
    prod = math.sqrt(max(0,s*t*(1-s)*(1-t)))
    discr = math.sqrt(max(0,tau*tau-4*prod*prod))
    return math.sqrt(max(0,(tau+discr)/2)),math.sqrt(max(0,(tau-discr)/2))


def sample_unit(rng,n):
    z = [complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(n)]
    norm=math.sqrt(sum(abs(v)**2 for v in z))
    return [v/norm for v in z]


def independent_spectrum(x,y):
    n=len(x)
    a=[[x[i]*y[j].conjugate() if (i==0 or j==0) else 0j for j in range(n)] for i in range(n)]
    gram=[[sum(a[i][k]*a[j][k].conjugate() for k in range(n)) for j in range(n)] for i in range(n)]
    trace=sum(gram[i][i].real for i in range(n))
    tr2=sum(abs(gram[i][j])**2 for i in range(n) for j in range(n))
    delta=math.sqrt(max(0,2*tr2-trace*trace))
    return math.sqrt(max(0,(trace+delta)/2)),math.sqrt(max(0,(trace-delta)/2))


def run():
    rng=random.Random(26051018)
    checks=0
    for p in (0.1,0.25,0.5,0.8,1.0):
        bound,u=sharp_constant(p)
        assert 0<u<=2/3+1e-10
        checks+=1
        for _ in range(1000):
            s,t=rng.random(),rng.random()
            a,b=sv_formula(s,t)
            value=(a**p+b**p)**(1/p)
            assert value<=bound*(1+2e-10)
            ss=(s+t)/2
            aa,bb=sv_formula(ss,ss)
            assert a**p+b**p<=aa**p+bb**p+3e-12
            checks+=2
        for _ in range(1000):
            x=sample_unit(rng,4);y=sample_unit(rng,4)
            a,b=independent_spectrum(x,y)
            aa,bb=sv_formula(abs(x[0])**2,abs(y[0])**2)
            assert abs(a-aa)<2e-7 and abs(b-bb)<2e-7
            checks+=1
    cp,up=sharp_constant(1)
    assert abs(cp-2/math.sqrt(3))<1e-12 and abs(up-2/3)<1e-12
    checks+=1
    c,u=sharp_constant(.5)
    uexact=(7-math.sqrt(13))/6
    cexact=math.sqrt(uexact*(4-3*uexact))+2*math.sqrt(uexact*(1-uexact))
    assert abs(u-uexact)<1e-12 and abs(c-cexact)<1e-12
    checks+=1
    print('PASS',checks,'finite diagnostic assertions', 'C(1/2)=',round(c,12),'C(1)=',round(cp,12))


if __name__=='__main__':
    run()
