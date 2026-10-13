#!/usr/bin/env python3
"""Exact checks for the Kingman cherry/doubleton-length covariance theorem.

Uses only the Python standard library. The coalescent clock has pair rate one.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial


def theoretical_level(n, k):
    if n < 5:
        raise ValueError("level formula requires n>=5")
    return F(k * (k - 1) * (n - k) * (n - k - 1) * (n + k - 6),
             3 * (n - 1) * (n - 2) * (n - 3) * (n - 4))


def expected_doubletons(n, k):
    return F(k * (k - 1) * (n - k), (n - 1) * (n - 2))


def expectation_from_compositions(n, k):
    """Use weighted factorial moments of a uniform ordered composition."""
    def falling(x, r):
        out = 1
        for j in range(r):
            out *= x - j
        return out

    def joint(a, b):
        # Falling factorial moment E[(B_k)_a (D_k)_b].
        remain = n - a - 2 * b
        slots = k - a - b
        if remain < slots or slots < 0 or (slots == 0 and remain != 0):
            return F(0)
        num = 1 if slots == 0 else comb(remain - 1, slots - 1)
        return F(falling(k, a + b) * num, comb(n - 1, k - 1))

    ed = joint(0, 1)
    ebd = joint(1, 1)
    ed2 = joint(0, 2) + ed
    es2d = joint(2, 1)
    ec = F(n, 3)
    ecd = (n * ed - ebd + ed2 + F(1, k - 1) * es2d) / 3
    return ed, ecd - ec * ed


def exact_state_recursion(n):
    """Markov recursion on counts of singleton, doubleton, and past cherries."""
    states = {(n, 0, 0): F(1)}
    level = {}
    ec = F(0)
    for k in range(n, 1, -1):
        ed = sum((p * d for (s, d, c), p in states.items()), F(0))
        ecd = F(0)
        for (s, d, c), p in states.items():
            # At k=2, two surviving singletons can happen only if n=2.
            future = F(s * (s - 1), 3 * (k - 1)) if k >= 3 else F(s * (s - 1), 2)
            ecd += p * d * (c + future)
        level[k] = (ed, ecd)
        nxt = defaultdict(F)
        for (s, d, c), p in states.items():
            r = k - s - d
            possibilities = [
                ((s - 2, d + 1, c + 1), s * (s - 1)),
                ((s - 1, d - 1, c), 2 * s * d),
                ((s - 1, d, c), 2 * s * r),
                ((s, d - 2, c), d * (d - 1)),
                ((s, d - 1, c), 2 * d * r),
                ((s, d, c), r * (r - 1)),
            ]
            for nxt_state, count in possibilities:
                if count:
                    nxt[nxt_state] += p * F(count, k * (k - 1))
        states = nxt
    ec = sum((p * c for (s, d, c), p in states.items()), F(0))
    e2 = sum((F(2, k * (k - 1)) * level[k][0] for k in level), F(0))
    eprod = sum((F(2, k * (k - 1)) * level[k][1] for k in level), F(0))
    return ec, e2, eprod - ec * e2, level


def independent_history_enumeration(n):
    """Enumerate labeled choices of merged ancestral blocks, without state compression."""
    denom = 1
    for k in range(2, n + 1):
        denom *= comb(k, 2)
    count = 0
    sum_cherries = 0
    sum_exposure = F(0)
    sum_joint = F(0)

    def visit(blocks, cherry_count, expo):
        nonlocal count, sum_cherries, sum_exposure, sum_joint
        k = len(blocks)
        if k == 1:
            count += 1
            sum_cherries += cherry_count
            sum_exposure += expo
            sum_joint += cherry_count * expo
            return
        d = sum(len(block) == 2 for block in blocks)
        exposure = expo + F(2 * d, k * (k - 1))
        for a, b in combinations(range(k), 2):
            merged = blocks[a] | blocks[b]
            more = tuple(blocks[j] for j in range(k) if j != a and j != b) + (merged,)
            is_cherry = len(blocks[a]) == len(blocks[b]) == 1
            visit(more, cherry_count + int(is_cherry), exposure)

    visit(tuple(frozenset((i,)) for i in range(n)), 0, F(0))
    assert count == denom
    ec = F(sum_cherries, count)
    e2 = sum_exposure / count
    covariance = sum_joint / count - ec * e2
    return count, ec, e2, covariance


def main():
    checks = 0
    for n in range(5, 75):
        total = F(0)
        for k in range(2, n + 1):
            ed, cov = expectation_from_compositions(n, k)
            assert ed == expected_doubletons(n, k)
            assert cov == theoretical_level(n, k)
            total += F(2, k * (k - 1)) * cov
            checks += 2
        assert total == F(5, 18)
        checks += 1

    for n in range(3, 16):
        ec, e2, cov, level = exact_state_recursion(n)
        assert ec == F(n, 3)
        assert e2 == 1
        assert cov == (F(0) if n == 3 else F(4, 9) if n == 4 else F(5, 18))
        for k, (ed, ecd) in level.items():
            if n >= 5:
                assert ed == expected_doubletons(n, k)
                assert ecd - ec * ed == theoretical_level(n, k)
                checks += 2
        checks += 3

    enumerated = 0
    for n in range(2, 8):
        count, ec, e2, cov = independent_history_enumeration(n)
        expected_ec = F(1) if n == 2 else F(n, 3)
        expected_e2 = F(0) if n == 2 else F(1)
        expected_cov = F(0) if n <= 3 else F(4, 9) if n == 4 else F(5, 18)
        assert (ec, e2, cov) == (expected_ec, expected_e2, expected_cov)
        checks += 3
        enumerated += count

    print(f"VERIFIED: {checks} exact identities; {enumerated} complete labeled coalescent merger histories (n=2..7)")


if __name__ == "__main__":
    main()
