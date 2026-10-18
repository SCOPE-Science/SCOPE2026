"""Finite reproducibility checks for a two-frequency harmonic HMC identity.

Run: python3 verify.py
These checks do not establish the universal trigonometric inequality.
"""
import math
import random


def optimum(m):
    if m < 1 or int(m) != m:
        raise ValueError("m must be a positive integer")
    return 0.0 if m % 2 else math.sin(math.pi / (2 * (m + 1))) ** 2


def scores(m, t):
    return math.cos(t) ** 2, math.cos(m * t) ** 2


def witness(m):
    return math.pi / 2 - math.pi / (2 * (m + 1))


checks = 0
for m in range(1, 33):
    predicted = optimum(m)
    t = math.pi / 2 if m % 2 else witness(m)
    a, b = scores(m, t)
    assert abs(max(a, b) - predicted) < 1e-13
    checks += 1
    if m % 2 == 0:
        # Test a weighted supporting inequality independently of optimization.
        for j in range(10001):
            t = j * math.pi / 10000
            a, b = scores(m, t)
            assert m * a + b + 1e-11 >= (m + 1) * predicted
            checks += 1

# Exact two-mode witnesses, expressed via low-degree radicals.
two = scores(2, math.pi / 3)
four = scores(4, 2 * math.pi / 5)
assert all(abs(v - 0.25) < 1e-13 for v in two)
assert all(abs(v - (3 - math.sqrt(5)) / 8) < 1e-13 for v in four)
checks += 4

# Check that mixing finitely supported integration times never beats the
# claimed universal factor, independently of whether the support is optimal.
rng = random.Random(73255)
for m in range(1, 33):
    for j in range(500):
        weights = [rng.random() for _ in range(4)]
        times = [rng.random() * math.pi * 8 for _ in range(4)]
        denom = sum(weights)
        a = sum(w * scores(m, t)[0] for w, t in zip(weights, times)) / denom
        b = sum(w * scores(m, t)[1] for w, t in zip(weights, times)) / denom
        assert max(a, b) + 1e-12 >= optimum(m)
        checks += 1

print(f"PASS: {checks} finite numeric consistency checks; universal proof is analytic.")
