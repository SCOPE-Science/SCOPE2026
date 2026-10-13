#!/usr/bin/env python3
"""Exact-rational verification of a two-dimensional affine SDCG example."""
from fractions import Fraction as Q

def add(u,v): return (u[0]+v[0],u[1]+v[1])
def neg(u): return (-u[0],-u[1])
def scale(c,u): return (c*u[0],c*u[1])
def dot(u,v): return u[0]*v[0]+u[1]*v[1]
def mul(A,v): return (A[0][0]*v[0]+A[0][1]*v[1],A[1][0]*v[0]+A[1][1]*v[1])
def solve(A,v):
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert det>0 and A[0][0]>0
    return ((A[1][1]*v[0]-A[0][1]*v[1])/det,(-A[1][0]*v[0]+A[0][0]*v[1])/det)

A=((Q(99,100),Q(3)),(Q(3),Q(999,100)))
g0=(-Q(1),-Q(300,251)); x0=solve(A,g0); d0=neg(g0)
alpha=Q(2,25); sigma=Q(3,10); kappa=Q(1); r=Q(1,100); xi1=Q(1,100)
z0=add(x0,scale(alpha,d0)); Fz=mul(A,z0)
assert Fz==(-Q(198901,313750),Q(0))
# The line-search trial is the first (largest) trial, so strict acceptance is enough.
assert -dot(Fz,d0)>0
assert (-dot(Fz,d0))**2 > (sigma*alpha*dot(d0,d0))**2*dot(Fz,Fz)
lam=dot(Fz,add(x0,neg(z0)))/dot(Fz,Fz)
assert lam==Q(25100,198901)
x1=add(x0,scale(-kappa*lam,Fz))
s=add(x1,neg(x0)); g1=mul(A,x1)
y=add(add(g1,neg(g0)),scale(r,s))
assert s==(Q(2,25),Q(0))
assert g1==(-Q(1151,1250),-Q(5994,6275))
assert y==(Q(2,25),Q(6,25))
assert dot(s,y)-xi1*dot(y,y)==Q(18,3125)>0
assert y==add(mul(A,s),scale(r,s))
a=(dot(g1,y)-dot(g1,s))/dot(s,y)
d1=add(neg(g1),scale(a,s))
assert a==-Q(8991,251)
assert d1==(-Q(610199,313750),Q(5994,6275))
assert dot(g1,d1)==Q(86467011299,98439062500)>0
assert dot(d1,mul(A,d1))>0
assert dot(g0,g0)>Q(1,1000)**2
assert dot(g1,g1)>Q(1,1000)**2
print('VERIFY_OK')
