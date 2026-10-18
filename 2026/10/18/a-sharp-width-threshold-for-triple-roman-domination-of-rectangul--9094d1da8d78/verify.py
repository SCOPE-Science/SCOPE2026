#!/usr/bin/env python3
"""Finite checks for exact triple Roman domination of rook graphs.
This script is not a substitute for the unrestricted lower-bound proof.
"""
from itertools import product

def valid(A):
 m=len(A);n=len(A[0]);
 for i in range(m):
  for j in range(n):
   k=A[i][j]
   if k>=3:continue
   surplus=sum(max(A[i][h]-1,0) for h in range(n) if h!=j)+sum(max(A[h][j]-1,0) for h in range(m) if h!=i)
   if k+surplus<3:return False
 return True

def construct(m,n):
 assert 2<=m<=n
 A=[[0]*n for _ in range(m)]
 if n>=2*m:
  for i in range(m):A[i][0]=4
 else:
  k=n-m; c=0
  for i in range(m):
   if i<k:
    A[i][c]=A[i][c+1]=2;c+=2
   else:
    A[i][c]=3;c+=1
  assert c==n
 return A

def reference_formula(m,n):return min(4*m,2*m+n)

def exhaustive_below(m,n):
 N=m*n; bound=reference_formula(m,n)
 checked=0
 # Enumerate all low-weight label vectors; no full-graph enumeration assertions.
 def dfs(seq,total):
  nonlocal checked
  if len(seq)==N:
   checked+=1
   A=[seq[i*n:(i+1)*n] for i in range(m)]
   assert not valid(A),(m,n,A)
   return
  for a in range(min(4,bound-1-total)+1):dfs(seq+[a],total+a)
 dfs([],0)
 return checked

def main():
 checks=0
 for m in range(2,35):
  for n in range(m,3*m+9):
   A=construct(m,n)
   assert valid(A),(m,n,A)
   assert sum(map(sum,A))==reference_formula(m,n)
   checks+=1
 counts={}
 for m,n in ((2,2),(2,3),(2,4),(2,6),(3,3),(3,4)):
  counts[f'{m}x{n}']=exhaustive_below(m,n)
 print('CONSTRUCTIONS_OK',checks)
 print('BELOW_BOUND_EXHAUSTIVE',counts)
 print('VERIFY_OK')
if __name__=='__main__':main()
