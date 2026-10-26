#!/usr/bin/env python3
"""Finite brute-force verification of partial rooted-tree involution counts."""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb, factorial, log


def injections_on_two():
    for r in range(3):
        for ds in combinations('01', r):
            for rs in combinations('01', r):
                for dst in permutations(rs):
                    yield tuple(zip(ds, dst))


def enumerate_maps(height):
    maps = [ {'': ''} ]
    for level in range(1, height + 1):
        next_maps = []
        for inj in injections_on_two():
            for chosen in product(maps, repeat=len(inj)):
                f = {'': ''}
                for (src, dst), sub in zip(inj, chosen):
                    for x, y in sub.items():
                        f[src + x] = dst + y
                next_maps.append(f)
        maps = next_maps
        expected = 2 ** (2 ** (level + 1) - 1) - 1
        assert len(maps) == expected, (level, len(maps), expected)
    return maps


def self_inverse(mapping):
    return all((image in mapping and mapping[image] == source)
               for source, image in mapping.items())


def mul(a, b):
    c = Counter()
    for x, ax in a.items():
        for y, by in b.items():
            c[x + y] += ax * by
    return c


def scaled_sum(*args):
    out = Counter()
    for coef, poly in args:
        for n, val in poly.items():
            out[n] += coef * val
    return out


def step(total, invol):
    # Root plus zero, one, or two active children; transposition contributes t^2 substitution.
    mapped = {2 * n: v for n, v in total.items()}
    total_next = scaled_sum((1, {0: 1}), (4, total), (2, mul(total, total)))
    invol_next = scaled_sum((1, {0: 1}), (2, invol), (1, mul(invol, invol)), (1, mapped))
    return Counter({n + 1: v for n, v in total_next.items()}), Counter({n + 1: v for n, v in invol_next.items()})


def main():
    full = Counter({1: 1})
    inv = Counter({1: 1})
    row = []
    for h in range(4):
        maps = enumerate_maps(h)
        raw_full = Counter(len(f) for f in maps)
        raw_inv = Counter(len(f) for f in maps if self_inverse(f))
        assert raw_full == full, (h, raw_full, full)
        assert raw_inv == inv, (h, raw_inv, inv)
        row.append((h, len(maps), sum(raw_inv.values())))
        if h < 3:
            full, inv = step(full, inv)
    assert row == [(0, 1, 1), (1, 7, 5), (2, 127, 43), (3, 32767, 2063)]
    # Verify recurrence independently at larger heights, where full enumeration is infeasible.
    for h in range(4, 7):
        full, inv = step(full, inv)
        assert sum(full.values()) == 2 ** (2 ** (h + 1) - 1) - 1
        assert sum(inv.values()) >= 1
    from decimal import Decimal, localcontext
    u = 2
    with localcontext() as ctx:
        ctx.prec = 55
        vals = []
        for h in range(1, 8):
            u = u * u + 2 ** (2 ** h - 1)
            vals.append(Decimal(u).ln() / Decimal(2 ** h))
        c7 = vals[-1]
        print('height,total,involutions:', row)
        print('height7-normalized-log:', c7)
        print('decay-rate:', 2 * Decimal(2).ln() - c7)
    # An additional independent check of the first-moment recurrence against
    # derivatives extracted from the rank polynomials for small heights.
    pp = Counter({1: 1})
    jj = Counter({1: 1})
    f, u, m, v = 1, 2, 1, 1
    for h in range(7):
        assert sum(pp.values()) == f
        assert sum(jj.values()) == u - 1
        assert sum(k * val for k, val in pp.items()) == m
        assert sum(k * val for k, val in jj.items()) == v
        if h < 6:
            pp, jj = step(pp, jj)
            old_f, old_u, old_m, old_v = f, u, m, v
            f = 1 + 4 * old_f + 2 * old_f * old_f
            u = old_u * old_u + old_f + 1
            m = f + 4 * (old_f + 1) * old_m
            v = (u - 1) + 2 * old_u * old_v + 2 * old_m
    # Higher integer recurrence supplies a quickly converging density constant.
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 48
        for h in range(7, 12):
            old_f, old_u, old_m, old_v = f, u, m, v
            f = 1 + 4 * old_f + 2 * old_f * old_f
            u = old_u * old_u + old_f + 1
            m = f + 4 * (old_f + 1) * old_m
            v = (u - 1) + 2 * old_u * old_v + 2 * old_m
        q = Decimal(v)/(Decimal(2**11)*Decimal(u))
        approx = (q + Decimal(2)**(-11))/2
        assert abs(approx - Decimal('0.708075950588044670778')) < Decimal('1e-20')
        print('binary-involution-domain-density:', approx)
    print('ALL_ROOTED_TREE_PARTIAL_INVOLUTION_CHECKS_PASSED')

if __name__ == '__main__':
    main()
