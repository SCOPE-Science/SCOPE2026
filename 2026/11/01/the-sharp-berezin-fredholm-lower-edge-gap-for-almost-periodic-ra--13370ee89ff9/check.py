#!/usr/bin/env python3
"""Finite numerical diagnostics for the sharp radial Fock lower-edge gap.
These diagnostics do not prove asymptotic or spectral statements.
Requires numpy and scipy; run: python check.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import erf, ndtr
from scipy.stats import gamma
from numpy.polynomial.hermite import hermgauss

freqs = (1.0, math.sqrt(2.0))
weights = (1.0, 0.7)
c = 1.3

def p(x):
    return sum(w * math.cos(v * x) for v, w in zip(freqs, weights))

def filtered(x, t):
    return sum(w * math.exp(-t * v*v) * math.cos(v * x)
               for v, w in zip(freqs, weights))

def eigenvalue(n, d):
    k = n+d
    # X~Gamma(k,1), t=sqrt(X); integrate at 14 standard deviations
    a = max(0, math.sqrt(k) - 14)
    b = math.sqrt(k) + 14
    val, err = quad(lambda t: 2*t*gamma.pdf(t*t, a=k)*p(t),
                    a, b, epsabs=3e-11, limit=400)
    assert err < 1e-7, (err,k)
    return c + val

def berezin_numeric(r):
    # dimension one; |r+W| where real/imag parts of W have N(0,1/2)
    x,w=hermgauss(38)
    s=0.0
    for i, xx in enumerate(x):
        for j, yy in enumerate(x):
            s += w[i]*w[j]*p(math.hypot(r+float(xx),float(yy)))
    return c+s/math.pi

checks = 0
for d in (1,2,5):
    for n in (100,400,1600):
        lam=eigenvalue(n,d)
        target=c+filtered(math.sqrt(n+d), 1/8)
        tolerance={100:0.11,400:0.06,1600:0.032}[n]
        assert abs(lam-target)<tolerance,(d,n,lam,target,lam-target)
        checks+=1

for r,tol in ((12,0.11),(30,0.05),(60,0.024)):
    b=berezin_numeric(r)
    target=c+filtered(r,1/4)
    assert abs(b-target)<tol,(r,b,target,b-target)
    checks+=1

s_eigen=sum(abs(w)*math.exp(-v*v/8) for v,w in zip(freqs,weights))
s_berezin=sum(abs(w)*math.exp(-v*v/4) for v,w in zip(freqs,weights))
assert s_eigen>s_berezin
assert c-s_eigen < 0 < c-s_berezin
checks+=3

# The nonperiodic example has limiting full-torus extrema (Kronecker density).
# These finite samples check the predicted values only as diagnostics.
rs=np.arange(0,4000,0.03)
for t in (1/8,1/4):
    vals=sum(w*math.exp(-t*v*v)*np.cos(v*rs) for v,w in zip(freqs,weights))
    theoretical=sum(abs(w)*math.exp(-t*v*v) for v,w in zip(freqs,weights))
    assert vals.min() < -theoretical+0.003, (t, vals.min(), -theoretical)
    assert vals.max() > theoretical-0.003, (t, vals.max(), theoretical)
    checks+=2
# The universal upper bound is the total variation of two Gaussian filters.
a_star = math.sqrt(math.log(2)/2)
k1 = lambda x: math.sqrt(2/math.pi)*math.exp(-2*x*x)
k2 = lambda x: 1/math.sqrt(math.pi)*math.exp(-x*x)
exact = 2*(erf(math.sqrt(math.log(2))) - erf(math.sqrt(math.log(2)/2)))
assert abs(k1(a_star)-k2(a_star)) < 1e-13
assert k1(0)>k2(0) and k1(1)<k2(1)
num, error=quad(lambda x: abs(k2(x)-k1(x)), -8,8,epsabs=1e-12,points=[-a_star,a_star])
assert error < 1e-10 and abs(num-exact)<1e-12
assert 0.3321281499<exact<0.3321281501
checks += 4

# Periodic -1 bumps of halfwidth a_star, with center spacing L, approximate
# the continuous L-infinity extremizer. Check the rigorous heat-mass envelope.
def periodic_mass(L,t,s):
    stdev=math.sqrt(2*t)
    return sum(ndtr((j*L+a_star-s)/stdev)-ndtr((j*L-a_star-s)/stdev)
               for j in range(-5,6))

for L in (8.,16.,32.):
    lo={}
    for t in (1/8,1/4):
        Q=erf(a_star/(2*math.sqrt(t)))
        tail=2*(1-ndtr((L/2-a_star)/math.sqrt(2*t)))
        center=1-2*periodic_mass(L,t,0)
        assert abs(center-(1-2*Q)) < 2e-5, (L,t,center,Q)
        for s in np.linspace(0,L/2,61):
            val=1-2*periodic_mass(L,t,float(s))
            assert 1-2*Q-2*tail-1e-12 <= val <= 1+1e-12, (L,t,s,val)
            checks+=1
        lo[t]=center
        checks+=1
    assert abs((lo[1/4]-lo[1/8])-exact) < 1e-4
    checks+=1

# The normalized sample irrational-frequency discrepancy is strictly within the
# universal optimum (the phases have a dense two-torus orbit).
sample_delta=(s_eigen-s_berezin)/sum(abs(w) for w in weights)
assert 0 < sample_delta < exact
checks+=1
print(f"CHECK_OK {checks} deterministic validations; sharp gap {exact:.16f}; two-tone gap {sample_delta:.16f}")
