#!/usr/bin/env python3
"""Exact finite-field point census for a distinguished genus-nine curve over F2.

Standard-library only. Represent a binary polynomial by its coefficient bitset,
and a finite-field element by its degree-<n representative modulo f_n.
"""
from math import gcd

MODULI = (0, 0x3, 0x7, 0xB, 0x13, 0x25, 0x43, 0x83, 0x11B, 0x203)
EXPECTED = (0, 4, 8, 4, 24, 44, 8, 116, 312, 508)
FACTORS = (
    (1, -1, 2),
    (1, 1, 2),
    (1, 1, 2),
    (1, 0, -1, 0, 4),
    (1, 0, -2, 0, 1, 0, -8, 0, 16),
)

def reduce_binary_polynomial(a, f):
    d = f.bit_length() - 1
    while a.bit_length() > d:
        a ^= f << (a.bit_length() - d - 1)
    return a

def mul(a, b, f):
    z = 0
    while b:
        if b & 1:
            z ^= a
        a <<= 1
        b >>= 1
    return reduce_binary_polynomial(z, f)

def pow_field(a, n, f):
    b = 1
    while n:
        if n & 1:
            b = mul(b, a, f)
        a = mul(a, a, f)
        n //= 2
    return b

def gcd_binary_polynomial(a, b):
    while b:
        while a and a.bit_length() >= b.bit_length():
            a ^= b << (a.bit_length() - b.bit_length())
        a, b = b, a
    return a

def check_irreducible(f, n):
    if n == 1:
        return f == 3
    x, u = 2, 2
    for k in range(1, n + 1):
        u = mul(u, u, f)
        if k <= n // 2 and gcd_binary_polynomial(u ^ x, f) != 1:
            return False
    return u == x

def trace(a, f, n):
    t = 0
    for _ in range(n):
        t ^= a
        a = mul(a, a, f)
    assert t in (0, 1)
    return t

def count(n):
    f = MODULI[n]
    assert check_irreducible(f, n)
    size = 1 << n
    sq = [mul(i, i, f) for i in range(size)]
    x4 = [sq[sq[x]] for x in range(size)]
    x3 = [mul(x, sq[x], f) for x in range(size)]
    x6 = [sq[x3[x]] for x in range(size)]
    x7 = [mul(x, x6[x], f) for x in range(size)]
    x8 = [sq[x4[x]] for x in range(size)]
    inverse = [0] + [pow_field(x, size - 2, f) for x in range(1, size)]
    assert all(mul(x, inverse[x], f) == 1 for x in range(1, size))

    # Method A: direct census of affine (x,z) on the plane model.
    counts_linear = [0] * size
    for z in range(size):
        counts_linear[x4[z] ^ z] += 1
    affine = 0
    zero_left = 0
    for x in range(size):
        a = x7[x] ^ x
        b = x8[x] ^ x6[x] ^ x4[x] ^ sq[x] ^ 1
        if a == 0:
            zero_left += 1
            assert b != 0
        else:
            affine += counts_linear[mul(b, inverse[a], f)]
    assert zero_left == (4 if n % 2 == 0 else 2)
    poles_plane = 8 if n % 2 == 0 else 4
    count_plane = affine + poles_plane

    # Method B: independently enumerate the double Artin-Schreier cover of E.
    # E: y^2 + xy = x^3 + 1 and z^2 + z = y/x + (x^4+x^3+1)/(x^4+x).
    rational = 1  # One totally ramified point above infinity of E.
    poles_E = 1
    E_points = 1
    for x in range(size):
        rhs = x3[x] ^ 1
        ys = [y for y in range(size) if sq[y] ^ mul(x, y, f) == rhs]
        E_points += len(ys)
        for y in ys:
            den = x4[x] ^ x
            if x == 0 or den == 0:
                poles_E += 1
                rational += 1  # Totally ramified at each rational pole.
            else:
                zrhs = mul(y, inverse[x], f) ^ mul(x4[x] ^ x3[x] ^ 1, inverse[den], f)
                rational += 2 if trace(zrhs, f, n) == 0 else 0
    assert poles_E == poles_plane
    assert rational == count_plane == EXPECTED[n], (n, rational, count_plane)
    return rational, affine, poles_E, E_points

def convolution(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return c

def main():
    points = [0]
    for n in range(1, 10):
        number, affine, poles, on_E = count(n)
        points.append(number)
        print('n=%d N=%d affine=%d ramified=%d E_points=%d field_modulus=0x%x' %
              (n, number, affine, poles, on_E, MODULI[n]))
    s = [0] + [2**n + 1 - points[n] for n in range(1, 10)]
    coeff = [1]
    for j in range(1, 10):
        v = -sum(coeff[j - k] * s[k] for k in range(1, j + 1))
        assert v % j == 0
        coeff.append(v // j)
    coeff += [0] * 9
    for j in range(9):
        coeff[18 - j] = 2**(9 - j) * coeff[j]
    product = [1]
    for f in FACTORS:
        product = convolution(product, f)
    assert coeff == product
    assert sum(coeff) == 1024
    assert all(coeff[18-j] == 2**(9-j)*coeff[j] for j in range(10))
    print('L_COEFFICIENTS=' + ','.join(map(str, coeff)))
    print('JACOBIAN_POINTS_F2=1024')
    print('NAKAJIMA_GENUS_NINE_ZETA_EXACT_OK')

if __name__ == '__main__':
    main()
