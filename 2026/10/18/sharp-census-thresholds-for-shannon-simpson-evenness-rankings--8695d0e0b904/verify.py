"""Exact integer-partition certificate for fixed-richness Hill-evenness comparisons.

Run: python3 verify.py  (Python >= 3.8; standard library only).
"""
from functools import lru_cache
from itertools import combinations

@lru_cache(None)
def partitions(total, smallest=1):
    """All nondecreasing positive partitions of total, with no part below smallest."""
    if total == 0:
        return ((),)
    return tuple(
        (part,) + tail
        for part in range(smallest, total + 1)
        for tail in partitions(total - part, part)
    )

def invariants(parts):
    second = sum(v * (v + 2) for v in parts)
    shannon_product = 1
    for v in parts:
        shannon_product *= (v + 1) ** (v + 1)
    return second, shannon_product

def classify(excess):
    profiles = [(p, *invariants(p)) for p in partitions(excess)]
    reversals = []
    quadratic_ties = []
    product_ties = []
    for a, b in combinations(profiles, 2):
        if (a[1] - b[1]) * (a[2] - b[2]) < 0:
            reversals.append((a[0], b[0]))
        if a[1] == b[1] and a[2] != b[2]:
            quadratic_ties.append((a[0], b[0]))
        if a[2] == b[2] and a[1] != b[1]:
            product_ties.append((a[0], b[0]))
    return profiles, reversals, quadratic_ties, product_ties

assert [len(partitions(k)) for k in range(8)] == [1, 1, 2, 3, 5, 7, 11, 15]
for excess in range(8):
    profiles, reversed_pairs, quad_ties, product_ties = classify(excess)
    if excess <= 5:
        assert not reversed_pairs and not quad_ties and not product_ties
    elif excess == 6:
        assert reversed_pairs == [] and product_ties == []
        assert {frozenset(p) for p in quad_ties} == {
            frozenset(((1, 1, 1, 3), (2, 2, 2))),
            frozenset(((1, 1, 4), (3, 3))),
        }
    else:
        assert {frozenset(p) for p in reversed_pairs} == {
            frozenset(((1, 1, 5), (3, 4)))
        }
    print(f'excess={excess} partition_types={len(profiles)} '
          f'strict_reversals={len(reversed_pairs)} '
          f'Hill2_tie_disagreements={len(quad_ties)}')

# Confirm explicit comparisons with arbitrary species count n >= 3.
for n in range(3, 61):
    A = (1,) * (n - 3) + (2, 2, 6)
    B = (1,) * (n - 3) + (1, 4, 5)
    assert sum(A) == sum(B) == n + 7
    assert sum(z * z for z in A) == n + 41
    assert sum(z * z for z in B) == n + 39
    assert __import__('math').prod(z ** z for z in A) == 746496
    assert __import__('math').prod(z ** z for z in B) == 800000
print('All exact finite classifications and witness tests passed.')
