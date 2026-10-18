#!/usr/bin/env python3
"""Reproducible graded linear-algebra checks for full-binary-form Jacobian quotients.

Only standard Python is needed. Finite modular calculations corroborate the
symbolic all-degree module presentation but do not replace its proof.
"""
from itertools import combinations
from math import comb


def monomials(n, degree):
    if n == 1:
        yield (degree,)
        return
    for first in range(degree + 1):
        for tail in monomials(n - 1, degree - first):
            yield (first,) + tail


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def generators(m):
    n = m + 3  # x_0,...,x_m,u,v
    U, V = m + 1, m + 2
    out = []
    for j in range(m + 1):
        e = [0] * n
        e[U], e[V] = m - j, j
        out.append({tuple(e): 1})
    d_u = {}
    d_v = {}
    for j in range(m):
        e = [0] * n
        e[j] = 1
        e[U], e[V] = m - j - 1, j
        d_u[tuple(e)] = m - j
    for j in range(1, m + 1):
        e = [0] * n
        e[j] = 1
        e[U], e[V] = m - j, j - 1
        d_v[tuple(e)] = j
    return out + [d_u, d_v]


def rank_ideal_degree(m, degree, prime):
    n = m + 3
    basis = list(monomials(n, degree))
    column = {exp: j for j, exp in enumerate(basis)}
    gen = generators(m)
    pivots = {}
    if degree >= m:
        for factor in monomials(n, degree - m):
            for g in gen:
                row = {column[plus(factor, exp)]: coef % prime
                       for exp, coef in g.items()}
                while row:
                    col = min(row)
                    v = row[col]
                    if v == 0:
                        del row[col]
                        continue
                    if col not in pivots:
                        inv = pow(v, -1, prime)
                        pivots[col] = {c: (t * inv) % prime
                                       for c, t in row.items() if t % prime}
                        break
                    sub = pivots[col]
                    for c, t in sub.items():
                        q = (row.get(c, 0) - v * t) % prime
                        if q:
                            row[c] = q
                        elif c in row:
                            del row[c]
    return len(basis) - len(pivots)


def expected(m, degree):
    return sum((r + 1) * comb(degree - r + m, m)
               for r in range(min(degree, m - 1) + 1)) - \
           (2 * comb(degree, m) if degree >= m else 0)


def check_derivative_matrix(m):
    # Its 2x2 minor using rows 0,1 is nonzero as a polynomial in x_i.
    # Specialization (x_0,x_1,x_2)=(1,0,1) makes it nonzero.
    # Rank-one locus is the Veronese rational normal curve:
    # x_j=binom(m,j)a^(m-j)b^j.
    for a, b in [(1, 1), (1, 2), (2, 1), (1, 3)]:
        x = [comb(m, j) * a ** (m - j) * b ** j
             for j in range(m + 1)]
        rows = [((m - j) * x[j], (j + 1) * x[j + 1])
                for j in range(m)]
        assert all(p * rows[0][1] == q * rows[0][0]
                   for p, q in rows)
    x = [1, 0, 1] + [0] * (m - 2)
    rows = [((m - j) * x[j], (j + 1) * x[j + 1])
            for j in range(m)]
    assert rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0] != 0


def main():
    checks = 0
    for m in (3, 4, 5):
        check_derivative_matrix(m)
        checks += 1
        for d in range(m, m + 4):
            target = expected(m, d)
            for p in (1000003, 1000033):
                got = rank_ideal_degree(m, d, p)
                assert got == target, (m, d, p, got, target)
                checks += 1
            print('m=%d d=%d Hilbert=%d' % (m, d, target))
    print('VERIFY_OK', checks)


if __name__ == '__main__':
    main()
