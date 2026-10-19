"""Numerical cross-check of all-order critical phase distribution in spherical shells.
Uses scipy: zero finding plus quantile distribution, not a proof of any limit.
"""
import math
import numpy as np
from scipy import special, optimize
from shell_phase_check import bessel_zeros
for d in (2,3,4,5,6):
  n=400
  nu=d/2
  alpha=bessel_zeros(nu-1,n+1)
  lo,hi=alpha[n-1],alpha[n]
  f=lambda x:x**nu*special.jv(nu,x)
  U=[]; Q=[]
  for m in range(1,n):
    X=optimize.brentq(lambda x:f(x)-f(alpha[m-1]),lo,hi,xtol=1e-10)
    U.append((X-lo)/(hi-lo)); Q.append(alpha[m-1]/X)
  U=np.array(U);Q=np.array(Q)
  assert len(U)==399 and np.all((U>0)&(U<1))
  assert np.max(np.abs(Q-np.arange(1,n)/n))<.02
  for eps in (.1,.2,.3):
    obs=np.mean(np.abs(U-.5)<eps)
    pred=math.sin(math.pi*eps)**(2/(d-1))
    print(f'd={d:2d} n={n} eps={eps:.1f} observed={obs:.5f} limiting={pred:.5f} error={abs(obs-pred):.5f}')
print('DISTRIBUTION_CHECKS_PASSED')
