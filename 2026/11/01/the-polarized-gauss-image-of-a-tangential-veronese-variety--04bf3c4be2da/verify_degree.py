"""Exact arithmetic checks for polarized Gauss-image degree identities."""
from math import comb
from fractions import Fraction


def hilbert(n, d, m):
    a = (2*n + 1)*(d - 2)
    b = n
    A = a + b
    z = Fraction(m*a + 1)
    for j in range(3, n + 2):
        z *= Fraction(m*A + j - 1, j - 1)
        z *= Fraction(m*b + j - 2, j - 2)
    return z


def degree(n, d):
    a = (2*n + 1)*(d - 2)
    b = n
    A = a + b
    return comb(2*n - 1, n) * a * (A**(n-1)) * (b**(n-1))


def check():
    count = 0
    for n in range(2, 8):
        for d in range(3, 10):
            r = 2*n - 1
            a = (2*n + 1)*(d - 2)
            b = n
            A = a + b
            finite_difference = sum(
                (-1)**(r - j)*comb(r, j)*hilbert(n, d, j)
                for j in range(r + 1)
            )
            bundle_pushforward = (
                comb(r, n-1)*A**n*b**(n-1)
                - comb(r, n)*A**(n-1)*b**n
            )
            assert finite_difference == bundle_pushforward == degree(n, d)
            assert all(hilbert(n, d, m).denominator == 1 for m in range(5))
            count += 1
    assert degree(2, 3) == 210
    assert degree(2, 4) == 720
    assert degree(3, 3) == 63000
    print('VERIFY_OK', count, 'exact degree tests')


if __name__ == '__main__':
    check()
