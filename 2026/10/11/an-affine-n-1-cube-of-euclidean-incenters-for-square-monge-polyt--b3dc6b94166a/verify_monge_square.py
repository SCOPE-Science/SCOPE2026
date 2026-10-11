#!/usr/bin/env python3
"""Exact standard-library checks for the square Monge-polytope center formula.

Finite checks corroborate the printed all-dimensional proof; they do not
independently prove the theorem in arbitrarily large dimension.
"""
from fractions import Fraction
from itertools import permutations, product


def baseline(i, j):
    z = j - i
    return z * (z - 1) // 2


def matrix(n, bits):
    # delta[k] is u[k]-u[k+1] for zero-indexed rows.
    u = [0] * n
    for k in range(n - 2, -1, -1):
        u[k] = u[k + 1] + bits[k]
    return [[baseline(i, j) + u[i] - u[j] for j in range(n)] for i in range(n)]


def slack(A, i, j):
    return A[i][j + 1] + A[i + 1][j] - A[i][j] - A[i + 1][j + 1]


def run():
    count = 0
    for n in range(2, 11):
        base = [[baseline(i, j) for j in range(n)] for i in range(n)]
        T = Fraction(n * n * (n * n - 1), 12)
        assert sum(map(sum, base)) == T
        assert all(slack(base, i, j) == 1 for i in range(n - 1) for j in range(n - 1))
        for bits in product((0, 1), repeat=n - 1):
            D = matrix(n, bits)
            assert min(map(min, D)) == 0
            assert sum(map(sum, D)) == T
            assert all(slack(D, i, j) == 1 for i in range(n - 1) for j in range(n - 1))
            zeroes = sum(x == 0 for row in D for x in row)
            assert zeroes == 2 * n - 1
            count += 1
        # Fraction-valued interior cube point; tangency count exactly n.
        D = matrix(n, (Fraction(1, 2),) * (n - 1))
        assert sum(map(sum, D)) == T
        assert sum(x == 0 for row in D for x in row) == n
        if n <= 6:
            # In the equality case E=u_i-u_j, every assignment has sum zero.
            for perm in permutations(range(n)):
                assert sum(D[i][perm[i]] - base[i][perm[i]] for i in range(n)) == 0
    print(f'VERIFY_OK square-monge n=2..10 cube_vertices={count} exact_T=yes mixed_slacks=yes tangencies=yes assignments_n<=6=yes')


if __name__ == '__main__':
    run()
