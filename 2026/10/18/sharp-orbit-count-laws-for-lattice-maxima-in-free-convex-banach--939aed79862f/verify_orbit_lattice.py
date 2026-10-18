"""Exact finite checks for the orbit-averaging lattice-join theorem.

This script checks concrete lower witnesses and upper certificates. It is
not a substitute for the all-dimensions analytic proof.
"""
from fractions import Fraction
from itertools import combinations
from math import prod


def all_compositions(n):
    for cuts_mask in range(1 << (n - 1)):
        starts = [0] + [i for i in range(1, n) if cuts_mask & (1 << (i-1))] + [n]
        yield [tuple(range(starts[j], starts[j + 1])) for j in range(len(starts)-1)]


def averaged_positive(x, block):
    return Fraction(sum(abs(x[i]) for i in block), len(block))


def orbit_cost(x, block, p):
    return sum((Fraction(abs(x[i])**p) for i in block), Fraction()) / len(block)


certificates = witnesses = random_checks = 0
for n in range(1, 8):
    for partition in all_compositions(n):
        r = len(partition)
        for p in (1,2,3):
            for k in range(1, 8):
                q=min(k, r)
                # For every binary point, the orbit-specific Jensen certificate.
                for mask in range(1 << n):
                    x = tuple((mask >> i) & 1 for i in range(n))
                    join = max(averaged_positive(x, block) for block in partition[:q])
                    upper = sum((orbit_cost(x, block, p) for block in partition[:q]), Fraction())
                    assert join**p <= upper, (n, partition, p, k, mask)
                    certificates += 1
                # The q full-orbit indicator rows obey all weak-p budgets.
                rows = [tuple(int(i in block) for i in range(n)) for block in partition[:q]]
                budgets = [sum(abs(row[i])**p for row in rows) for i in range(n)]
                assert max(budgets) == 1
                norm_power = sum(max(averaged_positive(row, block) for block in partition[:q])**p for row in rows)
                assert norm_power == q
                witnesses += 1
print(f'PASS {certificates} exact binary orbit-cost certificates; {witnesses} exact attaining multirow witnesses.')
