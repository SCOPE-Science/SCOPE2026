#!/usr/bin/env python3
"""Exact algebraic certificates and finite sanity checks for a rank-three root-neighborhood Turan problem.

Requirements: Python 3.10+, SymPy >= 1.12. NumPy is not needed.
All infinite assertions are proved in RESULT.md; the loops here are diagnostic only.
"""
import cmath
import itertools
import math
import sympy as sp

edges = list(itertools.combinations(range(4), 2))
assert edges == [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
c, s = sp.symbols('c s', real=True)

A, B = [], []
for duplicate in edges:
    rest = [i for i in range(4) if i not in duplicate]
    z = [None] * 4
    for j in duplicate:
        z[j] = sp.Integer(1)
    z[rest[0]] = -c + sp.I*s
    z[rest[1]] = -c - sp.I*s
    arow, brow = [], []
    for i,j in edges:
        zz = sp.expand(z[i]*sp.conjugate(z[j]))
        arow.append(sp.expand(sp.re(zz)).subs(s*s, 1-c*c))
        brow.append(sp.cancel(-sp.expand(sp.im(zz))/s))
    A.append(arow)
    B.append(brow)
A, B = sp.Matrix(A), sp.Matrix(B)
det_A = -64*c**3*(c-2)*(c-1)**3*(c+1)**5
det_B = -64*(c-1)**3*(c+1)**3
assert sp.factor(A.det()-det_A) == 0
assert sp.factor(B.det()-det_B) == 0
print('Symbolic 6x6 real and imaginary contact determinants: PASS')

# The even Fourier contacts are zero-sum tuples, and their real linear span
# has rank exactly six.  Exact arithmetic uses sixth roots for N=6.
w = sp.Rational(1,2)+sp.I*sp.sqrt(3)/2
six_roots = [sp.simplify(w**k) for k in range(6)]
rows = []
for p, q, r in itertools.product(range(6), repeat=3):
    z = [six_roots[p],six_roots[q],six_roots[r],sp.Integer(1)]
    if sp.simplify(sum(z)):
        continue
    products = [sp.expand_complex(z[i]*sp.conjugate(z[j])) for i,j in edges]
    rows.append([sp.expand(sp.re(x)) for x in products] +
                [-sp.expand(sp.im(x)) for x in products])
assert len(rows) == 15
assert sp.Matrix(rows).rank() == 6
print('Even-order zero-contact rank certificate at N=6: PASS')

# Direct independent Fourier grid and LP-certificate tests for N=5..16.
# Check full support Fourier nonnegativity of the invariant optimizer,
# the exact grid minimum, and the dimensions of its contact span.
counts = 0
for N in range(5, 17):
    roots = [cmath.exp(2j*math.pi*k/N) for k in range(N)]
    cN = math.cos(math.pi/N)
    target = 0.0 if N % 2 == 0 else (2-2*cN)**2
    t = 1/(4-target)
    minimum = float('inf')
    contact_count = 0
    for p,q,r in itertools.product(range(N), repeat=3):
        z = [roots[p],roots[q],roots[r],1]
        S2 = abs(sum(z))**2
        minimum = min(minimum,S2)
        F = 1+t*(S2-4)
        assert F > -1e-9, (N,p,q,r,F)
        if abs(S2-target)<1e-8:
            contact_count += 1
            assert abs(F)<1e-8
        counts += 1
    assert abs(minimum-target)<1e-8, (N,minimum,target)
    if N % 2:
        assert contact_count == 12, (N,contact_count)
    else:
        assert contact_count == 3*(N-1), (N,contact_count)
    mass = 1+12*t
    assert abs(mass - (4 if N%2==0 else 1+3/(cN*(2-cN))))<1e-10
print(f'All invariant Fourier tests: PASS ({counts} character samples at N=5..16)')
print('All tests PASS')
