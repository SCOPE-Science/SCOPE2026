"""Recovery test: certifies target obstruction for lane-672 (stdlib + sympy)."""
import sympy
from sympy import binomial
q = sympy.Symbol('q')

# 1. Unrefined LGV matrix A_ij = binom(i+j, 2j-i)
def b(a, k):
    if k < 0 or k > a:
        return 0
    return int(binomial(a, k))
def det_int(n, f):
    return sympy.Matrix([[f(i, j) for j in range(n)] for i in range(n)]).det()
unref = [det_int(n, lambda i, j: b(i + j, 2 * j - i)) for n in [1, 2, 3, 4]]
assert unref == [1, 2, 11, 170], unref
print('unrefined dets n=1..4:', unref)

# 2. q-binomials by two independent paths
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
for n in range(6):
    for k in range(n + 1):
        assert sympy.expand(qb_div(n, k) - qb_rec(n, k)) == 0, (n, k)
print('q-binomial paths agree to n=5')

def E(i, j, qbf):
    K = 2 * j - i
    if K < 0 or K > i + j:
        return sympy.Integer(0)
    return sympy.expand(q**(K * (K - 1) // 2) * qbf(i + j, K))
D4a = sympy.expand(sympy.Matrix([[E(i, j, qb_div) for j in range(4)] for i in range(4)]).det())
D4b = sympy.expand(sympy.Matrix([[E(i, j, qb_rec) for j in range(4)] for i in range(4)]).det())
assert D4a == D4b
S = sympy.expand(D4a / q**4)
print('D4 =', D4a)
print('S  =', S)
assert S.subs(q, 1) == 170
Q9 = sympy.Poly(S, q).quo(sympy.Poly((q + 1) * (q**4 + q**3 + q**2 + q + 1), q)).as_expr()
Q9 = sympy.expand(Q9)
print('Q9 =', Q9)
assert Q9.subs(q, 1) == 17
assert len(sympy.factor_list(Q9)[1]) == 1
assert Q9.subs(q, -1) == -7 and Q9.subs(q, 0) == 1  # real root in (-1,0)
p = sympy.Poly(S, q)
c = p.all_coeffs()[::-1]
assert not all(c[k] == c[14 - k] for k in range(15))  # non-reciprocal
print('Q9 ZZ-irreducible, non-cyclotomic (root in (-1,0)), S non-reciprocal: OK')

# 3. Integer cross-check at q=2
def qfact_val(n, v):
    p = 1
    for k in range(1, n + 1):
        p *= sum(v**j for j in range(k))
    return p
def qb_val(n, k, v):
    if k < 0 or k > n:
        return 0
    return qfact_val(n, v) // (qfact_val(k, v) * qfact_val(n - k, v))
def Ev(i, j, v):
    K = 2 * j - i
    if K < 0 or K > i + j:
        return 0
    return v**(K * (K - 1) // 2) * qb_val(i + j, K, v)
M2 = sympy.Matrix([[Ev(i, j, 2) for j in range(4)] for i in range(4)])
assert M2.det() == 2069808 and S.subs(q, 2) == 129363
from fractions import Fraction
num = den = 1
for i in range(4):
    num *= sum(2**j for j in range(3 * i + 1)) * qfact_val(6 * i, 2) * qfact_val(2 * i, 2)
    den *= qfact_val(4 * i + 1, 2) * qfact_val(4 * i, 2)
assert Fraction(num, den) == Fraction(114783149724712029, 85) != M2.det()
print('q=2: D4=2069808, S=129363=3*31*1391, naive-R=114783149724712029/85: mismatch certified')
print('RECOVERY_OK')
