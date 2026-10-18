#!/usr/bin/env python3
"""Finite diagnostics for centered Cantor correlation identities.

Uses Python's standard library only; this does not replace universal proofs.
"""
import cmath
import itertools
import math


def profile(b, c, limit):
    p = 2
    zeta2 = math.pi**2 / 6
    L = 2 - 2 * b - c * zeta2
    assert 0 < c < 2 * b and L > 0
    beta = [2 * b] + [c / j**p for j in range(1, limit + 1)]
    d = []
    tail = c * zeta2 + 2 * b
    for j in range(limit):
        d.append(2**(-j-2) * (L + tail + beta[j]))
        tail -= beta[j]
    return L, d


def run():
    count = 0
    for b, c in [(0.2, 0.06), (0.27, 0.12), (0.35, 0.21), (0.11, 0.03)]:
        L, d = profile(b, c, 700)
        assert abs(sum(d) - 1.0) < 2e-14; count += 1
        assert abs(d[0] - (1+b)/2) < 5e-15; count += 1
        assert d[0] > sum(d[1:]); count += 1
        Q = 2*b + c*sum((1/4)**j/j**2 for j in range(1, 80))
        R = c*sum((1/4)**j/j for j in range(1, 80))
        W0 = sum(4**(-j) * (d[j] * 4 * 2**j) for j in range(70))
        W1 = sum(j * 4**(-j) * (d[j] * 4 * 2**j) for j in range(70))
        assert abs(W0 - (8+2*Q)/3) < 1e-13; count += 1
        assert abs(W1 - (8-4*Q+6*R)/9) < 1e-13; count += 1
        A = L*(4+Q)/24
        assert abs(A - L*W0/16) < 1e-13; count += 1
        J = W1/W0
        for n in [10, 30, 60, 120, 250]:
            cov = sum(d[j]*d[j+n] for j in range(110))
            val = math.ldexp(cov, n)
            asymp = A*(1 + c/L/n + c/L*(1.5-J)/n**2)
            assert abs(val-asymp) < 0.002/n**2, (b,c,n,val,asymp)
            count += 1
        # Exact finite-cutoff Bernoulli covariance from all sign strings.
        K = 7
        for n in [0, 1, 2, 3]:
            exact = sum(d[j]*d[j+n] for j in range(K-n))
            brute = 0.0
            for sig in itertools.product((-1,1), repeat=K):
                x0 = sum(d[j]*sig[j] for j in range(K))
                xn = sum(d[j]*sig[n+j] for j in range(K-n))
                brute += x0*xn
            brute /= 2**K
            assert abs(brute-exact) < 4e-15; count += 1
        # Spectral factor: recover coefficients by Fourier sampling log spectrum.
        M = 2048
        m = 6
        coeffs = [0j]*m
        for j in range(M):
            theta=2*math.pi*j/M
            z=cmath.exp(1j*theta)
            spectrum=abs(sum(d[k]*z**k for k in range(27)))**2
            for k in range(m):
                coeffs[k] += math.log(spectrum)*cmath.exp(-1j*k*theta)/M
        assert abs(math.exp(coeffs[0].real/2)-d[0]) < 3e-10; count += 1
        # exp of Taylor series log(D) recovers the displacement coefficients.
        rec=[0j]*m
        rec[0]=math.exp(coeffs[0].real/2)
        for n in range(1,m):
            rec[n]=sum(k*coeffs[k]*rec[n-k] for k in range(1,n+1))/n
        for k in range(m):
            assert abs(rec[k]-d[k]) < 3e-9, (k,rec[k],d[k])
            count += 1
    print('VERIFY_OK',count,'diagnostics (finite cases only)')

if __name__ == '__main__':
    run()
