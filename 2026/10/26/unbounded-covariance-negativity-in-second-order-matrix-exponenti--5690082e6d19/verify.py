#!/usr/bin/env python3
"""Finite checks accompanying the analytical METD covariance theorem.

Only Python's standard library is needed. Numerical tests are not a proof
of universal claims; the accompanying proof supplies those claims.
"""
import math
from fractions import Fraction

checks = 0

def require(ok, note):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(note)

def f(x):
    assert x > 0
    return -math.expm1(-2.0*x)/(2.0*x)

def g(x):
    assert x > 0
    if x < 0.002:
        return 0.5-x/3+x*x/8-x*x*x/30+x**4/144-x**5/840
    return (1.0-(1.0+x)*math.exp(-x))/(x*x)

def first(a,b):
    return ((f(a), f(a)), (f(b), f(b)))

def second(a,b):
    return ((f(a), f(a)+(a-b)*g(a)),
            (f(b)+(b-a)*g(b), f(b)))

def symmetric(M):
    return ((M[0][0], (M[0][1]+M[1][0])/2),
            ((M[0][1]+M[1][0])/2,M[1][1]))

def det(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def min_eig_sym(M):
    return (M[0][0]+M[1][1]-math.hypot(M[0][0]-M[1][1],2*M[0][1]))/2

def gram(a,b):
    v=(a,b)
    return tuple(tuple(-math.expm1(-(x+y))/(x+y) for y in v) for x in v)

def simpson_exp(x, n=4000):
    h=1/n
    sm=1+math.exp(-x)
    for j in range(1,n):
        sm+=(4 if j%2 else 2)*math.exp(-x*j*h)
    return sm*h/3

# Closed forms independently compared against their defining integrals.
for x in (0.05, 0.2, 1.0, 2.5, 10.0):
    require(abs(f(x)-simpson_exp(2*x))<2e-9,'phi-one integral')
    n=8000
    h=1/n
    weighted=h*(0.0+math.exp(-x))/3
    weighted+=h/3*sum((4 if j%2 else 2)*(j*h)*math.exp(-x*j*h) for j in range(1,n))
    require(abs(g(x)-weighted)<3e-9,'commutator coefficient integral')

for a,b in ((1.1,1),(2,1),(10,1),(100,1),(1,4),(3,6)):
    q=gram(a,b)
    require(q[0][0]>0 and det(q)>0,'exact positive Gram covariance')
    s1=symmetric(first(a,b))
    require(abs(det(s1)+(f(a)-f(b))**2/4)<3e-14,'METD1 determinant identity')
    require(det(s1)<0,'METD1 non-PSD')
    s2=symmetric(second(a,b))
    off=(f(a)+f(b)+(a-b)*(g(a)-g(b)))/2
    require(abs(s2[0][1]-off)<1e-13,'METD2 symmetric cross-term')
    require(abs(s2[0][0]-f(a))<1e-15,'METD2 diagonal')

require(det(symmetric(second(10,1)))<0,'explicit METD2 counterexample')
require(Fraction(7,320)-Fraction(669,800)**2<0,'exact rational certificate')
require(Fraction(8,3)<Fraction(11,4),'elementary exponential bounds')
require(det(symmetric(second(2,1)))>0,'local contrast: moderate stiffness')

b=1
limit=-g(b)/2
previous=None
for a in (10,100,1000,10000,100000):
    observed=min_eig_sym(symmetric(second(a,b)))/a
    require(observed<0,'negative stiffness-scaled eigenvalue')
    if previous is not None:
        require(abs(observed-limit)<abs(previous-limit),'asymptotic convergence')
    previous=observed
require(abs(previous-limit)<1e-5,'sharp negative-eigenvalue slope')
require(f(100000)+f(1)<0.5,'exact covariance bounded in stiff limit')

print(f'PASS: {checks} checks; limiting slope = {limit:.12f}')
