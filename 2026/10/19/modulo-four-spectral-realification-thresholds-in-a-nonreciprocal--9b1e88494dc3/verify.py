"""Finite symbolic and numerical checks for a nonreciprocal impurity ring theorem.

Run: python verify.py  (requires numpy, scipy, sympy).
These checks are illustrative and do not establish an asymptotic theorem.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar


def ring(n, right, left, v):
    h = np.zeros((n, n), dtype=float)
    for k in range(n):
        h[(k + 1) % n, k] += right
        h[k, (k + 1) % n] += left
    h[0, 0] += v
    return h


def central_lobe_threshold(n, g):
    c = math.cosh(n*g)
    minima = []
    for j in range((n - 1)//2):
        lo = (2*j+1)*math.pi/n
        hi = (2*j+2)*math.pi/n
        def f(theta):
            return 2*(c - math.cos(n*theta))*math.sin(theta)/(-math.sin(n*theta))
        sol = minimize_scalar(f, bounds=(lo+1e-9, hi-1e-9),
                              method='bounded', options={'xatol':1e-13})
        assert sol.success
        minima.append(sol.fun)
    return max(minima)


def check_determinants():
    x, v = sp.symbols('x v')
    # A rational nonreciprocity point: t_R=2, t_L=1/2.
    right, left = sp.Integer(2), sp.Rational(1, 2)
    for n in range(3, 9):
        h = sp.zeros(n)
        for k in range(n):
            h[(k+1) % n, k] += right
            h[k, (k+1) % n] += left
        h[0,0] += v
        lhs = h.charpoly(x).as_expr()
        c = (sp.Integer(2)**n + sp.Rational(1,2)**n)/2
        rhs = 2*(sp.chebyshevt(n, x/2)-c) - v*sp.chebyshevu(n-1,x/2)
        assert sp.expand(lhs-rhs) == 0, n
    print('Exact characteristic identities: six dimensions, N=3,...,8: PASS')


def check_lobes_and_eigenvalues():
    cases = 0
    for n in range(3, 11):
        for g in (0.45, 0.75, 1.0):
            vc = central_lobe_threshold(n, g)
            minus = np.linalg.eigvals(ring(n, math.exp(g), math.exp(-g), .99*vc))
            plus = np.linalg.eigvals(ring(n, math.exp(g), math.exp(-g), 1.01*vc))
            assert max(abs(z.imag) for z in minus) > 1e-6, (n,g,'below')
            assert max(abs(z.imag) for z in plus) < 2e-6, (n,g,'above')
            cases += 1
    print(f'Crossings from complex to real: {cases} parameter configurations: PASS')


def check_prefactors():
    x = sp.symbols('x', real=True)
    # N=4 and N=5 are exactly computable central-lobe extrema.
    U3=sp.chebyshevu(3,x)
    U4=sp.chebyshevu(4,x)
    m4=abs(U3.subs(x,1/sp.sqrt(6)))
    m5=abs(U4.subs(x,sp.sqrt(sp.Rational(3,8))))
    assert sp.simplify(1/m4-3*sp.sqrt(6)/8)==0
    assert sp.simplify(1/m5-sp.Rational(4,5))==0
    for n in (3,7,11,15):
        assert sp.chebyshevu(n-1,0) == -1
    print('Exact central-lobe prefactors and residue check: PASS')


def check_sharp_correction():
    for n in (3,7,11):
        for g in (0.7,1.0):
            c=math.cosh(n*g)
            if c < 10: continue
            vc=central_lobe_threshold(n,g)
            approx=2*c - n*n/((n*n-1)*c)
            # A fixed-dimensional O(c^-3) prediction, not infinite validation.
            assert abs(vc-approx) < 5/c**3 + 5e-8, (n,g,vc,approx)
    print('Residue-three strong-asymmetry correction: PASS')

if __name__ == '__main__':
    check_determinants()
    check_lobes_and_eigenvalues()
    check_prefactors()
    check_sharp_correction()
