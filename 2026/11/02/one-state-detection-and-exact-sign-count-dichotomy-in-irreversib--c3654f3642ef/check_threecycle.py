#!/usr/bin/env python3
"""Standalone numerical check of an exact three-state-cycle correlation theorem.
Python 3 standard library only; no network or external dependencies.
The reference is independent Poisson uniformization of the original generator.
Tests are numerical sanity checks; the analytical proof covers all positive rates.
"""
from math import exp, sqrt, sin, cos, cosh, sinh, pi, log, atanh, isfinite
from random import Random

def exact_indicator(a, b, c, i, t):
    rates = (a, b, c)
    x = rates[i]
    y, z = (rates[(i+1)%3], rates[(i+2)%3])
    total = a+b+c
    dlt = total*total-4*(a*b+a*c+b*c)
    damping = total/2
    slope = x+y*z/(y+z)
    if abs(dlt) < 1e-12 * total*total:
        return exp(-damping*t)*(1+(damping-slope)*t)
    if dlt < 0:
        freq = sqrt(-dlt)/2
        return exp(-damping*t)*(cos(freq*t)+(damping-slope)/freq*sin(freq*t))
    gap = sqrt(dlt)/2
    return exp(-damping*t)*(cosh(gap*t)+(damping-slope)/gap*sinh(gap*t))

def uniformized_return(a, b, c, i, t):
    rates=(a,b,c)
    peak=max(rates)
    mu=peak*t
    weights=exp(-mu)
    v=[0.,0.,0.];v[i]=1.
    summ=weights*v[i]
    mass=weights
    for k in range(1, 500):
        next_v=[0.,0.,0.]
        for j in range(3):
            stay=1-rates[j]/peak
            next_v[j]+=v[j]*stay
            next_v[(j+1)%3]+=v[j]*rates[j]/peak
        v=next_v
        weights*=mu/k
        summ+=weights*v[i]
        mass+=weights
        if k>mu+12*sqrt(mu+1) and weights<1.e-17:
            break
    assert 1-mass<1.e-11 and mass<=1+1.e-10,(mass,mu)
    return summ

def first_zero(rates, i):
    a,b,c=rates
    s=a+b+c
    dlt=s*s-4*(a*b+b*c+a*c)
    x=rates[i];y=rates[(i+1)%3];z=rates[(i+2)%3]
    r=x+y*z/(y+z)
    h=s/2
    if dlt<0:
        w=sqrt(-dlt)/2
        return (pi/2+__import__('math').atan((h-r)/w))/w
    if abs(dlt)<1e-10:
        return 1/(r-h) if r>h else None
    gap=sqrt(dlt)/2
    return atanh(gap/(r-h))/gap if r>h+gap else None

def test():
    rng=Random(20261027)
    count=0
    maxerror=0.
    for case in range(900):
        if case==0:rates=(1.,1.,1.)
        elif case==1:rates=(4.,1.,1.)
        elif case==2:rates=(10.,1.,1.)
        elif case==3:rates=(8.,3.,1.)
        elif case==4:rates=(4.+1.e-5,1.,1.)
        elif case==5:rates=(4.-1.e-5,1.,1.)
        else:rates=tuple(exp(rng.uniform(-1.5,1.5)) for _ in range(3))
        a,b,c=rates
        for i in range(3):
            prob=1/rates[i]/sum(1/x for x in rates)
            for t in (0.,.07,.2,.8,2.3):
                expected=(uniformized_return(a,b,c,i,t)-prob)/(1-prob)
                predicted=exact_indicator(a,b,c,i,t)
                err=abs(predicted-expected)
                maxerror=max(maxerror,err)
                assert err<4.e-12,(case,rates,i,t,predicted,expected)
                count+=1
        disc=(a+b+c)**2-4*(a*b+b*c+a*c)
        if disc >= 1.e-8:
            ids=[i for i in range(3) if first_zero(rates,i) is not None]
            assert ids==[rates.index(max(rates))],(case,rates,disc,ids)
            count+=1
    assert abs(first_zero((4.,1.,1.),0)-2/3)<1.e-13
    count+=1
    assert abs(first_zero((1.,1.,1.),0)-pi/sqrt(3))<1.e-13
    count+=1
    print('PASS independent Poisson-uniformization comparisons:',count)
    print('max absolute numerical discrepancy:',format(maxerror,'.4g'))
    print('exact repeated-eigenvalue crossing t = 2/3: verified')
    print('equal-rate first zero t = pi/sqrt(3): verified')

if __name__=='__main__':test()
