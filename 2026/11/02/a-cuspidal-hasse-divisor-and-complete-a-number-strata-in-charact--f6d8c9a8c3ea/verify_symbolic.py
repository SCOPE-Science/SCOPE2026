#!/usr/bin/env python3
"""Exact coefficient and determinantal identities over F_7 for a genus-five hyperelliptic family."""
import itertools
import sympy as sp
x,a,b,c=sp.symbols('x a b c')
poly=sp.Poly((x**11+a*x**6+c*x**3+b*x)**3,x)
H=sp.Matrix(5,5,lambda i,j: poly.nth(7*(i+1)-(j+1)))
expected=sp.Matrix([
 [0,3*b**2*c,0,b**3,0],
 [3*b*(a**2+b),3*a*c**2,0,6*a*b*c,c**3],
 [6*a*c,0,a*(a**2+6*b),3*c**2,0],
 [0,0,3*c,0,3*(a**2+b)],
 [0,1,0,0,0]
])
assert all(sp.Poly(H[i,j]-expected[i,j],a,b,c,modulus=7).is_zero for i in range(5) for j in range(5))
F=2*c**5+b*(a**2-b)*(a**2+b)**2
expr=sp.Poly(sp.expand(H.det()+9*a*b**3*F),a,b,c,modulus=7)
assert expr.is_zero,expr
minor=H.minor_submatrix(2,0).det()
assert sp.Poly(sp.expand(minor+3*b**3*c**4),a,b,c,modulus=7).is_zero
assert sp.Poly(sp.expand(F.subs(c,0)-b*(a*a-b)*(a*a+b)**2),a,b,modulus=7).is_zero
# The c=0 row/column permutation pattern gives rank exactly 3 iff a^2+b=0,
# assuming b != 0; all three remaining nonzero entries are visibly independent.
M0=H.subs(c,0)
assert M0[0,3]==b**3 and M0[4,1]==1
assert sp.Poly(M0[1,0]-3*b*(a*a+b),a,b,modulus=7).is_zero
assert sp.Poly(M0[3,4]-3*(a*a+b),a,b,modulus=7).is_zero
assert sp.Poly(M0[2,2]-a*(a*a+6*b),a,b,modulus=7).is_zero
# On the generic cusp a!=0,b=-a^2, smoothness of the hyperelliptic
# polynomial at c=0 follows from b(a^2-4b) != 0.
assert sp.Poly(sp.expand((b*(a*a-4*b)).subs(b,-a*a)-5*a**2*(-a*a)),a,modulus=7).is_zero
print('EXACT_HASSE_CUSP_SYMBOLIC_OK')
