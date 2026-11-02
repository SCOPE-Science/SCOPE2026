#!/usr/bin/env python3
"""Reproduce numerical checks for the sharp weighted commutator constant of rank-one Hermitian matrices.

The symbolic proof is in RESULT.md. These floating-point checks are not an infinite-domain certificate.
"""
import cmath
import math
import random


def critical_overlap(a, b):
    if not (0 < a <= b):
        raise ValueError('positive eigenvalues in ascending order required')
    s, delta = a + b, b - a
    lo, hi = 0.0, 1.0
    for _ in range(90):
        t = (lo + hi) / 2
        f = s * (1 - 2 * t * t) + delta * t**3
        if f > 0:
            lo = t
        else:
            hi = t
    return (lo + hi) / 2


def sharp(a, b):
    t = critical_overlap(a, b)
    return 8 * t * t * (1 - t * t) / ((a + b) - (b - a) * t)**2


def conjugate_dot(u, v):
    return sum(x.conjugate() * y for x, y in zip(u, v))


def rankone(u):
    return [[z * w.conjugate() for w in u] for z in u]


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def ratio(u, v, eig):
    x, y = rankone(u), rankone(v)
    xy, yx = matmul(x, y), matmul(y, x)
    num = sum(abs(xy[i][j] - yx[i][j])**2 for i in range(len(eig)) for j in range(len(eig)))
    xu = sum(w * abs(z)**2 for z, w in zip(u, eig))
    yv = sum(w * abs(z)**2 for z, w in zip(v, eig))
    return num / (xu * yv)


def unit_random(n, gen):
    u = [complex(gen.gauss(0, 1), gen.gauss(0, 1)) for _ in range(n)]
    norm = math.sqrt(sum(abs(z)**2 for z in u))
    return [z/norm for z in u]


def equality_vectors(t, n):
    u = [0j] * n
    v = [0j] * n
    u[0] = v[0] = math.sqrt((1 + t)/2)
    u[1] = math.sqrt((1 - t)/2)
    v[1] = -u[1]
    return u, v


def main():
    gen = random.Random(237528)
    cases = [[1., 1.], [1., 2.], [1., 5.], [1., 100.], [0.25, 8.], [2., 3.], [1., 2., 5.], [1., 4., 8., 9.]]
    for eig in cases:
        a, b = eig[:2]
        t = critical_overlap(a, b)
        delta = (b-a)/(b+a)
        assert delta < t < 1
        C = sharp(a,b)
        u, v = equality_vectors(t, len(eig))
        eq = ratio(u, v, eig)
        assert abs(eq/C - 1) < 2e-12, (eig, eq, C)
        assert abs( C/(2/(a*b)) - (3*t*t-t**4-1)) < 2e-12
        for _ in range(2200):
            x, y = unit_random(len(eig), gen), unit_random(len(eig), gen)
            actual = ratio(x, y, eig)
            assert actual <= C * (1+2e-12), (eig, actual, C)
        print('CHECK', eig, 't*=%.12f'%t, 'C=%.12f'%C, 'equality=%.12f'%eq)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
