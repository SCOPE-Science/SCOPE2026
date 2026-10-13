#!/usr/bin/env python3
import sympy as sp

lam, mu, om, tau, n, Lam = sp.symbols("lam mu om tau n Lam", positive=True)
A0 = sp.Matrix([
    [-(om+mu), n*Lam/mu],
    [om, -(tau+mu)],
])
char0 = sp.factor((lam*sp.eye(2)-A0).det())
expected0 = sp.expand(
    lam**2 + (om+tau+2*mu)*lam
    + (om+mu)*(tau+mu) - n*Lam*om/mu
)
assert sp.simplify(char0-expected0) == 0

Rstar = sp.simplify(n*Lam*om/(mu*(om+mu)*(tau+mu)))
Rsrc = sp.simplify(n*Lam*om/(mu**2*(om+tau+mu)))
assert sp.simplify(
    Rsrc/Rstar - (1 + om*tau/(mu*(om+tau+mu)))
) == 0

square_gap = sp.expand(
    (om+tau+2*mu)**2
    - ((om-tau)**2 + 4*n*Lam*om/mu)
)
expected_gap = 4*(mu*(om+mu)*(tau+mu)-n*Lam*om)/mu
assert sp.simplify(square_gap-expected_gap) == 0

a, b, c = sp.symbols("a b c", positive=True)
J3 = sp.Matrix([
    [-(mu+c), 0, -a*b/om],
    [c, -a, a*b/om],
    [0, om, -b],
])
p = sp.factor((lam*sp.eye(3)-J3).det())
expected_p = sp.expand(
    lam**3 + (mu+c+a+b)*lam**2
    + (mu+c)*(a+b)*lam + a*b*c
)
assert sp.simplify(p-expected_p) == 0

vals = {mu:sp.Integer(1), om:sp.Integer(2), tau:sp.Integer(3),
        n:sp.Integer(1), Lam:sp.Integer(4)}
assert sp.simplify(Rstar.subs(vals)) == sp.Rational(2,3)
assert sp.simplify(Rsrc.subs(vals)) == sp.Rational(4,3)
Aw = A0.subs(vals)
cp = sp.expand((lam*sp.eye(2)-Aw).det())
assert sp.simplify(cp-(lam**2+7*lam+4)) == 0
for rr in sp.solve(cp, lam):
    assert float(sp.N(rr)) < 0

vals2 = {mu:sp.Integer(1), om:sp.Integer(2), tau:sp.Integer(3),
         n:sp.Integer(1), Lam:sp.Integer(8)}
assert sp.simplify(Rstar.subs(vals2)) == sp.Rational(4,3)
Istar2 = sp.simplify(
    ((n*Lam*om - mu*(om+mu)*(tau+mu)) /
     (n*(om+mu)*(tau+mu))).subs(vals2)
)
assert Istar2 == sp.Rational(1,3)
aa = vals2[om] + vals2[mu]
bb = vals2[tau] + vals2[mu]
cc = vals2[n] * Istar2
Acoef = vals2[mu] + cc + aa + bb
Bcoef = (vals2[mu] + cc)*(aa + bb)
Ccoef = aa*bb*cc
assert Acoef > 0 and Bcoef > 0 and Ccoef > 0 and Acoef*Bcoef > Ccoef

print("VERIFY_OK")
