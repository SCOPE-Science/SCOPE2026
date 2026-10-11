#!/usr/bin/env python3
"""Exact symbolic checks for a four-dimensional polynomial vector field.

This file checks algebraic identities; it is not a substitute for the
analytic invariance, LaSalle, and Wirtinger arguments in the proof.
"""
import sympy as sp
x, y, z, w, a, b = sp.symbols('x y z w a b', real=True)
state = (x, y, z, w)
field = (y, z, w*(y-a*z), b*x*z-y**2+z**2)
phi = w-b*x*y
Lie = sp.factor(sum(sp.diff(phi, v)*f for v,f in zip(state,field)))
assert sp.simplify(Lie - (z**2-(b+1)*y**2)) == 0
assert sp.simplify(Lie.subs(b,-1)-z**2) == 0
assert sp.simplify(Lie.subs(b,-2)-(z**2+y**2)) == 0
assert all(sp.simplify(f.subs({y:0,z:0}))==0 for f in field)
# If z=0, y is nonzero and z'=0 on a whole interval,
# then w=0 and w'=-y**2 !=0, so that interval cannot persist.
assert sp.simplify(field[2].subs(z,0)-w*y)==0
assert sp.simplify(field[3].subs(z,0)+y**2)==0
# At a nonzero sinusoidal y extremum: z=0, w'=-y**2, so
# w cannot be the constant -omega**2 forced by a=0, y''=-omega**2*y.
print('PASS: exact Lie derivative, equilibrium plane, endpoint and extremal identities')
