#!/usr/bin/env python3
import cmath
import math
from fractions import Fraction


def harmonic(k):
    return sum((Fraction(1, j) for j in range(1, k + 1)), Fraction(0, 1))


def fourier_frame(n, d):
    # n unit vectors in C^d: first d rows of the n-point DFT, column-normalized.
    return [[cmath.exp(2j * math.pi * x * j / n) / math.sqrt(d) for j in range(d)] for x in range(n)]


def frame_operator(frame, d):
    out = [[0j for _ in range(d)] for _ in range(d)]
    for v in frame:
        for j in range(d):
            for k in range(d):
                out[j][k] += v[j] * v[k].conjugate()
    return out


def assert_close(a, b, tol=2e-11):
    if abs(a - b) > tol:
        raise AssertionError((a, b))


def check_pair(n, d):
    frame = fourier_frame(n, d)
    S = frame_operator(frame, d)
    target = n / d
    for j in range(d):
        for k in range(d):
            assert_close(S[j][k], target if j == k else 0.0)

    # POVM sum E_x = (d/n)|psi_x><psi_x|.
    for j in range(d):
        for k in range(d):
            assert_close((d / n) * S[j][k], 1.0 if j == k else 0.0)

    # Self-referential POVM success probability.
    success = sum((1 / n) * (d / n) * abs(sum(z.conjugate() * z for z in v)) ** 2 for v in frame)
    assert_close(success, d / n)

    gap = harmonic(n) - harmonic(d)
    if n == d:
        assert gap == 0
    else:
        assert gap > 0

    hmin = math.log(n / d)
    qcond = hmin - float(gap)
    assert_close(hmin - qcond, float(gap))
    assert qcond >= -2e-14


def main():
    for d in range(1, 8):
        for n in range(d, d + 9):
            check_pair(n, d)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
