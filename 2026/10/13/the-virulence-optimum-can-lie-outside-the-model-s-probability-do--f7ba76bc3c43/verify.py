#!/usr/bin/env python3
import sympy as sp

b1,b2,p,q,c,delta = sp.symbols("b1 b2 p q c delta", positive=True)

bar = (b1+p*b2)/(1+p)
gamma = sp.simplify(p*c*bar**2/q)
R = sp.simplify(b1/delta + p*b2/gamma)
dR = sp.factor(sp.diff(R,b2))
expected_dR = q*(1+p)**2*(b1-p*b2)/(c*(b1+p*b2)**3)
assert sp.simplify(dR-expected_dR) == 0

# Exact witness.
subs = {
    p: sp.Rational(1,2),
    q: sp.Rational(1,2),
    c: sp.Integer(1),
    b1: sp.Integer(1),
    delta: sp.Rational(1,2),
}
gamma_w = sp.factor(gamma.subs(subs))
R_w = sp.factor(R.subs(subs))
dR_w = sp.factor(dR.subs(subs))

assert gamma_w == (b2+2)**2/9
assert sp.simplify(R_w - (2 + 9*b2/(2*(b2+2)**2))) == 0
assert sp.simplify(dR_w - 9*(2-b2)/(2*(b2+2)**3)) == 0

# gamma<1 iff b2<1 for b2>0 in the witness.
assert sp.simplify(gamma_w.subs(b2,2)) == sp.Rational(16,9)
assert sp.simplify(gamma_w.subs(b2,sp.Rational(1,2))) == sp.Rational(25,36)
assert sp.simplify(R_w.subs(b2,sp.Rational(1,2))) == sp.Rational(59,25)

# On 0<b2<1, dR_w is positive because both factors are positive.
assert dR_w.subs(b2, sp.Rational(1,2)) > 0
boundary_R = sp.limit(R_w, b2, 1, dir='-')
assert boundary_R == sp.Rational(5,2)

# General classification algebra.
B = (1+p)*sp.sqrt(q/(p*c))
beta_max = sp.simplify((B-b1)/p)
beta_u = b1/p
assert sp.simplify((beta_max-beta_u) - (B-2*b1)/p) == 0

print("VERIFY_OK")
print("general_derivative", dR)
print("witness_gamma", gamma_w)
print("witness_R0", R_w)
print("witness_derivative", dR_w)
print("source_optimizer_gamma", gamma_w.subs(b2,2))
print("interior_witness_gamma", gamma_w.subs(b2,sp.Rational(1,2)))
print("boundary_supremum", boundary_R)
