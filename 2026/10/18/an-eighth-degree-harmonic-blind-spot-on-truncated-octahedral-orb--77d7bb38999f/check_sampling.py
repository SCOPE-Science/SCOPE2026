#!/usr/bin/env python3
"""Standalone exact checker for degree-wise harmonic sampling at truncated-octahedral antipodal lines."""
import itertools
from fractions import Fraction
import hashlib
from sympy import Matrix, Rational, legendre

V=sorted({p for a in (-2,2) for b in (-1,1) for p in itertools.permutations((a,b,0))})
X=sorted(p for p in V if next(q for q in p if q)!=0 and next(q for q in p if q)>0)
assert len(V)==24 and len(X)==12 and len({p for p in V if tuple(-a for a in p) not in V})==0
T=Matrix(12,12,lambda i,j:Rational(sum(X[i][k]*X[j][k] for k in range(3)),5))
assert all(T[i,i]==1 for i in range(12))
assert all(abs(T[i,j])<=Rational(4,5) for i in range(12) for j in range(12) if i!=j)
expected=[1,3,5,6,9,9,10,12,11]
for l,r in enumerate(expected):
 G=Matrix(12,12,lambda i,j:legendre(l,T[i,j]))
 assert G.rank()==r, (l,G.rank(),r)
 if l==8:
  def signature(x):
   square=[a*a for a in x]
   disc=(square[0]-square[1])*(square[1]-square[2])*(square[2]-square[0])
   assert disc!=0
   return 1 if disc>0 else -1
  z=Matrix([signature(x) for x in X])
  assert G*z==Matrix.zeros(12,1)
  assert G.rank()==11
  assert G.nullspace()[0] in (z,-z) or len(G.nullspace())==1

# Rational Legendre values mod a prime, with denominator 5 invertible.
def check_mod(p):
 keys=sorted({int(5*T[i,j]) for i in range(12) for j in range(12)})
 assert all(abs(t)<=5 for t in keys)
 q={k:k*pow(5,-1,p)%p for k in keys}
 prev={k:1 for k in keys}; curr=q.copy()
 dets=[]
 def determinant(A):
  A=[row[:] for row in A]
  acc=1
  for j in range(12):
   pivot=next((i for i in range(j,12) if A[i][j]%p),None)
   if pivot is None:return 0
   if pivot!=j:
    A[j],A[pivot]=A[pivot],A[j];acc=-acc
   v=A[j][j]%p;acc=(acc*v)%p
   inv=pow(v,-1,p)
   for i in range(j+1,12):
    c=A[i][j]*inv%p
    if c:
     for h in range(j+1,12):A[i][h]=(A[i][h]-c*A[j][h])%p
     A[i][j]=0
  return acc%p
 for n in range(1,529):
  if n>=9:
   arr=[[curr[int(5*T[i,j])]%p for j in range(12)] for i in range(12)]
   d=determinant(arr)
   assert d!=0,(p,n)
   dets.append(d)
  if n<528:
   nxt={k:(((2*n+1)*q[k]*curr[k]-n*prev[k])*pow(n+1,-1,p))%p for k in keys}
   prev,curr=curr,nxt
 return dets

d1=check_mod(1000000007)
d2=check_mod(1000000009)
print('PASS: 24 vertices, 12 antipodal lines; ranks 0..8:',expected)
print('PASS: all 520 higher degrees 9..528 nonsingular over both prime fields')
print('nonzero determinant residues, endpoints:',d1[:3],d1[-3:],d2[:3],d2[-3:])
print('certificate SHA256',hashlib.sha256((';'.join(map(str,d1))+'|'+ ';'.join(map(str,d2))).encode()).hexdigest())
assert Fraction(3025*22,7*18*529)<1
print('For l >= 529, diagonal dominance follows from 11 sqrt(25*pi/(18*l))<1 using pi<22/7.')
