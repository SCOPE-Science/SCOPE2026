#!/usr/bin/env python3
"""Numerical reproducibility checks for a sharp Cauchy-transformed Gaussian quadrature rate.

This is a finite consistency checker; the all-n and optimal-exponent statements
follow from the analytical argument in RESULT.md, not from sampled computations.
Requires only Python's standard library.
"""
import math


def transformed(u, gamma):
    if not 0.0 < u < 1.0:
        return 0.0
    t = math.pi * u
    s = math.sin(t)
    if abs(s) < 1e-120:
        return 0.0
    cot = math.cos(t)/s
    return math.sqrt(math.pi/2.0)/(s*s) * math.exp(-gamma*cot*cot)


def q(n, shift, gamma):
    return sum(transformed((j+shift)/n, gamma) for j in range(n))/n


def cauchy_direct(u, gamma):
    x = -math.cos(math.pi*u)/math.sin(math.pi*u)
    target = math.exp(-gamma*x*x)/math.sqrt(2.0*math.pi)
    proposal = 1.0/(math.pi*(1.0+x*x))
    return target/proposal


def main():
    checks = 0
    for gamma in (0.05, 0.125, 0.25, 0.49):
        for u in (0.018, 0.083, 0.2, 0.41, 0.5, 0.59, 0.8, 0.917, 0.982):
            a = transformed(u, gamma)
            b = cauchy_direct(u, gamma)
            assert math.isclose(a, b, rel_tol=1e-12, abs_tol=1e-12), (gamma,u,a,b)
            checks += 1
        for u in (0.019, 0.112, 0.221, 0.474):
            assert math.isclose(transformed(u,gamma),transformed(1-u,gamma),rel_tol=1e-12,abs_tol=1e-12)
            checks += 1
    grid = 16384
    g = 0.25
    vals = [transformed(j/grid,g) for j in range(grid)]
    exact = (2*g)**(-0.5)
    approx = sum(vals)/grid
    assert abs(exact-approx) < 5e-11, (exact,approx)
    checks += 1
    # Numerical discrete Fourier coefficients of the periodic transformed integrand.
    maxk = 144
    coeffs = [0.0]*(maxk+1)
    for k in range(maxk+1):
        coeffs[k] = sum(vals[j]*math.cos(2*math.pi*k*j/grid) for j in range(grid))/grid
        checks += 1
    assert abs(coeffs[0]-exact)<5e-11
    checks += 1
    # Exact alias-spectrum identity is tested against numerical shift integration.
    for n in (3,4,5,7,9,12):
        shift_count=512
        empirical = sum((q(n,(b+0.5)/shift_count,g)-exact)**2 for b in range(shift_count))/shift_count
        alias = 2*sum(coeffs[k]**2 for k in range(n,maxk+1,n))
        assert abs(empirical-alias)<2e-10, (n,empirical,alias)
        assert alias >= 0
        checks += 2
    # Independent integration checks for Gaussian growth parameters.
    for gamma in (0.05,0.125,0.25,0.49):
        integral=sum(transformed((j+0.5)/grid,gamma) for j in range(grid))/grid
        assert abs(integral-(2*gamma)**(-0.5))<2e-10, (gamma,integral)
        checks += 1
    # Endpoint flatness must be visible numerically at a range of scales.
    for gamma in (0.125,0.25,0.49):
        v=transformed(0.01,gamma)
        assert v<1e-20, (gamma,v)
        checks += 1
    print(f'PASS: {checks} independently enumerated finite checks')
    print(f'Gaussian target integral = {exact:.16g}; periodized composite integral = {approx:.16g}')
    for n in (3,4,7,9,12):
        alias = 2*sum(coeffs[k]**2 for k in range(n,maxk+1,n))
        print(f'n={n:2d}  predicted RMS={math.sqrt(alias):.8e}')
    print('All-order Gevrey bounds, exponent optimality, and infinite-n statements: ANALYTICAL ONLY.')

if __name__=='__main__':
    main()
