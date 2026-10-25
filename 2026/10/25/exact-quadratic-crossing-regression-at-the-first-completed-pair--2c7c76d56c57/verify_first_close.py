#!/usr/bin/env python3
"""Direct exact enumeration of early-pair completion and crossings in random matchings."""
from collections import defaultdict
from fractions import Fraction
from math import factorial

def double_fact_odd(k):
    x=1
    for j in range(k,0,-2):x*=j
    return x

def matchings(points):
    if not points:
        yield ()
        return
    a=points[0]
    for idx in range(1,len(points)):
        b=points[idx]
        remain=points[1:idx]+points[idx+1:]
        for tail in matchings(remain):yield ((a,b),)+tail

def moment_regression(n,t):
    return Fraction(n*(n-3),6)+Fraction((t-1)*(t+2),12)

def survivor(n,t):
    if t < 2:return Fraction(1)
    x=Fraction(1)
    for s in range(2,t+1):x*=Fraction(2*(n-s+1),2*n-s+1)
    return x

def check(n):
    cnt=defaultdict(int); total=0; sumx=0
    for pairs in matchings(tuple(range(1,2*n+1))):
        t=min(b for a,b in pairs)
        x=sum(1 for i,(a,b) in enumerate(pairs) for c,d in pairs[i+1:] if (a<c<b<d) or (c<a<d<b))
        cnt[t,x]+=1;total+=1;sumx+=x
    assert total==double_fact_odd(2*n-1),(n,total)
    assert Fraction(sumx,total)==Fraction(n*(n-1),6)
    for t in range(2,n+2):
        denom=sum(v for (tt,xx),v in cnt.items() if tt==t)
        numer=sum(xx*v for (tt,xx),v in cnt.items() if tt==t)
        assert denom>0
        assert Fraction(numer,denom)==moment_regression(n,t),(n,t,Fraction(numer,denom),moment_regression(n,t))
        surv=Fraction(sum(v for (tt,xx),v in cnt.items() if tt>t),total)
        assert surv==survivor(n,t),(n,t,surv,survivor(n,t))
        if t<=n:
            condnum=sum(xx*v for (tt,xx),v in cnt.items() if tt>t)
            condtot=sum(v for (tt,xx),v in cnt.items() if tt>t)
            assert Fraction(condnum,condtot)==Fraction(n*(n-1),6)+Fraction(t*(t-1),12)
    et=Fraction(sum(tt*v for (tt,xx),v in cnt.items()),total)
    ex=Fraction(sum(xx*v for (tt,xx),v in cnt.items()),total)
    etx=Fraction(sum(tt*xx*v for (tt,xx),v in cnt.items()),total)
    cv=etx-et*ex
    assert cv>0
    print(f'n={n}, matchings={total}, regression_points={n}, cov(T,X)={cv}')

if __name__=='__main__':
    for n in range(2,8):check(n)
    print('All exact tests passed')
