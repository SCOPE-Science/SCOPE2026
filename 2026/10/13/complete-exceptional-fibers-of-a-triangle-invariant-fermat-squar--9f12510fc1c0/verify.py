#!/usr/bin/env python3
"""Exact characteristic-dependent point and polynomial checks for a Fermat pullback pencil.

The main theorem is proved algebraically; these tests audit small finite fields.
"""
import itertools
import sympy as sp

A,B,C=sp.symbols('A B C')
assert sp.expand((A+B+C)*(-A+B+C)*(A-B+C)*(A+B-C) - (4*(A*A*B*B+B*B*C*C+C*C*A*A)-(A*A+B*B+C*C)**2)) == 0
u,v,w=sp.symbols('u v w')
assert sp.expand((u+v+w)**2-3*(u*v+v*w+w*u) - (u*u+v*v+w*w-u*v-v*w-w*u))==0
omega=sp.symbols('omega')
prod=(u+omega*v+omega**2*w)*(u+omega**2*v+omega*w)
red=sp.rem(sp.expand(prod - (u*u+v*v+w*w-u*v-v*w-w*u)),omega**2+omega+1,omega)
assert sp.expand(red)==0
for m in range(2,42):
 assert (2*m-1)*(2*m-2)//2 - ((m-1)*(m-2)//2) == 3*m*(m-1)//2
for h in range(1,22):
 m=2*h
 assert (2*m-1)*(2*m-2)//2 == 4*((h-1)*(h-2)//2)+6*h*h-3
 assert (2*m-1)*(2*m-2)//2 == 2*((m-1)*(m-2)//2)+m*m-1

class Field:
 def __init__(self,p,e=1,modpoly=None):
  self.p=p; self.e=e; self.q=p**e; self.modpoly=modpoly
  if e>1: assert p==2 and modpoly is not None
 def plus(self,a,b):
  if self.e==1:return (a+b)%self.p
  return a^b
 def neg(self,a):
  if self.p==2:return a
  return (-a)%self.p
 def mul(self,a,b):
  if self.e==1:return (a*b)%self.p
  r=0; aa=a; bb=b
  while bb:
   if bb&1:r^=aa
   bb>>=1; aa<<=1
   if aa & self.q: aa^=self.modpoly
  return r
 def pow(self,a,k):
  r=1
  while k:
   if k&1:r=self.mul(r,a)
   a=self.mul(a,a); k>>=1
  return r
 def div(self,a,b):
  assert b
  return self.mul(a,self.pow(b,self.q-2))
 def int(self,n):return n%self.p
 def sub(self,a,b):return self.plus(a,self.neg(b))

def singles(k):
 xs=range(k.q)
 for x in xs:
  for y in xs:yield x,y,1
 for x in xs:yield x,1,0
 yield 1,0,0

def sing(k,lam):
 m=k.q-1; zero=0; one=1; two=k.int(2)
 out=[]
 for xyz in singles(k):
  a,b,c=[k.pow(x,m) for x in xyz]
  s=k.plus(k.plus(a,b),c)
  t=k.plus(k.plus(k.mul(a,b),k.mul(b,c)),k.mul(c,a))
  F=k.plus(k.mul(lam,k.mul(s,s)),t)
  if F != 0: continue
  partial=[]
  for x,r,o in zip(xyz,(a,b,c),(k.plus(b,c),k.plus(a,c),k.plus(a,b))):
   d=k.mul(k.int(m),k.mul(k.pow(x,m-1),k.plus(k.mul(two,k.mul(lam,s)),o)))
   partial.append(d)
  if partial==[0,0,0]:out.append(xyz)
 return out

configs=[Field(3),Field(5),Field(7),Field(11),Field(13),Field(2,2,0b111),Field(2,3,0b1011),Field(2,4,0b10011)]
for k in configs:
 m=k.q-1
 l0=0
 l4=k.neg(k.div(1,k.int(4))) if k.p!=2 else None
 l3=k.neg(k.div(1,k.int(3))) if k.p!=3 else None
 for lam in range(k.q):
  pts=sing(k,lam)
  expect=(3 if lam==l0 else 3*m if l4 is not None and lam==l4 else m*m if lam==l3 else 0)
  assert len(pts)==expect,(k.p,k.q,lam,expect,len(pts),pts)
  if lam==l0:assert set(pts)=={(1,0,0),(0,1,0),(0,0,1)}
  if l4 is not None and lam==l4:assert all(sum(x==0 for x in pt)==1 for pt in pts)
  if lam==l3:assert all(all(x!=0 for x in pt) for pt in pts)
 print(f'CHECK_OK: GF({k.q}), m={m}, all {k.q} affine parameters, singular counts {3}'+(f', {3*m}' if l4 is not None else '')+(f', {m*m}' if l3 is not None else ''))
print('VERIFY_OK: Heron factorization, two-conic factorization, exhaustive rational singular points for every parameter over GF(3,4,5,7,8,11,13,16)')
