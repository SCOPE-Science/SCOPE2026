#!/usr/bin/env python3
"""Exact algebraic identities for a characteristic-three sextic boundary.

Requires Python 3 and SymPy. The symbolic geometric argument is in RESULT.md;
finite witnesses are not used to prove assertions over all algebraically closed fields.
"""
from sympy import symbols, Poly, expand, cancel, diff, gcd

a, b, U, V, W, s, t, w, q, h = symbols('a b U V W s t w q h')

def zero_mod3(expression, variables):
    expression = expand(cancel(expression))
    return all(int(c) % 3 == 0 for c in Poly(expression, *variables, domain='ZZ').coeffs())

C = U**3 + V**3 + W**3 + a*(U**2*V + V**2*W + W**2*U) + b*(U*V**2 + V*W**2 + W*U**2)
A = a+b
B = b-a
local = A*w*t**2 + B*s**3 + A*s**2*t + b*s*t**2 + t**3
assert zero_mod3(C.subs({U:w+s,V:w+t-s,W:w}, simultaneous=True) - local, (a,b,s,t,w))

# The three cyclic axis equations have the same parameter polynomial.
f = q**3 + a*q**2 + b*q + 1
assert zero_mod3(C.subs({U:0,V:q,W:1})-f, (a,b,q))
assert zero_mod3(diff(f,q) - (b-a*q), (a,b,q))
D = a*a*b*b-(a+b)**3
# At q0=b/a, the double-root criterion is exactly D=0.
assert zero_mod3(expand(a**3 * f.subs(q,b/a) + D), (a,b))
assert zero_mod3(expand(a**3*(f.subs(q,b/a+h)-f.subs(q,b/a)-a*h*h-h*h*h)), (a,b,h))
# The perpendicular differential never vanishes on D=0 when a+b is nonzero:
CU = diff(C,U).subs({U:0,V:q,W:1})
assert zero_mod3(expand(a*a*CU.subs(q,b/a)-(a+b)**3), (a,b))

# A genuine nonempty boundary witness exists over the algebraic closure of F3:
# b satisfies b^3-b^2+1 and a=1; no root lies in F3, hence b != 0,+/-1.
P = q**3-q**2+1
assert all(int(P.subs(q,c))%3 != 0 for c in (0,1,2))
# The discriminant for a=1 is -(b^3-b^2+1) mod 3.
assert zero_mod3(D.subs(a,1)+P.subs(q,b), (b,))

print('KAWAKITA_CHAR3_BOUNDARY_SYMBOLIC_IDENTITIES_AND_NONEMPTY_WITNESS_PASS')
