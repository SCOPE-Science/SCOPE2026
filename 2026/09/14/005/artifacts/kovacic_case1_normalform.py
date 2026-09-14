"""Kovacic Case-1 normal-form certificate for H(2,q), symmetric half exponents.

Verifies with exact rational arithmetic:
 1. normalized invariant s = p'/2 + p^2/4 - r, numerator/denominator;
 2. pole locations/orders uniform in q (no cancellation, no degree drop);
 3. double-pole coefficients b_c (q-independent) and alpha sets;
 4. enumeration of all 27 sign combinations: every d < 0.
Run: python3 kovacic_case1_normalform.py
"""
import itertools
import sympy as sp

z, q, w = sp.symbols('z q w')

p = sp.Rational(1, 2) * (1/z + 1/(z - 1) + 1/(z - 2))
r = ((sp.Rational(1, 16)) * z - q) / (z * (z - 1) * (z - 2))
s = sp.together(sp.diff(p, z) / 2 + p**2 / 4 - r)
num, den = sp.fraction(s)
num = sp.expand(num)
den = sp.expand(den)
print("s numerator N(q,z) =", num)
print("s denominator      =", den)
print("den factored       =", sp.factor(den))
assert den == 16*z**6 - 96*z**5 + 208*z**4 - 192*z**3 + 64*z**2

# q-part of numerator
Nq = sp.expand(16*q*z**3 - 48*q*z**2 + 32*q*z)
N0 = sp.expand(num - Nq)
print("q-free part N0 =", N0)
for c in [0, 1, 2]:
    assert sp.expand(Nq).subs(z, c) == 0, f"q-part must vanish at {c}"
    val = sp.expand(num).subs(z, c)
    print(f"N(q,{c}) = {val} (q-independent, nonzero)")
    assert val != 0
# leading coefficient q-free and nonzero -> deg_z N = 4 for every q
assert sp.Poly(num, z).degree() == 4
assert sp.Poly(num, z).LC() == -4
# pole orders at 0,1,2 are exactly 2 for every q
for c in [0, 1, 2]:
    b = sp.simplify((z - c)**2 * s).subs(z, c)
    print(f"b_{c} = {b}")
    assert b == sp.Rational(-3, 16)
# order at infinity: deg den - deg num = 2 for every q
assert 6 - 4 == 2
sw = sp.simplify(s.subs(z, 1/w))
b_inf = sp.simplify(sw / w**2).subs(w, 0)  # lim z^2 s(z) = lim s(1/w)/w^2
print("b_inf =", b_inf)
assert b_inf == sp.Rational(-1, 4)

# alpha sets
alphas_fin = (sp.Rational(3, 4), sp.Rational(1, 4))
alphas_inf = (sp.Rational(1, 2),)
print("alpha_fin =", alphas_fin, " alpha_inf =", alphas_inf)

# enumerate all combos: at infinity alpha_inf is a singleton {1/2}
# (double root), so there are 2^3 = 8 combos, not 27.
bad = 0
vals = set()
for combo in itertools.product(alphas_fin, repeat=3):
    d = alphas_inf[0] - sum(combo)
    vals.add(d)
    assert d < 0, combo
    assert d not in (0, 1, 2, 3)
    bad += 1
print(f"checked {bad} combos; distinct d values = {sorted(vals)}")
print("ALL d < 0: Kovacic Case-1 admits no candidate degree for any q.")
print("CERTIFICATE OK")
