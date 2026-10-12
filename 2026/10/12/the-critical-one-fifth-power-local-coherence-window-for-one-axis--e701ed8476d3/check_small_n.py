import numpy as np
from functools import reduce
x=np.array([[0,1],[1,0]],complex);y=np.array([[0,-1j],[1j,0]],complex);z=np.diag([1.,-1.]);I=np.eye(2)
def tensor(mats):return reduce(np.kron,mats)
for n in [3,4,5]:
 J={k:sum((tensor([o/2 if j==i else I for j in range(n)]) for i in range(n))) for k,o in [('x',x),('y',y),('z',z)]}
 t=.17; e=.8; psi=np.ones(2**n,dtype=complex)/np.sqrt(2**n)
 psi=np.exp(-1j*t*np.diag(J['z'])**2)*psi; rho=np.outer(psi,psi.conj());
 # local dephasing offdiagonal e^Hamming
 for i in range(2**n):
  for j in range(2**n):rho[i,j]*=e**((i^j).bit_count())
 means={k:np.trace(rho@o).real for k,o in J.items()};cov=np.empty((2,2));
 for a,k in enumerate(['y','z']):
  for b,l in enumerate(['y','z']):cov[a,b]=np.trace(rho@(J[k]@J[l]+J[l]@J[k])/2).real - means[k]*means[l]
 A=1+(n-1)*e*e/2*(1-np.cos(2*t)**(n-2)); B=(n-1)*e*np.sin(t)*np.cos(t)**(n-2)
 form=np.array([[A,B],[B,1]])*n/4
 print(n,'means',means['x'], n*e/2*np.cos(t)**(n-1),'err',np.max(np.abs(form-cov)),cov,form)
