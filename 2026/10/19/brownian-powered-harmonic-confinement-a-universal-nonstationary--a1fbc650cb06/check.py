#!/usr/bin/env python3
"""Deterministic numerical checks for the stochastic-power trap asymptotic law.

The infinite-time theorem is proved analytically in RESULT.md. This program
checks scaling constants, a pathwise Laplace integral, and limiting mixture tails.
Requires numpy and scipy. Run: python check.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import erf, gamma

checks = 0

def close(a, b, rtol=1e-7, atol=1e-12):
    global checks
    if not math.isclose(a, b, rel_tol=rtol, abs_tol=atol):
        raise AssertionError((a,b,rtol))
    checks += 1

# For a constant positive rescaled stiffness path b(u)=h, this is the
# exact finite-t variance and is independent of any numerical quadrature.
for p in (0.5,1.0,2.0,3.0):
    for h in (0.7,1.0,1.4):
        for k0 in (0.0,0.3):
            for t in (20.0,100.0):
                kappa,sigma,D=1.3,0.9,0.7
                H=t**(1.0+p/2)
                A=kappa*sigma**p*h**p*H+k0*t
                q=D*H*(-math.expm1(-2*A))/A
                target=D/(kappa*sigma**p*h**p)
                # Static stiffness contributes only a relative O(t^{-p/2}).
                close(q/target,1.0,rtol=0.35 if p==0.5 else 0.16)

# Smooth, nonconstant prescribed Brownian-scale path b(u)=1+a(1-u).
# The inner time integral has a separate closed form; outer integral numerical.
for p in (0.8,1.3,2.0,3.0):
    for aa in (0.1,0.35):
        for t in (45.0,120.0):
            kappa,sigma,D,k0=1.3,0.9,0.7,0.4
            H=t**(1+p/2)
            A=2*kappa*sigma**p*H/(aa*(p+1))
            def integrand(z):
                inner=A*math.expm1((p+1)*math.log1p(aa*z/H))
                return math.exp(-inner-2*k0*z*t/H)
            q=2*D*quad(integrand,0,min(H,70),epsabs=1e-11)[0]
            target=D/(kappa*sigma**p)
            close(q/target,1.0,rtol=0.08)

# Cauchy law for p=2: the exact Gaussian-ratio characteristic function.
from scipy.stats import cauchy
for a in (0.15,0.8,1.9):
    for yy in (0.1,0.3,1,3,10):
        # Integrate over the independent denominator |G|>0.
        integral=quad(lambda g:math.exp(-(yy**2*a*a)/(2*g*g)) *
                      math.sqrt(2/math.pi)*math.exp(-g*g/2),0,13,
                      epsabs=1e-11)[0]
        close(integral,math.exp(-a*yy),rtol=2e-9)
        tail=(2/math.pi)*math.atan(a/yy)
        close(tail,2*cauchy.sf(yy,scale=a),rtol=1e-12)

# Tail constant P(|Y|>y) ~ C_p*y^{-2/p} for arbitrary power p.
for p in (0.9,1,1.5,2,2.7,4):
    a=0.8
    cp=math.sqrt(2/math.pi)*a**(2/p)*(2**(1/p))*gamma(0.5+1/p)/math.sqrt(math.pi)
    for y in (1000.0,2000.0):
        tail=quad(lambda z: math.erf(((a*z/y)**(2/p))/math.sqrt(2))*
                  math.sqrt(2/math.pi)*math.exp(-z*z/2),0,12,
                  epsabs=1e-16)[0]
        close((y**(2/p))*tail,cp,rtol=0.025)

# Finite-time Gaussian-conditional variance under sampled unit-time Brownian
# paths, checked against its endpoint Laplace limit; the sample is fixed-seed.
rng=np.random.default_rng(463281)
N=120000
p,t=2,80.0
H=t**(1+p/2)
kappa,sigma,D,k0=1.3,0.9,0.7,0.4
errors=[]
for _ in range(96):
    increments=rng.normal(0,1/math.sqrt(N),size=N)
    b=np.concatenate(([0.],np.cumsum(increments)))
    g=b[-1]
    if abs(g)<0.8: continue  # avoid the nonuniform small-endpoint boundary
    sq=b*b
    cum=np.zeros(N+1)
    cum[:-1]=np.cumsum(((sq[:-1]+sq[1:])/(2*N))[::-1])[::-1]
    u=np.arange(N+1)/N
    vals=np.exp(-2*kappa*sigma**p*H*cum-2*k0*t*(1-u))
    got=2*D*H*np.trapezoid(vals,dx=1/N)
    want=D/(kappa*sigma**p*abs(g)**p)
    errors.append(abs(got/want-1))
if len(errors)<25 or float(np.median(errors))>=0.09 or float(np.quantile(errors,0.9))>=0.22:
    raise AssertionError((len(errors),float(np.median(errors)),float(np.quantile(errors,.9))))
checks+=3
print(f"PASS: {checks} deterministic comparisons; sampled-path median relative error {np.median(errors):.4f}, n={len(errors)}")
