import numpy as np
from numpy.linalg import norm,eigvalsh
from scipy.linalg import expm
rng=np.random.default_rng(2037)
passes=0
for n,edges in [(3,[(0,1),(1,2)]),(4,[(0,1),(1,2),(2,3),(3,0)]),(5,[(0,1),(1,2),(2,3),(3,4),(4,0),(0,2)]),(6,[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5),(1,4)])]:
 for trial in range(5):
  m=len(edges); theta=rng.uniform(-np.pi,np.pi,n); u=np.exp(1j*theta)/np.sqrt(n); gamma=rng.uniform(.2,1.4); weighted=rng.uniform(.2,1.8,m); eps=rng.uniform(-.7,.7)
  wvec=[]; jumps=[]; Lt=np.zeros((n,n),complex); L0=np.zeros((n,n),complex)
  for z,(i,j) in enumerate(edges):
   eta=u[j]/u[i]; v=np.eye(n,dtype=complex)[:,i]+eta*np.eye(n,dtype=complex)[:,j]; w=np.eye(n,dtype=complex)[:,i]-eta*np.eye(n,dtype=complex)[:,j]
   l=np.outer(v,w.conj()); jumps.append(l); wvec.append(w);Lt+=weighted[z]*np.outer(w,w.conj());L0+=np.outer(w,w.conj())
  P=np.outer(u,u.conj()); C=rng.uniform(2,4); V=rng.normal(size=n)
  H=C*np.eye(n)-Lt+eps*np.diag(V)
  delta=norm((np.eye(n)-P)@H@u)
  np.testing.assert_allclose(delta**2,eps**2*np.var(V),rtol=1e-10,atol=1e-12); passes+=1
  lam2=np.sort(eigvalsh(L0))[1]; c=4*gamma*lam2/n
  def ell(X):
   out=-1j*(H@X-X@H)
   for l in jumps:
    B=l.conj().T@l
    out+=gamma*(l@X@l.conj().T-.5*(B@X+X@B))
   return out
  # stationarity solve with trace constraint
  superop=np.column_stack([ell(np.eye(n*n)[k].reshape(n,n,order='F')).reshape(n*n,order='F') for k in range(n*n)])
  eq=superop.conj().T@superop+np.outer(np.eye(n).reshape(-1,order='F'),np.eye(n).reshape(-1,order='F'))
  rhs=np.eye(n).reshape(-1,order='F')
  rho=np.linalg.solve(eq,rhs).reshape(n,n,order='F');rho=(rho+rho.conj().T)/2
  np.testing.assert_allclose(np.trace(rho),1,atol=1e-9); np.testing.assert_allclose(ell(rho),0,atol=1e-8);passes+=2
  assert eigvalsh(rho).min()>-1e-8;passes+=1
  q=1-np.trace(P@rho).real; M=2*norm(H,2)+8*gamma*m
  assert q + 1e-9 >= delta**2/M**2 and q<=(4*delta**2/(c*c+4*delta**2)+1e-9);passes+=2
  if trial==0:
   H0=C*np.eye(n)-Lt
   vecs=np.linalg.eigh(L0)[1]; rho0=np.outer(vecs[:,1],vecs[:,1].conj())
   # changing H to H0 for evolution bound
   Hsave=H;H=H0
   for t in [.04,.15,.6]:
    rt=(expm(superop*0) if False else None)
    A=np.column_stack([ell(np.eye(n*n)[k].reshape(n,n,order='F')).reshape(-1,order='F') for k in range(n*n)])
    rhot=(expm(A*t)@rho0.reshape(-1,order='F')).reshape(n,n,order='F')
    qt=(1-np.trace(P@rhot).real)
    assert qt <= np.exp(-c*t)*(1-np.trace(P@rho0).real)+1e-8
    passes+=1
   H=Hsave
# Frustrated triangle has no common annihilation kernel.
ns=3
frustrated=[(0,1,1.0),(1,2,1.0),(2,0,np.exp(0.7j))]
ww=[]
for i,j,eta in frustrated:
 e=np.eye(ns,dtype=complex)
 w=e[:,i]-eta*e[:,j]
 v=e[:,i]+eta*e[:,j]
 assert abs(np.vdot(w,v))<1e-12
 ww.append(w)
 passes+=1
Q=np.column_stack([x.conj() for x in ww]).T
assert np.linalg.matrix_rank(Q)==3
passes+=1
# Test the derivative spectral coefficient is exactly saturated.
n=4
edges=[(0,1),(1,2),(2,3)]
Ls=np.zeros((n,n)); js=[]
for i,j in edges:
 w=np.eye(n)[:,i]-np.eye(n)[:,j]
 v=np.eye(n)[:,i]+np.eye(n)[:,j]
 js.append(np.outer(v,w))
 Ls+=np.outer(w,w)
u=np.ones(n)/np.sqrt(n); P=np.outer(u,u)
lam,vec=np.linalg.eigh(Ls)
rho=np.outer(vec[:,1],vec[:,1]); gam=1.21
h=7*np.eye(n)-.7*Ls
rhs=-1j*np.trace(P@(h@rho-rho@h))
for j in js:
 B=j.T@j
 rhs+=gam*np.trace(P@(j@rho@j.T-.5*(B@rho+rho@B)))
assert np.isclose(rhs,4*gam*lam[1]/n,rtol=0,atol=1e-11)
passes+=1
print('checks',passes)
