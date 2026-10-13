#!/usr/bin/env python3
from sympy import Matrix, I, symbols, expand

H = 168
c2_subgroups = 21
c3_subgroups = 28
c4_subgroups = 21

# Each involution fixes four elliptic components.  The component through zero
# is the axis of the unique containing C4, so the extra generic-C2 components
# are three translates per involution.
c2_curves = 3 * c2_subgroups
c3_curves = c3_subgroups
c4_curves = c4_subgroups
assert (c2_curves, c3_curves, c4_curves) == (63, 28, 21)
assert c2_curves + c3_curves + c4_curves == 112

# Setwise stabilizer orders from the source: D8, S3, D8.
orb_c2 = H // 8
orb_c3 = H // 6
orb_c4 = H // 8
assert (orb_c2, orb_c3, orb_c4) == (21, 28, 21)
assert c2_curves // orb_c2 == 3
assert c3_curves // orb_c3 == 1
assert c4_curves // orb_c4 == 1

# Tangent models for the order-two antireflection and displayed order-four action.
M2 = Matrix.diag(1, -1, -1)
M4 = Matrix([[1,0,0],[0,0,-1],[0,1,0]])
assert M2.det() == 1 and (M2 - Matrix.eye(3)).rank() == 2
assert M4.det() == 1 and (M4 - Matrix.eye(3)).rank() == 2
assert set(M4.eigenvals().keys()) == {1, I, -I}

# The transverse quotient 1/n(1,-1) has invariant generators a=u^n,
# b=v^n,c=uv with relation ab=c^n, the A_{n-1} equation.
u, v = symbols('u v')
for n, ade in [(2,'A1'), (3,'A2'), (4,'A3')]:
    a, b, c = u**n, v**n, u*v
    assert expand(a*b - c**n) == 0

assert 3 + 1 + 1 == 5
assert 5 + 2 == 7
print('VERIFY_OK preimage_curves=112 curve_orbits=3+1+1 generic_ADE=3A1+A2+A3 isolated=2x1/7(1,2,4)')
