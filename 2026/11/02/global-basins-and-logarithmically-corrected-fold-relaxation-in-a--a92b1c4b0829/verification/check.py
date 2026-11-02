"""Exact symbolic verification of the fold and cubic normal-form coefficients."""
from sympy import symbols, Rational, sqrt, simplify, diff, expand, N, Matrix
x, u=symbols('x u')
c=Rational(50,9); b=Rational(1,90)
s=(9-sqrt(21))/30
a=Rational(1,99)+7*sqrt(21)/891
phi=lambda z:(b+c*z*z)/11
P=lambda z:-Rational(500,9)*z**3+50*z*z-Rational(100,9)*z+11*a+Rational(2,9)
assert simplify(P(s))==0 and simplify(diff(P(x),x).subs(x,s))==0
assert simplify(diff(P(x),x,2).subs(x,s)-100*sqrt(21)/9)==0
p=2*c*s/11; F=20-10*s; D=1+F*p/11
A=simplify((-c-10*p+F*c/11)/D)
q=simplify((c-p*A)/11)
B=simplify(-q*(10+2*F*A/11)/D)
r=simplify(-(p*B+2*q*A)/11)
assert simplify(A+c+10*p-F*q)==0
assert simplify(B+10*q-F*r)==0
assert simplify(p*A+11*q-c)==0
assert simplify(p*B+2*q*A+11*r)==0
J=Matrix([[-1-2*c*s-10*phi(s),F],[2*c*s,-11]])
assert simplify(J.det())==0
assert simplify(J.trace()+12+2*c*s+10*phi(s))==0
assert float(N(J.trace(),18)) < 0
assert float(N(A,18))>0 and float(N(B,18))<0 and float(N(-B/A,18))>0
# Verify the motivating three simple roots and sink–saddle–sink determinants.
a0=Rational(4,99)
P0=lambda z:-Rational(500,9)*z**3+50*z*z-Rational(100,9)*z+11*a0+Rational(2,9)
roots=[Rational(1,10),Rational(1,5),Rational(3,5)]
assert all(simplify(P0(z))==0 for z in roots)
assert [simplify(-diff(P0(x),x).subs(x,z)) for z in roots]==[Rational(25,9),-Rational(20,9),Rational(100,9)]
print('PASS: fold, signs, 4 center-manifold equalities, 3 equilibria')
print('A=',N(A,16),'B=',N(B,16),'L=',N(-B/A,16))
