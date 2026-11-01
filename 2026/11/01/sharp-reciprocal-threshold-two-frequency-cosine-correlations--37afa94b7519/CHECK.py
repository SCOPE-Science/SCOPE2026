"""Independent exact-rational checks for reciprocal-threshold cosine correlations.

Run: python3 CHECK.py. Uses only Python's standard library.
Finite checks supplement, but do not replace, the all-integer proof in RESULT.md.
"""
from fractions import Fraction
from math import gcd


def bernoulli_numerator(k, m):
    r = k % m
    return r * (r - m)


def fourier_probability(m, a, b):
    """The exact Bernoulli/Fourier formula for coprime frequencies."""
    assert m >= 4 and a > 0 and b > 0 and a != b and gcd(a, b) == 1
    a, b = sorted((a, b))
    base = Fraction(8, m * m)
    if (a + b) % 2 == 0:
        return base + Fraction(2 * (bernoulli_numerator(b - a, m)
                                    - bernoulli_numerator(a + b, m)),
                               a * b * m * m)
    return base + Fraction(bernoulli_numerator(2 * (b - a), m)
                           - bernoulli_numerator(2 * (a + b), m),
                           2 * a * b * m * m)


def arcs(m, a, negative):
    """Union of exact open arcs, represented by disjoint closed endpoints.

    Endpoints have zero measure; clipping at 0 and 1 is exact.
    """
    r = Fraction(1, m)
    centers = ((Fraction(k, a) if not negative else Fraction(2 * k + 1, 2 * a))
               for k in (range(a + 1) if not negative else range(a)))
    out = []
    for x in centers:
        lo = max(Fraction(0), x - r / a)
        hi = min(Fraction(1), x + r / a)
        if lo < hi:
            out.append((lo, hi))
    return out


def overlap(x, y):
    i = j = 0
    z = Fraction(0)
    while i < len(x) and j < len(y):
        lo = max(x[i][0], y[j][0])
        hi = min(x[i][1], y[j][1])
        if hi > lo:
            z += hi - lo
        if x[i][1] < y[j][1]:
            i += 1
        elif x[i][1] > y[j][1]:
            j += 1
        else:
            i += 1
            j += 1
    return z


def interval_probability(m, a, b):
    return (overlap(arcs(m, a, False), arcs(m, b, False))
            + overlap(arcs(m, a, True), arcs(m, b, True)))


def proof_inequality_bcheck():
    # Extreme values and periodic-difference bounds in the proof.
    for m in range(4, 65):
        for a in range(1, m + 1):
            delta = Fraction(a, m)
            gap_bound = -delta * (1 - delta)
            for j in range(0, 2 * m):
                left = Fraction(bernoulli_numerator(j, m), m * m)
                right = Fraction(bernoulli_numerator(j + a, m), m * m)
                assert left - right >= gap_bound


def main():
    checks = 0
    # Independent interval intersections, with no trigonometric or
    # Bernoulli calculations, must match the Fourier expression exactly.
    for m in range(4, 22):
        for b in range(2, 28):
            for a in range(1, b):
                if gcd(a, b) > 1:
                    continue
                assert fourier_probability(m, a, b) == interval_probability(m, a, b)
                checks += 1
    # Exhaustive finite stress-testing against exact target and minimizers.
    # The mathematical proof handles ALL m,a,b, not only these limits.
    for m in range(4, 53):
        L = m - 1 if m % 2 == 0 else m - 2
        target = Fraction(4, m * L)
        minimizers = []
        for b in range(2, 161):
            for a in range(1, b):
                if gcd(a, b) > 1:
                    continue
                val = fourier_probability(m, a, b)
                assert val >= target, (m, a, b, val, target)
                if val == target:
                    minimizers.append((a, b))
                checks += 1
        expected = [(1, L)] + ([(1, 9)] if m == 5 else [])
        assert sorted(minimizers) == sorted(expected), (m, minimizers)
        checks += 1
    proof_inequality_bcheck()
    checks += 1
    print('CHECK_OK', checks)


if __name__ == '__main__':
    main()
