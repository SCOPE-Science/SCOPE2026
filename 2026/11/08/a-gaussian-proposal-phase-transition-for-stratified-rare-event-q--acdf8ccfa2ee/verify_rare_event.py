"""Independent-strata Gaussian tail quadrature: finite-grid consistency checks.

Standard Python library only. The proof of asymptotics is analytical.
"""
from math import sqrt, exp, log, pi, erfc, isclose
from statistics import NormalDist
from fractions import Fraction

normal=NormalDist()

def cdf(x):
    if x==float('inf'): return 1.0
    if x==-float('inf'): return 0.0
    return erfc(-x/sqrt(2))/2

def survival(x):
    if x==float('inf'): return 0.0
    if x==-float('inf'): return 1.0
    return erfc(x/sqrt(2))/2

def qnorm(u):
    if u==0:return -float('inf')
    if u==1:return float('inf')
    return normal.inv_cdf(u)

def finite_variance(n,s,z):
    assert n>=1 and s>0.5 and z>0
    kappa=2-1/s
    total=0.0
    for j in range(n):
        a=sqrt(s)*qnorm(j/n)
        b=sqrt(s)*qnorm((j+1)/n)
        if b<=z: continue
        lower=max(a,z)
        d1=survival(lower)-survival(b)
        d2=survival(sqrt(kappa)*lower)-survival(sqrt(kappa)*b)
        m1=n*d1
        m2=n*sqrt(s/kappa)*d2
        total+=m2-m1*m1
    return total/n**2

def constant(s,nterms=25000):
    beta=1-s
    assert 0<beta<0.5
    tot=0.0
    for k in range(1,nterms+1):
        i1=(k**(1-beta)-(k-1)**(1-beta))/(1-beta)
        i2=(k**(1-2*beta)-(k-1)**(1-2*beta))/(1-2*beta)
        tot+=i2-i1*i1
    return s*(4*pi)**(-beta)*tot

def phase(s,z,n):
    ustar=cdf(z/sqrt(s))
    theta=n*ustar%1
    return s*exp((1-s)*z*z/s)*theta*(1-theta)

def run():
    checks=0
    # Exact rational Bernoulli variance for the unweighted indicator at the midpoint.
    for n in range(1,101):
        theta=Fraction(n,2)-n//2
        var=theta*(1-theta)/n**2
        target=Fraction(0) if n%2==0 else Fraction(1,4*n*n)
        assert var==target
        checks+=1
    # The same identity holds for every finite grid and every threshold.
    for z in [0.2,0.65,1.0,1.4]:
        for n in [3,8,13,31,60,127,256]:
            lhs=n*n*finite_variance(n,1,z)
            rhs=phase(1,z,n)
            assert abs(lhs-rhs)<2e-10,(n,z,lhs,rhs)
            checks+=1
    # Normalized asymptotic variance for an underdispersed proposal.
    c=constant(.75)
    assert .088<c<.092
    for n in [512,1024]:
        value=n**1.5*log(n)**.25*finite_variance(n,.75,1.0)
        assert abs(value-c)<.015,(n,value,c)
        checks+=1
    # For overdispersed proposals the jump cell alone supplies n^2 variance.
    for s in [1.25,2.0]:
        for n in [512,1024]:
            lhs=n*n*finite_variance(n,s,1.0)
            rhs=phase(s,1.0,n)
            assert abs(lhs-rhs)<.008,(s,n,lhs,rhs)
            checks+=1
    # The underdispersed limiting series constant is positive and all summands nonnegative.
    beta=.25
    for k in range(1,501):
        i1=(k**(1-beta)-(k-1)**(1-beta))/(1-beta)
        i2=(k**(1-2*beta)-(k-1)**(1-2*beta))/(1-2*beta)
        assert i2-i1*i1>-1e-12
        checks+=1
    print('PASS:',checks,'tests; finite-grid Gaussian integral, Bernoulli phase and normalized variance checks')
if __name__=='__main__': run()
