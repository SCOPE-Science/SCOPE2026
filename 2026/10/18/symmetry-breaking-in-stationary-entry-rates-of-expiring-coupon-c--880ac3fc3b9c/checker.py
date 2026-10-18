"""Reproducible finite checks for the stationary sliding-window entrance theorem.

Python standard library only. Finite tests do not prove the infinite theorem.
"""
from fractions import Fraction
from itertools import product
from math import exp, log, isclose

checks = 0


def weighted_word_probability(word, probabilities):
    value = Fraction(1)
    for symbol in word:
        value *= probabilities[symbol]
    return value


def brute_entry(probabilities, window_length):
    n = len(probabilities)
    total = Fraction(0)
    target = set(range(n))
    for word in product(range(n), repeat=window_length + 1):
        if set(word[:window_length]) != target and set(word[1:]) == target:
            total += weighted_word_probability(word, probabilities)
    return total


def formula_entry(probabilities, window_length):
    n = len(probabilities)
    total = Fraction(0)
    for a in range(n):
        onto_middle = Fraction(0)
        for word in product((b for b in range(n) if b != a), repeat=window_length - 1):
            if set(word) == set(range(n)) - {a}:
                onto_middle += weighted_word_probability(word, probabilities)
        total += probabilities[a] * (1 - probabilities[a]) * onto_middle
    return total


families = [
    (Fraction(2, 5), Fraction(3, 5)),
    (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)),
    (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 8)),
]
for probabilities in families:
    n = len(probabilities)
    for window_length in range(n, min(n + 5, 8)):
        brute = brute_entry(probabilities, window_length)
        derived = formula_entry(probabilities, window_length)
        assert brute == derived, (probabilities, window_length)
        checks += 1
        if n == 2:
            p, q = probabilities
            assert derived == p * q**window_length + q * p**window_length
            checks += 1

for M in range(2, 30):
    for num in range(1, 20):
        p = Fraction(num, 20)
        q = 1 - p
        r = p / q
        derivative = q**M - M * p * q**(M - 1) - p**M + M * q * p**(M - 1)
        g = 1 - M * r + M * r**(M - 1) - r**M
        assert derivative == q**M * g
        checks += 1

for M in range(4, 60):
    # Strict finite sign bracket: a positive root lies between 1/M and 2/M.
    rlo, rhi = Fraction(1, M), Fraction(2, M)
    g = lambda r: 1 - M * r + M * r**(M - 1) - r**M
    assert g(rlo) > 0 and g(rhi) < 0
    checks += 1

p = (1 - 1 / 3**0.5) / 2
u = p * (1 - p)
assert isclose(u, 1 / 6, abs_tol=1e-15)
assert isclose(p * (1 - p)**4 + (1 - p) * p**4, 1 / 12, abs_tol=1e-15)
checks += 2

for M in [30, 50, 75, 100]:
    p = 1 / (M + 1)
    flux = p * (1 - p)**M + (1 - p) * p**M
    assert abs(flux * M - exp(-1)) < 0.015
    checks += 1

print(f"VERIFY_OK: {checks} exact finite identities, sign checks, and asymptotic sanity checks")
