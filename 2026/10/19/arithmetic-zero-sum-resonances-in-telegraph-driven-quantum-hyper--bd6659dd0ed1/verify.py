#!/usr/bin/env python3
"""Independent noisy-density-matrix reconstruction of telegraph-induced occupation laws."""
import itertools, math
import numpy as np
from scipy.linalg import expm

def phi(omega, t, rate):
    omega = abs(omega)
    if omega < 1e-14:return 1.
    discriminant=rate*rate-4*omega*omega
    if abs(discriminant)<1e-13:return math.exp(-rate*t)*(1+rate*t)
    if discriminant>0:
        s=math.sqrt(discriminant)
        return math.exp(-rate*t)*(math.cosh(s*t)+(rate/s)*math.sinh(s*t))
    s=math.sqrt(-discriminant)
    return math.exp(-rate*t)*(math.cos(s*t)+(rate/s)*math.sin(s*t))

def moment(subset, h, rate, t):
    if not subset:return 1.
    return sum(phi(sum(sign*h[j] for sign,j in zip(signs,subset)),t,rate)
               for signs in itertools.product((-1,1),repeat=len(subset)))/2**len(subset)

def predicted(h,rate,t):
    n=len(h)
    ys=np.array(list(itertools.product((0,1),repeat=n)))
    out=np.zeros(2**n)
    for mask in range(2**n):
      subset=[j for j in range(n) if mask>>j&1]
      coeff=moment(subset,h,rate,t)
      if subset:
        parity=(-1)**(ys[:,subset].sum(axis=1))
      else:parity=np.ones(len(ys))
      out+=coeff*parity/(2**n)
    return out

def dense(h,rate,t):
    n=len(h);d=2**n
    I2=np.eye(2); X=np.array([[0,1],[1,0]])
    H=np.zeros((d,d))
    for j in range(n):
      matrices=[X if k==j else I2 for k in range(n)]
      block=matrices[0]
      for a in matrices[1:]:block=np.kron(block,a)
      H+=h[j]*block
    Id=np.eye(d*d)
    C=np.kron(np.eye(d),H)-np.kron(H.T,np.eye(d))
    g=np.block([[-1j*C-rate*Id,rate*Id],[rate*Id,1j*C-rate*Id]])
    init=np.zeros((d,d),complex);init[0,0]=1
    initv=init.reshape(-1,order='F')
    v=expm(g*t)@np.r_[initv*.5,initv*.5]
    rho=(v[:d*d]+v[d*d:]).reshape((d,d),order='F')
    return rho.diagonal().real

def limit(h):
    n=len(h)
    ys=np.array(list(itertools.product((0,1),repeat=n)))
    out=np.zeros(2**n)
    for mask in range(2**n):
      subset=[j for j in range(n) if mask>>j&1]
      if not subset:
       w=1.
      else:
       w=sum(abs(sum(s*h[j] for s,j in zip(signs,subset)))<1e-13 for signs in itertools.product((-1,1),repeat=len(subset)))/2**len(subset)
      out+=w*(-1)**(ys[:,subset].sum(axis=1))/2**n if subset else w/2**n
    return out

def run():
    tests=0;maxerr=0
    for h in ((1.,2.),(1.,1.),(1.,2.,3.),(1.,2.,3.25),(1.,2.,4.)):
     for rate,t in ((.7,.25),(1.2,1.3),(3.,2.2)):
      d=dense(h,rate,t);p=predicted(h,rate,t)
      assert min(p)>-1e-13
      assert abs(sum(p)-1)<1e-13
      err=max(abs(p-d));maxerr=max(maxerr,err);tests+=len(p)
      assert err<3e-12,(h,rate,t,err)
    for h in ((1.,2.,3.),(1.,2.,3.2),(1.,2.,4.),(1.,1.),(1.,2.,4.,8.)):
       p=limit(h)
       assert min(p)>-1e-13
       assert abs(sum(p)-1)<1e-13
       if h==(1.,2.,3.):
          assert abs(.5*sum(abs(p-1/8))-.125)<1e-13
          assert abs(p[0]-5/32)<1e-13 and abs(p[1]-3/32)<1e-13
       if h in ((1.,2.,3.2),(1.,2.,4.),(1.,2.,4.,8.)):
          assert max(abs(p-1/len(p)))<1e-13
    # Slow resonance: the full finite-time law approaches the proven single-pole profile.
    eps=0.12;rate=1.1;h=(1.,2.,3.+eps);t=110.
    q=rate-math.sqrt(rate*rate-4*eps*eps)
    a=.5*(1+rate/math.sqrt(rate*rate-4*eps*eps))
    tv=.5*sum(abs(predicted(h,rate,t)-1/8))
    expected=(a/8)*math.exp(-q*t)
    assert abs(tv/expected-1)<1e-9,(tv,expected)
    assert q>0 and abs(q/(eps*eps)-2/rate)<0.07
    # The best asymptotic rate is uniquely at the critical switching frequency.
    for lam in (.02,.08,.19,.21,.5,2.,10.):
       gap=lam-(math.sqrt(lam*lam-.2*.2) if lam>.2 else 0.)
       assert gap < .2
    print('VERIFY_OK dense_state_probabilities=',tests,'limit_profiles=5 slow_resonance=1 optimum_grid=7 max_error=',format(maxerr,'.2e'))
if __name__=='__main__':run()
