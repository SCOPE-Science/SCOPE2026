import numpy as np
import sympy as s
from scipy.optimize import brentq

E,z,a,b,c,u = s.symbols('E z a b c u',real=True)
examined=0
for m in range(1,6):
 K=s.zeros(m)
 for j in range(m-1): K[j,j+1]=c;K[j+1,j]=c
 H=s.zeros(m+1)
 H[0,0]=u+a*(z+1/z)
 H[0,1]=b*(1+1/z);H[1,0]=b*(1+z)
 for i in range(m):
  for j in range(m):H[i+1,j+1]=K[i,j]
 p=s.det(E*s.eye(m)-K)
 d=s.det(E*s.eye(m-1)-K[1:,1:]) if m>1 else s.Integer(1)
 predicted=s.expand((u-E)*p+a*(z+1/z)*p+b*b*(2+z+1/z)*d)
 actual=s.expand(s.det(H-E*s.eye(m+1)))
 assert s.simplify(actual-(-1)**m*predicted)==0, (m,s.simplify(actual-(-1)**m*predicted))
 assert s.expand(p-c**m*s.chebyshevu(m,E/(2*c)))==0
 assert s.expand(d-c**(m-1)*s.chebyshevu(m-1,E/(2*c)))==0
 examined+=1

ranks=0
for m in range(1,13):
 for (a,b,c) in [(1.2,0.75,1.0),(0.75,1.3,0.7)]:
  K=np.diag(c*np.ones(m-1),1)+np.diag(c*np.ones(m-1),-1)
  be,bevec=np.linalg.eigh(K)
  weights=bevec[0,:]**2
  def G(t): return np.sum(weights/(be-t))
  edges=[be[0]-50]+list(be)+[be[-1]+50]
  roots=[]
  for i in range(m):
   left=edges[i]+(1e-8 if i>0 else 0)
   right=edges[i+1]-1e-8
   roots.append(brentq(lambda t:G(t)-a/b**2,left,right,xtol=1e-13))
  assert len(roots)==m
  for j,root in enumerate(roots):
   ons=root+2*a
   for theta in [0,np.pi/7,np.pi/2,np.pi,1.77]:
    zz=np.exp(1j*theta)
    h=np.zeros((m+1,m+1),dtype=complex)
    h[0,0]=ons+2*a*np.cos(theta)
    h[0,1]=b*(1+1/zz);h[1,0]=b*(1+zz)
    h[1:,1:]=K
    spectrum=np.linalg.eigvalsh(h)
    assert abs(spectrum[j]-root)<1e-9,(m,j,root,theta,spectrum)
    assert all(abs(spectrum[t]-root)>1e-8 for t in range(m+1) if t!=j)
    weights_col=np.linalg.solve(K-root*np.eye(m), np.eye(m)[:,0])
    psi=np.concatenate(([1.],-b*(1+zz)*weights_col))
    assert np.linalg.norm(h@psi-root*psi)<1e-8
    ranks+=1
print('VERIFY_OK exact_characteristic_orders=',examined,'tuning_spectra=',ranks,'motif_lengths=1..12','band_ranks=1..m')
