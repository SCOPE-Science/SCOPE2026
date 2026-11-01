#!/usr/bin/env python3
"""Reproducible diagnostics for the stated short-distance orthotope theorem.

Run with Python 3 standard library. Diagnostics supplement, not replace, proof.
"""
from itertools import combinations
from math import gamma, pi, prod, sqrt

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def close(x, y, tol=1e-10):
    return abs(x-y) <= tol*(1+abs(x)+abs(y))

def ball(d):
    return pi**(d/2)/gamma(1+d/2)

def b(d, k):
    return gamma(1+d/2)/(pi**(k/2)*gamma(1+(d+k)/2))

def e(xs, k):
    return sum(prod(z) for z in combinations(xs,k))

def polydat(lengths):
    d=len(lengths)
    R=(prod(lengths)/ball(d))**(1/d)
    cs=[R/x for x in lengths]
    a=[(-1)**k*b(d,k)*e(cs,k) for k in range(d+1)]
    return R,cs,a

def polynomial(rho, a):
    return rho**(len(a)-1)*sum(v*rho**k for k,v in enumerate(a))

def solve(A, rhs):
    a=[list(map(float,row))+[float(val)] for row,val in zip(A,rhs)]
    n=len(a)
    for j in range(n):
        p=max(range(j,n), key=lambda i:abs(a[i][j]))
        check(abs(a[p][j])>1e-14,'singular interpolation system')
        a[j],a[p]=a[p],a[j]
        z=a[j][j]
        for k in range(j,n+1):a[j][k]/=z
        for i in range(n):
            if i != j:
                z=a[i][j]
                for k in range(j,n+1):a[i][k]-=z*a[j][k]
    return [row[-1] for row in a]

# The exact top coefficient must not depend on box shape.
for length in ([1.,2.],[1.,1.],[1.,2.,3.],[1.,1.,3.],
               [1.,1.,1.,1.],[1.,2.,3.,5.],[2.,4.,7.,11.,13.]):
    d=len(length);R,cs,a=polydat(length)
    check(close(prod(cs),1/ball(d)), 'normalization product')
    check(close(a[-1],(-1)**d*b(d,d)/ball(d)), 'shape-invariant top coefficient')
    for rho in (0.025,0.05):
        check(0<polynomial(rho,a)<1,'CDF small-radius range')

# Exact independent planar polar integration: for r below both sides,
# integral = pi*r^2/V-4*r^3*(1/a+1/b)/(3*V)+r^4/(2*V*a*b).
for aa,bb in [(1.,1.),(1.,2.),(2.,5.),(3.,7.)]:
    R,cs,A=polydat([aa,bb]); V=aa*bb
    for r in (0.1*min(aa,bb),0.5*min(aa,bb),0.95*min(aa,bb)):
        direct=pi*r*r/V-4*r**3*(1/aa+1/bb)/(3*V)+r**4/(2*V*aa*bb)
        check(close(polynomial(r/R,A),direct), 'independent 2D polar integral')

# Distinct evaluation nodes reconstruct all nontrivial coefficients in d>=2.
for length in ([1.,2.],[1.,2.,3.],[1.,1.,2.,5.],[1.,2.,3.,5.,8.]):
    d=len(length);R,cs,a=polydat(length)
    nodes=[0.08+0.045*j for j in range(d-1)]
    check(nodes[-1]*R<min(length),'nodes remain in polynomial window')
    mat=[];rhs=[]
    for rho in nodes:
        val=polynomial(rho,a)
        val=(val/rho**d-1-a[d]*rho**d)/rho
        rhs.append(val)
        mat.append([rho**(k-1) for k in range(1,d)])
    recovered=solve(mat,rhs)
    for k in range(1,d):
        check(close(recovered[k-1],a[k],tol=2e-8),'inversion from d-1 values')

# Exact 2D first-cap excess, computed by Simpson quadrature.
# The integrand is integrated only on the newly exposed displacement caps.
def integrate(f,a,b,n=8000):
    n += n%2
    h=(b-a)/n
    s=f(a)+f(b)
    for j in range(1,n):s+=(4 if j%2 else 2)*f(a+j*h)
    return s*h/3

def first_cap_excess_2d(lengths, eps):
    lo=min(lengths); other=max(lengths); V=prod(lengths)
    return (2*sum(z==lo for z in lengths)/V)*integrate(lambda x:(x/lo-1)*(2*sqrt(max(0.,(lo+eps)**2-x*x))-((lo+eps)**2-x*x)/other),lo,lo+eps)

def first_constant_2d(lengths):
    R,cs,a=polydat(lengths)
    m=sum(x==min(lengths) for x in lengths)
    star=min(lengths)/R
    return (8*m*ball(1)*sqrt(2)/(ball(2)*3*5))*star**(-0.5)
for lengths in ([1.,2.],[1.,3.],[1.,1.]):
    R,cs,a=polydat(lengths)
    C=first_constant_2d(lengths)
    for eps in (0.02,0.01,0.005):
        excess=first_cap_excess_2d(lengths,eps)
        ratio=excess/(C*(eps/R)**2.5)
        check(abs(ratio-1)<0.06,'first transition coefficient d2')

# First-excess formula in dimension 3 simplifies to m/2 exactly.
for multiplicity in (1,2,3):
    star=1.4
    c=(8*multiplicity*ball(2)*(2**1)*star**0)/(ball(3)*4*6)
    check(close(c,multiplicity/2), 'universal cubic onset d3')

print(f'PASS: {checks} diagnostic assertions; no infinite claim inferred from sampling.')
