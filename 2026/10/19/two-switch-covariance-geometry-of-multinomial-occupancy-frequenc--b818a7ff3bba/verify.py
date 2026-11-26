"""Exact verification of four singleton–doubleton covariance checkpoints."""
from fractions import Fraction
from itertools import product
from math import prod


def covariance(n):
    weights = (1, 15, 16)
    total = singleton = doubleton = cross = 0
    for allocation in product(range(3), repeat=n):
        occ = [allocation.count(i) for i in range(3)]
        a, b = occ.count(1), occ.count(2)
        weight = prod(weights[i] for i in allocation)
        total += weight
        singleton += a * weight
        doubleton += b * weight
        cross += a * b * weight
    assert total == 32**n
    return Fraction(total * cross - singleton * doubleton, total**2)


if __name__ == '__main__':
    expected = {
        3: Fraction(427917, 4194304),
        4: Fraction(-10632785853, 34359738368),
        9: Fraction(464148085603947606981, 1208925819614629174706176),
        10: Fraction(-189451469679866467748560575, 158456325028528675187087900672),
    }
    observed = {n: covariance(n) for n in expected}
    assert observed == expected
    assert [1 if v > 0 else -1 if v < 0 else 0 for v in observed.values()] == [1, -1, 1, -1]
    for n, value in observed.items():
        print(n, value)
