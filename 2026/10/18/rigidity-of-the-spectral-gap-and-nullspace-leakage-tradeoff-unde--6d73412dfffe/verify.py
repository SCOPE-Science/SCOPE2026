"""Reproducible algebraic and numeric checks for a three-dimensional spectral perturbation theorem.

Run with Python 3, NumPy, and SymPy. Numerical trials illustrate asymptotics;
the universal assertions are proved in RESULT.md rather than inferred from sampling.
"""
import numpy as np
import sympy as sp

x,y,z=sp.symbols('x y z',real=True)
D=sp.diag(x,y,z)
u=sp.Matrix([1,1,1])/sp.sqrt(3)
U=sp.Matrix.hstack(sp.Matrix([1,-1,0])/sp.sqrt(2),sp.Matrix([1,1,-2])/sp.sqrt(6))
P=sp.eye(3)-u*u.T
T=sp.simplify(U.T*D*U)
b=sp.simplify(U.T*D*u)
g2=sp.factor((T[0,0]-T[1,1])**2+4*T[0,1]**2)
l2=sp.factor((b.T*b)[0])
S=(x-y)**2+(y-z)**2+(z-x)**2
assert sp.simplify(g2-sp.Rational(2,9)*S)==0
assert sp.simplify(l2-sp.Rational(1,9)*S)==0
assert sp.simplify(g2-2*l2)==0
assert sp.simplify(P*P-P)==sp.zeros(3)
assert sp.simplify(U.T*U-sp.eye(2))==sp.zeros(2)

rng=np.random.default_rng(257395)
count=0
for u0 in [np.array([1.,1.,1.]),np.array([1.,2.,3.]),np.array([1.,1.,0.]),np.array([0.,0.,1.])]:
 u0/=np.linalg.norm(u0)
 Ap=np.outer(u0,u0)
 Q=np.eye(3)-Ap
 for sample in range(36):
  d=rng.uniform(0.,1.,3)
  if sample<3:
   d=np.eye(3)[sample]
  mat=Q@np.diag(d)@Q
  roots=np.linalg.eigvalsh(mat)
  # Compression has spectrum {0, mu_1, mu_2} (zero may lie anywhere for signed d).
  g=float(roots[-1]-roots[0]) if sample== -1 else None
  basis=np.linalg.svd(Q)[0][:,:2]
  # Obtain a robust basis for the plane orthogonal to u, not an arbitrary SVD null column.
  vals, vec=np.linalg.eigh(Q)
  W=vec[:,1:]
  m=np.linalg.eigvalsh(W.T@np.diag(d)@W)
  G=m[-1]-m[0]
  L=np.linalg.norm(Q@np.diag(d)@u0)
  for eps in (0.0005,0.0001):
   B=Ap+eps*np.diag(d)
   eig, v=np.linalg.eigh(B)
   gap=(eig[1]-eig[0])/eps
   leakage=np.linalg.norm(Ap@v[:,:2],2)/eps
   assert abs(gap-G)<0.004
   assert abs(leakage-L)<0.004
   count+=1
  if np.all(np.abs(u0)>0) and np.allclose(np.abs(u0),np.ones(3)/np.sqrt(3)):
   assert np.allclose(G,np.sqrt(2)*L,rtol=1e-12,atol=1e-12)

# The ratio on the i-th coordinate probe is sqrt((1-p_i)/p_i).
for a in [sp.Matrix([1,1,1]),sp.Matrix([1,2,3]),sp.Matrix([2,2,1])]:
 a=a/sp.sqrt((a.T*a)[0]); ps=[sp.simplify(v**2) for v in a]
 for i,p in enumerate(ps):
  Ei=sp.diag(*(1 if j==i else 0 for j in range(3)))
  residual2=sp.simplify((a.T*Ei*(sp.eye(3)-a*a.T)*Ei*a)[0])
  assert sp.simplify(residual2-p*(1-p))==0

# CDF derived by polar integration within the inscribed-hexagon branch.
for g in [0.06,0.15,0.32,0.48,1/np.sqrt(3)]:
 ddraw=rng.uniform(0.,1.,size=(600000,3))
 delta=np.sum((ddraw-ddraw.mean(axis=1,keepdims=True))**2,axis=1)
 gaps=np.sqrt((2./3.)*delta)
 empirical=np.mean(gaps<=g)
 exact=3*np.sqrt(3)*np.pi*g*g/2-9*g**3
 assert abs(empirical-exact)<0.004,(g,empirical,exact)
 assert 0<=exact<=1

print('PASS: balanced exact polynomial identities, coordinate rigidity probes,',count,'finite-perturbation comparisons, and 5 distribution checks')
