#!/usr/bin/env python3
"""Reproducibility diagnostics for spherical widths of complete-bipartite zonotopes.

Runs with the Python standard library. Finite diagnostics do not replace the proof.
"""
import itertools
import math
import random

MU=2/math.sqrt(math.pi)
B=math.sqrt(2/math.pi)
V=1/3+(2*math.sqrt(3)-4)/math.pi

def eta(d):
    return math.sqrt(2)*math.exp(math.lgamma((d+1)/2)-math.lgamma(d/2))

def moments(p,q):
    d=p+q-1
    e=MU*math.sqrt(d)/eta(d)
    e2=MU**2+(2-MU**2+V*(p+q-2))/(p*q)
    return e,e2

def f(x):
    return B*math.exp(-x*x/2)+x*math.erf(x/math.sqrt(2))

def simpson(func,lo,hi,k):
    h=(hi-lo)/k
    return h/3*(func(lo)+func(hi)+4*sum(func(lo+(2*i-1)*h) for i in range(1,k//2+1))+2*sum(func(lo+2*i*h) for i in range(1,k//2)))

def phi(x):
    return math.exp(-x*x/2)/math.sqrt(2*math.pi)

# Independently integrate the conditional absolute-difference kernel.
e_mean=simpson(lambda x:f(x)*phi(x),-9,9,2400)
e_square=simpson(lambda x:f(x)**2*phi(x),-9,9,2400)
e_cov=simpson(lambda x:f(x)*(x*x-1)*phi(x),-9,9,2400)
assert abs(e_mean-MU)<2e-8
assert abs(e_square-(V+MU**2))<2e-8
assert abs(e_cov-MU/2)<2e-8

# Check support function by exhaustive independent optimization of segment signs.
checks=0
for p,q in [(1,2),(2,2),(2,3),(3,3)]:
    edges=[(i,p+j) for i in range(p) for j in range(q)]
    n=p+q
    for t in range(10):
        x=[((19*i+11*t+7*i*t)%43-21)/17 for i in range(n)]
        mean=sum(x)/n
        x=[v-mean for v in x]
        width=sum(abs(x[i]-x[j]) for i,j in edges)
        mx=max(sum(sign*(x[i]-x[j])/2 for sign,(i,j) in zip(sgn,edges))
               for sgn in itertools.product((-1,1),repeat=len(edges)))
        mn=min(sum(sign*(x[i]-x[j])/2 for sign,(i,j) in zip(sgn,edges))
               for sgn in itertools.product((-1,1),repeat=len(edges)))
        assert abs(width-(mx-mn))<1e-10
        checks+=1

rng=random.Random(20261019)
# Spherical Monte Carlo for first and second moments (moderate n, fixed seed).
for p,q in [(1,6),(2,3),(3,4)]:
    n=p+q;d=n-1
    vals=[]
    for t in range(22000):
        g=[rng.gauss(0,1) for _ in range(n)]
        gm=sum(g)/n
        r=math.sqrt(sum((v-gm)**2 for v in g))
        w=sum(abs(g[i]-g[p+j]) for i in range(p) for j in range(q))/r
        vals.append(math.sqrt(d)*w/(p*q))
    m=sum(vals)/len(vals)
    second=sum(x*x for x in vals)/len(vals)
    e,e2=moments(p,q)
    assert abs(m-e)<.025,(p,q,m,e)
    assert abs(second-e2)<.060,(p,q,second,e2)

# Finite-n moment coefficients approach the claimed CLT limits.
for alpha in [.2,.35,.5]:
    n=2400
    p=round(alpha*n);q=n-p
    e,e2=moments(p,q)
    variance=e2-e*e
    predicted=V/(alpha*(1-alpha))-2/math.pi
    assert abs(n*variance-predicted)<.004, (alpha,n*variance,predicted)

# The fixed-side lower-tail law for p=1 is checked independently by inversion.
for eps in [0.004,0.001,0.0002]:
    lo,hi=0.0,1.0
    for _ in range(70):
        mid=(lo+hi)/2
        if f(mid)-B<eps:lo=mid
        else:hi=mid
    pexact=math.erf(((lo+hi)/2)/math.sqrt(2))
    asympt=(eps/B)**.5/math.gamma(1.5)
    assert abs(pexact/asympt-1)<.015,(eps,pexact,asympt)

print('VERIFY_OK support_cases=',checks,'quadratures=3 spherical_cases=3 asymptotic_ratios=3 edge_cdf=3')
