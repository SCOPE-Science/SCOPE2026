"""Exact-rational checks for correlated-noise leader-edge variance (stdlib only).

These finite checks corroborate but do not substitute for the mathematical proof.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random

checks = 0

def assert_eq(actual, expected):
    global checks
    assert actual == expected, (actual, expected)
    checks += 1

def assert_true(condition):
    global checks
    assert condition
    checks += 1

def inv(a):
    n = len(a)
    b = [[F(a[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        k = next(k for k in range(j, n) if b[k][j] != 0)
        b[j], b[k] = b[k], b[j]
        factor = b[j][j]
        b[j] = [x / factor for x in b[j]]
        for k in range(n):
            if k != j:
                factor = b[k][j]
                b[k] = [b[k][r] - factor * b[j][r] for r in range(2*n)]
    return [row[n:] for row in b]

def polar(a, q):
    g = inv(a)
    return sum((g[i][j] * q[i][j] for i in range(len(a)) for j in range(len(a))), F(0)) / 2

def covariance(b):
    n = len(b)
    return [[sum((F(b[i][k] * b[j][k]) for k in range(n)), F(0)) for j in range(n)] for i in range(n)]

def generated(rng, n, positive):
    s = [F(rng.randint(1, 4)) for _ in range(n)]
    a = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n): a[i][i] = s[i]
    for i, j in combinations(range(n), 2):
        w = F(rng.randint(0, 3))
        a[i][i] += w; a[j][j] += w
        a[i][j] -= w; a[j][i] -= w
    b = [[rng.randint(0, 3) if positive else rng.randint(-3, 3) for _ in range(n)] for _ in range(n)]
    q = covariance(b)
    t = [F(rng.randint(1, 3)) for _ in range(n)]
    return a, q, t

def with_edges(base, weights, mask):
    a = [row[:] for row in base]
    for i, w in enumerate(weights):
        if mask & (1 << i): a[i][i] += w
    return a

# Symmetric two-follower family: exact difference and sharp rho sign frontier.
for s in (F(1), F(2), F(5, 3)):
    for c in (F(1), F(2, 3), F(3)):
        for t in (F(1), F(2), F(5, 4)):
            a = [[s+c, -c], [-c, s+c]]
            A = 2*c*c + 2*c*s + c*t
            B = A + s*(s+t)
            denominator = s*(2*c+s)*(s+t)*(2*c+s+t)*(2*c*s+c*t+s*s+s*t)
            for rho in (F(-1), F(-4,5), F(-1,2), F(0), F(1,3), F(1)):
                q = [[F(1), rho], [rho, F(1)]]
                f = [polar(with_edges(a, [t,t], mask), q) for mask in range(4)]
                actual = f[0]+f[3]-f[1]-f[2]
                predicted = c*t*t*(A+rho*B)/denominator
                assert_eq(actual, predicted)
                assert_eq((actual > 0)-(actual < 0), (rho > -A/B)-(rho < -A/B))

q = [[F(1), F(-4,5)], [F(-4,5), F(1)]]
a = [[F(2), F(-1)], [F(-1), F(2)]]
f = [polar(with_edges(a, [F(1),F(1)], mask), q) for mask in range(4)]
assert_eq(f, [F(2,5),F(17,50),F(17,50),F(11,40)])
assert_eq(f[0]+f[3]-f[1]-f[2], F(-1,200))
assert_true(f[0]-f[1] < f[2]-f[3])
assert_eq(F(1)-F(16,25),F(9,25)) # covariance determinant is positive

# For nonnegative covariance, monotonicity and diminishing gains on many small graphs.
rng=Random(1044)
for positive in (True,False):
    for _ in range(160):
        n=rng.randint(2,4)
        a,q,t=generated(rng,n,positive)
        f=[polar(with_edges(a,t,mask),q) for mask in range(1<<n)]
        for mask in range(1<<n):
            for i in range(n):
                if not (mask & (1<<i)):
                    assert_true(f[mask] >= f[mask|(1<<i)])
                    if positive:
                        for j in range(n):
                            if i!=j and not (mask & (1<<j)):
                                assert_true(f[mask]+f[mask|(1<<i)|(1<<j)] >= f[mask|(1<<i)]+f[mask|(1<<j)])

print(f'{checks} exact-rational assertions passed')
