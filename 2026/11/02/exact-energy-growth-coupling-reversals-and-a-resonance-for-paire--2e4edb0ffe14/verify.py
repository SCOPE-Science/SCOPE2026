#!/usr/bin/env python3
"""Exact algebraic checks for randomly paired symplectic Euler oscillator steps.

Requires Python 3 and SymPy. All polynomial identities use exact arithmetic;
finite enumerations below are diagnostics, not substitutes for the proof.
"""
from fractions import Fraction
import sympy as sp

h, r = sp.symbols('h r', real=True)
I = sp.eye(2)
D = sp.Matrix([[1, h], [0, 1]])
K = sp.Matrix([[1, 0], [-h, 1]])
A, B = K * D, D * K

def exact_zero(mat):
    return all(sp.simplify(x) == 0 for x in mat)

def gram(M):
    return M.T * M

def gram_average(m1, m2):
    return sp.simplify((gram(m1) + gram(m2)) / 2)

assert sp.factor(A.det()) == sp.factor(B.det()) == 1
assert sp.factor(A.trace()) == sp.factor(B.trace()) == 2-h**2
s = 1 + sp.Rational(1, 2)*h**4*(h**2-2)**2
a = 1 + 2*h**6
assert exact_zero(gram_average(A*A, B*B) - s*I)
assert exact_zero(gram_average(A*B, B*A) - a*I)
g = sp.expand(2*r*s + (1-2*r)*a)
assert sp.factor(g - (1+2*h**6+r*h**4*(h**4-8*h**2+4))) == 0
assert sp.simplify((s-a) - h**4*(h**4-8*h**2+4)/2) == 0
assert sp.simplify((sp.sqrt(3)-1)**2 - (4-2*sp.sqrt(3))) == 0
assert sp.simplify((sp.sqrt(3)+1)**2 - (4+2*sp.sqrt(3))) == 0
assert exact_zero((A*A + I).subs(h, sp.sqrt(2)))
assert exact_zero((B*B + I).subs(h, sp.sqrt(2)))
assert sp.simplify(s.subs(h,sp.sqrt(2))) == 1
assert sp.simplify(a.subs(h,sp.sqrt(2))) == 17
assert sp.factor(g.subs(r,sp.Rational(1,4))-(1+h**4/2)**2) == 0

# Independently enumerate up to three i.i.d. blocks, at exact rational settings.
# A block with the word 'AB' uses A first and B second; orientation reversal
# does not affect this two-step averaged calculation.
settings = [
    (sp.Rational(1,4),sp.Rational(0)),
    (sp.Rational(1,2),sp.Rational(0)),
    (sp.Rational(1,2),sp.Rational(1,4)),
    (sp.Rational(1),sp.Rational(1,2)),
    (sp.Rational(3,2),sp.Rational(1,2)),
    (sp.Rational(2),sp.Rational(1,4)),
]
checks = 0
for hv, rv in settings:
    Av, Bv = A.subs(h,hv), B.subs(h,hv)
    table = [
        (Av*Av,rv), (Bv*Bv,rv),
        (Av*Bv,sp.Rational(1,2)-rv),
        (Bv*Av,sp.Rational(1,2)-rv)
    ]
    table = [(M,p) for M,p in table if p]
    assert sum(p for _,p in table) == 1
    states = [(sp.Matrix([sp.Rational(2),sp.Rational(-3)]),sp.Integer(1))]
    original_norm = 13
    for n in range(1,4):
        states = [(T*x,w*prob) for x,w in states for T,prob in table]
        lhs = sum(w*(x.dot(x)) for x,w in states)
        rhs = 13 * g.subs({h:hv,r:rv})**n
        assert sp.simplify(lhs-rhs) == 0,(hv,rv,n,lhs,rhs)
        checks += 1

# Exact reference values for the two physically distinct regimes.
assert sp.simplify(a.subs(h,sp.Rational(1,2))) == sp.Rational(33,32)
assert sp.simplify(s.subs(h,sp.Rational(1,2))) == sp.Rational(561,512)
assert sp.simplify(s.subs(h,1)) == sp.Rational(3,2)
assert sp.simplify(a.subs(h,1)) == 3

print(f'VERIFY_OK: polynomial_identities=11, rational_block_enumerations={checks}, resonance=2')
