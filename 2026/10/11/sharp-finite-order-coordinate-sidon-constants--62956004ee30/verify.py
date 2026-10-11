#!/usr/bin/env python3
import cmath
import itertools
import math
import random


def sidon_ratio(m, coeffs):
    w = cmath.exp(2j * math.pi / m)
    best = 0.0
    for ks in itertools.product(range(m), repeat=len(coeffs)):
        z = sum(coeffs[j] * (w ** ks[j]) for j in range(len(coeffs)))
        best = max(best, abs(z))
    return sum(abs(a) for a in coeffs) / best


def sharp_constant(m, n):
    return n * math.sin(math.pi / (m * n)) / math.sin(math.pi / m)


def extremizer(m, n):
    return [cmath.exp(2j * math.pi * j / (m * n)) for j in range(n)]


def main():
    exact_cases = 0
    for m in range(3, 8):
        for n in range(2, 5):
            got = sidon_ratio(m, extremizer(m, n))
            want = sharp_constant(m, n)
            assert abs(got - want) < 2e-12, (m, n, got, want)
            exact_cases += 1

    rng = random.Random(430046)
    random_cases = 0
    min_slack = float('inf')
    for m in range(3, 7):
        for n in range(2, 5):
            want = sharp_constant(m, n)
            for _ in range(80):
                coeffs = []
                for _j in range(n):
                    mag = 0.15 + 1.85 * rng.random()
                    phase = 2 * math.pi * rng.random()
                    coeffs.append(mag * cmath.exp(1j * phase))
                got = sidon_ratio(m, coeffs)
                slack = want - got
                min_slack = min(min_slack, slack)
                assert slack > -3e-12, (m, n, got, want)
                random_cases += 1

    print(
        'VERIFY_OK '
        f'exact_cases={exact_cases} random_cases={random_cases} '
        f'm_range=3..7 n_range=2..4 min_random_slack={min_slack:.12g}'
    )


if __name__ == '__main__':
    main()
