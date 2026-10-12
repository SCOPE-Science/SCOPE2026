#!/usr/bin/env python3
"""Independent numerical checks for an exact two-qubit phase-damping survival law."""
import math
import numpy as np
from scipy.integrate import quad

rng = np.random.default_rng(729100)

def ratio_cdf(h):
    if not (0 < h < 1):
        raise ValueError('the endpoint formula uses 0<h<1')
    return h*math.log(1/h)/(1-h)**2 - h/(1-h)

def ratio_density(h):
    if h <= 0:
        return 0.
    if abs(h-1.) < 1e-4:
        return 1/6
    return ((1+h)*math.log(1/h)-2*(1-h))/(1-h)**3

def spectral_entangled(v,s):
    rho = np.outer(v,v.conj())
    damping = np.array([[s**(int((i//2)!=(j//2))+int((i%2)!=(j%2)))
                        for j in range(4)] for i in range(4)])
    output = rho*damping
    partial_transpose = output.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    return np.linalg.eigvalsh(partial_transpose)[0] < -1e-12

def analytic_entangled(v,s):
    P, Q = v[0]*v[3], v[1]*v[2]
    return math.sqrt(abs(P*Q)) < (s/(1-s*s))*abs(P-Q)

def angle_prob(w,e):
    r=math.sqrt(w)
    threshold=(r+1/r-1/e**2)/2
    if threshold<=-1:
        return 0.
    if threshold>=1:
        return 1.
    return 1-math.acos(threshold)/math.pi

def exact_integral_and_bounds(s):
    e=s/(1-s*s)
    assert e<.5
    low=((math.sqrt(1+4*e*e)-1)/(2*e))**4
    high=((1-math.sqrt(1-4*e*e))/(2*e))**4
    central=quad(lambda w:ratio_density(w)*angle_prob(w,e),low,high,
                 epsabs=2e-14,epsrel=2e-11)[0]
    return 2*(ratio_cdf(low)+central), 2*ratio_cdf(low), 2*ratio_cdf(high)

for s in [.12,.45,.75]:
    for k in range(60):
        v=rng.normal(size=4)+1j*rng.normal(size=4)
        v=v/np.linalg.norm(v)
        assert spectral_entangled(v,s)==analytic_entangled(v,s),(s,k)

for s in [.2,.12,.08,.05,.03,.015]:
    exact, low, high=exact_integral_and_bounds(s)
    assert low<=exact<=high
    two_term=8*s**4*math.log(1/s)-2*s**4
    # The remainder is O(s^6 log(1/s)), not O(s^6).
    assert abs(exact-two_term) < 40*s**6*math.log(1/s)

# Check the exact product-ratio distribution by its independent defining integral.
for h in [.007,.03,.18,.5,.9]:
    alternative=quad(lambda x:h/((x+h)*(1+x)**2),0,math.inf,epsabs=1e-12)[0]
    assert abs(alternative-ratio_cdf(h))<2e-10
print('VERIFY_OK direct_PPT=180 ratio_CDF=5 phase_integrals=6 sharp_tail=passed')
