#!/usr/bin/env python3
"""Reproducible numerical checks for entropy contraction and the two-direction rate."""
import math
import numpy as np
rng=np.random.default_rng(27182818)
checks=0

def assert_close(a,b,atol=5e-10,rtol=5e-10):
    global checks
    np.testing.assert_allclose(a,b,atol=atol,rtol=rtol)
    checks+=1

def orthonormal(n,r):
    Q, _=np.linalg.qr(rng.standard_normal((n,r)))
    return Q[:,:r]

def step(M,V,lam):
    return M-(1-lam)*(M@V)@np.linalg.solve(V.T@M@V,V.T@M)+(1-lam)*V@V.T

def D(M):
    sign,logdet=np.linalg.slogdet(M)
    assert sign>0
    return np.trace(M)-logdet-len(M)

# Exact Schur elimination, SPD preservation, and nonincreasing Stein divergence
for n in [2,3,5]:
 for r in range(1,n+1):
  for trial in range(40):
   Y=rng.standard_normal((n,n)); M=.04*np.eye(n)+Y.T@Y/n
   V=orthonormal(n,r)
   lam=float(rng.uniform(.02,.98))
   G=(step(M,V,lam)-lam*M)/(1-lam)
   # Use an SVD to construct an orthogonal complement.
   if r<n:
    # deterministic orthogonal completion via full SVD
    Qfull=np.linalg.svd(V,full_matrices=True)[0]
    W=Qfull[:,r:]
   else:
    W=np.zeros((n,0))
   A=V.T@M@V
   B=V.T@M@W
   C=W.T@M@W
   assert_close(V.T@G@V,np.eye(r))
   assert_close(V.T@G@W,np.zeros((r,n-r)))
   assert_close(W.T@G@W,C-B.T@np.linalg.solve(A,B))
   drop=np.trace(A)-r-np.linalg.slogdet(A)[1]+np.trace(B.T@np.linalg.solve(A,B))
   assert_close(D(M)-D(G),drop)
   assert D(step(M,V,lam))<=D(M)+2e-10
   assert np.min(np.linalg.eigvalsh(step(M,V,lam)))>0
   checks+=2

# Global persistent excitation from cyclic but differently sized random subspaces
for n in [2,3,4]:
 for trial in range(15):
  basis=orthonormal(n,n)
  Vlist=[basis[:,j:j+1] for j in range(n)]
  Vlist.append(orthonormal(n,max(1,n-1)))
  Y=rng.standard_normal((n,n)); M=.5*np.eye(n)+Y@Y.T
  lam=float(rng.uniform(.15,.85))
  d0=D(M)
  for it in range(2500):
   M=step(M,Vlist[it%len(Vlist)],lam)
  assert_close(M,np.eye(n),atol=1e-7,rtol=0)
  assert D(M)<d0+1e-11
  checks+=1

# The two-step Jacobian is lambda I + (1-lambda) projection in each subspace.
for theta in [.02,.1,.4,.9,1.3]:
 for lam in [.2,.5,.85]:
  u=np.array([[1.],[0.]])
  v=np.array([[math.cos(theta)],[math.sin(theta)]])
  t=1-lam
  tr=2*lam+t*t*math.cos(theta)**4
  rp=(tr+math.sqrt(tr*tr-4*lam*lam))/2
  rm=lam*lam/rp
  assert rp<1 and rp>rm>lam*lam>0
  def basis_sym(x):
   return np.array([[x[0],x[2]/math.sqrt(2)],[x[2]/math.sqrt(2),x[1]]])
  def flatten(X):
   return np.array([X[0,0],X[1,1],math.sqrt(2)*X[0,1]])
  # Instead compute product derivative explicitly
  def linear(E,vec):
   W=np.eye(2)-vec@vec.T
   return lam*E+t*W@E@W
  L=np.column_stack([flatten(linear(linear(basis_sym(np.eye(3)[j]),u),v)) for j in range(3)])
  assert_close(np.sort(np.linalg.eigvals(L).real), np.sort([rp,rm,lam*lam]),atol=1e-12)
  # Finite-difference Jacobian for nonlinear full epoch
  eps=1e-6
  Jfd=np.column_stack([flatten((step(step(np.eye(2)+eps*basis_sym(np.eye(3)[j]),u,lam),v,lam)-np.eye(2))/eps) for j in range(3)])
  assert_close(Jfd,L,atol=3e-6,rtol=1e-6)
  checks+=2

# Rate boundary and standard forgetting anisotropy
for lam in [.2,.5,.75]:
 for theta in [.1,.02,.005]:
  tr=2*lam+(1-lam)**2*math.cos(theta)**4
  rp=(tr+math.sqrt(tr*tr-4*lam*lam))/2
  ratio=(1-rp)/(theta*theta)
  target=2*(1-lam)/(1+lam)
  if theta<=.005: assert_close(ratio,target,atol=1e-4,rtol=1e-4)
  u=np.array([1.,0.]);v=np.array([math.cos(theta),math.sin(theta)])
  EF=lam*np.outer(u,u)+np.outer(v,v)
  cond=np.linalg.cond(EF)
  if theta<=.005: assert_close(cond*theta*theta,(1+lam)**2/lam,atol=.001,rtol=.0002)
  checks+=1
print('PASS',checks,'deterministic numerical assertions')
