"""Reproducible independent quadrature for the Brownian snapshot Bayes law.

Requires numpy and scipy. Execute: python verify.py
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc, gammaln
from scipy.stats import beta, norm


def limit_error(a, b):
    return ((a/(a+b))*betainc(a+1,b,.5)
            +(b/(a+b))*(1-betainc(a,b+1,.5)))


def excess_and_threshold(a,b,delta):
    density = lambda u: beta.pdf(u,a,b)
    def weighted_difference(y):
        return quad(lambda u:(2*u-1)*density(u)*norm.pdf((y-u)/delta)/delta,
                    0,1,epsabs=2e-12,epsrel=2e-12,points=[.5],limit=160)[0]
    threshold=brentq(weighted_difference,.01,.99,xtol=1e-13)
    low=quad(lambda u:(1-2*u)*density(u)*norm.sf((threshold-u)/delta),
             0,.5,epsabs=3e-12,points=[.5],limit=160)[0]
    high=quad(lambda u:(2*u-1)*density(u)*norm.cdf((threshold-u)/delta),
              .5,1,epsabs=3e-12,points=[.5],limit=160)[0]
    return low+high,threshold


def exact_uniform(delta):
    h=1/(2*delta)
    return (.25+.5*norm.sf(h)
            +2*delta**2*(norm.cdf(h)-.5-h*norm.pdf(h)))


def exact_symmetric_floor(q):
    return .5-np.exp(gammaln(q+.5)-gammaln(q+1))/(2*np.sqrt(np.pi))


def main():
    comparisons=0
    for a,b in [(1.,1.),(.75,1.25),(2.,3.)]:
        fhalf=beta.pdf(.5,a,b)
        for delta in [.2,.1,.05,.025,.0125]:
            excess,threshold=excess_and_threshold(a,b,delta)
            assert excess > 0 and .01 < threshold < .99
            ratio=excess/(delta**2*fhalf)
            assert (ratio > 0 and (delta>.05 or abs(ratio-1)<.06)),(a,b,delta,ratio)
            if a==b==1.:
                formula=exact_uniform(delta)
                assert abs(formula-(limit_error(a,b)+excess))<2e-10
            comparisons+=1
        e1,_=excess_and_threshold(a,b,.05)
        e2,_=excess_and_threshold(a,b,.025)
        e3,_=excess_and_threshold(a,b,.0125)
        ratios=np.array([e1/.05**2,e2/.025**2,e3/.0125**2])/fhalf
        assert (abs(ratios[-1]-1)<abs(ratios[0]-1) or
                max(abs(ratios-1))<1e-9),ratios
    for q in [.01,.1,1.,5.,20.]:
        explicit=exact_symmetric_floor(q)
        assert abs(explicit-limit_error(q,q))<3e-13
    for q in [.001,.0005]:
        assert abs(exact_symmetric_floor(q)/(q*np.log(2))-1)<.003
    for q in [500.,1000.]:
        assert abs((.5-exact_symmetric_floor(q))*2*np.sqrt(np.pi*q)-1)<.001
    print(f"PASS: {comparisons} independent full-likelihood threshold/quadrature tests;"
          " symmetric exact formula, beta reduction and weak/strong switching limits")

if __name__=='__main__':
    main()
