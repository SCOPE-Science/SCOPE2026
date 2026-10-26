#!/usr/bin/env python3
"""Numerical quadrature checks for exact finite-N mirror-threshold occupation law.
Requires Python 3, SciPy. All computations are checks, not proof of limiting assertions.
"""
import math
from scipy.integrate import quad
from scipy.special import erf, erfc, erfcinv, gammaln

def qs(y):
    u=math.sqrt(y)
    return float(erf(u)), 0.5*float(erfc(u)-erfc(3*u))

def integrate_finite(N, k=None, z_moment=0):
    # Scale a=L^2/(4D)=1. Renewal age transform: dt = dy/y^2.
    b2=float(erfcinv(1/N))**2
    upper=max(100.0, 10*b2)
    def fun(y):
        if y<1.e-12:return 0.
        S,q=qs(y)
        if k is None:
            term=S**N
        elif k==-1:
            if S<=0:return 0.
            frac=min(q/S,1.0)
            term=S**N*(-math.expm1(N*math.log1p(-frac))) if frac<1 else S**N
        else:
            if q<=0 or S-q<=0:return 0.
            logbin=gammaln(N+1)-gammaln(k+1)-gammaln(N-k+1)
            term=math.exp(logbin+k*math.log(q)+(N-k)*math.log(S-q))
        if z_moment:
            term*= (N*float(erfc(math.sqrt(y))))**z_moment
        return term/y**2
    if k is None:
        result=quad(fun,0.,upper,epsabs=2.e-12,epsrel=1.e-10,limit=300,points=[b2])[0]
        result+=1/upper  # erf(sqrt(upper))^N is 1 to double precision
    else:
        result=quad(fun,0.,upper,epsabs=2.e-12,epsrel=1.e-10,limit=300,points=[b2])[0]
    return result

def check():
    comparisons=0
    for N in [1000,10000,100000,1000000,100000000]:
        b2=float(erfcinv(1/N))**2
        denominator=integrate_finite(N)
        assert 0.90<denominator*b2<1.05,(N,'denominator',denominator*b2)
        comparisons+=1
        rare=integrate_finite(N,-1)/denominator
        masses=[integrate_finite(N,k)/denominator for k in range(1,7)]
        # Partial counts cannot exceed total rare probability.
        assert 0<sum(masses)<rare<1,(N,rare,masses)
        comparisons+=1
        # The count-resolved probabilities have logarithmic decay.
        assert abs(math.log(N)*masses[0]-1/3)<0.02,(N,masses[0]*math.log(N))
        comparisons+=1
        assert abs(math.log(N)*rare-math.log(1.5))<0.04,(N,rare*math.log(N))
        comparisons+=1
        # Compare exact conditional layer mean against Gamma(k, rate=3/2).
        for k in [1,2,3]:
            m1=integrate_finite(N,k,1)/integrate_finite(N,k)
            target=2*k/3
            # Slow logarithmic approach; only verify qualitative consistent range.
            assert abs(m1-target)<0.5,(N,k,m1,target)
            comparisons+=1
        print('N=%d, b_N²=%.7f, mu_N*b_N²=%.7f, logN P(K>=1)=%.8f, logN P(K=1)=%.8f' %
              (N,b2,denominator*b2,rare*math.log(N),masses[0]*math.log(N)))
    print('PASS: %d quadrature comparisons; limiting statements proved separately.'%comparisons)

if __name__=='__main__':check()
