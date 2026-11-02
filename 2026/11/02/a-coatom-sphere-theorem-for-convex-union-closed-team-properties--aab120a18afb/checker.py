#!/usr/bin/env python3
"""Independent finite-case checks for the weak-ideal lattice sphere theorem.

Only Python's standard library is needed.  All set families are encoded as bitmasks
whose bit indexed by t records whether the team t is a member.
"""
from itertools import combinations
from math import comb


def proper_universe(n):
    return (1 << (1 << n)) - 1


def is_weak_ideal(f, n):
    teams = [a for a in range(1 << n) if f & (1 << a)]
    for a in teams:
        for b in teams:
            if not (f & (1 << (a | b))):
                return False
            if (a & b) == a:
                for c in range(1 << n):
                    if (a & c) == a and (c & b) == c and not f & (1 << c):
                        return False
    return True


def all_weak_ideals(n):
    # Choose a nonempty upward-closed set of teams inside P(M), with union M.
    # Being upward-closed inside P(M) forces M to be present automatically.
    families = {0}
    for m in range(1 << n):
        domain = [t for t in range(1 << n) if (t & m) == t]
        for b in range(1, 1 << len(domain)):
            f = sum((1 << domain[j]) for j in range(len(domain)) if (b >> j) & 1)
            if all(not (f & (1 << a)) or (f & (1 << c))
                   for a in domain for c in domain if (a & c) == a):
                families.add(f)
    return sorted(families, key=lambda f: (f.bit_count(), f))


def mobius_from_bottom(fams, full):
    mu = {}
    for f in fams:
        if f == 0:
            mu[f] = 1
        else:
            mu[f] = -sum(v for g, v in mu.items() if (g & f) == g)
    return mu[full]


def run():
    for n in range(1, 5):
        fams = all_weak_ideals(n)
        full = proper_universe(n)
        assert fams[0] == 0 and full in fams
        assert all(is_weak_ideal(f, n) for f in fams)
        if n <= 4:
            direct = {f for f in range(1 << (1 << n)) if is_weak_ideal(f, n)}
            assert direct == set(fams), (n, len(direct), len(fams))
        # Numerically verify all predicted coatoms and their maximality.
        coatoms = [f for f in fams if f != full and not any(
            f != g and g != full and (f & g) == f for g in fams)]
        c0 = full & ~(1 << 0)
        predicted = {c0}
        for i in range(n):
            predicted.add(sum((1 << a) for a in range(1 << n) if not (a >> i) & 1))
        assert set(coatoms) == predicted, (n, coatoms, predicted)
        assert all(f == full or any((f & c) == f for c in predicted) for f in fams)
        # Verify the claimed pattern of every coatom intersection.
        for bitset in range(1, 1 << len(coatoms)):
            inter = full
            for j, coatom in enumerate(coatoms):
                if (bitset >> j) & 1:
                    inter &= coatom
            assert (inter == 0) == (bitset == (1 << len(coatoms)) - 1)
        mu = mobius_from_bottom(fams, full)
        assert mu == (-1) ** (n - 1), (n, mu)
        print(f'n={n} weak_ideals={len(fams)} coatoms={len(coatoms)} mobius={mu} OK')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    run()
