#!/usr/bin/env python3
"""Exact polynomial checks for a characteristic-three cubic discriminant.

Dependencies: Python 3, sympy. No network access, external data, or hidden files.
This checker corroborates algebraic equalities; the accompanying proof establishes
normalization and the conductor by ring/module arguments.
"""
import sympy as s

a,b,c,L = s.symbols('a b c ell')
P = lambda expr,*gens: s.Poly(s.expand(expr),*gens,modulus=3)
Delta=a*a*b*b-b**3-a**3*c
assert P(Delta.subs({b:-a*L,c:L**3+a*L**2}),a,L).is_zero
for var,expect in [(a,-a*b*b),(b,-a*a*b),(c,-a**3)]:
    assert P(s.diff(Delta,var)-expect,a,b,c).is_zero

# The monic relation is ell^3+a ell^2-c. It makes B free over k[a,c].
rel=L**3+a*L**2-c
red=lambda expr:s.rem(s.expand(expr),rel,L).expand()
assert P(red(L**3)-(c-a*L**2),a,c,L).is_zero

# R-module basis of A in B: 1, a*ell, a^2*ell^2.
# b=-a ell, and multiplying each basis vector by b stays in its span.
products=[red((-a*L)*v) for v in (1,a*L,a**2*L**2)]
expected=[-a*L,-a**2*L**2,-a**3*c+a**4*L**2]
assert all(P(x-y,a,c,L).is_zero for x,y in zip(products,expected))

# Conductor generators a^2, a*b, b^2 become a^2, -a^2 ell, a^2 ell^2.
# Their products with ell and ell^2 lie in A; the proof gives necessity.
for gen in (a*a,-a*a*L,a*a*L*L):
    for j in (1,2):
        z=red(gen*L**j)
        # Extract coefficients in the R-basis; A-membership requires
        # divisibility by a^i in the coefficient of ell^i.
        q=s.Poly(z,L)
        for i in (1,2):
            coeff=q.nth(i)
            assert s.rem(coeff,a**i,a)==0, (gen,j,coeff,i)

# b^3 lies in J mod Delta, proving the entire (a,b)^3 ideal.
assert P(b**3-(a**2*b**2-a**3*c-Delta),a,b,c).is_zero
print('VERIFY_OK: characteristic-three cubic discriminant identities and module basis')
