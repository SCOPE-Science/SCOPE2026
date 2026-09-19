from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import ceil, factorial, sqrt


def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for a in range(cap, 0, -1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def exact_law(part):
    n = sum(part)
    counts = Counter(part)
    return {s: Fraction(s * multiplicity, n)
            for s, multiplicity in counts.items()}


def brute_law(part):
    labels = []
    for i, size in enumerate(part):
        labels.extend([i] * size)
    n = len(labels)
    counts = Counter()

    for order in permutations(range(n)):
        chosen = []
        for v in order:
            # In a complete multipartite graph, two vertices are nonadjacent
            # exactly when they are in the same part.
            if all(labels[v] == labels[u] for u in chosen):
                chosen.append(v)
        counts[len(chosen)] += 1

    total = factorial(n)
    return {size: Fraction(count, total) for size, count in counts.items()}


def variance(part):
    n = sum(part)
    s2 = sum(x * x for x in part)
    s3 = sum(x * x * x for x in part)
    return Fraction(s3, n) - Fraction(s2 * s2, n * n)


def predicted_extremizer(n):
    rho = (3 * n + sqrt(9 * n * n - 16 * n)) / 8
    a = ceil(rho)
    return (a,) + (1,) * (n - a)


law_types = 0
for n in range(3, 9):
    for part in partitions(n):
        if len(part) < 2:
            continue
        law_types += 1
        assert brute_law(part) == exact_law(part)

extremal_types = 0
for n in range(3, 41):
    types = [p for p in partitions(n) if len(p) >= 2]
    extremal_types += len(types)
    best = max(variance(p) for p in types)
    winners = [p for p in types if variance(p) == best]
    predicted = predicted_extremizer(n)
    assert winners == [predicted], (n, winners, predicted)

print(f"Exact-law brute-force types through n=8: {law_types} PASS")
print(f"Extremal partition types through n=40: {extremal_types} PASS")
