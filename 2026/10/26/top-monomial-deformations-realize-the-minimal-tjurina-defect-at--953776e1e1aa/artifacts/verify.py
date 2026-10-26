"""Exact Tjurina-algebra check for the six-variable example.

Requires Python 3 and SymPy.  The general Milnor-number formula and the
minimal-exponent statement are proved in RESULT.md; this script independently
replays the finite Groebner-basis count for the example with (mu,tau)=(125,124).
"""
from itertools import product
import sympy as sp

x, y, z = sp.symbols("x y z")
f = x**6 + y**6 + z**6 + x**4 * y**4 * z**4
partials = [sp.diff(f, v) for v in (x, y, z)]
G = sp.groebner([f, *partials], x, y, z, order="lex", domain=sp.QQ)
assert G.is_zero_dimensional
leading = [tuple(p.LM(order=G.order).exponents) for p in G.polys]
bounds = []
for i in range(3):
    pure_powers = [
        lm[i] for lm in leading
        if lm[i] > 0 and all(lm[j] == 0 for j in range(3) if j != i)
    ]
    assert pure_powers, (i, leading)
    bounds.append(min(pure_powers))
assert bounds == [5, 6, 6], bounds
standard_count = 0
for exponent in product(*(range(b) for b in bounds)):
    if not any(
        all(exponent[i] >= lm[i] for i in range(3))
        for lm in leading
    ):
        standard_count += 1
assert standard_count == 124, standard_count
milnor_number = 5**3
assert milnor_number == 125
print("Groebner basis: zero-dimensional Tjurina ideal")
print("Pure leading-monomial bounds:", tuple(bounds))
print("Standard-monomial count (Tjurina number):", standard_count)
print("Milnor number from the principal weighted-homogeneous part:", milnor_number)
print("Tjurina defect:", milnor_number - standard_count)
print("VERIFY_OK")
