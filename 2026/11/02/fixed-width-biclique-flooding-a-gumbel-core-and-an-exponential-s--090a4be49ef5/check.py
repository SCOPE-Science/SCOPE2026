"""Exact finite-state checks and reproducible distribution diagnostics for SI flooding on bicliques."""
from fractions import Fraction
from functools import lru_cache
import math
import random
import statistics


def exact_transforms(a, b, s=Fraction(2, 5)):
    c = Fraction(a + b, a * b)

    @lru_cache(None)
    def expectation(i, j):
        if (i, j) == (a, b):
            return Fraction(0)
        ra = (a - i) * j * c
        rb = (b - j) * i * c
        assert ra + rb > 0
        rhs = 1
        if ra:
            rhs += ra * expectation(i + 1, j)
        if rb:
            rhs += rb * expectation(i, j + 1)
        return rhs / (ra + rb)

    @lru_cache(None)
    def laplace(i, j):
        if (i, j) == (a, b):
            return Fraction(1)
        ra = (a - i) * j * c
        rb = (b - j) * i * c
        assert ra + rb > 0
        numerator = Fraction(0)
        if ra:
            numerator += ra * laplace(i + 1, j)
        if rb:
            numerator += rb * laplace(i, j + 1)
        return numerator / (s + ra + rb)

    return c, expectation, laplace


def simulate(a, b, i, j, rng):
    c = 1 / a + 1 / b
    t = 0.0
    while (i, j) != (a, b):
        ra = (a - i) * j * c
        rb = (b - j) * i * c
        r = ra + rb
        t += rng.expovariate(r)
        if rng.random() * r < ra:
            i += 1
        else:
            j += 1
    return t


def check():
    count = 0
    for a in range(2, 9):
        for b in range(1, min(a, 5) + 1):
            for s in (Fraction(1, 3), Fraction(2, 5), Fraction(2, 1)):
                c, E, L = exact_transforms(a, b, s)
                assert E(1, 0) - E(0, 1) == Fraction(a - b, a + b)
                count += 1
                assert L(1, 0) * (s + b * c) == b * c * L(1, 1)
                count += 1
                assert L(0, 1) * (s + a * c) == a * c * L(1, 1)
                count += 1
                assert 0 < L(1, 0) <= 1 and 0 < L(0, 1) <= 1
                count += 1
                assert L(0, 1) >= L(1, 0)
                count += 1
                assert E(1, 0) >= E(0, 1)
                count += 1
    rng = random.Random(20261030)
    runs = 2400
    for a, b, i, j, expected_centre in (
        (1400, 2, 0, 1, 0.5772156649015329),
        (1400, 2, 2, 0, 0.5772156649015329 + 1 / 2),
        (1400, 3, 1, 1, 0.5772156649015329),
        (1400, 3, 3, 0, 0.5772156649015329 + 1 / 3),
    ):
        values = [simulate(a, b, i, j, rng) - math.log(a) for _ in range(runs)]
        mean = statistics.mean(values)
        assert abs(mean - expected_centre) < 0.23, (a, b, i, j, mean)
        count += 1
    print(f"PASS {count} exact assertions/diagnostics; no infinite-limit claim depends on simulation")


if __name__ == '__main__':
    check()
