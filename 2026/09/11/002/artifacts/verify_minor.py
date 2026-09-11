"""Fallback-core certificate: principal 3x3 minor obstruction (stdlib + sympy).

Replays the exact preset-fallback binary test's second conjunct for the
leading principal 3x3 minor (indices 0,1,2) of the area-weighted CSTCPP LGV
matrix E_ij = q^{C(K,2)} qBinom(i+j,K), K = 2j-i, and certifies it cannot
equal any Andrews-type closed q-integer product Q3.
"""
import sympy
from sympy import binomial

q = sympy.Symbol('q')


def qnum(n):
    return sum(q**k for k in range(n)) if n > 0 else (sympy.Integer(1) if n == 0 else sympy.Integer(0))


def qfact(n):
    p = sympy.Integer(1)
    for k in range(1, n + 1):
        p = sympy.expand(p * qnum(k))
    return p


def qb_div(n, k):
    if k < 0 or k > n:
        return sympy.Integer(0)
    num = qfact(n)
    den = sympy.expand(qfact(k) * qfact(n - k))
    quot, rem = sympy.div(sympy.Poly(num, q), sympy.Poly(den, q))
    assert rem.is_zero, (n, k)
    return quot.as_expr()


def qb_rec(n, k):
    if k < 0 or k > n:
        return sympy.Integer(0)
    if k == 0 or k == n:
        return sympy.Integer(1)
    return sympy.expand(qb_rec(n - 1, k - 1) + q**k * qb_rec(n - 1, k))


def E(i, j, qbf):
    K = 2 * j - i
    if K < 0 or K > i + j:
        return sympy.Integer(0)
    return sympy.expand(q**(K * (K - 1) // 2) * qbf(i + j, K))


# Explicit logged entries of the leading principal 3x3 minor
M3 = sympy.Matrix([[E(i, j, qb_div) for j in range(3)] for i in range(3)])
print('M3 =')
print(M3)
assert M3[0, 0] == 1 and M3[0, 1] == 0 and M3[0, 2] == 0
assert M3[1, 1] == q + 1 and M3[1, 2] == q**3 and M3[2, 1] == 1

d_a = sympy.expand(M3.det())
d_b = sympy.expand(sympy.Matrix([[E(i, j, qb_rec) for j in range(3)] for i in range(3)]).det())
assert d_a == d_b  # two independent q-binomial code paths agree
print('det(3x3) =', d_a)
assert d_a == q**6 + 2 * q**5 + 3 * q**4 + 2 * q**3 + 2 * q**2 + q
assert d_a.subs(q, 1) == 11  # q=1 = unrefined CSTCPP n=3 count

S3 = sympy.expand(d_a / q)
print('S3 =', S3)
assert S3 == q**5 + 2 * q**4 + 3 * q**3 + 2 * q**2 + 2 * q + 1
assert S3.subs(q, 1) == 11

# (i) ZZ-irreducible: singleton factor list over ZZ
fl = sympy.factor_list(S3)
print('factor_list ZZ:', fl)
assert len(fl[1]) == 1 and fl[1][0][1] == 1 and sympy.Poly(fl[1][0][0], q).degree() == 5

# (ii) q-integer-product sign lemma: [n]_{-1} is 1 (n odd) or 0 (n even),
# so any product of q-integers is >= 0 at q=-1; S3(-1) = -1 forbids it.
assert S3.subs(q, -1) == -1 and S3.subs(q, 0) == 1
print('S3(-1) = -1, S3(0) = 1: not a q-integer product; real root in (-1,0)')

# (iii) Non-reciprocal: ascending coeffs [1,2,2,3,2,1] vs reverse
c = sympy.Poly(S3, q).all_coeffs()[::-1]
assert list(c) == [1, 2, 2, 3, 2, 1]
assert c[2] != c[3]
print('non-reciprocal (c2=2 vs c3=3): not a reciprocal Andrews-type product')

# (iv) Prime specialization S3(2) = 101
assert S3.subs(q, 2) == 101 and sympy.isprime(101)
print('S3(2) = 101 prime')

# (v) Naive n=3 q-analog of the DLMF product is not the partner
def qfact_val(n, v):
    p = 1
    for k in range(1, n + 1):
        p *= sum(v**j for j in range(k))
    return p


from fractions import Fraction
num = den = 1
for i in range(3):
    num *= sum(2**j for j in range(3 * i + 1)) * qfact_val(6 * i, 2) * qfact_val(2 * i, 2)
    den *= qfact_val(4 * i + 1, 2) * qfact_val(4 * i, 2)
assert Fraction(num, den) == Fraction(2634489, 17) != d_a.subs(q, 2) == 202
print('naive-R3(2) = 2634489/17 vs det(2) = 202: mismatch certified')

# (vi) Shift robustness: q^{a*C(K,2)+b*i+c*j}, all 8 (a,b,c) in {0,1}^3
def Es(i, j, a, b, c):
    K = 2 * j - i
    if K < 0 or K > i + j:
        return sympy.Integer(0)
    return sympy.expand(q**(a * (K * (K - 1) // 2) + b * i + c * j) * qb_div(i + j, K))


for a in [0, 1]:
    for b in [0, 1]:
        for c_ in [0, 1]:
            d = sympy.expand(sympy.Matrix([[Es(i, j, a, b, c_) for j in range(3)]
                                           for i in range(3)]).det())
            S = sympy.expand(d / q**min(k[0] for k in sympy.Poly(d, q).as_dict()))
            assert S.subs(q, 1) == 11
            assert len(sympy.factor_list(S)[1]) == 1  # stays irreducible/non-product
print('shift robustness (8/8 monomial shifts keep irreducible non-product cofactor): OK')
print('VERIFY_MINOR_OK')
