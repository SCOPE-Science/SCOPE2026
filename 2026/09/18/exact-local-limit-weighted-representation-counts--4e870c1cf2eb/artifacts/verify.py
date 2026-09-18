#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
from math import exp, pi, sqrt


def boundary_columns(k, T):
    q = []
    for s in range(k):
        n = next(n for n in range(T, T + k) if n % k == s)
        q.append((n - s) // k)
    cols = []
    for x in range(T + k):
        r = x % k
        cols.append(tuple((1 if x <= q[s] else 0) + (1 if r == s else 0)
                          for s in range(k)))
    return cols, q


def exact_count(k, T, c=0):
    states = {(0,) * k: 1}
    for v in boundary_columns(k, T)[0]:
        nxt = defaultdict(int)
        for z, mult in states.items():
            zp = tuple(z[i] + v[i] for i in range(k))
            zm = tuple(z[i] - v[i] for i in range(k))
            nxt[zp] += mult
            nxt[zm] += mult
        states = nxt
    return states.get((2 * c,) * k, 0)


def det_fraction(A):
    A = [row[:] for row in A]
    n = len(A)
    out = Fraction(1)
    for i in range(n):
        p = next(j for j in range(i, n) if A[j][i])
        if p != i:
            A[i], A[p] = A[p], A[i]
            out = -out
        piv = A[i][i]
        out *= piv
        for j in range(i + 1, n):
            if A[j][i]:
                f = A[j][i] / piv
                for h in range(i, n):
                    A[j][h] -= f * A[i][h]
    return out


def theoretical_covariance(k):
    return [[Fraction(k * (i == j) + (k + 2), k * k)
             for j in range(k)] for i in range(k)]


def C(k):
    return (8 * k / pi) ** (k / 2) / sqrt(k + 3)


def main():
    for k in range(2, 9):
        cov = theoretical_covariance(k)
        got = det_fraction(cov)
        want = Fraction(k + 3, k ** k)
        assert got == want, (k, got, want)
    print("covariance determinants: verified for k=2,...,8")

    for k in range(2, 9):
        for T in (97, 101, 113):
            cols, q = boundary_columns(k, T)
            sums = [sum(v[s] for v in cols) for s in range(k)]
            assert sums == [2 * (qq + 1) for qq in q]
            assert all(x % 2 == 0 for x in sums)
    print("boundary coefficient sums and even-lattice parity: verified")

    print("fixed-c normalized counts")
    for k, Ts in ((2, (40, 80, 160)), (3, (25, 40))):
        print(f"k={k}, predicted constant={C(k):.12f}")
        for T in Ts:
            n = exact_count(k, T, 0)
            scaled = n * (T ** (k / 2)) / (2 ** T)
            print(f"  T={T:3d}: scaled={scaled:.12f}")

    T = 160
    c = 6
    gamma = c / sqrt(T)
    n = exact_count(2, T, c)
    scaled = n * T / (2 ** T)
    prediction = C(2) * exp(-8 * gamma * gamma / 5)
    print("sqrt(T)-scale check for k=2")
    print(f"  T={T}, c={c}, scaled={scaled:.12f}, gaussian_prediction={prediction:.12f}")


if __name__ == "__main__":
    main()
