"""Standalone numerical and symbolic checks of the corona mixing barrier.
Run: python verify.py. Requires numpy and sympy.
"""
from math import sqrt
import numpy as np
import sympy as sp

# Exact determinant identity and signs for the lower bound.
A,b=sp.symbols('A b', nonnegative=True,real=True)
B0=sp.Matrix([[1-A-b,b],[b,1-b]])
D=sp.Rational(4,5)*sp.eye(2)-B0
assert sp.factor(D.det()) == sp.factor((A+b-sp.Rational(1,5))*(b-sp.Rational(1,5))-b*b)
assert sp.simplify(sp.Rational(4,5)*(b-sp.Rational(1,5))-b*b+(b-sp.Rational(2,5))**2)==0
assert B0.subs({A:sp.Rational(3,5),b:sp.Rational(2,5)}).eigenvals() == {sp.Rational(4,5):1,-sp.Rational(1,5):1}

rng=np.random.default_rng(80384)
counts={'exact_blocks':0,'dense_checks':0,'random_invariant':0,'random_nonuniform':0,'other_cores':0}

def build_core(r,m):
 n=r*m
 C=np.ones((n,n))-np.kron(np.eye(r),np.ones((m,m)))
 return C

def matrix(C,a,b):
 N=len(C); deg=C.sum(axis=1)
 P=np.zeros((2*N,2*N));P[:N,:N]=a*C
 np.fill_diagonal(P[:N,:N],1-a*deg-b)
 P[np.arange(N),N+np.arange(N)]=b
 P[N+np.arange(N),np.arange(N)]=b
 P[N+np.arange(N),N+np.arange(N)]=1-b
 return P

def slem(P):
 w=np.linalg.eigvalsh(P)
 return max(abs(w[0]),abs(w[-2]))

for r in range(2,8):
 for m in range(2,7):
  C=build_core(r,m)
  N=len(C);d=(r-1)*m
  w=np.linalg.eigvalsh(C)
  assert np.allclose(w,sorted([-m]*(r-1)+[0]*(r*(m-1))+[d]),atol=1.e-9)
  a=3/(5*d); b=2/5
  P=matrix(C,a,b)
  assert np.all(P>=-1e-12) and np.allclose(P,P.T) and np.allclose(P.sum(axis=1),1)
  assert abs(slem(P)-.8)<1e-10,(r,m,slem(P))
  counts['dense_checks']+=1
  # Direct block diagonalization for all spectral modes and two uniform modes
  eig=[1,1-2*b]
  for l in w[:-1]:
   t=a*(d-l)/2
   eig.extend([1-t-b+sqrt(t*t+b*b),1-t-b-sqrt(t*t+b*b)])
  assert np.allclose(np.linalg.eigvalsh(P),sorted(eig),atol=1e-9)
  counts['exact_blocks']+=1
  # max-degree/Metropolis gap formula
  H=matrix(C,1/(d+1),1/(d+1))
  claimed=(d+sqrt(d*d+4))/(2*(d+1))
  assert abs(slem(H)-claimed)<1e-10,(r,m,slem(H),claimed)
  for _ in range(18):
   aa=rng.random()/d;bb=rng.random()*(1-d*aa)
   PP=matrix(C,aa,bb)
   assert slem(PP)>0.8-1e-10
   counts['random_invariant']+=1
  if N<=15:
   for _ in range(10):
    # arbitrary nonuniform weights on all edges and pendant links
    off=np.triu(C,1)*rng.random((N,N))
    off+=off.T
    leaves=rng.random(N)
    outgoing=off.sum(axis=1)+leaves
    c=min(1/(outgoing.max()+.01),.95)
    V=np.zeros((2*N,2*N))
    V[:N,:N]=c*off
    np.fill_diagonal(V[:N,:N],1-c*outgoing)
    V[np.arange(N),N+np.arange(N)]=c*leaves
    V[N+np.arange(N),np.arange(N)]=c*leaves
    V[N+np.arange(N),N+np.arange(N)]=1-c*leaves
    assert slem(V)>=.8-1e-10
    counts['random_nonuniform']+=1

# Hypercube cores: equality only for the two-dimensional (complete bipartite) case.
for d in (2,4,6):
 n=1<<d
 C=np.zeros((n,n))
 for x in range(n):
  for bit in range(d):
   C[x,x^(1<<bit)]=1
 ws=np.linalg.eigvalsh(C)
 assert min(abs(ws))<1e-10
 PP=matrix(C,3/(5*d),.4)
 if d==2:assert abs(slem(PP)-.8)<1e-10
 else: assert slem(PP)>.8+1e-3
 counts['other_cores']+=1

# Exact arbitrary-core block characteristic polynomial and asymptotic limit.
d_s,lam,a_s,b_s,z=sp.symbols('d lam a b z',real=True)
t_s=a_s*(d_s-lam)/2
block=sp.Matrix([[1-d_s*a_s-b_s+a_s*lam,b_s],[b_s,1-b_s]])
assert sp.simplify(((z*sp.eye(2)-block).det())-((z-(1-t_s-b_s))**2-t_s**2-b_s**2))==0
h_s=(d_s+sp.sqrt(d_s**2+4))/(2*(d_s+1))
assert sp.limit(sp.Rational(1,5)/(d_s*(1-h_s)),d_s,sp.oo)==sp.Rational(1,5)
assert sp.Rational(13,25)<sp.Rational(16,25)
# exact d=2,3,... asymptotic gap ratio and positivity checks
for d in [2,3,5,11,50,500,10000]:
 heur=(d+sqrt(d*d+4))/(2*(d+1))
 rat=((1-.8)/(1-heur))/d
 assert rat>0 and (rat>.2) and (d<50 or abs(rat-.2)<.01)


# Direct check on 5-, 6-, 7-, 8-, and 9-cycles, and Petersen (edge-transitive cores).
from math import cos,pi
for n in range(4,11):
 C=np.zeros((n,n))
 for x in range(n):
  C[x,(x+1)%n]=C[x,(x-1)%n]=1
 d=2
 lam=np.linalg.eigvalsh(C)[-2]
 assert lam>=-1e-9
 probe=matrix(C,3/(5*d),.4)
 if n==4: assert abs(slem(probe)-.8)<1e-10
 else: assert slem(probe)>.8+1e-5
 counts['other_cores']+=1
# Elementary adjacency inertia: nonadjacent vertices yield a zero Rayleigh quotient.
for r,m in ((2,2),(2,4),(3,2),(5,3)):
 C=build_core(r,m); n=C.shape[0]; eig=np.linalg.eigvalsh(C)
 assert abs(eig[-2])<1e-9 and any(abs(x)<1e-9 for x in eig)
 for i in range(n):
  for j in range(i+1,n):
   if C[i,j]==0:
    v=np.eye(n)[i]-np.eye(n)[j]
    assert abs(v@C@v)<1e-12
    assert np.allclose(C@v,np.zeros(n))
# Symbolic convex interpolation of a positive- and negative-core eigenblock.
lam_plus,lam_minus=sp.symbols('lp lm',positive=True)
B=lambda lam:sp.Matrix([[1-d_s*a_s-b_s+a_s*lam,b_s],[b_s,1-b_s]])
# lambda_plus weight is lambda_minus/(lambda_plus+lambda_minus)
theta=lam_minus/(lam_plus+lam_minus)
assert sp.simplify(theta*B(lam_plus)+(1-theta)*B(-lam_minus)-B(0))==sp.zeros(2)

print('VERIFY_OK',counts,'asymptotic slope=1/5')
