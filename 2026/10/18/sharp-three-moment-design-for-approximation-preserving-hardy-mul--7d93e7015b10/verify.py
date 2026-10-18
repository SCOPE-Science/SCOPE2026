"""Reproduce algebraic and numerical checks for the three-free-moment extremizers.

Requires Python 3, sympy and numpy. The analytical all-degree proof appears in RESULT.md;
this verifier is an independent finite numerical consistency check.
"""
import math
import cmath
import sympy as sp
import numpy as np

r = (sp.sqrt(7) - 1) / 3
constant = (7 + 14 * sp.sqrt(7)) / 27
assert sp.simplify(3*r*r + 2*r - 2) == 0
assert sp.simplify(1 + 2*r - r*r - r**3 - constant) == 0
assert sp.simplify((1-r*r) + r*(1-r*r) + r - constant) == 0

r_float = float(r)
maximum_moment_error = 0.0
maximum_radial_error = 0.0
minimum_weight = 1.0
cases = 0
for n in range(2, 13):
    for j in range(9):
        a = r_float * cmath.exp(1j * (0.13*n + 0.27*j))
        u = cmath.exp(1j * (0.19*n - 0.31*j))
        b = (1-r_float*r_float)*u
        c = -(1-r_float*r_float)*a.conjugate()*u*u
        # Roots are precisely the level-one boundary points of
        # z^(n+1)(a+uz)/(1+conjugate(a)uz).
        coeffs = [u, a] + [0]*(n-1) + [-a.conjugate()*u, -1]
        nodes = np.roots(np.asarray(coeffs, dtype=np.complex128))
        weights = np.array([
            1.0/(n+1+(1-r_float*r_float)/abs(a+u*z)**2)
            for z in nodes
        ])
        expected = [1+0j] + [0j]*n + [a, b, c]
        actual = [sum(w*z**(-k) for w,z in zip(weights,nodes))
                  for k in range(n+4)]
        maximum_moment_error = max(maximum_moment_error,
                                   *(abs(v-w) for v,w in zip(actual,expected)))
        maximum_radial_error = max(maximum_radial_error,
                                   *(abs(abs(z)-1) for z in nodes))
        minimum_weight = min(minimum_weight,*weights)
        assert abs(sum(weights)-1) < 2e-10
        assert abs(abs(a)+abs(b)+abs(c)-float(constant)) < 1e-12
        assert all(w > 0 for w in weights)
        cases += 1
assert maximum_moment_error < 2e-9
assert maximum_radial_error < 2e-10
assert minimum_weight > 0
print('symbolic critical equation and algebraic optimum: PASS')
print('boundary root/weight/moment consistency: PASS')
print('number of evaluated phase/order combinations:', cases)
print('max moment residual: %.3e' % maximum_moment_error)
print('max unit-circle radial residual: %.3e' % maximum_radial_error)
print('minimum positive quadrature weight: %.5f' % minimum_weight)
print('optimal value: %.12f' % float(constant))
