import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(314159)
checks=0
worst=0.0

def predicted(n,J,L,K):
 c=-np.cos(np.pi/n); a=J*(1-c); kc=np.sqrt(2*a*L/n)
 if K<kc: return n*J*c-L, 0.0,0.0
 if K< a: return n*J*c-n*K*K/a+L,K/a,2.0
 return n*(J-2*K)+L,1.0,2.0

def energy(spins,n,J,L,K):
 r=spins[:n];p,q=spins[n:];return J*np.einsum('ij,ij->',r,np.roll(r,-1,axis=0))+K*(r.sum(axis=0)@(p+q))+L*(p@q)

def cone(n,m,s):
 q=(n-1)*np.pi/n; j=np.arange(n); rad=np.sqrt(1-m*m)
 rim=np.array([rad*np.cos(j*q),rad*np.sin(j*q),np.full(n,m)]).T
 if s==0:hub=np.array([[1,0,0],[-1,0,0]])
 else:
  # resultant (0,0,-s) and two unit vectors
  p=np.sqrt(1-s*s/4)
  hub=np.array([[p,0,-s/2],[-p,0,-s/2]])
 return np.vstack([rim,hub])

for n in (5,7,9,11):
 for J in (0.7,1.3):
  a=J*(1+np.cos(np.pi/n))
  for L in (0.2,0.4*n*a):
   kc=np.sqrt(2*a*L/n)
   for K in (0.3*kc,0.999*kc,1.001*kc,(kc+a)/2,0.999*a,1.001*a,1.4*a):
    E,m,s=predicted(n,J,L,K)
    witness=cone(n,m,s)
    gap=abs(energy(witness,n,J,L,K)-E)
    worst=max(worst,gap);assert gap<2e-11,(n,J,L,K,gap);checks+=1
    # Numeric lower bound for arbitrary independent spins via actual energy and Fourier inequality
    for _ in range(30):
     x=rng.normal(size=(n+2,3));x/=np.linalg.norm(x,axis=1)[:,None]
     eng=energy(x,n,J,L,K)
     assert eng+1e-9>=E,(n,J,L,K,eng,E)
     checks+=1
    # Nonlinear 2D optimization without using theorem
    def obj(x):
     m,ss=x;return n*J*(-np.cos(np.pi/n))+n*a*m*m-n*K*m*ss+L*(ss*ss/2-1)
    ret=minimize(obj,x0=[0.46,0.9],bounds=[(0,1),(0,2)],method='L-BFGS-B',options={'ftol':1e-14,'gtol':1e-12})
    assert ret.fun>=E-1e-8 and ret.fun<=E+1e-6,(ret.fun,E,n,J,L,K)
    checks+=1

# Equality manifold at the critical point
for n in (5,7,9,11):
 J=1.2; a=J*(1+np.cos(np.pi/n));L=0.3*n*a;kc=np.sqrt(2*a*L/n)
 for m in np.linspace(0,kc/a,18):
  s=2*a*m/kc
  E=n*J*(-np.cos(np.pi/n))-L
  err=abs(energy(cone(n,m,s),n,J,L,kc)-E)
  assert err<1e-10,(n,m,err)
  checks+=1
  # The two hubs interpolate from opposite to parallel at coexistence.
  hu=cone(n,m,s)[-2:]
  assert abs((hu[0]@hu[1])-(s*s/2-1))<1e-12
  checks+=1

# Local oriented plaquette chirality in the noncoplanar regime.
for n in (5,7,9,11):
 J=1.2; a=J*(1+np.cos(np.pi/n));L=0.3*n*a;kc=np.sqrt(2*a*L/n)
 for K in np.linspace(1.03*kc,0.97*a,21):
  m=K/a; s=2; z=cone(n,m,s); rim=z[:n];h=z[-2:].sum(axis=0)
  chi=np.einsum('j,ij->i',h,np.cross(rim,np.roll(rim,-1,axis=0)))
  assert np.max(abs(abs(chi)-2*(1-m*m)*np.sin(np.pi/n)))<1e-11
  assert np.max(abs(chi-chi.mean()))<1e-11
  checks+=2

# Direct nonconvex spin search for isolated sample points
for n,J,L,K_multiple in ((5,1,1,0.8),(5,1,1,1.2),(5,1,1,1.6),(7,1,1,1.15),(7,1,1,2.5)):
 a=J*(1+np.cos(np.pi/n));kc=np.sqrt(2*a*L/n);K=K_multiple*kc
 E,_,_=predicted(n,J,L,K)
 def f(x):
  z=x.reshape(n+2,3)
  r=z/np.maximum(np.linalg.norm(z,axis=1)[:,None],1e-12)
  return energy(r,n,J,L,K)
 vals=[]
 for _ in range(4):
  z=rng.normal(size=(n+2,3))
  res=minimize(f,z.ravel(),method='L-BFGS-B',options={'maxiter':1000,'ftol':1e-13,'gtol':1e-8})
  vals.append(res.fun)
 best=min(vals)
 assert best<=E+2e-5,(n,J,L,K,best,E)
 assert best>=E-1e-7,(n,J,L,K,best,E)
 checks+=1
print('PASS',checks,'assertions; max witness error',worst)
