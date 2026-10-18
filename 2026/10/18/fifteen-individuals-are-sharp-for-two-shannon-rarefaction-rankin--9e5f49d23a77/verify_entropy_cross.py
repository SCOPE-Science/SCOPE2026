#!/usr/bin/env python3
"""Exact certificate for two-crossing plug-in Shannon entropy rarefaction.

Uses integer combinatorics and certified rational bounds for logarithms.
Requires Python 3 standard library only; no floating-point operations in classification.
"""
from fractions import Fraction
from functools import lru_cache
from collections import Counter
from itertools import combinations
from math import comb, log

MAX_N=15
SCALE=10**36
TERMS=400
PRIMES=(2,3,5,7,11,13)


def log_interval(k):
    """Integer-scale enclosure of natural log(k), rigorously via atanh."""
    x=Fraction(k-1,k+1)
    p=x
    tot=Fraction(0)
    for j in range(TERMS):
        tot += 2*p/(2*j+1)
        p *= x*x
    rem=2*p/((2*TERMS+1)*(1-x*x))
    lo=tot.numerator*SCALE//tot.denominator
    upper=tot+rem
    hi=-(-upper.numerator*SCALE//upper.denominator) # ceil
    assert lo<=hi and hi-lo<=2, (k,hi-lo)
    return lo,hi

LOGS={p:log_interval(p) for p in PRIMES}


def factors(j):
    if j==1:return (0,)*len(PRIMES)
    return _factor(j)

@lru_cache(None)
def _factor(j):
    vec=[]
    for p in PRIMES:
        e=0;t=j
        while t%p==0:
            e+=1;t//=p
        vec.append(e)
    prod=1
    for p,e in zip(PRIMES,vec):prod*=p**e
    assert prod==j
    return tuple(vec)

@lru_cache(None)
def partitions(n,least=1):
    if n==0:return ((),)
    return tuple((a,)+rest for a in range(least,n+1)
                 for rest in partitions(n-a,a))

@lru_cache(None)
def one_species_vec(n,a,m):
    # Numerator of E[(J/m)log J], with common denominator m*comb(n,m).
    out=[0]*len(PRIMES)
    for j in range(2,min(a,m)+1):
        if not 0<=m-j<=n-a:continue
        w=j*comb(a,j)*comb(n-a,m-j)
        for k,e in enumerate(factors(j)):out[k]+=w*e
    return tuple(out)

@lru_cache(None)
def profile_vec(n,profile,m):
    v=[0]*len(PRIMES)
    for a in profile:
        u=one_species_vec(n,a,m)
        for k in range(len(PRIMES)):v[k]+=u[k]
    return tuple(v)


def sign_integer_log_combo(v):
    if not any(v):return 0
    lo=sum(c*(LOGS[p][0] if c>=0 else LOGS[p][1])
           for p,c in zip(PRIMES,v))
    hi=sum(c*(LOGS[p][1] if c>=0 else LOGS[p][0])
           for p,c in zip(PRIMES,v))
    if lo>0:return 1
    if hi<0:return -1
    raise AssertionError(('sign enclosure unresolved',v,lo,hi))


def compare(n,a,b,m):
    # H_a - H_b: log(m) terms cancel, leaving T_b - T_a.
    va,vb=profile_vec(n,a,m),profile_vec(n,b,m)
    return sign_integer_log_combo(tuple(z-y for y,z in zip(va,vb)))


def classification():
    report=[]; candidates=[]
    for n in range(2,MAX_N+1):
        pp=[x for x in partitions(n) if len(x)>=2]
        byrich={r:[x for x in pp if len(x)==r] for r in range(2,n+1)}
        tally=Counter(); npairs=0
        for r in range(2,n+1):
            for a,b in combinations(byrich[r],2):
                npairs+=1
                signs=[compare(n,a,b,m) for m in range(2,n+1)]
                nonzero=[s for s in signs if s]
                crossings=sum(u!=v for u,v in zip(nonzero,nonzero[1:]))
                tally[crossings]+=1
                if crossings>=2:candidates.append((n,a,b,crossings,tuple(signs)))
        report.append((n,len(pp),npairs,dict(sorted(tally.items()))))
    return report,candidates


def direct_entropy(profile,m):
    import itertools
    labels=[i for i,a in enumerate(profile) for _ in range(a)]
    n=len(labels);total=0.0
    for sel in combinations(range(n),m):
        cc=Counter(labels[i] for i in sel)
        total += -sum((x/m)*log(x/m) for x in cc.values())
    return total/comb(n,m)


def h_float(profile,m):
    n=sum(profile)
    base=log(m)
    vv=profile_vec(n,profile,m)
    return base-sum(c*log(p) for c,p in zip(vv,PRIMES))/(m*comb(n,m))

if __name__=='__main__':
    r,c=classification()
    for row in r:print('census',row)
    print('crossing candidates',len(c));print('candidates',c)
    assert len(c)==1
    n,a,b,num,signs=c[0]
    assert n==15 and a==(1,1,4,4,5) and b==(2,2,2,2,7) and num==2
    assert signs[:9]==(1,)*9 and signs[9:13]==(-1,)*4 and signs[13:]==(1,)
    for m in range(2,16):
        print('witness',m,compare(n,a,b,m),f'{h_float(a,m)-h_float(b,m):+.12f}')
    for profile in (a,b):
        for m in (2,3,5,10,11,13,14,15):
            d=direct_entropy(profile,m)
            v=h_float(profile,m)
            assert abs(v-d)<1e-12,(profile,m,v,d)
    print('DIRECT_SUBSET_CROSSCHECK PASS')
    print('CERTIFIED_COMPLETE_CLASSIFICATION PASS')
