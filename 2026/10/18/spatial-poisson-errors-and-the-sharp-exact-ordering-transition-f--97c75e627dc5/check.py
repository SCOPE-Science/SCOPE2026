"""Exact finite checks for geometric and inhomogeneous exponential-race rankings.

Run with Python 3 and its standard library: python check.py
This verifies rational finite identities; the asymptotic results require the proof.
"""
from fractions import Fraction
from itertools import permutations


def ranking_probability(order, rates):
    remaining = sum(rates)
    value = Fraction(1)
    for label in order:
        value *= rates[label] / remaining
        remaining -= rates[label]
    assert remaining == 0
    return value


def run():
    tests = 0
    for n in range(2, 8):
        ratio_families = [
            [Fraction(1, 3 * n)] * (n - 1),
            [Fraction(1, 4)] * (n - 1),
            [Fraction(i + 1, 5 * n) for i in range(1, n)],
        ]
        for ratios in ratio_families:
            rates = [Fraction(1)]
            for ratio in ratios:
                rates.append(rates[-1] * ratio)
            probabilities = [(order, ranking_probability(order, rates))
                             for order in permutations(range(n))]
            assert sum((p for _, p in probabilities), Fraction(0)) == 1
            tests += 1

            identity_probability = next(p for order, p in probabilities
                                        if order == tuple(range(n)))
            identity_race_formula = Fraction(1)
            for i in range(n):
                identity_race_formula *= rates[i] / sum(rates[i:])
            assert identity_probability == identity_race_formula
            tests += 1

            if len(set(ratios)) == 1:
                ratio = ratios[0]
                identity_geometric_formula = Fraction(1)
                for length in range(2, n + 1):
                    identity_geometric_formula *= (1 - ratio) / (1 - ratio ** length)
                assert identity_probability == identity_geometric_formula
                tests += 1

            for i in range(n):
                for j in range(i + 1, n):
                    event_probability = sum(
                        (p for order, p in probabilities
                         if order.index(j) < order.index(i)), Fraction(0))
                    assert event_probability == rates[j] / (rates[i] + rates[j])
                    tests += 1

            for i in range(n - 2):
                event_probability = sum(
                    (p for order, p in probabilities
                     if order.index(i + 2) < order.index(i + 1) < order.index(i)),
                    Fraction(0))
                exact = (rates[i + 2] / sum(rates[i:i + 3])
                         * rates[i + 1] / sum(rates[i:i + 2]))
                assert event_probability == exact
                tests += 1

            for i in range(n - 1):
                for j in range(i + 2, n - 1):
                    event_probability = sum(
                        (p for order, p in probabilities
                         if (order.index(i + 1) < order.index(i)
                             and order.index(j + 1) < order.index(j))),
                        Fraction(0))
                    expected = (rates[i + 1] / (rates[i] + rates[i + 1])
                                * rates[j + 1] / (rates[j] + rates[j + 1]))
                    assert event_probability == expected
                    tests += 1

            probability_nonadj = sum(
                (p for order, p in probabilities
                 if any(order.index(j) < order.index(i)
                        for i in range(n) for j in range(i + 2, n))),
                Fraction(0))
            union_bound = sum((rates[j] / (rates[i] + rates[j])
                               for i in range(n) for j in range(i + 2, n)),
                              Fraction(0))
            assert probability_nonadj <= union_bound
            tests += 1

    print(f"PASS: {tests} independent exact-rational finite checks")


if __name__ == "__main__":
    run()
