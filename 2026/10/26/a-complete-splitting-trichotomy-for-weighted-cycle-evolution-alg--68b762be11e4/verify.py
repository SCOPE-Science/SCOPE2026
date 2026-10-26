#!/usr/bin/env python3
"""Exact finite-field monomial automorphism and isomorphism checks.
Uses exponents modulo 3 for F4* (no floating arithmetic)."""
from itertools import product
from collections import Counter

def automorphisms(A):
 n=len(A)
 ans=[]
 for k in range(n):
  for u0 in range(3):
   u=[u0]
   for i in range(n):
    x=(2*u[-1]+A[(i+k)%n]-A[i])%3
    if i<n-1: u.append(x)
    elif x!=u0: break
   else: ans.append((k,tuple(u)))
 return ans

def mul(x,y):
 k,u=x; ell,v=y;n=len(u)
 return ((k+ell)%n,tuple((v[i]+u[(i+ell)%n])%3 for i in range(n)))

def identity(n):return (0,(0,)*n)

def element_order(g):
 z=identity(len(g[1])); N=3*len(g[1])+1
 for h in range(1,N+1):
  z=mul(g,z)
  if z==identity(len(g[1])):return h
 raise AssertionError('missing order')

def iso(A,B):
 n=len(A)
 for k in range(n):
  for t0 in range(3):
   t=[t0]
   for i in range(n):
    r=(2*t[-1] + B[(i+k)%n]-A[i])%3
    if i<n-1:t.append(r)
    elif r != t0: break
   else:return True
 return False

def invariant(A):
 return sum((-1)**i*x for i,x in enumerate(A))%3

def test(n):
 expected=[]
 reps=[(0,)*n]
 if n%2==0:reps+=[(1,)+(0,)*(n-1)]
 for a in reps:
  G=automorphisms(a)
  delta=invariant(a) if n%2==0 else None
  if n%2: assert len(G)==n,(n,len(G))
  elif delta==0:assert len(G)==3*n,(n,len(G))
  else:assert len(G)==3*n//2,(n,len(G))
  assert len(set(G))==len(G)
  Gset=set(G)
  assert all(mul(x,y) in Gset for x in G for y in G)
  maxorder=max(map(element_order,G))
  if n%2==0 and delta!=0:
   assert maxorder==3*n//2,(n,maxorder)
   h=n//2
   split=any((x[0]==2%n and element_order(x)==h) for x in G)
   assert split==(h%3!=0),(n,h,split)
  if n%2 and n>1:assert maxorder==n
  print('n',n,'rep',a,'delta',delta,'|Aut|',len(G),'max order',maxorder)
 if n<=6:
  cnt=Counter();total=0
  for a in product(range(3),repeat=n):
   total+=1
   h=automorphisms(a)
   if n%2:assert len(h)==n
   else:assert len(h)==(3*n if invariant(a)==0 else 3*n//2)
   tag=(0 if n%2 else (invariant(a)!=0))
   assert iso(a,reps[int(tag)]),(n,a,tag)
   cnt[tag]+=1
  expected_count=3**n
  assert total==expected_count
  if n%2==0: assert cnt[False]==3**(n-1) and cnt[True]==2*3**(n-1)
  print('All',total,'weights passed: partition',dict(cnt))

for n in (1,2,3,4,5,6,8,10,12,18):test(n)
print('VERIFY_OK')
