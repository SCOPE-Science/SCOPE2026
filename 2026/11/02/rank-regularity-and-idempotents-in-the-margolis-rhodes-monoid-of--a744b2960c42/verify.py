#!/usr/bin/env python3
"""Independent finite checks of simplex-preimage continuity on labeled star graphs."""
from collections import Counter
from itertools import product
from math import comb, factorial


def fall(n, k):
    z = 1
    for j in range(k):
        z *= n - j
    return z


def formulas(m):
    P, E, N = Counter(), Counter(), Counter()
    for j in range(m + 1):
        P[j] += comb(m, j) * fall(m + 1, j)
    P[1] += 2*m
    for j in range(m + 1):
        P[j + 1] += comb(m, j) * fall(m, j)
    P[2] += m*m
    for j in range(m):
        P[j + 1] += m*m * comb(m - 1, j) * fall(m - 1, j)
    for j in range(m + 2):
        E[j] += comb(m + 1, j)
    E[1] += m
    for j in range(m):
        E[j + 1] += m * comb(m - 1, j)
    for j in range(2, m + 1):
        N[j] += comb(m, j) * comb(m, j - 1) * factorial(j)
    return P, E, N


def continuous(f, m):
    n = m + 1
    face = {frozenset()}
    face.update(frozenset([v]) for v in range(n))
    face.update(frozenset([0, v]) for v in range(1, n))
    fibers = [frozenset(i for i, value in enumerate(f) if value == v)
              for v in range(n)]
    return all(a in face for a in fibers) and all(
        fibers[0].union(fibers[v]) in face for v in range(1, n))


def check(m, check_regular):
    n = m + 1
    P, E, R = Counter(), Counter(), Counter()
    for f in product(range(-1, n), repeat=n):
        if not continuous(f, m):
            continue
        image = sorted(set(f) - {-1})
        rank = len(image)
        P[rank] += 1
        # f^2 = f iff every image point is defined and fixed.
        if all(f[v] == v for v in image):
            E[rank] += 1
        if check_regular:
            fibers = [tuple(i for i, a in enumerate(f) if a == v) for v in image]
            # f g f = f iff a continuous section on the image exists.
            for section in product(*fibers):
                g = [-1] * n
                for x, y in zip(image, section):
                    g[x] = y
                if continuous(g, m):
                    R[rank] += 1
                    break
    expected_P, expected_E, expected_N = formulas(m)
    assert P == expected_P, (m, 'all', P, expected_P)
    assert E == expected_E, (m, 'idempotent', E, expected_E)
    if check_regular:
        assert Counter({j: P[j] - R[j] for j in range(m + 2) if P[j] > R[j]}) == expected_N, (m, 'nonregular', P, R, expected_N)
    print('m=%d maps=%d idempotents=%d regular=%s verified' % (
        m, sum(P.values()), sum(E.values()), str(sum(R.values())) if check_regular else 'not brute-checked'))


def main():
    for m in range(1, 7):
        check(m, m <= 5)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
