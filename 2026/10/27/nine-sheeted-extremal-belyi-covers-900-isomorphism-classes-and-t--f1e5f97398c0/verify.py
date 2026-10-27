"""Exact finite verification for nine-sheeted totally ramified Belyi covers.

Run with standard Python 3: python verify.py
Every 9-cycle is encoded once by its orbit of 0, so the search is exhaustive.
"""
from collections import Counter
from itertools import permutations
from fractions import Fraction
from math import factorial

N = 9
SIGMA = tuple((i + 1) % N for i in range(N))


def cycle_from_order(order):
    """Construct (0, order[0], ..., order[7])."""
    out = [None] * N
    old = 0
    for new in order:
        out[old] = new
        old = new
    out[old] = 0
    return tuple(out)


def is_full_cycle(p):
    x = 0
    for k in range(1, N + 1):
        x = p[x]
        if x == 0:
            return k == N
    raise AssertionError("invalid permutation")


def conjugate_by_sigma_power(tau, k):
    """Return sigma**k * tau * sigma**(-k)."""
    return tuple((tau[(i - k) % N] + k) % N for i in range(N))


admissible = set()
all_cycles = 0
for order in permutations(range(1, N)):
    tau = cycle_from_order(order)
    assert is_full_cycle(tau)
    all_cycles += 1
    if is_full_cycle(tuple(SIGMA[tau[i]] for i in range(N))):
        admissible.add(tau)

assert all_cycles == factorial(8) == 40320
assert len(admissible) == 8064

# Direct orbit partition, independent of Burnside's formula.
remaining = set(admissible)
orbit_sizes = Counter()
while remaining:
    tau = next(iter(remaining))
    orbit = {conjugate_by_sigma_power(tau, k) for k in range(N)}
    assert orbit <= remaining
    remaining -= orbit
    orbit_sizes[len(orbit)] += 1

assert orbit_sizes == {1: 3, 3: 2, 9: 895}
assert sum(orbit_sizes.values()) == 900

# A second count: fixed points of the two possible nonidentity orders.
fix_order_3 = sum(conjugate_by_sigma_power(t, 3) == t for t in admissible)
fix_order_9 = sum(conjugate_by_sigma_power(t, 1) == t for t in admissible)
assert (fix_order_3, fix_order_9) == (9, 3)
assert (8064 + 2 * fix_order_3 + 6 * fix_order_9) // 9 == 900

# The orbit of a triple has cardinality 9 / |Aut(cover)|.
aut_distribution = {9 // s: count for s, count in sorted(orbit_sizes.items())}
assert aut_distribution == {9: 3, 3: 2, 1: 895}
assert sum(Fraction(count, order) for order, count in aut_distribution.items()) == 896

print("ALL_CYCLES=40320")
print("ADMISSIBLE=8064")
print("FIXED_ORDER_3=9")
print("FIXED_ORDER_9=3")
print("AUTOMORPHISM_ORDER_COUNTS=1:895,3:2,9:3")
print("UNROOTED_BELYI_COVERS=900")
print("VERIFY_OK")
