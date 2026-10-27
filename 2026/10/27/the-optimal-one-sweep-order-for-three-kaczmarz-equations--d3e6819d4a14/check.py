"""Standalone exact-arithmetic checks for three-row Kaczmarz ordering.

Requires Python 3.10+ standard library. Checks identities and finite samples;
the global ordering theorem and sharp supremum are proved analytically.
"""
from fractions import Fraction as F
from itertools import permutations
from random import Random
from math import sqrt

n=3
I=[[F(int(i==j)) for j in range(n)] for i in range(n)]

def dot(u,v): return sum((x*y for x,y in zip(u,v)),F(0))
def transpose(A): return list(map(list,zip(*A)))
def mm(A,B):
 BT=transpose(B);return [[dot(row,col) for col in BT] for row in A]
def tr(A):return sum((A[i][i] for i in range(n)),F(0))
def det(A):
 return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
         -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
         +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def proj(u): return [[I[i][j]-u[i]*u[j] for j in range(n)] for i in range(n)]
def norm_sq_formula(Q,p):
 return (float(Q+p)+sqrt(max(0.,float((Q+p)**2-4*p))))/2
def rational_unit(x,y):
 d=1+x*x+y*y
 return [(1-x*x-y*y)/d,2*x/d,2*y/d]

def check(rows):
 assert all(dot(x,x)==1 for x in rows)
 G=[[dot(u,v) for v in rows] for u in rows]
 dg=det(G)
 assert dg>0
 P=[proj(x) for x in rows]
 Q=1-dg
 eigen_invariants=[]
 vals=[]
 for order in permutations(range(3)):
  i,j,k=order
  M=mm(P[k],mm(P[j],P[i]))
  B=mm(transpose(M),M)
  a,b,c=G[i][j],G[i][k],G[j][k]
  p=(a*c)**2
  T=a*a+c*c+(b-a*c)**2
  assert T==Q+p,(order,T,Q+p)
  assert tr(B)==T
  e2=(tr(B)**2-tr(mm(B,B)))/2
  assert e2==p,(order,e2,p)
  assert det(B)==0
  s=norm_sq_formula(Q,p)
  # Eigenvalues of the sweep, not just the singular values.
  eigen_invariants.append((tr(M),(tr(M)**2-tr(mm(M,M)))/2,det(M)))
  vals.append((order,p,s))
 assert len(set(eigen_invariants))==1,eigen_invariants
 assert eigen_invariants[0]==(sum((G[0][1]**2,G[0][2]**2,G[1][2]**2))-G[0][1]*G[0][2]*G[1][2],G[0][1]*G[0][2]*G[1][2],F(0))
 for _o,p,s in vals:
  for _oo,pp,ss in vals:
   if p>pp: assert s<=ss+1e-11
 if Q>0:
  assert min(v[2] for v in vals)>=float(Q)/2-1e-10
  assert max(v[2] for v in vals)<=float(Q)+1e-10
 return vals

if __name__=='__main__':
 rng=Random(260932034)
 count=0
 for _ in range(160):
  xy=[(F(rng.randint(-5,5),rng.randint(3,10)),F(rng.randint(-5,5),rng.randint(3,10))) for _ in range(3)]
  rows=[rational_unit(*v) for v in xy]
  if det([[dot(x,y) for y in rows] for x in rows])==0:continue
  check(rows);count+=1
 print('PASS: exact Fraction identities and all six orderings for',count,'generic rational triples')
 # Rational star triple with two orthogonal leaves.
 for m in (2,3,4,8,16,32,64,128,256):
  z=F(1,m);t=2*z/(1+2*z*z);h=(1-2*z*z)/(1+2*z*z)
  rows=[[h,t,t],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]
  vals=check(rows)
  worst=max(q for _,_,q in vals)
  best=min(q for _,_,q in vals)
  Q=2*t*t
  p=t**4
  assert abs(worst-float(Q))<1e-12
  assert abs(best-norm_sq_formula(Q,p))<1e-12
  print('rational star t=',t,'norm penalty=',round(sqrt(worst/best),12))
 print('PASS: rational star family tends to the sharp sqrt(2) penalty')
