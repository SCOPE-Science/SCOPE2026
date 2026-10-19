"""Reproducible finite exact checks for weighted-chord cycle controllability.

Run: python3 verify.py
Only Python standard-library components are required.
Finite checks support, but do not replace, the all-size proof.
"""
from fractions import Fraction
from math import gcd


def predicted_defect(n, d, weight):
    assert n >= 4 and 2 <= d <= n // 2
    m = n - d
    g = gcd(n, 2 * d)
    exceptional = (d % 2 == 0 and m % 2 == 0
                   and Fraction(weight) == Fraction(1, d) + Fraction(1, m))
    return (g - 1) // 2 + int(exceptional)


def modular_krylov_rank(n, d, weight, prime=1000003):
    w = Fraction(weight)
    p, q = w.numerator, w.denominator
    assert q % prime != 0
    vector = [0] * n
    vector[0] = 1
    pivots = {}
    for _ in range(n):
        residual = vector[:]
        while True:
            leading = next((i for i, x in enumerate(residual) if x % prime), None)
            if leading is None:
                break
            if leading not in pivots:
                inv = pow(residual[leading], -1, prime)
                pivots[leading] = [(x * inv) % prime for x in residual]
                break
            coefficient = residual[leading]
            row = pivots[leading]
            residual = [(x - coefficient * y) % prime
                        for x, y in zip(residual, row)]
        next_vector = [(q * (2 * vector[i] - vector[(i-1) % n]
                             - vector[(i+1) % n])) % prime
                       for i in range(n)]
        change = p * (vector[0] - vector[d])
        next_vector[0] = (next_vector[0] + change) % prime
        next_vector[d] = (next_vector[d] - change) % prime
        vector = next_vector
    return len(pivots)


def rational_laplacian_action(n, d, weight, x):
    w = Fraction(weight)
    y = [2*x[j]-x[(j-1) % n]-x[(j+1) % n] for j in range(n)]
    shift = w * (x[0] - x[d])
    y[0] += shift
    y[d] -= shift
    return y


def resonant_eigenvector(n, d):
    m = n - d
    assert d % 2 == m % 2 == 0
    x = [Fraction(0) for _ in range(n)]
    x[d] = Fraction(1)
    for j in range(1, d):
        x[j] = Fraction((1 if (j-d) % 2 == 0 else -1) * j, d)
    for j in range(1, m):
        x[n-j] = Fraction((1 if (j-m) % 2 == 0 else -1) * j, m)
    return x


def main():
    checks = 0
    for n in range(4, 49):
        for d in range(2, n // 2 + 1):
            critical = Fraction(1, d) + Fraction(1, n-d)
            weights = (Fraction(1), Fraction(1, 2), Fraction(3, 2),
                       critical, 2 * critical)
            for weight in weights:
                desired = n - predicted_defect(n, d, weight)
                rank = modular_krylov_rank(n, d, weight)
                assert rank == desired, (n, d, weight, rank, desired)
                checks += 1
            if d % 2 == 0 and (n-d) % 2 == 0:
                x = resonant_eigenvector(n, d)
                y = rational_laplacian_action(n, d, critical, x)
                assert x[0] == 0 and y == [4*z for z in x]
    assert predicted_defect(4, 2, Fraction(1)) == 2
    assert predicted_defect(6, 2, Fraction(3, 4)) == 1
    assert predicted_defect(10, 2, Fraction(1)) == 0
    print('PASS: %d finite-field Krylov-rank checks and exact rational'
          ' resonance eigenvectors; n=4..48.' % checks)


if __name__ == '__main__':
    main()
