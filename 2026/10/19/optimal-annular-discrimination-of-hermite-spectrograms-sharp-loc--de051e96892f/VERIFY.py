#!/usr/bin/env python3
"""Numerical checks for the two-level Hermite phase-space contrast theorem."""
import numpy as np
from scipy.special import gammaln, gammaincc
from scipy.optimize import brentq
from scipy.integrate import quad

def density(t, k):
    return np.exp(-t + k*np.log(t) - gammaln(k+1)) if t>0 else (1. if k==0 else 0.)

def gap(t,n,m):
    return density(t,m)-density(t,n)

def threshold(n,m):
    return np.exp((gammaln(m+1)-gammaln(n+1))/(m-n))

def mode(n,m):
    h=threshold(n,m)
    return brentq(lambda t: derivative_gap(t,n,m),h+1.e-8,max(m+20*np.sqrt(m+1),h+30),xtol=1e-11)

def derivative_gap(t,n,m):
    return density(t,m)*(m/t-1)-density(t,n)*(n/t-1)

def endpoints(n,m,area):
    t0=threshold(n,m)
    pk=mode(n,m)
    # left lies strictly between threshold and mode, while right exceeds mode
    left=brentq(lambda t: gap(t,n,m)-gap(t+area,n,m),t0+1e-9,pk-1e-9,xtol=5e-12)
    return left,left+area

def optimum(n,m,A):
    a,b=endpoints(n,m,A)
    return (gammaincc(m+1,a)-gammaincc(m+1,b))-(gammaincc(n+1,a)-gammaincc(n+1,b))

def contrast_direct(n,m,a,b):
    return quad(lambda x:gap(x,n,m),a,b,epsabs=1e-12)[0]

def stable_coeff(n,m,A):
    a,b=endpoints(n,m,A)
    return 1/(4*(1/derivative_gap(a,n,m)-1/derivative_gap(b,n,m)))

def test():
    count=0
    for n,m in [(0,1),(0,3),(1,2),(2,5),(10,11),(50,55)]:
      for A in [0.3,1.,3.,10.]:
        a,b=endpoints(n,m,A)
        d=optimum(n,m,A)
        assert a>threshold(n,m) and a<mode(n,m)<b
        assert abs(gap(a,n,m)-gap(b,n,m))<2e-10
        assert abs(d-contrast_direct(n,m,a,b))<1e-10
        for shift in [0.01,0.05,0.15]:
            if a-shift>0:
                assert d>contrast_direct(n,m,a-shift,b-shift)
            assert d>contrast_direct(n,m,a+shift,b+shift)
        count+=1
    # stability: remove and add equal small areas at the two annulus boundaries,
    # distributing mass inversely proportional to boundary slopes
    n,m,A=1,3,2.
    a,b=endpoints(n,m,A)
    l=derivative_gap(a,n,m)
    r=-derivative_gap(b,n,m)
    S=1/l+1/r
    target=1/(4*S)
    for h in [1e-2,5e-3,2e-3,1e-3]:
        # remove internal layers: [a,a+x], [b-y,b] and insert external:
        # The two boundary lengths use reciprocal-slope proportions.
        x=h*(1/l)/S
        y=h*(1/r)/S
        # defect cost: removing inside [a,a+x],[b-y,b], inserting [a-x,a],[b,b+y]
        defect=(quad(lambda t:gap(t,n,m),a,a+x)[0] + quad(lambda t:gap(t,n,m),b-y,b)[0]
                -quad(lambda t:gap(t,n,m),a-x,a)[0] - quad(lambda t:gap(t,n,m),b,b+y)[0])
        delta=2*h
        print('stability',h,'ratio',defect/delta**2,'target',target)
        assert abs(defect/delta**2-target)<0.05*target
    # Gaussian scaling for c positive
    def phi(x): return np.exp(-x*x/2)/np.sqrt(2*np.pi)
    for n,m,s in [(200,220,1.0),(800,840,1.0),(200,228,2.),(800,856,2.)]:
      N=n+1; A=s*np.sqrt(N); c=(m-n)/np.sqrt(N)
      a,b=endpoints(n,m,A)
      alpha=(a-N)/np.sqrt(N)
      val=optimum(n,m,A)
      ideal=quad(lambda u:phi(u-c)-phi(u),alpha,alpha+s)[0]
      print('scaling',n,m,s,alpha,val,ideal,'relerr',abs(val-ideal)/ideal)
      assert ideal>0 and abs(val-ideal)<0.08
    # Fixed level gap: sqrt(N)*contrast/k tends to an integral of u*normal_density.
    for n,k,s in [(200,1,1.5),(500,2,1.0),(800,2,2.0)]:
      N=n+1
      a,b=endpoints(n,n+k,s*np.sqrt(N))
      alpha=(a-N)/np.sqrt(N)
      scaled=optimum(n,n+k,s*np.sqrt(N))*np.sqrt(N)/k
      limit=phi(alpha)-phi(alpha+s)
      assert limit>0 and abs(scaled-limit)<0.02
    print('PASS:',count,'endpoint families, sharp stability, both asymptotic regimes')
if __name__=='__main__': test()
