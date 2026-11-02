#!/usr/bin/env python3
"""Reproduce exact stationary sensitivity identities and a rational two-community example."""
from sympy import symbols, Matrix, Rational, simplify, factor, trace
x, y, g1, g2, h1, h2 = symbols('x y g1 g2 h1 h2')
q1=(1-g1)*x+g1*y
q2=(1-g2)*y+g2*x
F1=((1+h1-2*h1*x)*q1-(1-h1)*x)/2
F2=((1+h2-2*h2*y)*q2-(1-h2)*y)/2
J=Matrix([F1,F2]).jacobian([x,y]); D=factor(J.det())
a,b,c,d=J[0,0],J[0,1],J[1,0],J[1,1]
assert simplify((a+b)-h1*(1-x-q1))==0
assert simplify((c+d)-h2*(1-y-q2))==0
assert simplify(F1.diff(g1)-(y-x)*(1+h1-2*h1*x)/2)==0
assert simplify(F2.diff(g2)-(x-y)*(1+h2-2*h2*y)/2)==0
# Implicit differentiation, including the factor det(J), as polynomial identities.
v1 = -J.adjugate()*Matrix([F1.diff(g1),0]);v2 = -J.adjugate()*Matrix([0,F2.diff(g2)])
assert simplify((v1[0]-v1[1]) +(c+d)*F1.diff(g1))==0
assert simplify((v2[0]-v2[1]) -(a+b)*F2.diff(g2))==0
P={x:Rational(9,10),y:Rational(3,4),g1:Rational(1,4),g2:Rational(1,4),h1:Rational(5,28),h2:-Rational(2,19)}
assert F1.subs(P)==F2.subs(P)==0
assert q1.subs(P)==Rational(69,80)
assert q2.subs(P)==Rational(63,80)
assert (y+q2-1).subs(P)==Rational(43,80)
assert (x+q1-1).subs(P)==Rational(61,80)
J0=J.subs(P); assert J0==Matrix([[-Rational(109,448),Rational(3,28)],[Rational(5,38),-Rational(3,40)]])
assert trace(J0)==-Rational(713,2240)
assert J0.det()==Rational(1413,340480)
assert ((v1[0]-v1[1])/D).subs(P)==Rational(688,785)
assert ((v2[0]-v2[1])/D).subs(P)==-Rational(1220,471)
# Both consensus states are unstable according to their exact determinant conditions.
cplus=(g1*h2*(1-h1)+g2*h1*(1-h2)+2*h1*h2).subs(P)
cminus=(-g1*h2*(1+h1)-g2*h1*(1+h2)+2*h1*h2).subs(P)
assert cplus==-Rational(3,304) and cminus==-Rational(99,2128)
print('PASS symbolic sensitivities and exact rational equilibrium')
print('Jacobian:',J0,'trace:',trace(J0),'det:',J0.det())
print('dPolarization/dGamma1 =',((v1[0]-v1[1])/D).subs(P))
print('dPolarization/dGamma2 =',((v2[0]-v2[1])/D).subs(P))
