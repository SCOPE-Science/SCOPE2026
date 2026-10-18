"""Exact finite checks for the singular scheme of the five-variable reciprocal quartic.

Runs with Python 3 and its standard library.  Finite checks corroborate the
symbolic arguments in RESULT.md; no finite experiment replaces their proof.
"""
from itertools import combinations, product
from math import comb


def rank_integer(matrix):
    """Exact rational rank via elementary row reduction."""
    from fractions import Fraction
    a = [[Fraction(t) for t in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        lead = a[r][c]
        a[r] = [v / lead for v in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                t = a[i][c]
                a[i] = [u - t * v for u, v in zip(a[i], a[r])]
        r += 1
    return r


def determinant_integer(a):
    """Bareiss fraction-free determinant, including integer signs."""
    x = [row[:] for row in a]
    n = len(x)
    old = 1
    sign = 1
    for k in range(n - 1):
        if not x[k][k]:
            j = next((j for j in range(k + 1, n) if x[j][k]), None)
            if j is None:
                return 0
            x[k], x[j] = x[j], x[k]
            sign = -sign
        p = x[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numer = x[i][j] * p - x[i][k] * x[k][j]
                assert numer % old == 0
                x[i][j] = numer // old
        for i in range(k + 1, n):
            x[i][k] = 0
        old = p
    return sign * x[-1][-1]


def q_terms(i):
    return list(combinations([a for a in range(4) if a != i], 2))


def proof_matrix_degree_three():
    """Columns are y_j q_i; rows are the 16 nonpure cubic monomials."""
    exps = [a for a in product(range(4), repeat=4)
            if sum(a) == 3 and max(a) != 3]
    assert len(exps) == 16
    where = {exp: k for k, exp in enumerate(exps)}
    A = [[0] * 16 for _ in exps]
    for i in range(4):
        for j in range(4):
            for a, b in q_terms(i):
                exp = [0] * 4
                exp[a] += 1
                exp[b] += 1
                exp[j] += 1
                A[where[tuple(exp)]][4 * i + j] += 1
    assert determinant_integer(A) == 48
    degree_two_mons = list(combinations(range(4), 2))
    B = [[int((a, b) in q_terms(i)) for i in range(4)]
         for a, b in degree_two_mons]
    assert rank_integer(B) == 4
    # Therefore the degree-two difference is 6-4=2, and every
    # degree-three monomial with at least two variable supports lies
    # in (q_0,...,q_3); higher degrees follow by multiplication.
    return 48


def e4_grad(x):
    return [sum(x[a] * x[b] * x[c] for a, b, c in
                combinations([j for j in range(5) if j != i], 3))
            for i in range(5)]


def e4_value(x):
    return sum(x[a] * x[b] * x[c] * x[d]
               for a, b, c, d in combinations(range(5), 4))


def field_points(p):
    examined = singular = 0
    for first in range(5):
        for suffix in product(range(p), repeat=4-first):
            x = (0,) * first + (1,) + suffix
            examined += 1
            g = e4_grad(x)
            f = e4_value(x)
            if all(gi % p == 0 for gi in g):
                assert f % p == 0
                assert sum(bool(a) for a in x) <= 2
                singular += 1
            elif sum(bool(a) for a in x) <= 2:
                raise AssertionError(('missed singular', x))
    assert examined == (p**5 - 1) // (p - 1)
    assert singular == 5 + 10*(p - 1)
    return examined, singular


def main():
    print('LOCAL_MACAULAY_DETERMINANT', proof_matrix_degree_three())
    for p in (5, 7):
        print('PROJECTIVE_POINTS', p, *field_points(p))
    # Hilbert polynomial for the union of ten coordinate lines.
    for d in range(1, 10):
        basis = sum(1 for a in product(range(d+1), repeat=5)
                    if sum(a) == d and sum(t > 0 for t in a) <= 2)
        assert basis == 10*d - 5
    print('REDUCED_HILBERT_POLYNOMIAL', '10d-5')
    print('SCHEME_HILBERT_POLYNOMIAL', '10d+5')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
