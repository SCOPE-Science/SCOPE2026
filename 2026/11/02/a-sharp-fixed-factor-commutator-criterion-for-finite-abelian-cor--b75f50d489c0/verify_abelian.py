#!/usr/bin/env python3
"""Exact finite-abelian-group tests of fixed-factor commutator theorem.
No algebraic software or external packages. Integer coefficients only.
"""
from itertools import product
from collections import defaultdict
from math import gcd
from random import Random

class DSU:
 def __init__(self,n):self.p=list(range(n))
 def find(self,x):
  if self.p[x]!=x:self.p[x]=self.find(self.p[x])
  return self.p[x]
 def join(self,x,y):self.p[self.find(x)]=self.find(y)
 def groups(self):
  r=defaultdict(list)
  for i in range(len(self.p)):r[self.find(i)].append(i)
  return list(r.values())

def test(moduli,rng):
  els=list(product(*[range(n) for n in moduli]));N=len(els);index={x:i for i,x in enumerate(els)}
  def plus(x,y):return tuple((a+b)%n for a,b,n in zip(x,y,moduli))
  def neg(x):return tuple((-a)%n for a,n in zip(x,moduli))
  def muls(k,x):return tuple((k*a)%n for a,n in zip(x,moduli))
  def sigma(x):return muls(-2,x)
  def basis(i):v=[0]*N;v[i]=1;return v
  def op(x,y):return plus(neg(x),muls(2,y))
  def bracket_i(i,j):
   z=[0]*N;z[index[op(els[i],els[j])]]+=1;z[index[op(els[j],els[i])]]-=1
   return z
  def bracket(a,b):
   out=[0]*N
   for i,u in enumerate(a):
    if not u:continue
    for j,v in enumerate(b):
     if v:
      out[index[op(els[i],els[j])]]+=u*v
      out[index[op(els[j],els[i])]]-=u*v
   return out
  G=DSU(N);D=DSU(N)
  for i in range(N):
   D.join(i,index[sigma(els[i])])
   for j in range(N):
    p=op(els[i],els[j]);q=op(els[j],els[i]);G.join(index[p],index[q])
  Gp=G.groups();Dp=D.groups();g=len(Gp);c=len(Dp)
  expected_g=1
  for n in moduli:expected_g*=gcd(n,3)
  assert g==expected_g,(moduli,g,expected_g)
  odd_parts=[];a=0
  for n in moduli:
   count=0
   while n%2==0:n//=2;count+=1
   a=max(a,count)
   odd_parts.append(n)
  expected=(all(x in (1,3) for x in odd_parts))
  assert (g==c)==expected,(moduli,g,c)
  if expected:
   origin=tuple(0 for _ in moduli)
   for x in els:
    root=x;primitive=[0]*N
    for t in range(a):
     primitive[index[neg(root)]]+=1
     root=sigma(root)
    assert root==sigma(root)
    target=basis(index[x]);target[index[root]]-=1
    assert bracket(primitive,basis(index[origin]))==target,(moduli,x)
   for t in range(3):
    a_coeff=[rng.randint(-5,5) for i in range(N)]
    # Produce a generic element of W by subtracting each root coefficient.
    w=[0]*N;primitive=[0]*N
    for x,co in zip(els,a_coeff):
     root=x
     for tt in range(a):
      primitive[index[neg(root)]]+=co
      root=sigma(root)
     w[index[x]]+=co;w[index[root]]-=co
    assert bracket(primitive,basis(index[origin]))==w
  else:
   component={i:k for k,group in enumerate(Dp) for i in group}
   coset={i:k for k,group in enumerate(Gp) for i in group}
   i,j=next((i,j) for i in range(N) for j in range(i+1,N) if coset[i]==coset[j] and component[i]!=component[j])
   assert sum((1 if v==i else -1 if v==j else 0) for v in Dp[component[i]])==1
  return (moduli,N,g,c,c-g,expected)

if __name__=='__main__':
 rng=Random(329602)
 examples=[(2,), (3,), (4,), (5,), (6,), (8,), (9,), (12,), (18,), (24,), (36,),
           (2,2),(2,3),(2,5),(3,3),(3,9),(4,4),(4,3),(2,2,3),(2,3,3),(2,2,3,3),
           (2,2,2,2),(2,4,3),(2,3,5),(2,2,5),(5,5),(2,9),(2,2,9),(4,9)]
 results=[test(ns,rng) for ns in examples]
 print('moduli,order,cosets,components,obstruction_rank,universal_fixed_factor')
 for r in results:print(r)
 print('Direct basis-commutator span, incidence, integral primitive and integer sampling checked in',len(examples),'groups.')
 print('VERIFY_OK')
