#!/usr/bin/env python3
import sympy as sp

# Exact strict-extension witness.
N0 = sp.Integer(1)
beta0 = sp.Integer(1)
betap = sp.Integer(-2)
mu = sp.Integer(0)
p = [sp.Rational(3,10), sp.Rational(2,5), sp.Rational(3,10)]
kappa = [sp.Integer(0)]*3
gamma = [sp.Rational(1,5), sp.Integer(1), sp.Integer(5)]

c = [2*(1-mu)*p[i]*(1-kappa[i]) for i in range(3)]
a = [beta0+gamma[i] for i in range(3)]
w = [sp.simplify(c[i]*beta0/a[i]) for i in range(3)]
assert w == [sp.Rational(1,2), sp.Rational(2,5), sp.Rational(1,10)]
assert sum(w) == 1

source_sign_terms = [
    sp.simplify(beta0 + betap*N0*gamma[i]/a[i])
    for i in range(3)
]
assert source_sign_terms == [sp.Rational(2,3), sp.Integer(0), sp.Rational(-2,3)]
assert any(x > 0 for x in source_sign_terms)
assert any(x < 0 for x in source_sign_terms)

r = sp.simplify(-N0*betap/beta0)
b = [sp.simplify(w[i]*(a[i]-r*gamma[i])) for i in range(3)]
assert b == [sp.Rational(2,5), sp.Integer(0), sp.Rational(-2,5)]

one = sp.ones(3,1)
A = -sp.diag(*a) + sp.Matrix(b)*one.T
lam = sp.symbols("lam")
charpoly = sp.factor(A.charpoly(lam).as_expr())
expected = sp.factor((lam+2) * (lam**2 + sp.Rational(36,5)*lam + sp.Rational(132,25)))
assert sp.expand(charpoly-expected) == 0

eigs_expected = [
    sp.Integer(-2),
    sp.Rational(-18,5) + sp.Rational(8,5)*sp.sqrt(3),
    sp.Rational(-18,5) - sp.Rational(8,5)*sp.sqrt(3),
]
for ev in eigs_expected:
    assert sp.simplify(charpoly.subs(lam, ev)) == 0
    assert float(ev.evalf()) < 0

# Directly replay the equilibrium normalization and determinant identity.
assert sp.simplify(sum(c[i]*beta0/a[i] for i in range(3)) - 1) == 0

secular = sp.simplify(
    1 - sum(b[i]/(lam+a[i]) for i in range(3))
)
rewritten = sp.simplify(
    sum(w[i]*(lam+r*gamma[i])/(lam+a[i]) for i in range(3))
)
assert sp.simplify(secular-rewritten) == 0

print("VERIFY_OK")
print("equilibrium_fractions", [str(x) for x in w])
print("source_sign_terms", [str(x) for x in source_sign_terms])
print("jacobian", A.tolist())
print("characteristic_polynomial", charpoly)
print("eigenvalues", [str(x) for x in eigs_expected])
