#!/usr/bin/env python3
"""Finite algebra diagnostics for the sharp Faber--Schauder point-sampling theorem.

Tests only finitely many parameters; the mathematical proof is in RESULT.md.
"""
import math


def hat(level, cell, x):
    return 2 ** (-level / 2 - 1) * max(0.0, 1.0 - 2.0 * abs(2 ** level * x - cell - 0.5))


def energy_norm_single_hat(level, exponent):
    base = 2 ** (-level / 2)
    return base * (1.5 + (level + 1) ** (1.0 / exponent))


def worst_tent_amplitude(level, exponent):
    return (0.5 * 2 ** (-level / 2)) / energy_norm_single_hat(level, exponent)


def bounds(sample_budget, exponent):
    low_level = math.ceil(math.log2(sample_budget + 1))
    upper_level = math.floor(math.log2(sample_budget - 1))
    low = 0.5 / ((low_level + 1) ** (1.0 / exponent) + 1.5)
    upper = 0.5 / ((upper_level + 1) ** (1.0 / exponent))
    return low, upper


def main():
    tests = 0
    for exponent in [1.1, 1.5, 2.0, 3.0, 5.0, 20.0]:
        for level in range(11):
            scale = 2 ** (-level / 2)
            # Exactly one nonzero Z component and level+1 identical H components.
            expected_norm = scale / 2 + scale + (level + 1) ** (1.0 / exponent) * scale
            assert math.isclose(energy_norm_single_hat(level, exponent), expected_norm)
            tests += 1
            for cell in [0, 2 ** level - 1]:
                mid = (cell + 0.5) / (2 ** level)
                left = cell / (2 ** level)
                right = (cell + 1) / (2 ** level)
                assert math.isclose(hat(level, cell, mid), scale / 2)
                assert hat(level, cell, left) < 1e-12
                assert hat(level, cell, right) < 1e-12
                tests += 3
            normalized_peak = (scale / 2) / energy_norm_single_hat(level, exponent)
            assert math.isclose(normalized_peak, worst_tent_amplitude(level, exponent))
            tests += 1
        for n in [2, 3, 4, 5, 7, 9, 17, 31, 65, 257, 1025, 4097]:
            low, upper = bounds(n, exponent)
            assert 0 < low <= upper
            assert 2 ** math.floor(math.log2(n - 1)) + 1 <= n
            assert 2 ** math.ceil(math.log2(n + 1)) > n
            tests += 3
    print(f"PASS: {tests} finite assertions; analytical proof required for the theorem")


if __name__ == '__main__':
    main()
