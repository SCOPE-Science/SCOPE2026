#!/usr/bin/env python3
"""Exact polynomial identity for cyclic trigonal genus-four covers in F_7."""
import sympy as sp

x = sp.symbols('x')
c = sp.symbols('c0:5')
f = x**5 + sum(c[i] * x**i for i in range(5))
q2 = sp.Poly(f**2, x)
q4 = sp.Poly(f**4, x)
h = sp.Poly(q2.nth(6), *c, modulus=7)
B = sp.Matrix(3, 3, lambda i, j: q4.nth(7*(i+1)-(j+1)))
B = B.applyfunc(lambda z: sp.Poly(z, *c, modulus=7).as_expr())
detB = sp.Poly(B.det(method='berkowitz'), *c, modulus=7)
delta = sp.Poly(sp.discriminant(f, x), *c, modulus=7)
assert h == sp.Poly(c[3]**2 + 2*c[4]*c[2] + 2*c[1], *c, modulus=7)
assert detB == h*delta
assert delta.total_degree() >= 1
assert sp.Poly(f.subs({v:0 for v in c}),x).as_expr() == x**5
# x^5+1 is a smooth, nonordinary witness on the hyperplane h=0.
w = {c[0]:1, c[1]:0, c[2]:0, c[3]:0, c[4]:0}
assert h.eval(w) == 0
assert int(delta.eval(w)) % 7 != 0
print('UNIVERSAL_SYMBOLIC_IDENTITY_OK')
print('Hasse coefficient h:', h.as_expr())
print('det B equals h times quintic discriminant in GF(7)[c0,...,c4]')
print('distinct determinant monomials:',len(detB.terms()),'discriminant monomials:',len(delta.terms()))
