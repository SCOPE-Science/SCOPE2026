"""Reproducible exact rational witness checks for hollow symmetric determinants.

Uses only the Python standard library. This verifies finite witness identities,
not the all-dimensional arguments concerning irreducible components.
"""
from fractions import Fraction as F
from itertools import combinations

A5 = [
 [0,-1,-1,1,0],
 [-1,0,0,1,1],
 [-1,0,0,1,1],
 [1,1,1,0,-1],
 [0,1,1,-1,0],
]
A6 = [
 [0,1,1,1,0,1],
 [1,0,0,0,-1,1],
 [1,0,0,0,-1,1],
 [1,0,0,0,-1,0],
 [0,-1,-1,-1,0,1],
 [1,1,1,0,1,0],
]

def rref(A):
 A = [[F(v) for v in row] for row in A]
 m = len(A)
 n = len(A[0]) if A else 0
 piv=[]
 k=0
 for j in range(n):
  z=next((i for i in range(k,m) if A[i][j]),None)
  if z is None: continue
  A[k], A[z]=A[z], A[k]
  d=A[k][j]
  A[k]=[v/d for v in A[k]]
  for i in range(m):
   if i!=k:
    d=A[i][j]
    if d: A[i]=[u-d*v for u,v in zip(A[i],A[k])]
  piv.append(j);k+=1
  if k==m: break
 return A,piv

def rank(A):return len(rref(A)[1])

def null(A):
 R,piv = rref(A)
 n=len(A[0]); free=[j for j in range(n) if j not in piv]
 out=[]
 for j in free:
  v=[F(0)]*n;v[j]=F(1)
  for i,k in enumerate(piv):v[k]=-R[i][j]
  out.append(v)
 return out

def add_hyperbolic(A):
 n=len(A);B=[row[:]+[0,0] for row in A]
 B.extend([[0]*n+[0,1],[0]*n+[1,0]])
 return B

def normal_rank(A):
 k,l=null(A)
 T=[[k[i]*k[j],k[i]*l[j]+k[j]*l[i],l[i]*l[j]]
    for i,j in combinations(range(len(A)),2)]
 return rank(T)

for n in range(5,13):
 A = [row[:] for row in (A5 if n%2 else A6)]
 while len(A)<n:A=add_hyperbolic(A)
 assert len(A)==n and all(A[i][i]==0 for i in range(n))
 assert all(A[i][j]==A[j][i] for i in range(n) for j in range(n))
 assert rank(A)==n-2
 assert len(null(A))==2
 assert normal_rank(A)==3
 assert all(any(A[i][j] for j in range(n)) for i in range(n))
 print('rank-n-2-transverse',n,'OK')

# Rank-(n-1) example with a full-support kernel: not a critical point
# of the hollow determinant, because its off-diagonal adjugate is nonzero.
B5=[[0,-50,-32,-26,-64],[-50,0,-34,-4,-2],
    [-32,-34,0,-26,-32],[-26,-4,-26,0,-10],
    [-64,-2,-32,-10,0]]
assert rank(B5)==4 and len(null(B5))==1
assert all(null(B5)[0]);print('full-support-kernel',5,'OK')

# A generic zero-row component contains rank-(n-1) points: the complementary
# hollow matrix with every off-diagonal equal to one is invertible.
for n in range(5,13):
 B=[[0 if i==j else 1 for j in range(n-1)] for i in range(n-1)]
 assert rank(B)==n-1
 A=[row+[0] for row in B]+[[0]*n]
 assert rank(A)==n-1 and len(null(A))==1
 assert null(A)[0][-1]!=0 and all(x==0 for x in null(A)[0][:-1])
 print('zero-row-rank-n-1',n,'OK')

print('VERIFY_OK')
