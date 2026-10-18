"""Exact arithmetic checks for the middle-cohomology lattice of a Grassmannian linear section.

Run: python3 checker.py
No third-party packages are required. Mathematical topology theorems cited in
RESULT.md are premises of the proof, not certified by this computation.
"""
from fractions import Fraction as F
from math import gcd, isclose, pi, sqrt
import cmath

# Bivariate polynomial arithmetic over the rational numbers.
def mon(i,j,c=1):
    return {(i,j):F(c)}
def add(*polys):
    out={}
    for p in polys:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def scale(p,c):
    return {k:v*F(c) for k,v in p.items() if v*c}
def mul(p,q):
    out={}
    for (i,j),v in p.items():
        for (a,b),w in q.items():out[(i+a,j+b)]=out.get((i+a,j+b),F(0))+v*w
    return {k:v for k,v in out.items() if v}
def power(p,n):
    z=mon(0,0)
    for _ in range(n):z=mul(z,p)
    return z
x=mon(1,0); y=mon(0,1); h=add(x,y); delta=add(x,scale(y,-1))
s2=add(power(x,2),mul(x,y),power(y,2));s11=mul(x,y)
# For degree-12 symmetric f, integrate on Gr(2,8): [x^7 y^6](x-y)f.
def integrate(p):
    z=mul(delta,p)
    return z.get((7,6),F(0))
ch2=scale(add(scale(add(power(x,2),power(y,2)),8),scale(power(delta,2),-2),scale(power(h,2),-8)),F(1,2))
ch4=scale(add(scale(add(power(x,4),power(y,4)),8),scale(power(delta,4),-2),scale(power(h,4),-8)),F(1,24))
c2=scale(ch2,-1)
c4=add(scale(power(ch2,2),F(1,2)),scale(ch4,-6))
intX=lambda p:integrate(mul(power(h,8),p))
G=((intX(mul(s2,s2)),intX(mul(s2,s11))),
   (intX(mul(s11,s2)),intX(mul(s11,s11))))
assert G==((62,28),(28,14)), G
det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
assert det==84
assert gcd(*[int(G[i][j]) for i in range(2) for j in range(2)])==2
assert integrate(power(h,12))==132
assert c2==add(s2,scale(s11,5))
chi=intX(c4); c2sq=intX(power(c2,2))
assert (chi,c2sq)==(636,692)
signature=(3*c2sq+14*chi)/45
assert signature==244
b4=chi-4
assert b4==632
assert (b4+signature)//2==438 and (b4-signature)//2==194
assert signature%8==4 and c2sq%8==4
# A=span(sigma_2,sigma_11); c2=(1,5). The discriminant form of
# its orthogonal complement is q(u,v) = u+5v -(u,v)G^{-1}(u,v)^t (mod 2).
def qK(u,v):
    return F(u+5*v)-F(14*u*u-56*u*v+62*v*v,84)
# HNF of GZ^2 has column generators (6,0),(4,14).
for u in range(6):
 for v in range(14):
    assert (qK(u+6,v)-qK(u,v)).denominator==1
    assert (qK(u+6,v)-qK(u,v)).numerator%2==0
    assert (qK(u+4,v+14)-qK(u,v)).denominator==1
    assert (qK(u+4,v+14)-qK(u,v)).numerator%2==0
S=sum(cmath.exp(1j*pi*float(qK(u,v))) for u in range(6) for v in range(14))
assert abs(S-1j*sqrt(84))<1e-10, S
print('PASS: Plucker degree=132; Gram=((62,28),(28,14)); det=84; Smith=(2,42)')
print('PASS: Euler=636; c2^2=692; signature=244; H4 rank=632; inertia=(438,194)')
print('PASS: characteristic square/signature congruent mod 8; 84-class Gauss sum i*sqrt(84)')
print('LIMIT: integrality, primitive embedding, torsion-freeness, Wu and lattice uniqueness use cited theorems.')
