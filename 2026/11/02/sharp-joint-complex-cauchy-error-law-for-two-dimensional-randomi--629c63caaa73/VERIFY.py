"""Independent finite numerical checks of a two-mode Gaussian Ritz limit."""
import numpy as np
from numpy.linalg import det
from scipy.linalg import eig

A=np.diag([-1.,0.,1.])
v=np.array([0.,1.,0.]); u=np.array([1.,0.,1.])/np.sqrt(2); w=np.array([1.,0.,-1.])/np.sqrt(2)

def wed(e): return np.column_stack((np.sqrt(1-e*e)*v+e*u,w))

def d(x,y): return x[0]*y[1]-x[1]*y[0]

def cgauss(rng,*shape):return (rng.standard_normal(shape)+1j*rng.standard_normal(shape))/np.sqrt(2)


def run():
 rng=np.random.default_rng(20261025)
 ncheck=0
 for eps in [0.,1e-3,0.13,0.82]:
  P=wed(eps)
  assert np.allclose(P.conj().T@P,np.eye(2),atol=1e-14)
  assert np.allclose(P.conj().T@A@P,[[0,-eps],[-eps,0]],atol=2e-14)
  ncheck+=2
 for j in range(600):
  O=cgauss(rng,3,2)
  V=O.conj().T@v; U=O.conj().T@u; W=O.conj().T@w
  if abs(d(V,U))<1e-3: continue
  z=-d(W,U)/d(V,U); g=-d(V,W)/d(V,U)
  assert np.linalg.norm(W+z*V+g*U)<1e-10
  P=wed(1e-5); H=O.conj().T@A@P; C=O.conj().T@P
  roots,ys=eig(H,C)
  near=int(np.argmin(abs(roots)))
  mu=roots[near]; beta=ys[1,near]/ys[0,near]
  errz=abs(mu/1e-5-z)/(1+abs(z))
  errg=abs(beta/1e-5-g)/(1+abs(g))
  assert errz<.025,(errz,j)
  assert errg<.025,(errg,j)
  R=(P@ys[:,near])
  theta=np.arccos(np.clip(abs(np.vdot(R,v))/np.linalg.norm(R),0.,1.))
  rho=(R.conj()@A@R)/(R.conj()@R)
  assert abs(theta/1e-5-np.sqrt(1+abs(g)**2))/(1+abs(g))<.03
  assert abs(rho.real/1e-10+2*g.real)/(1+abs(g))<.05
  ncheck+=5
 N=120000
 V=cgauss(rng,N,2);U=cgauss(rng,N,2);W=cgauss(rng,N,2)
 D=V[:,0]*U[:,1]-V[:,1]*U[:,0]
 Z=-(W[:,0]*U[:,1]-W[:,1]*U[:,0])/D
 G=-(V[:,0]*W[:,1]-V[:,1]*W[:,0])/D
 for r in [.4,1.,2.,4.]:
  empirical=np.mean(abs(Z)>r); expected=1/(1+r*r)
  assert abs(empirical-expected)<.012,(r,empirical,expected)
  ncheck+=1
 for r in [1.,2.,5.]:
  empirical=np.mean(np.sqrt(1+abs(G)**2)>r); expected=1/(r*r)
  assert abs(empirical-expected)<.012
  ncheck+=1
 for r in [.5,2.,5.]:
  empirical=np.mean(abs(2*G.real)>r); expected=1-r/np.sqrt(r*r+4)
  assert abs(empirical-expected)<.012,(r,empirical,expected)
  ncheck+=1
 # Correlated joint Cauchy law: radial square of the pair follows beta-prime(2,1)
 # P(|Z|^2+|G|^2>t)=(1+2t)/(1+t)^2 for t>=0.
 for t in [.5,1.,3.,8.]:
  empirical=np.mean(abs(Z)**2+abs(G)**2>t)
  expected=(1+2*t)/(1+t)**2
  assert abs(empirical-expected)<.012,(t,empirical,expected)
  ncheck+=1
 for r,t in [(1.,1.),(.5,2.),(2.,.5)]:
  empirical=np.mean((abs(Z)>r)&(abs(G)>t))
  expected=1/(1+r*r+t*t)
  assert abs(empirical-expected)<.012,(r,t,empirical,expected)
  ncheck+=1
 print('PASS',ncheck,'checks')



run()

import numpy as np
from scipy.linalg import eig
rng=np.random.default_rng(20261025)
def cg(*shape):return (rng.normal(size=shape)+1j*rng.normal(size=shape))/np.sqrt(2)
checks=0
for trial in range(1000):
 n=4; Q,_=np.linalg.qr(cg(n,n)); L=np.array([-3.,0.,1.5,5.]); A=Q@np.diag(L)@Q.conj().T
 lam=L[1];v=Q[:,1];u=(Q[:,0]+Q[:,2])/np.sqrt(2);w=np.exp(0.7j)*(Q[:,0]-Q[:,2])/np.sqrt(2) # nonzero complex coupling
 H=A-lam*np.eye(n)
 b=H@w;a=H@u;s=np.vdot(b,a)/np.vdot(b,b)
 ap=a-s*b; sigma=np.linalg.norm(ap); bn=np.linalg.norm(b)
 assert sigma>0
 O=cg(n,2);V=O.conj().T@v;BB=O.conj().T@(b/bn);RR=O.conj().T@(ap/sigma)
 z1,z2=-np.linalg.solve(np.column_stack((V,BB)),RR)
 M=-sigma*z1; Beta=-s+sigma/bn*z2
 eps=1.e-6
 W=np.column_stack((np.sqrt(1-eps**2)*v+eps*u,w))
 EE,Y=eig(O.conj().T@A@W,O.conj().T@W)
 j=np.argmin(np.abs(EE-lam)); m=(EE[j]-lam)/eps;beta=Y[1,j]/Y[0,j]/eps
 assert abs(m-M)/(1+abs(M))<0.02,(m,M,trial)
 assert abs(beta-Beta)/(1+abs(Beta))<0.02,(beta,Beta,trial)
 Psi=W@Y[:,j]
 R=(np.vdot(Psi,A@Psi)/np.vdot(Psi,Psi)).real
 R_lim=np.vdot(u+Beta*w,H@(u+Beta*w)).real
 assert abs((R-lam)/eps**2-R_lim)/(1+abs(R_lim))<.04
 checks+=3
print('general analytic-to-eigensolver consistency PASS',checks)

