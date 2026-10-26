#!/usr/bin/env python3
"""Algebraic and quadrature checks for the on/off-trap stationary law.
All parameter values are dimensionless; no external data are used.
"""
import math
import numpy as np
from scipy.integrate import quad

def conditional(alpha,q):
    q=np.asarray(q,dtype=float)
    phip=np.exp(-q*q/2)*(1+q*q/alpha)**(-alpha/2)
    phim=phip*alpha/(alpha+q*q)
    return phip,phim

def stationary(alpha,q):
    p,m=conditional(alpha,q)
    return (p+m)/2

def published(alpha,q):
    q=np.asarray(q,dtype=float)
    return np.exp(-q*q/2)*(2*alpha+q*q)/(2*alpha)*(alpha/(alpha+q*q))**(alpha/2+1)

def profile(alpha,x):
    a=math.sqrt(alpha)
    k=1+alpha/2
    return k*np.exp(-a*x)-np.exp(-math.sqrt(2)*a*x)

def driving_density(alpha,x):
    a=math.sqrt(alpha)
    return a*((1+alpha/2)*np.exp(-a*x)-math.sqrt(2)*np.exp(-math.sqrt(2)*a*x))

def levymarg(alpha,x):
    x=abs(x)
    return profile(alpha,x)/x

def logchar_levy(alpha,q):
    # cos(qx)-1 removes the logarithmic Levy-density singularity at zero.
    def integrand(x):
        if x==0.0: return 0.0
        return 2*(math.cos(q*x)-1)*float(profile(alpha,x))/x
    val,err=quad(integrand,0,np.inf,epsabs=2e-11,epsrel=2e-11,limit=250)
    return -q*q/2+val

def check():
    critical=2*(math.sqrt(2)-1)
    rng=np.random.default_rng(7748)
    for alpha in [0.12,0.4,0.8,critical,1.0,2.0,5.0,30.0]:
        for q in [0.0,.15,.72,2.5,6.3]:
            f=float(stationary(alpha,q)); g=float(published(alpha,q))
            assert abs(f-g) < 2e-14,('source identity',alpha,q,f,g)
        for q in [0.15,.72,2.5]:
            assert abs(math.log(float(stationary(alpha,q)))-logchar_levy(alpha,q))<2e-9,('Levy log CF',alpha,q)
        # The two conditional characteristic functions solve the Fourier stationarity equations.
        for q in [.2,.67,1.5]:
            p,m=map(float,conditional(alpha,q));
            pp=p*(-q-alpha*q/(alpha+q*q))
            assert abs(-q*pp-q*q*p+alpha*(m-p))<2e-13
            assert abs(-q*q*m+alpha*(p-m))<2e-13
        assert abs(float(stationary(alpha,0))-1)<1e-12
        # Jump Lévy intensity equals exactly alpha in the admissible regime.
        if alpha >= critical-1e-12:
            val,_=quad(lambda x:2*driving_density(alpha,x),0,np.inf)
            assert abs(val-alpha)<1e-8,(alpha,val)
            for x in np.geomspace(1e-8,40,100):
                assert driving_density(alpha,x)>=-1e-13
        else:
            assert driving_density(alpha,0.0)<0
            assert driving_density(alpha,20.0/math.sqrt(alpha))>0
        # The Bernoulli-Laplace factor is a Poisson law with rate log 2.
        cp_rate,_=quad(lambda x:2*(math.exp(-math.sqrt(alpha)*x)-math.exp(-math.sqrt(2*alpha)*x))/x if x>0 else 2*(math.sqrt(2)-1)*math.sqrt(alpha),0,np.inf)
        assert abs(cp_rate-math.log(2))<2e-10
    # Exact even cumulants from the Levy representation match the source moments.
    for alpha in np.exp(rng.uniform(-2,3,50)):
        variance=1+2*((1+alpha/2)/alpha-1/(2*alpha))
        fourth_cumulant=12*((1+alpha/2)/alpha**2-1/(4*alpha**2))
        assert math.isclose(variance,2+1/alpha,rel_tol=1e-13)
        assert math.isclose(fourth_cumulant,6/alpha+9/alpha**2,rel_tol=1e-13)
        fourth_moment=fourth_cumulant+3*variance**2
        assert math.isclose(fourth_moment,6*(2+3/alpha+2/alpha**2),rel_tol=1e-13)
    # Every stationary marginal can be sampled from Gaussian plus gamma variance mixture.
    # Trapped: shape alpha/2, untrapped: shape alpha/2+1, each with probability 1/2.
    alpha=1.7
    n=140_000
    labels=rng.integers(0,2,n)
    var=rng.gamma(alpha/2+labels,2/alpha,size=n)
    x=rng.normal(0,1,n)+np.sqrt(var)*rng.normal(0,1,n)
    for q in [0.2,0.6,1.1]:
        diff=abs(np.mean(np.cos(q*x))-float(stationary(alpha,q)))
        assert diff<0.012,(q,diff)
    print('PASS: conditional Fourier equations, source identity, Levy-Khintchine integrals,')
    print('positive/negative background jump boundary, exact compound-Poisson rate,')
    print('Lévy intensity, moment formulas, and independent mixture sampling.')
    print('alpha_critical=',format(critical,'.15f'))

if __name__=='__main__':
    check()
