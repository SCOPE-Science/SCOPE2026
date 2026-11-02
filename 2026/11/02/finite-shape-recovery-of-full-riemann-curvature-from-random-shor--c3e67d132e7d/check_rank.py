"""Exact finite-field ranks of the ellipsoid curvature-observation map."""
import numpy as np
from itertools import combinations_with_replacement

def modular_rank(arr,p=104729):
 A=[[int(z)%p for z in row] for row in arr]
 n,m=len(A),len(A[0]);r=0
 for c in range(m):
  pivot=next((i for i in range(r,n) if A[i][c]),None)
  if pivot is None:continue
  A[pivot],A[r]=A[r],A[pivot]
  inv=pow(A[r][c],-1,p)
  for j in range(c,m):A[r][j]=(A[r][j]*inv)%p
  for i in range(r+1,n):
   k=A[i][c]
   if k:
    for j in range(c,m):A[i][j]=(A[i][j]-k*A[r][j])%p
  r+=1
  if r==n:break
 return r

def run(n):
 basis=[]
 for i in range(n):
  for j in range(i,n):
   X=np.zeros((n,n),dtype=np.int64);X[i,j]=1;X[j,i]=1
   basis.append(X)
 pairs=list(combinations_with_replacement(range(len(basis)),2))
 rng=np.random.default_rng(4500+n)
 N=n*n*(n*n-1)//12
 matrix=[]
 for k in range(N+6):
  L=np.tril(rng.integers(-2,3,size=(n,n),dtype=np.int64))
  np.fill_diagonal(L,rng.integers(3,7,size=n,dtype=np.int64))
  Q=L@L.T;Q2=Q@Q;tQ=int(np.trace(Q))
  row=[]
  for ia,ib in pairs:
   A,B=basis[ia],basis[ib]
   Ric=int(np.trace(A))*B+int(np.trace(B))*A-A@B-B@A
   RQ=2*(int(np.trace(A@Q))*int(np.trace(B@Q))-int(np.trace(A@Q@B@Q)))
   f=(n+4)*RQ+2*(n+2)*int(np.trace(Ric@Q2))-2*tQ*int(np.trace(Ric@Q))
   row.append(f)
  matrix.append(row)
 rank=modular_rank(matrix)
 assert rank==N,(n,rank,N)
 print('MODULAR_FULL_CURVATURE_TOMOGRAPHY_RANK',n,N)
for n in [2,3,4,5]:run(n)
print('ALL_RANK_CHECKS_PASSED')

from fractions import Fraction
sec={(0,1):Fraction(1),(2,3):Fraction(1),
     (0,2):Fraction(-1,2),(0,3):Fraction(-1,2),
     (1,2):Fraction(-1,2),(1,3):Fraction(-1,2)}
ric_diag=[sum(v for (i,j),v in sec.items() if i==k or j==k) for k in range(4)]
assert ric_diag==[0]*4
q=[2,2,1,1]
RQQ=2*sum(v*q[i]*q[j] for (i,j),v in sec.items())
assert RQQ==2
assert Fraction(RQQ,3*(4+2)**2)==Fraction(1,54)
print('FOUR_DIMENSIONAL_RICCI_FLAT_WEYL_EXAMPLE_EXACT_PASSED')
