"""Exact short-window covariance certificates; Python 3 standard library."""
from fractions import Fraction as Q
from math import comb


def multiply(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def check():
    expected = {
        2: (1, [1], 1), 3: (Q(4, 3), [1, 0, 1], 1),
        4: (Q(1, 2), [3, -2, 5, 1, 3], Q(5, 2)),
        5: (Q(4, 5), [2, -3, 3, 1, 4, 1, 2], Q(23, 20)),
        6: (Q(1, 3), [5, -12, 5, -1, 14, 5, 11, 3, 5], Q(11, 56)),
    }
    for n, (scale, power, minimum) in expected.items():
        counts = [[sum(abs(j-i) == k for j in range(n))
                   for k in range(n)] for i in range(n)]
        h = [[[n*(abs(j-i) == k)-counts[i][k] for k in range(n)]
              for j in range(n)] for i in range(n)]  # polynomial n H a_i
        total = [0] * (2*n)
        for i in range(n-1):
            for a, b in zip(h[i], h[i+1]):
                delta = [u-v for u, v in zip(a, b)]
                for k, x in enumerate(multiply(delta, delta)):
                    total[k] += x
                for s in (a, b):
                    for k, x in enumerate(multiply(s, s)):
                        total[k] -= x
                        total[k+1] += x
        assert total == [n*n*scale*v for v in multiply([1, -1, -1, 1], power)]
        d = len(power) - 1
        bernstein = [sum(power[j]*Q(comb(k, j), comb(d, j))
                         for j in range(k+1)) for k in range(d+1)]
        assert min(bernstein) == minimum > 0
        print(f'n={n}: exact factorization; min Bernstein coefficient = {minimum}')


if __name__ == '__main__':
    check()
