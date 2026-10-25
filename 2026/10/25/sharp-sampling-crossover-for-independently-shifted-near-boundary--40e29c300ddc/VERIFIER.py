#!/usr/bin/env python3
"""Reproduce numerical checks for randomly shifted Poisson-kernel trapezoidal quadrature.

Uses only the Python standard library.  Analytic proofs are in RESULT.md.
"""
from math import cos, exp, pi, log, isclose
import random

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def poisson(q, u):
    return (1-q*q)/((1-q)**2 + 2*q*(1-cos(u)))

def trapezoid(N, r, theta):
    return sum(poisson(r,theta+2*pi*j/N) for j in range(N))/N

def simpson(f, a, b, N):
    assert N%2 == 0
    h=(b-a)/N
    s=f(a)+f(b)
    for j in range(1,N):
        s += (4 if j%2 else 2)*f(a+j*h)
    return s*h/3

for N in range(1,22):
    for r in (0.13, 0.53, 0.88, 0.985):
        for offset in (0.09, 0.25, 0.56, 1.5, 2.4):
            theta=offset/N
            lhs=trapezoid(N,r,theta)
            rhs=poisson(r**N,N*theta)
            check(abs(lhs-rhs) < 2.e-10*(1+abs(rhs)),f'alias N={N},r={r},theta={theta}')

for q in (0.13,0.35,0.70,0.90,0.97):
    numer_mean=simpson(lambda u:poisson(q,u), -pi,pi,16384)/(2*pi)
    numer_second=simpson(lambda u:poisson(q,u)**2,-pi,pi,16384)/(2*pi)
    check(abs(numer_mean-1)<2e-9,'mean')
    check(abs(numer_second-(1+q*q)/(1-q*q))<2e-8,'second moment')
    for p in (0.10,0.50,0.80,0.95):
        z=poisson(q,pi*(1-p))
        c=(1+q*q-(1-q*q)/z)/(2*q)
        # The survival function at p-th quantile is 1-p.
        from math import acos
        check(abs(acos(max(-1,min(1,c)))/pi-(1-p))<2e-10,'quantile')

for q in (0.4,0.8,0.98):
    numerical_first=simpson(lambda u:poisson(q,u),-pi,pi,65536)/(2*pi)
    numerical_second=simpson(lambda u:poisson(q,u)**2,-pi,pi,65536)/(2*pi)
    for m in (1,3,12,100):
        observed=(numerical_second-numerical_first**2)/m
        predicted=2*q*q/(m*(1-q*q))
        check(abs(observed-predicted)<3e-8,'independent variance integration')

# Verify the finite critical-window Laplace integral against its Poisson-shot-noise limit.
# The limit integral is truncated to +/- 300; its omitted exponent is < 2*t/(pi*300).
for lam,t in ((0.5,0.7),(1.0,0.35),(2.0,1.1)):
    eps=0.0005
    m=round(lam/eps)
    q=1-eps
    avg=simpson(lambda u:1-exp(-t*poisson(q,u)/m),-pi,pi,131072)/(2*pi)
    finite=(1-avg)**m
    limit_exp=lam/(2*pi)*simpson(
        lambda x:1-exp(-2*t/(lam*(1+x*x))),-300,300,120000)
    limit=exp(-limit_exp)
    check(abs(finite-limit)<0.006,'Poisson critical-window Laplace check')

# For near-boundary samples: the median tends to 0, while the mean is exactly 1.
for eps in (0.02,0.01,0.005,0.001):
    q=1-eps
    med=poisson(q,pi/2)
    check(med < eps*1.02,'median collapse')
    check(abs((2*q*q/(1-q*q))*eps-1) < 0.06,'variance asymptotic')

# Deterministic seeded empirical checks of the resolved and critical regimes.
rng=random.Random(654781)
for q,m in ((0.6,60000),(0.98,60000)):
    sm=0.0
    sq=0.0
    for _ in range(m):
        y=poisson(q,2*pi*rng.random())
        sm+=y
        sq+=y*y
    err=abs(sm/m-1)
    tolerance=8*(2*q*q/(1-q*q)/m)**0.5
    check(err < tolerance,'random quadrature mean')

print(f'PASS: {checks} independently computed assertions.')
