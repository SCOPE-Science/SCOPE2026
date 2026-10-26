"""Check exact one-step map and sharp stability/tuning formulas for the stated bilinear update."""
import math
import numpy as np
import sympy as sp

eta, beta, lam, sig = sp.symbols('eta beta lam sig', real=True)
d=1-lam
G=sp.Matrix([[1+eta*beta*sig, -eta*d*sig], [eta*d*sig,1+eta*beta*sig]])
r2=sp.factor((G.T*G)[0,0])
assert sp.simplify((G.T*G)-r2*sp.eye(2))==sp.zeros(2)
assert sp.simplify((r2-1)-(2*eta*beta*sig+eta**2*(beta**2+d**2)*sig**2))==0

mu,L=sp.symbols('mu L',positive=True)
c=beta**2+d**2
eta_star=-2*beta/(c*(L+mu))
assert sp.simplify((r2.subs(sig,mu)-r2.subs(sig,L)).subs(eta,eta_star))==0
assert sp.simplify(r2.subs({sig:mu,eta:eta_star})-(1-4*beta**2*mu*L/(c*(L+mu)**2)))==0

rng=np.random.default_rng(19345)
num=0
for n in [1,2,3,7]:
 for lam0 in [0.1,1.,2.3]:
  for beta0 in [-2.,-0.5,0.,0.01,0.7]:
   for eta0 in [0.015, 0.1, 0.4]:
    B=rng.normal(size=(n,n)); K=B.T@B+np.eye(n)*0.2
    sigs=np.linalg.eigvalsh(K)
    M=np.block([[np.eye(n)+eta0*beta0*K, -eta0*(1-lam0)*K],
                [eta0*(1-lam0)*K, np.eye(n)+eta0*beta0*K]])
    formula=max(math.hypot(1+eta0*beta0*s,eta0*(1-lam0)*s) for s in sigs)
    norm=np.linalg.svd(M,compute_uv=False)[0]
    assert abs(norm-formula)<2e-12*max(1,formula),(n,lam0,beta0,eta0,norm,formula)
    num+=1
for mu0,L0 in [(1.,1.),(0.1,3.),(1.,10.),(5.,10.)]:
 for b in [-2.,-0.1]:
  for l in [0.1,1.,2.1]:
   c0=b*b+(1-l)**2
   e=-2*b/(c0*(mu0+L0))
   r=lambda t: max(math.hypot(1+t*b*s,t*(1-l)*s) for s in (mu0,L0))
   target=math.sqrt(1-4*b*b*mu0*L0/(c0*(mu0+L0)**2))
   assert abs(r(e)-target)<2e-7
   assert all(r(e)<=r(e*f)+1e-12 for f in [0,0.01,.25,.5,.9,1.01,1.1,2,4])
print(f'PASS: symbolic identities and {num} arbitrary-SPD matrix cases, plus exact-rate stationary checks')
# Test the identity-alignment obstruction and the spectral-shape phase transition.
for n in [2,3,6]:
 for eta0 in [0.001,0.03,0.35]:
  for beta0 in [-4.,-0.5,0.,0.1,3.]:
   for lam0 in [0.1,1.,2.5]:
    rng = np.random.default_rng(int(1000*n+10000*eta0+100*abs(beta0)+10*lam0))
    ortho = np.linalg.qr(rng.normal(size=(n,n)))[0]
    eigs = np.linspace(-2,2,n)
    K=ortho@np.diag(eigs)@ortho.T
    M=np.block([[np.eye(n)+eta0*beta0*K, -eta0*(1-lam0)*K],
                [eta0*(1-lam0)*K, np.eye(n)+eta0*beta0*K]])
    spectral_radius = max(abs(np.linalg.eigvals(M)))
    assert spectral_radius >= 1-1e-12

rng=np.random.default_rng(123987)
for n in [1,2,4,8]:
 for j in range(40):
  K=rng.normal(size=(n,n)); U,s,Vt=np.linalg.svd(K)
  K=U@np.diag(s+0.5)@Vt
  s=s+0.5
  b=10**rng.uniform(-1,1)
  delta=rng.uniform(-2,2)
  eta0=10**rng.uniform(-3,0)
  M=np.block([[np.eye(n)-eta0*b*K@K.T, -eta0*delta*K],
              [eta0*delta*K.T, np.eye(n)-eta0*b*K.T@K]])
  expected=max(math.hypot(1-eta0*b*t*t,eta0*delta*t) for t in s)
  assert abs(np.linalg.norm(M,2)-expected) < 1e-11*max(1,expected)
  lo,hi=min(s),max(s)
  T=delta**2; H=b*b*(hi**2-lo**2)
  if T>=H:
   optim=b/(T+b*b*lo*lo)
   rate=math.sqrt(T/(T+b*b*lo*lo))
  else:
   optim=2*b/(T+b*b*(lo*lo+hi*hi))
   rate=math.sqrt(1-4*b**4*lo*lo*hi*hi/(T+b*b*(lo*lo+hi*hi))**2)
  obj=lambda t: max(math.hypot(1-t*b*x*x,t*delta*x) for x in s)
  assert abs(obj(optim)-rate)<3e-9
  assert all(rate<=obj(optim*f)+3e-10 for f in [0.,0.5,0.75,.95,1.05,1.5,2.,10.])
print('PASS: indefinite-no-go, 160 aligned arbitrary-matrix SVD and optimal-step cases')
