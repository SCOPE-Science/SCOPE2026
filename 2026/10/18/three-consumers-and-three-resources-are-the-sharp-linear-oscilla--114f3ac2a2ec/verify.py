#!/usr/bin/env python3
"""Exact linear-stability identities for a cyclic consumer-resource system.

Run with Python 3, SymPy and NumPy; finite numerical checks are diagnostics.
"""
import sympy as s
import numpy as np

L,h=s.symbols('L h')
S=s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
C=4*(s.eye(3)+S)
D=s.eye(3)+S/4
B=C*D.T
assert B==s.Matrix([[5,4,1],[1,5,4],[4,1,5]])
assert C.applyfunc(lambda x:x!=0)==D.applyfunc(lambda x:x!=0)
z=s.symbols('z')
assert s.factor(B.charpoly(z).as_expr())==(z-10)*(z*z-5*z+13)
J=s.zeros(6)
J[:3,3:6]=C
J[3:6,:3]=-D.T
J[3:6,3:6]=-h*s.eye(3)
char=s.factor(J.charpoly(L).as_expr())
target=(L*L+h*L+10)*((L*L+h*L+s.Rational(5,2))**2+s.Rational(27,4))
assert s.expand(char-target)==0
hcrit=3*s.sqrt(30)/10
dcrit=hcrit-s.Rational(5,4)
assert dcrit>0
quartic=s.expand(target/(L*L+h*L+10)) if False else s.expand((L*L+h*L+s.Rational(5,2))**2+s.Rational(27,4))
assert s.expand(quartic-(L**4+2*h*L**3+(h*h+5)*L*L+5*h*L+13))==0
hurwitz=s.expand((2*h)*(h*h+5)*(5*h)-(5*h)**2-(2*h)**2*13)
assert s.expand(hurwitz-h*h*(10*h*h-27))==0
assert s.simplify(quartic.subs(h,hcrit)-(L*L+s.Rational(5,2))*(L*L+2*hcrit*L+s.Rational(26,5)))==0
w=s.sqrt(s.Rational(5,2))
assert s.simplify((s.I*w)**2+hcrit*s.I*w+s.Rational(5,2)-3*s.sqrt(3)*s.I/2)==0
slope=s.simplify(s.re(-s.I*w/(2*s.I*w+hcrit)))
assert slope==-s.Rational(50,127)
for delta,should_be_stable in [(0.1,False),(0.3,False),(0.5,True),(1,True)]:
    vals=np.linalg.eigvals(np.array(J.subs(h,s.Rational(5,4)+s.Rational(str(delta))).evalf(),dtype=float))
    assert (max(vals.real)<0)==should_be_stable
print('PASS: exact block spectrum, support, Hurwitz, crossing frequency and slope; numerical sidedness')
