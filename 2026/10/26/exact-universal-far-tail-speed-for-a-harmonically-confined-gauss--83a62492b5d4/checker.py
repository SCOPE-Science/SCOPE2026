#!/usr/bin/env python3
"""Exact finite coefficient checks and scale diagnostics for the Gaussian-shot tail theorem.

This script is not a proof of the infinite-tail asymptotic; see RESULT.md for the
Chernoff and many-recent-jumps arguments.
"""
from fractions import Fraction
from math import factorial, log, sqrt, exp

checks=0
for k,r,D,variance in [(1,1,0,1),(2,3,1,4),(3,7,5,2),(5,2,0,9)]:
    k,r,D,v = map(Fraction,(k,r,D,variance))
    maxm=28
    a=[Fraction(0)]*(maxm+1)
    K=[Fraction(0)]*(maxm+1)
    for m in range(1, maxm//2+1):
        # Gaussian mark moment generating coefficient, E(e^{tY})
        a[2*m]=(v/2)**m/factorial(m)
        # Compound-Poisson Ornstein-Uhlenbeck log-mgf coefficient
        K[2*m]=r*a[2*m]/(2*k*m)
    K[2]+=D/(2*k)
    M=[Fraction(0)]*(maxm+1)
    M[0]=Fraction(1)
    for m in range(1,maxm+1):
        M[m]=sum(j*K[j]*M[m-j] for j in range(1,m+1))/m
        checks+=1
        assert k*m*M[m] == (D*M[m-2] if m>=2 else 0)+r*sum(a[j]*M[m-j] for j in range(2,m+1))
        checks+=1
        if m%2:
            assert M[m]==0
            checks+=1
    # Check stationary second and fourth cumulants directly.
    assert M[2]*2 == D/k + r*v/(2*k)
    assert M[4]*24-3*(M[2]*2)**2 == 3*r*v*v/(4*k)
    checks+=2

# Leading event probability cost: log(n/(r delta)) - log p_x = 2 log(x) + o(log x).
# Compare normalized upper-bound exponent (Chernoff) and normalized event cost.
for eps in (0.1,0.2,0.4):
    assert 0 < (1-eps)**2 < 1
    for L in (100.,200.,500.):
        # x=e^L; n ~ (1+eps)e^L/(sigma sqrt(2L)); delta=1/L.
        # Scale these logs without creating e^L or computing huge factorials.
        sigma,r,k=2.0,3.0,5.0
        log_n=L+log(1+eps)-log(sigma)-0.5*log(2*L)
        log_rdelta=log(r)-log(L)
        # Gaussian band [a,a+1]; rough lower bound p >= density(a+1) * exp(-a/sigma²) style:
        # using monotone normal density on [a,a+1], p >= normal_density(a+1).
        a=sigma*sqrt(2*L)
        log_p_lower=-(a+1)**2/(2*sigma*sigma)-log(sigma*sqrt(2*3.141592653589793))
        n_coefficient=(1+eps)/(sigma*sqrt(2*L))
        # exact upper bound cost from Stirling inequality log(n!) <= n log n.
        normalized_rare_cost=n_coefficient*(log_n-log_rdelta-log_p_lower)/sqrt(L)
        assert normalized_rare_cost > 0
        # asymptotically tends to (sqrt2/sigma)*(1+eps)
        assert abs(normalized_rare_cost-(sqrt(2)/sigma)*(1+eps))<0.36
        # Chernoff shot cumulant upper envelope divided by x sqrt(log x)
        normalized_log_mgf_upper=(r/(2*k))*L*exp(-L*(1-(1-eps)**2))/sqrt(L)
        assert normalized_log_mgf_upper<0.001
        checks+=3
print(f'{checks} deterministic exact-coefficient and asymptotic-scale checks passed')
