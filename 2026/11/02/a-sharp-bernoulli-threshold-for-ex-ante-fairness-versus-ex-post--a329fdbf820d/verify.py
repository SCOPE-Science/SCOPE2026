"""Independent, finite exact arithmetic checks of the stated Bernoulli-allocation theorem.

Usage: python3 verify.py
No external libraries are used.
"""
from itertools import product
from math import comb
from fractions import Fraction


def enumerated_success(r, t):
    """Enumerate all valuations for each agent separately, then combine counts."""
    wins_heavy = wins_other = 0
    for bits in product((0, 1), repeat=r + 1):
        heavy_plus = r * bits[0] + sum(bits[1:1+t])
        other_plus = sum(bits[1+t:])
        if heavy_plus >= other_plus:
            wins_heavy += 1
        if other_plus >= heavy_plus:
            wins_other += 1
    return Fraction(wins_heavy * wins_other, 2 ** (2 * (r+1)))


def theorem_probability(r, t):
    assert r >= 1 and 0 <= t <= r
    T = 2 ** (r + 1)
    if t == 0:
        return Fraction((2 ** r + 1) ** 2, T ** 2)
    S_t = sum(comb(r, j) for j in range(t, r+1))
    S_t1 = sum(comb(r, j) for j in range(t+1, r+1))
    return Fraction(S_t * (T - S_t1), T*T)


def peak_by_crossing(r):
    if r <= 2:
        return [0]
    T = 2 ** (r + 1)
    S = [sum(comb(r, k) for k in range(t, r+1)) for t in range(r+2)]
    for t in range(1, r):
        test = (r+1)*S[t+1] - (t+1)*T
        if test <= 0:
            return [t, t+1] if test == 0 else [t]
    return [r]


def check():
    tests = 0
    for r in range(1, 11):
        for t in range(r+1):
            lhs = enumerated_success(r, t)
            rhs = theorem_probability(r, t)
            assert lhs == rhs, (r,t,lhs,rhs)
            tests += 1
    peaks = 0
    for r in range(1, 201):
        values = [theorem_probability(r,t) for t in range(r+1)]
        maximum = max(values)
        actual = [t for t,p in enumerate(values) if p == maximum]
        assert actual == peak_by_crossing(r), (r,actual,peak_by_crossing(r))
        assert (maximum > values[0]) == (r >= 3), (r,actual)
        peaks += 1
    print(f'VERIFY_OK direct_exact_cases={tests} crossing_threshold_cases={peaks} r3_p0={theorem_probability(3,0)} r3_p1={theorem_probability(3,1)}')


if __name__ == '__main__':
    check()
