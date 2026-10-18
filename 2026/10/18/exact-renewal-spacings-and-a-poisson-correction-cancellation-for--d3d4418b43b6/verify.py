#!/usr/bin/env python3
"""Reproducible mathematical checks for one-dimensional isolated-Poisson renewal spacings."""
import math
import numpy as np
import sympy as sp
from numpy.random import default_rng


def transforms(mu, radius, s):
    x = mu/(mu+s)
    e = math.exp(-(mu+s)*radius)
    a = x*e
    b = x*(1.0-e)
    # Algebraic rearrangement avoids catastrophic cancellation when mu*radius is large.
    omx = s/(mu+s)
    phi = a*(omx+a)/(omx*(1+a)+a*a)
    return phi, a, b


def direct_phi(mu, radius, s):
    c = mu*radius
    u = s/mu
    E = math.exp(c*(1+u))
    return (1+u*E)/(1+u*E+u*(1+u)*E*E)


def retained(mu, radius, s, n):
    ph, _, _ = transforms(mu, radius, s)
    return ph/(n-(n-1)*ph)


def coefficient(lam, tau, s):
    t=lam*tau
    m=math.exp(t)/lam
    return math.exp(t)/lam**2*(math.exp(t/2)-1-t)*s*s/(1+m*s)**2


def main():
    checks=0
    z,c=sp.symbols('z c', real=True,positive=True)
    A=sp.exp(-(1+z)*c)/(1+z)
    B=(1-sp.exp(-(1+z)*c))/(1+z)
    phi=sp.cancel(A*(1-B)/(1-B-A*B))
    closed=(1+z*sp.exp(c*(1+z)))/(1+z*sp.exp(c*(1+z))+z*(1+z)*sp.exp(2*c*(1+z)))
    assert sp.simplify(phi-closed)==0;checks+=1
    mean=sp.simplify(-sp.diff(phi,z).subs(z,0))
    assert sp.simplify(mean-sp.exp(2*c))==0;checks+=1
    second=sp.simplify(sp.diff(phi,z,2).subs(z,0)-2*mean**2)
    assert sp.simplify(second-2*sp.exp(2*c)*(sp.exp(c)-1-2*c))==0;checks+=1
    for mu in [0.6,1,2.3,17]:
      for radius in [0.03,0.2,0.4,0.9]:
        for s in [0,0.01,0.1,0.5,2,7]:
          ph,a,b=transforms(mu,radius,s)
          assert abs(ph-direct_phi(mu,radius,s))<2e-12;checks+=1
          p=math.exp(-mu*radius)
          omx=s/(mu+s)
          fl=p*(omx+a)/(omx*(1+a)+a*a)
          assert abs(ph-(a/p)*fl)<2e-12;checks+=1
          for n in [1,2,6,20]:
            calc=retained(mu,radius,s,n)
            assert abs(calc - ((ph/n)/(1-(1-1/n)*ph)))<2e-12;checks+=1
    for lam in [0.7,1.0,1.6]:
      for tau in [0.2,1,2,4]:
        t=lam*tau; m=math.exp(t)/lam
        for s in [0.08,0.3,0.9,2.0]:
          lim=1/(1+m*s)
          pred=coefficient(lam,tau,s)
          n=2000; val=retained(n*lam,tau/(2*n),s,n)
          # First-order error scales as 1/n with bounded second-order remainder.
          assert abs(n*(val-lim)-pred)<0.025;checks+=1
    lo,hi=1.0,4.0
    for _ in range(90):
      mid=(lo+hi)/2
      if math.exp(mid/2)-1-mid>0: hi=mid
      else: lo=mid
    tstar=(lo+hi)/2
    assert abs(tstar-2.5128624172523395)<1e-10;checks+=1
    for t in [0.1,0.9,2.1,2.8,4.0]:
      sign=math.exp(t/2)-1-t
      assert (sign>0)==(t>tstar);checks+=1
    rng=default_rng(40109)
    # The two-sided isolate of point index i occurs iff gaps[i-1] and gaps[i] are long.
    for cval in [0.3,1.0]:
      gaps=rng.exponential(scale=1.0,size=600000)
      ids=np.flatnonzero((gaps[:-1]>cval)&(gaps[1:]>cval))+1
      coords=np.concatenate(([0.],np.cumsum(gaps)))
      intervals=np.diff(coords[ids])
      expected=math.exp(2*cval)
      assert len(intervals)>40000;checks+=1
      assert abs(float(np.mean(intervals))/expected-1)<0.022;checks+=1
      assert abs(float(np.corrcoef(intervals[:-1],intervals[1:])[0,1]))<0.023;checks+=1
    print('PASS: checks=',checks,'; critical parameter=',tstar)


if __name__=='__main__':
    main()
