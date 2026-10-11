#!/usr/bin/env python3
from fractions import Fraction as F
from math import sqrt, pi, sin, cos, tan, atan

class Q5:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q5) else Q5(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Q5) else Q5(o)))
    def __rsub__(self,o): return Q5(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q5) else Q5(o)
        return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,Q5): return Q5(self.a/F(o),self.b/F(o))
        den=o.a*o.a-5*o.b*o.b
        return Q5((self.a*o.a-5*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=o if isinstance(o,Q5) else Q5(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return f'Q5({self.a},{self.b})'
    def val(self): return float(self.a)+float(self.b)*sqrt(5)

phi=Q5(F(1,2),F(1,2))
zero=Q5(0)
half=Q5(F(1,2))
verts=[]
for a in (-1,1):
    for b in (-1,1):
        verts += [
            (zero,Q5(F(a,2)),phi*F(b,2)),
            (Q5(F(a,2)),phi*F(b,2),zero),
            (phi*F(a,2),zero,Q5(F(b,2))),
        ]
# all 12 are distinct under exact coordinates
keys={(v[0].a,v[0].b,v[1].a,v[1].b,v[2].a,v[2].b) for v in verts}
assert len(keys)==12

def dot(x,y): return sum((x[i]*y[i] for i in range(3)),Q5(0))
def sub(x,y): return tuple(x[i]-y[i] for i in range(3))
R2=dot(verts[0],verts[0])
assert R2==Q5(F(5,8),F(1,8))
# unit-edge graph: exactly 30 pairs at squared distance 1, degree 5.
deg=[0]*12; edges=0
for i in range(12):
    for j in range(i+1,12):
        d2=dot(sub(verts[i],verts[j]),sub(verts[i],verts[j]))
        if d2==1:
            edges+=1; deg[i]+=1; deg[j]+=1
assert edges==30 and deg==[5]*12
# For an adjacent pair, v.v' = R^2-1/2, so sin^2(delta)=1/(4R^2).
sin2d=Q5(F(1,2),F(-1,10))  # (5-sqrt(5))/10
cos2d=Q5(F(1,2),F(1,10))   # (5+sqrt(5))/10
assert sin2d+cos2d==1
assert (R2*4)*sin2d==1
# sin^2(pi/5)=(5-sqrt(5))/8; product with cos^2(delta)=1/4.
sin2a=Q5(F(5,8),F(-1,8))
assert sin2a*cos2d==Q5(F(1,4))
# Therefore sin(alpha) cos(delta)=1/2 (all quantities positive).
# The exact cell calculation gives I_C=pi/9 + 10 sin^2(delta)/(3 sqrt(3)).
# Combining E[w^2]=(12 R^2/pi) I_C and 4 R^2 sin^2(delta)=1 yields
# E[w^2]=(4/3)R^2 + 10/(pi sqrt(3)). Check the algebraic first term.
assert R2*F(4,3)==Q5(F(5,6),F(1,6))
target=(5+sqrt(5))/6 + 10*sqrt(3)/(3*pi)
# Independent deterministic midpoint quadrature over the five spherical sectors.
delta=asin_delta=__import__('math').asin(1/(2*sqrt(R2.val())))
alpha=pi/5
N=200000
acc=0.0
for k in range(N):
    psi=-alpha+(2*alpha)*(k+0.5)/N
    th=atan(tan(delta)/cos(psi))
    acc += (1-cos(th)**3)/3
Icell=5*(2*alpha/N)*acc
quad=12*R2.val()/pi*Icell
assert abs(quad-target)<2e-10, (quad,target)
print('VERIFY_OK')
print('vertices=12 edges=30 degree=5 exact')
print('R2=(5+sqrt(5))/8')
print('sin2_delta=(5-sqrt(5))/10')
print('sin(pi/5)*cos(delta)=1/2')
print('mean_square_width=',repr(target))
