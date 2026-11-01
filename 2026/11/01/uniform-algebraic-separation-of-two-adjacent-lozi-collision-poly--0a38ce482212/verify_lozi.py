"""Exact rational-polynomial check of two Lozi formal collision loci.

Requires Python 3.10+ and SymPy (tested with SymPy 1.13.1).  All
identities are polynomial identities over the integers; no sampling or
floating-point root approximations are used for the certificate.
"""
import math
import sympy as sp

A, B, T = sp.symbols('a b t')
C = A - B - 1
Q = {1: sp.Matrix([[-A, -B], [1, 0]]),
     -1: sp.Matrix([[A, -B], [1, 0]])}

EXPECTED_P4 = (
    A**5 - A**4*B - A**4 + A**3*B**2 - A**3
    + A**2*B**3 - A**2*B**2 + A**2*B - A**2
    + A*B**4 + A*B**2 + A - B**5 + B**4 - B**3 - B**2 + B - 1
)
EXPECTED_P5 = (
    A**6 - A**5*B - A**5 + A**4*B**2 - A**4*B - A**4
    + A**3*B**3 + 2*A**3*B - A**3 + A**2*B**4
    - A**2*B**3 + A**2*B - A**2 + A*B**5 + A*B**3
    - A*B**2 + A - B**6 + B**5 - B**4 + B**3 - B**2 + B - 1
)

EXPECTED_BERNSTEIN = [
    5,133,1698,13910,82399,376725,1384117,4197642,
    10704416,23257071,43465817,70393416,99410297,123226487,
    135272275,133373291,120803314,103699756,86971606,72046909,
    57843940,43349490,29180938,17091469,8475190,3457434,
    1117524,269891,43711,3641,13
]

def collision_polynomial(m):
    signs = [1] + [-1]*(m-2) + [1,1,1]
    assert len(signs) == m+2
    M, u = sp.eye(2), sp.zeros(2,1)
    for sigma in signs:
        u = Q[sigma]*u + sp.Matrix([C, 0])
        M = Q[sigma]*M
    numerator = -sp.expand(((sp.eye(2)-M).adjugate()*u)[1])
    polynomial, remainder = sp.div(numerator, C, A, B, domain='ZZ')
    assert remainder == 0
    return sp.expand(polynomial), sp.expand((sp.eye(2)-M).det())

P4, D4 = collision_polynomial(4)
P5, D5 = collision_polynomial(5)
assert sp.expand(P4-EXPECTED_P4)==0
assert sp.expand(P5-EXPECTED_P5)==0

R = sp.resultant(P4,P5,A)
assert sp.degree(R,B)==30
assert R.subs(B,0)==-5
assert R.subs(B,1)==-13

# For b=t/(1+t), (1+t)^30 * [-R(b)] = sum_k c_k t^k.
poly_t = sp.Poly(sp.cancel((1+T)**30*(-R.subs(B,T/(1+T)))),T)
coeff = [int(poly_t.nth(k)) for k in range(31)]
assert coeff == EXPECTED_BERNSTEIN
assert all(c>0 for c in coeff)

# Convex Bernstein combination gives an exact, uniform rational lower bound.
gaps = [sp.Rational(c,math.comb(30,k)) for k,c in enumerate(coeff)]
delta = min(gaps)
assert delta == sp.Rational(5252318,6322725)
assert gaps.index(delta)==16

print('VERIFIED: two affine-word collision polynomials')
print('VERIFIED: nonzero resultant, degree 30, with 31 positive coefficients')
print('VERIFIED: exact global gap -Res >= 5252318/6322725 on b in [0,1]')
print('VERIFIED: no common complex a root for any real b in [0,1]')
print('Proof scope: resultant identity and Bernstein positivity; no orbit-admissibility assertion.')
