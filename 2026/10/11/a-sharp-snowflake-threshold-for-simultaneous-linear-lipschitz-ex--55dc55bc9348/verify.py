"""Reproducible checks for the regular-polygon linear-extension theorem.

All finite computations are corroboration; the all-n proof is analytic.
Requires only Python 3 standard library.
"""
from math import sin, pi, log, sqrt, tan
from random import Random


def chord(n, j):
    return 2.0 * sin(pi * j / n)


def F(n, alpha):
    return sum(chord(n, j) ** alpha for j in range(1, n)) / n


def phase(n):
    lo, hi = 0.0, 1.0
    assert F(n, lo) < 1 < F(n, hi)
    for _ in range(65):
        mid = (lo + hi) / 2
        if F(n, mid) > 1:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def lipschitz(f, n, alpha, center_value=None):
    val = 0.0
    for i in range(n):
        for j in range(i):
            val = max(val, abs(f[i] - f[j]) / chord(n, i - j) ** alpha)
    if center_value is not None:
        val = max(val, *(abs(x-center_value) for x in f))
    return val


def main():
    tests = 0
    rng = Random(7624031)
    for n in range(3, 19):
        for alpha in (0.1, 0.4, 0.65, 0.9, 1.0):
            K = max(1., F(n, alpha))
            d = [0.0] + [chord(n, j)**alpha for j in range(1, n)]
            exact_ratio = lipschitz(d, n, alpha, sum(d)/n) / lipschitz(d, n, alpha)
            assert abs(exact_ratio - K) < 2e-13, (n, alpha, exact_ratio, K)
            tests += 1
            for _ in range(8):
                f = [rng.uniform(-1, 1) for _ in range(n)]
                v = sum(f)/n
                ratio = lipschitz(f, n, alpha, v) / lipschitz(f, n, alpha)
                assert ratio <= K + 2e-13, (n, alpha, ratio, K)
                tests += 1
    for n in (3, 4, 5, 8, 16, 37, 64, 125, 256):
        assert abs(sum(log(chord(n, j)) for j in range(1, n)) - log(n)) < 1e-11
        assert abs(F(n, 1.) - 2/(n*tan(pi/(2*n)))) < 5e-13
        assert abs(F(n, phase(n)) - 1) < 2e-14
        tests += 3
    assert abs(phase(3) - 2*log(3/2)/log(3)) < 2e-14
    assert abs(phase(4) - 2*log(sqrt(5)-1)/log(2)) < 2e-14
    tests += 2
    lim = sqrt(24)/pi
    scaled = []
    for n in (1024, 4096, 16384):
        scaled.append(phase(n)*sqrt(n))
    assert 0 < scaled[0] < scaled[1] < scaled[2] < lim
    assert lim - scaled[2] < 0.15
    tests += 2
    print('POLYGON_LINEAR_EXTENSION_VERIFY_OK')
    print('checks:', tests)
    print('asymptotic_target:', round(lim, 12))
    print('scaled_roots:', [round(a, 8) for a in scaled])


if __name__ == '__main__':
    main()
