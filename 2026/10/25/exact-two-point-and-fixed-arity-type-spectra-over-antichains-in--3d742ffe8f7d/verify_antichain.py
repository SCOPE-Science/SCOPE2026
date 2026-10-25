#!/usr/bin/env python3
"""Independent enumeration of finite poset extensions of a named antichain.

Usage: python verify_antichain.py
Only the Python standard library is required.
"""
from collections import defaultdict
from itertools import product


def is_poset(rel, size):
    """Verify irreflexivity and the full transitivity condition directly."""
    for x in range(size):
        if (x, x) in rel:
            return False
    for x in range(size):
        for y in range(size):
            if (x, y) in rel:
                for z in range(size):
                    if (y, z) in rel and (x, z) not in rel:
                        return False
    return True


def labelled_posets(r):
    pairs = [(i, j) for i in range(r) for j in range(i + 1, r)]
    for word in product(range(3), repeat=len(pairs)):
        rel = set()
        for (i, j), t in zip(pairs, word):
            if t == 1:
                rel.add((i, j))
            if t == 2:
                rel.add((j, i))
        if is_poset(rel, r):
            yield frozenset(rel)


def enumerate_extensions(q_rel, r, n):
    """Directly enumerate all stated base-new relations, then check transitivity."""
    total = 0
    for word in product(range(3), repeat=r * n):
        rel = {(n + u, n + v) for (u, v) in q_rel}
        for (a, q), t in zip(product(range(n), range(r)), word):
            if t == 1:
                rel.add((a, n + q))
            if t == 2:
                rel.add((n + q, a))
        if is_poset(rel, n + r):
            total += 1
    return total


def local_patterns(q_rel, r):
    """Derive all admissible one-parameter relation patterns from Q."""
    patterns = []
    for word in product(range(3), repeat=r):
        lo = sum(1 << q for q in range(r) if word[q] == 1)
        hi = sum(1 << q for q in range(r) if word[q] == 2)
        rel = set(q_rel)
        for q, t in enumerate(word):
            if t == 1:
                rel.add((r, q))
            if t == 2:
                rel.add((q, r))
        if is_poset(rel, r + 1):
            patterns.append((lo, hi))
    return patterns


def union_state_count(q_rel, r, n):
    """Distinct-state DP, separate from direct full poset checking."""
    options = local_patterns(q_rel, r)
    states = {(0, 0): 1}
    for _ in range(n):
        nxt = defaultdict(int)
        for (low, high), count in states.items():
            for lo, hi in options:
                a, b = low | lo, high | hi
                if (a & b) == 0:
                    nxt[(a, b)] += count
        states = nxt
    return sum(states.values())


def inclusion_exclusion(q_rel, r, n):
    """Direct finite union over the 2^r global orientation templates."""
    options = local_patterns(q_rel, r)
    allbits = (1 << r) - 1
    templates = []
    for lower in range(1 << r):
        upper = allbits ^ lower
        templates.append(frozenset((lo, hi) for lo, hi in options
                                   if (lo & upper) == 0 and (hi & lower) == 0))
    ans = 0
    for subset in range(1, 1 << len(templates)):
        selected = [templates[i] for i in range(len(templates))
                    if subset & (1 << i)]
        size = len(set.intersection(*map(set, selected)))
        ans += (1 if subset.bit_count() % 2 else -1) * size**n
    return ans


def sample_posets_four():
    all_four = list(labelled_posets(4))
    # Unique representative shapes under labels are not needed here.
    # Diverse fixed labelled representatives exercise different order constraints.
    select = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 8, 4, 2)]
    chosen = [all_four[0], all_four[-1]]
    for ix in [1, 7, 35, 93, 180]:
        chosen.append(all_four[ix])
    return list(dict.fromkeys(chosen))


def test():
    checks = 0
    distribution = []
    for r in range(4):
        posets = list(labelled_posets(r))
        for q in posets:
            for n in range(4):
                direct = enumerate_extensions(q, r, n)
                dp = union_state_count(q, r, n)
                ie = inclusion_exclusion(q, r, n)
                assert direct == dp == ie, (r, n, q, direct, dp, ie)
                checks += 1
        distribution.append((r, len(posets)))
    # Several four-point diagrams, tested independently with two new base points.
    for q in sample_posets_four():
        for n in range(3):
            direct = enumerate_extensions(q, 4, n)
            dp = union_state_count(q, 4, n)
            ie = inclusion_exclusion(q, 4, n)
            assert direct == dp == ie, (4, n, q, direct, dp, ie)
            checks += 1
    # Complete two-variable type formula; directly enumerate each of the three Q.
    posets2 = list(labelled_posets(2))
    values = []
    for n in range(6):
        total = sum(enumerate_extensions(q, 2, n) for q in posets2)
        closed = 4 * 4**n + 6 * 3**n - 8 * 2**n + 1
        assert total == closed, (n, total, closed)
        values.append(total)
        checks += 1
    # A longer check uses the independent state DP, to exclude short-prefix coincidences.
    for n in range(6, 31):
        total = sum(union_state_count(q, 2, n) for q in posets2)
        closed = 4 * 4**n + 6 * 3**n - 8 * 2**n + 1
        assert total == closed
        checks += 1
    print('labelled_new_posets_by_arity', distribution)
    print('two_type_counts_for_antichain_sizes_0_to_5', values)
    print('independent_extension_checks', checks)
    print('general_fixed_arity_inclusion_exclusion: PASS')
    print('direct_poset_enumeration_vs_union_state_dp: PASS')
    print('two_type_closed_form: PASS')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    test()
