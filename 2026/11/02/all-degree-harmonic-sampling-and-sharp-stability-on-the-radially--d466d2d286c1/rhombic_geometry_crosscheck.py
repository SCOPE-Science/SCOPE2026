#!/usr/bin/env python3
"""Supplementary symbolic direct-geometry cross-check of the spectral sector formulas.

Requires SymPy. This finite check supplements the all-degree matrix derivation.
"""
import sympy as S
z = S.symbols('z')
t = S.symbols('t')
cube = [(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)]
axes = [(1,0,0),(0,1,0),(0,0,1)]
R = [S.Matrix(x)/S.sqrt(3) for x in cube] + [S.Matrix(x) for x in axes]
for k in list(range(17)) + [18]:
    P = S.legendre(k,t)
    K = S.Matrix(7,7,lambda i,j:S.simplify(P.subs(t,R[i].dot(R[j]))))
    exact = K.charpoly(z).as_expr()
    a = S.legendre(k,S.Rational(1,3))
    d = S.legendre(k,0)
    c = S.legendre(k,S.sqrt(3)/3)
    if k % 2:
        predicted = (z-(1-3*a))*((z-(1+a))*(z-1)-4*c**2)**3
    else:
        predicted = (z-(1-a))**3*(z-(1-d))**2*((z-(1+3*a))*(z-(1+2*d))-12*c**2)
    assert S.expand(exact-predicted)==0,k
print('RHOMBIC_DODECAHEDRON_GEOMETRY_CROSSCHECK_OK 18 degrees')
