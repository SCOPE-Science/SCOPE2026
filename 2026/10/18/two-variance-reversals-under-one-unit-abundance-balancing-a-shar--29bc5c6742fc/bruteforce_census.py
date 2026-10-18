#!/usr/bin/env python3
"""Alternate finite-census certificate using direct equiprobable sample subsets."""
from itertools import combinations
from fractions import Fraction


def partitions(total, maximum=None):
    if maximum is None:
        maximum = total
    if total == 0:
        yield ()
    for first in range(1, min(total, maximum) + 1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def variance_direct(profile, sample_size):
    labels = tuple(label for label, count in enumerate(profile) for _ in range(count))
    all_values = [len({labels[i] for i in selection})
                  for selection in combinations(range(len(labels)), sample_size)]
    size = len(all_values)
    mean = Fraction(sum(all_values), size)
    return Fraction(sum(z*z for z in all_values), size) - mean*mean


counts = []
for n in range(2, 9):
    transfers = set()
    for profile in partitions(n):
        for i in range(len(profile)):
            for j in range(len(profile)):
                if i != j and profile[i] >= profile[j] + 2:
                    other = list(profile)
                    other[i] -= 1
                    other[j] += 1
                    transfers.add((profile, tuple(sorted(other))))
    exceptional = []
    for before, after in transfers:
        nonzero = []
        for m in range(1, n):
            delta = variance_direct(after, m) - variance_direct(before, m)
            if delta:
                nonzero.append(1 if delta > 0 else -1)
        changes = sum(nonzero[j] != nonzero[j - 1] for j in range(1, len(nonzero)))
        if changes >= 2:
            exceptional.append((before, after))
    assert len(transfers) == {2: 0, 3: 0, 4: 1, 5: 2, 6: 5, 7: 9, 8: 17}[n]
    assert sorted(exceptional) == ([( (4, 3, 1), (2, 2, 4) )] if n == 8 else [])
    counts.append((n, len(transfers), len(exceptional)))
for row in counts:
    print(*row)
print('DIRECT FINITE-CENSUS CERTIFICATE PASS')
