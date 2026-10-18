"""Reproduce finite checks for a one-defect cycle Poisson stability law.

The exact part uses rational arithmetic and matrix inversion implemented separately from the rank-one identity.
The large-order part checks numerical behavior but does not prove limits.
Run: python CHECK.py
"""
from fractions import Fraction as F
from math import isclose


def matrix_inverse(a):
    n = len(a)
    aug = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        scale = aug[k][k]
        aug[k] = [z / scale for z in aug[k]]
        for i in range(n):
            if i == k:
                continue
            scale = aug[i][k]
            if scale:
                aug[i] = [a - scale * b for a, b in zip(aug[i], aug[k])]
    return [row[n:] for row in aug]


def graph_green_direct(n, w):
    l = [[F(0) for _ in range(n)] for _ in range(n)]
    for k in range(n):
        j = (k + 1) % n
        a = w if k == n - 1 else F(1)
        l[k][k] += a
        l[j][j] += a
        l[k][j] -= a
        l[j][k] -= a
    mat = [[l[i][j] + F(1, n) for j in range(n)] for i in range(n)]
    inverse = matrix_inverse(mat)
    return [[inverse[i][j] - F(1, n) for j in range(n)] for i in range(n)]


def graph_green_rank_one(n, w):
    delta = F(n) * (1 - w) / (1 + (n - 1) * w)
    v = [F(n - 1 - 2 * i, 2 * n) for i in range(n)]
    return [[F(n*n - 1, 12*n) - F(((i-j)%n) * (n-((i-j)%n)), 2*n)
             + delta * v[i] * v[j] for j in range(n)] for i in range(n)]


def row_norm(row):
    med = sorted(row)[len(row)//2]
    return sum(abs(z-med) for z in row)


def norm_from_rank(n, w):
    delta = n*(1-w)/(1+(n-1)*w)
    v = [(n-1-2*i)/(2*n) for i in range(n)]
    g = [(n*n-1)/(12*n) - d*(n-d)/(2*n) for d in range(n)]
    best = 0.
    ix = []
    for i in range(n):
        row = [g[(i-j)%n] + delta*v[i]*v[j] for j in range(n)]
        z = row_norm(row)
        if z > best + 1e-9:
            best, ix = z, [i]
        elif abs(z-best) < 1e-9:
            ix.append(i)
    return best, ix


def homogeneous_value(n):
    f = F(n*n, 32)
    r = n % 4
    return f + (F(0) if r == 0 else F(1, 8) if r == 2
                else F(n-2, 32*n) if r == 1 else F(n+2, 32*n))


def check():
    assertions = 0
    for n in range(3, 12):
        for w in (F(1, 4), F(1, 2), F(1), F(3, 2), F(3), F(7)):
            a = graph_green_direct(n, w)
            b = graph_green_rank_one(n, w)
            assert a == b
            assertions += n * n
            assert all(sum(row) == 0 for row in b)
            assertions += n
            for row in b:
                score = row_norm(row)
                ordered = sorted(range(n), key=lambda i: row[i])
                f = [F(0)] * n
                for i in ordered[:n//2]:
                    f[i] = -F(1)
                for i in ordered[n - n//2:]:
                    f[i] = F(1)
                assert sum(f) == 0 and max(abs(z) for z in f) <= 1
                assert sum(z*f[j] for j,z in enumerate(row)) == score
                assertions += 2
            if w == 1:
                assert row_norm(b[0]) == homogeneous_value(n)
                assertions += 1
    for n in range(3, 101):
        b, _ = norm_from_rank(n, 1.)
        assert abs(b - float(homogeneous_value(n))) < 1e-8
        assertions += 1
    for w in (0.2, 0.5, 2., 8.):
        target = max((1-w)/w, 0.) / 16
        for n in (64, 128, 256, 512):
            base, _ = norm_from_rank(n, 1.)
            val, loc = norm_from_rank(n, w)
            observed = (val-base)/n
            assert abs(observed-target) < 0.03
            assertions += 1
            if w < 1 and n >= 128:
                assert min(min(abs(i/n-.25),abs(i/n-.75)) for i in loc) < 0.045
                assertions += 1
    print(f"PASS: {assertions} exact/numerical consistency assertions")
    print("The checks do not establish asymptotic statements or historical priority.")

if __name__ == '__main__':
    check()
