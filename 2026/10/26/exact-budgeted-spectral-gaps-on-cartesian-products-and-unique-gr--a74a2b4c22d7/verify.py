#!/usr/bin/env python3
"""Standalone exact and numerical checks of optimized Cartesian-grid Laplacians.

Run: python3 verify.py
Requires Python 3, SymPy and NumPy. The theorem itself has an analytic proof.
"""
from fractions import Fraction
from itertools import product
from math import prod
import random
import numpy as np
import sympy as sp

CASES = [(2, 2), (2, 3), (3, 4), (2, 2, 3), (2, 3, 3), (2, 3, 4), (3, 3, 3), (4, 5)]


def data(shape, budget=1):
    nverts = prod(shape)
    delta = sum(n*n-1 for n in shape)
    target = Fraction(12*budget, nverts*delta)
    verts = list(product(*(range(1, n+1) for n in shape)))
    idx = {v: i for i, v in enumerate(verts)}
    edges = []
    for vertex in verts:
        for ax, n in enumerate(shape):
            if vertex[ax] < n:
                nxt = list(vertex)
                nxt[ax] += 1
                nxt = tuple(nxt)
                rate = target * vertex[ax] * (n - vertex[ax]) / 2
                edges.append((idx[vertex], idx[nxt], rate, ax))
    return verts, edges, target


def gram_laplacian(count, edges, values=None):
    out = sp.zeros(count)
    for k, (i, j, w, _) in enumerate(edges):
        w = w if values is None else values[k]
        out[i, i] += w
        out[j, j] += w
        out[i, j] -= w
        out[j, i] -= w
    return out


def expected_spectrum(shape, t):
    return sorted([t * sum(k*(k+1) for k in ks)/2 for ks in product(*(range(n) for n in shape))])


def main():
    symbolic_count = 0
    eigenmode_count = 0
    alternatives = 0
    full_spectrum_count = 0
    rng = random.Random(681024)
    for shape in CASES:
        vertices, edges, lam = data(shape)
        n = len(vertices)
        L = gram_laplacian(n, edges)
        assert sum([w for i,j,w,k in edges]) == 1
        for ax, size in enumerate(shape):
            coordinate = sp.Matrix([v[ax] - sp.Rational(size+1,2) for v in vertices])
            assert L*coordinate == sp.Rational(lam.numerator,lam.denominator)*coordinate
            eigenmode_count += 1
        # Exact characteristic polynomial identity for small cases.
        if n <= 12:
            z = sp.Symbol('z')
            characteristic = L.charpoly(z).as_expr()
            exact = sp.prod(z-sp.Rational(v.numerator,v.denominator) for v in expected_spectrum(shape,lam))
            assert sp.expand(characteristic-exact) == 0
            full_spectrum_count += 1
        else:
            ev = np.linalg.eigvalsh(np.array(L, dtype=float))
            expvals = sorted(float(v) for v in expected_spectrum(shape,lam))
            assert np.max(np.abs(ev - expvals)) < 3e-12
            full_spectrum_count += 1
        symbolic_count += 1
        optimal = float(lam)
        for trial in range(180):
            rv=[rng.expovariate(1) for e in edges]
            total=sum(rv); rv=[q/total for q in rv]
            candidate=np.zeros((n,n))
            for (i,j,_,_), w in zip(edges,rv):
                candidate[i,i]+=w; candidate[j,j]+=w
                candidate[i,j]-=w; candidate[j,i]-=w
            gap=np.linalg.eigvalsh(candidate)[1]
            assert gap <= optimal + 2e-11, (shape,trial,gap,optimal)
            alternatives += 1
        # Coordinate-cut Rayleigh formula, using all optimal rates.
        for ax, size in enumerate(shape):
            target_sum = lam*n*(size*size-1)/12
            actual=sum(w for i,j,w,k in edges if k==ax)
            assert actual==target_sum
    # Cartesian tensorization check for K_3 square P_4: alpha(K3)=1, alpha(P4)=1/5.
    # The allocation is an instance of the general product formula.
    B=sp.Rational(1)
    alphaK=sp.Rational(1)
    alphaP=sp.Rational(1,5)
    expected=B/(4/alphaK+3/alphaP)
    assert expected==sp.Rational(1,19)
    LK=sp.Matrix([[sp.Rational(2,3),sp.Rational(-1,3),sp.Rational(-1,3)],
                  [sp.Rational(-1,3),sp.Rational(2,3),sp.Rational(-1,3)],
                  [sp.Rational(-1,3),sp.Rational(-1,3),sp.Rational(2,3)]])
    Lp=sp.zeros(4)
    for i in range(1,4):
        w=sp.Rational(i*(4-i),2)
        Lp[i-1,i-1]+=w;Lp[i,i]+=w
        Lp[i-1,i]-=w;Lp[i,i-1]-=w
    # LK and Lp have gap one; rescale both by the predicted product gap.
    prodL=sp.kronecker_product(expected*LK,sp.eye(4))+sp.kronecker_product(sp.eye(3),expected*Lp)
    eigenvalues=sorted(v for x,m in prodL.eigenvals().items() for v in [x]*m)
    assert eigenvalues[0] == 0 and eigenvalues[1] == expected
    # 4 fibers of K3 cost 4*expected, 3 fibers of P4 cost 3*5*expected.
    assert 4*expected+3*5*expected == B
    print('exact_grid_budget_and_coordinate_checks:',symbolic_count,'shapes;',eigenmode_count,'coordinate eigenvectors')
    print('exact_or_numerical_full_spectrum_checks:',full_spectrum_count)
    print('random_asymmetric_competitors_checked:',alternatives)
    print('general_tensor_example: K3 x P4, optimum 1/19, exact eigenvalue and budget verified')
    print('RESULT: PASS')

if __name__ == '__main__':
    main()
