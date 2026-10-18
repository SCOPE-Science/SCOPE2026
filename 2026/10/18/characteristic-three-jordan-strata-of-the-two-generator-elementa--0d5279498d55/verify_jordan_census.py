#!/usr/bin/env python3
"""Finite-field checks for truncated-3 group-algebra Jordan census."""
from itertools import product
from collections import Counter
import random

MON=[(i,j) for i in range(3) for j in range(3)]
IDX={v:i for i,v in enumerate(MON)}
DEG={d:[i for i,v in enumerate(MON) if sum(v)==d] for d in range(5)}

class Field:
 def __init__(self,q):
  assert q in (3,9)
  self.q=q
 def add(self,a,b):
  if self.q==3:return (a+b)%3
  return (a%3+b%3)%3+3*((a//3+b//3)%3)
 def mul(self,a,b):
  if self.q==3:return (a*b)%3
  aa,bb=a%3,a//3;cc,dd=b%3,b//3
  return (aa*cc+2*bb*dd)%3+3*((aa*dd+bb*cc)%3)
 def neg(self,a):
  return self.add(0,self.add(a,a)) # char3
 def sub(self,a,b):return self.add(a,self.neg(b))

def rank(M,F):
 a=[row[:] for row in M];m=len(a);n=len(a[0]); r=0
 for j in range(n):
  h=next((k for k in range(r,m) if a[k][j]),None)
  if h is None:continue
  a[r],a[h]=a[h],a[r]
  pivot=a[r][j]; inv=next(x for x in range(1,F.q) if F.mul(x,pivot)==1)
  a[r]=[F.mul(inv,z) for z in a[r]]
  for k in range(m):
   if k!=r and a[k][j]:
    v=a[k][j]
    a[k]=[F.sub(z,F.mul(v,w)) for z,w in zip(a[k],a[r])]
  r+=1
  if r==m:break
 return r

def mat(c,F):
 A=[[0]*9 for _ in range(9)]
 for j,(x,y) in enumerate(MON):
  for k,(u,v) in enumerate(MON):
   if x+u<3 and y+v<3:
    i=IDX[(x+u,y+v)]
    A[i][j]=F.add(A[i][j],c[k])
 return A

def expected(c,F):
 L=DEG[1];Q=DEG[2];C=DEG[3];D=DEG[4]
 if any(c[i]!=0 for i in L):return (6,3)
 if any(c[i]!=0 for i in Q):
  aa=c[IDX[(2,0)]];bb=c[IDX[(1,1)]];cc=c[IDX[(0,2)]]
  d=F.sub(F.mul(bb,bb),F.mul(aa,cc))
  return (4,1) if d else (3,0)
 if any(c[i]!=0 for i in C):return (2,0)
 if any(c[i]!=0 for i in D):return (1,0)
 return (0,0)

def predict_census(q):
 return {(0,0):1,(1,0):q-1,(2,0):q*(q*q-1),
         (3,0):q**3*(q*q-1),(4,1):q**3*(q**3-q*q),
         (6,3):q**6*(q*q-1)}

def test_one(F,coeff):
 c=[0]*9
 for j,v in zip([IDX[x] for x in MON if x!=(0,0)],coeff):c[j]=v
 M=mat(c,F)
 r=rank(M,F)
 M2=[[0]*9 for _ in range(9)]
 for i in range(9):
  for j in range(9):
   s=0
   for k in range(9):s=F.add(s,F.mul(M[i][k],M[k][j]))
   M2[i][j]=s
 t=rank(M2,F)
 expected_pair=expected(c,F)
 assert (r,t)==expected_pair, (F.q,coeff,r,t,expected_pair)
 return (r,t)

def run():
 rng=random.Random(3191106)
 for q in (3,9):
  F=Field(q)
  if q==3:
   rows=product(range(q),repeat=8)
  else:
   # All quadratic-leading forms, with independently sampled higher terms.
   rows=[]
   nonconst=[x for x in MON if x!=(0,0)]
   quadratic=[IDX[x]-1 for x in MON if sum(x)==2]
   cubic=[IDX[x]-1 for x in MON if sum(x)==3]
   quartic=[IDX[x]-1 for x in MON if sum(x)==4]
   linear=[IDX[x]-1 for x in MON if sum(x)==1]
   for u in product(range(q),repeat=3):
    arr=[0]*8
    for j,v in zip(quadratic,u):arr[j]=v
    for j in cubic+quartic:arr[j]=rng.randrange(q)
    rows.append(tuple(arr))
   for u in product(range(q),repeat=2):
    arr=[0]*8
    for j,v in zip(cubic,u):arr[j]=v
    for j in quartic:arr[j]=rng.randrange(q)
    rows.append(tuple(arr))
   for value in range(q):
    arr=[0]*8
    for j in quartic:arr[j]=value
    rows.append(tuple(arr))
   for i in range(1000):
    arr=[rng.randrange(q) for _ in range(8)]
    # force a nonzero linear part
    arr[linear[0]]=rng.randrange(1,q)
    rows.append(tuple(arr))
  counts=Counter(test_one(F, coeff) for coeff in rows)
  if q==3:assert counts==predict_census(q),(counts,predict_census(q))
  print('GF(%d): verified %d operators; encountered %s'%(q,sum(counts.values()),sorted(counts.items())))
 for q in (3,9,27,81):
  assert sum(predict_census(q).values())==q**8
  print('arithmetic normalization GF(%d): %d'%(q,q**8))
 print('VERIFY_OK_C3_SQUARE_JORDAN_CENSUS')

if __name__=='__main__':run()
