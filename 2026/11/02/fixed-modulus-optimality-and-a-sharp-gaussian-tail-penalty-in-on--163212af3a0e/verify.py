#!/usr/bin/env python3
"""Standalone finite checks for the stated one-vector spectral-sketch formulas.

The infinite-dimensional quantifiers and asymptotics are proved in RESULT.md,
not inferred from these finite checks.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import gamma, sqrt, pi
import random

checks = 0

def check(expr, why):
    global checks
    if not expr:
        raise AssertionError(why)
    checks += 1


def exact_weight_gap(a, q, support):
    """Exact expectation, and pairwise swapped law for iid finite support."""
    d=len(a)
    b=tuple(x ** (2*q+1) for x in a)
    B=sum(b)
    C0=sum(x*y for x,y in zip(a,b))/B
    EC=F(0)
    penalty=F(0)
    alphas=[F(0) for _ in a]
    for w in product(support, repeat=d):
        prob=F(1,len(support)**d)
        S=sum(x*y for x,y in zip(b,w))
        EC += prob * sum(x*y*z for x,y,z in zip(a,b,w))/S
        for i in range(d):
            alphas[i] += prob*w[i]/S
        for i,j in combinations(range(d), 2):
            wp=list(w)
            wp[i],wp[j]=wp[j],wp[i]
            Sp=sum(x*y for x,y in zip(b,wp))
            penalty += prob * b[i]*b[j]*(a[i]-a[j])*(b[i]-b[j])*(w[i]-w[j])**2/(2*B*S*Sp)
    check(EC <= C0, ('optimality',a,q,support))
    check(C0-EC == penalty, ('penalty',a,q,support))
    check(sum(b[i]*alphas[i] for i in range(d))==1, 'normalization')
    for i,j in combinations(range(d),2):
        check((alphas[i]-alphas[j])*(b[i]-b[j]) <= 0, 'exchangeable antitonicity')
    if len(set(a))>1 and len(set(support))>1:
        check(C0>EC, 'strictness')
    else:
        check(C0==EC, 'equality case')


# Exact expectation over all random-amplitude vectors, no numerical quadrature.
for a in [(F(1),F(2),F(3)),(F(1),F(1),F(5)),(F(2),F(2),F(2)),
          (F(1),F(2),F(4),F(7)),(F(1),F(3),F(3),F(6),F(9))]:
    for q in range(4):
        for supp in [(F(1),F(1)),(F(1),F(3)),(F(1,2),F(5,2))]:
            exact_weight_gap(a,q,supp)

# The spike formula is exact at any dimension and any power index.
for d in range(3,9):
    for a1 in (F(2), F(3), F(5)):
        for q in range(4):
            beta=a1**(2*q+1)
            aa=(a1,)+(F(1),)*(d-1)
            bb=(beta,)+(F(1),)*(d-1)
            cre=sum(x*y for x,y in zip(aa,bb))/sum(bb)
            risk=sum(aa)-cre
            check(risk-(d-1)==(a1-1)*(d-1)/(beta+d-1),'spike exact sign')

# Validate Gaussian spike's beta integral against direct Gaussian sampling.
# Non-proof diagnostic: sample mean only, large enough tolerance for bounded risks.
rng=random.Random(260829)
for d,a1,q in [(3,2,0),(3,2,2),(4,3,1),(5,2,1),(7,2,0)]:
    B=a1**(2*q+1)
    n=160000
    summ=0.0
    for _ in range(n):
        W1=rng.gauss(0,1)**2
        Wtail=sum(rng.gauss(0,1)**2 for _ in range(d-1))
        summ += Wtail/(B*W1+Wtail)
    mc=summ/n
    # Direct independent beta integral by midpoint integration in u=sqrt(t).
    nu=(d-1)/2
    beta_norm=gamma(.5)*gamma(nu)/gamma(nu+.5)
    N=120000
    integral=0.0
    for k in range(N):
        u=(k+.5)/N
        integral += 2*((1-u*u)**nu)/(1+(B-1)*u*u)
    integral /= N*beta_norm
    check(abs(mc-integral)<0.009,('Gaussian spike beta integral',d,a1,q,mc,integral))

# Exact Gaussian versus sign in d=2 (a consistency check, not the novelty claim).
for a1,a2,q in [(4.0,1.0,0),(4.0,1.0,1),(9.0,1.0,2),(2.0,1.0,3)]:
    v=(a2/a1)**(q+.5)
    gauss=a2+(a1-a2)*v/(1+v)
    rad=a2+(a1-a2)*v*v/(1+v*v)
    check(rad<gauss,'aligned sign better')

print(f'PASS: {checks} exact and numerical check groups')
