#!/usr/bin/env python3
"""Reproduce exact Hessian and discriminant identities for cyclic-six quartic flexes.

Requires Python 3 and SymPy. All equalities are in polynomial rings over QQ;
this script uses no sampled parameter values or numerical tolerances.
"""
import sympy as S

x, y, z, r, t = S.symbols('x y z r t')
F = x**3*z + y**4 + r*y**2*z**2 + z**4
H = S.expand(S.hessian(F, (x,y,z)).det())
B = (4*r**2*y**2*z**3 + r*x**3*z**2 - 8*r*y**4*z
     -8*r*z**5 + 6*x**3*y**2 -48*y**2*z**3)
assert S.expand(H + 18*x*B) == 0
P = 2*t**3 + 5*r*t**2 + (18-r**2)*t + 3*r
g = t**2 + r*t + 1
# The curve equation on z=1 is x^3 + g(y^2)=0.
rem = S.rem(H.subs(z,1), x**3+g.subs(t,y**2), x)
assert S.expand(rem - 54*x*P.subs(t,y**2)) == 0
assert S.expand(S.discriminant(P,t) -
    3*(r*r-4)*(11*r**4-1080*r**2+3888)) == 0
assert S.expand(S.resultant(P,g,t) - 16*(r*r-4)**2) == 0
assert S.expand(P.subs(t,0)-3*r) == 0
# At x=0, B modulo g(y^2) is 12*y^2*(r^2-4).
assert S.expand(S.rem(B.subs({z:1,x:0}),g.subs(t,y**2),y)
                -12*y**2*(r**2-4)) == 0
# For P=2(t-a)^3, its t^2 coefficient forces a=-5r/6.
a = -5*r/S.Integer(6)
triple_linear = S.factor((18-r*r)-6*a*a)
triple_constant = S.factor(3*r+2*a**3)
assert S.expand(triple_linear - (18-S.Rational(31,6)*r*r)) == 0
assert S.expand(triple_constant - r*(3-S.Rational(125,108)*r*r)) == 0
assert S.resultant(triple_linear,triple_constant,r) != 0
Q=11*r**4-1080*r**2+3888
u=S.symbols('u')
assert S.discriminant(11*u**2-1080*u+3888,u)==576**2*3
assert S.factor(Q.subs(r,0)) != 0
assert S.factor(Q.subs(r,2)) != 0
print('VERIFY_OK: Hessian reduction; cubic discriminant/resultant; simple boundary flexes; excluded triple roots; exactly two exceptional squared parameters')
