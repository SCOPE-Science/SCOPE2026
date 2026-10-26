"""Exact rational checks for the cyclic second-difference embedding formulas.

This finite checker is diagnostic; the theorem for arbitrary cycle order
uses an analytic Green-kernel computation and a cited isoperimetric theorem.
"""
from fractions import Fraction
from itertools import combinations


def green(n, d):
    d = d % n
    h = d * (n - d)
    c = Fraction(n**4 + 10*n*n - 11, 720*n)
    return c - Fraction(h, 12*n) - Fraction(h*h, 24*n)


def laplace(v):
    n = len(v)
    return [2*v[j] - v[(j-1) % n] - v[(j+1) % n] for j in range(n)]


def energy(n, pos):
    b = set(pos)
    sigma = [1 if j in b else -1 for j in range(n)]
    return sum((Fraction(sigma[j] * sigma[k])*green(n, j-k)
                for j in range(n) for k in range(n)), Fraction(0))


def target(n):
    m = n // 2
    h = m*(n-m)
    return Fraction(h*(2*h*h+(n*n+15)*h+24), 180*n)


def main():
    tested = 0
    for n in range(3, 61):
        v = [green(n,d) for d in range(n)]
        assert sum(v) == 0
        tested += 1
        ll = laplace(laplace(v))
        for j in range(n):
            assert ll[j] == (Fraction(n-1,n) if j==0 else Fraction(-1,n))
            tested += 1
        assert energy(n, range(n//2)) == target(n)
        tested += 1
        for d in range(1,n//2+1):
            assert green(n,d)<green(n,d-1)
            tested += 1
    for n in range(3,14):
        best = max(energy(n, a) for mask in range(1<<n)
                   for a in [tuple(j for j in range(n) if mask & (1<<j))])
        assert best == target(n)
        tested += 1
    print('PASS: %d exact rational checks; all subsets tested for 3 <= n <= 13.' % tested)


if __name__ == '__main__':
    main()
