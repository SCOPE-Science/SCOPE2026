#!/usr/bin/env python3
"""Numerical cross-checks of analytic moment and scaling identities.
Not a proof of the stable-limit theorem. Requires scipy.
"""
import math
from scipy.integrate import quad

checks=0

def ok(test, label):
    global checks
    if not test:
        raise AssertionError(label)
    checks+=1

for beta,alpha,scale,K in [(1.,2.5,1.,1.),(.5,1.8,2.,3.),(1.5,3.,.7,2.)]:
    p=1+beta/2
    q=alpha/p
    ok(1<q<2,'stable exponent')
    ok(alpha>p and alpha<2*p,'range')
    m=scale/(alpha-1)
    ES_p=scale**p*math.gamma(p+1)*math.gamma(alpha-p)/math.gamma(alpha)
    integrand=lambda s: s**p*(alpha/scale)*(1+s/scale)**(-alpha-1)
    numer=quad(integrand,0,math.inf,epsabs=1e-8)[0]
    ok(abs(numer/ES_p-1)<2e-7,'Pareto power moment')
    EZ=2*math.sqrt(K/math.pi)/p
    EZ_num=quad(lambda u: 2*math.sqrt(K/math.pi)*u**(beta/2),0,1)[0]
    ok(abs(EZ/EZ_num-1)<1e-12,'Brownian area mean')
    mu=EZ*ES_p/m
    mu_simple=2*math.sqrt(K/math.pi)*(alpha-1)*scale**(p-1)*math.gamma(p)*math.gamma(alpha-p)/math.gamma(alpha)
    ok(abs(mu/mu_simple-1)<1e-12,'renewal reward speed')
    for x in (1e10,1e14):
        tail=(1+x**(1/p)/scale)**(-alpha)
        limit=scale**alpha*x**(-q)
        ok(abs(tail/limit-1)<.005,'Breiman Pareto factor')
    ok(alpha>q,'time-clock fluctuations subordinate')

p=1.5;alpha=2.5
mu=2/math.sqrt(math.pi)*(alpha-1)*math.gamma(p)*math.gamma(alpha-p)/math.gamma(alpha)
ok(abs(mu-2/math.sqrt(math.pi))<1e-12,'simple Brownian example')
print('PASS',checks,'deterministic independent numerical identities; stable convergence is analytic')
