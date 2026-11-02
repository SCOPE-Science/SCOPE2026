"""Exact exhaustive tests of monotone maximal subgroup-chain counts.

Run: python3 verify_increasing_dihedral.py
No third-party dependencies. Direct subgroup enumeration is independent of
those formulas and is used only for small groups; the general proof is symbolic.
"""
from functools import lru_cache
from itertools import product
from math import prod


def group_table(moduli, dihedral):
    points = tuple(product(*(range(t) for t in moduli)))
    address = {a: i for i, a in enumerate(points)}
    n = len(points)
    size = (2 if dihedral else 1) * n
    table = [[0] * size for _ in range(size)]
    for x in range(size):
        ax, sx = points[x % n], x // n
        for y in range(size):
            ay, sy = points[y % n], y // n
            az = tuple((a + (-1 if sx else 1) * b) % t
                       for a, b, t in zip(ax, ay, moduli))
            table[x][y] = address[az] + n * ((sx + sy) % 2)
    return table


def enumerate_subgroups(table):
    n = len(table)
    def closure(gens):
        seen = {0}
        work = [0]
        while work:
            x = work.pop()
            for g in gens:
                y = table[x][g]
                if y not in seen:
                    seen.add(y)
                    work.append(y)
        return frozenset(seen)
    subgroups = [frozenset({0})]
    observed = set(subgroups)
    for h in subgroups:
        for x in range(n):
            if x in h:
                continue
            k = closure(tuple(h) + (x,))
            if k not in observed:
                observed.add(k)
                subgroups.append(k)
    full = frozenset(range(n))
    assert full in observed
    covers = {}
    for h in subgroups:
        upper = [k for k in subgroups if h < k]
        covers[h] = [k for k in upper if not any(h < j < k for j in upper)]
    return full, covers


def count_chains(full, covers, monotone):
    @lru_cache(None)
    def count(h, last):
        if h == full:
            return 1
        result = 0
        for k in covers[h]:
            index = len(k) // len(h)
            if not monotone or index >= last:
                result += count(k, index if monotone else 1)
        return result
    return count(frozenset({0}), 1)


def primary_factors(n):
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            power = 1
            while n % p == 0:
                n //= p
                power *= p
            factors.append(power)
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def primary_flags(moduli):
    """Independently count primary subgroup chains of the abelian kernel."""
    table = group_table(moduli, False)
    full, covers = enumerate_subgroups(table)
    return count_chains(full, covers, True)


def predicted(moduli):
    a = prod(moduli)
    odd = a
    while odd % 2 == 0:
        odd //= 2
    return primary_flags(moduli) * (2 * a - odd)


def run():
    cases = [(2,), (3,), (4,), (5,), (6,), (8,), (10,), (12,),
             (2,2), (2,4), (3,3), (2,2,2), (2,3), (4,3), (2,2,3)]
    for moduli in cases:
        full, covers = enumerate_subgroups(group_table(moduli, True))
        direct = count_chains(full, covers, True)
        forecast = predicted(moduli)
        assert direct == forecast, (moduli, direct, forecast)
        total = count_chains(full, covers, False)
        assert 0 < direct <= total
        print(f"{moduli!s:14s}: monotone={direct:5d}, all={total:5d}, "
              f"subgroups={len(covers):3d}")
    print("VERIFY_OK")


if __name__ == "__main__":
    run()
