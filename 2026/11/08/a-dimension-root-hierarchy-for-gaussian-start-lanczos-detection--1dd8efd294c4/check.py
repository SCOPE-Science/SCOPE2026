#!/usr/bin/env python3
"""Finite-arithmetic tests for the rank-one negative-spike Krylov-curvature criterion.
This script is supplemental; the theorem is proved analytically.
"""
import numpy as np
from fractions import Fraction as F
from math import sqrt
from scipy.stats import chi2

def moment_test(a, positive, masses, negmass, k):
    b=np.array(positive, dtype=float)
    w=np.array(masses, dtype=float)
    B=np.vander(b, N=k, increasing=True)
    gram = B.T@np.diag(b*w)@B
    u=(-a)**np.arange(k)
    L=a*negmass*float(u@np.linalg.solve(gram,u))
    values=np.r_[-a,b]
    weights=np.r_[negmass,w]
    # moment Gram matrix J, finite-size Rayleigh quotient on the Krylov columns
    V=np.vander(values,N=k,increasing=True)
    C=V.T@np.diag(weights)@V
    D=V.T@np.diag(weights*values)@V
    chol=np.linalg.cholesky(C)
    Lmat=np.linalg.solve(chol,D)@np.linalg.inv(chol.T)
    ritz=np.linalg.eigvalsh((Lmat+Lmat.T)/2)
    return L>1, ritz[0]<0, L,ritz[0]

def exact_k2():
    a,b,c,x,y,z=map(F, ['3','1','4','2','11','7'])
    # coefficients of determinant for K_2 generated from v,Hv
    m=lambda j: -a**j*x if j%2 else a**j*x
    m1=-a*x+b*y+c*z
    m2=a*a*x+b*b*y+c*c*z
    m3=-a**3*x+b**3*y+c**3*z
    d=m1*m3-m2*m2
    rhs=b*c*y*z*(c-b)**2-a*x*(b*y*(a+b)**2+c*z*(a+c)**2)
    assert d==rhs
    return str(d)

rng=np.random.default_rng(9217)
N=0
for q in range(2,5):
 for k in range(1,q+1):
  for i in range(160):
   b=np.arange(1,q+1,dtype=float)*(0.65+rng.uniform(0.05,0.3))
   masses=1+rng.gamma(shape=2,size=q)
   x=0.05+rng.gamma(shape=2)
   a=rng.uniform(0.2,5.)
   rule,exact,L,r=moment_test(a,b,masses,x,k)
   if abs(L-1)>1e-6 and abs(r)>1e-6:
    assert rule==exact, (q,k,a,L,r)
    N+=1

# Three-step detection for two positive levels: negative isolated mode always present
for j in range(100):
 b,c=np.sort(rng.uniform(0.5,5,size=2))
 a=rng.uniform(0.2,10)
 masses=rng.uniform(0.2,3,size=3)
 v=np.array([-a,b,c]); K=np.vander(v,N=3,increasing=True)
 M=K.T@np.diag(masses)@K
 W=K.T@np.diag(masses*v)@K
 Q=np.linalg.solve(np.linalg.cholesky(M), W)@np.linalg.inv(np.linalg.cholesky(M).T)
 assert np.linalg.eigvalsh((Q+Q.T)/2)[0]<-a+1e-5

# Asymptotic limiting probability is the chi-square upper tail for three bands.
p=np.array([0.2,0.3,0.5]);bs=np.array([1.,2.,4.]);k=2
t=2.0
B=np.vander(bs,N=k,increasing=True)
G=B.T@np.diag(bs*p)@B
ell=np.linalg.inv(G)[-1,-1]
lim=chi2.sf(1/(t**(2*k-1)*ell),1)
assert 0<lim<1
# Simulated large-d limit with multinomial block multiplicities, no normalized vector required.
d=250000;m=(p*(d-1)).astype(int);m[-1]+=d-1-sum(m)
V=np.stack([rng.chisquare(int(mj),size=3000) for mj in m],axis=1)
U=rng.chisquare(1,size=3000)
a=t*d**(1/(2*k-1));u=(-a)**np.arange(k)
# compute Gram 2x2 formula vectorized exactly to avoid huge matrices
v0=(V*bs).sum(1); v1=(V*bs**2).sum(1);v2=(V*bs**3).sum(1)
phi=(v2*u[0]**2 -2*v1*u[0]*u[1]+v0*u[1]**2)/(v0*v2-v1*v1)
prob=np.mean(a*U*phi>1)
assert abs(prob-lim)<0.08,(prob,lim)
print('VERIFY_OK',N,'finite Krylov/Schur matches; 100 three-band exhaustion checks; two-band symbolic=',exact_k2())
print('SCALING_CHECK dimension=',d,'observed=',round(prob,5),'asymptotic=',round(lim,5),'ell=',round(ell,6))
