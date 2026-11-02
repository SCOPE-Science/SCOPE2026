#!/usr/bin/env python3
"""Exact finite-size and numerical checks for terminal coupon-batch laws."""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, log, exp, cos, sin, pi, sqrt, sinh

CHECKS=0

def check(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1

def direct(n,d,rounds):
    subsets=[sum(1 << k for k in C) for C in combinations(range(n),d)]
    prob=Fraction(1,len(subsets))
    states={0:Fraction(1)}
    answer={}
    allmask=(1<<n)-1
    for t in range(1,rounds+1):
        next_states={}
        for mask,weight in states.items():
            missing=n-mask.bit_count()
            if missing and missing <= d:
                for subset in subsets:
                    if mask | subset==allmask:
                        key=(t,missing)
                        answer[key]=answer.get(key,Fraction(0))+weight*prob
            for subset in subsets:
                newmask=mask | subset
                next_states[newmask]=next_states.get(newmask,Fraction(0))+weight*prob
        states=next_states
    return answer

def exact_ie(n,d,t,r):
    if r>d or r<1:
        return Fraction(0)
    denominator=comb(n,d)
    u=Fraction(0)
    for j in range(n-r+1):
        possible=comb(n-r-j,d) if n-r-j>=d else 0
        u+=(-1)**j*comb(n-r,j)*Fraction(possible,denominator)**(t-1)
    return comb(n,r)*u*Fraction(comb(n-r,d-r),denominator)

def profile(c,phase,r):
    q=1-c
    total=0.
    for k in range(-110,160):
        z=q**(k-1-phase)
        if z<800:
            total+=exp(-z)*(c*z)**r/factorial(r)
    return total

for n in range(3,8):
  for d in range(1,n):
    obs=direct(n,d,6)
    for t in range(1,7):
      for r in range(1,d+1):
        check(obs.get((t,r),Fraction(0))==exact_ie(n,d,t,r),(n,d,t,r))

for c in [0.5,0.8,0.9]:
    q=1-c
    a=-log(q)
    for r in range(1,8):
        midpoint=sum(profile(c,(i+0.5)/256,r) for i in range(256))/256
        expected=c**r/(a*r)
        check(abs(midpoint-expected)<2e-11,(c,r,midpoint,expected))
    for phase in [0,0.25,0.5,0.9]:
        count=0.
        for k in range(-100,160):
            z=q**(k-1-phase)
            count+=exp(-q*z)-exp(-z)
        check(abs(count-1)<1e-12,(c,phase,count))

c=0.9
q=0.1
a=-log(q)
m=2048
re=sum(profile(c,(i+0.5)/m,1)*cos(-2*pi*(i+0.5)/m) for i in range(m))/m
im=sum(profile(c,(i+0.5)/m,1)*sin(-2*pi*(i+0.5)/m) for i in range(m))/m
coefficient_size=sqrt(re*re+im*im)
y=2*pi/a
predicted=(c/a)*sqrt(pi*y/sinh(pi*y))
check(abs(coefficient_size-predicted)<1e-12,(coefficient_size,predicted))
check(abs(profile(0.9,0.0,1)-profile(0.9,0.5,1))>0.05,'nonconstant phase')
print('ALL CHECKS PASSED:',CHECKS)
print('q=0.1 uniqueness probabilities at phases 0,1/2:', profile(.9,0,1),profile(.9,.5,1))
print('first Fourier coefficient magnitude:',coefficient_size)
