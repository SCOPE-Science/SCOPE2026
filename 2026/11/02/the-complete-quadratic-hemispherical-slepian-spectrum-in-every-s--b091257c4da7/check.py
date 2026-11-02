#!/usr/bin/env python3
"""Independent moment-matrix check of exact hemisphere restriction spectra.

Run: python check.py.  Uses normalized spherical measure; no sampled data.
"""
import math
import numpy as np
from scipy.linalg import eigvalsh


def sphere_half_moment(exponents, hemi):
    """Exactly derived gamma-product moments, numerically evaluated.
    If hemi=False, integrate over entire S^(d-1); otherwise x_0>0.
    """
    d = len(exponents)
    if hemi:
        if any(e % 2 for e in exponents[1:]):
            return 0.0
        val = math.lgamma(d/2) - math.lgamma((d+sum(exponents))/2)
        val += math.lgamma((exponents[0]+1)/2) - math.lgamma(0.5)
        val += sum(math.lgamma((e+1)/2) - math.lgamma(0.5) for e in exponents[1:])
        return 0.5*math.exp(val)
    if any(e % 2 for e in exponents):
        return 0.0
    val = math.lgamma(d/2) - math.lgamma((d+sum(exponents))/2)
    val += sum(math.lgamma((e+1)/2)-math.lgamma(0.5) for e in exponents)
    return math.exp(val)


def monomials(d):
    out = [(0,)*d]
    for i in range(d):
        e = [0]*d; e[i]=1; out.append(tuple(e))
    for i in range(d):
        for j in range(i,d):
            if i == j == d-1:  # x_{d-1}^2 is redundant by the sphere equation
                continue
            e = [0]*d; e[i]+=1; e[j]+=1
            out.append(tuple(e))
    assert len(out) == d*(d+3)//2
    return out


def formula(d):
    mu = math.exp(math.lgamma(d/2)-0.5*math.log(math.pi)-math.lgamma((d+1)/2))
    s0 = d*mu*math.sqrt((3*d+5)/2)/(d+1)
    s1 = d*mu*math.sqrt(d+2)/(d+1)
    assert 0 < s1 < s0 < 1
    return sorted([.5+s0/2, .5-s0/2] + ([.5+s1/2, .5-s1/2] * (d-1)) + [.5]*(d*(d-1)//2))


def independent_spectrum(d):
    exps = monomials(d)
    q = len(exps)
    full = np.empty((q,q)); half = np.empty((q,q))
    for i,a in enumerate(exps):
        for j,b in enumerate(exps):
            z=tuple(x+y for x,y in zip(a,b))
            full[i,j] = sphere_half_moment(z,False)
            half[i,j] = sphere_half_moment(z,True)
    vals = eigvalsh(half, full)
    return vals


def run():
    total = 0
    for d in range(3,11):
        found = independent_spectrum(d)
        expected = np.array(formula(d))
        err = np.max(np.abs(found-expected))
        assert err < 2e-12, (d,err)
        assert abs(sum(found)-len(found)/2) < 1e-12
        total += len(found)
        print(f'd={d} dim={len(found)} gap={err:.2g} upper={found[-1]:.12f} lower={found[0]:.12f}')
    # Exact formula identities for d=3: mu=1/2, s0=3 sqrt(7)/8, s1=3 sqrt(5)/8.
    s0,s1 = 3*math.sqrt(7)/8,3*math.sqrt(5)/8
    a=formula(3)
    assert abs(a[-1]-(1+s0)/2)<1e-14
    assert abs(a[-2]-(1+s1)/2)<1e-14
    # Check strict parity-step decay through d=100 using the exact rational ratios.
    for d in range(3,101):
        assert (d+2)**2*(3*d+11) < (d+3)**2*(3*d+5)
        assert (d+2)*(d+4) < (d+3)**2
    print(f'ALL_CHECKS_PASS {total} independent eigenvalues; exact d=3; parity-step inequalities')

if __name__ == '__main__':
    run()
