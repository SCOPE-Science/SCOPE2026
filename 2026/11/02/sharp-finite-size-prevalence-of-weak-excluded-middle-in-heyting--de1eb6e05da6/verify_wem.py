#!/usr/bin/env python3
"""Exact small-poset tests for weak excluded middle in finite downset algebras.

All arithmetic is integral; no random sampling or external dependencies are used.
Natural-order labellings represent every finite poset up to isomorphism.
"""
from fractions import Fraction


def downsets(predecessors):
    n = len(predecessors)
    return [
        s for s in range(1 << n)
        if all(not (s >> i & 1) or (s & d) == d
               for i, d in enumerate(predecessors))
    ]


def extend_order(predecessors):
    """Adjoin a new maximum with each possible old downset as predecessors."""
    for d in downsets(predecessors):
        yield predecessors + (d,)


def components(predecessors):
    n = len(predecessors)
    links = [0] * n
    for top, below in enumerate(predecessors):
        for bottom in range(top):
            if below >> bottom & 1:
                links[top] |= 1 << bottom
                links[bottom] |= 1 << top
    unseen = (1 << n) - 1
    out = []
    while unseen:
        seed = unseen & -unseen
        unseen -= seed
        todo = seed
        comp = seed
        while todo:
            bit = todo & -todo
            todo -= bit
            v = bit.bit_length() - 1
            new = links[v] & unseen
            if new:
                todo |= new
                comp |= new
                unseen &= ~new
        out.append(comp)
    return out


def direct_count(predecessors, all_ideals):
    n = len(predecessors)
    full = (1 << n) - 1
    successes = 0
    for ideal in all_ideals:
        neg = 0
        for i, below in enumerate(predecessors):
            if ((below | (1 << i)) & ideal) == 0:
                neg |= 1 << i
        negneg = 0
        for i, below in enumerate(predecessors):
            if ((below | (1 << i)) & neg) == 0:
                negneg |= 1 << i
        if (neg | negneg) == full:
            successes += 1
    return successes


def structural_count(predecessors, all_ideals):
    successes = 1
    for comp in components(predecessors):
        minima = sum(1 << i for i in range(len(predecessors))
                     if comp >> i & 1 and predecessors[i] == 0)
        all_minima_present = sum(
            1 for ideal in all_ideals
            if (ideal & ~comp) == 0 and (ideal & minima) == minima
        )
        successes *= 1 + all_minima_present
    return successes


def is_extremal(predecessors):
    n = len(predecessors)
    if n < 3:
        return False
    return predecessors == (0, 0) + (3,) * (n - 2)


def audit_small_orders():
    family = [()]
    counts = [1, 2, 7, 40, 357, 4824]
    for n in range(1, 7):
        family = [successor for p in family for successor in extend_order(p)]
        assert len(family) == counts[n - 1]
        number_failing_kc = 0
        winners = []
        for poset in family:
            ideals = downsets(poset)
            successes = direct_count(poset, ideals)
            assert successes == structural_count(poset, ideals)
            if successes == len(ideals):
                continue
            number_failing_kc += 1
            assert n >= 3
            rate = Fraction(successes, len(ideals))
            optimum = Fraction((1 << (n - 2)) + 1,
                               (1 << (n - 2)) + 3)
            assert rate <= optimum, (poset, rate, optimum)
            if rate == optimum:
                winners.append(poset)
                assert is_extremal(poset), poset
        if n >= 3:
            assert len(winners) == 1
        print(f"n={n} orders={len(family)} failures={number_failing_kc} "
              f"extremizers={len(winners)}")


def audit_strength_distinction():
    # Same algebra cardinality, Boolean-center size, and regular-element size,
    # but different prevalence of weak excluded middle.
    first = (0, 0, 2, 7)
    second = (0, 0, 3, 3)
    assert len(downsets(first)) == len(downsets(second)) == 7
    assert len(components(first)) == len(components(second)) == 1
    assert sum(x == 0 for x in first) == sum(x == 0 for x in second) == 2
    assert direct_count(first, downsets(first)) == 4
    assert direct_count(second, downsets(second)) == 5
    print("SAME_STRONG_DEGREES_DIFFERENT_WEAK_DEGREE_PASS 4/7 5/7")


def audit_extremizers():
    for n in range(3, 17):
        p = (0, 0) + (3,) * (n - 2)
        good = (1 << (n - 2)) + 1
        total = (1 << (n - 2)) + 3
        assert len(downsets(p)) == total
        # Full direct checking up to n=13 is inexpensive; larger n check formula.
        if n <= 13:
            assert direct_count(p, downsets(p)) == good
        assert structural_count(p, downsets(p)) == good
    print("EXTREMAL_FAMILY_PASS n=3..16")


if __name__ == "__main__":
    audit_small_orders()
    audit_strength_distinction()
    audit_extremizers()
    print("WEAK_EXCLUDED_MIDDLE_EXACT_CHECKS_PASS")
