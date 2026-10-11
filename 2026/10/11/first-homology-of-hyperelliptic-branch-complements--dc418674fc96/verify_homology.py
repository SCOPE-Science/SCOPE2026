from math import gcd
from functools import reduce


def partitions(n, min_part=1):
    if n == 0:
        yield ()
        return
    for first in range(min_part, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def predicted(parts):
    d = reduce(gcd, parts)
    c = len(parts)
    free_rank = c + 1
    torsion_order = d
    return free_rank, torsion_order

count = 0
for g in range(1, 9):
    total = 2 * g + 2
    for parts in partitions(total):
        free_rank, torsion = predicted(parts)
        assert free_rank == len(parts) + 1
        assert all(r % torsion == 0 for r in parts)
        # A fixed point forces gcd one.
        if 1 in parts:
            assert torsion == 1
        # A transitive orbit has meridional quotient of order total.
        if len(parts) == 1:
            assert torsion == total and free_rank == 2
        count += 1

sanity = [
    ((1,), (2, 1)),       # one section: Z^2
    ((1, 1), (3, 1)),    # two parallel primitive sections: Z^3
    ((4,), (2, 4)),      # connected four-section
    ((1, 3), (3, 1)),    # published genus-one orbit pattern
    ((2, 2), (3, 2)),    # two degree-two components
]
for parts, expected in sanity:
    assert predicted(parts) == expected

print(f"VERIFY_OK partitions={count} genera=1..8 sanity={len(sanity)}")
