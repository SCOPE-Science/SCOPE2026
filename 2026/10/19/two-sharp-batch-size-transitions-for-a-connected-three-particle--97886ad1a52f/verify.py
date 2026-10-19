#!/usr/bin/env python3
"""Exact rational and polynomial checks for three-particle batch-reset cumulants.

Requires Python 3.10+ and SymPy. The unbounded assertions use exact
polynomial coefficient positivity; finite enumerations are auxiliary checks.
"""
from fractions import Fraction
from sympy import symbols, factor, expand, Poly, cancel, prod

n, m, t, u = symbols('n m t u', integer=True)
H = 3*n*n - 3*n*m - 6*n + m*m + 3*m + 2
T = 2*n*m - n - m*m - 2*m + 2
H3 = 3*n*n - 15*n + 20
V = cancel(2*n**3*(m-1)*T/(m**3*(2*n-m-1)*H))

# Independent reconstruction from the stationary generator on products of
# distinct squared positions. In units of the single-particle reset rate,
# q_j is the probability a batch hits at least one of j labels.
q = [None] + [factor(1-prod((n-m-j)/(n-j) for j in range(i)))
               for i in range(1, 4)]
A1 = 1/q[1]
A2 = 2/(q[1]*q[2])
A3 = 6/(q[1]*q[2]*q[3])
assert factor(A3 - 3*A2*A1 + 2*A1**3 - V) == 0

# The direct comparison of the three-batch optimum with a general batch
# cancels to a positive denominator and (m-3)*B(n,m).
C = expand((5*n-13)*m**3*(2*n-m-1)*H
           - 27*(n-2)*H3*(m-1)*T)
B = cancel(C/(m-3))
assert B.is_polynomial(m, n)
assert expand(C - (m-3)*B) == 0
assert factor(V.subs(m, 3)-V -
    2*n**3*(m-3)*B/
    (27*(n-2)*H3*m**3*(2*n-m-1)*H)) == 0

# For 4<=m<=7 and n>=10, B has strictly positive coefficients when n=10+t.
small_coefficients = {
    4: [219, 4701, 34290, 90480, 40320],
    5: [417, 8607, 60663, 158325, 87420],
    6: [675, 13149, 86634, 208080, 100512],
    7: [993, 18057, 109005, 231315, 82926],
}
for mm, expected in small_coefficients.items():
    coeffs = Poly(expand(B.subs({n:10+t, m:mm})), t).all_coeffs()
    assert [int(v) for v in coeffs] == expected
    assert all(v>0 for v in coeffs)

# For m>=8 and n>=m+2, use m=8+t, n=10+t+u. All coefficients positive.
big = Poly(expand(B.subs({m:8+t,n:10+t+u})), t, u)
assert len(big.terms()) == 25
assert all(v>0 for powers,v in big.terms())
coefficient_certificate = {
    (6,0):5,
    (5,1):30,(5,0):201,
    (4,2):70,(4,1):1005,(4,0):3241,
    (3,3):75,(3,2):1904,(3,1):13044,(3,0):26299,
    (2,4):30,(2,3):1545,(2,2):18989,(2,1):80709,(2,0):108534,
    (1,4):408,(1,3):10446,(1,2):81541,(1,1):230736,(1,0):191264,
    (0,4):1371,(0,3):23061,(0,2):125178,(0,1):225600,(0,0):49536,
}
assert {powers:int(v) for powers,v in big.terms()} == coefficient_certificate

# Exact endpoint identities and polynomial-positive comparisons.
assert factor(V.subs(m,n)-2) == 0
assert factor(V.subs(m,n-1)-(2+2/(n-1)**3)) == 0
P5 = 5*n**5-89*n**4+508*n**3-1306*n**2+1620*n-810
assert factor(V.subs(m,3)-V.subs(m,n-1)-
    2*n*(n-4)*P5/(27*(n-2)*(n-1)**3*H3)) == 0
assert Poly(expand(P5.subs(n,10+t)),t).all_coeffs() == [5,161,1948,10534,21900,2790]
assert factor(V.subs(m,3)-V.subs(m,n)-
    2*(n-3)*(5*n**3-79*n**2+330*n-360)/(27*(n-2)*H3)) == 0
assert all(x>0 for x in Poly(expand((5*n**3-79*n**2+330*n-360).subs(n,10+t)),t).all_coeffs())
assert factor(V.subs(m,3)-V.subs(m,2)+
    n**3*(n*n-77*n+228)/(108*(n-2)*(2*n-3)*H3)) == 0

# The remaining 3<=n<=9 cases are finite exact comparisons.
expected_small = {3:2,4:3,5:4,6:5,7:6,8:7,9:8}
for nn, best in expected_small.items():
    vals = [(factor(V.subs({n:nn,m:mm})),mm) for mm in range(1,nn+1)]
    assert max(vals)[1] == best
    assert len({v for v,j in vals if v==max(vals)[0]}) == 1

# Independent exact rational enumeration (sanity check, not an infinite proof).
def rational_V(nn, mm):
    hh=3*nn*nn-3*nn*mm-6*nn+mm*mm+3*mm+2
    tt=2*nn*mm-nn-mm*mm-2*mm+2
    return Fraction(2*nn**3*(mm-1)*tt, mm**3*(2*nn-mm-1)*hh)
for nn in range(3,151):
    vals=[rational_V(nn,mm) for mm in range(1,nn+1)]
    best=(nn-1 if nn<=9 else (3 if nn<=73 else 2))
    assert vals.index(max(vals))+1 == best
    assert vals.count(max(vals)) == 1
print('PASS: generator moments, exact all-size positivity certificates, endpoint comparisons, and N<=150 checks')
