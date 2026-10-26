"""Reproducible checks for the critical hub-immigration contact-process limit.
Runs with Python 3, numpy, scipy, sympy. No external data or network access.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve
from scipy.special import hyp1f1
import sympy as s

checks=0
u, h, B=s.symbols('u h B',positive=True,real=True)
f0=u**(h-1)*(1-u)*s.exp(B*u)
f1=u**h*s.exp(B*u)
# PDMP stationary equations: -(v_z f_z)' + jumps in - jumps out =0.
assert s.simplify(-s.diff(-u*f0,u)+f1-(h+B*u)*f0)==0
assert s.simplify(-s.diff((1-u)*f1,u)+(h+B*u)*f0-f1)==0
assert s.simplify(-u*f0+(1-u)*f1)==0
checks+=3

# Integral relations for all integer h where possible and explicit moments.
for hh in (0.3,0.75,1.,2.,3.):
 for bb in (0.,0.25,1.4,3.):
  Z=quad(lambda x:x**(hh-1)*math.exp(bb*x),0,1,epsabs=1e-11)[0]
  a=lambda r:quad(lambda x:x**(hh+r-1)*math.exp(bb*x),0,1,epsabs=1e-11)[0]/Z
  assert abs(Z-hyp1f1(hh,hh+1,bb)/hh)<3e-9
  # Stationary moments for smooth polynomial test functions
  for r in range(5):
   ar=a(r);ar1=a(r+1);ar2=a(r+2)
   lhs=(r+hh)*ar-(r+hh+1-bb)*ar1-bb*ar2
   assert abs(lhs)<1e-9,(hh,bb,r,lhs)
   checks+=1
  checks+=1


def finite(m,beta,eta):
 lam=beta/math.sqrt(m)
 n=2*(m+1)
 Q=lil_matrix((n,n),dtype=float)
 for z in (0,1):
  for k in range(m+1):
   i=z*(m+1)+k
   def add(j,rate):
    if rate>0:
     Q[i,j]+=rate
     Q[i,i]-=rate
   if z and k<m: add(i+1,lam*(m-k))
   if k: add(i-1,k)
   add((1-z)*(m+1)+k, 1. if z else eta+lam*k)
 Q=Q.tocsc()
 A=Q.transpose().tolil(); b=np.zeros(n)
 A[-1,:]=np.ones(n);b[-1]=1.
 pi=spsolve(A.tocsc(),b)
 assert np.min(pi)>-5e-13 and abs(pi.sum()-1)<1e-10
 assert np.max(np.abs(pi@Q))<1e-9
 kk=np.tile(np.arange(m+1),2)
 zz=np.repeat([0.,1.],m+1)
 E=lambda v:np.dot(pi,v)
 p=E(zz);eK=E(kk);eK2=E(kk**2); eHK=E(kk*zz)
 U=kk/(beta*math.sqrt(m))
 return dict(p=p,u=E(U),u2=E(U**2),hu=E(zz*U),eK=eK,m=m,
  leafcov=(eK2-eK)/(m-1)-eK**2/m if m>1 else 0,
  hubleafcov=math.sqrt(m)*(eHK/m-p*eK/m),
  flux_resid=np.max(np.abs(pi@Q)))

for beta,eta in ((0.8,0.5),(1.2,0.75),(2.0,1.5)):
 b=beta**2
 Z=quad(lambda x:x**(eta-1)*math.exp(b*x),0,1,epsabs=1e-11)[0]
 a=lambda r:quad(lambda x:x**(eta+r-1)*math.exp(b*x),0,1,epsabs=1e-11)[0]/Z
 var=a(2)-a(1)**2
 print('beta eta',beta,eta,'limit hub',a(1),'limit var',var)
 for m in (10,50,200,500):
  q=finite(m,beta,eta)
  print('m',m,'hub',round(q['p'],8),'u',round(q['u'],8),
   'hubleafcorr',round(q['hubleafcov'],8), 'leafcorr',round(q['leafcov'],8),
   'target',round(beta*var,8),round(beta**2*var,8))
  assert abs(q['p']-q['u']-q['hu']*beta/math.sqrt(m))<1e-10 # exact leaf balance
  checks+=4
 print()
print('PASS',checks,'checks')
