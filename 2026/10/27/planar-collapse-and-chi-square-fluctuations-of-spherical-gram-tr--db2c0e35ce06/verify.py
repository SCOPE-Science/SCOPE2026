#!/usr/bin/env python3
"""Reproducible checks for spherical Gram triangle moment and fluctuation identities.

Stdlib-only; analytic derivation is given in RESULT.md. This file tests
finite algebra, tensor quadrature, and the planar pointwise identity.
"""
from fractions import Fraction as F
from math import comb, sqrt, cos, pi
from itertools import product
import random

class Q2:
    __slots__=('a','b')
    def __init__(self, a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o):
        if not isinstance(o,Q2): o=Q2(o)
        return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Q2(-self.a,-self.b)
    def __sub__(self,o):return self+-o if isinstance(o,Q2) else self+Q2(-o)
    def __rsub__(self,o):return -self+o
    def __mul__(self,o):
        if not isinstance(o,Q2):o=Q2(o)
        return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,int):return Q2(self.a/o,self.b/o)
        raise TypeError('only integer division required')
    def __eq__(self,o):
        if not isinstance(o,Q2):o=Q2(o)
        return self.a==o.a and self.b==o.b
    def __repr__(self):return f'({self.a})+({self.b})sqrt2'

# Circular octagon: dot products are exact Q(sqrt(2)) elements.
c=[Q2(1),Q2(0,F(1,2)),Q2(0),Q2(0,-F(1,2)),Q2(-1),Q2(0,-F(1,2)),Q2(0),Q2(0,F(1,2))]
def dot(i,j):return c[(i-j)%8]
def tri(i,j,k):return dot(i,j)*dot(i,k)*dot(j,k)

sum_t=Q2();sum_t2=Q2();sum_pair=Q2();sum_identity=Q2()
for i,j,k in product(range(8),repeat=3):
    h=tri(i,j,k)
    sum_t+=h;sum_t2+=h*h
    target=(dot(i,j)*dot(i,j)+dot(i,k)*dot(i,k)+dot(j,k)*dot(j,k)-1)/2
    assert h==target, ('planar rank-two identity',i,j,k,h,target)
assert sum_t/512==Q2(F(1,4))
assert sum_t2/512==Q2(F(5,32))
for i,j,k,l in product(range(8),repeat=4):
    sum_pair+=tri(i,j,k)*tri(i,j,l)
assert sum_pair/4096==Q2(F(3,32))
print('EXACT_PLANAR_OCTAGON: 512 triangle identities; 4096 shared-edge products')

# Direct fourth-moment tensor checks for twelve regular icosahedron points.
phi=(1+sqrt(5.0))/2
pts=[]
for a in (-1,1):
 for b in (-1,1):
  pts.extend([(0.,float(a),float(b)*phi), (float(a),float(b)*phi,0.), (float(b)*phi,0.,float(a))])
assert len(pts)==12
rad=sqrt(1+phi*phi)
pts=[tuple(t/rad for t in p) for p in pts]
def moment(*indices):return sum(__import__('math').prod(p[k] for k in indices) for p in pts)/12
for i in range(3):
 assert abs(moment(i,i)-F(1,3))<1e-15
 assert abs(moment(i,i,i,i)-F(1,5))<1e-15
 for j in range(3):
  if i==j:continue
  assert abs(moment(i,i,j,j)-F(1,15))<1e-15
  assert abs(moment(i,i,i,j))<1e-15
# These tensor identities certify the quadrature for all polynomials with
# coordinate degree at most four in each independently sampled point.
R=[[sum(pts[i][k]*pts[j][k] for k in range(3)) for j in range(12)] for i in range(12)]
s1=s2=sp=0.0
for a,b,c_ in product(range(12),repeat=3):
 h=R[a][b]*R[a][c_]*R[b][c_]
 s1+=h;s2+=h*h
for a,b,c_,e in product(range(12),repeat=4):
 sp+=R[a][b]**2*R[a][c_]*R[b][c_]*R[a][e]*R[b][e]
assert abs(s1/12**3 - 1/9)<1e-13
assert abs(s2/12**3 - F(11,225))<1e-13
assert abs(sp/12**4 - F(3,135))<1e-13,sp/12**4
print('ICOSAHEDRAL_QUADRATURE: exact design tensor conditions, 20736 four-point products')

# All-d rational identity checks and exact combinatorial overlap counts.
for d in range(2,25):
 A=F((d-1)*(d*d+8*d+4), d**4*(d+2)**2)
 c2=F(2*(d-1),d**4*(d+2))
 g3=F((d-2)*(d-1)*(d+4),d**4*(d+2)**2)
 assert A-3*c2==g3
 assert (g3==0)==(d==2)
 assert F(d+8,d*d*(d+2)**2)-F(1,d**4)==A
 for n in range(3,15):
  var=comb(n,3)*A+2*comb(n,2)*comb(n-2,2)*c2
  hoeffding=(n-2)**2*comb(n,2)*c2+comb(n,3)*g3
  assert var==hoeffding, (d,n,var,hoeffding)
print('RATIONAL_HOEFFDING: 23 dimensions x 12 sample sizes; strict residual dimension threshold')

# Empirical law check (supplemental and explicitly not an infinite proof).
# Fixed d=2, n=1000: T via Gram trace identity, avoiding O(n^3).
rng=random.Random(20261019)
def one(n):
 xx=xy=yy=0.0
 for _ in range(n):
  a=rng.random()*2*pi;x=cos(a);y=__import__('math').sin(a)
  xx+=x*x;xy+=x*y;yy+=y*y
 tr2=xx*xx+2*xy*xy+yy*yy
 tr3=xx**3+yy**3+3*(xx+yy)*xy*xy
 return (tr3-3*tr2+2*n)/6
n=500
xs=[(one(n)-comb(n,3)/4)/n**2 for _ in range(2200)]
mu=sum(xs)/len(xs)
var=sum((x-mu)**2 for x in xs)/len(xs)
assert abs(mu)<0.007,mu
# d=2 target: centered chi2_2/16, variance 4/256 = 1/64.
assert abs(var-F(1,64))<0.003,(mu,var)
print('SIMULATION_DIAGNOSTIC: n=500,d=2,replications=2200; mean',round(mu,6),'variance',round(var,6),'target variance 0.015625')
print('VERIFY_OK')
