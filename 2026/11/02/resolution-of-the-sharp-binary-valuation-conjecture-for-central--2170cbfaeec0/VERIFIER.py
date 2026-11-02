"""Exact checks for a dyadic congruence of central Delannoy numbers.

Finite computations corroborate but do not replace the mathematical proof.
Only Python's standard library is needed.
"""
from fractions import Fraction
from math import comb


def nu2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def delannoy_prefix(length):
    assert length >= 2
    out = [1, 3]
    for n in range(length - 2):
        v = 3 * (2 * n + 3) * out[-1] - (n + 1) * out[-2]
        assert v % (n + 2) == 0
        out.append(v // (n + 2))
    return out


def poly_j(j):
    p = [Fraction(1)]
    for i in range(1, j):
        q = [Fraction(0) for _ in range(len(p) + 2)]
        for m, c in enumerate(p):
            q[m] += c
            q[m + 1] -= 2 * c / i
            q[m + 2] += c / (i * i)
        p = q
    return p


def test():
    nmax = 4096
    d = delannoy_prefix(nmax + 1)
    assert d[4] == 321 and d[8] == 265729
    for n in range(1, nmax + 1):
        expected = 1 if n & 1 else (2 if (n & 3) else 3 * nu2(n))
        assert nu2(d[n] - 1) == expected, (n, d[n])
    for n in range(1, 81):
        assert d[n] == sum(comb(n, k) ** 2 * (2 ** k) for k in range(n + 1))

    p4, p8 = poly_j(4), poly_j(8)
    assert p4[1] == Fraction(-11, 3)
    assert p4[2] == Fraction(193, 36)
    assert p8[2] == Fraction(2105161, 176400)
    assert (Fraction(193, 9) + Fraction(2105161, 11025)).numerator % 2 == 0
    assert (Fraction(193, 9) + Fraction(2105161, 11025)).denominator % 2 == 1

    # Exact finite integer checks for the small-j cases in the proof.
    small_min = [2, 3, 0, 3, 2, 5, 0]
    for j in range(2, 32):
        v = sorted((nu2(i) for i in range(1, j) for _ in range(2)), reverse=True)
        prefix = 0
        es = []
        for m, w in enumerate(v, 1):
            prefix += w
            if m >= 2:
                es.append((m, j - 2 * nu2(j) + 2 * (m - 1) - prefix))
        if j <= 8:
            assert min(e for m, e in es) == small_min[j - 2]
            assert [m for m, e in es if e == 0] == ([2] if j in (4, 8) else [])
        else:
            B = j - 2 * nu2(j) - 2 - 2 * sum(
                (j - 1) // (1 << h) for h in range(3, 20)
            )
            assert B >= 4
            assert all(e >= B for m, e in es)

    for j in range(2, 1025):
        lb = j + 1 - 2 * nu2(j) - (j - 1).bit_length() + 1
        # floor(log_2(j-1)) = bit_length(j-1)-1
        assert lb == j + 1 - 2 * nu2(j) - ((j - 1).bit_length() - 1)
        if j != 4:
            assert lb >= 1, (j, lb)
    for precision in (16, 32, 64, 96):
        modulus = 1 << precision
        total = 0
        for j in range(1, 2 * precision + 50):
            v = nu2(j)
            if j - 2 * v >= precision:
                continue
            total = (total + (1 << (j - 2 * v)) * pow(j >> v, -2, modulus)) % modulus
        assert total == 0
    print('VERIFY_OK: 4096 valuations, 80 direct sums, exact coefficients, bounds and dyadic sums')


if __name__ == '__main__':
    test()
