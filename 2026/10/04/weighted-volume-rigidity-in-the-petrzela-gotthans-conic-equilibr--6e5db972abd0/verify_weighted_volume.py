#!/usr/bin/env python3
import sympy as sp

x, y, z, a, b, r = sp.symbols('x y z a b r', real=True)
f = sp.Matrix([
    z,
    -z * (a*y + b*x*z),
    x + y**2 - r,
])
vars_ = (x, y, z)
div_f = sp.simplify(sum(sp.diff(f[i], vars_[i]) for i in range(3)))
rho = sp.exp(a*x)
weighted_div = sp.simplify(sum(sp.diff(rho*f[i], vars_[i]) for i in range(3)))
cohomology = sp.simplify(div_f + a*f[0])

assert sp.simplify(div_f + a*z) == 0
assert cohomology == 0
assert weighted_div == 0

print('div(f) =', div_f)
print('div(f) + a*x_dot =', cohomology)
print('div(exp(a*x) f) =', weighted_div)
print('VERIFY_WEIGHTED_VOLUME_OK')
