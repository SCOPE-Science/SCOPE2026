#!/usr/bin/env python3
"""Exact polynomial certificate for a genus-four cyclic trigonal family in characteristic 7.
Requires sympy. Run: python verify_symbolic.py ."""
import itertools
import sympy as sp

p = 7
x, u, v = sp.symbols('x u v')
f = x**5 + u*x**3 + v*x + 1

def red(expression, *vars):
    return sp.Poly(sp.expand(expression), *vars, modulus=p).as_expr()

def coefficient_matrix(power, ids):
    coeffs = sp.Poly(sp.expand(f**power), x)
    return sp.Matrix([[red(coeffs.nth(7*(r+1)-1-c), u, v)
                       for c in ids] for r in ids])

h = coefficient_matrix(2, [0])[0, 0]
B = coefficient_matrix(4, [0,1,2])
delta = red(sp.discriminant(f, x), u, v)
assert red(h - (u*u + 2*v), u, v) == 0
assert red(B.det()-h*delta, u, v) == 0
assert red(delta.subs(v,3*u*u)-3*(u**5-1)**2, u) == 0

M = B.subs(v,3*u*u).applyfunc(lambda z: red(z,u))
expected_M = sp.Matrix([[3*u**7, 3*u**5-3, -3*u**8+u**3],
                        [-2*u, 0, -u*u], [1, 0, -3*u]])
assert (M-expected_M).applyfunc(lambda z:red(z,u)) == sp.zeros(3)
assert red(M.det(),u)==0
# The matrix M has rank exactly two wherever u^5 != 1:
assert red((M[0,0]*M[2,1]-M[0,1]*M[2,0])+3*(u**5-1),u)==0

# Hasse-Witt is the transpose of the seventh-power Cartier coefficient matrix;
# its second iterate has transpose M(u^7)M(u).
P2 = (M.subs(u,u**7)*M).applyfunc(lambda z:red(z,u))
minors=[]
for i,j in itertools.combinations(range(3),2):
    for k,l in itertools.combinations(range(3),2):
        m=sp.Poly(P2[i,k]*P2[j,l]-P2[i,l]*P2[j,k],u,modulus=p)
        if not m.is_zero:minors.append(m)
g = sp.Poly(0,u,modulus=p)
for minor in minors:g=sp.gcd(g,minor)
expected_g=sp.Poly(u*(u**5-1)**9*(u**5+1)*(u**10+1),u,modulus=p).monic()
assert g.monic()==expected_g

S=sp.Poly(u*(u**5+1)*(u**10+1),u,modulus=p)
assert sp.gcd(S,S.diff()).degree()==0
# The third semilinear iterate vanishes at *all* 16 roots, certified
# by reduction in GF(7)[u]/S rather than finite sampling.
def residue(e):
    return sp.rem(sp.Poly(sp.expand(e),u,modulus=p),S).as_expr()
P=sp.eye(3)
for k in range(3):
    Tk=M.subs(u,u**(7**k)).applyfunc(residue)
    P=(Tk*P).applyfunc(residue)
assert P==sp.zeros(3)
fac=sp.factor_list(S.as_expr(),modulus=p)[1]
assert sorted([z.degree() if isinstance(z,sp.Poly) else sp.Poly(z,u).degree() for z,mult in fac for _ in range(mult)])==[1,1,2,4,4,4]
print('SYMBOLIC_DIVISOR_AND_STABLE_RANK_OK')
print('H=',h, 'disc=',delta)
print('S=',S.as_expr(), 'factor degrees:',[1,1,2,4,4,4])
