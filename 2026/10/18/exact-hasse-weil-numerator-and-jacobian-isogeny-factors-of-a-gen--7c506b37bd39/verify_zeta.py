#!/usr/bin/env python3
"""Exact independent point counts and Weil polynomial for a genus-nine F2 curve.
Only the Python standard library is used. Equation and genus are specified in
Tafazolian, arXiv:2609.14830, Proposition 7.2; no source text is reproduced.
"""

MODULI = (0, 3, 7, 11, 19, 37, 67, 131, 283, 515)
EXPECTED = (0, 4, 8, 4, 24, 44, 8, 116, 312, 508)


def gf2_remainder(a, b):
    assert b
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def gf2_gcd(a, b):
    while b:
        a, b = b, gf2_remainder(a, b)
    return a


def gf2_raw_multiply(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result


def check_irreducible(modulus, n):
    assert modulus.bit_length() == n + 1
    x = 2
    xclass = gf2_remainder(2, modulus)
    for i in range(1, n + 1):
        x = gf2_remainder(gf2_raw_multiply(x, x), modulus)
        if i <= n // 2:
            assert gf2_gcd(x ^ xclass, modulus) == 1
    assert x == xclass


def point_counts(n):
    q = 1 << n
    modulus = MODULI[n]
    check_irreducible(modulus, n)
    multiplication = [
        [gf2_remainder(gf2_raw_multiply(a, b), modulus)
         for b in range(q)] for a in range(q)
    ]
    square = [multiplication[a][a] for a in range(q)]
    fourth = [square[square[a]] for a in range(q)]

    # Direct count on the smooth affine locus A(x) != 0 of
    # A(x)*(z^4+z) = B(x).
    affine = 0
    for x in range(q):
        x2, x4 = square[x], fourth[x]
        x6 = multiplication[x2][x4]
        x8 = square[x4]
        x7 = multiplication[x6][x]
        A = x7 ^ x
        B = x8 ^ x6 ^ x4 ^ x2 ^ 1
        if A:
            for z in range(q):
                if multiplication[A][fourth[z] ^ z] == B:
                    affine += 1
        else:
            assert B != 0  # No affine point above each of the pole x-values.

    # The eight geometric ramification points in the Artin--Schreier double
    # cover are: O, (0,1), and the two points (a,0) for every a^3=1.
    # Each is totally ramified and defined over F_4 at latest.
    pole_count = 2 + 2 * sum(
        1 for a in range(1, q)
        if multiplication[multiplication[a][a]][a] == 1
    )
    total_direct = affine + pole_count

    # Independent count on the elliptic double-cover description.
    inverse = [0] * q
    for a in range(1, q):
        inverse[a] = next(b for b in range(1, q)
                          if multiplication[a][b] == 1)

    def absolute_trace(value):
        out = 0
        for _ in range(n):
            out ^= value
            value = square[value]
        assert out in (0, 1)
        return out

    total_as = 1  # Over the pole O at infinity.
    as_poles = 1
    for x in range(q):
        x2 = square[x]
        x3 = multiplication[x2][x]
        x4 = fourth[x]
        d = x4 ^ x
        for y in range(q):
            if square[y] ^ multiplication[x][y] != x3 ^ 1:
                continue
            if not d:
                total_as += 1
                as_poles += 1
            else:
                f = multiplication[y][inverse[x]] ^ multiplication[x4 ^ x3 ^ 1][inverse[d]]
                if absolute_trace(f) == 0:
                    total_as += 2
    assert pole_count == as_poles
    assert total_direct == total_as == EXPECTED[n]
    return total_direct, affine, pole_count


def poly_multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def main():
    rows = [(n, *point_counts(n)) for n in range(1, 10)]
    counts = [row[1] for row in rows]
    sums = [(1 << n) + 1 - counts[n-1] for n in range(1, 10)]
    c = [1]
    for n in range(1, 10):
        rhs = -sum(c[n-k] * sums[k-1] for k in range(1, n+1))
        assert rhs % n == 0
        c.append(rhs // n)
    assert c == [1, 1, 2, 0, 2, 2, -4, -8, -11, 5]
    full = c + [(2 ** (9-i)) * c[i] for i in range(8, -1, -1)]
    factors = [
        [1,-1,2], [1,1,2], [1,1,2], [1,0,-1,0,4],
        [1,0,-2,0,1,0,-8,0,16],
    ]
    factored = [1]
    for factor in factors:
        factored = poly_multiply(factored, factor)
    assert full == factored and len(full) == 19
    number_jacobian = sum(full)
    assert number_jacobian == 1024
    assert sum((-1)**i * ci for i,ci in enumerate(full)) == 512
    print('n, points, smooth-affine points, ramification points:')
    for row in rows:
        print(*row, sep=', ')
    print('Frobenius power sums:', sums)
    print('Numerator coefficients (ascending):', full)
    print('Independent factor-product comparison: PASS')
    print('Jacobian cardinality over F2:', number_jacobian)


if __name__ == '__main__':
    main()
