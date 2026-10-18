"""Exact rational checks for positivity horizons of theta steps on complete multipartite Laplacians.

Python 3 standard library only. Finite tests supplement, and do not replace,
the all-orders projector and inverse-positive proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement


def inverse(A):
    n = len(A)
    M = [list(A[i]) + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if M[i][k])
        M[k], M[pivot] = M[pivot], M[k]
        z = M[k][k]
        M[k] = [a / z for a in M[k]]
        for i in range(n):
            if i == k:
                continue
            z = M[i][k]
            if z:
                M[i] = [M[i][j] - z * M[k][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def partitions(N, minimum=2):
    if N == 0:
        yield ()
    else:
        for p in range(minimum, N + 1):
            for rest in partitions(N - p, p):
                yield (p,) + rest


def laplacian(parts):
    n = sum(parts)
    classes = sum(([i] * size for i, size in enumerate(parts)), [])
    return [[F(n - parts[classes[i]]) if i == j else
             F(-1 if classes[i] != classes[j] else 0)
             for j in range(n)] for i in range(n)]


def step(L, theta, h):
    n = len(L)
    if theta == 0:
        return [[F(int(i == j)) - h * L[i][j]
                 for j in range(n)] for i in range(n)]
    A = [[F(int(i == j)) + theta * h * L[i][j]
          for j in range(n)] for i in range(n)]
    R = inverse(A)
    return [[(R[i][j] - (1 - theta) * F(int(i == j))) / theta
             for j in range(n)] for i in range(n)], R


def diag_return(n, p, t):
    return (F(1, n) + F(p - 1, p) / (1 + (n - p) * t)
            + F(n - p, n * p) / (1 + n * t))


def run():
    checks = 0
    thetas = [F(0), F(1, 5), F(1, 2), F(2, 3), F(3, 4), F(9, 10), F(1)]
    steps = [F(0), F(1, 7), F(1, 2), F(1), F(3, 2), F(3), F(7)]
    for n in range(4, 11):
        for parts in partitions(n):
            if len(parts) < 2:
                continue
            L = laplacian(parts)
            labels = sum(([p] * p for p in parts), [])
            s = min(parts)
            for theta in thetas:
                for h in steps:
                    if theta == 0:
                        T = step(L, theta, h)
                    else:
                        T, R = step(L, theta, h)
                        for i, p in enumerate(labels):
                            assert R[i][i] == diag_return(n, p, theta * h)
                            checks += 1
                    actual = all(T[i][j] >= 0 for i in range(n) for j in range(n))
                    if theta >= F(n - 1, n):
                        predicted = True
                    else:
                        A = (n - s) * (n * (1 - theta) - 1)
                        B = theta * (2*n - s) - (n - s)
                        predicted = 1 + B*h - A*theta*h*h >= 0
                    assert actual == predicted, (n, parts, theta, h, actual, predicted)
                    checks += 1
                    assert all(sum(row) == 1 for row in T)
                    checks += 1
                    if h > 0 and theta > 0:
                        for i, p in enumerate(labels):
                            for j, q in enumerate(labels):
                                if p < q:
                                    assert R[i][i] < R[j][j]
                                    checks += 1
    print(f'VERIFY_OK {checks} exact rational assertions')


if __name__ == '__main__':
    run()
