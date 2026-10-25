#!/usr/bin/env python3
"""Finite exact-rational tests for a heterogeneous equilateral one-point extension law.
These tests are corroborative, not a proof for unrestricted real parameters.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product

def valid(r):
 return all(a+b>=1 and abs(a-b)<=1 for i,a in enumerate(r) for b in r[i+1:])

def sharp(r):
 seq=sorted(r); s=F(0); c=F(1)
 for k,x in enumerate(seq,1):
  s+=x
  if k>=2:c=max(c,F(k-1)/s)
 return c

def weights(r,c):
 lb=[max(F(0),F(1)-c*x) for x in r]
 assert sum(lb)<=1,(r,c,lb)
 lb[0]+=F(1)-sum(lb)
 assert sum(lb)==1 and all(a>=0 for a in lb)
 return lb

def TV(alpha,i):
 return (abs(alpha[i]-1)+sum(abs(a) for j,a in enumerate(alpha) if i!=j))/2

def scalar_norm(alpha,i):
 best=F(0)
 for bits in product((0,1),repeat=len(alpha)):
  if not 0<sum(bits)<len(alpha):continue
  val=abs(sum(alpha[j]*bits[j] for j in range(len(alpha)))-bits[i])
  best=max(best,val)
 return best

def normalize(alpha):
 P=sum(max(a,F(0)) for a in alpha)
 assert P>=1
 return [max(a,F(0))/P for a in alpha]

count=0;pair_checks=0;sign_checks=0;uniqueness=0
for n in (2,3,4):
 vals=[F(k,4) for k in range(1,9)]
 for r in combinations_with_replacement(vals,n):
  if not valid(r):continue
  c=sharp(r);alpha=weights(r,c)
  positive=sum(max(F(0),F(1)-c*x) for x in r)
  assert positive<=1
  assert all((1-alpha[i])/r[i]<=c for i in range(n))
  for i in range(n):
   assert scalar_norm(alpha,i)==TV(alpha,i)==1-alpha[i]
   pair_checks+=1
  # Exact cutoff comparison by all subsets, not just sorted prefixes.
  subsets=[(sum(bits),sum(r[i] for i in range(n) if bits[i])) for bits in product((0,1),repeat=n)]
  assert max(F(1),max(F(k-1)/total for k,total in subsets if k>=2))==c
  if c>1:
   assert positive==1
   assert all(alpha[i]==max(F(0),1-c*r[i]) for i in range(n))
   uniqueness+=1
  assert c<=F(2)-F(2,n) if n>=3 else c==1
  count+=1

# Verify that normalized positive coefficients dominate each index for signed
# families with prescribed small-denominator coefficient grids.
for n in (2,3,4):
 vals=[F(k,3) for k in range(-3,6)]
 for a in product(vals,repeat=n-1):
  alpha=list(a)+[F(1)-sum(a)]
  beta=normalize(alpha)
  for i in range(n):
   assert scalar_norm(alpha,i)==TV(alpha,i)
   assert TV(beta,i)<=TV(alpha,i)
   sign_checks+=1

r=(F(1,2),F(1,2),F(1,2),F(1),F(1))
c=sharp(r);a=weights(r,c)
assert c==F(4,3) and a==[F(1,3)]*3+[F(0)]*2
assert sharp((F(1,2),)*5)==F(8,5)
print('EQUILATERAL_EXTENSION_CERTIFICATE_OK',
      'radius_cases='+str(count),
      'point_norms='+str(pair_checks),
      'signed_comparisons='+str(sign_checks),
      'unique_positive_weight_cases='+str(uniqueness))
