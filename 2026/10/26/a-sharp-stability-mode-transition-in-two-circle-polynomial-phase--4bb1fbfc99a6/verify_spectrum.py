#!/usr/bin/env python3
"""Numerical checks of a two-circle polynomial intensity Jacobian and its angular spectrum.

Run: python verify_spectrum.py
Requires numpy and scipy.
These are finite-dimensional checks, not a substitute for the analytic proof.
"""
import numpy as np
from scipy.optimize import brentq


def singular_formula(m, r, R):
    vals = [2.0 * np.hypot(r ** (2 * m), R ** (2 * m))]
    for j in range(1, m + 1):
        B = np.array([[r ** (2*m+j), r ** (2*m-j)],
                      [R ** (2*m+j), R ** (2*m-j)]])
        sj = np.sqrt(2) * np.linalg.svd(B, compute_uv=False)
        vals.extend([sj[0], sj[0], sj[1], sj[1]])
    return np.sort(vals)


def sampled_real_jacobian(m, r, R):
    count = 4*m+3
    theta = 2 * np.pi * np.arange(count) / count
    rows = []
    for radius in (r, R):
        z = radius*np.exp(1j*theta)
        base = z ** m
        b = np.stack([z**k for k in range(2*m+1)], axis=1)
        a = np.conj(base)[:, None] * b
        rows.append(np.concatenate((2*a.real, -2*a.imag), axis=1) / np.sqrt(count))
    return np.vstack(rows)


def mode_coeff(j, m, r):
    return 2*j*r**(2*m+j-1) / np.sqrt(1+r**(4*j))


def critical_radius(m):
    def f(r):
        return (np.log(m)+(m-1)*np.log(r)
                +0.5*np.log1p(r**4)-0.5*np.log1p(r**(4*m)))
    return brentq(f, 1e-10, 1-1e-12)


def main():
    number = 0
    for m in (2, 3, 5, 7):
        for r, R in ((.21, .76), (.55, .92), (.72, .91)):
            J = sampled_real_jacobian(m, r, R)
            sval = np.linalg.svd(J, compute_uv=False)
            actual = np.sort(sval[sval > 1e-10])
            expected = singular_formula(m, r, R)
            assert actual.size == 4*m+1, (m, actual.size)
            assert np.allclose(actual, expected, rtol=1e-10, atol=1e-12), (m, r, R)
            number += 1
    for m in (2, 3, 5, 10):
        for r in (.3, .55, .8):
            h=1e-6
            x=np.min(singular_formula(m,r,r+h))
            theory=min(mode_coeff(j,m,r) for j in range(1,m+1))*h
            assert abs(x/theory-1) < 2e-4, (m,r,x/theory)
            coeff=np.array([mode_coeff(j,m,r) for j in range(1,m+1)])
            assert np.min(coeff) == min(coeff[0],coeff[-1])
            number += 1
    for m in (2,3,4,5,10,20,50,100):
        rt=critical_radius(m)
        ratio=mode_coeff(m,m,rt)/mode_coeff(1,m,rt)
        assert abs(ratio-1)<5e-11
        if m > 2:
            mids=np.array([mode_coeff(j,m,rt) for j in range(2,m)])
            assert np.min(mids)>mode_coeff(1,m,rt)
        print('m=%d, threshold r=%.12f, -m log(r)-log(m)=%.9f'
              %(m,rt,-m*np.log(rt)-np.log(m)))
        number += 1
    print('PASS:',number,'finite-dimensional checks of singular spectrum, coalescing modes and thresholds')


if __name__=='__main__':main()
