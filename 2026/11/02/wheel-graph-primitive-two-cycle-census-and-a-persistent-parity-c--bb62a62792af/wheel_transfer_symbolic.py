#!/usr/bin/env python3
"""Symbolically reproduce the transfer matrix and rational orbit series."""
import sympy as sp
z,t,u=sp.symbols('z t u')
T=sp.Matrix([[0,1,0,0],[0,0,3*z,2*z],[1,2,0,0],[0,0,2*z,z]])
assert sp.expand(T.charpoly(u).as_expr()-(u**4-z*u**3-6*z*u**2-(2*z**2+3*z)*u-z**2))==0
P=sp.expand((sp.eye(4)-t*T).det())
assert sp.expand(P-(1-z*t-6*z*t**2-(3*z+2*z**2)*t**3-z**2*t**4))==0
B=sp.cancel(-z*sp.diff(P,z)/P).subs(z,1)
expected=t*(1+5*t+2*t**2)/((1+t)*(1-3*t-t**2))
assert sp.cancel(B-expected)==0
print('det(I-tT)=',P)
print('sum_n (N2(n)/n)t^n =',sp.factor(B))
for n in range(3,10):
    polynomial=sp.expand(z*sp.diff(sp.trace(T**n),z))
    assert sp.simplify(polynomial.subs(z,1)-n*int(sp.series(B,t,0,n+1).coeff(t,n)))==0
    if n<=5: print(f'n={n} orbit polynomial=',polynomial)
print('WHEEL_TRANSFER_SYMBOLIC_VERIFY_OK')
