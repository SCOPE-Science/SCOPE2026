#!/usr/bin/env python3
"""Reproducibility checks for the two-level Wigner annulus theorem.
Uses NumPy and SciPy for independent numerical quadrature, not for proof.
"""
import math
import cmath
import random
from scipy.integrate import quad

PI = math.pi

def h0(y):
    return 2**0.25 * math.exp(-PI*y*y)

def h1(y):
    return (2*math.sqrt(PI)*y)*h0(y)

def numerical_wigner(x, xi, a, b):
    def integrand(y):
        f1 = a*h0(x+y/2) + b*h1(x+y/2)
        f2 = a*h0(x-y/2) + b*h1(x-y/2)
        return f1*f2.conjugate()*cmath.exp(-2j*PI*xi*y)
    return complex(quad(lambda y: integrand(y).real, -10, 10, epsabs=5e-11)[0],
                   quad(lambda y: integrand(y).imag, -10, 10, epsabs=5e-11)[0])

def closed_wigner(x,xi,a,b):
    t=4*PI*(x*x+xi*xi)
    z= x+1j*xi
    return 2*math.exp(-t/2)*(abs(a)**2 + abs(b)**2*(t-1) + 4*math.sqrt(PI)*(a*b.conjugate()*z).real)

def uv(s,t):
    u=lambda r: r*math.exp(-r)
    v=lambda r: r*(2-r)*math.exp(-r)
    return u(s)-u(t), v(s)-v(t)

def formula(s,t,b):
    u,v=uv(s,t)
    return math.exp(-s)-math.exp(-t) + 4*u*b - (2*u+v)*b*b

def exact_optimizer(s,t):
    u,v=uv(s,t)
    if u<=0: return 0.0
    if v<=0: return 1.0
    return 2*u/(2*u+v)

def independent_polar(s,t,b,phase):
    a=math.sqrt(1-b)
    c=math.sqrt(b)*cmath.exp(1j*phase)
    def integrand(radius):
        def aint(theta):
            x=radius*math.cos(theta)
            y=radius*math.sin(theta)
            return closed_wigner(x,y,a,c)**2
        return radius*quad(aint,0,2*PI,epsabs=2e-10)[0]
    return quad(integrand, math.sqrt(s/(4*PI)), math.sqrt(t/(4*PI)),epsabs=2e-10)[0]

def main():
    rng=random.Random(52817)
    n=0
    # Direct Fourier integral from definition vs explicit cross-Wigner expression.
    for k in range(36):
        x=rng.uniform(-0.68,0.68)
        xi=rng.uniform(-0.63,0.63)
        b=rng.uniform(0,1)
        phase=rng.uniform(-PI,PI)
        a=math.sqrt(1-b)
        c=math.sqrt(b)*cmath.exp(1j*phase)
        got=numerical_wigner(x,xi,a,c)
        expected=closed_wigner(x,xi,a,c)
        assert abs(got-expected)<5e-9,(x,xi,got,expected)
        n+=1
    print('direct_wigner_integrals:',n)
    n=0
    # Independently integrate over the physical annulus (no radial moment identity).
    for k in range(24):
        s=rng.uniform(0.02,5.0)
        t=s+rng.uniform(0.02,5.0)
        b=rng.uniform(0,1)
        phase=rng.uniform(-PI,PI)
        got=independent_polar(s,t,b,phase)
        expected=formula(s,t,b)
        assert abs(got-expected)<1e-9,(s,t,b,got,expected)
        n+=1
    print('independent_annular_integrals:',n)
    n=0
    for k in range(400):
        s=rng.uniform(0.002,10.0)
        t=s+rng.uniform(0.002,9.0)
        b=exact_optimizer(s,t)
        val=formula(s,t,b)
        for z in (0,1,rng.random(),rng.random(),rng.random()):
            assert val>=formula(s,t,z)-1e-12,(s,t,b,z,val,formula(s,t,z))
        n+=1
    print('global_optimizer_checks:',n)
    # Explicit coherent advantage at a nondegenerate annulus.
    s,t=1.,3.
    b=exact_optimizer(s,t)
    assert 0 < b < 1
    assert formula(s,t,b) > max(formula(s,t,0.), formula(s,t,1.)) + 0.01
    u,v=uv(s,t)
    gain=min(4*u*u,v*v)/(2*u+v)
    assert abs(gain-(formula(s,t,b)-max(formula(s,t,0),formula(s,t,1))))<1e-12
    print('coherent_example: s=1, t=3, b=%.15f, gain=%.15f'%(b,gain))
    # Pointwise thin-annulus limiting populations, including both exact thresholds.
    def thin_limit(tau):
        if tau<=1: return 0.
        if tau>=2+math.sqrt(2): return 1.
        return 2*(tau-1)/(-tau*tau+6*tau-4)
    n=0
    for tau in (0.2,0.9,1.,1.2,1.75,2.5,3.,2+math.sqrt(2),3.8,7.):
        for eps in (1e-3,1e-4):
            got=exact_optimizer(tau,tau+eps)
            assert abs(got-thin_limit(tau)) < 0.01,(tau,eps,got,thin_limit(tau))
            n+=1
    print('thin_shell_limits:',n)
    print('ALL CHECKS PASS')
if __name__=='__main__':
    main()
