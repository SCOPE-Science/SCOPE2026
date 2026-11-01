"""Reproduce scalar rank-resonance identities and dense-matrix spectral trajectories."""
from fractions import Fraction as F
import random
import math
import numpy as np

random.seed(20261027)
rng = np.random.default_rng(20261027)

# The exact radial map in the nonzero regime.
def radial_step(r, s, tau):
    return F(0) if r == 0 else abs(s * r - tau)

def scalar_step(x, q, tau):
    if x == 0 or q == 0:
        return F(0)
    return q*x - tau*(1 if q*x > 0 else -1)

checks=0
for s in [F(1,9), F(2,5), F(3,4), F(17,19)]:
  for tau in [F(1,7),F(3,4)]:
    for k in range(1,9):
      resonance=tau*(s**(-k)-1)/(1-s)
      x=resonance
      for j in range(1,k+1):
        x=radial_step(x,s,tau)
        assert x>0 if j<k else x==0
        checks+=1
      assert radial_step(x,s,tau)==0
    # Various nonresonant data, to check exact radial monotonicity about the attractor.
    c=tau/(1+s)
    for j in range(1,321):
      x=F(j,31)*tau
      if x in [tau*(s**(-k)-1)/(1-s) for k in range(1,15)]: continue
      for t in range(24):
        y=radial_step(x,s,tau)
        assert y!=0
        assert abs(y-c)<=s*abs(x-c)
        x=y
        checks+=1
      for q in [s,-s]:
        z=F(j,31)*tau
        for t in range(18):
          zz=scalar_step(z,q,tau)
          assert abs(zz)==radial_step(abs(z),s,tau)
          z=zz
          checks+=1

# Dense-matrix tests: iterate the *polar factor of the provisional step*.
def polar(Z):
    u, singular, vh = np.linalg.svd(Z, full_matrices=False)
    keep=singular>2.e-12
    return (u[:, keep]@vh[keep, :]) if keep.any() else np.zeros_like(Z)

for m,n in [(2,2),(3,2),(5,4)]:
  for q in [-0.93,-0.43,0.17,0.72,0.95]:
    tau=.37
    s=abs(q)
    c=tau/(1+s)
    for trial in range(35):
      U,_=np.linalg.qr(rng.normal(size=(m,n)))
      V,_=np.linalg.qr(rng.normal(size=(n,n)))
      sig=rng.uniform(.13,3.7,n)
      X=U@np.diag(sig)@V.T
      Xinit=X.copy()
      for j in range(650):
        Z=q*X
        X=Z-tau*polar(Z)
      S=np.linalg.svd(X, compute_uv=False)
      assert np.max(np.abs(S-c))<1.e-10, (m,n,q,trial,S,c)
      assert abs(np.linalg.norm(X,'fro')-math.sqrt(n)*c)<1.e-10
      nxt=q*X-tau*polar(q*X)
      if q>0:
        assert np.linalg.norm(nxt+X, 'fro')<1.e-10
      else:
        assert np.linalg.norm(nxt-X, 'fro')<1.e-10
      checks+=n+2

# The exact proximal map does not have this floor.
for q in [-F(2,3),F(2,3)]:
  for t in [F(1,5),F(9,5)]:
    x=t
    for k in range(200):
      x=max(abs(q)*x-F(1,10),0)
    assert x==0
    checks+=1
print('CHECKS_OK',checks)
