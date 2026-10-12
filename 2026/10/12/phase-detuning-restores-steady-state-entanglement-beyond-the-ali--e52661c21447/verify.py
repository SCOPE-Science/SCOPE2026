"""Numerical Lyapunov and partial-transpose consistency checks for the phase-control theorem."""
import math
import numpy as np

O2=np.array([[0.,1.],[-1.,0.]])
OMEGA=np.kron(np.eye(2), O2)

def direct(J,gamma,y,r,phi1,phi2):
  S=math.sinh(2*r);K=math.cosh(2*r); aa=y*K/2; mm=-y*S/2
  A=np.array([[-gamma/2,0,0,J],[0,-gamma/2,-J,0],[0,J,-gamma/2,0],[-J,0,0,-gamma/2]],float)
  D=np.zeros((4,4))
  for i,phi in [(0,phi1),(2,phi2)]:
    M=mm*np.exp(2j*phi)
    D[i:i+2,i:i+2]=gamma*np.array([[aa+M.real,M.imag],[M.imag,aa-M.real]])
  V=np.linalg.solve(np.kron(np.eye(4),A)+np.kron(A,np.eye(4)), -D.reshape(-1)).reshape(4,4)
  Vpt=V.copy(); L=np.diag([1,1,1,-1]);Vpt=L@V@L
  eig=sorted(abs(np.linalg.eigvals(1j*OMEGA@Vpt)))
  return eig[0],V,np.max(np.abs(A@V+V@A.T+D))

def theory(J,gamma,y,r,phi1,phi2):
  t=2*J/gamma;mu=1/(1+t*t);chi=t/(1+t*t)
  S=math.sinh(2*r);z=S*abs(math.cos(phi1-phi2))
  return y/2*(math.sqrt(1+(1-mu*mu)*z*z)-chi*z)

rng=np.random.default_rng(142)
for k in range(1500):
  J=10**rng.uniform(-2,1); gamma=10**rng.uniform(-1,1);
  r=rng.uniform(0,2);y=rng.uniform(1,4)
  p1,p2=rng.uniform(-math.pi,math.pi,2)
  got,V,res=direct(J,gamma,y,r,p1,p2); want=theory(J,gamma,y,r,p1,p2)
  assert res<1e-10,(k,res)
  assert abs(got-want)<1e-9, (k,got,want)
  mu=gamma*gamma/(gamma*gamma+4*J*J)
  zstar=math.sqrt(mu/(1-mu*mu));S=math.sinh(2*r)
  if S>=zstar:
    # choose phase with effective amplitude exactly optimal
    d=math.acos(zstar/S)
    nup,_V,_res=direct(J,gamma,y,r,0,d)
    assert abs(2*nup/y-1/math.sqrt(1+mu))<1e-9

# Fixed coupling and squeezing phase scan, verify interior optimum and non-monotone restoration
for t in [0.1,0.25,1.,2.,8.]:
  gamma=1.; J=t/2;y=1.07
  mu=1/(1+t*t);zstar=math.sqrt(mu/(1-mu*mu));rstar=math.asinh(zstar)/2
  for mult in [0.6,1,1.7,4.]:
    r=mult*rstar;S=math.sinh(2*r)
    target=y/2*(1/math.sqrt(1+mu) if S>=zstar else math.sqrt(1+(1-mu*mu)*S*S)-t/(1+t*t)*S)
    vals=[direct(J,gamma,y,r,0,math.pi*j/160)[0] for j in range(81)]
    assert min(vals)+1e-4 >=target,(t,mult,min(vals),target)
print('VERIFY_OK: 1500 random direct Lyapunov/PPT comparisons, 5 coupling families; phase-plateau checks')
