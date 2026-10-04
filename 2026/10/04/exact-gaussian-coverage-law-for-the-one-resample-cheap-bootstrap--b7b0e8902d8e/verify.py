#!/usr/bin/env python3
import itertools
import math
from collections import defaultdict
from fractions import Fraction


def collision_counts(n):
    """Return counts A_n(n,c): labeled maps [n]->[n] with collision count c."""
    dp = {(0, 0): 1}
    for _boxes in range(n):
        nd = defaultdict(int)
        for (b0, c0), v in dp.items():
            for k in range(n - b0 + 1):
                b = b0 + k
                c = c0 + k * (k - 1) // 2
                nd[(b, c)] += v * math.comb(b, k)
        dp = nd
    return {c: v for (b, c), v in dp.items() if b == n}


def brute_counts(n):
    out = defaultdict(int)
    for draw in itertools.product(range(n), repeat=n):
        occ = [0] * n
        for j in draw:
            occ[j] += 1
        c = sum(k * (k - 1) // 2 for k in occ)
        out[c] += 1
    return dict(out)


def exact_central_moments(n, cnt):
    total = n ** n
    mean = Fraction(n - 1, 2)
    vals = []
    for r in (2, 3, 4):
        vals.append(sum(Fraction(v, total) * (Fraction(c) - mean) ** r for c, v in cnt.items()))
    return vals


def formula_moments(n):
    n = Fraction(n)
    mu2 = (n - 1) ** 2 / (2 * n)
    mu3 = 3 * (n - 2) * (n - 1) ** 2 / (2 * n ** 2)
    mu4 = (n - 1) ** 2 * (3 * n ** 3 + 32 * n ** 2 - 165 * n + 180) / (4 * n ** 3)
    return [mu2, mu3, mu4]


def coverage(n, alpha):
    cnt = collision_counts(n)
    a = 1.0 / math.tan(math.pi * alpha / 2.0)
    total = n ** n
    value = 0.0
    for c, count in cnt.items():
        q = 2.0 * c / n
        g = 0.0 if c == 0 else (2.0 / math.pi) * math.atan(a * math.sqrt(q))
        value += (count / total) * g
    return value


def coefficient(alpha):
    a = 1.0 / math.tan(math.pi * alpha / 2.0)
    return a * (3.0 + 5.0 * a * a) / (2.0 * math.pi * (1.0 + a * a) ** 2)


def main():
    # Recurrence exactly reproduces exhaustive labeled resampling at small n.
    for n in range(2, 5):
        assert collision_counts(n) == brute_counts(n)

    # Exact occupancy totals and the second-to-fourth central moment identities.
    for n in range(2, 31):
        cnt = collision_counts(n)
        assert sum(cnt.values()) == n ** n
        assert exact_central_moments(n, cnt) == formula_moments(n)

    alpha = 0.05
    expected = {
        2: 0.47500000000000003,
        10: 0.9429201071484832,
        20: 0.9468018332436843,
        30: 0.9478965996216816,
    }
    for n, target in expected.items():
        got = coverage(n, alpha)
        assert abs(got - target) < 5e-15, (n, got, target)

    c = coefficient(alpha)
    assert abs(c - 0.062090032300721396) < 5e-16
    # Finite-n values approach the proved first-order coefficient from the exact law.
    assert abs(30 * (0.95 - coverage(30, alpha)) - c) < 0.0011
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
