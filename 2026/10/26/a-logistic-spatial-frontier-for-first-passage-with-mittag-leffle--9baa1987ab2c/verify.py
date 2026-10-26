"""Finite independent checks for a singular first-passage limit.

Run: python verify.py
Uses only the Python standard library. These checks are finite and do not
replace the analytical proof of the limiting law.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import exp, log, pi, sin, cos, isfinite
from random import Random

checks = 0


def assert_close(x, y, tol):
    global checks
    assert isfinite(x) and abs(x-y) < tol, (x, y, tol)
    checks += 1


def assert_equal(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1


def increment_law(u, v, d):
    if d == 0:
        return (1-v)/(1-u)
    return ((v-u)/(1-u)) * (1-v) * v**(d-1)


# Exact uniform-category enumeration on three nested thresholds.
# The four categories are equal quarters; thresholds are 1/4, 1/2, 3/4.
u1, u2, u3 = Q(1,4), Q(1,2), Q(3,4)
for n in (5, 7):
    counts = Counter()
    for cats in product(range(4), repeat=n):
        indices = tuple(next((i for i, c in enumerate(cats) if c>=threshold), n)
                        for threshold in (1,2,3))
        if indices[2] < n:
            counts[indices] += 1
    for (k,l,m), observed in counts.items():
        exact = (1-u1)*u1**k*increment_law(u1,u2,l-k)*increment_law(u2,u3,m-l)
        assert_equal(Q(observed,4**n),exact)


# Independent Poisson jump decomposition: finite exponent sums converge
# to the exact geometric probability-generating function.
for u in (0.1,0.25,0.5,0.75):
    for z in (0.0,0.2,0.5,0.9,1.0):
        exponent=sum((z**j-1.0)*(u**j)/j for j in range(1,200))
        assert_close(exp(exponent),(1-u)/(1-u*z),2e-14)


# Published Mittag-Leffler rate survival integral at x=exp(y/alpha).
# Composite Simpson quadrature on [0,2]; at the tested alpha's the omitted
# tail is far smaller than the stated tolerances.
def rate_survival(alpha,y,steps=8000):
    assert steps%2 == 0
    h=2.0/steps
    z=exp(y)
    def integrand(r):
        return exp(-r**(1.0/alpha))/(r*r+2.0*r*z*cos(pi*alpha)+z*z)
    acc=integrand(0.0)+integrand(2.0)
    for j in range(1,steps):
        acc+=(4 if j%2 else 2)*integrand(j*h)
    return sin(pi*alpha)/(pi*alpha)*z*acc*h/3.0

for y in (-1.0,0.0,1.0):
    exact=1/(1+exp(y))
    a02=rate_survival(0.2,y)
    a01=rate_survival(0.1,y)
    a005=rate_survival(0.05,y)
    a002=rate_survival(0.02,y)
    assert abs(a002-exact)<abs(a005-exact)<abs(a01-exact)<abs(a02-exact)
    checks+=1
    assert_close(a002,exact,0.0035)


# Brownian first-hit within half a refresh period: exact one-block event
# H_x <= lambda, with H_x = x^2/Z^2 and unit-variance normal Z.
# Kanter's stable-sampling identity gives alpha*log(lambda) without overflow.
rng=Random(74018)
alpha=0.03
simulations=36000
betas=(-0.5,0.0,0.5)
counts={b:0 for b in betas}
for i in range(simulations):
    G=rng.expovariate(1.0)
    E=rng.expovariate(1.0)
    U=pi*rng.random()
    Z=rng.gauss(0.0,1.0)
    yalpha=log(G)+alpha*log(sin(alpha*U))-log(sin(U)) \
          +(1-alpha)*(log(sin((1-alpha)*U))-log(E))
    val=yalpha+2*alpha*log(abs(Z))
    for b in betas:
        counts[b]+=(val>=2*b)
for b in betas:
    rate=counts[b]/simulations
    target=1/(1+exp(2*b))
    assert_close(rate,target,0.025)


# The two-target limit covariance follows from independent increments.
for (b1,b2) in ((-1.,0.),(-0.5,0.5),(0.,1.)):
    u=exp(2*b1)/(1+exp(2*b1))
    mean=u/(1-u)
    variance=u/(1-u)**2
    assert_close(mean,exp(2*b1),2e-14)
    assert_close(variance,exp(2*b1)*(1+exp(2*b1)),2e-14)

print('PASS: %d finite exact and numerical assertions' % checks)
print('Exact nested-threshold enumeration and Poisson PGFs: pass')
print('Mittag-Leffler logarithmic-rate convergence checks: pass')
print('Brownian one-block first-passage simulation: pass')
print('These finite checks do not certify infinite-parameter convergence.')
