"""Verify curvature expansions for generalized one-parameter means.

Requires SymPy >= 1.14.  The symbolic checks reproduce the leading
near-diagonal coefficients stated in RESULT.md.  The numerical checks use
the exact hyperbolic derivative formulas only as sanity checks.
"""
import sympy as sp

u, r, a, z = sp.symbols("u r a z", positive=True)

# log(sinh(z)/z) through z^6
phi = z**2/sp.Integer(6) - z**4/sp.Integer(180) + z**6/sp.Integer(2835)

def ph(arg):
    return sp.expand(phi.subs(z, arg))

L = sp.expand((ph(u*(r+a)) - ph(u*r))/a)
J = sp.series(sp.exp(L), u, 0, 7).removeO()
J2 = sp.expand(sp.diff(J, r, 2))
j2_u4 = sp.expand(J2).coeff(u, 4)
assert sp.simplify(j2_u4 - (5 - 6*r - 3*a)/45) == 0

K = sp.expand((ph(u*(r+a)) + ph(u*(a-r)) - 2*ph(u*r))/a)
K2 = sp.expand(sp.diff(K, r, 2))
k2_u4 = sp.expand(K2).coeff(u, 4)
assert sp.simplify(k2_u4 + 2*a/15) == 0

# Direct numerical signs for alpha=1, u=0.1.
def phi1(t):
    return sp.coth(t) - 1/t

def phi2(t):
    if t == 0:
        return sp.Rational(1, 3)
    return 1/t**2 - 1/sp.sinh(t)**2

aa = sp.Integer(1)
uu = sp.Rational(1, 10)
mid = -sp.Rational(1, 2)
lp_mid = (uu/aa) * (phi1(uu*(mid+aa)) - phi1(uu*mid))
lpp_mid = (uu**2/aa) * (phi2(uu*(mid+aa)) - phi2(uu*mid))
j2_over_j_mid = sp.N(lpp_mid + lp_mid**2, 50)

rr = sp.Integer(1)
k2_num = sp.N(
    (uu**2/aa) * (
        phi2(uu*(rr+aa)) + phi2(uu*(aa-rr)) - 2*phi2(uu*rr)
    ),
    50,
)

assert j2_over_j_mid > 0
assert k2_num < 0

print("coeff J_alpha'' / m at u^4:", sp.factor(j2_u4))
print("coeff (log product)'' at u^4:", sp.factor(k2_u4))
print("alpha=1, u=0.1, J''/J at r=-1/2:", j2_over_j_mid)
print("alpha=1, u=0.1, (log product)'' at r=1:", k2_num)
