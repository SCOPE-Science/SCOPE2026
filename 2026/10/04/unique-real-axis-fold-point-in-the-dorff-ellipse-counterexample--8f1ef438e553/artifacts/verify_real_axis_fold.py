#!/usr/bin/env python3
import sympy as sp

x = sp.symbols("x")
a = sp.Rational(-10, 11)
b = sp.Rational(1, 44)
A = sp.Rational(-9890884608, 9139543205)
B = sp.Rational(-251761689, 562995861428)
C = sp.Rational(41190732, 12795360487)
D = sp.Rational(1373955264, 9139543205)

def S(r):
    return x * (2 - r*x) / (1 - r*x)**2

pp = 1 + A**2*S(a*a) + 2*A*B*S(a*b) + B**2*S(b*b)
qp = D**2*S(a*a) + 2*D*C*S(a*b) + C**2*S(b*b)

P4 = sp.Poly(
    24297200*x**4
    - 94137557624*x**3
    + 96137381658603*x**2
    - 231722242336904*x
    - 360263217096475,
    x,
)
P6 = sp.Poly(
    20269382049144670000*x**6
    - 76570023016489888285400*x**5
    + 64433804996566834468116815*x**4
    + 6563513204097494574954697684*x**3
    + 196525575821143049386765307327*x**2
    - 546666175276725488438747500196*x
    - 701902078885331749352905757780,
    x,
)

pm = sp.factor(sp.cancel(pp - qp))
pq = sp.factor(sp.cancel(pp + qp))

expected_pm = -sp.Rational(3748096, 24606462475) * P4.as_expr() / (
    (x - 1936)**2 * (100*x - 121)**2
)
expected_pq = -sp.Rational(3748096, 818606249961404385845) * P6.as_expr() / (
    (x - 1936)**2 * (5*x + 242)**2 * (100*x - 121)**2
)

assert sp.simplify(pm - expected_pm) == 0
assert sp.simplify(pq - expected_pq) == 0

assert sp.count_roots(P4, -1, 1) == 0
assert P4.eval(0) < 0
assert sp.count_roots(P6, -1, 1) == 1

lo = sp.Rational("-0.961916078016036")
hi = sp.Rational("-0.961916078016035")
assert P6.eval(lo) > 0
assert P6.eval(hi) < 0

J = sp.cancel(pp**2 - qp**2)
assert sp.simplify(J.subs(x, 0) - 1) == 0
assert J.subs(x, sp.Rational(-99, 100)) < 0

roots = [
    r for r in sp.nroots(P6, n=60, maxsteps=200)
    if abs(sp.im(r)) < sp.Float("1e-50") and -1 < sp.re(r) < 1
]
assert len(roots) == 1

print("VERIFY_OK")
print("x_star =", sp.N(sp.re(roots[0]), 50))
print("P4 roots in (-1,1) =", sp.count_roots(P4, -1, 1))
print("P6 roots in (-1,1) =", sp.count_roots(P6, -1, 1))
