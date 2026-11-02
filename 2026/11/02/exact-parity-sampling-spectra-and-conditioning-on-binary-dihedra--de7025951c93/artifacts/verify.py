#!/usr/bin/env python3
"""Reproduce the exact spectral, rank and conditioning assertions for a two-circle sample in S^3.

Only Python's standard library is required. The checks are finite tests, not
substitutes for the analytic proof in RESULT.md.
"""
import cmath
import math


def multiplicities(m, degree):
    modulus = 2 * m
    result = [0] * modulus
    for r in range(degree + 1):
        result[(degree - 2 * r) % modulus] += 1
    return result


def eigenvalues(m, degree):
    counts = multiplicities(m, degree)
    out = []
    for j in range(2 * m):
        if j == 0 and degree % 2 == 0:
            out.extend([2 * m * (counts[0] + 1), 2 * m * (counts[0] - 1)])
        else:
            out.extend([2 * m * counts[j]] * 2)
    assert len(out) == 4 * m
    return sorted(out)


def expected_rank(m, degree):
    if degree % 2:
        return 2 * min(degree + 1, m)
    if degree < 2 * m:
        return 2 * min(degree + 1, m) - 1
    return 2 * m


def expected_condition(m, degree):
    if degree % 2:
        if degree + 1 <= m or (degree + 1) % m == 0:
            return (1, 1)
        q = (degree + 1) // m
        return (q + 1, q)
    if degree in (0, 2 * m - 2):
        return (1, 1)
    if degree < 2 * m:
        return (2, 1)
    q = degree // (2 * m)
    return (q + 1, q)


def polynomial(degree, value):
    if degree == 0:
        return 1.0
    if degree == 1:
        return 2.0 * value
    a, b = 1.0, 2.0 * value
    for _ in range(2, degree + 1):
        a, b = b, 2.0 * value * b - a
    return b


def points(m):
    samples = []
    for j in range(2 * m):
        t = math.pi * j / m
        samples.append((math.cos(t), math.sin(t), 0.0, 0.0))
    for j in range(2 * m):
        t = math.pi * j / m
        samples.append((0.0, 0.0, math.cos(t), math.sin(t)))
    return samples


def gram(m, degree):
    data = points(m)
    return [[polynomial(degree, sum(a * b for a, b in zip(x, y))) for y in data] for x in data]


def test():
    checked = 0
    for m in range(2, 49):
        for degree in range(180):
            spectrum = eigenvalues(m, degree)
            nonzero = [v for v in spectrum if v > 0]
            assert len(nonzero) == expected_rank(m, degree), (m, degree)
            top, bottom = expected_condition(m, degree)
            assert max(nonzero) * bottom == min(nonzero) * top, (m, degree)
            assert (len(set(nonzero)) == 1) == (top == bottom), (m, degree)
            newer = eigenvalues(m, degree + 4 * m)
            assert newer[:2 * m] == [0] * (2 * m)
            assert newer[2 * m:] == [v + 8 * m for v in spectrum[2 * m:]]
            checked += 1
    print("EXACT_SPECTRAL_CHECKS_OK", checked)

    direct = 0
    for m in (2, 3, 4, 5, 7, 9):
        size = 4 * m
        for degree in tuple(range(0, min(4 * m + 1, 24))) + (4 * m + 1,):
            data = gram(m, degree)
            count = multiplicities(m, degree)
            # Direct cyclic Fourier eigenvectors on each block, plus the two
            # constant combinations for even degree.
            c = [data[0][r] for r in range(2 * m)]
            for j in range(2 * m):
                computed = sum(c[r] * cmath.exp(-2j * math.pi * j * r / (2 * m))
                               for r in range(2 * m))
                assert abs(computed.imag) < 1e-7
                assert abs(computed.real - 2 * m * count[j]) < 1e-7
            cross = polynomial(degree, 0.0)
            for i in range(2 * m):
                for j in range(2 * m, size):
                    assert abs(data[i][j] - cross) < 1e-8
            if degree % 2:
                assert abs(cross) < 1e-8
            else:
                assert abs(abs(cross) - 1.0) < 1e-8
                assert abs(count[0] - (2 * (degree // (2 * m)) + 1)) == 0
            direct += 1
        for degree in (0, 1, 2, 2 * m - 2, 2 * m - 1, 2 * m, 4 * m + 1):
            old = gram(m, degree)
            new = gram(m, degree + 4 * m)
            for i in range(size):
                for j in range(size):
                    anticenter = (i + m) % (2 * m) if i < 2 * m else 2 * m + (i - 2 * m + m) % (2 * m)
                    target = 4 * m * (int(i == j) + (-1) ** degree * int(j == anticenter))
                    assert abs(new[i][j] - old[i][j] - target) < 5e-8, (m, degree, i, j)
    print("DIRECT_BLOCK_AND_SHIFT_CHECKS_OK", direct)


if __name__ == "__main__":
    test()
