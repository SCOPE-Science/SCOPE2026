#!/usr/bin/env python3
"""Exact quadratic-jet check for the local nodality calculation.

Run: python3 verify_universal_jet.py
Requires SymPy (tested with Python 3).

This is an algebraic identity for symbolic coefficients, not a search over cubics.
The normalization of the base-point-free binary quadratic pencil is proved
separately in the accompanying mathematical text.
"""
from itertools import product
from sympy import symbols, expand, Poly, Matrix, factor, diff, simplify

s, t, U, V, W = symbols('s t U V W')
a, b, c, d, e, f = symbols('a b c d e f')
A, B, C, D, E, F, G, H, I, J = symbols('A B C D E F G H I J')
k = symbols('k', nonzero=True)
q0 = A*U**2+B*U*V+C*V**2+D*U*W+E*V*W
q1 = F*U**2+G*U*V+H*V**2+I*U*W+J*V*W

# Ten monomials of transverse degree three, with a nonzero W^3 coefficient.
R3 = 0
for i in range(4):
    for j in range(4-i):
        h = 3-i-j
        coef = k if (i,j,h)==(0,0,3) else symbols('c%d%d%d'%(i,j,h))
        R3 += coef*U**i*V**j*W**h
X = s**2*U+t**2*V + s*q0+t*q1+R3
subs = {U:a*s+b*t, V:c*s+d*t, W:e*s+f*t}
res = expand(X.subs(subs))
coeffs = [res.coeff(s,3),res.coeff(s,2).coeff(t,1),res.coeff(s,1).coeff(t,2),res.coeff(t,3)]
J4=Matrix([[diff(eq,x).subs({a:0,b:0,c:0,d:0,e:0,f:0}) for x in (a,b,c,d)] for eq in coeffs])
assert J4==Matrix.eye(4), J4

# No degree-two obstruction in the two free coordinates: the solved variables
# a,b,c,d therefore vanish to order at least three in the formal local ring.
free = {a:0,b:0,c:0,d:0}
for eq in coeffs:
    h=Poly(expand(eq.subs(free)),e,f)
    assert all(sum(m)>=3 for m,_ in h.terms()),h

# The transverse-gradient column, written in basis s^2,st,t^2, defines M(X).
cols=[]
for x in (U,V,W):
    gx=expand(diff(X,x).subs(subs).subs(free))
    cols.append([gx.coeff(s,2),gx.coeff(s,1).coeff(t,1),gx.coeff(t,2)])
M=Matrix(3,3,lambda i,j:cols[j][i])
m=expand(M.det())
quad=expand(sum(coef*e**alpha*f**beta for (alpha,beta),coef in Poly(m,e,f).terms() if alpha+beta==2))
assert simplify(quad+6*k*e*f)==0,quad
Hessian=Matrix([[diff(quad,z1,z2) for z2 in (e,f)] for z1 in (e,f)])
assert simplify(Hessian.det()+36*k*k)==0,Hessian.det()
print('UNIVERSAL_TRIPLE_LINE_QUADRATIC_JET_OK')
print('fano_jacobian_det:',J4.det())
print('second_type_local_equation_quadratic_jet:',quad)
print('quadratic_hessian_det:',factor(Hessian.det()))
