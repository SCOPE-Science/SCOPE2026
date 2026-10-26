"""Exact finite checks for reflexive meet-compatible relations on finite chains."""
from itertools import product
from math import factorial, comb


def relation_from_thresholds(n, upper, lower):
    relation = {(i, i) for i in range(n)}
    for i in range(n):
        relation.update((i, j) for j in range(i + 1, upper[i] + 1))
        relation.update((j, i) for j in range(i + 1, lower[i] + 1))
    return frozenset(relation)


def meet_closed(relation):
    return all((min(a, c), min(b, d)) in relation
               for (a, b) in relation for (c, d) in relation)


def count_direct(n):
    off_diagonal = [(i, j) for i in range(n) for j in range(n) if i != j]
    diagonal = {(i, i) for i in range(n)}
    count = symmetric = equivalence = 0
    size_profile = [0] * (n * (n - 1) + 1)
    relations = set()
    for bits in product((0, 1), repeat=len(off_diagonal)):
        relation = frozenset(diagonal | {p for p, b in zip(off_diagonal, bits) if b})
        if not meet_closed(relation):
            continue
        relations.add(relation)
        count += 1
        size_profile[len(relation) - n] += 1
        if all((b, a) in relation for a, b in relation):
            symmetric += 1
            if all(((a, b) not in relation or (b, c) not in relation or (a, c) in relation)
                   for a in range(n) for b in range(n) for c in range(n)):
                equivalence += 1
    return relations, count, symmetric, equivalence, size_profile


def polynomial_profile(n):
    coeff = [1]
    for k in range(1, n + 1):
        for _ in range(2):
            nxt = [0] * (len(coeff) + k - 1)
            for j, value in enumerate(coeff):
                for shift in range(k):
                    nxt[j + shift] += value
            coeff = nxt
    return coeff


for n in range(1, 5):
    direct, total, symmetric, congruences, profile = count_direct(n)
    expected = factorial(n) ** 2
    assert total == expected, (n, total, expected)
    assert symmetric == factorial(n), (n, symmetric)
    assert congruences == 2 ** (n - 1), (n, congruences)
    assert profile == polynomial_profile(n), (n, profile)
    thresholds = product(*(range(i, n) for i in range(n)))
    reconstructed = set()
    for upper in thresholds:
        for lower in product(*(range(i, n) for i in range(n))):
            relation = relation_from_thresholds(n, upper, lower)
            assert meet_closed(relation), (n, upper, lower)
            reconstructed.add(relation)
    assert reconstructed == direct, n
    print(f'n={n}: diagonal={total}, symmetric={symmetric}, congruences={congruences}')

n = 5
num = 0
seen = set()
for upper in product(*(range(i, n) for i in range(n))):
    for lower in product(*(range(i, n) for i in range(n))):
        relation = relation_from_thresholds(n, upper, lower)
        assert meet_closed(relation)
        seen.add(relation)
        num += 1
assert num == len(seen) == factorial(n) ** 2
assert sum(polynomial_profile(n)) == num
print(f'n={n}: {num} generated distinct compatible relations verified')
print('VERIFY_OK')
