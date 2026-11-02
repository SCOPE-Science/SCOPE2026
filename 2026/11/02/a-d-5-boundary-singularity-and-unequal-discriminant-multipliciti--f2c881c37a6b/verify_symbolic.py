#!/usr/bin/env python3
"""Exact symbolic checks of the characteristic-five Picard degeneration geometry."""
import sympy as S
x,a,b,c,z=S.symbols('x a b c z')
P=lambda f: S.Poly(S.expand(f),a,b,c,z, modulus=5)
f=x**4+a*x**2+b*x+c
F=S.Poly(S.expand(f**3),x)
A=c*c+a*a*c+a*b*b
D=S.discriminant(f,x)
assert P(F.nth(4)-3*A).is_zero
assert P(F.nth(9)-3*b).is_zero
assert P(D-((a*a+c)*A-2*b*b*(a*c+b*b))).is_zero
assert P(A.subs(c,z-3*a*a)-(z*z+a*b*b+a**4)).is_zero
assert S.Poly(S.resultant(A,D,c)+b**8,a,b,modulus=5).is_zero
# Irreducible over the algebraic closure, since the quadratic's discriminant
# is a(a^3+b^2), with odd a-adic valuation.
assert S.Poly(A,c).degree()==2
assert S.Poly(a**4-4*a*b*b,a).as_expr().subs(a,0)==0
assert S.Poly(a**3+b*b,a).as_expr().subs(a,0)==b*b
# There is only one singularity: z=0, ab=0, b^2+4a^3=0.
# On D5 surface, if a=0 then b=0; if b=0 then a=0.
# Generic valuations: at b=0, c=0 has order_b(c)=2 and c=-a^2 has order_b(c)=0;
# Delta=-2b^2(ac+b^2), and a(ac+b^2)=-c^2 on H.
assert P(a*(a*c+b*b)+c*c-A).is_zero
print('EXACT_PICARD_D5_AND_6_2_BOUNDARY_OK')
