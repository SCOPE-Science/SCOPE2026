#!/usr/bin/env python3
"""Exact finite regression tests for all-order Legendre bootstrap diagonal theorem.

Requires SymPy. Numerical/finite checks do not replace the all-order proof.
"""
import sympy as sp

z, E = sp.symbols("z E", real=True)
w = z * (1 - z)
fp = {0: sp.Integer(1), 1: sp.Rational(1, 2)}


def f(m):
    for n in range(2, m + 1):
        if n not in fp:
            fp[n] = sp.factor(-(
                (n - 1)**3 * fp[n - 2]
                + (2*n - 1) * (2*E - n*n + n) * fp[n - 1]
            ) / (n * (n*n - 4*E - 1)))
    return fp[m]


def derivative_as_pair(order):
    """Returns A,B with D^order psi=A psi'+B psi under Legendre ODE."""
    a, b = sp.Integer(0), sp.Integer(1)
    for _ in range(order):
        a, b = (sp.cancel(sp.diff(a, z) + b - a * sp.diff(w, z) / w),
                sp.cancel(sp.diff(b, z) - a * E / w))
    return a, b


def formal_diagonal(j):
    a, b = derivative_as_pair(j)
    a, b = a * w**(2*j), b * w**(2*j)
    for _ in range(j):
        a, b = (sp.cancel(sp.diff(a, z) + b - a * sp.diff(w, z) / w),
                sp.cancel(sp.diff(b, z) - a * E / w))
    # S^j w^(2j) S^j = (-1)^j D^j w^(2j) D^j.
    p = sp.factor((-1)**j * (b - sp.diff(a, z) / 2))
    polynomial = sp.Poly(p, z)
    return sp.factor(sum(c * f(deg[0]) for deg, c in polynomial.terms()))


def product(j):
    return sp.factor(
        sp.binomial(2*j, j) / 4**j
        * sp.prod((E - k*(k+1))**2 for k in range(j))
        / sp.prod(4*E-(4*m*m-1) for m in range(1, j+1))
    )


def physical_norm(j, n):
    psi = sp.sqrt(2*n+1) * sp.legendre(n, 2*z-1)
    return sp.integrate(sp.expand(w**(2*j) * sp.diff(psi, z, j)**2), (z, 0, 1))


def run():
    count = 0
    for j in range(1, 7):
        actual = formal_diagonal(j)
        expect = product(j)
        assert sp.cancel(actual-expect) == 0, ("symbolic diagonal", j, actual, expect)
        count += 1
        print("symbolic product", j, "OK")
    assert sp.cancel(formal_diagonal(1) - E**2 / (2*(4*E-3))) == 0
    assert sp.cancel(formal_diagonal(2) - 3*E**2*(E-2)**2 / (8*(4*E-3)*(4*E-15))) == 0
    count += 2
    for n in range(8):
        for j in range(5):
            rhs = sp.Integer(1) if j == 0 else product(j).subs(E, n*(n+1))
            lhs = physical_norm(j, n)
            assert sp.simplify(lhs-rhs) == 0, ("Legendre norm", j, n, lhs, rhs)
            count += 1
    for j in range(1, 7):
        left = sp.Rational((j-1)**2) - sp.Rational(1,4)
        right = sp.Rational(j*j) - sp.Rational(1,4)
        mid = (left + right) / 2
        if mid == j*(j-1):
            mid = (2*left + right) / 3
        assert product(j).subs(E, mid) < 0, ("negative diagonal", j)
        count += 1
    print("PASS: %d exact regression assertions; no infinite claim based on finite tests" % count)


if __name__ == '__main__':
    run()
