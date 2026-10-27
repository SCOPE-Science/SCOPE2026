"""Exact finite-state replay of a homogeneous competitive ecological sign map.

All updates use rational arithmetic. This program checks finite instances;
it does not establish the infinite-population limit by enumeration.
"""
from fractions import Fraction
from itertools import product
from math import comb


def update(state, interaction):
    n = len(state)
    nxt = []
    total = sum(state)
    for current in state:
        growth = current * (
            2 - current - interaction * (total - current) / (n - 1)
        )
        nxt.append(current + (1 if growth > 0 else -1 if growth < 0 else 0))
    return tuple(nxt)


def predicted(n, k, interaction):
    threshold = (n - 1) * (1 / interaction - 1)
    assert threshold.denominator != 1
    if k > threshold:
        return k
    if n - k > threshold:
        return n - k
    return n


def check():
    values = (
        Fraction(1, 4), Fraction(2, 5), Fraction(3, 5),
        Fraction(4, 7), Fraction(7, 10), Fraction(3, 4),
        Fraction(7, 8), Fraction(9, 10), Fraction(11, 20)
    )
    tests = 0
    for n in range(3, 12):
        for interaction in values:
            threshold = (n - 1) * (1 / interaction - 1)
            if threshold.denominator == 1:
                continue
            group_counts = [0] * (n + 1)
            for state in product((1, 2), repeat=n):
                k = state.count(2)
                after_one = update(state, interaction)
                after_two = update(after_one, interaction)
                after_three = update(after_two, interaction)
                after_four = update(after_three, interaction)
                assert after_four == after_two, (n, interaction, state)
                assert sum(x > 0 for x in after_two) == predicted(n, k, interaction), (
                    n, interaction, state
                )
                if sum(x > 0 for x in after_two) >= 2:
                    assert after_two != after_three, (n, interaction, state)
                else:
                    assert after_three == after_four, (n, interaction, state)
                if all(x > 0 for x in after_two):
                    group_counts[k] += 1
                tests += 1
            observed_full = sum(group_counts)
            formula_full = 2 + sum(
                comb(n, k) for k in range(1, n)
                if n - threshold < k < threshold
            )
            assert observed_full == formula_full, (n, interaction, observed_full)
    print(f"PASS: {tests} exact rational initial states; finite binomial census and two-step entry into a fixed point or period-two orbit")


if __name__ == "__main__":
    check()
