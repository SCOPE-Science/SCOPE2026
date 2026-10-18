#!/usr/bin/env python3
"""Direct tests over F_9=F_3[u]/(u^2+1) for a one-square algebra."""
from itertools import product
from math import prod
from fractions import Fraction

def pair(x):return (x%3,x//3)
def field(x,y,op):
 a,b=pair(x);c,d=pair(y)
 if op=='+':return (a+c)%3+3*((b+d)%3)
 if op=='-':return (a-c)%3+3*((b-d)%3)
 return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
ADD=[[field(i,j,'+') for j in range(9)] for i in range(9)]
SUB=[[field(i,j,'-') for j in range(9)] for i in range(9)]
MUL=[[field(i,j,'*') for j in range(9)] for i in range(9)]
INV=[0]+[next(j for j in range(1,9) if MUL[i][j]==1) for i in range(1,9)]

def rank(mat):
 A=[row[:] for row in mat];r=0
 for col in range(len(A[0])):
  pivot=next((i for i in range(r,len(A)) if A[i][col]),None)
  if pivot is None:continue
  A[r],A[pivot]=A[pivot],A[r]
  A[r]=[MUL[INV[A[r][col]]][v] for v in A[r]]
  for i in range(len(A)):
   if i!=r:
    f=A[i][col]
    A[i]=[SUB[v][MUL[f][w]] for v,w in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r

def count(diag):
 n=2; result={}
 for vec in product(range(9),repeat=4):
  M=[vec[:2],vec[2:]]
  gg=[[0,0],[0,0]]
  for i in range(2):
   for j in range(2):
    acc=0
    for k in range(2):acc=ADD[acc][MUL[MUL[M[k][i]][diag[k]]][M[k][j]]]
    gg[i][j]=acc
  lam=MUL[gg[0][0]][INV[diag[0]]]
  if any(gg[i][j]!=(MUL[lam][diag[i]] if i==j else 0) for i in range(2) for j in range(2)):
   continue
  for f in product(range(9),repeat=2):
   R=[list(M[0])+[0],list(M[1])+[0],list(f)+[lam]]
   rr=rank(R);result[rr]=result.get(rr,0)+1
 return dict(sorted(result.items()))


def expected(diag):
 # In F_9, -1=2 is a square; 1+u (symbol 4) is nonsquare.
 eps=1 if diag==[1,1] else -1
 order=2*(9-eps)*(9-1)
 h={3:9**2*order,0:1,1:9**2-1}
 if eps==1:
  cnt=2*(9**2-1)
  h[1]+=cnt*9;h[2]=cnt*(9**2-9)
 return dict(sorted(h.items()))
for d in [[1,1],[1,4]]:
 got=count(d);want=expected(d)
 assert got==want,(d,got,want)
 print('GF9',d,got)
print('VERIFY_OK_ORTHOGONAL_EVOLUTION_GF9')
