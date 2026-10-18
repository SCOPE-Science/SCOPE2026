#!/usr/bin/env python3
"""Exact rational checks for a tent-window Gabor frame-bound formula.

Run: python3 verify_frame_bounds.py
No nonstandard Python packages or network calls are required.
Finite tests supplement, and do not replace, the proof for all integers m >= 2.
"""
from fractions import Fraction as F
from math import comb


def fiber(m, tau):
    """Unscaled selfadjoint Jacobi fiber at t=tau/m, 0 <= tau < 1."""
    assert m >= 2 and 0 <= tau < 1
    h = F(1, m)
    u = [(F(j) + tau) / m for j in range(m)]
    d = [(1 - x)**2 + x**2 for x in u]
    e = [(1 - u[j]) * (u[j] - h) for j in range(1, m)]
    return d, e


def ground_vector(m, tau):
    """Strictly positive Gamma-binomial weights, up to a common factor."""
    assert 0 < tau < 1
    v = [F(1)]
    for j in range(m - 1):
        v.append(v[-1] * (m - j - tau - 1) / (j + tau))
    return v


def ground_residual(m, tau):
    d, e = fiber(m, tau)
    v = ground_vector(m, tau)
    mu = F(2 * (m - 1), m * m)
    res = []
    for j in range(m):
        z = (d[j] - mu) * v[j]
        if j:
            z -= e[j-1] * v[j-1]
        if j < m-1:
            z -= e[j] * v[j+1]
        res.append(z)
    expected = [F(0)] * m
    expected[0] = (1 - tau)**2 / m**2 * v[0]
    expected[-1] = tau**2 / m**2 * v[-1]
    return res == expected


def boundary_eigenvector(m):
    d, e = fiber(m, F(0))
    v = [F(0)] + [F(comb(m-2, j-1)) for j in range(1,m)]
    mu = F(2 * (m - 1), m*m)
    for j in range(m):
        z = d[j] * v[j]
        if j: z -= e[j-1]*v[j-1]
        if j < m-1: z -= e[j]*v[j+1]
        if z != mu*v[j]:
            return False
    return True


def positive_definite_tridiagonal(diag, off):
    """Exact LDL pivot positivity; off is the upper subdiagonal."""
    pivot = diag[0]
    if pivot <= 0:
        return False
    for j in range(1,len(diag)):
        pivot = diag[j] - off[j-1]**2 / pivot
        if pivot <= 0:
            return False
    return True


def run():
    tests = 0
    for m in range(2, 29):
        assert boundary_eigenvector(m)
        tests += 1
        b = F(m, m+1)
        bound_A = F(2*(m*m-1),m**3)
        bound_B = F(m+1,m)
        assert b*bound_A == F(2*(m-1),m*m)
        assert b*bound_B == 1
        tests += 2
        for tau in (F(1,11),F(1,4),F(1,2),F(3,4),F(10,11)):
            d,e = fiber(m,tau)
            assert all(z > 0 for z in e)
            assert ground_residual(m,tau)
            tests += 2
            # Exactly check both matrix bounds at each interior fiber.
            mu = F(2*(m-1),m*m)
            assert positive_definite_tridiagonal([x-mu for x in d],[-y for y in e])
            assert positive_definite_tridiagonal([1-x for x in d],[-y for y in e])
            tests += 2
            row = []
            for j in range(m):
                row.append(d[j] + (e[j-1] if j else 0) + (e[j] if j<m-1 else 0))
            assert all(z<1 for z in row)
            tests += 1
        d0, e0 = fiber(m,F(0))
        assert d0[0] == 1 and e0[0] == 0
        tests += 1
    # Direct finite Walnut coefficients for selected fibers, avoiding pre-expanded formulas.
    def tent(x):
        return max(F(0), 1-abs(x))
    for m in range(2,13):
        h = F(1,m)
        L = 1+h
        for tau in (F(1,4),F(3,4)):
            for j in range(m):
                u=(j+tau)/m
                got0=sum((tent(u-k)**2 for k in range(-3,4)),F(0))
                got1=sum((tent(u-k)*tent(u-k-L) for k in range(-3,4)),F(0))
                assert got0 == (1-u)**2+u**2
                assert got1 == (1-u)*(u-h) if u>=h else got1 == 0
                tests += 2
    print('PASS: all exact rational identities and LDL spectral inequalities')
    print('checked_instances:',tests)
    print('integer_range: 2..28; interior_phase_samples: 1/11,1/4,1/2,3/4,10/11')
    print('boundary_smallest_eigenvalue: 2(m-1)/m^2')
    print('frame_bounds: A=2(m^2-1)/m^3; B=(m+1)/m')
    print('condition_ratio: m^2/[2(m-1)]')

if __name__=='__main__':
    run()
