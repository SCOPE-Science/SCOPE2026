"""Exact rational checks for a six-bin exchangeable checkerboard copula."""
from fractions import Fraction as F
from itertools import combinations

N = 6
EPS = F(1, 100000)

def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def transpose(a):
    return [list(row) for row in zip(*a)]

def multiply(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]

def mean_step(i, n, strength=F(1)):
    a = identity(n)
    r = strength / 2
    a[i][i] = a[i+1][i+1] = 1-r
    a[i][i+1] = a[i+1][i] = r
    return a

def tp2(a):
    n = len(a)
    for i, j in combinations(range(n), 2):
        for k, l in combinations(range(n), 2):
            if a[i][k]*a[j][l] < a[i][l]*a[j][k]:
                return False
    return True

def doubly(a):
    return all(sum(row)==1 for row in a) and all(sum(row)==1 for row in transpose(a))

b = identity(4)
for i in (0, 2, 1, 2, 1):
    t = mean_step(i, 4)
    assert tp2(t)
    b = multiply(b, t)
a = multiply(transpose(b), b)
p = [[F(0) for _ in range(N)] for _ in range(N)]
for i in range(4):
    for j in range(4):
        p[i][j] = a[i][j]
for i in (4, 5):
    for j in (4, 5):
        p[i][j] = F(1, 2)
expected = [
    [32, 12, 12, 8, 0, 0],
    [12, 17, 17, 18, 0, 0],
    [12, 17, 17, 18, 0, 0],
    [8, 18, 18, 20, 0, 0],
    [0, 0, 0, 0, 32, 32],
    [0, 0, 0, 0, 32, 32],
]
assert p == [[F(v,64) for v in row] for row in expected]
assert doubly(p) and p == transpose(p) and tp2(p)
contrast = lambda m: m[1][2]-m[4][2]-m[1][3]+m[4][3]
assert contrast(p) == -F(1,64)

r = identity(N)
for k in range(5):
    for i in range(N-1):
        step = mean_step(i, N, EPS)
        assert tp2(step)
        r = multiply(r, step)
assert all(x > 0 for row in r for x in row)
assert tp2(r) and doubly(r)
positive = multiply(multiply(transpose(r), p), r)
assert all(x > 0 for row in positive for x in row)
assert doubly(positive) and positive == transpose(positive)
assert tp2(positive)
assert max(abs(positive[i][j] - p[i][j]) for i in range(N) for j in range(N)) <= 50*EPS
assert contrast(positive) < -F(1,64) + 200*EPS < 0
print('PASS: exact dyadic base, symmetric doubly stochastic, 225 TP2 minors')
print('PASS: 25-step strictly positive smoothing, 225 TP2 minors, uniform bounds')
print('Base density PMI contrast:', 6*contrast(p))
print('Smoothed density PMI contrast approximately:', float(6*contrast(positive)))
