#!/usr/bin/env python3
"""Exact checks for the two-rank theorem for a tame characteristic-two family.
Uses integer modular arithmetic and a separate finite-field point count.
These finite tests are not used as a proof for arbitrary parameters.
"""

from math import gcd


def member(i, M):
    N = 3 * M
    r, s = 2 * M + 3, 2 * M
    return (i * r) % N + (i * s) % N > N


def in_J(a, M):
    return (6 * a > M and 3 * a < M) or (3 * a > 2 * M and 6 * a < 5 * M)


def check_h(h):
    M = 4 ** h + 1
    N = 3 * M
    assert gcd(3, M) == 1
    H = {i for i in range(1, N) if member(i, M)}
    assert len(H) == M
    # The inverse of 2 modulo N has order dividing 4h; explicitly test each
    # orbit, without relying on the claimed symbolic-dynamics formula.
    survived = set()
    for i in H:
        j = i
        orbit = set()
        while j not in orbit:
            orbit.add(j)
            j = (2 * j) % N
        if orbit <= H:
            survived.add(i)
    claimed_q = [q for q in range(1, M) if all(in_J(pow(4, j, M) * q % M, M)
                                                 for j in range(h))]
    assert len(survived) == 2 ** (h + 1), (h, len(survived))
    assert len(claimed_q) == 2 ** h, (h, len(claimed_q))
    residue_one = {i % M for i in survived if i % 3 == 1}
    assert residue_one == set(claimed_q), (h, residue_one ^ set(claimed_q))
    return M, len(H), len(survived)


# Irreducible binary polynomials of degrees one through five.
MOD = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101}


def gf_mul(a, b, d):
    result = 0
    polynomial = MOD[d]
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & (1 << d):
            a ^= polynomial
    return result & ((1 << d) - 1)


def gf_pow(a, exponent, d):
    out = 1
    while exponent:
        if exponent & 1:
            out = gf_mul(out, a, d)
        a = gf_mul(a, a, d)
        exponent >>= 1
    return out


def curve_points(d):
    # Count on the smooth completion of y^3 = x^5 + x^{-5}.
    # One point lies over each of x=0 and infinity, since gcd(3,5)=1.
    q = 1 << d
    count = 2
    for x in range(1, q):
        value = gf_pow(x, 5, d) ^ gf_pow(x, ((q - 1) - (5 % (q - 1))) % (q - 1), d)
        if value == 0:
            count += 1
        elif gcd(3, q - 1) == 1:
            count += 1
        elif gf_pow(value, (q - 1) // 3, d) == 1:
            count += 3
    return count


def point_count_check():
    g = 5
    coefficients = [1]
    counts = []
    # Newton recursion: n a_n = sum_{j=1}^n a_{n-j} (N_j - 2^j - 1).
    for n in range(1, g + 1):
        Nn = curve_points(n)
        counts.append(Nn)
        numer = sum(coefficients[n-j] * (counts[j-1] - (1 << j) - 1)
                    for j in range(1, n+1))
        assert numer % n == 0
        coefficients.append(numer // n)
    assert counts == [3, 9, 9, 37, 33], counts
    assert coefficients == [1, 0, 2, 0, 7, 0], coefficients
    # Degree modulo two of the numerator of the zeta function is the p-rank.
    assert max(j for j, a in enumerate(coefficients) if a % 2) == 4
    return counts, coefficients


if __name__ == '__main__':
    for h in range(1, 9):
        M, genus, p_rank = check_h(h)
        print('h=%d M=%d genus=%d p_rank=%d' % (h, M, genus, p_rank))
    counts, coefficients = point_count_check()
    print('F_2^r-point counts for r=1..5:', counts)
    print('L-coefficients through genus:', coefficients)
    print('VERIFY_OK')
