"""Exact checks for covariance signs in symmetric unit-reinforcement urns.

Run: python verify.py
Only Python standard-library modules are required.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def weak_compositions(n, d):
    for separators in combinations(range(n + d - 1), d - 1):
        last = -1
        values = []
        for sep in separators:
            values.append(sep - last - 1)
            last = sep
        values.append(n + d - 2 - last)
        yield tuple(values)


def analytic_covariances(d, n, r):
    total_compositions = comb(n + d - 1, d - 1)
    u = Fraction(d - 1, n + d - 1)
    v = Fraction(comb(n - r + d - 2, d - 2), total_compositions)
    local = u * v * Fraction((d - 1) * r - n,
                             (d - 1) * (d + n - r - 2))
    aggregate = d * u * v * Fraction(d * (r - 1) - 2 * (n - 1),
                                    d + n - r - 2)
    return local, aggregate


def enumerated_covariances(vectors, d, r):
    count = len(vectors)
    z1 = sum(v[0] == 0 for v in vectors)
    xr = sum(v[1] == r for v in vectors)
    both = sum(v[0] == 0 and v[1] == r for v in vectors)
    local = Fraction(both, count) - Fraction(z1 * xr, count * count)
    z_all = [sum(x == 0 for x in v) for v in vectors]
    r_all = [sum(x == r for x in v) for v in vectors]
    aggregate = (Fraction(sum(a * b for a, b in zip(z_all, r_all)), count)
                 - Fraction(sum(z_all) * sum(r_all), count * count))
    return local, aggregate


def polya_count_probabilities(d, n):
    # Exact independent recurrence for draw-by-draw Pólya sampling.
    zero = (0,) * d
    law = {zero: Fraction(1)}
    for step in range(n):
        next_law = {}
        for vector, probability in law.items():
            for color in range(d):
                updated = list(vector)
                updated[color] += 1
                updated = tuple(updated)
                increment = probability * Fraction(1 + vector[color], d + step)
                next_law[updated] = next_law.get(updated, Fraction(0)) + increment
        law = next_law
    return law


def main():
    comparisons = 0
    for d in range(3, 9):
        for n in range(1, 11):
            vectors = list(weak_compositions(n, d))
            assert len(vectors) == comb(n + d - 1, d - 1)
            for r in range(1, n + 1):
                exact = enumerated_covariances(vectors, d, r)
                closed = analytic_covariances(d, n, r)
                assert exact == closed, (d, n, r, exact, closed)
                def sign(value):
                    return (value > 0) - (value < 0)
                assert sign(exact[0]) == sign((d - 1) * r - n)
                assert sign(exact[1]) == sign(d * (r - 1) - 2 * (n - 1))
                comparisons += 1
    for d in range(3, 6):
        for n in range(1, 7):
            law = polya_count_probabilities(d, n)
            benchmark = Fraction(1, comb(n + d - 1, d - 1))
            assert len(law) == comb(n + d - 1, d - 1)
            assert sum(law.values(), Fraction()) == 1
            assert set(law.values()) == {benchmark}
    assert analytic_covariances(5, 4, 2) == (Fraction(1, 70), Fraction(-1, 14))
    assert analytic_covariances(4, 3, 2) == (Fraction(1, 40), Fraction(0))
    assert analytic_covariances(3, 4, 2) == (Fraction(0), Fraction(-1, 5))
    print(f"PASS: {comparisons} exact covariance triples and 18 Pólya recursions")


if __name__ == "__main__":
    main()
