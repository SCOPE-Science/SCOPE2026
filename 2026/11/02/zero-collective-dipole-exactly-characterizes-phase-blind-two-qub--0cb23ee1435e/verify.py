#!/usr/bin/env python3
"""Independent finite-dimensional checks for the phase-blind charger theorem.
Requires numpy and scipy. Exact proof is in RESULT.md; these are consistency checks.
"""
import numpy as np
from scipy.linalg import expm

I2=np.eye(2,dtype=complex)
S=np.array([[0,1],[0,0]],dtype=complex)
SP=S.conj().T
N=SP@S
PAULI=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1.,-1.]).astype(complex)]
def k3(a,b,c):return np.kron(np.kron(a,b),c)
sm1=k3(S,I2,I2);sm2=k3(I2,S,I2);smb=k3(I2,I2,S)
HINT=(sm1+sm2)@smb.conj().T+(sm1.conj().T+sm2.conj().T)@smb
HFREE=(sm1.conj().T@sm1+sm2.conj().T@sm2)
HB=smb.conj().T@smb
A=np.array([0,1,-1,0],complex)/np.sqrt(2)
B=np.array([0,1,1,0],complex)/np.sqrt(2)
KET00=np.array([1,0,0,0],complex)
KET11=np.array([0,0,0,1],complex)

checks=0
def verify(cond,context=''):
 global checks
 checks+=1
 if not cond: raise AssertionError((checks,context))

def map_energy(a,b,c,d,e,gamma,delta,g,t):
 omega=np.hypot(delta,2*np.sqrt(2)*g)
 u=np.cos(omega*t/2)-1j*delta/omega*np.sin(omega*t/2)
 v=-1j*2*np.sqrt(2)*g/omega*np.sin(omega*t/2)
 pp=abs(v)**2
 k=np.conj(a)*b+np.conj(b)*d
 return (e+pp*(abs(b)**2+abs(d)**2-e*(abs(a)**2+2*abs(b)**2+abs(d)**2))+
         2*np.real(np.sqrt(e*(1-e))*np.exp(-1j*gamma)*np.conj(u)*v*k)),pp

def evolve(a,b,c,d,e,gamma,delta,g,t):
 chi=a*KET00+b*B+c*A+d*KET11
 bat=np.array([np.sqrt(1-e),np.sqrt(e)*np.exp(1j*gamma)])
 H=(1.1*HFREE+(1.1+delta)*HB+g*HINT)
 U=expm(-1j*H*t)
 psi=U@np.kron(chi,bat)
 obs=float(np.vdot(psi,HB@psi).real)
 return obs,psi

def local_equalizer(psi):
 # unnormalized charger columns associated with battery 0 and 1
 cols=psi.reshape(4,2)
 u,v=cols[:,0],cols[:,1]
 p0=float(np.vdot(u,u).real);p1=float(np.vdot(v,v).real)
 if min(p0,p1)<1e-10:return None
 D=np.outer(v,v.conj())/p1-np.outer(u,u.conj())/p0
 r=np.array([np.trace(D@np.kron(x,I2)).real for x in PAULI])
 s=np.array([np.trace(D@np.kron(I2,x)).real for x in PAULI])
 T=np.array([[np.trace(D@np.kron(x,y)).real for y in PAULI] for x in PAULI])
 # First analyzer axis restricted to x-z plane.
 n=np.array([r[2],0.,-r[0]])
 if np.linalg.norm(n)<1e-12:n=np.array([0.,0.,1.])
 else:n/=np.linalg.norm(n)
 sn=T.T@n
 m=np.cross(s,sn)
 if np.linalg.norm(m)<1e-12:
  w=s if np.linalg.norm(s)>1e-12 else sn
  if np.linalg.norm(w)<1e-12:m=np.array([0.,0.,1.])
  else:
   q=np.array([1.,0.,0.]) if abs(w[0])<.8*np.linalg.norm(w) else np.array([0.,1.,0.])
   m=np.cross(w,q);m/=np.linalg.norm(m)
 else:m/=np.linalg.norm(m)
 verify(abs(r@n)<1e-9 and abs(s@m)<1e-9 and abs(n@T@m)<1e-9,'Bloch zero diagonal')
 NAX=sum(x*X for x,X in zip(n,PAULI));MAX=sum(x*X for x,X in zip(m,PAULI))
 _,V=np.linalg.eigh(NAX);_,W=np.linalg.eigh(MAX)
 Q=np.kron(V,W)
 projected=Q.conj().T@cols
 for j in range(4):
  denom=np.sum(np.abs(projected[j,:])**2)
  if denom>1e-11:
   ep=abs(projected[j,1])**2/denom
   verify(abs(ep-p1)<2e-10,'local equalization')
 return p1

def main():
 rng=np.random.default_rng(40_2026)
 for trial in range(350):
  z=rng.normal(size=4)+1j*rng.normal(size=4);z/=np.linalg.norm(z)
  a,b,c,d=z
  delta=rng.uniform(-2,2);g=rng.uniform(.05,1.4);t=rng.uniform(.05,7)
  e=rng.uniform(.02,.98);gamma=rng.uniform(-np.pi,np.pi)
  predicted,p=map_energy(a,b,c,d,e,gamma,delta,g,t)
  observed,psi=evolve(a,b,c,d,e,gamma,delta,g,t)
  verify(abs(predicted-observed)<5e-12,'8x8 exact energy formula')
  local_equalizer(psi)
 for trial in range(200):
  # an open family of non-Bell-like, phase-blind charger states
  z=rng.normal(size=3)+1j*rng.normal(size=3);z/=np.linalg.norm(z)
  a,c,d=z;b=0j
  delta=rng.uniform(-1.3,1.3);g=rng.uniform(.2,1);t=rng.uniform(.01,9)
  e=rng.uniform(.05,.95)
  baseline=None
  for gamma in [0,.19,1.2,2.7,5.5]:
   predicted,p=map_energy(a,b,c,d,e,gamma,delta,g,t)
   observed,psi=evolve(a,b,c,d,e,gamma,delta,g,t)
   verify(abs(predicted-observed)<5e-12,'phase-blind exact 8x8 map')
   if baseline is not None:verify(abs(observed-baseline)<5e-12,'phase independence')
   baseline=observed
  A0=abs(d)**2;B0=abs(a)**2+abs(d)**2
  verify(abs(baseline-(e+p*(A0-B0*e)))<5e-12,'affine dark class')
 # Opposite transverse polarizations: coherent, separable, non-Bell witness.
 a=.5;b=0j;c=-1/np.sqrt(2);d=-.5
 for trial in range(100):
  delta=rng.uniform(-2,2);g=rng.uniform(.1,1.1);t=rng.uniform(.01,6)
  for gamma in [.13,2.2]:
   ep,p=map_energy(a,b,c,d,.3,gamma,delta,g,t)
   verify(abs(ep-(.3+p*(.25-.5*.3)))<1e-14,'product witness')
 # General non-Bell bright-cancellation class.
 for trial in range(100):
  a=(rng.normal()+1j*rng.normal())*.3
  b=(rng.normal()+1j*rng.normal())*.3
  if abs(b)<1e-9:continue
  d=-np.conj(a)*b/np.conj(b)
  c=(rng.normal()+1j*rng.normal())*.3
  z=np.array([a,b,c,d]);z/=np.linalg.norm(z)
  a,b,c,d=z
  for gamma in [0.,.8,2.7]:
   pp,_=map_energy(a,b,c,d,.35,gamma,.46,.37,2.3)
   base,_=map_energy(a,b,c,d,.35,0.,.46,.37,2.3)
   verify(abs(pp-base)<1e-13,'bright-cancellation class')
 print(f'PASS: {checks} finite-dimensional assertions; independent proof required for all-parameter statement')
if __name__=='__main__':main()
