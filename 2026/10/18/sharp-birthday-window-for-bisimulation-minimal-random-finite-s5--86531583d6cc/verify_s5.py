"""Exact finite checks of bisimulation irredundancy in one-agent S5 models.

Usage: python verify_s5.py
The independent route refines modal equivalence signatures directly, whereas
its prediction is computed through a coefficient formula.
"""
from itertools import product
from math import comb, factorial


def partitions(n):
    # Standard restricted-growth labels, uniquely encoding set partitions.
    if n == 0:
        yield ()
        return
    def extend(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for x in range(maximum + 2):
            yield from extend(prefix + [x], max(maximum, x))
    yield from extend([0], 0)


def bisimulation_classes(partition, colors):
    n = len(partition)
    cls = list(colors)
    while True:
        signatures = []
        for i in range(n):
            successor_classes = frozenset(cls[j] for j in range(n)
                                          if partition[j] == partition[i])
            signatures.append((colors[i], successor_classes))
        unique = {s: k for k, s in enumerate(sorted(set(signatures)))}
        updated = [unique[s] for s in signatures]
        # Use equivalence relations, not the numeric names of classes.
        before = {(i, j) for i in range(n) for j in range(n) if cls[i] == cls[j]}
        after = {(i, j) for i in range(n) for j in range(n) if updated[i] == updated[j]}
        if before == after:
            return len(set(updated))
        cls = updated


def coefficient_prediction(n, q):
    # Extract [z^n] prod_{j=1}^q (1+z^j)^binom(q,j).
    coefficients = [0] * (n+1)
    coefficients[0] = 1
    for j in range(1, min(q, n)+1):
        exponent = comb(q, j)
        # Each of the exponent distinct color subsets is present at most once.
        for _ in range(exponent):
            for t in range(n, j-1, -1):
                coefficients[t] += coefficients[t-j]
    return factorial(n)*coefficients[n]


def run():
    cases = 0
    for n in range(1, 6):
        ps = list(partitions(n))
        for q in range(1, 5):
            brute = sum(bisimulation_classes(part, colors) == n
                        for part in ps for colors in product(range(q), repeat=n))
            prediction = coefficient_prediction(n, q)
            assert brute == prediction, (n, q, brute, prediction)
            cases += 1
    assert coefficient_prediction(2, 2) == 4
    assert coefficient_prediction(3, 2) == 12
    print(f'VERIFY_OK {cases} independent partition-refinement/coefficient comparisons')

if __name__ == '__main__':
    run()
