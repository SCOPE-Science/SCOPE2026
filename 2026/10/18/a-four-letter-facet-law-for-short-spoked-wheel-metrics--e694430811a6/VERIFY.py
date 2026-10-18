#!/usr/bin/env python3
"""Exact checks for the unit Lipschitz ball of a uniformly weighted metric wheel.

Requires Python's standard library only.  No numerical tolerance is used.
The proof of the theorem is analytic; finite checks supplement that proof.
"""
from fractions import Fraction as F
from itertools import combinations, product

SYMBOLS = 'AaBb'


def permitted(x, y):
    return (x, y) not in [('A', 'B'), ('B', 'A')]


def good_word(w):
    n = len(w)
    return all(permitted(w[i], w[(i + 1) % n]) and
               (w[i] != 'a' or w[(i - 1) % n] == 'A' or w[(i + 1) % n] == 'A') and
               (w[i] != 'b' or w[(i - 1) % n] == 'B' or w[(i + 1) % n] == 'B')
               for i in range(n))


def matrix_multiply(X, Y):
    rows, inner, cols = len(X), len(Y), len(Y[0])
    assert len(X[0]) == inner
    return [[sum(X[i][k] * Y[k][j] for k in range(inner))
             for j in range(cols)] for i in range(rows)]


def transfer_matrix():
    pairs = [(x, y) for x in SYMBOLS for y in SYMBOLS if permitted(x, y)]
    T = [[int(y == u and (y != 'a' or x == 'A' or v == 'A')
              and (y != 'b' or x == 'B' or v == 'B'))
          for u, v in pairs] for x, y in pairs]
    return pairs, T


def traces_and_charpoly(T):
    n = len(T)
    P = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = []
    for k in range(1, n + 1):
        P = matrix_multiply(P, T)
        traces.append(sum(P[i][i] for i in range(n)))
    # Newton identities: det(z I - T) = sum_{k=0}^n c_k z^(n-k).
    coeff = [1]
    for k in range(1, n + 1):
        num = -sum(coeff[k - j] * traces[j - 1] for j in range(1, k + 1))
        assert num % k == 0, ('nonintegral char coefficient', k, num)
        coeff.append(num // k)
    return traces, coeff


def direct_word_count(n):
    return sum(good_word(word) for word in product(SYMBOLS, repeat=n))


def halfspaces(m, radius):
    # Inequalities a dot x <= b.
    inequalities = []
    for i in range(m):
        e = [0] * m
        e[i] = 1
        inequalities.append((tuple(e), radius))
        inequalities.append((tuple(-v for v in e), radius))
        e = [0] * m
        e[i] = 1
        e[(i + 1) % m] = -1
        inequalities.append((tuple(e), F(1)))
        inequalities.append((tuple(-v for v in e), F(1)))
    return inequalities


def solve_square(system):
    n = len(system)
    a = [[F(x) for x in row] + [F(y)] for row, y in system]
    for j in range(n):
        row = next((i for i in range(j, n) if a[i][j]), None)
        if row is None:
            return None
        a[j], a[row] = a[row], a[j]
        divisor = a[j][j]
        a[j] = [u / divisor for u in a[j]]
        for i in range(n):
            if i != j:
                factor = a[i][j]
                if factor:
                    a[i] = [a[i][k] - factor * a[j][k] for k in range(n+1)]
    return tuple(a[i][n] for i in range(n))


def enumerate_by_active_bases(n, r):
    inequalities = halfspaces(n, r)
    found = set()
    for indices in combinations(range(len(inequalities)), n):
        x = solve_square([inequalities[i] for i in indices])
        if x is not None and all(sum(a[i] * x[i] for i in range(n)) <= b
                                 for a, b in inequalities):
            found.add(x)
    return found


def expected_points(n, radius):
    values = {'A': radius, 'a': radius - 1,
              'B': -radius, 'b': 1 - radius}
    return {tuple(values[t] for t in w)
            for w in product(SYMBOLS, repeat=n) if good_word(w)}


def unweighted_count(n):
    # D'Ali--Delucchi--Michalek, Proposition 4.22:
    # disallow neighboring +/- and runs of three zeros.
    return sum(all((w[i], w[(i + 1) % n]) not in [('A', 'B'), ('B', 'A')]
                   and not (w[i] == w[(i + 1) % n] == w[(i + 2) % n] == 'z')
                   for i in range(n))
               for w in product('ABz', repeat=n))


def main():
    pairs, T = transfer_matrix()
    assert len(pairs) == 14
    traces, coeff = traces_and_charpoly(T)
    # Product z^9 (z^2-z+1)(z^3-z^2-3z-2).
    # Descending-order coefficients, including trailing zeros.
    expected = [1, -2, -1, 0, -1, -2] + [0] * 9
    assert coeff == expected, (coeff, expected)
    # Cayley-Hamilton identity is checked via the exact char polynomial.
    for n in range(3, 9):
        assert direct_word_count(n) == traces[n - 1], n
    assert [traces[n-1] for n in range(3, 11)] == [14, 38, 102, 252, 632, 1582, 3974, 9986]
    # Exact independent vertex enumeration by arbitrary active constraint bases.
    # This does not assume the four-letter classification.
    for n in (3, 4, 5):
        r = F(3, 4)
        points = enumerate_by_active_bases(n, r)
        assert points == expected_points(n, r), (n, len(points), len(expected_points(n, r)))
        assert len(points) == traces[n - 1]
    # At the lower endpoint every spoke bound is tight at a cube vertex.
    for n in range(3, 6):
        if n <= 4:
            assert len(enumerate_by_active_bases(n, F(1, 2))) == 2 ** n
        # The upper endpoint is the known unweighted wheel polytope.
        if n <= 5:
            assert len(enumerate_by_active_bases(n, F(1))) == unweighted_count(n)
    assert [unweighted_count(n) for n in range(3, 10)] == [14, 26, 62, 138, 310, 706, 1598]
    print('VERIFY_OK: exact 14-state transfer, characteristic polynomial, cyclic words,')
    print('independent rational active-basis enumeration, and endpoint comparisons.')


if __name__ == '__main__':
    main()
