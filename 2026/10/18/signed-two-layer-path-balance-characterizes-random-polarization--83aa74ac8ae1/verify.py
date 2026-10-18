#!/usr/bin/env python3
"""Finite exact checks for signed two-layer reinforced Bernoulli networks.
The almost-sure classification requires the analytic proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def matmul(A,B):
 n=len(A)
 return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def rank(A):
 A=[list(map(F,row)) for row in A]; m=len(A);n=len(A[0]);r=0
 for j in range(n):
  p=next((i for i in range(r,m) if A[i][j]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r]; c=A[r][j];A[r]=[x/c for x in A[r]]
  for i in range(m):
   if i!=r and A[i][j]:
    c=A[i][j]; A[i]=[u-c*v for u,v in zip(A[i],A[r])]
  r+=1
  if r==m:break
 return r

def irreducible(P):
 n=len(P)
 for start in range(n):
  seen={start}; todo=[start]
  while todo:
   i=todo.pop()
   for j in range(n):
    if P[i][j]>0 and j not in seen:seen.add(j);todo.append(j)
  if len(seen)!=n:return False
 return True

def gauge(B,W,s):
 n=len(B);h={0:1};edges=[]
 for i,j,k in product(range(n),repeat=3):
  if B[i][j]>0 and W[j][k]>0:
   edges.append((i,k,s[j]))
   if abs(s[j])!=1:return None
 todo=[0]
 while todo:
  i=todo.pop()
  for u,k,sign in edges:
   if u!=i:continue
   v=h[i]*sign
   if k in h and h[k]!=v:return None
   if k not in h:h[k]=v;todo.append(k)
 if len(h)!=n:return None
 if any(h[i]!=sign*h[k] for i,k,sign in edges):return None
 return [h[i] for i in range(n)]

def check(B,W,s):
 n=len(B);P=matmul(B,W)
 assert all(sum(r)==1 and all(x>=0 for x in r) for M in (B,W) for r in M)
 if not irreducible(P):return False
 R=matmul(matmul(B,[[F(s[i]) if i==j else F(0) for j in range(n)] for i in range(n)]),W)
 h=gauge(B,W,s)
 IminusR=[[F(int(i==j))-R[i][j] for j in range(n)] for i in range(n)]
 assert (rank(IminusR)<n)==(h is not None)
 if h is not None:
  assert R==[[h[i]*P[i][j]*h[j] for j in range(n)] for i in range(n)]
  # exact conditional mean identity for transformed observations
  z=[F(i+2,n+5) for i in range(n)]
  yy=[(z[i] if h[i]==1 else 1-z[i]) for i in range(n)]
  for j in range(n):
   recipients=[i for i in range(n) if B[i][j]>0]
   if not recipients:continue
   t=h[recipients[0]]
   p=F(1,2)+F(s[j],2)*sum((W[j][k]*(2*z[k]-1) for k in range(n)),F(0))
   pp=p if t==1 else 1-p
   assert pp==sum((W[j][k]*yy[k] for k in range(n)),F(0))
 return True

F2=F(1,2)
W=[[F2,F2,0,0],[0,0,F2,F2],[F2,F2,0,0],[0,0,F2,F2]]
B=[[F2,0,0,F2],[F2,0,0,F2],[0,F2,F2,0],[0,F2,F2,0]]
P=matmul(B,W)
assert P==[[F(1,4)]*4 for _ in range(4)]
h=[1,1,-1,-1];s=[1,1,-1,-1]
assert gauge(B,W,s)==h
assert check(B,W,s)
assert gauge(B,W,[1,1,1,-1]) is None
assert check(B,W,[1,1,1,-1])
assert check(B,W,[1,F(0),-1,-1])
alpha=[sum((F(1,4)*B[i][j] for i in range(4)),F(0)) for j in range(4)]
assert alpha==[F(1,4)]*4
varlb=sum((a*a*F(1,4) for a in alpha),F(0))
assert varlb==F(1,16)

random=Random(20261013)
def sample_row(n):
 subset=[i for i in range(n) if random.randrange(2)]
 if not subset:subset=[random.randrange(n)]
 return [F(int(i in subset),len(subset)) for i in range(n)]
cases=0
for n in (2,3,4):
 for rep in range(900):
  W=[sample_row(n) for _ in range(n)]
  B=[sample_row(n) for _ in range(n)]
  s=[random.choice([F(-1),F(0),F(1)]) for _ in range(n)]
  cases+=bool(check(B,W,s))
print('EXACT_SIGNED_PATH_CHECKS_OK',cases,'IRREDUCIBLE_NETWORKS','PRIMITIVE_POLARIZATION_VARIANCE_LOWER_BOUND=1/16')
