#!/usr/bin/env python3
"""Numerical checks for the unequal-depth Kelvin-Helmholtz onset theorem.

Requirements: Python 3, scipy, numpy, mpmath. Independent checks compare
thresholds from the exact dispersion relation with the scalar minimization.
The analytic theorem is proved in RESULT.md, not inferred from these tests.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar
import mpmath as mp


def s_and_prime(z, heights, reciprocal_densities):
    s, sp = 0.0, 0.0
    for h, w in zip(heights, reciprocal_densities):
        x = h*math.sqrt(z)
        if x < 0.005:
            s += w*h*(1-x*x/3 + 2*x**4/15-17*x**6/315)
            sp += w*h**3*(-1/3+4*x*x/15-17*x**4/105)
        else:
            t = math.tanh(x)
            s += w*t/math.sqrt(z)
            sp += w*h**3*(x*(1-t*t)-t)/(2*x**3)
    return s, sp


def critical(z, h, w):
    s, sp = s_and_prime(z, h, w)
    return -s/sp-z


def threshold(B, h, w):
    m1 = sum(a*b for a,b in zip(w,h))
    m3 = sum(a*b**3 for a,b in zip(w,h))
    b0 = 3*m1/m3
    if B <= b0:
        return 0., B*m1
    right = max(1., B)
    while critical(right,h,w) < B:
        right *= 2
    z = brentq(lambda v: critical(v,h,w)-B, 1e-12, right,
               xtol=1e-12, rtol=1e-12)
    s,_ = s_and_prime(z,h,w)
    return z, (B+z)*s


def test_random():
    rng = np.random.default_rng(51720)
    count = 0
    for _ in range(240):
        h = np.exp(rng.uniform(-2.,2.,size=2))
        w = np.exp(rng.uniform(-2.,2.,size=2))
        if abs(h[0]-h[1]) < 0.01:continue
        m1 = np.sum(w*h);m3=np.sum(w*h**3)
        b0=3*m1/m3
        B=b0*float(np.exp(rng.uniform(-1.0,2.0)))
        z,f=threshold(B,h,w)
        vals = [critical(q,h,w) for q in np.geomspace(1e-3/h.max()**2,1e4/h.min()**2,140)]
        # Monotonicity on a resolved, nonsingular range.
        assert all(vals[i+1]>vals[i]-1e-8*max(vals[i],1) for i in range(len(vals)-1))
        if B>b0:
            def obj(v):
                q=math.exp(v)
                return (B+q)*s_and_prime(q,h,w)[0]
            fit=minimize_scalar(obj, bounds=(math.log(z)-4,math.log(z)+4),
                                method='bounded',options={'xatol':1e-11})
            assert abs(math.exp(fit.x)/z-1) < 0.001
            assert abs(fit.fun/f-1) < 1e-8
        else:
            assert z==0 and abs(f-B*m1)<1e-8
        # Direct exact dispersion discriminant threshold, independent algebra.
        rho=1/w
        k=float(np.exp(rng.uniform(-2,2)))
        alpha=rho/np.tanh(k*h)
        direct=(B/k+k)*(1/alpha[0]+1/alpha[1])
        transformed=(B+k*k)*s_and_prime(k*k,h,w)[0]
        assert abs(direct/transformed-1)<1e-9
        count+=1
    return count


def test_critical_scaling():
    mp.mp.dps=55
    cases=[([mp.mpf('1'),mp.mpf('3')],[mp.mpf('.4'),mp.mpf('1.2')]),
           ([mp.mpf('.2'),mp.mpf('4')],[mp.mpf('2'),mp.mpf('.1')]),
           ([mp.mpf('.8'),mp.mpf('1.4')],[mp.mpf('.5'),mp.mpf('2')])]
    checks=0
    for h,w in cases:
        M=lambda j:sum(a*b**j for a,b in zip(w,h))
        b0=3*M(1)/M(3)
        C=mp.mpf(12)/5*M(1)*M(5)/M(3)**2-2
        assert C>=mp.mpf('0.4')
        for ratio in ['0.001','0.0001','0.00001']:
            e=b0*mp.mpf(ratio)
            B=b0+e
            def S(z):
                return sum(a*mp.tanh(b*mp.sqrt(z))/mp.sqrt(z) for a,b in zip(w,h))
            def deriv(z):return mp.diff(S,z)
            def Bc(z):return -S(z)/deriv(z)-z
            z=mp.findroot(lambda zz: Bc(zz)-B,(e/C*mp.mpf('.9'),e/C*mp.mpf('1.1')))
            rel=abs(z/(e/C)-1)
            gap=B*M(1)-(B+z)*S(z)
            approx=M(3)*e*e/(6*C)
            assert rel<mp.mpf('0.02')
            assert abs(gap/approx-1)<mp.mpf('0.02')
            checks+=1
    return checks


if __name__=='__main__':
    n=test_random();m=test_critical_scaling()
    print('PASS:',n,'random onset/discriminant checks;',m,'high-precision edge-scaling checks')
