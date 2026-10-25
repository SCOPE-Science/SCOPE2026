#!/usr/bin/env python3
"""Exact symbolic checks for twelve order-five rotation samples."""
import sympy as sp
R=sp.sqrt(5); F=(1+R)/2
vectors=[]
for a,b in [(1,F), (1,-F), (-1,F), (-1,-F)]:
    vectors.extend([(0,a,b),(a,b,0),(b,0,a)])
assert len(vectors)==12
D=F+2 # norm squared 1+phi^2=phi+2
A=sp.zeros(12); B=sp.zeros(12); P=sp.zeros(12)
for i,u in enumerate(vectors):
 for j,v in enumerate(vectors):
  x=sp.simplify(sum(s*t for s,t in zip(u,v))/D)
  if i==j:
   assert x==1
  elif x==-1: P[i,j]=1
  elif sp.simplify(x-1/R)==0: A[i,j]=1
  elif sp.simplify(x+1/R)==0: B[i,j]=1
  else: raise AssertionError((i,j,x))
# Quaternion composition: cos(theta/2) for relative 72-degree rotations.
cos2=(3+R)/8; sin2=(5-R)/8
for x,target in [(sp.Integer(1),sp.Integer(1)), (1/R,F/2), (-1/R,sp.Rational(1,2)), (-sp.Integer(1),(F-1)/2)]:
 assert sp.simplify(cos2+sin2*x-target)==0
# Derive finite-angle character tables from Chebyshev's identity.
for l in range(15):
 a=sp.chebyshevu(2*l,F/2)
 b=sp.chebyshevu(2*l,(F-1)/2)
 c=sp.chebyshevu(2*l,sp.Rational(1,2))
 assert sp.simplify(a-[1,F,0,-F,-1][l%5])==0
 assert sp.simplify(b-[1,1-F,0,F-1,-1][l%5])==0
 assert sp.simplify(c-[1,0,-1][l%3])==0
assert A*P==B
assert set(A.eigenvals().items())=={(5,1),(-1,5),(R,3),(-R,3)}
assert (P*P)==sp.eye(12)
assert all(sum(A.row(i))==5 and sum(B.row(i))==5 and sum(P.row(i))==1 for i in range(12))
# SO(3) character at 72,120,144 degrees, in each case periodic in degree.
def chi(l):
 return sp.Integer(2*l+1),[1,F,0,-F,-1][l%5],[1,0,-1][l%3],[1,1-F,0,F-1,-1][l%5]
def vals(l):
 n,a,c,b=chi(l)
 return [sp.simplify(n+5*a+5*c+b), sp.simplify(n-a-c+b), sp.simplify(n+R*(a-c)-b),sp.simplify(n-R*(a-c)-b)]
for l in range(100):
 n,a,c,b=chi(l)
 G=n*sp.eye(12)+a*A+c*B+b*P
 ev=vals(l)
 assert sum(x*m for x,m in zip(ev,[1,5,3,3]))==12*n
 # Polynomial annihilation and eigenvalue multiplicity via known projectors
 for x in set(ev):
  if l<=12:
   assert (G-x*sp.eye(12)).nullspace().__len__()==sum(m for y,m in zip(ev,[1,5,3,3]) if y==x),(l,x)
 assert all(x.is_nonnegative for x in ev), (l,ev)
 if l==0: assert [m for x,m in zip(ev,[1,5,3,3]) if x!=0]==[1]
 if l==1: assert [m for x,m in zip(ev,[1,5,3,3]) if x!=0]==[1,5,3]
 if l==2: assert [m for x,m in zip(ev,[1,5,3,3]) if x!=0]==[5,3,3]
 if l>=3: assert all(x>0 for x in ev)
print('EXACT_CHECK_PASS: icosahedral axes, valencies, A spectrum, four spectral branches and 100-degree positivity checks')
print('l=0..6:')
for l in range(7):print(l,[str(x) for x in vals(l)])
