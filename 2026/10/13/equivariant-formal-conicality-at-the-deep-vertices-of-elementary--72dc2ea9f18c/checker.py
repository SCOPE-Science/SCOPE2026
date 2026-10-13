"""Exact finite consistency checks for symmetric-quartic local models.

The general formal-contact statement is established in the accompanying proof;
finite symbolic tests here do not replace the induction over all degrees.
Requires SymPy.
"""
import itertools
from math import comb
import sympy as sp
from sympy.polys.polyfuncs import symmetrize


def elem(z, k):
    if k == 0:
        return sp.Integer(1)
    if k > len(z):
        return sp.Integer(0)
    return sp.Add(*(sp.prod(c) for c in itertools.combinations(z, k)))


def gradient_numeric(a, d):
    return [sum(sp.prod(a[j] for j in choice)
                for choice in itertools.combinations(
                    [j for j in range(len(a)) if j != i], d - 1))
            for i in range(len(a))]


identity_checks = 0
for m in range(4, 9):
    z = sp.symbols('z0:' + str(m))
    e3 = elem(z, 3)
    for r in range(2, m - 1):
        h = sp.expand(sum(z[i] ** r * sp.diff(e3, z[i])
                          for i in range(m)))
        p, rem, subs = symmetrize(h, z, formal=True)
        assert rem == 0
        symbols = [a for a, _ in subs]
        assert sp.expand(p).coeff(symbols[r + 1]) == (-1) ** (r + 1) * (r + 2)
        assert sp.expand(p).subs({symbols[j]: 0 for j in range(2, m)}) == 0
        assert sp.expand(p).subs({symbols[j]: 0 for j in range(2, r + 1)}) == (
            (-1) ** (r + 1) * (r + 2) * symbols[r + 1])
        identity_checks += 1
print('Newton-triangular identities:', identity_checks, 'PASS')

chart_checks = 0
for m in range(4, 7):
    z = sp.symbols('z0:' + str(m))
    e1, e3, e4 = elem(z, 1), elem(z, 3), elem(z, 4)
    shifted = [zi + zi**2 / 4 for zi in z]
    polynomial = sp.Poly(sp.expand((1 - e1 / 4) *
                                   (elem(shifted, 3) + elem(shifted, 4)) - e3), *z)
    for powers, coeff in polynomial.terms():
        assert sum(powers) >= 5 or coeff == 0
    chart_checks += 1
print('First formal-contact elimination at vertices:', chart_checks, 'PASS')

hessian_checks = 0
for k in range(2, 9):
    z = sp.symbols('z0:' + str(k))
    hess = sp.hessian(elem(z, 2), z)
    assert hess.det() == (-1) ** (k - 1) * (k - 1)
    hessian_checks += 1
print('Transverse quadratic ranks:', hessian_checks, 'PASS')

samples = 0
for n in range(5, 8):
    for a in itertools.product((-1, 0, 1), repeat=n):
        crit = all(g == 0 for g in gradient_numeric(a, 4))
        assert crit == (sum(v != 0 for v in a) <= 2)
        samples += 1
print('Integer critical-locus specializations:', samples, 'PASS')
print('All exact checks completed.')
