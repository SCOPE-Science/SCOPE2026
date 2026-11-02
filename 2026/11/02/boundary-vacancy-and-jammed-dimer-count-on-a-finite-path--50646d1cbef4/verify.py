#!/usr/bin/env python3
"""Independent finite checks for the boundary-vacancy/dimer-count identity.

Standard-library exact arithmetic. Finite verification complements the proof
and is not an infinite-range certificate.
"""
from fractions import Fraction as Q
from math import factorial
from itertools import permutations


def recurrences(top):
    u, a, c = [[Q(0)] * (top + 1) for _ in range(3)]
    u[1] = Q(1)
    for n in range(2, top + 1):
        a[n] = Q(n - 1 + 2 * sum(a[:n - 1]), n - 1)
        u[n] = Q(sum(u[1:n - 1]), n - 1)
        c[n] = Q(sum(c[j] + u[j] * (1 + a[n - j - 2])
                     for j in range(1, n - 1)), n - 1)
    return u, a, c


def epart(m, t):
    return sum((Q(t ** j, factorial(j)) for j in range(m + 1)), Q(0))


def tpart(m, t):
    return sum((Q((m + 1 - j) * t ** j, factorial(j))
                for j in range(m + 1)), Q(0))


def coefficients(n):
    return (epart(n - 1, -1),
            Q(n - tpart(n - 1, -2), 2),
            (tpart(n - 1, -1) - tpart(n - 2, -1)
             + 2 * tpart(n - 3, -1) - tpart(n - 1, -3)
             - tpart(n - 2, -3)) / 4)


def exhaustive(n):
    # Orderings of all n-1 attempted edges, with equal probability.
    counts = [0, 0, 0]
    for order in permutations(range(n - 1)):
        covered = [False] * n
        dimers = 0
        for k in order:
            if not covered[k] and not covered[k + 1]:
                covered[k] = covered[k + 1] = True
                dimers += 1
        vacant = int(not covered[0])
        counts[0] += vacant
        counts[1] += dimers
        counts[2] += vacant * dimers
    denominator = factorial(n - 1)
    return tuple(Q(z, denominator) for z in counts)


def tail_upper(m, z):
    # For the infinite tail sum_{j=m}^infty z^j/j!; m+1 > z.
    assert m + 1 > z
    return Q(z ** m, factorial(m)) * Q(m + 1, m + 1 - z)


def main():
    assertions = 0
    u, a, c = recurrences(150)
    assert (u[1], a[1], c[1]) == (1, 0, 0)
    assertions += 1
    for n in range(1, 151):
        assert (u[n], a[n], c[n]) == coefficients(n)
        assertions += 3
    for n in range(2, 9):
        assert (u[n], a[n], c[n]) == exhaustive(n)
        assertions += 3
    zeros = {2, 3, 5}
    for n in range(2, 151):
        covariance = c[n] - u[n] * a[n]
        assert covariance == 0 if n in zeros else covariance < 0
        assertions += 1
    exact_values = {
        4: Q(-2, 9), 5: Q(0), 6: Q(-77, 450),
        7: Q(-91, 1296), 8: Q(-1751, 14700),
        9: Q(-25651, 259200),
    }
    for n, expected in exact_values.items():
        assert c[n] - u[n] * a[n] == expected
        assertions += 1
    n = 10
    bound = ((tail_upper(n, 1) + tail_upper(n-1, 1)
              + 2*tail_upper(n-2, 1) + 3*tail_upper(n-1, 3)
              + 3*tail_upper(n, 3))/4
             + tail_upper(n, 2)
             + tail_upper(n, 1)*(Q(n, 2) + 1 + tail_upper(n, 2)))
    assert bound == Q(5574423318619, 74071065600000)
    assertions += 1
    assert bound < Q(1, 12)
    assertions += 1
    print(f'PASS: {assertions} exact assertions; exhaustive edge orders for n=2..8;')
    print('closed coefficients checked against first-edge recurrences through n=150;')
    print('negative/zero signs checked through n=150; rational tail bound at n=10 passed.')
    print('These finite checks are not an exhaustive proof of the infinite sign theorem.')


if __name__ == '__main__':
    main()
