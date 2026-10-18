#!/usr/bin/env python3
"""Exact enumeration test for joint simple-chord / crossing moment identity.
Stdlib only, no external data. This is corroboration, not a proof at unbounded size.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial
from itertools import combinations

def matchings(points):
    if not points:
        yield ()
        return
    a=points[0]
    for j in range(1,len(points)):
        b=points[j]
        for tail in matchings(points[1:j]+points[j+1:]):
            yield ((a,b),)+tail

def dist(n):
    c=Counter()
    for m in matchings(tuple(range(2*n))):
        x=sum(a<c_<b<d or c_<a<d<b for i,(a,b) in enumerate(m) for (c_,d) in m[i+1:])
        s=sum((b-a==1 or (a==0 and b==2*n-1)) for a,b in m)
        c[(x,s)]+=1
    return c

def odd_double(m):
    z=1
    for j in range(1,m+1,2): z*=j
    return z

def ak(n,k):
    if k==0:return Fraction(1)
    matching_k=Fraction(2*n,2*n-k)*comb(2*n-k,k)
    number_ordered=factorial(k)*matching_k
    denominator=1
    for j in range(k): denominator*=2*n-2*j-1
    return Fraction(number_ordered,denominator)

def check():
    checks=0
    ds={0:Counter({(0,0):1}),1:Counter({(0,1):1})}
    for n in range(2,7):
        counts=ds[n]=dist(n)
        denom=odd_double(2*n-1)
        assert sum(counts.values())==denom
        p=Counter({(x,s):Fraction(v,denom) for (x,s),v in counts.items()})
        xdist=Counter()
        for (x,s),v in p.items():xdist[x]+=v
        ex=sum(Fraction(x)*v for x,v in xdist.items())
        varx=sum((x-ex)**2*v for x,v in xdist.items())
        es=sum(Fraction(s)*v for (x,s),v in p.items())
        vars=sum((s-es)**2*v for (x,s),v in p.items())
        cov=sum((x-ex)*(s-es)*v for (x,s),v in p.items())
        assert ex==Fraction(n*(n-1),6)
        assert varx==Fraction(n*(n-1)*(n+3),45)
        assert es==Fraction(2*n,2*n-1)
        assert vars==Fraction(4*n*(n-1),(2*n-1)**2)
        assert cov==-Fraction(2*n*(n-1),3*(2*n-1))
        checks+=5
        for k in range(n+1):
            left=Counter()
            for (x,s),prob in p.items():
                if s>=k:
                    left[x]+=prob*Fraction(factorial(s),factorial(s-k))
            r=ak(n,k)
            right_count=ds[n-k] if n-k<2 else ds[n-k]
            right_total=odd_double(2*(n-k)-1) if n-k>0 else 1
            for x in set(left)|{v for v,_ in right_count}:
                right=r*Fraction(sum(z for (v,s),z in right_count.items() if v==x),right_total)
                assert left[x]==right,(n,k,x,left[x],right)
                checks+=1
        print('n',n,'matchings',denom,'moments & all factorial-crossing laws OK')
    for n in range(2,9):
        for k in range(n+1):
            num=0
            for starts in combinations(range(2*n),k):
                used=set()
                possible=True
                for a in starts:
                    b=(a+1)%(2*n)
                    if a in used or b in used:
                        possible=False
                        break
                    used.update((a,b))
                if possible:num+=1
            formula=Fraction(2*n,2*n-k)*comb(2*n-k,k)
            assert num==formula,(n,k,num,formula)
            checks+=1
    print('OK checks',checks)

if __name__=='__main__': check()
