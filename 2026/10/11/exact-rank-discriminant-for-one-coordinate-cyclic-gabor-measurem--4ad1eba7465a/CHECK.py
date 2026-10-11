#!/usr/bin/env python3
"""Direct finite-dimensional spot checks for a one-defect cyclic Gabor rank formula.
The symbolic proof is in RESULT.md; floating-point rank checks do not replace it.
Only the Python standard library is required.
"""
import cmath
import math


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def phi(n):
    return sum(math.gcd(j, n) == 1 for j in range(1, n + 1))


def congruence_count(n, r):
    r %= n
    return sum(d * phi(n // d) for d in divisors(math.gcd(n, r)) if d < n) - (n - 1 if r == 0 else 0)


def rank_predicted(n, z, tol=1e-9):
    if abs(z - 1) < tol:
        return n
    zeros = (n - 1) * int(abs(abs(z) - 1) < tol)
    zeros += (n - 1) * int(abs(2 * z.real + n - 2) < tol)
    c = -(z - 1) / (z.conjugate() - 1)
    for r in range(n):
        if abs(c - cmath.exp(2j * math.pi * r / n)) < tol:
            zeros += congruence_count(n, r)
            break
    return n * n - zeros


def matrix_rank(matrix, tol=1e-8):
    arr = [row[:] for row in matrix]
    m, n = len(arr), len(arr[0])
    rank = 0
    for col in range(n):
        if rank == m:
            break
        pivot = max(range(rank, m), key=lambda r: abs(arr[r][col]))
        if abs(arr[pivot][col]) <= tol:
            continue
        arr[rank], arr[pivot] = arr[pivot], arr[rank]
        value = arr[rank][col]
        for j in range(col, n):
            arr[rank][j] /= value
        for row in range(rank + 1, m):
            v = arr[row][col]
            if v:
                for j in range(col, n):
                    arr[row][j] -= v * arr[rank][j]
        rank += 1
    return rank


def rank_direct(n, z):
    g = [z] + [1 + 0j] * (n - 1)
    rows = []
    for a in range(n):
        for b in range(n):
            v = [cmath.exp(2j * math.pi * b * x / n) * g[(x - a) % n] for x in range(n)]
            rows.append([v[x] * v[y].conjugate() for x in range(n) for y in range(n)])
    return matrix_rank(rows)


def main():
    tested = 0
    for n in range(3, 11):
        for r in range(n):
            exact = congruence_count(n, r)
            enumerated = sum((a * b - r) % n == 0 for a in range(1, n) for b in range(1, n))
            assert exact == enumerated, (n, r, exact, enumerated)
        values = [1 + 0j, 2 + 0j, -1 + 0j, 1 + 1j, 2 + 2j, complex(cmath.exp(2j * math.pi / n))]
        for z in values:
            actual = rank_direct(n, z)
            predicted = rank_predicted(n, z)
            assert actual == predicted, (n, z, actual, predicted)
            tested += 1
        assert (rank_predicted(n, 1 + 1j) == n * n) == (phi(n) == n - 1)
        assert rank_predicted(n, 2 + 2j) == n * n
    print(f"PASS: {tested} direct projector-span ranks and {sum(range(3,11))} congruence counts")
    print("PASS: prime/composite phase-line distinction and universal rational generator for n=3..10")


if __name__ == "__main__":
    main()
