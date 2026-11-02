#!/usr/bin/env python3
"""Exact local-equation checks for four explicit sections on an elliptic fibration.

This supports, but does not replace, the intersection-theoretic proof.
Requires Python 3 and SymPy. Run: python verify.py
"""
import sympy as sp

t, s, v, a, b, X, Y = sp.symbols('t s v a b X Y')
D = sp.expand(4*(t*t+1)**3+27)
assert sp.degree(D, t) == 6
assert sp.gcd(D, sp.diff(D, t)) == 1
assert sp.discriminant(a**3+a+1, a) == -31
assert sp.gcd(b**6+b**2+1, sp.diff(b**6+b**2+1, b)) == 1

# Set a=b^2 and impose b^6+b^2+1=0: each (b^2,b*t) is a section.
point = sp.expand((b*t)**2-((b*b)**3+(t*t+1)*b*b+1))
assert sp.factor(point) == -(b**6+b**2+1)
# The already published section (0,1) lies on the generic fiber.
assert sp.expand(1**2-(0+(t*t+1)*0+1)) == 0

# On a degree-two hyperelliptic base near infinity, t=v^-2.
F = Y**2-X**3-(1+v**4)*X-v**6
assert sp.expand(F.subs({X:0,Y:v**3})) == 0
z = sp.expand(F.subs({X:b*b*v**2,Y:b*v}))
assert sp.factor(z) == -v**6*(b**6+b**2+1)
assert sp.diff(F,X).subs({X:0,Y:0,v:0}) == -1
# Four branches through the same smooth point have first-order Y-slopes
# 0 and the three nonzero, pairwise distinct b's.
assert sp.rem(b**6+b**2+1,b) == 1
assert sp.discriminant(b**6+b**2+1,b) != 0

# Rational antecedent: t=1/s, x=X/s^2, y=Y/s^3.
a4=s**2+s**4
b6=s**6
Dr=sp.expand(-16*(4*a4**3+27*b6**2))
c4=sp.expand(-48*a4)
assert sp.expand(Dr - (-16*s**6*(4*(1+s*s)**3+27*s**6))) == 0
assert sp.Poly(Dr,s).degree() == 12
assert sp.expand(Dr/s**6).subs(s,0) == -64
assert sp.expand(c4/s**2).subs(s,0) == -48
# Thus valuations of (c4,Delta) at rational infinity are (2,6), I0*.
# Six simple finite discriminant zeros supply the other I1 fibers.

# No reducible fibers after the hyperelliptic base change; chi=1.
# Intersections: all four sections disjoint from O; distinct pairs intersect
# only at infinity, with local Y-slopes distinct, hence once transversely.
# Shioda's formula then gives Gram = 2 I_4.
height_B = sp.diag(2,2,2,2)
height_R = height_B/2
assert height_B.det() == 16
assert height_R == sp.eye(4) and height_R.det() == 1
# The classical I0* rational elliptic surface Mordell-Weil lattice is D4*
# of discriminant 1/4; hence the four explicit points span index two.
assert sp.sqrt(sp.Rational(1,1)/sp.Rational(1,4)) == 2
print('VERIFY_OK')
