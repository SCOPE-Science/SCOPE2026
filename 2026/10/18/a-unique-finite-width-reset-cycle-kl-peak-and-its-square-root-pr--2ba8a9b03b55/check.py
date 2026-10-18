"""Independent numerical consistency checks for Gaussian-reset KL-cycle rate laws.

Run: python check.py
Requires NumPy and SciPy. These tests supplement the analytic arguments.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar

count=0

def verify(condition, message):
    global count
    if not condition:
        raise AssertionError(message)
    count+=1

def z(x):
    return -math.expm1(-x)

def f(x,a):
    y=z(x)
    return a*a*y*y/(2*(1+a*y))

def fp(x,a):
    y=z(x)
    return a*a*math.exp(-x)*y*(2+a*y)/(2*(1+a*y)**2)

def poisson(q,a):
    # Renormalized exponential-age expectation; independent quadrature.
    cut=min(1., max(.02,20*q/a))
    integrand=lambda y: math.exp(-y)*fp(y/q,a)
    return (quad(integrand,0,cut,epsabs=2e-10,epsrel=2e-10,limit=250)[0]
           +quad(integrand,cut,80,epsabs=2e-10,epsrel=2e-10,limit=250)[0])

def periodic(q,a):
    return q*f(1/q,a)

def root_of_rate(fun,a):
    m=minimize_scalar(lambda s:-fun(math.exp(s),a),bounds=(-9,15),method='bounded',options={'xatol':1e-10})
    verify(m.success,'optimizer unsuccessful')
    return math.exp(m.x),-m.fun

for a in [0.05,.1,.25,1.,3.,10.,100.,1000.]:
    for x in [.04,.2,.5,1.,2.,4.,10.]:
        # Derivative of the exact Gaussian Jeffreys divergence.
        h=1.e-5*min(1.,x)
        numeric=(f(x+h,a)-f(x-h,a))/(2*h)
        verify(abs(numeric-fp(x,a))<=2e-7*max(1.,fp(x,a)),f'finite derivative failed {a=} {x=}')
        ratio=1+a*z(x)
        verify(abs(f(x,a)-.5*(ratio+1/ratio-2))<=1e-10*max(1.,f(x,a)),'Gaussian KL identity')
    for q in [.15,.3,.8,1.2,2.,5.,10.,25.]:
        # Integration-by-parts route versus direct renewal integral.
        alt=q*q*quad(lambda t: math.exp(-q*t)*f(t,a),0,math.inf,epsabs=2e-11,epsrel=2e-11,limit=250)[0]
        verify(abs(alt-poisson(q,a))<=2e-8*max(1.,alt),'Poisson renewal formulas disagree')
    qp,mp=root_of_rate(poisson,a)
    qd,md=root_of_rate(periodic,a)
    verify(poisson(.5*qp,a)<mp and poisson(2*qp,a)<mp,'Poisson peak')
    verify(periodic(.5*qd,a)<md and periodic(2*qd,a)<md,'Periodic peak')
    verify(mp>0 and md>0,'positive peaks')
    print(f'a={a:g} : Poisson q*={qp:.8f}, max={mp:.8f}; periodic q*={qd:.8f}, max={md:.8f}')

for a in [1e4,1e5,1e6]:
    qp,mp=root_of_rate(poisson,a)
    qd,md=root_of_rate(periodic,a)
    verify(abs(qp/math.sqrt(a)-1)<.05,'Poisson square-root coefficient')
    verify(abs(qd/math.sqrt(a)-1/math.sqrt(2))<.02,'Periodic square-root coefficient')
    if a>=1e5:
        verify(abs((md-mp)/math.sqrt(a)-(1-1/math.sqrt(2)))<.035,'protocol gap asymptotic')
    print(f'a={a:g} : Poisson q*/sqrt(a)={qp/math.sqrt(a):.8f}; periodic q*/sqrt(a)={qd/math.sqrt(a):.8f}; gap/sqrt(a)={(md-mp)/math.sqrt(a):.8f}')
print(f'PASSED {count} consistency assertions')
