#!/usr/bin/env python3
import sympy as sp

x, y = sp.symbols('x y')
X, Y, Z, a, lam = sp.symbols('X Y Z a lam')

# q=2 specialization of the quotient in equation (8).
N = (x**8 - x)*(y**2 - y) - (y**8 - y)*(x**2 - x)
D = (x**4 - x)*(y**2 - y) - (y**4 - y)*(x**2 - x)
N2 = sp.Poly(N, x, y, modulus=2)
D2 = sp.Poly(D, x, y, modulus=2)
Q, R = sp.div(N2, D2)
assert R.is_zero
q_expected = sp.Poly(
    x**4 + y**4 + x**2*y**2 + x**2*y + x**2
    + x*y**2 + x*y + y**2 + 1,
    x, y, modulus=2,
)
assert Q == q_expected

# Homogenized member Q-lambda=0; subtraction equals addition in characteristic 2.
F0 = (
    X**4 + Y**4 + X**2*Y**2 + X**2*Y*Z + X**2*Z**2
    + X*Y**2*Z + X*Y*Z**2 + Y**2*Z**2
)
F = F0 + (1 + lam)*Z**4
expected_derivatives = [Y*Z*(Y+Z), X*Z*(X+Z), X*Y*(X+Y)]
for variable, expected in zip((X, Y, Z), expected_derivatives):
    got = sp.Poly(sp.diff(F, variable), X, Y, Z, lam, modulus=2)
    want = sp.Poly(expected, X, Y, Z, lam, modulus=2)
    assert got == want

# The derivative equations have exactly the seven projective F_2 points as geometric solutions:
# if Z=0, XY(X+Y)=0; if Z!=0, set Z=1 and obtain X(X+1)=Y(Y+1)=0.
projective_F2 = [
    (1,0,0), (0,1,0), (1,1,0),
    (0,0,1), (1,0,1), (0,1,1), (1,1,1),
]
for p in projective_F2:
    subs = {X:p[0], Y:p[1], Z:p[2]}
    for d in expected_derivatives:
        assert int(d.subs(subs)) % 2 == 0

# On the three points at infinity the member has value 1; on the four affine points it has 1+lambda.
for p in projective_F2[:3]:
    value = sp.Poly(sp.expand(F.subs({X:p[0],Y:p[1],Z:p[2]})), lam, modulus=2)
    assert value == sp.Poly(1, lam, modulus=2)
for p in projective_F2[3:]:
    value = sp.Poly(sp.expand(F.subs({X:p[0],Y:p[1],Z:p[2]})), lam, modulus=2)
    assert value == sp.Poly(lam + 1, lam, modulus=2)

# At lambda=1 the quartic factors over F_4.  Let a^2+a+1=0.
U = X*(X+Z)
V = Y*(Y+Z)
F1 = F0
factor_product = (U + a*V)*(U + (a+1)*V)
G = sp.groebner([a**2+a+1], a, X, Y, Z, modulus=2)
_, rem = G.reduce(sp.Poly(factor_product-F1, a,X,Y,Z, modulus=2).as_expr())
assert sp.Poly(rem, a,X,Y,Z, modulus=2).is_zero

# Smoothness of the first conic A=U+aV: its derivatives are Z, aZ, X+aY.
A = U + a*V
partials_A = [sp.Poly(sp.diff(A,t), a,X,Y,Z, modulus=2).as_expr() for t in (X,Y,Z)]
assert partials_A == [Z, a*Z, X + a*Y]
# The derivative equations force Z=0 and X=aY. Substitution into A reduces to Y^2, nonzero projectively.
A_forced = sp.expand(A.subs({Z:0, X:a*Y}))
_, remA = G.reduce(sp.Poly(A_forced-Y**2, a,X,Y,Z, modulus=2).as_expr())
assert sp.Poly(remA, a,X,Y,Z, modulus=2).is_zero

# The conjugate conic is smooth by the same calculation under a -> a+1.
B = U + (a+1)*V
partials_B = [sp.Poly(sp.diff(B,t), a,X,Y,Z, modulus=2).as_expr() for t in (X,Y,Z)]
assert partials_B == [Z, Z*a + Z, X + Y*a + Y]
B_forced = sp.expand(B.subs({Z:0, X:(a+1)*Y}))
_, remB = G.reduce(sp.Poly(B_forced-Y**2, a,X,Y,Z, modulus=2).as_expr())
assert sp.Poly(remB, a,X,Y,Z, modulus=2).is_zero

print('VERIFY_OK q=2_exception=lambda=1 factors=2_smooth_F4_conics smooth_else=all_lambda_ne_1')
