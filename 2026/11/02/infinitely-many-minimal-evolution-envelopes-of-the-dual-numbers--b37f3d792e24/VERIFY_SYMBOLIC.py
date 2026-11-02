#!/usr/bin/env python3
"""Symbolic rational proof checker for the displayed one-parameter family."""
import sympy as sp
z=sp.symbols('z', real=True)
b=[sp.Integer(1),sp.Integer(2),z]
V=sp.Matrix([[1,1,1],b,[v*v for v in b]])
assert sp.factor(V.det())!=0
w=[sp.factor(v) for v in V.inv()*sp.Matrix([1,0,0])]
e=[sp.factor(v) for v in V.inv()*sp.Matrix([0,1,0])]
assert [sp.simplify(x) for x in (V*sp.Matrix(w)-sp.Matrix([1,0,0]))]==[0,0,0]
assert [sp.simplify(x) for x in (V*sp.Matrix(e)-sp.Matrix([0,1,0]))]==[0,0,0]
assert [sp.factor(x) for x in w]==[2*z/(z-1),-z/(z-2),2/((z-1)*(z-2))]
assert all(sp.simplify(a-b)==0 for a,b in zip(e,[-(z+2)/(z-1),(z+1)/(z-2),-3/((z-1)*(z-2))]))
r=[sp.factor(e[i]/w[i]) for i in range(3)]
assert all(sp.simplify(a-b)==0 for a,b in zip(r,[-(z+2)/(2*z),-(z+1)/z,-sp.Rational(3,2)]))
I=sp.factor(sum(r)**2/sum(x*x for x in r))
expected=2*(3*z+2)**2/(7*z*z+6*z+4)
assert sp.factor(I-expected)==0
assert sp.simplify(sp.diff(I,z)-2*(3*z+2)*(12-10*z)/(7*z*z+6*z+4)**2)==0
print('Vdet:',sp.factor(V.det()))
print('w:',w)
print('epsilon:',e)
print('eigenvalues:',r)
print('I:',I)
print('derivative:',sp.factor(sp.diff(I,z)))
print('VERIFY_OK')
