#!/usr/bin/env python3
"""Exact polynomial-ring identities over F5, without third-party packages."""
P=5;N=6
Z=(0,)*N

def mono(exps,coeff=1):return {tuple(exps):coeff%5} if coeff%5 else {}
def const(n):return {Z:n%5} if n%5 else {}
def add(*ps):
 o={}
 for a in ps:
  for key,value in a.items():o[key]=(o.get(key,0)+value)%5
 return {key:value for key,value in o.items() if value}
def neg(a):return {k:-v%5 for k,v in a.items()}
def mul(a,b):
 o={}
 for e,v in a.items():
  for f,w in b.items():
   key=tuple(e[i]+f[i] for i in range(N))
   o[key]=(o.get(key,0)+v*w)%5
 return {e:v for e,v in o.items() if v}
def powp(a,n):
 o=const(1)
 for j in range(n):o=mul(o,a)
 return o
def scale(a,n):return {e:v*n%5 for e,v in a.items() if v*n%5}
def c(i):return mono([int(j==i) for j in range(N)])
def coefx(a,j):
 return {e[:5]+(0,):v for e,v in a.items() if e[5]==j}
def subst(a,values):
 o={}
 for e,v in a.items():
  term=const(v)
  for i,ex in enumerate(e):
   if ex:term=mul(term,powp(values[i],ex))
  o=add(o,term)
 return o

b0,b1,b2,b3,b4,X=[c(i) for i in range(6)]
F=add(b0,mul(b1,X),mul(b2,powp(X,2)),mul(b3,powp(X,3)),mul(b4,powp(X,4)),powp(X,5))
cube=powp(F,3)
V0=add(scale(mul(b4,powp(b0,2)),3),mul(mul(b3,b1),b0),scale(mul(powp(b2,2),b0),3),scale(mul(b2,powp(b1,2)),3))
V1=add(mul(b4,b0),mul(b3,b1),scale(powp(b2,2),3),scale(mul(powp(b4,2),b1),3),mul(mul(b4,b3),b2),powp(b3,3))
V2=scale(b4,3)
assert [coefx(cube,j) for j in [4,9,14]]==[V0,V1,V2]
Q=add(mul(powp(b4,5),V0),mul(powp(b3,5),V1),mul(powp(b2,5),V2))
assert Q
# Writing P=A z^2+B z+C, z=c0.
A={(0,)+e[1:]:v for e,v in Q.items() if e[0]==2}
assert A==scale(powp(b4,6),3)
# Specialize c4=1,c3=0,c2=1,c1=t,c0=z; polynomial Q=3z^2+3z+3t^2+3.
t,z=b1,b0
special=subst(Q,[z,t,const(1),const(0),const(1),X])
assert special==add(scale(powp(z,2),3),scale(z,3),scale(powp(t,2),3),const(3))
# Discriminant: (3)^2 - 4*(3)*(3t^2+3) = 4t^2+3 over F5.
disc=add(const(9),neg(scale(mul(const(3),add(scale(powp(t,2),3),const(3))),4)))
assert disc==add(scale(powp(t,2),4),const(3))
# The discriminant has nonzero constant and nonzero t^2 terms but no t term,
# so it cannot be a square of a linear polynomial over any field of char5.
print('EXACT_POLYNOMIAL_IDENTITIES_AND_NONSQUARE_DISCRIMINANT_OK')
