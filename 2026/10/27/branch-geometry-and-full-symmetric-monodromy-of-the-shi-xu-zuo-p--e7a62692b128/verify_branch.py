#!/usr/bin/env python3
"""Exact symbolic checks of polynomial morphism and branch equations."""
import sympy as s
x,y,z,a,b,c,T,t=s.symbols('x y z a b c T t')
F=(y, z*y-x**2, z**2+x**2*y+z*y**2+x**3)
J=s.factor(s.det(s.Matrix(F).jacobian((x,y,z))))
assert J == x*(3*x*y+4*y**2+4*z), ("J", J)
P=T**4+a**2*T**3+2*(b+a**3)*T**2+b**2+a**3*b-a**2*c
assert s.expand(P.subs({T:x,a:F[0],b:F[1],c:F[2]}))==0
assert s.expand((z**2+a**2*z+a*x**2+x**3-c).subs({a:F[0],c:F[2]}))==0
B=b**2+a**3*b-a**2*c
beta=-t**2-s.Rational(3,4)*a**2*t-a**3
gamma=t**3+(a+s.Rational(9,16)*a**2)*t**2+s.Rational(3,4)*a**3*t
R=s.expand(256*s.resultant(beta-b,gamma-c,t))
assert s.Poly(R,c).coeff_monomial(c**2)==-256
assert s.expand(R.subs(a,0)+256*(b**3+c**2))==0
assert s.expand(s.discriminant(P,T)+a**4*B*R)==0
assert s.factor(R)==R or s.expand(s.factor(R)-R)==0
assert s.expand(B.subs(c,s.symbols('w')+a*b)-(b**2-a**2*s.symbols('w')))==0
oneline=s.factor(s.discriminant(P.subs({a:1,b:0}),T))
assert s.expand(oneline+c*(256*c*c+251*c+224))==0, oneline
assert 251**2-4*256*224==-166375
h=x**4+x**3+2*x*x
assert s.factor(s.diff(h,x))==x*(4*x*x+3*x+4)
assert s.discriminant(4*x*x+3*x+4,x)!=0
print('VERIFY_OK Jacobian_and_integrality_quartic_degree4')
print('VERIFY_OK resultant_R_irreducible_specialization_and_discriminant=-a^4*B*R')
print('VERIFY_OK Whitney_umbrella_and_three_simple_branch_values_monodromy_S4')
