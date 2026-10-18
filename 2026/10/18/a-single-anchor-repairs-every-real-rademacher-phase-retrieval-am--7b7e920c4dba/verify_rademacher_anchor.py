"""Finite exact checks of the sign-frame anchor criterion and ambiguity margin.

The finite checks test specified small dimensions; the accompanying proof treats all
finite dimensions and does not rely on exhaustive enumeration.
"""
from itertools import product
from fractions import Fraction
from math import sqrt


def rank(rows, d):
    a = [[Fraction(v) for v in row] for row in rows]
    pivot = 0
    for j in range(d):
        k = next((k for k in range(pivot, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        z = a[pivot][j]
        a[pivot] = [v / z for v in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                z = a[i][j]
                a[i] = [v - z * t for v, t in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == d:
            break
    return pivot


def projective_signs(d):
    return [(1,) + tail for tail in product((-1, 1), repeat=d-1)]


def complement_property(rows, d):
    # Exhaustive over all partitions for dimensions 2--4 only.
    m = len(rows)
    for mask in range(1 << m):
        left = [rows[i] for i in range(m) if mask & (1 << i)]
        right = [rows[i] for i in range(m) if not (mask & (1 << i))]
        if rank(left, d) < d and rank(right, d) < d:
            return False
    return True


def margin_for_ambiguous_pair(a, i, j, alpha, beta, sgn):
    d = len(a)
    u = [0.0] * d
    v = [0.0] * d
    u[i], u[j] = alpha, sgn * alpha
    v[i], v[j] = beta, -sgn * beta
    x = [ui + vi for ui, vi in zip(u, v)]
    y = [ui - vi for ui, vi in zip(u, v)]
    eps = list(product((-1, 1), repeat=d))
    assert all(abs(abs(sum(e[k]*x[k] for k in range(d))) -
                   abs(sum(e[k]*y[k] for k in range(d)))) < 1e-10 for e in eps)
    residual = abs(abs(sum(a[k]*x[k] for k in range(d))) -
                   abs(sum(a[k]*y[k] for k in range(d))))
    norm = lambda w: sqrt(sum(z*z for z in w))
    distance = min(norm([xi-yi for xi,yi in zip(x,y)]),
                   norm([xi+yi for xi,yi in zip(x,y)]))
    return residual / distance


def main():
    for d in (2, 3, 4):
        base = projective_signs(d)
        good = tuple(2**j for j in range(d))
        bad = (1, 1) + tuple(2**j for j in range(2, d))
        assert not complement_property(base, d)
        assert complement_property(base + [good], d)
        assert not complement_property(base + [bad], d)
        gap = min(abs(abs(good[i])-abs(good[j])) for i in range(d) for j in range(i+1,d))/sqrt(2)
        for i in range(d):
            for j in range(i+1,d):
                for sign in (-1, 1):
                    for alpha, beta in ((1,1),(1,2),(2,1),(-3,2)):
                        got=margin_for_ambiguous_pair(good,i,j,alpha,beta,sign)
                        assert got + 1e-9 >= gap, (d,i,j,got,gap)
        e_i, e_j = min(((i,j) for i in range(d) for j in range(i+1,d)),
                       key=lambda ij: abs(abs(good[ij[0]])-abs(good[ij[1]])))
        assert abs(margin_for_ambiguous_pair(good,e_i,e_j,1,1,1)-gap)<1e-9
        print(f'd={d}: finite complement partitions verified; exact margin attained ({gap:.12g})')
    print('PASS: all finite checks')


if __name__ == '__main__':
    main()
