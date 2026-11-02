#!/usr/bin/env python3
"""Finite arithmetic checks for coupon singleton second-order law.

Only the analytic proof in RESULT.md establishes the infinite limiting statement.
"""
import cmath
import math
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from scipy.integrate import quad

checks = 0

def test(c, detail):
    global checks
    checks += 1
    if not c:
        raise AssertionError(detail)

@lru_cache(None)
def assoc_stirling(m, k):
    if m == 0 and k == 0:
        return 1
    if m < 0 or k < 0 or (m > 0 and k == 0) or 2*k > m:
        return 0
    return k*assoc_stirling(m-1,k) + (m-1)*assoc_stirling(m-2,k-1)

def exact_joint(d,t,s):
    if s < 1 or s > d or s > t or t < d:
        return Fraction(0)
    return Fraction(math.factorial(d)*math.comb(t-1,s-1)*assoc_stirling(t-s,d-s),d**t)

# Direct dynamic programming on coupon occupancy counts, never using a Stirling recurrence.
for d in range(2,8):
    transient={(d,0):Fraction(1)}
    for t in range(1,21):
        nxt=defaultdict(Fraction)
        seen=defaultdict(Fraction)
        for (zero,one),prob in transient.items():
            p=prob*Fraction(zero,d)
            if zero==1:
                seen[one+1]+=p
            else:
                nxt[(zero-1,one+1)]+=p
            if one:
                nxt[(zero,one-1)] += prob*Fraction(one,d)
            occupied_twice=d-zero-one
            if occupied_twice:
                nxt[(zero,one)] += prob*Fraction(occupied_twice,d)
        transient=dict(nxt)
        for s in range(1,d+1):
            test(seen[s]==exact_joint(d,t,s),(d,t,s,seen[s],exact_joint(d,t,s)))
        test(sum(transient.values())+sum(exact_joint(d,k,s) for k in range(d,t+1) for s in range(1,d+1))==1,(d,t,'mass'))

# A separate continuous-time calculation: condition on the unique maximum of
# independent Exp(1) first arrival times. The other n-1 counts are iid
# Poisson(y) conditioned to be at least one.
def pmix(d,s):
    def g(u):
        if u==0:
            return 0.
        if u==1:
            p=1.
        else:
            p=-u*math.log(u)/(1-u)
        return d*(1-u)**(d-1)*math.comb(d-1,s-1)*p**(s-1)*(1-p)**(d-s)
    return quad(g,0,1,epsabs=2e-12,epsrel=2e-12,limit=160)[0]

for d in range(2,9):
    l=300
    for s in range(1,d+1):
        exact=float(sum(exact_joint(d,t,s) for t in range(d,l+1)))
        approx=pmix(d,s)
        test(abs(exact-approx)<1e-10,(d,s,exact,approx))
    expected=sum(s*pmix(d,s) for s in range(1,d+1))
    harmonic=sum(Fraction(1,i) for i in range(1,d+1))
    test(abs(expected-float(harmonic))<1e-10,(d,expected,harmonic))

# Verify the exact conditional mean/variance of the zero-truncated Poisson
# from its first two factorial moments at several relevant times.
for d in (5,100,10000):
    for offset in (-1.0,0.0,1.0):
        y=math.log(d)+offset
        if y<=0: continue
        q=math.exp(-y)
        mean=y/(1-q)
        var=y/(1-q)-y*y*q/(1-q)**2
        # direct summation of zero-truncated Poisson with stable probabilities
        pt=y/(math.expm1(y))
        masses=[]
        for k in range(1,150):
            masses.append((k,pt))
            pt*=y/(k+1)
        em=sum(k*p for k,p in masses)
        va=sum((k-mean)**2*p for k,p in masses)
        test(abs(em-mean)<1e-8,(d,y,'mean',em,mean))
        test(abs(va-var)<1e-8,(d,y,'variance',va,var))

# Numerical characteristic-function check for Poisson-time noise only.
# Gaussian-mixture limit has CF E exp(-t^2 E/2)=1/(1+t^2/2).
def cf_pois_center(n,z):
    ln=math.log(n)
    a=z/math.sqrt(ln)
    def f(u):
        if u<=0: return 0j
        y=math.log(n/u)
        q=(u/n)*y/(1-u/n)
        base=1+q*(cmath.exp(1j*a)-1)
        return (1-u/n)**(n-1)*cmath.exp(1j*a*(1-u*ln)) * cmath.exp((n-1)*cmath.log(base))
    hi=35.
    r=quad(lambda u:f(u).real,0,hi,epsabs=1e-8,limit=300)[0]
    im=quad(lambda u:f(u).imag,0,hi,epsabs=1e-8,limit=300)[0]
    return complex(r,im)
for z in (0.7,1.5):
    goal=1/(1+z*z/2)
    e1=abs(cf_pois_center(10000,z)-goal)
    e2=abs(cf_pois_center(1000000,z)-goal)
    test(e2<e1,(z,e1,e2))
    test(e2<0.25,(z,e2))

print('OK',checks,'finite exact and numerical assertions; infinite theorem proved separately')
