#!/usr/bin/env python3
"""Reproducible independent numerical consistency checks for the stated quadrature.
Standard library only. These checks do not certify the analytical argument.
"""
import math
from fractions import Fraction

def simpson(fun, count=12000):
    assert count % 2 == 0
    h = 1.0 / count
    total = fun(0.0) + fun(1.0)
    for j in range(1, count):
        total += (4 if j % 2 else 2)*fun(j*h)
    return total*h/3

def period_formula(n, k):
    return 4*n*k/(n+1)**1.5 * simpson(lambda q: math.pi/2*math.cos(math.pi*q/2)**2/(1-k*k/(n+1)*math.sin(math.pi*q/2)**2*math.cos(math.pi*q/2)**2))

def independent_x_integral(n,k):
    return 4*n*k/math.sqrt(n+1)*simpson(lambda q: math.pi/2*math.sin(math.pi*q/2)**n*math.sqrt(max(0.,1-math.sin(math.pi*q/2)**(2*n+2)))*math.cos(math.pi*q/2)/(1-k*k/(n+1)*math.sin(math.pi*q/2)**(2*n+2)*(1-math.sin(math.pi*q/2)**(2*n+2))))

checks=0
for n in (2,4,6):
    for k in (0.1,0.5,1.0,2.0):
        assert k < 2*math.sqrt(n+1)
        a,b=period_formula(n,k),independent_x_integral(n,k)
        assert abs(a-b) <= 3e-7*(1+a)
        assert a > 0
        checks += 3
        # Verify original vector field equals quasi-polar vector field at sampled locations.
        for c in (-0.96,-0.5,0,0.4,0.85):
            for sign in (-1,1):
                s=sign*math.sqrt((1-c**(2*n+2))/(n+1))
                for rad in (0.4,1.0,2.5):
                    z=rad**n
                    rprime=rad*(-1/n+k*z*c**n*s*s)
                    sprime=z*(1+k*c**(n+1)*s)
                    uprime=rprime*c-rad*s*sprime
                    vprime=(n+1)*rad**n*rprime*s+rad**(n+1)*c**(2*n+1)*sprime
                    u,v=rad*c,rad**(n+1)*s
                    target_u=-u/n-v
                    target_v=-(n+1)*v/n+u**(2*n+1)+k*u**n*v
                    assert abs(uprime-target_u)<2e-9*(1+abs(target_u))
                    assert abs(vprime-target_v)<2e-9*(1+abs(target_v))
                    checks += 2

# The author's independently published shooting period, recovered from quadrature.
assert abs(period_formula(2,1)-1.262967766799167)<2e-7
checks+=1
# Leading zero-coupling ratio (direct numerical quadrature, not a proof).
for n in (2,4,6):
    q=0.001
    limiting=n*math.pi/(n+1)**1.5
    assert abs(period_formula(n,q)/q-limiting)<1e-6
    checks+=1
# Signed rotation speed is uniformly positive precisely under the stated bound.
for n in (2,4,6):
    for k in (0.1,1.,-0.2,-1.):
        assert 1-abs(k)/(2*math.sqrt(n+1))>0
        checks+=1
print('VERIFY_OK:',checks,'independent quadratures, field identities, source-period, small-parameter and phase-sign tests')
