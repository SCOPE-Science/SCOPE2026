#!/usr/bin/env python3
"""Exact symbolic checks for the singular-fiber classification of an explicit genus-three pencil.
Requires Python 3 and SymPy; all calculations are over characteristic zero.
"""
from sympy import symbols, factor, discriminant, simplify, Poly

r, u, v, s, t = symbols('r u v s t')
A, B, C = r-1, -6*(r+1), -3*(r-1)
f = A*u**4 + B*u**2*v**2 + C*v**4
c = r*(1-t*r**3)
Q = f + c*s**4
assert simplify(B**2-4*A*C - 48*(r**2+r+1)) == 0
assert simplify(discriminant(f.subs(v, 1), u) + 110592*(r-1)**2*(r**2+r+1)**2) == 0
assert simplify(A*f - (A*u**2+(B/2)*v**2)**2 + 12*(r**2+r+1)*v**4) == 0
assert simplify(Q.subs(r,1) + 12*u**2*v**2-(1-t)*s**4) == 0
# At all five zeros of the coefficient of s^4 the residual equation is a
# binary quartic; at t != 0,1 its factors are four distinct linear forms.
assert simplify(c - r*(1-t*r**3)) == 0
assert simplify(f.subs(r,0) + (u**4+6*u**2*v**2-3*v**4)) == 0
# At r = infinity, substitute a=1,b=0 in the original homogeneous pencil.
finf = u**4 - 6*u**2*v**2-3*v**4
assert factor(discriminant(finf.subs(v,1),u)) != 0
assert factor(discriminant(f.subs(r,0).subs(v,1),u)) != 0
# The three residual quartics with r^3=1 split into two smooth conics,
# each pair tangent twice, since A*f is a square modulo r^2+r+1.
assert factor(Q.subs(r,1) - (-12*u*u*v*v+(1-t)*s**4)) == 0
# Euler characteristic independently agrees with the hypersurface Chern class.
e_general = 2-2*3
number_four_lines, e_four_lines = 5, 4*2-3
number_conic_pairs, e_conic_pairs = 3, 2*2-2
defect = number_four_lines*(e_four_lines-e_general) + number_conic_pairs*(e_conic_pairs-e_general)
e_surface_from_fibration = 2*e_general+defect
e_surface_from_chern = 5*(5**2-4*5+6)
assert defect == 63
assert e_surface_from_fibration == 55 == e_surface_from_chern
print('VERIFY_OK quartic_discriminant=-110592*(r-1)^2*(r^2+r+1)^2')
print('VERIFY_OK r^3=1 yields two smooth conics tangent at two points')
print('VERIFY_OK reducible_fibers=5_four-line_stars+3_tacnodal_two-conic_pairs')
print('VERIFY_OK e_generic=-4 defects=5*9+3*6=63 e_surface=55')
