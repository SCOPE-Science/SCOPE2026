#!/usr/bin/env python3
"""Finite numerical checks for a closed-form theorem on Gabor lifting.
Run: python verify.py; requires numpy. These tests support but do not replace the proof.
"""
import cmath
import math
import numpy as np


def family(p, z):
    g = np.ones(p, dtype=complex)
    g[0] += z
    return g / np.linalg.norm(g)


def diagonal_singular_values(p,z):
    B = p + abs(z)**2 + 2*z.real
    gamma = abs(z)**2 + 2*z.real
    result = [1.0]
    result += [abs(gamma)/B]*(p-1)
    result += [abs(p+2*z.real)/B]*(p-1)
    for j in range(1,p):
        result += [abs(z + z.conjugate()*cmath.exp(2j*math.pi*j/p))/B]*(p-1)
    return np.sort(np.sqrt(p)*np.array(result))


def actual_singular_values(p,z):
    h = family(p,z)
    ii = np.arange(p)
    M = []
    for k in range(p):
        for ell in range(p):
            v = np.roll(h,k) * np.exp(2j*np.pi*ell*ii/p)
            M.append(np.outer(v.conjugate(),v).reshape(-1))
    return np.sort(np.linalg.svd(np.array(M),compute_uv=False))


def ratio(p,z):
    return diagonal_singular_values(p,z)[0] / math.sqrt(p)


def run():
    error=0.0; matrices=0
    for p in [5,7,11]:
        for z in [1j*math.sqrt(p),-1j*math.sqrt(p),0.7+0.8j,-1.5+0.65j]:
            actual=actual_singular_values(p,z)
            expected=diagonal_singular_values(p,z)
            error=max(error,float(np.max(np.abs(actual-expected))))
            assert np.allclose(actual,expected,atol=3e-12,rtol=2e-11)
            matrices+=1
        z=1j*math.sqrt(p)
        assert abs(ratio(p,z)-math.sin(math.pi/p)/math.sqrt(p))<1e-13
        assert abs(ratio(p,-z)-math.sin(math.pi/p)/math.sqrt(p))<1e-13
        for r in np.linspace(0,2.5*math.sqrt(p),41):
            for phi in np.linspace(0,2*math.pi,145,endpoint=False):
                trial=r*cmath.exp(1j*phi)
                assert ratio(p,trial)<=math.sin(math.pi/p)/math.sqrt(p)+2e-13
    print(f'VERIFY_OK matrices={matrices} first_three_primes=[5,7,11] actual_SVD=PASS parameter_grid=17835 max_singular_error={error:.3g}')


if __name__=='__main__': run()
