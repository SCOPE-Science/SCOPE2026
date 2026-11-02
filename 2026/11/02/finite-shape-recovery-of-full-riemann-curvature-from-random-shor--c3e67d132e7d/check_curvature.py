#!/usr/bin/env python3
"""Exact rational tests for ellipsoidal two-point curvature tomography.
Public reproducibility file; requires sympy only.
"""
import sympy as s
from itertools import combinations_with_replacement

def sym_basis(n):
 out=[]
 for i in range(n):
  for j in range(i,n):
   M=s.zeros(n);M[i,j]=1;M[j,i]=1
   out.append(M)
 return out

def kn_data(A,B):
 n=A.rows
 ric=s.trace(A)*B+s.trace(B)*A-A*B-B*A
 def RQ(Q):return 2*(s.trace(A*Q)*s.trace(B*Q)-s.trace(A*Q*B*Q))
 return ric,RQ

def value(n,ric,RQ,Q):
 a=s.Rational(1,3*(n+2)**2)*RQ(Q)
 b=s.Rational(2,3*(n+2)*(n+4))*(s.trace(ric*Q*Q)-s.trace(Q)*s.trace(ric*Q)/(n+2))
 return s.factor(a+b)

def test(n):
 basis=sym_basis(n)
 maps=[kn_data(basis[i],basis[j]) for i,j in combinations_with_replacement(range(len(basis)),2)]
 u=s.eye(n)[:,0]
 Q=u*u.T
 for ric,rq in maps:
  assert s.simplify(value(n,ric,rq,Q)-s.Rational(2*(n+1),3*(n+2)**2*(n+4))*ric[0,0])==0
 for i in range(n):
  for j in range(i+1,n):
   Q=s.zeros(n);Q[i,i]=1;Q[j,j]=1
   for ric,rq in maps:
    # sectional curvature equals half R(Q,Q)
    sec=rq(Q)/2
    reconstructed=s.Rational(3*(n+2)**2,2)*value(n,ric,rq,Q)-s.Rational(n,n+4)*(ric[i,i]+ric[j,j])
    assert s.simplify(sec-reconstructed)==0
 for ric,rq in maps:
  q=s.eye(n)
  assert s.factor(value(n,ric,rq,q)-s.Rational(n+8,3*(n+2)**2*(n+4))*s.trace(ric))==0
 print('ROUND_RANK_ONE_AND_ORTHONORMAL_TWO_PLANE_FORMULAS_EXACT',n)
 if n<=3:
  # Generate deterministic positive-definite integer Q through lower-triangular factors.
  import random
  rng=random.Random(18000+n)
  shapes=[]
  for k in range(30):
   L=s.eye(n)
   for i in range(n):
    L[i,i]=1+rng.randrange(1,4)
    for j in range(i):L[i,j]=rng.randrange(-2,3)
   shapes.append(L*L.T)
  matrix=s.Matrix([[value(n,ric,rq,Q) for ric,rq in maps] for Q in shapes[:min(len(shapes),15)]])
  rank=matrix.rank()
  expected=n*n*(n*n-1)//12
  assert rank==expected,(n,rank,expected)
  print('GENERIC_FULL_CURVATURE_RANK_EXACT',n,rank)

for n in (2,3):test(n)
print('ALL_CHECKS_PASSED')
