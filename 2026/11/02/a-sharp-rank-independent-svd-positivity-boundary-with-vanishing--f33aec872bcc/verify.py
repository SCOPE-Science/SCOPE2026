"""Exact rational checks for a compound-symmetric nonnegative SVD theorem.

Python 3 standard library only. Finite checks test constructed examples;
they are not a replacement for the theorem's general proof.
"""
from fractions import Fraction as F


def zero(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    a = zero(n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def add(a, b, x=F(1), y=F(1)):
    return [[x * a[i][j] + y * b[i][j]
             for j in range(len(a))] for i in range(len(a))]


def scale(a, s):
    return [[s * z for z in row] for row in a]


def mm(a, b):
    n = len(a)
    return [[sum((a[i][h] * b[h][j] for h in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def fnormsq(a):
    return sum((v * v for row in a for v in row), F(0))


def witness(n, r):
    """Orthogonal projector of rank r-1 in the constant-vector complement."""
    k = r - 1
    p = zero(n)
    p[0][0] = p[1][1] = F(1, 2)
    p[0][1] = p[1][0] = F(-1, 2)
    for i in range(2, k + 2):
        for j in range(2, k + 2):
            p[i][j] += F(int(i == j)) - F(1, k)
    return p


def partition_projector(n, r):
    q = zero(n)
    groups = [[i] for i in range(r - 1)] + [list(range(r - 1, n))]
    for group in groups:
        for i in group:
            for j in group:
                q[i][j] = F(1, len(group))
    return q


def check_case(n, r):
    alpha = F(1)
    beta = F(n - 2, 4)  # strictly below threshold (n-2)/2
    epsilon = beta / n
    ident, ones = eye(n), [[F(1, n) for _ in range(n)] for _ in range(n)]
    p, q = witness(n, r), partition_projector(n, r)
    k = r - 1
    assert mm(p, p) == p and mm(q, q) == q
    assert sum(p[i][i] for i in range(n)) == k
    assert sum(q[i][i] for i in range(n)) == r
    assert all(sum(row) == 0 for row in p)
    assert all(sum(row) == 1 for row in q)
    assert p[0][1] == -F(1, 2)
    assert all(-F(1, 2) <= p[i][j] <= F(1, 2)
               for i in range(n) for j in range(n) if i != j)
    a = add(scale(ident, alpha), scale(ones, beta))
    b = add(scale(ones, alpha + beta), scale(p, alpha))
    c = add(scale(q, alpha), scale(ones, beta))
    assert fnormsq(add(a, b, F(1), F(-1))) == alpha * alpha * (n - r)
    assert fnormsq(add(a, c, F(1), F(-1))) == alpha * alpha * (n - r)
    assert min(min(row) for row in c) > 0
    # Explicit rank-r nonnegative factorization from the group indicators.
    groups = [[i] for i in range(r - 1)] + [list(range(r - 1, n))]
    h = [[F(int(a == b), len(groups[a])) + beta / n
          for b in range(r)] for a in range(r)]
    assert all(z >= 0 for row in h for z in row)
    c_factored = [[h[next(a for a, g in enumerate(groups) if i in g)]
                       [next(b for b, g in enumerate(groups) if j in g)]
                   for j in range(n)] for i in range(n)]
    assert c == c_factored
    delta = alpha / 2 - (alpha + beta) / n
    assert delta > 0 and b[0][1] == -delta
    ap = add(a, scale(p, epsilon))
    bp = add(scale(ones, alpha + beta), scale(p, alpha + epsilon))
    assert min(min(row) for row in ap) > 0
    assert bp[0][1] == -delta - epsilon / 2
    assert fnormsq(add(ap, bp, F(1), F(-1))) == alpha * alpha * (n - r)
    assert fnormsq(add(ap, a, F(1), F(-1))) == epsilon * epsilon * k


if __name__ == "__main__":
    count = 0
    for n in range(3, 11):
        for r in range(2, n):
            check_case(n, r)
            count += 1
    n, r, alpha, beta, epsilon = 3, 2, F(1), F(1, 4), F(1, 12)
    p = witness(n, r)
    b12 = (alpha + beta) / n + (alpha + epsilon) * p[0][1]
    assert b12 == F(-1, 8)
    print(f"PASS: {count} exact-rational dimension/rank cases and the 3x3 illustration")
