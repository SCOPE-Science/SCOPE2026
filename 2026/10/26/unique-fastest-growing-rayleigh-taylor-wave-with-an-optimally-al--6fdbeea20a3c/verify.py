"""Numerical checks for the two-layer fixed-height Rayleigh--Taylor optimizer.

This checks finite samples of the closed formulas; the continuum claims
follow from the accompanying analytic proof. Requires numpy and scipy.
"""

import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

RNG = np.random.default_rng(1729)


def growth_squared(k, h, a, b, L, kc):
    if not (0 < k < kc and 0 < h < L):
        return 0.0
    den = a / np.tanh(k*h) + b / np.tanh(k*(L-h))
    return k*(kc*kc-k*k)/den  # common positive surface-tension factor omitted


def split(a, b, L, k):
    rlog = 0.5*math.log(a/b)
    S = k*L
    x = 0.5*(np.logaddexp(0., rlog+S) - np.logaddexp(0., rlog-S))
    return float(x/k)


def denominator_closed(a, b, L, k):
    S = k*L
    return (a+b)/np.tanh(S) + 2*np.sqrt(a*b)/np.sinh(S)


def elasticity(S, c):
    return 1 + S*(1+c*np.cosh(S))/(np.sinh(S)*(np.cosh(S)+c))


def k_opt(a, b, L, kc):
    c = 2*np.sqrt(a*b)/(a+b)
    return kc*brentq(
        lambda x: 2*x*x/(1-x*x)-elasticity(kc*L*x,c),
        0.56, 0.72, xtol=2e-14
    )


def test_fixed_k_allocation(n=900):
    passed = 0
    for _ in range(n):
        b = 10**RNG.uniform(-1.5,1.5)
        a = b*(1+10**RNG.uniform(-1.2,1.7))
        L = 10**RNG.uniform(-1.,0.8)
        k = 10**RNG.uniform(-1.,.8)
        if k*L > 7:
            continue
        h = split(a,b,L,k)
        D = denominator_closed(a,b,L,k)
        direct = a/np.tanh(k*h)+b/np.tanh(k*(L-h))
        assert abs(D/direct-1)<3e-12
        assert 0.5<h/L<np.sqrt(a)/(np.sqrt(a)+np.sqrt(b))
        deq = (a+b)/np.tanh(k*L/2)
        deficit = (np.sqrt(a)-np.sqrt(b))**2/np.sinh(k*L)
        assert np.isclose(deq-D, deficit, rtol=2e-9, atol=2e-11)
        numeric = minimize_scalar(
            lambda v: a/np.tanh(k*v)+b/np.tanh(k*(L-v)),
            bounds=(L*1e-6,L*(1-1e-6)), method="bounded",
            options={"xatol":L*1e-12}
        )
        assert D <= numeric.fun*(1+1e-10)
        if k*L < 3:
            assert abs(numeric.x-h)/L < 2e-4
        passed += 1
    return passed


def test_global_optimizer(n=800):
    passed = 0
    for _ in range(n):
        b = 10**RNG.uniform(-1.5,1.5)
        a = b*(1+10**RNG.uniform(-1.2,1.7))
        L = 10**RNG.uniform(-1.3,1.2)
        kc = 10**RNG.uniform(-1.3,1.2)
        if L*kc>12:
            continue
        k = k_opt(a,b,L,kc)
        h = split(a,b,L,k)
        assert kc/np.sqrt(3)<k<kc/np.sqrt(2)
        numeric = minimize_scalar(
            lambda z: -growth_squared(z,split(a,b,L,z),a,b,L,kc),
            bounds=(0.3*kc,0.85*kc), method="bounded",
            options={"xatol":kc*1e-12}
        )
        assert abs(k-numeric.x)/kc < 2e-5
        assert growth_squared(k,h,a,b,L,kc) > growth_squared(k,L/2,a,b,L,kc)
        c = 2*np.sqrt(a*b)/(a+b)
        step = min(1e-5,kc*L*1e-5)
        S = k*L
        if S>step:
            der = (elasticity(S+step,c)-elasticity(S-step,c))/(2*step)
            assert der<-1e-10
        passed += 1
    return passed


def test_depth_order(n=400):
    for _ in range(n):
        b = 10**RNG.uniform(-1.,1.)
        a = b*(1+10**RNG.uniform(-1.,1.))
        kc = 10**RNG.uniform(-1.,1.)
        L0 = 10**RNG.uniform(-1.,.5)/kc
        k0 = k_opt(a,b,L0,kc)
        k1 = k_opt(a,b,2*L0,kc)
        assert k0>k1
        v0=growth_squared(k0,split(a,b,L0,k0),a,b,L0,kc)
        v1=growth_squared(k1,split(a,b,2*L0,k1),a,b,2*L0,kc)
        assert v1>v0
        S0=kc*L0*.6
        S1=S0*2
        p0=split(a,b,S0/kc/.6,kc*.6)/(S0/kc/.6)
        p1=split(a,b,S1/kc/.6,kc*.6)/(S1/kc/.6)
        assert p0>p1
    return n


def test_limits():
    a,b,kc=4.,1.,1.
    L=1e-3
    ks=k_opt(a,b,L,kc)
    H=split(a,b,L,ks)
    val=growth_squared(ks,H,a,b,L,kc)
    target=(kc**4*L)/(4*(np.sqrt(a)+np.sqrt(b))**2)
    assert abs(ks/(kc/np.sqrt(2))-1)<2e-6
    assert abs(H/L-np.sqrt(a)/(np.sqrt(a)+np.sqrt(b)))<2e-6
    assert abs(val/target-1)<2e-6
    L=80.
    ks=k_opt(a,b,L,kc)
    H=split(a,b,L,ks)
    val=growth_squared(ks,H,a,b,L,kc)
    target=2*kc**3/(3*np.sqrt(3)*(a+b))
    assert abs(ks/(kc/np.sqrt(3))-1)<2e-6
    assert abs(val/target-1)<2e-6
    assert abs((2*H-L)-np.log(a/b)/(2*ks))<1e-6
    return 6


if __name__ == "__main__":
    n1=test_fixed_k_allocation()
    n2=test_global_optimizer()
    n3=test_depth_order()
    n4=test_limits()
    print(f"PASS: {n1} fixed-wavenumber, {n2} full-optimum, "
          f"{n3} height-order families, {n4} limit checks (some "
          "extreme parameter samples skipped for conditioning).")
