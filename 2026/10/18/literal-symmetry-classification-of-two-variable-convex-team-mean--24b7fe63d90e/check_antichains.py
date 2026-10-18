#!/usr/bin/env python3
"""Independent certificate: enumerate pairs of minimal/maximal antichains."""
from itertools import product
from collections import Counter


P = range(16)

def leq(a, b):
    return a & b == a


def antichains():
    out = []
    for f in range(65536):
        X = [i for i in P if f & (1 << i)]
        if all(a == b or (not leq(a, b) and not leq(b, a))
               for a in X for b in X):
            out.append((f, X))
    return out


def signed_group():
    group = set()
    for swap in (0, 1):
        for flip_x, flip_y in product((0, 1), repeat=2):
            p = []
            for v in range(4):
                x, y = divmod(v, 2)
                if swap:
                    x, y = y, x
                p.append(2 * (x ^ flip_x) + (y ^ flip_y))
            group.add(tuple(p))
    return tuple(sorted(group))


def map_antichain(mask, g):
    out = 0
    for subset in P:
        if mask >> subset & 1:
            changed_subset = 0
            for v in range(4):
                if subset >> v & 1:
                    changed_subset |= 1 << g[v]
            out |= 1 << changed_subset
    return out


def compatible(lo, hi):
    return (all(any(leq(x, y) for y in hi) for x in lo)
            and all(any(leq(x, y) for x in lo) for y in hi))


def main():
    ac = antichains()
    assert len(ac) == 168
    pairs = {(0, 0)}  # Unique representation of the empty convex family.
    for lm, lo in ac:
        if not lo:
            continue
        for um, hi in ac:
            if hi and compatible(lo, hi):
                pairs.add((lm, um))
    assert len(pairs) == 3938
    G = signed_group()
    assert len(G) == 8
    fix = []
    for g in G:
        mapped = lambda p: (map_antichain(p[0], g), map_antichain(p[1], g))
        fix.append(sum(mapped(pair) == pair for pair in pairs))
    assert sorted(fix) == [26, 26, 186, 186, 186, 526, 526, 3938]
    assert sum(fix) == 5600
    unseen = pairs.copy()
    sizes = Counter()
    while unseen:
        pair = min(unseen)
        orb = {(map_antichain(pair[0], g), map_antichain(pair[1], g)) for g in G}
        assert orb <= unseen
        unseen -= orb
        sizes[len(orb)] += 1
    assert dict(sizes) == {1: 26, 2: 54, 4: 289, 8: 331}
    assert sum(sizes.values()) == 700
    print('ANTICHAIN_CERT_OK antichains=168 valid_pairs=3938 '
          'fixed_sorted=[26,26,186,186,186,526,526,3938] '
          'orbits=700 sizes={1:26,2:54,4:289,8:331}')


if __name__ == '__main__':
    main()
