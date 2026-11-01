#!/usr/bin/env python3
"""Finite consistency checks of the triangular reflection-depth formulas.

Numerical polygon clipping is separate from the analytic barycentric-overlap proof;
these finite checks are not a substitute for its universal argument.
"""
import math
import random
from fractions import Fraction

rng = random.Random(314159265)
TOL=5e-10


def clip_polygon(poly, a,b,c):
    # Keep a*x+b*y<=c; ordinary Sutherland-Hodgman clipping.
    if not poly: return []
    out=[]
    for P,Q in zip(poly,poly[1:]+poly[:1]):
        p=a*P[0]+b*P[1]-c
        q=a*Q[0]+b*Q[1]-c
        if p<=0: out.append(P)
        if (p<0 and q>0) or (p>0 and q<0):
            t=p/(p-q)
            out.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
        elif p==0 and q!=0: pass
    return out


def area(poly):
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly,poly[1:]+poly[:1])))/2 if len(poly)>=3 else 0.


def direct_fraction(b):
    # Barycentric coordinates: lambda=(1-x-y,x,y).
    poly=[(0.,0.),(1.,0.),(0.,1.)]
    poly=clip_polygon(poly,-1,-1,b[0]-1)
    poly=clip_polygon(poly,1,0,b[1])
    poly=clip_polygon(poly,0,1,b[2])
    return 2*area(poly)


def formula_fraction(b):
    if min(b)<0: return 0.
    return sum(((-1)**len(S))*max(0.,1-sum(b[i] for i in S))**2
               for S in ((),(0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2)))


def F(s):
    if s<=0 or s>=2:return 0.
    return 2*s-1.5*s*s if s<=1 else .5*(2-s)**2


def depth(lam):
    L=max(lam)
    t=min(L,2/3)
    return 1-2*t+1.5*t*t


def level(alpha):
    return (2-math.sqrt(6*alpha-2))/3

# Exact rational branch calculations.
for k in range(151):
    s=Fraction(k,100)
    b=(s,(2-s)/2,(2-s)/2)
    m=sum((-1)**len(S)*max(Fraction(0),1-sum(b[i] for i in S))**2
          for S in ((),(0,),(1,),(2,),(0,1),(0,2),(1,2),(0,1,2)))
    expected=2*s-Fraction(3,2)*s*s if s<=1 else (2-s)**2/2
    assert m==expected, (k,m,expected)
assert abs(F(Fraction(2,3))-float(Fraction(2,3)))<1e-13
assert depth([Fraction(1,3)]*3)==Fraction(1,2)
assert abs(depth([1,0,0])-float(Fraction(1,3)))<1e-13
assert level(Fraction(3,8))==0.5
count=154

# Compare the independent polygon clipping to inclusion-exclusion on random shifts.
for z in range(4500):
    u=rng.uniform(-0.6,1.6);v=rng.uniform(-0.6,1.6)
    b=(2-u-v,u,v)
    got=direct_fraction(b)
    expected=formula_fraction(b)
    assert abs(got-expected)<TOL,(b,got,expected)
    count+=1

# Check globally bounded mass of every translated reversed test triangle
# missing y, including y outside the original triangle.
for z in range(6500):
    x,y=rng.uniform(-0.8,1.8),rng.uniform(-0.8,1.8)
    lam=(1-x-y,x,y)
    b1=rng.uniform(-0.6,1.6);b2=rng.uniform(-0.6,1.6)
    b=(2-b1-b2,b1,b2)
    if any(b[i]<lam[i] for i in range(3)):
        val=direct_fraction(b)
        assert val<=1-depth(lam)+TOL, (lam,b,val,depth(lam))
    count+=1

# Explicit near-optimal excluded translates; compare direct clipped area
# to the bound by letting an active cap approach the target barycentric value.
for z in range(1200):
    x,y=rng.uniform(-.3,1.3),rng.uniform(-.3,1.3)
    lam=(1-x-y,x,y)
    t=min(max(lam),2/3)
    s=t-1e-7
    b=[(2-s)/2]*3
    j=lam.index(max(lam));b[j]=s
    assert abs(sum(b)-2)<1e-13
    assert b[j]<lam[j]
    val=direct_fraction(tuple(b))
    assert abs(val-(1-depth(lam)))<5e-7,(lam,val,depth(lam))
    count+=1

# Exact level shape and area: reversed similarity; intersection fraction via
# an independent inclusion-exclusion integration of the uniform simplex.
for i in range(1,999):
    alpha=1/3+i*(1/2-1/3)/1000
    u=level(alpha)
    assert abs(depth((u,u,1-2*u))-alpha)<1e-9
    s=3*u-1
    pr=1-3*(1-u)**2+3*max(0,1-2*u)**2
    if u<=0.5: assert abs(pr-s*s)<1e-9
    else: assert abs(pr-(1-3*(1-u)**2))<1e-9
    count+=1

print(f'PASS: {count} deterministic exact/numerical consistency checks')
