"""Exact grounded-Laplacian tests for clique-cone one-leader transitions.

Run: python VERIFY.py
Dependencies: sympy, numpy, scipy.
No sampled test replaces the stated all-size analytical proof.
"""
from itertools import combinations, product
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq


def cycle(m):
    assert m >= 3
    return sorted({tuple(sorted((i, (i + 1) % m))) for i in range(m)})


def clique(m):
    return list(combinations(range(m), 2))


def cube(d):
    assert d >= 2
    return [(i, i ^ (1 << j)) for i in range(1 << d)
            for j in range(d) if i < (i ^ (1 << j))]


def prism(m):
    return [(i, (i + 1) % m) for i in range(m)] + [
        (i + m, (i + 1) % m + m) for i in range(m)] + [
        (i, i + m) for i in range(m)]


def laplacian(r, m, edges, t):
    n = r + m
    mat = sp.zeros(n)
    def add(i, j, w):
        mat[i, i] += w
        mat[j, j] += w
        mat[i, j] -= w
        mat[j, i] -= w
    for i, j in combinations(range(r), 2):
        add(i, j, sp.Integer(1))
    for i in range(r):
        for j in range(m):
            add(i, r + j, sp.Integer(1))
    for i, j in edges:
        add(r + i, r + j, t)
    return mat


def trace_ground(mat, v):
    idx = [i for i in range(mat.rows) if i != v]
    inv = mat.extract(idx, idx).inv(method='DM')
    return sum(inv[i, i] for i in range(inv.rows))

cases = []
for m in range(3, 8):
    cases.append((f'cycle{m}', m, cycle(m)))
for m in range(2, 8):
    cases.append((f'clique{m}', m, clique(m)))
for d in (2, 3):
    cases.append((f'cube{d}', 1 << d, cube(d)))
cases.append(('triangular-prism', 6, prism(3)))

exact_checks = 0
symmetry_checks = 0
for name, m, edges in cases:
    h = sp.zeros(m)
    for i, j in edges:
        h[i, i] += 1
        h[j, j] += 1
        h[i, j] -= 1
        h[j, i] -= 1
    for r in (1, 2, 3):
        for t in (sp.Rational(1, 5), sp.Integer(1), sp.Rational(9, 2)):
            L = laplacian(r, m, edges, t)
            j_h = trace_ground(L, 0)
            j_v = trace_ground(L, r)
            n = r + m
            S = sum((r * sp.eye(m) + t * h).inv(method='DM')[i, i]
                    for i in range(m)) - sp.Rational(1, r)
            expected = sp.Rational(n, m) * (S - sp.Rational(m - 1, n))
            assert sp.simplify(j_v - j_h - expected) == 0, (name, r, t, j_h, j_v, expected)
            exact_checks += 1
            if name.startswith('clique') and t == 1:
                assert j_h == j_v
            if name.startswith('clique') and t != 1:
                assert (j_h < j_v) == (t < 1)
            if r > 1:
                assert j_h == trace_ground(L, r - 1)
                symmetry_checks += 1
            assert j_v == trace_ground(L, r + m - 1)
            symmetry_checks += 1
print('exact comparison identities:', exact_checks)
print('orbit symmetry comparisons:', symmetry_checks)

# Independent numerical threshold calculation using the exact cycle spectrum
spectral_checks = 0
asymptotic_checks = 0
for r in (1, 2, 3, 5):
    y = brentq(lambda v: v / math.tanh(v) - (r + 1), 1e-9, r + 2)
    c = r / (4 * y * y)
    d = r*r*(r+1) / (2 * y*y * (y*y-r*(r+1)))
    for m in (20, 40, 80, 160):
        def f(t):
            return sum(1/(r + 4*t*math.sin(math.pi*k/m)**2)
                       for k in range(1, m)) - (m-1)/(r+m)
        tstar = brentq(f, 0, 10 * m*m)
        assert abs(f(tstar)) < 1e-9
        assert tstar > 0
        assert m/4 - 1e-8 <= tstar <= m/(4*math.sin(math.pi/m)**2) + 1e-8
        assert abs(tstar - c*m*m - d*m) < 2, (r,m,tstar,c*m*m+d*m)
        spectral_checks += 1
        asymptotic_checks += 1
print('cycle threshold/bounds checks:', spectral_checks)
print('quadratic-plus-linear asymptotic comparisons:', asymptotic_checks)
print('All checks passed.')
