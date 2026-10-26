"""Reproduce the two-site exponential-splitting mean-square stability law.
Requires numpy and mpmath. No random simulation is used as proof.
"""
import math
import numpy as np
import mpmath as mp
mp.mp.dps=65

def formula(a,b,v,h):
    t=mp.exp(-2*a*h); q=mp.exp(-2*b*h); E=mp.exp(v*h)
    A=(1+q*q)/2; B=(1-q*q)/2
    rho=t*(A*(E+1)+mp.sqrt(A*A*(E-1)**2+4*E*B*B))/2
    cutoff=mp.log((1-t*A)/(t*(A-t*q*q)))/h
    mu=-2*(a+b)+v/2+mp.sqrt(v*v/4+4*b*b)
    return rho,cutoff,mu

def direct(a,b,v,h):
    t=math.exp(-a*h);q=math.exp(-2*b*h)
    P=t*np.array([[(1+q)/2,(1-q)/2],[(1-q)/2,(1+q)/2]])
    E=math.exp(v*h)
    # Symmetric covariance in basis C11,C12,C22. Noise first and deterministic second.
    mats=[np.array([[1.,0.],[0.,0.]]),np.array([[0.,1.],[1.,0.]]),np.array([[0.,0.],[0.,1.]])]
    rows=[]
    for C in mats:
       Q=C.copy();Q[0,0]*=E;Q[1,1]*=E
       N=P@Q@P
       rows.append([N[0,0],N[0,1],N[1,1]])
    M=np.array(rows).T
    vals=np.linalg.eigvals(M)
    return float(max(abs(vals))),sorted([float(np.real(z)) for z in vals])

cases=0
for a in [0.2,1.,3.,9.]:
 for b in [0.15,0.7,1.,4.]:
  for v in [0.,a,2*a,2.3*a,3.5*a,10*a]:
   for h in [0.005,0.02,0.1,0.3,0.8,2.]:
    rho,cutoff,mu=formula(mp.mpf(str(a)),mp.mpf(str(b)),mp.mpf(str(v)),mp.mpf(str(h)))
    d,_=direct(a,b,v,h)
    assert math.isclose(float(rho),d,rel_tol=1.5e-12,abs_tol=3e-13),(a,b,v,h,rho,d)
    if v>0:
     assert (float(rho)<1)==(v<float(cutoff)),(a,b,v,h,rho,cutoff)
    assert float(cutoff)>2*a-1e-12
    cases+=1

# Natural two-interior-node P1 mass-lumped Dirichlet mesh on [0,1].
a=b=mp.mpf(9);v=mp.mpf('22.5')
_,_,mu=formula(a,b,v,mp.mpf('0.02'))
assert mu<0
rho1,crit1,_=formula(a,b,v,mp.mpf(1)/9)
rho2,crit2,_=formula(a,b,v,mp.mpf(2)/9)
assert rho1<1<rho2 and crit1>v>crit2
# Orthonormal e_i(x) = sqrt(22.5)*max(1-15*|x-x_i|,0).
# Squared L2 integral of triangle: amplitude**2*2/(3*15) = 1.
assert mp.mpf('22.5')*2/(3*15)==1
# Small-step derivative and asymptotic variance thresholds for varied a,b.
for a,b in [(mp.mpf(1),mp.mpf(1)),(mp.mpf(2),mp.mpf('0.3')),(mp.mpf('0.5'),mp.mpf(7))]:
 tc=2*a*(a+2*b)/(a+b)
 for h in [mp.mpf('0.0000001'),mp.mpf('0.00000001')]:
  _,crit,_=formula(a,b,0,h)
  assert abs(crit-tc)<mp.mpf('0.00001'),(crit,tc)
 for h in [mp.mpf(20),mp.mpf(50)]:
  _,crit,_=formula(a,b,0,h)
  assert abs((crit-2*a)*h-mp.log(2))<mp.mpf('0.0001'),(crit,h)
print('matrix_eigenvalue_checks:',cases)
print('natural_FE_a_b_variance:', '9', '9',str(v))
print('natural_FE_continuous_moment_exponent:',mp.nstr(mu,17))
print('natural_FE_step_1_over_9_factor:',mp.nstr(rho1,17))
print('natural_FE_step_2_over_9_factor:',mp.nstr(rho2,17))
print('natural_FE_step_1_over_9_variance_cutoff:',mp.nstr(crit1,17))
print('natural_FE_step_2_over_9_variance_cutoff:',mp.nstr(crit2,17))
print('asymptotic_cutoffs: passed')
