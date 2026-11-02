#!/usr/bin/env python3
"""Independent direct-kernel checks for two orthogonal regular circles on S^3.

Requires only the Python standard library. This finite test supplements, but does
not prove, the all-parameter analytic theorem in RESULT.md.
"""
import cmath
import math


def counts(m, degree):
    n = 2 * m
    ans = [0] * n
    for j in range(degree + 1):
        ans[(degree - 2 * j) % n] += 1
    return ans


def claimed_rank(m, degree):
    if degree % 2:
        return 2 * min(m, degree + 1)
    if degree < 2 * m:
        return 2 * min(m, degree + 1) - 1
    return 2 * m


def exact_spectrum(m, degree):
    n = 2 * m
    c = counts(m, degree)
    sign = (-1) ** (degree // 2) if degree % 2 == 0 else 0
    result = [n * (degree + 1) * c[a] for a in range(1, n) for _ in (0, 1)]
    result.extend((n * (degree + 1) * (c[0] + sign),
                   n * (degree + 1) * (c[0] - sign)))
    return result


def second_chebyshev(degree, x):
    a = 1.0
    if degree == 0:
        return a
    b = 2 * x
    for _ in range(2, degree + 1):
        a, b = b, 2 * x * b - a
    return b


def points(m, phase1, phase2):
    n = 2 * m
    first = [(math.cos(math.pi * j / m + phase1),
              math.sin(math.pi * j / m + phase1), 0, 0) for j in range(n)]
    second = [(0, 0, math.cos(math.pi * j / m + phase2),
               math.sin(math.pi * j / m + phase2)) for j in range(n)]
    return first + second


def dot(x, y):
    return sum(u * v for u, v in zip(x, y))


def residual(matrix, vec, eigenvalue):
    return max(abs(sum(a * b for a, b in zip(row, vec)) - eigenvalue * vec[i])
               for i, row in enumerate(matrix))


def direct_test(m, degree, phase1, phase2):
    n = 2 * m
    coords = points(m, phase1, phase2)
    kernel = [[(degree + 1) * second_chebyshev(degree, dot(x, y))
               for y in coords] for x in coords]
    freq = counts(m, degree)
    sign = (-1) ** (degree // 2) if degree % 2 == 0 else 0
    lam0 = n * (degree + 1) * freq[0]
    coupling = n * (degree + 1) * sign
    cases = 0
    for r in range(1, n):
        v = [cmath.exp(2j * math.pi * r * j / n) for j in range(n)]
        lam = n * (degree + 1) * freq[r]
        for first in (True, False):
            w = v + [0] * n if first else [0] * n + v
            err = residual(kernel, w, lam)
            assert err <= 3e-8 * (1 + abs(lam) + (degree + 1)**2 * n), (m, degree, r, first, err)
            cases += 1
    for parity in (-1, 1):
        w = [1] * n + [parity] * n
        lam = lam0 + parity * coupling
        err = residual(kernel, w, lam)
        assert err <= 3e-8 * (1 + abs(lam) + (degree + 1)**2 * n), (m, degree, parity, err)
        cases += 1
    return cases


def main():
    symbolic = 0
    for m in range(2, 21):
        for degree in range(121):
            spectrum = exact_spectrum(m, degree)
            assert len(spectrum) == 4 * m
            assert all(v >= 0 for v in spectrum)
            assert sum(v > 0 for v in spectrum) == claimed_rank(m, degree)
            assert sum(spectrum) == 4 * m * (degree + 1)**2
            if degree == 2 * m - 2:
                assert sorted(v for v in spectrum if v) == [4 * m * (2 * m - 1)] * (2 * m - 1)
            if degree == 2 * m - 1:
                assert sorted(v for v in spectrum if v) == [8 * m * m] * (2 * m)
            if degree == 2 * m:
                positive = sorted(v for v in spectrum if v)
                assert positive == [4 * m * (2 * m + 1)] * (2 * m - 1) + [8 * m * (2 * m + 1)]
            if degree >= 2 * m:
                assert all(abs(v - 2 * (degree + 1)**2) <= 4 * m * (degree + 1)
                           for v in spectrum if v)
            symbolic += 1
    direct = 0
    configurations = 0
    for phase1, phase2 in ((0., 0.), (.137, -.219), (math.pi / 11, math.pi / 17)):
        for m in range(2, 9):
            for degree in range(0, 17):
                direct += direct_test(m, degree, phase1, phase2)
                configurations += 1
    print(f"PASS: {symbolic} exact spectrum, rank and trace cross-checks")
    print(f"PASS: {configurations} raw-kernel/phase configurations, {direct} eigenvector tests")
    print("The infinite theorem is established in RESULT.md, not by these tests.")


if __name__ == '__main__':
    main()
