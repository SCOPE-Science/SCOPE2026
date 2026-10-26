#!/usr/bin/env python3
"""Exact arithmetic checks for a finite-population frequency-count covariance theorem.

Run: python verify.py  [writes stable JSON certificate to stdout]
"""
from itertools import combinations
from fractions import Fraction
from math import comb
import json


def hypergeo(B, r, n, m):
    if n > B+r or n<0 or m<0 or m>B or n-m<0 or n-m>r:
        return Fraction(0)
    return Fraction(comb(B,m)*comb(r,n-m),comb(B+r,n))

def covariance_formula(B,r,n):
    p1=hypergeo(B,r,n,1)
    p2=hypergeo(B,r,n,2)
    return p2*(Fraction(n*B,B+r)-2-p1)

def T(B,r,n):
    return Fraction(n*B,B+r)-2-hypergeo(B,r,n,1)

def covariance_by_histogram(B,r,n):
    # Aggregate every equally likely labeled n-subset; independent computation.
    # Label the dominant species 0 and the singleton species 1..r.
    pop=[0]*B+list(range(1,r+1))
    freq={}
    ex=ey=exy=0
    total=0
    for ix in combinations(range(len(pop)), n):
        c={}
        for j in ix:
            c[pop[j]]=c.get(pop[j],0)+1
        x=sum(v==1 for v in c.values())
        y=sum(v==2 for v in c.values())
        ex+=x;ey+=y;exy+=x*y;total+=1
    return Fraction(exy,total)-Fraction(ex*ey,total*total)

def sign(v):
    return (v>0)-(v<0)


def run():
    checks=0
    signs={"negative":0,"zero":0,"positive":0}
    examples={}
    # All labeled samples for modest finite populations; exact fractions throughout.
    for n in range(2,7):
        for r in range(max(1,n-1),8):
            for B in range(2,13-r):
                if B+r < n: continue
                a=covariance_formula(B,r,n)
                b=covariance_by_histogram(B,r,n)
                assert a==b,(B,r,n,a,b)
                checks+=1
                signs[{ -1:'negative',0:'zero',1:'positive'}[sign(a)]]+=1
    # Monotonicity of the sign-governing expression on a wide exact grid.
    monotonic=0
    thresholds={}
    for n in range(3,11):
        for r in range(n-1,45):
            ts=[T(B,r,n) for B in range(2,141)]
            assert all(ts[j+1]>ts[j] for j in range(len(ts)-1)),(n,r)
            assert ts[0]<0 and ts[-1]>0,(n,r)
            monotonic+=len(ts)-1
        for r in (n-1,10 if 10>=n-1 else n-1,30,100):
            k=next(B for B in range(2,1000) if T(B,r,n)>0)
            assert T(k-1,r,n)<=0 and T(k,r,n)>0
            thresholds[f'{n},{r}']=k
    for B in (2,5,6):
        cov=covariance_formula(B,2,3)
        examples[f'B={B},r=2,n=3']={'numerator':cov.numerator,'denominator':cov.denominator,'sign':sign(cov)}
    # Large-r finite-grid convergence is a sanity check, not a proof.
    import math
    qroots={}
    for n in (3,4,5,8,10):
        lo,hi=0.,1.
        for _ in range(75):
            q=(lo+hi)/2
            if n*q*(1-(1-q)**(n-1)) > 2: hi=q
            else: lo=q
        q=(lo+hi)/2
        qroots[str(n)]={'q':round(q,12),'B_over_r':round(q/(1-q),12)}
    return {
       'schema_version':1,
       'method':'independent exhaustive labeled-subset enumeration with exact rational fractions; hypergeometric formula cross-check; monotonic sign expression grid; real-root binary search only as approximation',
       'exhaustive_cases':checks,'exhaustive_covariance_sign_counts':signs,
       'monotonic_adjacent_pairs_checked':monotonic,
       'examples':examples,'first_positive_B_thresholds':thresholds,
       'fixed_n_large_r_limit_roots_approx':qroots,
       'logical_limit':'All-integer and limiting theorems require the accompanying paper proof; finite checks are not universal certification.'
    }

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,ensure_ascii=False,separators=(',',':')))
