#!/usr/bin/env python3
"""Numerical cross-checks for noisy depth-one scalar Anderson acceleration.

Requires numpy>=1.24 and scipy>=1.10. Run: python verify.py
The moment-existence and asymptotic statements require the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_hermitenorm, ndtr


def parameters(a, x, sigma):
    h = (a - 2.0)**2 + 1.0
    mean_d = (a - 1.0)**2 * x
    p0 = math.exp(-mean_d**2 / (2.0 * sigma**2 * h)) / (sigma * math.sqrt(2.0 * math.pi * h))
    mean0 = (a - 1.0) * (3.0 - a) * x / h
    var0 = sigma**2 / h
    c = 2.0 * p0 * (mean0**2 + var0)
    k = (math.pi / 2.0) * p0 * (mean0**4 + 6.0 * mean0**2 * var0 + 3.0 * var0**2)
    return h, mean_d, p0, mean0, var0, c, k


def aa_outputs(a, x, sigma, z0, z1, lam):
    y0 = a*x + sigma*z0
    y1 = a*y0 + sigma*z1
    f0 = y0-x
    f1 = y1-y0
    d = f1-f0
    raw = y1 - (f1/d)*(y1-y0)
    regularized = y1 - (f1*d/(d*d+lam))*(y1-y0)
    identity = x-f0*f0/d
    reg_identity = x+(lam*(2.0*f0+d)-f0*f0*d)/(d*d+lam)
    return raw, regularized, identity, reg_identity, f0, d


def exact_tail_probability(a, x, sigma, t, nodes=160):
    # Integrate over the first Gaussian oracle error using Gauss-Hermite nodes.
    z, w = roots_hermitenorm(nodes)
    f0 = (a-1.0)*x + sigma*z
    mean_d_given_f0 = (a-1.0)*x+(a-2.0)*f0
    lo = -f0*f0/(t-x)
    hi = f0*f0/(t+x)
    prob = ndtr((hi-mean_d_given_f0)/sigma) - ndtr((lo-mean_d_given_f0)/sigma)
    return float(np.dot(w,prob)/math.sqrt(2.0*math.pi))


def regularized_second_moment(a, x, sigma, lam):
    h, md, p0, m0, v, _, _ = parameters(a,x,sigma)
    sd = sigma*math.sqrt(h)
    def integrand(u):
        d = math.sqrt(lam)*u
        mean_f = (a-1.0)*x+(a-2.0)*(d-md)/h
        denom = d*d+lam
        A = x + lam*d/denom
        B = 2.0*lam/denom
        C = -d/denom
        m2=mean_f**2+v
        m3=mean_f**3+3.0*mean_f*v
        m4=mean_f**4+6.0*mean_f**2*v+3.0*v*v
        val = A*A+2*A*B*mean_f+(B*B+2*A*C)*m2+2*B*C*m3+C*C*m4
        density = math.exp(-0.5*((d-md)/sd)**2)/(sd*math.sqrt(2*math.pi))
        return val*density*math.sqrt(lam)
    result,_=quad(integrand,-np.inf,np.inf,limit=400,epsabs=1e-9,epsrel=1e-8)
    return result


def main():
    rng=np.random.default_rng(20261012)
    count=0
    for a,x,sigma in [(0.0,0.0,1.0),(0.6,2.0,1.0),(-0.3,-1.1,0.35),(0.95,0.4,1.7)]:
        h,md,p0,m,v,c,k=parameters(a,x,sigma)
        assert c>0 and k>0 and v>0
        count+=3
        for _ in range(300):
            z0,z1=rng.normal(size=2)
            raw,reg,identity,reg_identity,f0,d=aa_outputs(a,x,sigma,z0,z1,0.01)
            assert math.isclose(raw, identity,rel_tol=1e-9,abs_tol=1e-9)
            assert math.isclose(reg,reg_identity,rel_tol=1e-9,abs_tol=1e-9)
            assert math.isclose(d,(a-1)**2*x+sigma*((a-2)*z0+z1),rel_tol=1e-9,abs_tol=1e-9)
            count+=3
        for t in (1000.0,10000.0):
            pr=exact_tail_probability(a,x,sigma,t)
            assert abs(t*pr/c-1.0)<0.003,(a,x,sigma,t,t*pr,c)
            count+=1
        for lam in (1e-4,1e-5):
            risk=regularized_second_moment(a,x,sigma,lam)
            assert math.isfinite(risk) and risk>0
            ratio=math.sqrt(lam)*risk/k
            assert abs(ratio-1.0)<0.12,(a,x,sigma,lam,ratio)
            count+=2
        print(f'a={a}, x0={x}, sigma={sigma}, tail_coefficient={c:.12g}, risk_coefficient={k:.12g}')
    print(f'PASS: {count} finite numerical/algebraic checks; infinite moment and limits require the proof.')

if __name__=='__main__': main()
