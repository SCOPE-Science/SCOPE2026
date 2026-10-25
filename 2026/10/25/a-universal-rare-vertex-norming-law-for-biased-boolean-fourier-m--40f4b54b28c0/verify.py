#!/usr/bin/env python3
"""Exact finite tests for biased-product Fourier-multiplier endpoint norms.
Mathematical proofs are in RESULT.md; these tests are not substitutes for them.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, sqrt, pi, e
from random import Random

RNG = Random(20261023)
P_CHOICES = [F(1,5), F(1,4), F(1,3), F(2,5), F(1,2), F(3,5), F(2,3), F(3,4), F(4,5)]

def kernel(x, y, p, lambdas):
    n = len(p)
    return sum((lam * __import__('functools').reduce(
        lambda acc,i: acc * (x[i]-p[i])*(y[i]-p[i]) / (p[i]*(1-p[i])),
        (i for i in range(n) if mask & (1<<i)), F(1)))
        for mask,lam in enumerate(lambdas))

def row_mass(x, p, lambdas):
    n = len(p)
    return sum((abs(kernel(x, y,p,lambdas)) *
                 __import__('functools').reduce(lambda a,i:a*(p[i] if y[i] else 1-p[i]),range(n),F(1))
                for y in product((0,1), repeat=n)),F(0))

def rare_row_via_product(p,lambdas):
    return row_mass(tuple(int(v<=F(1,2)) for v in p),p,lambdas)

def degree2_closed(n, alpha):
    rho=(1-alpha)/alpha
    out=F(0)
    for j in range(n+1):
        prob=F(comb(n,j))*alpha**j*(1-alpha)**(n-j)
        s=F(j)/alpha-n
        q=j*rho**2+(n-j)
        out+=prob*abs(1+s+(s*s-q)/2)
    return out

check_cases=0
max_checks=0
for n in range(1,6):
    points=list(product((0,1),repeat=n))
    for rep in range(12):
        p=tuple(RNG.choice(P_CHOICES) for _ in range(n))
        lambdas=[F(RNG.randint(-5,5), RNG.choice([1,2,3,5])) for _ in range(1<<n)]
        masses=[row_mass(x,p,lambdas) for x in points]
        rare=rare_row_via_product(p,lambdas)
        assert max(masses)==rare,(n, rep, p, masses, rare)
        check_cases+=1
        max_checks+=len(points)

quadratic_cases=0
for n in range(2,15):
    for alpha in (F(1,5),F(1,4),F(1,3),F(2,5),F(1,2)):
        p=(alpha,)*n
        # Direct product-row enumeration is avoidable: compare conditional
        # expectation grouped by the exact number of rare-coordinate hits.
        # Independently reconstruct the elementary symmetric degree-two kernel.
        a=F(0)
        rho=(1-alpha)/alpha
        for j in range(n+1):
            vals=[rho]*j+[-1]*(n-j)
            kernel2=F(1)+sum(vals)+sum(vals[i]*vals[k] for i in range(n) for k in range(i+1,n))
            a+=F(comb(n,j))*alpha**j*(1-alpha)**(n-j)*abs(kernel2)
        b=degree2_closed(n,alpha)
        assert a==b,(n,alpha,a,b)
        quadratic_cases+=1

monotone_cases=0
for n in (1,2,3,4):
    for rep in range(15):
        lambdas=[F(RNG.randint(-4,4),RNG.choice([1,3,7])) for _ in range(1<<n)]
        p0=tuple(RNG.choice((F(1,10),F(1,5),F(1,3))) for _ in range(n))
        i=RNG.randrange(n)
        p1=list(p0);p1[i]=F(1,2);p1=tuple(p1)
        assert rare_row_via_product(p1,lambdas)<=rare_row_via_product(p0,lambdas)
        monotone_cases+=1

# Fixed-bias central-limit coefficient: this is a numerical diagnostic, not proof.
alpha=0.2
rho=(1-alpha)/alpha
for n in (100,1000,10000):
    # Stable recurrence for binomial masses, beginning at the mode.
    mode=int((n+1)*alpha)
    from math import lgamma,log,exp
    def mass(j):
        return exp(lgamma(n+1)-lgamma(j+1)-lgamma(n-j+1)+j*log(alpha)+(n-j)*log(1-alpha))
    terms=[]
    for j in range(n+1):
        if abs(j-n*alpha)>12*sqrt(n*alpha*(1-alpha))+10:
            continue
        s=j/alpha-n
        q=j*rho*rho+(n-j)
        terms.append(mass(j)*abs(1+s+(s*s-q)/2))
    ratio=sum(terms)/n
    if n==10000:
        assert abs(ratio/rho-sqrt(2/(pi*e)))<0.01,(ratio,rho)
print(f'VERIFY_OK exact_real_spectra={check_cases} exact_row_checks={max_checks} '
      f'exact_quadratic={quadratic_cases} exact_bias_monotonicity={monotone_cases} '
      f'CLT_ratio_n10000={ratio/rho:.9f} target={sqrt(2/(pi*e)):.9f}')
