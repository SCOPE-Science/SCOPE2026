#!/usr/bin/env python3
"""Exact-arithmetic verifier for the four-cycle centered maximal L2 constant.

Uses only the Python standard library. Every one of the 3**4 ball-choice
matrices is tested; no sampled configurations or floating-point comparisons.
"""
from fractions import Fraction as F
from itertools import product, permutations
from collections import Counter

N = 4
ZERO = F(0)
ONE = F(1)


def average_row(vertex, radius):
    if radius == 0:
        entries = [vertex]
    elif radius == 1:
        entries = [(vertex - 1) % N, vertex, (vertex + 1) % N]
    elif radius == 2:
        entries = list(range(N))
    else:
        raise ValueError('radius must be 0,1,2')
    return [F(int(j in entries), len(entries)) for j in range(N)]


def choice_matrix(choice):
    return [average_row(v, choice[v]) for v in range(N)]


def gram(matrix):
    return [[sum((matrix[k][i] * matrix[k][j] for k in range(N)), ZERO)
             for j in range(N)] for i in range(N)]


def determinant(matrix):
    n = len(matrix)
    acc = ZERO
    for perm in permutations(range(n)):
        inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = ONE
        for i in range(n):
            term *= matrix[i][perm[i]]
        acc += -term if inv % 2 else term
    return acc


def leading_minors_above(matrix, rational_bound):
    for k in range(1, N + 1):
        principal = [[(rational_bound if i == j else ZERO)-matrix[i][j]
                      for j in range(k)] for i in range(k)]
        if determinant(principal) <= 0:
            return False
    return True


def polynomial_coefficients(matrix):
    # Determinant det(t I - B) by multilinearity, evaluated through the
    # principal-minor formula: coefficient of t**(4-k) is (-1)**k
    # times the sum of all k-by-k principal minors of B.
    from itertools import combinations
    coefficients = []
    for k in range(N + 1):
        total = ZERO
        for subset in combinations(range(N), k):
            minor = [[matrix[i][j] for j in subset] for i in subset]
            total += determinant(minor)
        coefficients.append((-1 if k % 2 else 1)*total)
    return coefficients


def main():
    # The global second-best spectral square is below 29/20. This
    # is checked, not assumed, using 79 exact rational PSD tests.
    small_bound = F(29, 20)
    exceptional = []
    count = 0
    category_counts = Counter()
    for choice in product(range(3), repeat=N):
        B = gram(choice_matrix(choice))
        if leading_minors_above(B, small_bound):
            category_counts[sum(c == 2 for c in choice)] += 1
        else:
            exceptional.append(choice)
        count += 1
    assert count == 81
    assert exceptional == [(0, 1, 0, 1), (1, 0, 1, 0)], exceptional
    assert sum(category_counts.values()) == 79

    witness = gram(choice_matrix((1, 0, 1, 0)))
    assert witness == [
        [F(1,9), F(1,9), ZERO, F(1,9)],
        [F(1,9), F(11,9), F(1,9), F(2,9)],
        [ZERO, F(1,9), F(1,9), F(1,9)],
        [F(1,9), F(2,9), F(1,9), F(11,9)],
    ]
    # det(t I - B)=(t-1)(9t-1)(9t^2-14t+1)/81.
    assert polynomial_coefficients(witness) == [
        ONE, -F(8,3), F(158,81), -F(8,27), F(1,81)
    ], polynomial_coefficients(witness)

    # For s=sqrt(10), the vector (1,3+s,1,3+s) is a strictly
    # positive eigenvector with eigenvalue (7+2s)/9.
    # Store each coordinate as (rational_part, coefficient_of_s).
    vec = [(ONE, ZERO), (F(3), ONE), (ONE, ZERO), (F(3), ONE)]
    eigenvalue = (F(7,9), F(2,9))
    for i in range(N):
        got = tuple(sum((witness[i][j]*vec[j][k] for j in range(N)), ZERO)
                    for k in range(2))
        a, b = eigenvalue
        c, d = vec[i]
        expected = (a*c + 10*b*d, a*d + b*c)
        assert got == expected, (i, got, expected)
    # Certified rational inequality 29/20 < (7+2sqrt(10))/9.
    # Equivalent to 40 sqrt(10)>121, hence 16000>14641.
    assert 40*40*10 > 121*121
    # Verify strict ball dominance for the extremizer:
    # low vertices: radius1 best; high vertices: radius0 best.
    for i, chosen in enumerate((1, 0, 1, 0)):
        values = [tuple(sum((average_row(i,r)[j]*vec[j][k] for j in range(N)),ZERO)
                        for k in range(2)) for r in range(3)]
        # All differences a + b sqrt(10) here have either a,b>=0,
        # or can be checked directly by squared rational comparison.
        def positive(pair):
            a,b=pair
            if b==0:return a>0
            if b>0:return (a>=0) or (10*b*b>a*a)
            return (a>0 and a*a>10*b*b)
        for r in range(3):
            if r != chosen:
                assert positive(tuple(values[chosen][k]-values[r][k]
                                      for k in range(2))), (i,r,values)
    print('EXACT_CHECK_OK; checked=81; rational-PSD=79; exceptional=2;')
    print('exceptions=(0,1,0,1),(1,0,1,0); coefficient and eigenvector checks passed')
    print('rational-PSD-by-number-of-global-balls=' + repr(dict(category_counts)))

if __name__ == '__main__':
    main()
