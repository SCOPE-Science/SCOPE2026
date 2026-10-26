"""Exact finite checks for bipartite biregular pairing multigraph cycle covariance."""
from itertools import permutations
from fractions import Fraction
from math import comb, factorial


def falling(t, k):
    product = 1
    for i in range(k):
        product *= t - i
    return product


def exhaustive(n, m, d, e):
    L = n * d
    assert L == m * e and L <= 8 and n >= 2 and m >= 2
    left = [i // d for i in range(L)]
    right = [j // e for j in range(L)]
    sx = sy = sxy = 0
    for matching in permutations(range(L)):
        counts = [[0] * m for _ in range(n)]
        for u, v in enumerate(matching):
            counts[left[u]][right[v]] += 1
        x = sum(k * (k - 1) // 2 for row in counts for k in row)
        y = sum(
            counts[i][j] * counts[i][k] * counts[h][j] * counts[h][k]
            for i in range(n) for h in range(i + 1, n)
            for j in range(m) for k in range(j + 1, m)
        )
        sx += x
        sy += y
        sxy += x * y
    population = factorial(L)
    return (
        Fraction(sx, population), Fraction(sy, population),
        Fraction(sxy, population) - Fraction(sx * sy, population * population)
    )


def predicted(n, m, d, e):
    L = n * d
    assert L == m * e
    ex = Fraction(L * (d - 1) * (e - 1), 2 * (L - 1))
    ey = Fraction(comb(n, 2) * comb(m, 2) * falling(d, 2)**2 * falling(e, 2)**2,
                  falling(L, 4))
    if min(d, e) == 1:
        return ex, ey, Fraction(0)
    if L == 4:
        return ex, ey, Fraction(-4, 9)
    p = (d + e - 4) * L**2 - (3*d*e - 11) * L + 6*d*e - 4*d - 4*e - 4
    return ex, ey, -ey * Fraction(2*p, (L-5)*(L-4)*(L-1))


def main():
    cases = [(2,2,2,2), (3,3,2,2), (4,4,2,2), (2,3,3,2),
             (3,2,2,3), (2,2,3,3), (2,4,4,2)]
    for args in cases:
        actual = exhaustive(*args)
        expected = predicted(*args)
        assert actual == expected, (args, actual, expected)
        print('PASS', args, 'EX=',actual[0], 'EY=',actual[1], 'COV=',actual[2])

if __name__ == '__main__':
    main()
