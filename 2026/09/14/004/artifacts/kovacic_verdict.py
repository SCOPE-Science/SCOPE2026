"""Exact rational verification of Kovacic Cases 1-3 for target Heun operator.
Heun: t=-1, gamma=delta=epsilon=2/3, alpha=1/3, beta=2/3, q=0.
Normalized form xi'' = r xi with r = P^2/4 + P'/2 - Q.
Checks pole orders, b-coefficients, exponent differences, E-sets, and degree bounds.
All arithmetic exact (sympy Rational)."""
import sympy as sp
z = sp.Symbol('z')
P = sp.Rational(2,3)*(1/z + 1/(z-1) + 1/(z+1))
Q = sp.Rational(2,9)/(z**2-1)
r = sp.simplify(P**2/4 + sp.diff(P,z)/2 - Q)
rclaim = sp.Rational(-2,9)*(z**2+1)**2/(z**2*(z**2-1)**2)
assert sp.simplify(r - rclaim) == 0, "r mismatch"
print("r =", rclaim)
for c in [0, 1, -1]:
    assert sp.simplify((z-c)**3 * rclaim).limit(z, c) is not None
    # order exactly 2: (z-c)^2 r -> nonzero finite, (z-c)^3 r -> 0
    b = sp.limit((z-c)**2 * rclaim, z, c)
    assert sp.limit((z-c)**3 * rclaim, z, c) == 0
    print(f"c={c}: b={b}, 1+4b={1+4*b}, sqrt={sp.sqrt(1+4*b)}")
    assert b == sp.Rational(-2,9)
# infinity order
assert sp.limit(z**2 * rclaim, z, sp.oo) == sp.Rational(-2,9)
assert sp.Poly(sp.together(rclaim).as_numer_denom()[1], z).degree() - sp.Poly(sp.together(rclaim).as_numer_denom()[0], z).degree() == 2
print("binf=-2/9, ord_inf=2")
# Case 1: alphas {1/3,2/3}; max d = 2/3-3*(1/3) = -1/3 <0
from itertools import product
vals=[sp.Rational(1,3), sp.Rational(2,3)]
ok1=[(ai,a0,a1,am1) for ai in vals for a0 in vals for a1 in vals for am1 in vals
     if (ai-a0-a1-am1) >= 0 and (ai-a0-a1-am1).q==1 and False]
ds1={ai-a0-a1-am1 for ai in vals for a0 in vals for a1 in vals for am1 in vals}
print("Case1 max d:", max(ds1), "-> all negative:", all(d<0 for d in ds1))
assert all(d < 0 for d in ds1)
# Case 2: E={2} everywhere since 2+-2/3 not integers; d=(2-6)/2=-2
E2={2}
d2=(2-2-2-2)/2
print("Case2 only tuple d:", d2); assert d2<0
# Case 3: E subsets of {4..8}, min 4: e_inf - sum <= 8-12 = -4 <0 for all n
for n,E in [(4,{4,5,6,7,8}),(6,{4,6,8}),(12,{4,5,6,7,8})]:
    worst = max(E)-3*min(E)
    print(f"n={n}: max(e_inf-sum)={worst}, max d={(sp.Rational(n,12)*worst)} <0")
    assert worst < 0
print("ALL CASES FAIL -> Galois group SL(2,C).")
