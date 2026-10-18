#!/usr/bin/env python3
"""Exact finite cross-checks for the cubic Laguerre specialization.

The infinite assertions are proved in RESULT.md; these tests are not a
substitute for the integer-divisibility argument there.
"""
from math import isqrt
import sympy as sp

X, a = sp.symbols('X a')
A = a + 3
P = X**3 - 3*A*X**2 + 3*A*(A-1)*X - A*(A-1)*(A-2)
Y = sp.symbols('Y')
assert sp.expand(P.subs(X, Y+A) - (Y**3 - 3*A*Y - 2*A)) == 0
assert sp.simplify(sp.discriminant(P, X) - 108*(a+2)*(a+3)**2) == 0
assert sp.simplify(-6*sp.assoc_laguerre(3,a,X)-P) == 0

finite = 0
for parameter in range(513):
    f = sp.Poly(P.subs(a, parameter), X)
    assert f.is_irreducible
    delta = int(f.discriminant())
    square = isqrt(delta)**2 == delta
    expected = ((parameter+2)%3 == 0 and
                isqrt((parameter+2)//3)**2 == (parameter+2)//3)
    assert square == expected
    finite += 1

exceptional = []
for k in range(1, 61):
    parameter = 3*k*k - 2
    f = sp.Poly(P.subs(a, parameter), X)
    delta = int(f.discriminant())
    assert isqrt(delta)**2 == delta
    assert f.is_irreducible
    exceptional.append(parameter)

assert len(exceptional) == 60 and exceptional[0] == 1
print('SYMBOLIC_SHIFT_AND_DISCRIMINANT_OK')
print('SYMBOLIC_LAGUERRE_NORMALIZATION_OK')
print(f'EXACT_IRREDUCIBILITY_AND_DISCRIMINANT_INSTANCES_OK: {finite}')
print(f'CYCLIC_SUBFAMILY_INSTANCES_OK: {len(exceptional)}')
print('FINITE_CHECKS_COMPLETE; INFINITE_PROOF_IS_THE_DIVISIBILITY_ARGUMENT')
