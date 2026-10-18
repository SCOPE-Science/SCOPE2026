#!/usr/bin/env python3
"""Numerical consistency tests for radial Bergman-to-Fock spectral limits.

Needs Python 3, numpy, and scipy. This is supplementary to the proof.
"""
import math
import numpy as np
from scipy.special import betainc, gammainc, gammaln

def spectrum(d, t, s, nmax=110):
    n = np.arange(nmax)
    b = betainc(n + d, s + 1, t / s)
    f = gammainc(n + d, t)
    a = np.exp(-t + (n + d) * np.log(t) - gammaln(n + d)) * (n + d + 1 + t) / 2
    mult = np.array([math.comb(int(k + d - 1), d - 1) for k in n], dtype=float)
    return b, f, a, mult

def exact_trace(d, t, s):
    x = math.prod(s + j for j in range(1, d + 1)) / (s - t) ** d
    return t ** d / math.factorial(d) * (x - 1)

def limit_trace(d, t):
    return t ** d / math.factorial(d) * (d * (d + 1) / 2 + d * t)

def main():
    count = 0
    for d in (1, 2, 3, 4):
        for t in (0.2, 1.0, 3.2):
            for s in (60.0, 250.0, 600.0):
                b, f, a, mult = spectrum(d, t, s)
                delta = b - f
                assert np.min(delta) >= -2e-13, (d,t,s,'negative eigenvalue')
                observed = float(np.dot(mult, delta))
                expected = exact_trace(d, t, s)
                assert abs(observed - expected) < 2e-9, (d,t,s,observed,expected)
                assert abs(float(np.dot(mult, a)) - limit_trace(d, t)) < 2e-8
                if s >= 600:
                    error = float(np.dot(mult, abs(s * delta - a)))
                    assert error < 0.11 * (1.0 + limit_trace(d,t)), (d,t,error)
                count += 1
    for d in (1, 2, 3, 4):
        for k in (0, 1, 2, 3):
            threshold = math.sqrt(1.0 + (k + d) * (k + d + 1)) - 1.0
            n = np.arange(k + 3)
            _, _, aa, _ = spectrum(d, threshold, 200, k + 3)
            assert abs(aa[k] - aa[k + 1]) < 1e-12
            assert aa[k] > max([0.] + list(aa[:k])) if k>0 else aa[k]>0
            assert aa[k] > max(aa[k+2:]) if k+2<len(aa) else True
            count += 1
    print(f'PASS: {count} cases; positivity, exact traces, trace-class first-order, spectral thresholds')

if __name__ == '__main__':
    main()
