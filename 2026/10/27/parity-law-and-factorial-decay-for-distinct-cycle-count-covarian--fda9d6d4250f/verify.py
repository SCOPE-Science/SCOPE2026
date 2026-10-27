"""Standalone exact checks for the covariance-sign theorem on uniform derangements."""
from fractions import Fraction
from math import factorial
from itertools import permutations


def partials(n):
    out = [Fraction(1)]
    for k in range(1, n + 1):
        out.append(out[-1] + Fraction((-1) ** k, factorial(k)))
    return out


def covariance(n, j, k, a):
    r = n - j - k
    return (a[n] * a[r] - a[n-j] * a[n-k]) / (j*k*a[n]*a[n])


def cycle_counts(p):
    n = len(p)
    seen = [False] * n
    out = [0] * (n + 1)
    for i in range(n):
        if not seen[i]:
            v, size = i, 0
            while not seen[v]:
                seen[v] = True
                v = p[v]
                size += 1
            out[size] += 1
    return out


def main():
    tests = 0
    maxn = 80
    a = partials(maxn)
    for n in range(5, maxn + 1):
        for j in range(2, n):
            for k in range(j + 1, n - j + 1):
                r = n - j - k
                c = covariance(n, j, k, a)
                assert c and (c > 0) == (r % 2 == 0), (n,j,k,c)
                tests += 1
    # Direct exhaustive sample-space check, not a replacement for the proof.
    exhaustive = 0
    for n in range(5, 9):
        counts = []
        for p in permutations(range(n)):
            if all(p[i] != i for i in range(n)):
                counts.append(cycle_counts(p))
        den = len(counts)
        assert den == factorial(n) * a[n]
        for j in range(2, n):
            for k in range(j + 1, n - j + 1):
                mj = Fraction(sum(z[j] for z in counts), den)
                mk = Fraction(sum(z[k] for z in counts), den)
                cross = Fraction(sum(z[j]*z[k] for z in counts), den)
                assert cross - mj*mk == covariance(n,j,k,a)
                exhaustive += 1
    for n in (5,6,7,8,9):
        print(f'n={n}, j=2, k=3, covariance={covariance(n,2,3,a)}')
    print(f'PASS: {tests} exact signs through n={maxn}; {exhaustive} exhaustive joint-moment comparisons on n=5..8')

if __name__ == '__main__':
    main()
