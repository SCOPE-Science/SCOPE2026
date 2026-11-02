#!/usr/bin/env python3
"""Self-contained exhaustive partner census for sl_3(F_2); integer arithmetic only."""
from collections import Counter
from itertools import product
# Algebra basis consists of the two trace-zero diagonals and the six off-diagonal units.
units=[(0,0),(1,1),(2,2)]
def e(i,j):return 1 << (3*i+j)
B=[e(0,0)^e(2,2),e(1,1)^e(2,2)] + [e(i,j) for i in range(3) for j in range(3) if i!=j]
assert len(B)==8
rep=[0]*256; lookup={}
for x in range(256):
 t=0
 for j in range(8):
  if (x>>j)&1:t^=B[j]
 rep[x]=t;lookup[t]=x
assert len(lookup)==256

def basic_bracket(u,v):
 r=0
 for i in range(3):
  for j in range(3):
   if not ((u>>(3*i+j))&1):continue
   for k in range(3):
    for l in range(3):
     if (v>>(3*k+l))&1:
      if j==k:r^=e(i,l)
      if l==i:r^=e(k,j)
 return r
br_basis=[[lookup[basic_bracket(u,v)] for v in B] for u in B]
assert all(br_basis[i][j]==br_basis[j][i] for i in range(8) for j in range(8))
def bracket(x,y):
 z=0
 for i in range(8):
  if x>>i&1:
   for j in range(8):
    if y>>j&1:z^=br_basis[i][j]
 return z
# Separate table-building route uses bilinear structure constants, not 3x3 products.
BRT=[[bracket(x,y) for y in range(256)] for x in range(256)]

def span_dim(a,b):
 piv=[0]*8
 independent=[]
 def insert(v):
  t=v
  for k in range(7,-1,-1):
   if t>>k&1:
    if piv[k]:t^=piv[k]
    else:
     piv[k]=t
     independent.append(t)
     return True
  return False
 insert(a);insert(b)
 k=0
 while k<len(independent):
  for j in range(k):insert(BRT[independent[k]][independent[j]])
  k+=1
 return len(independent)
counts=[];dist=Counter(); all_partner=Counter()
for a in range(256):
 ps=0
 for b in range(256):
  d=span_dim(a,b)
  dist[d]+=1
  ps+=(d==8)
 counts.append(ps);all_partner[ps]+=1
print('DIM_DIST', sorted(dist.items()))
print('PARTNER_SPECTRUM', sorted(all_partner.items()))
print('TOTAL_PAIRS',sum(counts))
assert sorted(dist.items())==[(0,1),(1,765),(2,3618),(3,7392),(4,20160),(5,20160),(8,13440)]
assert sorted(all_partner.items())==[(0,50),(56,24),(64,126),(72,56)]
assert sum(counts)==13440
assert counts[0]==0
print('VERIFY_OK')
