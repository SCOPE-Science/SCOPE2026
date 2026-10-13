#!/usr/bin/env python3
import sympy as sp

s = sp.symbols("s", real=True)
kappa = sp.symbols("kappa", positive=True)

# Shifted-gamma member: tau=1, rate a=1, shape b=2.
beta = (s-1)*sp.exp(-(s-1))

# At t=3 and alpha=1, g(t)=t.
printed_over_kappa = sp.simplify(3 * sp.integrate(beta, (s,1,3)))
target_over_kappa = sp.simplify(sp.integrate((3-s)*beta, (s,1,3)))
gap = sp.simplify(printed_over_kappa-target_over_kappa)
first_moment = sp.simplify(sp.integrate(s*beta, (s,1,3)))

assert printed_over_kappa == 3 - 9*sp.exp(-2)
assert target_over_kappa == 4*sp.exp(-2)
assert gap == 3 - 13*sp.exp(-2)
assert sp.simplify(gap-first_moment) == 0

# Prove positivity without relying on floating-point comparison:
# exp(2) > 1 + 2 + 2^2/2 + 2^3/6 = 19/3 > 13/3.
# Hence 3 - 13 exp(-2) > 0.
lower_exp2 = sp.Rational(19,3)
assert lower_exp2 > sp.Rational(13,3)

print("VERIFY_OK")
print("printed_over_kappa", printed_over_kappa)
print("target_over_kappa", target_over_kappa)
print("gap", gap)
print("gap_numeric", sp.N(gap,30))
