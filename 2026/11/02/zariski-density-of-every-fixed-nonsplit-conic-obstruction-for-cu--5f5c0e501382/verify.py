#!/usr/bin/env python3
"""Exact symbolic check of the concrete Hamilton-conic cubic witness.

Requires SymPy. This verifies an explicit example, not the density proof.
"""
import sympy as s
X, Y, z, m = s.symbols("X Y z m", real=True)
i = s.I
P = X**3 + (1+i)*X**2*Y + (2+3*i)*X*Y**2 + (1-2*i)*Y**3
Q = s.expand(s.conjugate(P.subs({X:Y, Y:-X}, simultaneous=True)))
assert s.expand(Q.subs({X:-Y, Y:X}, simultaneous=True) - s.conjugate(P)) == 0
assert s.expand(-P.subs({X:-Y, Y:X}, simultaneous=True) - s.conjugate(Q)) == 0
p = s.expand(P.subs({X:z, Y:1}))
q = s.expand(Q.subs({X:z, Y:1}))
assert s.resultant(p, q, z) == 675
fixed = s.expand(p-z*q)
assert s.discriminant(fixed, z) == 27760
mult_num = s.expand(s.diff(p,z)*q-p*s.diff(q,z))
multpoly = s.Poly(s.resultant(fixed, m*q**2-mult_num, z),m)
expected = 675*m**4+920*m**3+5658*m**2+10984*m+9523
assert multpoly.degree()==4
assert s.rem(multpoly.as_expr(),expected,m)==0
assert s.discriminant(expected,m) == 67927190083003088896000
assert s.simplify(multpoly.LC())!=0
print('VERIFY_OK')
