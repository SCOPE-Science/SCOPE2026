from fractions import Fraction
from itertools import product

VALUES = (Fraction(-1), Fraction(1), Fraction(2))
RATIOS = (Fraction(1, 5), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3), Fraction(5))
PARTITIONS = (((0, 1), ()), ((), (0, 1)), ((0,), (1,)), ((1,), (0,)))

def wmms(values, weights, i):
    row = values[i]
    best = None
    for p1, p2 in PARTITIONS:
        a = sum((row[k] for k in p1), Fraction(0)) / weights[0]
        b = sum((row[k] for k in p2), Fraction(0)) / weights[1]
        candidate = min(a, b)
        best = candidate if best is None else max(best, candidate)
    return weights[i] * best

def has_exact_allocation(values, weights):
    targets = (wmms(values, weights, 0), wmms(values, weights, 1))
    for mask in range(4):
        u0 = sum((values[0][k] for k in range(2) if mask & (1 << k)), Fraction(0))
        u1 = sum((values[1][k] for k in range(2) if not (mask & (1 << k))), Fraction(0))
        if u0 >= targets[0] and u1 >= targets[1]:
            return True
    return False

profiles = 0
for flat in product(VALUES, repeat=4):
    values = (flat[:2], flat[2:])
    for ratio in RATIOS:
        assert has_exact_allocation(values, (ratio, Fraction(1))), (values, ratio)
        profiles += 1
print(f"PASS: {profiles} exact-arithmetic profile/ratio checks; finite sanity check only.")
