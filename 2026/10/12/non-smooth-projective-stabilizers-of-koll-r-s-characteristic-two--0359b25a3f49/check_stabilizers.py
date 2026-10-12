#!/usr/bin/env python3
"""Independent finite-field checks for the plane stabilizers of explicit rational cuspidal curves.

No network or nonstandard dependencies. These finite checks support but do not replace
proof of the theorem over algebraically closed fields and for all powers of two.
"""


def multiply(a, b, degree, modulus):
    acc = 0
    while b:
        if b & 1:
            acc ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= modulus
    return acc


def poly_mul(a, b, degree, modulus):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] ^= multiply(x, y, degree, modulus)
    return c


def poly_pow(a, n, degree, modulus):
    result = [1]
    while n:
        if n & 1:
            result = poly_mul(result, a, degree, modulus)
        n >>= 1
        if n:
            a = poly_mul(a, a, degree, modulus)
    return result


def test(n, modulus):
    q = 2 ** n
    degree = 2 * n
    field_size = 1 << degree
    found = []
    for a in range(1, field_size):
        for b in range(field_size):
            t = [b, a]
            x = poly_pow(t, q, degree, modulus)
            h = poly_pow(t, q + 2, degree, modulus)
            h[0] ^= b
            h[1] ^= a
            if any(c for j, c in enumerate(x) if j not in (0, q)):
                continue
            if any(c for j, c in enumerate(h) if j not in (0, 1, q, q + 2)):
                continue
            if h[q + 2] != h[1]:
                continue
            found.append((a, b))
    expected = 3 * field_size if q == 2 else q + 1
    assert len(found) == expected, (q, len(found), expected)
    if q >= 4:
        assert all(b == 0 for a, b in found)
    else:
        assert set(b for a, b in found) == set(range(field_size))
    # Build the full linearized stabilizer equations from the homogeneous F,
    # rather than inserting the expected five relations by hand.
    # Columns 0..8 are the matrix entries D_(i,j), column 9 is the scalar
    # lambda in delta(F)=lambda*F.
    F = {(0, q, 2), (q + 2, 0, 0), (1, 0, q + 1)}
    equations = {}
    for exponents in F:
        equations[exponents] = equations.get(exponents, 0) ^ (1 << 9)
        for i in range(3):
            if exponents[i] % 2 == 0:
                continue
            derivative = list(exponents)
            derivative[i] -= 1
            for j in range(3):
                monomial = derivative.copy()
                monomial[j] += 1
                tkey = tuple(monomial)
                equations[tkey] = equations.get(tkey, 0) ^ (1 << (3 * i + j))
    rows = [row for row in equations.values() if row]
    pivot = 0
    for bit in range(10):
        leading = next((j for j in range(pivot, len(rows))
                        if rows[j] & (1 << bit)), None)
        if leading is None:
            continue
        rows[pivot], rows[leading] = rows[leading], rows[pivot]
        for j in range(len(rows)):
            if j != pivot and rows[j] & (1 << bit):
                rows[j] ^= rows[pivot]
        pivot += 1
    assert pivot == 6, (q, pivot)
    assert 10 - pivot - 1 == 3  # remove one scalar projective direction
    return q, field_size, len(found)


if __name__ == '__main__':
    # Irreducible modulus polynomials: x^2+x+1, x^4+x+1, x^6+x+1.
    results = [test(1, 0b111), test(2, 0b10011), test(3, 0b1000011)]
    assert results == [(2, 4, 12), (4, 16, 5), (8, 64, 9)]
    print('STABILIZER_CHECK_OK', results)
