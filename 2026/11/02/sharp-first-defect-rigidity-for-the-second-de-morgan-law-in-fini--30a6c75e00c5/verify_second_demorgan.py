#!/usr/bin/env python3
"""Exact finite-poset checks for the second De Morgan pair-failure theorem.

All counts are integer arithmetic. Python 3 standard library only.
A finite poset is stored as bitmasks lower[j] of principal downsets.
"""
from itertools import combinations
from collections import Counter


def naturally_labeled_posets(n):
    edges = list(combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        lower = [1 << j for j in range(n)]
        for e, (i, j) in enumerate(edges):
            if mask >> e & 1:
                lower[j] |= 1 << i
        if all((lower[j] & lower[k]) == lower[k]
               for j in range(n) for k in range(j)
               if lower[j] >> k & 1):
            yield tuple(lower)


def ideals(lower):
    n = len(lower)
    return [x for x in range(1 << n)
            if all((x & lower[j]) == lower[j]
                   for j in range(n) if x >> j & 1)]


def failures_by_direct_negation(lower):
    downsets = ideals(lower)
    neg = {a: sum(1 << p for p, dp in enumerate(lower) if not dp & a)
           for a in downsets}
    # First law and closure of negations are also checked.
    assert all(neg[a] in downsets for a in downsets)
    assert all(neg[a | b] == (neg[a] & neg[b])
               for a in downsets for b in downsets)
    return sum(neg[a & b] != (neg[a] | neg[b])
               for a in downsets for b in downsets)


def failures_by_minimal_traces(lower):
    d = ideals(lower)
    mn = sum(1 << i for i, x in enumerate(lower) if x == (1 << i))
    weights = Counter(a & mn for a in d)
    ancestor_minima = {x & mn for x in lower}
    return sum(wa * wb
               for a, wa in weights.items() for b, wb in weights.items()
               if any((a & s) and (b & s) and not (a & b & s)
                      for s in ancestor_minima))


def is_two_fork_ordinal_sum(lower):
    n = len(lower)
    mins = [i for i, s in enumerate(lower) if s == (1 << i)]
    if len(mins) != 2 or n < 3:
        return False
    a, b = mins
    return all((lower[j] >> a & 1) and (lower[j] >> b & 1)
               for j in range(n) if j not in mins)


def a_k_plus_q(k, qlower):
    # Q labels begin at k. Every Q-point lies above all k minimal elements.
    all_min = (1 << k) - 1
    return tuple([1 << a for a in range(k)] +
                 [all_min | (s << k) for s in qlower])


def chain_lower(r):
    return tuple((1 << (i + 1)) - 1 for i in range(r))


def check():
    total = 0
    for n in range(1, 7):
        count = two = violating = 0
        for lower in naturally_labeled_posets(n):
            count += 1
            f = failures_by_direct_negation(lower)
            g = failures_by_minimal_traces(lower)
            assert f == g, (lower, f, g)
            assert (f == 2) == is_two_fork_ordinal_sum(lower), (lower, f)
            ds = ideals(lower)
            neg = {a: sum(1 << p for p, dp in enumerate(lower) if not dp & a)
                   for a in ds}
            unary_defect = sum((neg[a] | neg[neg[a]]) != (1 << n) - 1 for a in ds)
            assert f >= unary_defect, (lower, f, unary_defect)
            assert (f == unary_defect) == (f == 0 or is_two_fork_ordinal_sum(lower))
            assert f == 0 or f >= 2 and f % 2 == 0
            # Exact fixed-cardinality bound for every non-De Morgan algebra.
            if f:
                violating += 1
                h = len(ideals(lower))
                assert h >= 5
                assert f >= 2  # This gives the sharp bound 1 - 2/h**2.
            if f == 2:
                two += 1
        total += count
        expected = [0, 1, 2, 7, 40, 357, 4824][n]
        assert count == expected, (n, count)
        print('POSSETS_OK n=%s count=%s non_DM=%s exactly_two=%s' %
              (n, count, violating, two))
    assert total == 5231
    # All cardinalities from five through twenty-three are attained.
    for size in range(5, 24):
        r = size - 4
        p = a_k_plus_q(2, chain_lower(r))
        assert len(ideals(p)) == size
        assert failures_by_direct_negation(p) == 2
    print('ALL_ALGEBRA_SIZES_5_THROUGH_23_SHARP_PASS')
    # Unary weak excluded middle does not determine the binary defect.
    witnesses = ((1, 3, 4, 13, 19), (1, 2, 6, 15, 17))
    stats = []
    for p in witnesses:
        d = ideals(p)
        neg = {a: sum(1 << v for v, dp in enumerate(p) if not dp & a)
               for a in d}
        wem_good = sum((neg[a] | neg[neg[a]]) == (1 << len(p)) - 1
                       for a in d)
        stats.append((len(d), wem_good, failures_by_direct_negation(p)))
    assert stats == [(11, 7, 6), (11, 7, 8)], stats
    print('SAME_UNARY_DIFFERENT_BINARY_DEFECT_PASS', stats)
    # General k-minimum upper-ordinal-sum count; Q may have arbitrary order.
    families = 0
    for k in range(2, 6):
        for r in range(1, 5):
            for q in naturally_labeled_posets(r):
                p = a_k_plus_q(k, q)
                h = (1 << k) - 1 + len(ideals(q))
                f = 3**k - 2**(k+1) + 1
                assert len(ideals(p)) == h
                assert failures_by_direct_negation(p) == f
                families += 1
    print('ORDINAL_SUM_FORMULA_PASS instances=%s' % families)
    print('ALL_SECOND_DEMORGAN_CHECKS_PASS examined_posets=%s' % total)


if __name__ == '__main__':
    check()
