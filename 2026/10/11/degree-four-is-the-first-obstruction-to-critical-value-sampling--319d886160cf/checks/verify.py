#!/usr/bin/env python3
"""Exact algebraic verification of the minimal quartic critical-value hull witness.
Requires sympy >= 1.12. Run: python3 checks/verify.py.
"""
import sympy as s
z = s.symbols('z')
I = s.I
a = s.Rational(8, 5)
p = z**4 + s.Rational(32, 15)*z**3 + 2*z**2 + s.Rational(32, 5)*z
w = s.Rational(2, 21)
assert s.simplify(s.diff(p, z) - 4*(z+a)*(z**2+1)) == 0
fibers = (
    (-a, s.Rational(8,15)+I*s.sqrt(578)/15,
         s.Rational(8,15)-I*s.sqrt(578)/15),
    (I, s.Rational(4,15)-s.Rational(9,5)*I,
        -s.Rational(12,5)-I/5),
    (-I, s.Rational(4,15)+s.Rational(9,5)*I,
         -s.Rational(12,5)+I/5),
)
for critical, root1, root2 in fibers:
    identity = p-p.subs(z,critical)-(z-critical)**2*(z-root1)*(z-root2)
    assert s.simplify(identity) == 0
r = s.Rational(5,14)
assert 0 < r < 1
for sign in (1, -1):
    first = sign*I
    second = s.Rational(4,15)-sign*s.Rational(9,5)*I
    assert s.simplify(w-((1-r)*first+r*second)) == 0
right_midpoint = s.Rational(8,15)
t = s.simplify((w+a)/(right_midpoint+a))
assert t == s.Rational(89,112) and 0 < t < 1
assert s.simplify(w-((1-t)*(-a)+t*right_midpoint)) == 0
assert w > 0
print('EXACT_SYMBOLIC_CHECK_PASS')
