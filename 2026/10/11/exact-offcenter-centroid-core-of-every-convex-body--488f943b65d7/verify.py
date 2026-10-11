#!/usr/bin/env python3
"""Supplementary exact checks for the offcenter centroid core theorem."""
from fractions import Fraction as F
from math import factorial
import sympy as s
v,lam,a,b=s.symbols('v lam a b',positive=True)
for n in (2,3,4,5):
    f=(lam+(1-lam)*v)**(n-1)
    den=s.integrate(f,(v,0,1))
    num=s.integrate(v*f,(v,0,1))
    m=-b+(a+b)*num/den
    assert s.simplify(s.limit(m,lam,0,dir='+')-(n*a-b)/(n+1))==0
    assert s.simplify(s.limit(m,lam,s.oo)-(a-n*b)/(n+1))==0
# Affine triangle with centroid 0: vertices (2,0),(-1,1),(-1,-1).
# Uniform affine map from equilateral model preserves area ratios.
tri=[(F(2),F(0)),(F(-1),F(1)),(F(-1),F(-1))]
scaled=[(2*x/3,2*y/3) for x,y in tri]
hex_pts=[((p[0]-q[0])/3,(p[1]-q[1])/3) for p in tri for q in tri]
points=sorted(set(scaled+hex_pts))
def cross(o,p,q):return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])
lo=[]
for p in points:
    while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
    lo.append(p)
hi=[]
for p in reversed(points):
    while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
    hi.append(p)
hull=lo[:-1]+hi[:-1]
def area(poly):return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2
assert len(hull)==9
assert area(hull)/area(tri)==F(7,9)
hex_hull=sorted(set(hex_pts))
low=[]
for p in hex_hull:
    while len(low)>1 and cross(low[-2],low[-1],p)<=0:low.pop()
    low.append(p)
high=[]
for p in reversed(hex_hull):
    while len(high)>1 and cross(high[-2],high[-1],p)<=0:high.pop()
    high.append(p)
hex_boundary=low[:-1]+high[:-1]
assert len(hex_boundary)==6
assert area(hex_boundary)/area(tri)==F(2,3)
print('OFFCENTER_CORE_CHECKS_OK')
