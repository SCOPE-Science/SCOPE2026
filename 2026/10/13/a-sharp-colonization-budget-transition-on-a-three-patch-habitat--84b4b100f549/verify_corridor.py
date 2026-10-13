#!/usr/bin/env python3
"""Exact polynomial verification for a three-patch occupancy CTMC (Python stdlib only)."""
from functools import lru_cache
from fractions import Fraction
from itertools import product

# Sparse Z[x,y] polynomials, monomial key (x_degree,y_degree).
def const(n):
    return {} if not n else {(0, 0): int(n)}

def add(p, q):
    r = p.copy()
    for a, b in q.items():
        r[a] = r.get(a, 0) + b
        if not r[a]:
            del r[a]
    return r

def neg(p):
    return {k: -v for k, v in p.items()}

def sub(p, q):
    return add(p, neg(q))

def mul(p, q):
    r = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            e = (i+k, j+l)
            r[e] = r.get(e, 0) + a*b
    return {e: v for e, v in r.items() if v}

def prod(*args):
    r = const(1)
    for a in args:
        r = mul(r, a)
    return r

X = {(1, 0): 1}
Y = {(0, 1): 1}
ONE = const(1)
ZERO = {}
C = add(X, Y)
U = mul(X, Y)

# Positive-state indexing: 001, 010, 011, 100, 101, 110, 111.
STATES = list(range(1, 8))
IDX = {state: i for i, state in enumerate(STATES)}

def build_transient_matrix():
    q = [[ZERO for _ in STATES] for _ in STATES]
    for mask in STATES:
        i = IDX[mask]
        for v in range(3):
            if mask & (1 << v):
                after = mask ^ (1 << v)
                q[i][i] = add(q[i][i], ONE)
                if after:
                    q[i][IDX[after]] = sub(q[i][IDX[after]], ONE)
            else:
                for a, b, rate in ((0, 1, X), (1, 2, Y)):
                    if (v == a and mask & (1 << b)) or (v == b and mask & (1 << a)):
                        q[i][i] = add(q[i][i], rate)
                        q[i][IDX[mask | (1 << v)]] = sub(q[i][IDX[mask | (1 << v)]], rate)
    return q

def determinant(M):
    n = len(M)
    @lru_cache(None)
    def D(i, remaining):
        if i == n:
            assert not remaining
            return ONE
        ret = ZERO
        pos = 0
        for j in range(n):
            if remaining & (1 << j):
                term = mul(M[i][j], D(i+1, remaining ^ (1 << j)))
                ret = add(ret, term if pos % 2 == 0 else neg(term))
                pos += 1
        return ret
    return D(0, (1 << n) - 1)

q = build_transient_matrix()
det_q = determinant(q)
center_index = IDX[2]
q_center = [[(ONE if j == center_index else q[i][j]) for j in range(7)] for i in range(7)]
det_center = determinant(q_center)

A = add(add(prod(C, C), prod(const(7), C)), const(6))
B = add(A, prod(add(prod(const(2), C), const(7)), U))
N = prod(add(add(U, C), const(2)), add(prod(add(C, const(3)), U), A))

# Cramer's rule and the claimed closed form T_center=N/(2B).
assert det_q == prod(const(2), add(C, const(2)), B)
assert det_center == prod(add(C, const(2)), N)

# Exact verification of endpoint comparisons on a grid of rational rates.
def gauss(mat, rhs):
    a = [[Fraction(z) for z in row] + [Fraction(rhs[i])] for i, row in enumerate(mat)]
    n = len(a)
    for j in range(n):
        k = next(k for k in range(j, n) if a[k][j])
        a[j], a[k] = a[k], a[j]
        z = a[j][j]
        a[j] = [v / z for v in a[j]]
        for i in range(n):
            if i == j:
                continue
            z = a[i][j]
            if z:
                a[i] = [t - z * v for t, v in zip(a[i], a[j])]
    return [row[-1] for row in a]

def evalp(p, x, y):
    return sum(Fraction(v) * x**i * y**j for (i,j), v in p.items())

def solution(x, y):
    mat = [[evalp(z, x, y) for z in row] for row in q]
    return gauss(mat, [1]*7)[center_index]

def formula(x, y):
    c, u = x + y, x*y
    a = c*c + 7*c + 6
    return (u+c+2)*((c+3)*u+a) / (2*(a+(2*c+7)*u))

checks = 0
for x0, y0 in product(range(0, 8), repeat=2):
    x, y = Fraction(x0, 3), Fraction(y0, 5)
    assert solution(x,y) == formula(x,y)
    checks += 1

for c in [Fraction(1,8),Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(4),Fraction(10)]:
    concentrated = formula(c, Fraction(0))
    equal = formula(c/2, c/2)
    assert equal-concentrated == c*c*(c-1)/(8*(2*c+3))
    for j in range(101):
        x = c*Fraction(j,100)
        val = formula(x,c-x)
        assert val <= (equal if c >= 1 else concentrated)

print('VERIFY_OK polynomial_determinants=2 exact_CTMC_instances=%d exact_budget_grid=%d' % (checks,7*101))
