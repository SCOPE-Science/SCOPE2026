#!/usr/bin/env python3
"""Finite numerical diagnostics for a state-inference theorem for switching traps.
Requires numpy and scipy. These finite checks are not substitutes for the proof.
"""
from math import exp, gamma, lgamma, log, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gammainc, gammaincc, roots_genlaguerre
from scipy.stats import chi2

CHECKS = 0

def require(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1

def odds(a, b, dimension, radius):
    """Posterior off/on odds as a Gamma-scale Gaussian integral."""
    # Shift the log integrand to avoid underflow near high-dimensional saddles.
    center = -b - dimension * log(2)/2 - radius**2/4
    def piece(v, power):
        if v <= 0:
            return 0.0
        lp = (a-1)*log(v)-b*v-dimension*np.log1p(v)/2-radius**2/(2*(1+v))
        return v**power * exp(max(-740, min(600, lp-center)))
    def integral(power):
        return sum(quad(piece, low, high, args=(power,),epsabs=1e-10,
                        epsrel=1e-10,limit=250)[0]
                   for low,high in [(0,1),(1,3),(3,np.inf)])
    return integral(1)/integral(0)

def boundary(a,b,d):
    if odds(a,b,d,0) >= 1:
        return None
    upper=max(12.,4*sqrt(d))
    return brentq(lambda r:odds(a,b,d,r)-1,0,upper,xtol=1e-10)

def floor(a,b):
    return (b*gammaincc(a,b)+a*gammainc(a+1,b))/(a+b)

def numerical():
    for a,b in [(0.5,0.5),(1,2),(3,1),(0.4,0.2),(4,4),(0.25,2)]:
        require(0<floor(a,b)<0.5,'Bayes error floor must be positive')
        for d in [1,2,4,16,64]:
            rs=[0.,0.5,1.,2.,4.,8.,16.,32.]
            values=[odds(a,b,d,r) for r in rs]
            require(all(x<y for x,y in zip(values,values[1:])),
                    'Posterior odds must rise strictly with radius')
            t=boundary(a,b,d)
            if t is None:
                require(values[0]>=1,'No positive boundary requires off decision at origin')
            else:
                require(values[0]<1,'Positive boundary requires on decision at origin')
                require(abs(odds(a,b,d,t)-1)<1e-8,'Exact crossing condition')
        for d in [256,1024]:
            predicted=2*d+8*(b-a)+16*(1+b-a)/d
            left=sqrt(predicted-8)
            right=sqrt(predicted+8)
            t=brentq(lambda r:odds(a,b,d,r)-1,left,right)
            require(abs(t*t-predicted)<1.0 if d==256 else abs(t*t-predicted)<0.06,
                    'High-dimensional two-term boundary expansion')
    # An independent normal-Gamma-mixture calculation of the Bayes error.
    a=b=1.; d=64
    t=boundary(a,b,d)
    v,w=roots_genlaguerre(160,a-1)
    w=w/gamma(a)
    err_on=np.dot(w,chi2.sf(t*t/(1+v/b),d))
    err_off=np.dot(w*v/a,chi2.cdf(t*t/(1+v/b),d))
    exact=0.5*(err_on+err_off)
    require(abs(exact-0.3270696998)<1e-6,'Independent Bayes risk quadrature')
    require(floor(1,1)<exact<0.5,'Irreducible positive Bayes floor')
    print('PASS',CHECKS,'finite numerical assertions')
    print('Symmetric unit-shape infinite-dimensional Bayes error:',floor(1,1))
    print('Symmetric d=64 Bayes error:',exact)

if __name__=='__main__': numerical()
