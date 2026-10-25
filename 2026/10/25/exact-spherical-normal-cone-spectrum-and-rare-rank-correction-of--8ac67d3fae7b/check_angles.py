#!/usr/bin/env python3
"""Finite numerical corroboration for the two-row partial matching polytope's Gaussian normal-cone angles."""
import itertools, math
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr, ndtri, erfcx

SQRT2PI=math.sqrt(2*math.pi)

def analytic(n):
    # Gaussian CDF integral via integration by parts; B is a genuine one-dimensional integral.
    a=(1-2.0**(-n))/n
    def integrand(t):
        phi=math.exp(-t*t/2)/SQRT2PI
        return phi*ndtr(t)**(n-1)*erfcx(t/2)/(2*math.sqrt(2))
    b=quad(integrand,0,max(12,5*math.sqrt(2*math.log(n+1))),epsabs=1e-13,epsrel=1e-12)[0]
    p0=2.0**(-2*n)
    p1=2.0**(1-n)*(a/2+b)
    p2=(1-p0-2*n*p1)/(n*(n-1))
    return p0,p1,p2,a,b

def exact_rankone(n,seed=1,samples=200000):
    # Different computation from integral: maximize among complete finite list of matchings.
    v=[np.zeros((2,n),dtype=np.float64)]
    for i in range(2):
      for j in range(n):
        x=np.zeros((2,n));x[i,j]=1;v.append(x)
    for j in range(n):
      for k in range(n):
        if j!=k:
          x=np.zeros((2,n));x[0,j]=1;x[1,k]=1;v.append(x)
    vv=np.stack([x.reshape(-1) for x in v]); rk=np.sum(vv,axis=1)
    rng=np.random.default_rng(seed+n)
    rank_counts=np.zeros(3,dtype=np.int64)
    for start in range(0,samples,2000):
      g=rng.normal(size=(min(2000,samples-start),2*n))
      idx=(g@vv.T).argmax(axis=1)
      rank_counts+=np.bincount(rk[idx].astype(int),minlength=3)
    return rank_counts/samples

for n in range(2,9):
  p0,p1,p2,a,b=analytic(n)
  assert min(p0,p1,p2)>0
  assert abs(p0+2*n*p1+n*(n-1)*p2-1)<1e-13
  probs=exact_rankone(n,samples=50000 if n<=5 else 120000)
  theory=np.array([p0,2*n*p1,n*(n-1)*p2])
  err=max(abs(probs-theory))
  se=max(math.sqrt(x*(1-x)/(50000 if n<=5 else 120000)) for x in theory)
  assert err<6*se+0.003,(n,err,se)
  print('n=',n,'theory',theory,'direct',probs,'max_err',round(err,5),'p0,p1,p2=',(p0,p1,p2))
for n in (10,50,100,1000):
  p0,p1,p2,a,b=analytic(n)
  correction=(2*n*p1/(2**(1-n))-1)*math.sqrt(math.pi*math.log(n))
  print('n=',n,'relative_correction_scaled',correction,'rank1_total',2*n*p1)
print('GAUSSIAN_NORMAL_CONE_CHECKS_PASS')
