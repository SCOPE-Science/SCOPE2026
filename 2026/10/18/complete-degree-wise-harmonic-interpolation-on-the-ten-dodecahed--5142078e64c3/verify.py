#!/usr/bin/env python3
"""Exact checks for degree-wise spherical-harmonic sampling on dodecahedral axes.

Run with Python >=3.9 (standard library only): python verify.py.
"""
from fractions import Fraction as F
from itertools import product

Z=(F(0),F(0)); ONE=(F(1),F(0)); PHI=(F(1,2),F(1,2))
INVPHI=(F(-1,2),F(1,2))

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,a): return (x[0]*a,x[1]*a)
def integer(x): return x==(F(int(x[0])),F(0))
def norm(v):
 t=Z
 for x in v: t=add(t,mul(x,x))
 return t

def antipode(v): return tuple(neg(a) for a in v)

def dot(x,y):
 z=Z
 for a,b in zip(x,y):z=add(z,mul(a,b))
 return z

def vertices():
 x=[tuple((F(a),F(0)) for a in signs) for signs in product((-1,1),repeat=3)]
 for a,b in product((-1,1),repeat=2):
  t=scale(INVPHI,a);u=scale(PHI,b)
  x.extend([(Z,t,u),(t,u,Z),(u,Z,t)])
 return x

V=vertices()
assert len(V)==20 and len(set(V))==20
assert all(norm(v)==(F(3),F(0)) for v in V)
X=[]
for v in V:
 if antipode(v) not in X: X.append(v)
assert len(X)==10 and all(v!=antipode(w) for v in X for w in X)

N=10
U=[[0]*N for _ in range(N)]
W=[[0]*N for _ in range(N)]
D=[[0]*N for _ in range(N)]
T=[[Z]*N for _ in range(N)]
for i in range(N):
 for j in range(N):
  t=scale(dot(X[i],X[j]),F(1,3));T[i][j]=t
  if i==j:
   assert t==ONE
   continue
  if mul(t,t)==(F(5,9),F(0)):
   U[i][j]=1 if t[1]>0 else -1
   D[i][j]=1
  elif mul(t,t)==(F(1,9),F(0)):
   W[i][j]=1 if t[0]>0 else -1
  else: raise AssertionError('Unexpected dot product')
assert all(sum(D[i])==3 and sum(int(x!=0) for x in W[i])==6 for i in range(N))

def matmul(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
I=[[int(i==j) for j in range(N)] for i in range(N)]
J=[[1]*N for _ in range(N)]
assert matmul(U,U)==[[3*I[i][j]+W[i][j] for j in range(N)] for i in range(N)]
assert matmul(U,W)==[[2*U[i][j] for j in range(N)] for i in range(N)]
assert matmul(D,D)==[[2*I[i][j]-D[i][j]+J[i][j] for j in range(N)] for i in range(N)]
assert all(sum(U[i][k]*U[i][k] for k in range(N))==3 for i in range(N))

# P_ell(1/3)=p_ell; P_ell(sqrt(5)/3)=(sqrt(5))^(ell mod 2) q_ell.
p=[F(1),F(1,3)]
q=[F(1),F(1,3)]
MAXDEG=61
for n in range(1,MAXDEG):
 p.append(((2*n+1)*F(1,3)*p[n]-n*p[n-1])/(n+1))
 q.append(((2*n+1)*F(5 if n%2 else 1,3)*q[n]-n*q[n-1])/(n+1))

EXPECTED=[1,3,5,7,9,6,10,10,9,10,10,10,10,10,9]
exact_checks=0
for ell in range(MAXDEG+1):
 a=p[ell];b=q[ell]
 if ell%2==0:
  spectrum=[(1+3*b+6*a,1), (1+b-2*a,5), (1-2*b+a,4)]
 else:
  spectrum=[(1+5*b+2*a,3), (1-5*b+2*a,3), (1-3*a,4)]
 assert all(z>=0 for z,m in spectrum),(ell,spectrum)
 rank=sum(m for z,m in spectrum if z>0)
 assert rank==(EXPECTED[ell] if ell<15 else N),(ell,rank,spectrum)
 exact_checks+=len(spectrum)
 if ell<15:
  print('degree',ell,'rank',rank,'spectrum fractions',spectrum)

 # Direct independent Legendre recurrence at all actual root-line dot products.
 for i in range(N):
  for j in range(N):
   t=T[i][j]
   b0=ONE
   if ell==0: z=b0
   else:
    b1=t
    for n in range(1,ell):
     b2=scale(sub(scale(mul(t,b1),2*n+1),scale(b0,n)),F(1,n+1))
     b0,b1=b1,b2
    z=b1
   if i==j: predicted=ONE
   elif ell%2:
    predicted=add(scale((F(0),b),U[i][j]),(a*W[i][j],F(0)))
   else:
    predicted=(a if D[i][j]==0 else b,F(0))
   assert z==predicted,(ell,i,j,z,predicted)
   exact_checks+=1

# Classical Bernstein bound |P_ell(cos(theta))| <= sqrt(2 / [pi (ell+1/2)sin(theta)]).
# The elementary rational estimates below imply the Gershgorin row sum <1 for ell>=62.
# pi>157/50, sqrt(2)>707/500.
assert F(2)>F(707,500)**2
assert F(3,1)/(F(157,50)*F(707,500))<F(103,125)**2
assert F(3,1)/F(157,50)<F(49,50)**2
assert (6*F(103,125)+3*F(49,50))**2<F(125,2)
print('PASS: 20 vertices, 10 lines; signed/unsigned graph identities, full exact Gram comparison,')
print('      complete rank table through degree 61; rigorous Bernstein-Gershgorin bound from 62.')
print('      exact component comparisons:',exact_checks)
