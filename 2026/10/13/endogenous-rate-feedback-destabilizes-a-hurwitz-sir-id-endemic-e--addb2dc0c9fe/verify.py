"""Exact rational certificate for a five-variable epidemiological equilibrium.

Requires SymPy; run: python verify.py
"""
import sympy as sp

S, I, R, a, b = sp.symbols('S I R a b', real=True)
mu, r, sigma, P, dp, dm, gp, gm = sp.symbols(
    'mu r sigma P dp dm gp gm', positive=True
)
N = S + I + R
F = sp.Matrix([
    P - b*I*S/N - mu*S + r*R,
    b*I*S/N - (mu+a+sigma)*I,
    sigma*I - (mu+r)*R,
    dp*I-dm*a*R,
    gp*I-gm*b*R,
])
state = (S,I,R,a,b)
parameters = {
    mu:sp.Rational(2,25), r:sp.Rational(1,10), sigma:sp.Rational(1,5),
    P:sp.Rational(313,3800), dp:sp.Rational(1,45), dm:sp.Integer(1),
    gp:sp.Rational(80,9), gm:sp.Integer(20),
    S:sp.Rational(3,4), I:sp.Rational(9,76), R:sp.Rational(5,38),
    a:sp.Rational(1,50), b:sp.Rational(2,5),
}
assert sum(parameters[t] for t in (S,I,R)) == 1
assert all(v == 0 for v in F.subs(parameters))
assert sp.Rational(1,100) < parameters[a] < sp.Rational(1,10)
assert sp.Rational(1,5) < parameters[b] < sp.Rational(4,5)
assert sp.cancel((b/(mu+a+sigma)).subs(parameters)) == sp.Rational(4,3)
J = F.jacobian(state).subs(parameters)
z = sp.symbols('z')
p5 = sp.Poly(J.charpoly(z).as_expr(), z)
p3 = sp.Poly(J[:3,:3].charpoly(z).as_expr(), z)
assert p5.all_coeffs() == [
    sp.Integer(1), sp.Rational(2917,950), sp.Rational(1606999,3610000),
    sp.Rational(33399687,685900000), sp.Rational(2478983,274360000),
    sp.Rational(2817,5487200),
]
assert p3.all_coeffs() == [
    sp.Integer(1), sp.Rational(146,475), sp.Rational(6921,190000),
    sp.Rational(2817,1900000),
]
c = p3.all_coeffs()
assert all(t>0 for t in c) and c[1]*c[2] > c[3]

def routh_first_column(coeff):
    n = len(coeff) - 1
    width = (n+2)//2
    rows = [list(coeff[::2]), list(coeff[1::2])]
    for row in rows:
        row.extend([sp.S.Zero]*(width-len(row)))
    while len(rows)<n+1:
        above, previous = rows[-2], rows[-1]
        assert previous[0] != 0
        row = [sp.factor((previous[0]*above[j+1]-above[0]*previous[j+1])/
                         previous[0]) for j in range(width-1)]
        row.append(sp.S.Zero)
        rows.append(row)
    return [row[0] for row in rows]

first = routh_first_column(p5.all_coeffs())
assert [sp.sign(t) for t in first] == [1,1,1,-1,1,1]
assert all(t != 0 for t in first)
a5,a4,a3,a2,a1,a0=p5.all_coeffs()
delta3=sp.factor(a4*a3*a2-a4*a4*a1-a5*a2*a2+a5*a4*a0)
assert delta3 == -sp.Rational(11422998795700081,588073512500000000)
print('VERIFY_OK')
print('three-state polynomial:',p3.as_expr())
print('five-state polynomial:',p5.as_expr())
print('Routh first-column signs:',[int(sp.sign(t)) for t in first])
print('Delta3:',delta3)
