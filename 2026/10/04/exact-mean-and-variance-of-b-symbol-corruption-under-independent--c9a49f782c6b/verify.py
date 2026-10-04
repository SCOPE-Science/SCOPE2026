from fractions import Fraction
from itertools import product


def corruption_count(bits, b):
    n = len(bits)
    return sum(any(bits[(i + j) % n] for j in range(b)) for i in range(n))


def union_size(n, b, d):
    if d == 0:
        return b
    return 2 * b - max(0, b - d) - max(0, b - (n - d))


def general_formula(n, b, p):
    r = 1 - p
    mean = n * (1 - r ** b)
    var = n * (sum(r ** union_size(n, b, d) for d in range(n)) - n * r ** (2 * b))
    return mean, var


def simplified_variance(n, b, p):
    assert n >= 2 * b
    r = 1 - p
    return n * (r ** b + 2 * sum(r ** j for j in range(b + 1, 2 * b)) - (2 * b - 1) * r ** (2 * b))


small_cases = 0
patterns_checked = 0
for n in range(1, 10):
    for b in range(1, n + 1):
        for p in (Fraction(1, 7), Fraction(1, 3), Fraction(1, 2), Fraction(4, 5)):
            e1 = Fraction(0)
            e2 = Fraction(0)
            for bits in product((0, 1), repeat=n):
                prob = Fraction(1)
                for bit in bits:
                    prob *= p if bit else 1 - p
                w = corruption_count(bits, b)
                e1 += prob * w
                e2 += prob * w * w
                patterns_checked += 1
            mean, var = general_formula(n, b, p)
            assert e1 == mean, (n, b, p, e1, mean)
            assert e2 - e1 * e1 == var, (n, b, p, e2 - e1 * e1, var)
            small_cases += 1

large_cases = 0
for b in range(1, 51):
    for n in range(2 * b, 121):
        for p in (Fraction(1, 11), Fraction(2, 5), Fraction(7, 10)):
            _, v = general_formula(n, b, p)
            assert v == simplified_variance(n, b, p), (n, b, p)
            large_cases += 1

print(f"VERIFY_OK small_moment_cases={small_cases} patterns={patterns_checked} simplified_grid_cases={large_cases}")
