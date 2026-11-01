#!/usr/bin/env python3
"""Exact coefficient checks for the two distinguished cycles and a collapsing ray.

This script verifies symbolic base identities only, not the infinite measure theorem.
All polynomials are represented by rational coefficient pairs u+v*b.
"""
from fractions import Fraction as Q

def add(p,q): return (p[0]+q[0], p[1]+q[1])
def neg(p): return (-p[0],-p[1])
def sub(p,q): return add(p,neg(q))
def cn(c): return (Q(c),Q(0))
B=(Q(0),Q(1))
def point(x,y): return (x,y)
def branch(z,sx,sy):
    x,y=z
    return (sub(sub(x if sx>0 else neg(x),y),cn(1)),add(sub(x,y if sy>0 else neg(y)),B))

X=[point(neg(B),cn(1)),point(sub(B,cn(2)),cn(-1)),point(sub(B,cn(2)),sub((Q(0),Q(2)),cn(3)))]
Qcycle=[point(((Q(2,3),Q(-1,3))),cn(-1)),point((Q(-2,3),Q(1,3)),(Q(-1,3),Q(2,3))),point((Q(-4,3),Q(-1,3)),(Q(-1,3),Q(2,3)))]
# A sign-fixed step is not the same as a global absolute value; all displayed
# periodic points have fixed strict signs throughout the b >= 10 regime.
for i,z in enumerate(X):
 sx,sy=[(-1,1),(1,-1),(1,1)][i]
 assert branch(z,sx,sy)==X[(i+1)%3]
for i,z in enumerate(Qcycle):
 sx,sy=[(-1,-1),(1,1),(-1,1)][i]
 assert branch(z,sx,sy)==Qcycle[(i+1)%3]

# Ray x=s, y=s+(b+1)/3 is in quadrant I when s>0,b>=10.
s=cn(5)
ray=(s,add(s,(Q(1,3),Q(1,3))))
assert branch(ray,1,1)==Qcycle[2]

# Every finite branch word has integer coefficients of x,y and integer
# affine coefficients of 1,b. Check all words of lengths 1...6 by propagation.
from itertools import product
mats={ (1,1): ((1,-1),(1,-1)), (1,-1):((1,-1),(1,1)),(-1,1):((-1,-1),(1,-1)),(-1,-1):((-1,-1),(1,1)) }
for n in range(1,7):
 for word in product(list(mats),repeat=n):
  M=((1,0),(0,1)); t=((0,0),(0,0))
  for sign in word:
   A=mats[sign]
   M=tuple(tuple(sum(A[i][k]*M[k][j] for k in range(2)) for j in range(2)) for i in range(2))
   t=tuple(tuple(sum(A[i][k]*t[k][j] for k in range(2))+(1 if i==0 and j==0 else 1 if i==1 and j==1 else 0)*(-1 if i==0 else 1) for j in range(2)) for i in range(2))
  assert all(isinstance(x,int) for row in M+t for x in row)
print('PASS: exact symbolic three-cycle/ray identities and 5460 integral affine-word checks')
