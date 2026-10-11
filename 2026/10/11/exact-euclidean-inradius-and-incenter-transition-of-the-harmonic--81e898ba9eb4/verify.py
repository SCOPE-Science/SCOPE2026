#!/usr/bin/env python3
from fractions import Fraction
import math

checks=0
for n in range(3,201):
    mu=Fraction(n+1,2)+Fraction(1,n)
    target2=Fraction((n*n-n+2)**2,4*n*(n-1))
    active=[]
    for s in range(1,n+1):
        for t in range(1,n+1):
            if s+t<n or (s==n and t==n):
                continue
            slack=mu*(s+t)-Fraction(s*(s+1)+t*(t+1),2)-1
            norm2=Fraction(s*(n-s)+t*(n-t),n)
            assert norm2>0
            dist2=slack*slack/norm2
            assert dist2>=target2,(n,s,t,dist2,target2)
            if dist2==target2:
                active.append((s,t))
            checks+=1
    assert set(active)=={(1,n),(n,1)},(n,active)

# Rank two: parameter x=(2+p,2-p), y=(2+q,2-q).
# At radius one, opposite diagonal facets force p=q, and
# coordinate facets give |p| <= 1-1/sqrt(2).
bound=1-1/math.sqrt(2)
for p in [-bound, -bound/2, 0.0, bound/2, bound]:
    q=p
    distances=[
        math.sqrt(2)*(1+p),
        math.sqrt(2)*(1-p),
        math.sqrt(2)*(1+q),
        math.sqrt(2)*(1-q),
        1+p-q,
        1-p+q,
    ]
    assert min(distances)>=1-1e-12
    assert abs(min(distances)-1)<1e-12

# Outside the segment along p=q, a coordinate facet is closer than one.
for p in [bound+0.01, -bound-0.01]:
    q=p
    distances=[
        math.sqrt(2)*(1+p),
        math.sqrt(2)*(1-p),
        math.sqrt(2)*(1+q),
        math.sqrt(2)*(1-q),
        1+p-q,
        1-p+q,
    ]
    assert min(distances)<1

print(f"VERIFY_OK harmonic-polytope-inradius cardinality_checks={checks} n=3..200 rank2=exact")
