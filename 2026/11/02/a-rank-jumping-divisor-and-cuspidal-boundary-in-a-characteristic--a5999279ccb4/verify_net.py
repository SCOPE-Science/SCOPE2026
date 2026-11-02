#!/usr/bin/env python3
"""Exact characteristic-three certificate for a genus-four bielliptic net.
Requires Python 3 and SymPy. Uses polynomial arithmetic, never floating point.
"""
import sympy as S

x, y, z, w, s, t = S.symbols('x y z w s t')
P = y**2*z-x**3-x*z**2-z**3
Q = w**2-x*y-s*x*z-t*z**2
E = ((1,1,1,2),(1,1,2,1),(1,2,1,1),(2,1,1,1))


def zero_mod3(e):
    return S.Poly(S.expand(e), s, t, modulus=3).is_zero


f = S.Poly(S.expand(P**2*Q**2),x,y,z,w)
M = []
for i in range(4):
    row = []
    for j in range(4):
        a = tuple(3*E[i][k]-E[j][k] for k in range(4))
        assert min(a)>=0
        coeff=f.coeff_monomial(x**a[0]*y**a[1]*z**a[2]*w**a[3])
        row.append(S.Poly(coeff,s,t,modulus=3).as_expr())
    M.append(row)
expected = [[0,0,0,0], [0,s,-1,s+t], [0,0,0,1], [0,0,-1,s]]
assert all(zero_mod3(M[i][j]-expected[i][j]) for i in range(4) for j in range(4))
B=S.Matrix([row[1:] for row in M[1:]])
assert zero_mod3(B.det()-s)
assert zero_mod3(S.det(S.Matrix([row[2:] for row in M[2:]]))-1)

# The norm polynomial for the zeros of xy+sx+t, away from x=0.
F=x**5+x**3+(1-s**2)*x**2+s*t*x-t**2
R=S.resultant(F,S.diff(F,x),x)
D=-(s**2-1)**2+s**3*(t**3+t)+s**2*(t**2-t**4)-t**6
assert zero_mod3(R-t**2*D)
assert zero_mod3(D.subs(s,0)+(t**2+1)**3)
assert zero_mod3(D.subs(t,0)+(s**2-1)**2)

# At s=0 and t^2=-1 the eliminated polynomial has a triple root at x=-1.
F_special=x**5+x**3+x**2+1
assert S.Poly(F_special-(x+1)**3*(x**2+1),x,modulus=3).is_zero

# Check the base cubic is smooth in characteristic 3 (f'(x)=1).
assert S.Poly(S.diff(x**3+x+1,x)-1,x,modulus=3).is_zero

print('CHAR3_BIELLIPTIC_NET_RESULTANT_HASSE_RANK_CUSP_EXACT_PASS')
print('Transposed Hasse-Witt coefficient matrix:',M)
print('Discriminant polynomial:',S.expand(D))
