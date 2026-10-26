import numpy as np
from numpy.linalg import norm
rng=np.random.default_rng(532087)
angles=np.arange(4096)*np.pi/2048
c=np.cos(angles);s=np.sin(angles)
def rho2(A):
 H=(A+A.conj().T)/2;K=(A-A.conj().T)/(2j)
 vals=np.linalg.eigvalsh(c[:,None,None]*H+s[:,None,None]*K)
 return np.mean(np.max(abs(vals),axis=1)**2)
def low(A):return norm(A.conj().T@A + A@A.conj().T,ord=2)/4
def numrad(A):
 H=(A+A.conj().T)/2;K=(A-A.conj().T)/(2j)
 vals=np.linalg.eigvalsh(c[:,None,None]*H+s[:,None,None]*K)
 return np.max(np.max(abs(vals),axis=1))
for j in range(300):
 X=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); A=X-np.trace(X)/2*np.eye(2)
 assert abs(rho2(A)-np.trace(A.conj().T@A).real/4)<1e-9
 assert abs(rho2(A)-low(A))<1e-9
for j in range(300):
 X=rng.normal(size=(2,2));A=(X+X.T)*np.exp(1j*rng.uniform(-3,3))
 assert abs(rho2(A)-low(A))<1e-8
for j in range(300):
 X=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));A=X
 if abs(np.trace(A))>.1 and norm(A-np.trace(A)/2*np.eye(2))>.1:
  if norm(A-A.conj().T)>1e-8: pass
 assert rho2(A)+1e-9>=low(A)
 assert rho2(A)<=numrad(A)**2+1e-5
for j in range(300):
 u=rng.normal(size=(2,))+1j*rng.normal(size=(2,));v=rng.normal(size=(2,))+1j*rng.normal(size=(2,)); A=np.outer(u,v.conj())
 # force nilpotent via orthogonal projection
 v=v - u*np.vdot(u,v)/np.vdot(u,u)
 A=np.outer(u,v.conj())
 assert abs(rho2(A)-numrad(A)**2)<1e-5
print('PASS 1200 families: trace-zero, phase Hermitian, arbitrary, nilpotent')
