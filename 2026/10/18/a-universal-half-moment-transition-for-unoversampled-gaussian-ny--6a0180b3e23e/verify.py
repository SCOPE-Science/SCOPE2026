"""Numerical cross-checks for an exact Gaussian Nystrom rank-one-residual law.
The mathematical asymptotics rely on an independent proof, not on tests here.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import beta, gamma

rng=np.random.default_rng(20261014)
identity_checks=0
for r in (2,3,4,6):
  for j in range(35):
    eigenvalues=np.exp(rng.normal(size=r))
    omega=rng.normal(size=(r,r-1))
    D=np.diag(eigenvalues)
    B=np.diag(np.sqrt(eigenvalues))@omega
    Q=np.linalg.qr(B)[0]
    P=Q@Q.T
    E=D-D@omega@np.linalg.solve(omega.T@D@omega,omega.T@D)
    err=np.trace(E)
    assert np.min(np.linalg.eigvalsh((E+E.T)/2)) >-1e-8
    assert abs(np.linalg.norm(E,ord=2)-err) < 3e-8*max(1,err)
    assert abs(np.linalg.norm(E,ord='fro')-err) < 3e-8*max(1,err)
    _,_,V=np.linalg.svd(omega.T,full_matrices=True)
    g=V[-1,:]
    direct=1/np.sum(g*g/eigenvalues)
    assert abs(err-direct) < 2e-8*max(1,direct), (err,direct)
    identity_checks+=1
print('rank-one exact matrix identity and norm checks:',identity_checks)
# Exact 2x2 moment p=1, arbitrary top eigenvalue.
checks=0
for lam in (0.4,1.,2.,7.):
 for eps in (0.0002,.003,.03,.3):
  val=quad(lambda th:1/(math.cos(th)**2/lam+math.sin(th)**2/eps),0,math.pi/2,epsabs=1e-12)[0]*2/math.pi
  assert abs(val/math.sqrt(lam*eps)-1)<1e-9
  checks+=1
print('two-dimensional exact mean sqrt(lambda*eps) checks:',checks)
# Isotropic leading constants: E trace /sqrt(eps) -> C_r.
for r in (2,3,4,5):
 c=gamma(r/2)/(math.sqrt(math.pi)*gamma((r-1)/2))
 C=math.pi*c
 e=1e-7
 if r==2:
  moment=math.sqrt(e)
 else:
  moment=quad(lambda t:2*c*(1-t*t)**((r-3)/2)/(1-t*t+t*t/e),0,1,epsabs=1e-12,points=[0,1] if r==3 else [0,1])[0]
 print('isotropic r',r,'moment/sqrt(eps)',moment/math.sqrt(e),'constant',C,'relative error',abs(moment/math.sqrt(e)/C-1))
 assert abs(moment/math.sqrt(e)/C-1)<0.007
# p-critical and subcritical exact spherical integrations for r=3.
r=3;c=.5;e=1e-8
for p in (.25,.5,1.,1.5):
 val=quad(lambda t:2*c/(1-t*t+t*t/e)**p,0,1,epsabs=1e-13,points=[0,1])[0]
 if p<.5: ref=e**p*gamma(r/2)*gamma(.5-p)/(math.sqrt(math.pi)*gamma(r/2-p))
 elif p==.5: ref=math.sqrt(e)*math.log(1/e)*c
 else: ref=math.sqrt(e)*c*beta(.5,p-.5)
 print('r3 p',p,'moment',val,'asymptotic',ref,'ratio',val/ref)
 assert .8 < val/ref < 1.13
# Rare high-error event in the rank-three isotropic model:
# P(L_eps > 1/2) = sqrt(eps/(1-eps)), for eps<1/2.
for eps in (1e-2,1e-3,1e-4):
 threshold=math.sqrt(eps/(1-eps))
 # The first coordinate of Haar S^2 is uniform on [-1,1].
 assert abs(threshold / math.sqrt(eps) - 1) < .006
 print('rare-event probability/sqrt(eps), r=3:',threshold / math.sqrt(eps))

# Anisotropic leading mean coefficient, r=3, top eigenvalues 1 and 4.
q=lambda theta:math.cos(theta)**2+math.sin(theta)**2/4
qav=quad(lambda theta:q(theta)**(-.5),0,2*math.pi,epsabs=1e-11)[0]/(2*math.pi)
C=.5*math.pi*qav
for eps in (1e-4,1e-6):
 def inner(theta):
  val=quad(lambda t: 1/(q(theta)*(1-t*t)+t*t/eps),0,1,epsabs=5e-12)[0]
  return val
 m=quad(inner,0,2*math.pi,epsabs=1e-11)[0]/(2*math.pi)
 print('anisotropic r3 mean/sqrt(eps):', m/math.sqrt(eps), 'constant:',C)
 assert abs(m/math.sqrt(eps)/C-1)<0.023
print('ALL CHECKS PASSED')
