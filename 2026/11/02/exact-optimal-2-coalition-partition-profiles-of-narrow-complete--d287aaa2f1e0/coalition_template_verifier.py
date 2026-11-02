#!/usr/bin/env python3
"""Exact finite-template and labeled-partition checks for optimal 2-coalitions.

Run: python3 coalition_template_verifier.py
Only the Python standard library is used. The theorem's unbounded step is
proved mathematically in RESULT.md; these loops certify its finite base.
"""
from math import factorial
from collections import Counter

EXPECTED = {
    3: {((2, 1),)},
    4: {((2, 0), (2, 1)), ((3, 1),)},
    5: {((1, 2), (2, 1)), ((2, 0), (3, 1)),
        ((2, 1), (3, 0)), ((4, 1),)},
}


def dominates(a, b, s, t):
    """A set with a left-shore and b right-shore vertices 2-dominates."""
    return (a == s or b >= 2) and (b == t or a >= 2)


def is_coalition_partition(blocks, s, t):
    if not blocks or sum(a for a, b in blocks) != s or sum(b for a, b in blocks) != t:
        return False
    for i, (a, b) in enumerate(blocks):
        if a + b == 0:
            return False
        if dominates(a, b, s, t):
            if a + b != 2:
                return False
        elif not any(j != i and not dominates(c, d, s, t)
                     and dominates(a + c, b + d, s, t)
                     for j, (c, d) in enumerate(blocks)):
            return False
    return True


def optimal_templates(s, t):
    """Exhaust every multiset of nonsingleton part-occupancy types of excess s-1."""
    e0 = s - 1
    kinds = sorted((a, b) for a in range(s + 1) for b in range(t + 1)
                   if 2 <= a + b <= e0 + 1)
    found = set()
    examined = 0

    def search(start, excess, aa, bb, large):
        nonlocal examined
        if excess == 0:
            examined += 1
            blocks = large + [(1, 0)] * (s - aa) + [(0, 1)] * (t - bb)
            if is_coalition_partition(blocks, s, t):
                found.add(tuple(large))
            return
        for j in range(start, len(kinds)):
            a, b = kinds[j]
            w = a + b - 1
            if w <= excess and a + aa <= s and b + bb <= t:
                search(j, excess - w, aa + a, bb + b, large + [(a, b)])

    search(0, e0, 0, 0, [])
    return found, examined


def number_of_labeled_partitions(template, s, t):
    count = Counter(template)
    a_total = sum(a for a, b in template)
    b_total = sum(b for a, b in template)
    result = factorial(s) // factorial(s - a_total)
    result *= factorial(t) // factorial(t - b_total)
    denom = 1
    for (a, b), multiplicity in count.items():
        denom *= (factorial(a) * factorial(b)) ** multiplicity
        denom *= factorial(multiplicity)
    assert result % denom == 0
    return result // denom


def closed_count(s, t):
    if s == 3:
        return 3 * t
    if s == 4:
        return 10 * t
    if s == 5:
        return 25 * t + 15 * t * (t - 1) * (t - 2)
    raise ValueError(s)


def labeled_partitions(n):
    codes = [0] * n

    def generate(i, highest):
        if i == n:
            groups = [[] for _ in range(highest + 1)]
            for v, k in enumerate(codes):
                groups[k].append(v)
            yield groups
            return
        for nxt in range(highest + 2):
            codes[i] = nxt
            yield from generate(i + 1, max(highest, nxt))

    yield from generate(1, 0)


def direct_count(s, t):
    wanted = t + 1
    total = 0
    for part in labeled_partitions(s + t):
        if len(part) != wanted:
            continue
        blocks = [(sum(x < s for x in group), sum(x >= s for x in group))
                  for group in part]
        if is_coalition_partition(blocks, s, t):
            total += 1
    return total


def main():
    checked = 0
    examined = 0
    for s in (3, 4, 5):
        e = s - 1
        for t in range(s + 1, 2 * e + 3):
            found, attempted = optimal_templates(s, t)
            examined += attempted
            checked += 1
            assert found == EXPECTED[s], (s, t, found ^ EXPECTED[s])
            weighted = sum(number_of_labeled_partitions(template, s, t)
                           for template in found)
            assert weighted == closed_count(s, t), (s, t, weighted)
        # Optional larger stress-tests; logical stabilization is proved in text.
        for t in (2 * e + 5, 2 * e + 9):
            found, _ = optimal_templates(s, t)
            assert found == EXPECTED[s], (s, t)
            assert sum(number_of_labeled_partitions(p, s, t) for p in found) == closed_count(s, t)
    direct = [(3, 4), (4, 5), (5, 6)]
    for s, t in direct:
        actual = direct_count(s, t)
        assert actual == closed_count(s, t), (s, t, actual)
    print('VERIFY_OK', checked, 'finite template baselines;',
          examined, 'candidate occupancy multisets;',
          len(direct), 'independent labeled partition enumerations')


if __name__ == '__main__':
    main()
