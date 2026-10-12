#!/usr/bin/env python3
"""Finite exact moment replay and numerical asymptotic sanity checks."""
from fractions import Fraction
from itertools import product
import math


def exact_rho(n, t):
    l=(1-t)**n
    e=t**n
    b=(1-2*t)**n
    s=l+e
    return (s*s-b)/(l+3*e-s*s)


def exhaustive_rho(n, t):
    p={0:t,1:1-2*t,2:t}
    m1=m2=v1=v2=mv=Fraction(0)
    for outcome in product((0,1,2), repeat=n):
        weight=math.prod(p[x] for x in outcome)
        mn=min(outcome)
        mx=max(outcome)
        m1 += weight*mn
        m2 += weight*mn*mn
        v1 += weight*mx
        v2 += weight*mx*mx
        mv += weight*mn*mx
    vm=m2-m1*m1
    vx=v2-v1*v1
    assert vm==vx and vm>0
    return (mv-m1*v1)/vm

nchecks=0
for n in range(2,7):
    for t in (Fraction(1,7), Fraction(1,4), Fraction(1,3), Fraction(2,5), Fraction(1,2)):
        a=exact_rho(n,t)
        b=exhaustive_rho(n,t)
        assert a==b, (n,t,a,b)
        assert a>0
        nchecks+=1
assert exact_rho(2,Fraction(1,3))==Fraction(8,19)
assert exact_rho(3,Fraction(3,10))==Fraction(81,319)

lo,hi=1.0,2.0
for _ in range(90):
    mid=(lo+hi)/2
    if (2-mid)*math.exp(mid)>2:
        lo=mid
    else:
        hi=mid
cstar=(lo+hi)/2
constant=cstar*(2-cstar)
assert 1.5936<cstar<1.5937
assert 0.6476<constant<0.6477
assert abs(constant-cstar*cstar/math.expm1(cstar))<1e-13

def floating_rho(n,t):
    l=(1-t)**n
    e=t**n
    b=(1-2*t)**n
    s=l+e
    return (s*s-b)/(l+3*e-s*s)

# A grid gives only a lower bound on the exact optimum; no proof relies on it.
for n in (16,32,64,128,256):
    candidates=[(floating_rho(n,(j+1)/(25*n)),(j+1)/(25*n)) for j in range(1,int(25*n/2)-1)]
    best_r,best_t=max(candidates)
    assert abs(n*best_r-constant)<1.0/n
    assert abs(n*best_t-cstar)<8.0/math.sqrt(n)

print(
  'VERIFY_OK'
  f' exact_enumeration_cases={nchecks}'
  f' c_star={cstar:.15f}'
  f' sharp_constant={constant:.15f}'
  f' n256_at_limit_scale={256*floating_rho(256,cstar/256):.12f}'
)
