"""Finite consistency checks for the three-tap cyclic self-STFT support classification.

The unrestricted theorem is algebraic.  Floating-point tests only corroborate it.
"""
import cmath
import math
import random


def direct_support(n, values, start=0, step=1):
    f = [0j] * n
    for h, v in enumerate(values):
        f[(start + h * step) % n] = complex(v)
    total = 0
    rows = {}
    for x in range(n):
        nonzero = 0
        for k in range(n):
            val = sum(
                f[t] * f[(t - x) % n].conjugate()
                * cmath.exp(-2j * math.pi * k * t / n)
                for t in range(n)
            )
            nonzero += abs(val) > 1e-7
        if nonzero:
            rows[x] = nonzero
            total += nonzero
    return total, rows


def theoretical_support(n, values):
    a, b, c = [complex(x) for x in values]
    ra, rb, rc = abs(a) ** 2, abs(b) ** 2, abs(c) ** 2
    root = -b * c.conjugate() / (a * b.conjugate())
    e = int(abs(abs(a) - abs(c)) < 1e-9 and abs(root ** n - 1) < 1e-8)
    if n % 2 == 0 and abs(rb - ra - rc) < 1e-9:
        d = 1
    elif abs(ra - rc) < 1e-9 and any(
        abs(rb + 2 * ra * math.cos(2 * math.pi * j / n)) < 1e-9
        for j in range(1, (n + 1) // 2)
    ):
        d = 2
    else:
        d = 0
    return 5 * n - 2 * e - d, e, d


def witnesses(n):
    j = max(j for j in range(1, (n + 1) // 2)
            if math.cos(2 * math.pi * j / n) < -1e-10)
    r = -2 * math.cos(2 * math.pi * j / n)
    w = {
        "generic": ((1, 1, 2), 5 * n),
        "outer_rows_cancel": ((1, 1j * math.sqrt(3), 1), 5 * n - 2),
        "all_four_zeros": ((1, 1j * math.sqrt(r), 1), 5 * n - 4),
        "central_two_only": ((1, math.sqrt(r) * cmath.exp(1j * math.pi / (4 * n)), 1), 5 * n - 2),
    }
    if n % 2 == 0:
        w["one_central_zero"] = ((1, math.sqrt(5), 2), 5 * n - 1)
        w["three_zeros"] = ((1, 1j * math.sqrt(2), 1), 5 * n - 3)
    return w


def main():
    random.seed(1729)
    tests = 0
    for n in range(5, 19):
        observed = set()
        for name, (vals, target) in witnesses(n).items():
            predicted, e, d = theoretical_support(n, vals)
            assert predicted == target, (n, name, predicted, target, e, d)
            for shift, step in [(0, 1), (2, n - 1)]:
                direct, rows = direct_support(n, vals, shift, step)
                assert direct == predicted, (n, name, direct, predicted, rows)
                tests += 1
            observed.add(predicted)
        expected = {5 * n - 2, 5 * n, 5 * n - 4} if n % 2 else set(range(5 * n - 4, 5 * n + 1))
        assert observed == expected, (n, observed, expected)
        for _ in range(30):
            # Generic complex coefficients: keep magnitude away from zero.
            vals = tuple(random.uniform(0.6, 3) * cmath.exp(1j * random.uniform(-math.pi, math.pi)) for _ in range(3))
            predicted, _, _ = theoretical_support(n, vals)
            direct, _ = direct_support(n, vals)
            assert direct == predicted, (n, vals, direct, predicted)
            tests += 1
    print(f"VERIFY_OK tests={tests}; cyclic orders=5..18; every predicted support level witnessed")


if __name__ == "__main__":
    main()
