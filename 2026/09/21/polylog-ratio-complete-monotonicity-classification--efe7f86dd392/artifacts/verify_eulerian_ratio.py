#!/usr/bin/env python3
"""Exact and numerical checks for the Eulerian-ratio classification."""

import sympy as sp

z = sp.symbols("z", positive=True)


def eulerian_poly(n):
    """Return A_n(z)=sum_k <n,k> z^k using the differential recurrence."""
    if n < 1:
        raise ValueError("n must be positive")
    A = sp.Integer(1)
    for k in range(1, n):
        A = sp.expand((1 + k*z)*A + z*(1-z)*sp.diff(A, z))
    return A


A1, A2, A3, A4 = [eulerian_poly(n) for n in range(1, 5)]
assert A1 == 1
assert A2 == 1 + z
assert A3 == 1 + 4*z + z**2
assert A4 == 1 + 11*z + 11*z**2 + z**3

F1 = sp.cancel(A2 / ((1-z)*A1))
F2 = sp.cancel(A3 / ((1-z)*A2))
F3 = sp.cancel(A4 / ((1-z)*A3))

assert sp.simplify(F1 - (1+z)/(1-z)) == 0
assert sp.simplify(F2 - (1+4*z+z**2)/(1-z**2)) == 0

# The i=2 power-series coefficients are 1,4,2,4,2,... .
series_F2 = sp.series(F2, z, 0, 9).removeO().expand()
expected_F2 = 1 + sum((4 if n % 2 else 2)*z**n for n in range(1, 9))
assert sp.expand(series_F2 - expected_F2) == 0

# First inner Eulerian root and non-cancellation in the next numerator.
rho3 = -2 + sp.sqrt(3)
assert sp.simplify(A3.subs(z, rho3)) == 0
assert sp.simplify(A4.subs(z, rho3)) != 0
assert -1 < float(rho3) < 0

# For h(t)=R(e^{-t}), (-1)^m h^(m)(t)=(z d/dz)^m R(z).
D = F3
for _ in range(10):
    D = sp.cancel(z * sp.diff(D, z))
witness = sp.cancel(D.subs(z, sp.Rational(1, 500)))
assert witness < 0

print("F3^(10)(log 500) =", witness)
print("decimal =", sp.N(witness, 20))
print("first right-half-plane pole has real part =", sp.N(sp.log(2+sp.sqrt(3)), 20))

# Numerical sanity check of the structural root statement for small indices.
for n in range(3, 11):
    A = eulerian_poly(n)
    roots = [complex(r) for r in sp.nroots(A, n=30, maxsteps=100)]
    inner = [r.real for r in roots if abs(r.imag) < 1e-20 and -1 < r.real < 0]
    assert inner, (n, roots)
    # Palindromicity.
    assert sp.expand(A - z**(n-1)*A.subs(z, 1/z)) == 0

print("representative Eulerian-root checks passed for n=3,...,10")
