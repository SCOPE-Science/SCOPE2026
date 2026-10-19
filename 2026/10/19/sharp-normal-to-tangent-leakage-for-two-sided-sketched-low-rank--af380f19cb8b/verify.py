"""Exact-rational checks for the sharp two-sided oblique-tangent leakage theorem.

Standalone: Python 3 standard library only. All tests are finite corroborations.
"""
from fractions import Fraction as F


def witness(e, s):
    """Gram matrix with spectrum exactly [1-e,1+e], s=sqrt(1-e^2)."""
    assert s * s == 1 - e * e
    a, b, c = 1 - e * e, e * s, 1 + e * e
    assert a > 0 and a + c == 2 and a * c - b * b == 1 - e * e
    # e is therefore the positive half-eigenvalue gap of this symmetric 2x2 Gram matrix.
    t = b / a
    assert t * t == e * e / (1 - e * e)
    return t


def normal_leak_square(x, y):
    # The exact oblique image of E_22 has entries [-xy,x;y,0].
    return (x * y) ** 2 + x ** 2 + y ** 2


witnesses = [(F(3, 5), F(4, 5)), (F(3, 5), F(3, 5)),
             (F(5, 13), F(12, 13)), (F(0), F(4, 5))]
root = {F(0): F(1), F(3, 5): F(4, 5), F(4, 5): F(3, 5),
        F(5, 13): F(12, 13), F(12, 13): F(5, 13)}
for el, er in witnesses:
    x, y = witness(el, root[el]), witness(er, root[er])
    bound2 = 1 / ((1 - el * el) * (1 - er * er)) - 1
    assert normal_leak_square(x, y) == bound2
assert normal_leak_square(F(3, 4), F(4, 3)) == F(481, 144)
assert normal_leak_square(F(3, 4), F(3, 4)) == F(369, 256)

# Rational circle parametrization: for t rational, (cos,sin)=((1-t^2)/(1+t^2),2t/(1+t^2)).
# The matrix I+e[[cos,sin],[sin,-cos]] has eigenvalues 1+-e.
grid_count = 0
for e in [F(1, 5), F(3, 5), F(4, 5), F(12, 13)]:
    for d in range(1, 26):
        for p in range(-25, 26):
            t = F(p, d)
            co, si = (1 - t*t)/(1 + t*t), 2*t/(1 + t*t)
            a, b = 1 + e*co, e*si
            assert a > 0
            # Exact finite-rational test of the optimal one-sided bound.
            assert b*b*(1-e*e) <= e*e*a*a
            grid_count += 1
print(f"VERIFY_OK exact_rational_witnesses={len(witnesses)} one_sided_grid={grid_count} sharp_pairs=2")
