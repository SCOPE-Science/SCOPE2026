#!/usr/bin/env python3
"""Numerical checks of harmonic Feynman–Kac coefficient and inner-tail integral.
No numerical integration is used as a proof of the limiting probability law.
"""
import math
from scipy.integrate import quad
from scipy.special import gamma, erfc

checks=0
for k, sgm in [(0.5,1.0),(1.0,1.0),(0.5,2.0)]:
    c=2*math.sqrt(sgm)
    C = 2/math.sqrt(c)*quad(lambda y: math.exp(-2*k*y)/math.sqrt(math.sinh(c*y)),0,20,epsabs=1e-10)[0]
    G = math.sqrt(math.pi)*gamma(k/(2*math.sqrt(sgm))+0.25)/(2*sgm**0.75*gamma(k/(2*math.sqrt(sgm))+0.75))
    assert abs(C/G-1)<1e-8
    checks+=1
    prev=0
    for t in (20,100,500):
        def integrand(s):
            z=c*s
            return 0. if z>700 else 2*math.exp(-2*k*s)/math.sqrt(math.cosh(z)+c*(t-s)*math.sinh(z))
        E=quad(integrand,0,t,epsabs=1e-9)[0]
        value=E*math.sqrt(t)
        assert prev<value<C
        prev=value
        checks+=1
for sgm in (1.0,2.0,3.0):
    er=2/math.sqrt(2*math.pi)*quad(lambda b: erfc(b*math.sqrt(sgm/2)),0,20,epsabs=1e-12)[0]
    exact=2/(math.pi*math.sqrt(sgm))
    assert abs(er/exact-1)<1e-10
    checks+=1
print(f'{checks} deterministic checks passed; these do not certify the probability-limit proof')
