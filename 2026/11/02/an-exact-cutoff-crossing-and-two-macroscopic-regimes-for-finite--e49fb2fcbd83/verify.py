#!/usr/bin/env python3
"""Finite exact consistency checks for the cutoff Charlier Jacobi theorem.

Run: python3 verify.py
Uses only the Python standard library. Numerical checks are supplementary
and are not a proof of the asymptotic statements.
"""
from fractions import Fraction
from math import factorial, sqrt, exp, pi, lgamma, log

checks = 0

def assertion(statement):
    global checks
    assert statement
    checks += 1

def d_at_one(n, t):
    x, y = Fraction(1), t - 1
    if n == 0:
        return x
    for j in range(2,n+1):
        x,y=y,(j-2+t)*y-t*(j-1)*x
    return y

def trace_formula(n,t):
    return Fraction(factorial(n),1)*sum(
        (t**k/Fraction(factorial(k)*(n-k),1) for k in range(n)),Fraction(0)
    )/t**n

def trace_frobenius(n,t):
    return sum((Fraction(factorial(j), factorial(i))*t**(-j+i-1)
                for j in range(n) for i in range(j+1)),Fraction(0))

def chirality_eigenvector(n):
    # Unsquared normalization: w_j=(-1)^j*t^(j/2)/sqrt(j!)*(1-j/t).
    t = float(n)
    v=[(-1)**j*t**(j/2)/sqrt(factorial(j))*(1-j/t) for j in range(n)]
    residual=[]
    for j in range(n):
        lhs=(j+t-1)*v[j]
        if j>0:lhs+=sqrt(t*j)*v[j-1]
        if j+1<n:lhs+=sqrt(t*(j+1))*v[j+1]
        residual.append(lhs)
    return max(abs(z) for z in residual)/max(abs(z) for z in v)

def poisson_factor(n,rho):
    t=rho*n
    # E[N/(N-K) 1_(K<N)], use stable log-Poisson summation.
    a=[]
    for k in range(n):
        x=-t+k*log(t)-lgamma(k+1)
        a.append(x+log(n/(n-k)))
    h=max(a)
    return exp(h)*sum(exp(z-h) for z in a)

for n in range(1,21):
    for t in (Fraction(1,7),Fraction(2,5),Fraction(1),Fraction(7,2),Fraction(9)):
        assertion(d_at_one(n,t)==t**(n-1)*(t-n))
        assertion(trace_formula(n,t)==trace_frobenius(n,t))
for n in range(1,61):
    # n>1 may involve huge cancellation, so prefer below 45.
    if n<=30:assertion(chirality_eigenvector(n)<3e-10)
for rho in (0.2,0.4,0.65,0.85):
    ratios=[]
    for n in (100,250,500,800):
        f=poisson_factor(n,rho)
        expected=1/(1-rho)
        assertion(f>0)
        ratios.append(abs(f/expected-1))
    assertion(ratios[3]<ratios[0])
print(f'PASS {checks} checks: exact determinant, reciprocal trace, critical eigenvector and Poisson prefactor')
