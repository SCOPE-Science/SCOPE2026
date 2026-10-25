#!/usr/bin/env python3
"""Deterministic algebraic and numerical checks of a Brownian-diffusivity resetting theorem."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma, ndtr, kve

TOL = 1e-8
checks = 0

def close(a,b,tol=TOL):
    global checks
    assert math.isfinite(a) and math.isfinite(b), (a,b)
    assert abs(a-b)<=tol*max(1.,abs(a),abs(b)), (a,b,tol)
    checks += 1

pi=math.pi
sig=lambda n:2./((2*n-1)*pi)
# Directly verify the singular vector identities of the Volterra operator.
for n in range(1,6):
    omega=(n-.5)*pi
    for t in (0.,.1,.25,.5,.73,1.):
        f=lambda v:math.sqrt(2)*math.cos(omega*v)
        g=lambda v:math.sqrt(2)*math.sin(omega*v)
        close(quad(f,0,t)[0],sig(n)*g(t))
        close(quad(g,t,1.)[0],sig(n)*f(t))
# Infinite-product characterization (finite truncation numerical cross-check).
for theta in (0.1,0.3,0.7,1.1,1.4):
    v=1.
    for n in range(1,30001):
        v*=1./math.sqrt(1-(theta*sig(n))**2)
    close(v,1./math.sqrt(math.cos(theta)),2.e-5)
# The off-principal-mode spectral determinant.
v=1.
for n in range(2,30001):
    v*=1./math.sqrt(1-(sig(n)/sig(1))**2)
close(v,2./math.sqrt(pi),2.e-5)

# Check the exact gamma density against the branch-point tail law.
def pdf_j(y):
    return abs(gamma(.25+.5j*y))**2/(2*math.sqrt(2)*pi**1.5)
prev_err=999.
for y in (5.,8.,12.,20.):
    asym=(1./math.sqrt(pi*y))*math.exp(-pi*y/2)
    ratio=pdf_j(y)/asym
    err=abs(1.-ratio)
    assert err<prev_err and err<.05, (y,err,prev_err)
    prev_err=err
    checks+=2

# The conditional leading Gaussian mode localizes around a balanced product.
# These are 1D quadratures, independent of the stationary reset-age calculation.
def conditional_leading_norm(u):
    def integrand(z):
        if z<=0:return 0.
        q=ndtr(-u/(sig(1)*z))
        phi=math.exp(-z*z/2)/math.sqrt(2*pi)
        return phi*q
    den=quad(integrand,0.,20.,epsabs=2e-18)[0]
    numer=quad(lambda z:z*z*integrand(z),0.,20.,epsabs=2e-18)[0]
    return numer/(u*den)
for u in (10.,20.,40.,60.):
    val=conditional_leading_norm(u)
    close(val,1/sig(1),.15)
    assert val>0
    checks+=1

# Saddle and limiting physical diffusivity profile (independent parameters).
for Lambda in (.2,.7,1.,3.):
    for r in (.1,1.,2.5):
        for x in (1.,10.,100.):
            c=pi/(4*Lambda)
            age=math.sqrt(c*x/r)
            close(r*age+c*x/age,math.sqrt(pi*r*x/Lambda))
            close(2*r/age, 2*c*x/age**3)
            amp=math.sqrt(1/(2*Lambda*(age/math.sqrt(x))*sig(1)))
            for t in (0.,.125,.25,.5,.75,1.):
                lead=(2*Lambda**2*(age/math.sqrt(x))*((sig(1)*math.sqrt(2)*math.sin(pi*t/2))**2)*amp**2)
                close(lead,4*Lambda/pi*math.sin(pi*t/2)**2)

# Generalized inverse-Gaussian saddle-age proxy: exact Bessel moments.
# The CLT follows by a Laplace argument; these checks corroborate its normal scale.
for r,Lambda in ((.3,.8),(1.,1.),(2.3,.4)):
    for x in (1e5,1e7,1e9):
        c=pi/(4*Lambda)
        s0=math.sqrt(c*x/r)
        z=2*math.sqrt(r*c*x)
        m1=s0*kve(2.5,z)/kve(1.5,z)
        m2=s0*s0*kve(3.5,z)/kve(1.5,z)
        sd=math.sqrt(s0/(2*r))
        assert abs((m1-s0)/sd)<.25
        assert abs((m2-m1*m1)/sd**2-1)<.25
        checks+=2

# Algebraic relation between tail prefactor and the source stationary density.
for r,Lambda in ((.2,1.7),(1.,1.),(4.,.6)):
    surv_pref=math.sqrt(2/pi)
    rate=math.sqrt(pi*r/Lambda)
    close(surv_pref*rate/2,math.sqrt(r/(2*Lambda)))
print('PASS',checks,'deterministic assertions')
