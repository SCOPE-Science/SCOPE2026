#!/usr/bin/env python3
"""Deterministic quadrature corroborating a Gaussian-copula boundary expansion.

Run: python VERIFY.py
Requires numpy and scipy. Quadrature is NOT the universal proof.
"""
import math
import numpy as np
from scipy.integrate import simpson
from scipy.special import ndtr, ndtri


def phi(x):
    return math.exp(-x*x/2) / math.sqrt(2*math.pi)


def theoretical_slope(p, w):
    q = float(ndtri(p))
    return 2*w*(1-w)*phi(q)*(q + phi(q)/p)


def exact_2d_integral(p, w, r, npoints=60001):
    """One-dimensional quadrature for the bivariate Gaussian joint law."""
    uc = p*w/(1-p*(1-w))
    xc = float(ndtri(uc))
    x = np.linspace(xc, 9.0, npoints)
    u = ndtr(x)
    v_thresh = p*(1-w)*u/(u-p*w)
    v_thresh = np.clip(v_thresh, np.nextafter(0.0, 1.0), np.nextafter(1.0, 0.0))
    cond = ndtr((ndtri(v_thresh)-r*x)/math.sqrt(1-r*r))
    integrand = np.exp(-x*x/2) * cond / math.sqrt(2*math.pi)
    return uc + float(simpson(integrand, x=x))


def main():
    cases = [(0.05,0.50),(0.20,0.25),(0.50,0.50),(0.90,0.40)]
    count = 0
    for p,w in cases:
        slope = theoretical_slope(p,w)
        assert slope > 0
        errs = []
        for r in (0.99, 0.997, 0.999):
            prob = exact_2d_integral(p,w,r)
            assert p < prob < 1, (p,w,r,prob)
            estimate = (prob-p)/(1-r)
            errs.append(abs(estimate-slope))
            count += 1
            print(f'p={p:.2f} w={w:.2f} r={r:.3f} probability={prob:.12f} estimate={estimate:.8f} slope={slope:.8f}')
        assert errs[-1] < errs[0] and errs[-1] < 0.005, (p,w,errs)
    print(f'PASS: {count} deterministic one-dimensional quadrature comparisons. Universal statement requires the analytic proof.')


if __name__ == '__main__':
    main()
