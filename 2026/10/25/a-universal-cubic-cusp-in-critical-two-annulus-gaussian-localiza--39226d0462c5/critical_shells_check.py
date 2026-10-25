"""Numerical corroboration for critical Gaussian ring spectral cusp.
Run: python critical_shells_check.py (NumPy/SciPy); finite checks do not prove asymptotics.
"""
import numpy as np
from scipy.special import gammaln
from numpy.polynomial.legendre import leggauss
from math import sqrt,exp,pi

def spectrum(R,kappa):
    delta=1+kappa*R**(-1/3)
    n0=int(R)
    radius=int(max(15, 10*R**(1/3)*(1+abs(kappa)**0.5)))
    n=np.arange(n0-radius,n0+radius+1)
    nodes,weights=leggauss(24)
    eig=np.zeros(len(n))
    for v in [-delta,delta]:
        t=R+v*sqrt(R)+nodes/2
        val=np.exp(n[:,None]*np.log(t)[None,:]-t[None,:]-gammaln(n[:,None]+1))
        eig+=val@weights/2
    return n,eig,delta

def P(y,k): return k*y*y-y**4/12-2*y/3

def critical_roots(k):
    rr=np.roots([1.,0.,-6*k,2.])
    return sorted(float(np.real(x)) for x in rr if abs(np.imag(x))<1e-7)

if __name__=='__main__':
    checks=0
    for k in [-1.,0.,0.2,0.7,1.]:
      roots=critical_roots(k)
      for R in [100000,1000000]:
        n,ev,a=spectrum(R,k)
        inds=np.where((ev[1:-1]>=ev[:-2])&(ev[1:-1]>ev[2:]))[0]+1
        globalmax=n[np.argmax(ev)]
        y=(globalmax-R)/R**(1/3)
        lead=2*exp(-a*a/2)/sqrt(2*pi*R)
        shape=(ev.max()/lead-1)*R**(2/3)
        expected=P(roots[0],k)
        assert abs(y-roots[0]) < 0.6,(k,R,y,roots[0])
        assert abs(shape-expected) < 0.3,(k,R,shape,expected)
        checks+=2
        print(f'k={k:+.1f} R={R} integer peaks={((n[inds]-R)/R**(1/3)).round(3).tolist()} critical_roots={np.round(roots,3)} maxscaled={y:.4f} shape={shape:.5f} predicted={expected:.5f}')
    print('PASS',checks,'finite numerical assertions')
