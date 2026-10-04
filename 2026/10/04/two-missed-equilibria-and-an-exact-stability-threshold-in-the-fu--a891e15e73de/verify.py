import sympy as sp

d, lam = sp.symbols("d lam", positive=True)
x, y, z, w = sp.symbols("x y z w")

F = sp.Matrix([
    35*(y-x)+w,
    12*y-10*x*z,
    -3*z+10*x*y,
    d*y+x**2,
])

J = F.jacobian([x,y,z,w])

def charpoly_at(subs):
    return sp.expand((lam*sp.eye(4)-J.subs(subs)).det())

for s in (sp.Integer(1), sp.Integer(-1)):
    E = {
        x: s*sp.Rational(3,5),
        y: -sp.Rational(9,25)/d,
        z: -s*sp.Rational(18,25)/d,
        w: 35*(s*sp.Rational(3,5)+sp.Rational(9,25)/d),
    }
    assert sp.simplify(F.subs(E)) == sp.zeros(4,1)

origin_poly = sp.factor(charpoly_at({x:0,y:0,z:0,w:0}))
assert origin_poly == lam*(lam+35)*(lam+3)*(lam-12)

Eplus = {
    x: sp.Rational(3,5),
    y: -sp.Rational(9,25)/d,
    z: -sp.Rational(18,25)/d,
    w: 35*(sp.Rational(3,5)+sp.Rational(9,25)/d),
}
Eminus = {
    x: -sp.Rational(3,5),
    y: -sp.Rational(9,25)/d,
    z: sp.Rational(18,25)/d,
    w: 35*(-sp.Rational(3,5)+sp.Rational(9,25)/d),
}

pplus = sp.Poly(charpoly_at(Eplus), lam)
pminus = sp.Poly(charpoly_at(Eminus), lam)

expected_plus = sp.Poly(
    lam**4 + 26*lam**3
    -(1581*d+1260)/(5*d)*lam**2
    +(18*d-7560)/(5*d)*lam
    -sp.Rational(216,5),
    lam,
)
expected_minus = sp.Poly(
    lam**4 + 26*lam**3
    +(1260-1569*d)/(5*d)*lam**2
    +(7560-18*d)/(5*d)*lam
    +sp.Rational(216,5),
    lam,
)
assert sp.simplify(pplus.as_expr()-expected_plus.as_expr()) == 0
assert sp.simplify(pminus.as_expr()-expected_minus.as_expr()) == 0

def routh_first_col(poly):
    a4,a3,a2,a1,a0 = poly.all_coeffs()
    b1 = sp.factor((a3*a2-a1)/a3)
    c1 = sp.factor((b1*a1-a3*a0)/b1)
    return [sp.factor(a4), sp.factor(a3), b1, c1, sp.factor(a0)]

rp = routh_first_col(expected_plus)
rm = routh_first_col(expected_minus)
assert sp.simplify(rp[2] + 6*(3427*d+2100)/(65*d)) == 0
assert sp.simplify(rp[3] - 18*(47*d**2-1437240*d-882000)/(5*d*(3427*d+2100))) == 0
assert sp.simplify(rm[2] + 12*(1699*d-1050)/(65*d)) == 0
assert sp.simplify(rm[3] + 54*(3*d**2-238210*d+147000)/(5*d*(1699*d-1050))) == 0

dH = (sp.Integer(119105)-455*sp.sqrt(68521))/3
qminus = 3*d**2-238210*d+147000
assert sp.simplify(qminus.subs(d,dH)) == 0

omega2 = sp.simplify((7560-18*dH)/(130*dH))
assert sp.simplify(omega2 - 9*(261+sp.sqrt(68521))/50) == 0
k = sp.simplify(sp.Rational(216,5)/omega2)
assert sp.simplify(k - (-sp.Rational(783,5)+3*sp.sqrt(68521)/5)) == 0

factor_target = sp.expand((lam**2+omega2)*(lam**2+26*lam+k))
assert sp.simplify(expected_minus.as_expr().subs(d,dH)-factor_target) == 0

for dv, expected_rhp_plus, expected_rhp_minus in [
    (sp.Rational(1,10), 1, 0),
    (sp.Rational(1,1), 1, 2),
    (sp.Rational(10,1), 1, 2),
    (sp.Rational(30,1), 1, 2),
]:
    roots_p = [complex(r) for r in sp.nroots(expected_plus.as_expr().subs(d,dv), n=30)]
    roots_m = [complex(r) for r in sp.nroots(expected_minus.as_expr().subs(d,dv), n=30)]
    assert sum(r.real > 1e-12 for r in roots_p) == expected_rhp_plus
    assert sum(r.real > 1e-12 for r in roots_m) == expected_rhp_minus

print("VERIFY_OK")
