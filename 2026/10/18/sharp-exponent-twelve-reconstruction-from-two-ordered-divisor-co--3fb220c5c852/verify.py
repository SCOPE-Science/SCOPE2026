#!/usr/bin/env python3
"""Exact integer certificate for the divisor-pair signature threshold."""
from math import comb

PRIMES = (2, 3, 5, 7, 11, 13)


def valuation(n, p):
    ans = 0
    while n % p == 0:
        n //= p
        ans += 1
    return ans


def matrix(max_exponent=12):
    return [[valuation(e + 1, p) for e in range(1, max_exponent + 1)]
            for p in PRIMES] + [
                [valuation(comb(e + 2, 2), p) for e in range(1, max_exponent + 1)]
                for p in PRIMES]


def bareiss_det(matrix_data):
    """Exact fraction-free Gaussian elimination, preserving signed determinant."""
    a = [row[:] for row in matrix_data]
    n = len(a)
    assert all(len(row) == n for row in a)
    sign, denom = 1, 1
    for i in range(n - 1):
        if a[i][i] == 0:
            swap = next((j for j in range(i + 1, n) if a[j][i] != 0), None)
            if swap is None:
                return 0
            a[i], a[swap] = a[swap], a[i]
            sign *= -1
        pivot = a[i][i]
        for j in range(i + 1, n):
            for k in range(i + 1, n):
                numerator = a[j][k] * pivot - a[j][i] * a[i][k]
                assert numerator % denom == 0
                a[j][k] = numerator // denom
            a[j][i] = 0
        denom = pivot
    return sign * a[n - 1][n - 1]


def signature_values(exponents):
    a = b = 1
    for e in exponents:
        a *= e + 1
        b *= comb(e + 2, 2)
    return (a, b)


def direct_counts(n):
    tau = sum(n % a == 0 for a in range(1, n + 1))
    d3 = 0
    for a in range(1, n + 1):
        if n % a:
            continue
        m = n // a
        d3 += sum(m % b == 0 for b in range(1, m + 1))
    return tau, d3


def exponents_from_integer(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append(e)
        d += 1
    if n > 1:
        out.append(1)
    return out


def main():
    A = matrix()
    assert len(A) == 12 and all(len(row) == 12 for row in A)
    det = bareiss_det(A)
    assert det == 1, det
    assert signature_values((2, 2, 13)) == signature_values((1, 6, 8)) == (126, 3780)
    A13 = matrix(13)
    collision_coeff = [-1, 2, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 1]
    assert all(sum(row[j]*collision_coeff[j] for j in range(13)) == 0 for row in A13)
    # Direct triple-enumeration sanity checks, separate from multiplicative formula.
    for n in range(2, 401):
        assert direct_counts(n) == signature_values(exponents_from_integer(n)), n
    # Exhaustive signature-fingerprint collision test for exponent partitions
    # of total sum up to 13. The first distinct-signature collision
    # appears at exponent cap 13 (not necessarily at small total sum).
    vectors = {}
    def walk(min_e, rem, parts):
        if parts:
            values = signature_values(parts)
            earlier = vectors.get(values)
            if earlier is not None and earlier != tuple(parts):
                assert max(parts + list(earlier)) >= 13, (earlier, parts)
            else:
                vectors[values] = tuple(parts)
        for e in range(min_e, rem + 1):
            walk(e, rem-e, parts + [e])
    walk(1, 13, [])
    print('CERTIFICATE PASS')
    print('12x12 valuation matrix determinant =', det)
    print('13th exponent linear relation =', tuple(collision_coeff))
    print('first explicit boundary collision = (2,2,13) versus (1,6,8)')
    print('both invariant pairs =', signature_values((2,2,13)))
    print('direct factorization checks = 399; bounded signature checks =', len(vectors))


if __name__ == '__main__':
    main()
