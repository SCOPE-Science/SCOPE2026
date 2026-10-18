#!/usr/bin/env python3
"""Checks finite stationary law, Stirling partition identity, and finite-size critical slow-site asymptotics.
Requires Python 3 and NumPy. Finite Markov-generator checks use exact rational arithmetic.
"""
from fractions import Fraction
from math import factorial, log
import numpy as np


def comps(s, m):
    if m == 1:
        yield (s,)
    else:
        for a in range(s + 1):
            for rest in comps(s - a, m - 1):
                yield (a,) + rest

def wm_exact(s, m):
    return sum((Fraction(1, 1) / mult(c) for c in comps(s,m)), Fraction(0))

def mult(c):
    ans = 1
    for x in c: ans *= x+1
    return ans

def stirling_first(n,k):
    arr = [0]*(k+1); arr[0]=1
    for t in range(1,n+1):
        for j in range(min(t,k),0,-1):
            arr[j] = arr[j-1] + (t-1)*arr[j]
        arr[0]=0
    return arr[k]

def stationary_check(L, m, N, q):
    states=list(comps(N,L))
    weights={a:Fraction(1,1)*q**(-sum(a[:m]))/mult(a[:m]) for a in states}
    for a in states:
        rates=[(q*Fraction(x+1,x) if j<m else Fraction(1)) if x else Fraction(0) for j,x in enumerate(a)]
        flux=-weights[a]*sum(rates)
        for j in range(L):
            target=(j+1)%L
            if a[target]:
                b=list(a); b[j]+=1; b[target]-=1; b=tuple(b)
                rate=q*Fraction(b[j]+1,b[j]) if j<m else Fraction(1)
                flux+=weights[b]*rate
        assert flux==0,(a,flux)
    return len(states)

def wvals(s,m):
    w=np.arange(1,s+2,dtype=float)**-1
    a=np.array([1.0])
    for _ in range(m):
        a=np.convolve(a,w)[:s+1]
    return a

checks=0; balances=0
for L in range(4,7):
    for m in range(3,L):
        for N in range(0,5):
            for q in (Fraction(1,2),Fraction(2,3)):
                balances+=stationary_check(L,m,N,q); checks+=1
print('EXACT_GENERATOR_CASES',checks,'BALANCED_STATES',balances)

stirling_cases=0
for m in range(1,6):
    for s in range(0,14):
        lhs=wm_exact(s,m)
        rhs=Fraction(factorial(m)*stirling_first(s+m,m),factorial(s+m))
        assert lhs==rhs,(s,m,lhs,rhs)
        stirling_cases+=1
print('EXACT_STIRLING_IDENTITIES',stirling_cases)

# Independent direct enumeration checks conditional logarithmic exponents for m=3.
for s in (500,2000,8000):
    w3=wvals(s,3); norm=w3[s]
    ratio=norm/(3*log(s)**2/s)
    print('PARTITION_ASYMPTOTIC',s,ratio)
    # Pair-exceedance exact via convolution, inclusion/exclusion for m=3.
    a=int(np.ceil(.2*s)); w=1/(1+np.arange(s+1,dtype=float)); wlarge=w.copy(); wlarge[:a]=0
    wpair=np.convolve(wlarge,wlarge)[:s+1]
    two=np.dot(wpair,w[:s+1][::-1])/norm
    three=np.dot(wpair,wlarge[:s+1][::-1])/norm
    at_least_two=3*two-2*three
    coefficient=at_least_two*log(s)
    target=2*log(4.0)
    print('RARE_PAIR_COEFFICIENT',s,coefficient,'LIMIT',target)
    assert 0<at_least_two<1
    # Conditional J=0 and log minor thresholds t1,t2.
    for t1,t2 in ((.25,.4),(.5,.7),(.7,.75)):
        xmax=min(s,int(s**t1)); ymax=min(s,int(s**t2))
        total=0.0
        for x in range(xmax+1):
            y=np.arange(min(ymax,s-x)+1)
            total+=np.sum(1/(1+x)/(1+y)/(1+s-x-y))
        observed=total/norm
        expected=t1*t2/3
        print('LOG_PROFILE',s,t1,t2,observed,'LIMIT',expected)
print('ALL_FINITE_CHECKS_PASSED')
