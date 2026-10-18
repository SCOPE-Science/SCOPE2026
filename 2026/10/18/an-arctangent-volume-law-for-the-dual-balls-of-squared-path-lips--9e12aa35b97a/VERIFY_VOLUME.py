#!/usr/bin/env python3
"""Exact finite checks for 1-Lipschitz balls on squared paths.

The two routes use (a) symbolic iterated integration and (b) vertices plus
triangulated boundary simplices, with exact determinant volumes. SciPy chooses
facets numerically, while every reported vertex and simplex volume is checked
exactly over the rationals.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

x, z = sp.symbols('x z')

def transfer_volumes(max_d):
    p = sp.Integer(1)
    values = []
    for d in range(1, max_d + 1):
        integral = sp.integrate(p, (x, 0, 1))
        values.append(sp.factor(2 * integral))
        p = sp.factor(integral + sp.integrate(p.subs(x, sp.Symbol('u')), (sp.Symbol('u'), 0, 1-x)))
    return values

def independent_polytope_volume(d):
    if d == 1:
        return sp.Integer(2)
    A = []
    for j in range(d):
        e = [0] * d; e[j] = 1
        A.extend((e[:],[-t for t in e]))
    for j in range(d-1):
        e = [0] * d; e[j] = 1; e[j+1] = -1
        A.extend((e[:],[-t for t in e]))
    A = np.array(A, dtype=int)
    verts = set()
    for ids in combinations(range(len(A)), d):
        B = A[list(ids), :]
        try:
            vertex = np.linalg.solve(B.astype(float), np.ones(d))
        except np.linalg.LinAlgError:
            continue
        if not np.all(A @ vertex <= 1+1.e-8):
            continue
        v = tuple(int(round(t)) for t in vertex)
        assert np.linalg.norm(vertex-np.array(v),np.inf)<1.e-8, ('non-integral',v,vertex)
        assert all(sum(int(a)*q for a,q in zip(row,v))<=1 for row in A)
        verts.add(v)
    vv = sorted(verts)
    hull = ConvexHull(np.array(vv,dtype=float))
    total = sp.Integer(0)
    for simplex in hull.simplices:
        mat = sp.Matrix([vv[j] for j in simplex])
        total += abs(mat.det()) / sp.factorial(d)
    return sp.factor(total)

def main():
    values = transfer_volumes(12)
    expectation = [sp.Integer(2),sp.Integer(3),sp.Rational(14,3),sp.Rational(29,4),sp.Rational(169,15)]
    assert values[:len(expectation)] == expectation
    for d in range(1,6):
        v=independent_polytope_volume(d)
        assert v==values[d-1], ('volume mismatch', d,v,values[d-1])
        print(f'dimension={d}; exact_volume={v}; independent_hull=PASS')
    # Verify the exact analytic resolvent expression through coefficient degree 11.
    G=2*(1+sp.sin(z)-sp.cos(z))/(z*(2*sp.cos(z)-1-sp.sin(z)))
    Taylor=sp.series(G,z,0,12).removeO().expand()
    for k,v in enumerate(values):
        assert sp.simplify(Taylor.coeff(z,k)-v)==0, ('resolvent mismatch',k)
    theta=sp.atan(sp.Rational(3,4))
    f=sp.cos(theta*x)-sp.Rational(1,2)*sp.sin(theta*x)
    # Use exact trigonometry at the 3-4-5 angle to check endpoint and integrals.
    assert sp.simplify(sp.cos(theta)-sp.Rational(4,5))==0
    assert sp.simplify(sp.sin(theta)-sp.Rational(3,5))==0
    assert sp.simplify(f.subs(x,1)-sp.Rational(1,2))==0
    assert sp.simplify(2*sp.integrate(f,(x,0,1))-1/theta)==0
    assert sp.simplify(2*sp.integrate(f**2,(x,0,1))-sp.Rational(5,4))==0
    assert sp.simplify((2*sp.cos(theta)-1-sp.sin(theta)))==0
    # Mittag-Leffler/cotangent representation: exact derivatives match
    # the first eight independently integrated volumes.
    C=sp.symbols('C', real=True)
    cot_derivative=C/sp.Integer(2)
    for n in range(2,10):
        cot_derivative=sp.expand(-(1+C*C)*sp.diff(cot_derivative,C)/2)
        lattice=sp.Rational(4,5)*(-1)**(n-1)*cot_derivative.subs(C,3)/sp.factorial(n-1)
        assert sp.simplify(lattice-values[n-2])==0, ('lattice mismatch',n)
    print('8 EXACT COTANGENT/LATTICE COEFFICIENTS: PASS')
    print('12 EXACT TAYLOR COEFFICIENTS AND PERRON NORMALIZATION: PASS')
    print('ALL EXACT SQUARED-PATH LIPSCHITZ VOLUME CHECKS PASSED')

if __name__=='__main__':
    main()
