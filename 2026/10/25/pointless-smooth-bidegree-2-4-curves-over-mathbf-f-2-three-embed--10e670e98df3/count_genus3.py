#!/usr/bin/env python3
"""Exact GF(2) genus-three bidegree-(2,4) smoothness and p-rank census.
Polynomials use bit i for coefficient of x**i.  Coordinates are
[s:t] on first P1 and [u:v] on second P1, with x=u/v.
All computations use Python integer arithmetic without external dependencies.
"""
from collections import Counter
import json

def mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1;b>>=1
    return r

def deriv(a):
    return sum(1<<(i-1) for i in range(1,a.bit_length(),2) if (a>>i)&1)

def degree(a):return a.bit_length()-1

def rem(a,b):
    if b==0:raise ZeroDivisionError
    d=degree(b)
    while a and degree(a)>=d:a^=b<<(degree(a)-d)
    return a

def gcd(a,b):
    while b:a,b=b,rem(a,b)
    return a

IRREDS=(2,3,7,11,13,19,25,31)
assert [degree(x) for x in IRREDS]==[1,1,2,3,3,4,4,4]

def distinct_geometric_roots(b):
    assert b
    return (int(not ((b>>4)&1))+
            sum(degree(q) for q in IRREDS if rem(b,q)==0))

def smooth(a,b,c):
    if b==0:return False
    # On affine base chart v != 0: derivative in x=u/v.
    # Unique root in [s:t] over each geometric root of b.
    ac=mul(a,c)
    e=mul(deriv(a),c)^mul(a,deriv(c))
    delta=mul(e,e)^mul(mul(deriv(b),deriv(b)),ac)
    if gcd(b,delta)!=1:return False
    # At infinity, z=v/u; derivative at z=0 is coefficient of u**3*v.
    if not ((b>>4)&1):
        a4,c4=(a>>4)&1,(c>>4)&1
        a3,c3,b3=(a>>3)&1,(c>>3)&1,(b>>3)&1
        if not ((a3&c4)^(a4&c3)^(b3&a4&c4)):
            return False
    return True

def rational_points(a,b,c):
    ans=0
    for mask in [1,31,16]:
        def ev(f):return (f&mask).bit_count()&1
        av,bv,cv=ev(a),ev(b),ev(c)
        if bv==0:
            assert av or cv
            ans+=1
        else:ans+=(0 if av and cv else 2)
    return ans

def main():
    counts=Counter(); total=0
    for a in range(32):
        for b in range(1,32):
            r=distinct_geometric_roots(b)-1
            assert r in (0,1,2,3)
            for c in range(32):
                if not smooth(a,b,c):continue
                total+=1
                counts[(r,rational_points(a,b,c))]+=1
    result={'count':total,'joint':[{ 'p_rank':f,'points':n,'count':counts[(f,n)] }
       for f in range(4) for n in range(7) if counts[(f,n)]]}
    print(json.dumps(result,sort_keys=True,indent=2))
    assert sum(counts.values())==total
if __name__=='__main__':main()
