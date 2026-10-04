#!/usr/bin/env python3
import sympy as sp

z, s, r = sp.symbols("z s r")
i = sp.I

Rp = (1 + z) / (1 - z)
Tp = (1 - i*z) / (1 + i*z)
Fp = sp.factor(s*Rp + (1-s)*Tp)

expected = (
    1 + (2*s-1)*(1+i)*z + i*z**2
) / ((1-z)*(1+i*z))
assert sp.simplify(Fp - expected) == 0

c, q = sp.symbols("c q", real=True)
sroot = (1-c+q) / 2

# Boundary-root relation, after clearing positive half-angle denominators.
root_cleared = sp.expand(
    sroot*c*(1+c) - (1-sroot)*q*(1+q)
)
assert sp.factor(root_cleared) == (q-c)*(c**2+q**2-1)/2

D1 = 1 - 2*r*c + r**2
D2 = 1 - 2*r*q + r**2
cross = sp.expand(
    sroot*q*D2 - (1-sroot)*c*D1
)
target = (q-c)*(1+c+q)*(1-r)**2/2

# The difference is a multiple of the unit-circle relation.
diff = sp.factor(cross-target)
assert sp.simplify(diff - r*(c-q)*(c**2+q**2-1)) == 0

# The weight imbalance agrees with the trigonometric imbalance.
assert sp.simplify((2*sroot-1) - (q-c)) == 0

print("VERIFY_OK")
print("derivative rational identity: exact")
print("boundary-root identity: exact modulo c^2+q^2=1")
print("radial sign factorization: exact modulo c^2+q^2=1")
