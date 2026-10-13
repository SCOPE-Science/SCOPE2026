#!/usr/bin/env python3
import sympy as sp
from fractions import Fraction as F

q,a,M = sp.symbols("q a M", positive=True)
expr = sp.simplify((a*q/M)*(1-q)/2)
assert sp.simplify(expr - a*q*(1-q)/(2*M)) == 0
assert sp.simplify(sp.Rational(1,4) - q*(1-q) - (q-sp.Rational(1,2))**2) == 0

samples = [
    (2, [F(1),F(3,2)], [F(1,3),F(2,5)], [F(1,2),F(3,4)], [F(1,10),F(1,5)]),
    (3, [F(2),F(1,2),F(5,4)], [F(1,2),F(1,4),F(3,5)], [F(4,5),F(1,3),F(2,3)], [F(1,20),F(1,10),F(3,20)])
]
for n, aa, qq, rr, bb in samples:
    MM = F(n) + sum(aa)
    lhs = F(0)
    for ai, qi, ri in zip(aa, qq, rr):
        pi = ai*qi/MM
        ci = ri*pi
        Ri = (1-qi)/2
        assert pi/ai < 1/MM
        assert ci < pi
        lhs += ci*Ri
    assert lhs < F(1,8)
    assert 1+sum(bb) > 1
    assert lhs < 1+sum(bb)

print("VERIFY_OK")
print("certificate_identity", expr)
print("quadratic_gap", sp.factor(sp.Rational(1,4)-q*(1-q)))
