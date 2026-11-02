#!/usr/bin/env python3
"""Independent finite checks of a proposed minimal-connected-domination formula.

Execute with Python 3.10 or later. Only the standard library is used.
Graph tests use row/column adjacency and exhaustive vertex subsets, without
using bipartite-tree structure to decide connected domination or minimality.
"""
from collections import Counter
from math import comb, factorial
from itertools import product


def stirling2(a, b):
    if a == b == 0:
        return 1
    if b == 0 or a == 0 or b > a:
        return 0
    return b * stirling2(a - 1, b) + stirling2(a - 1, b - 1)


def formula(m, n):
    assert m >= 2 and n >= 2
    out = Counter()
    q = min(m - 1, n - 1)
    for c in range(1, q + 1):
        out[m + c - 1] += (comb(n, c) * m**(c - 1) *
                             factorial(c) * stirling2(m - 1, c))
        out[n + c - 1] += (comb(m, c) * n**(c - 1) *
                             factorial(c) * stirling2(n - 1, c))
    return dict(out)


def direct(m, n):
    size = m * n
    all_bits = (1 << size) - 1
    adjacency = []
    for i in range(m):
        for j in range(n):
            mask = 0
            for a in range(m):
                for b in range(n):
                    if (a == i or b == j) and (a != i or b != j):
                        mask |= 1 << (a * n + b)
            adjacency.append(mask)

    def connected_dominating(selection):
        if not selection:
            return False
        covered = selection
        remaining = selection
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            covered |= adjacency[bit.bit_length() - 1]
        if covered != all_bits:
            return False
        reached = selection & -selection
        frontier = reached
        while frontier:
            added = 0
            active = frontier
            while active:
                bit = active & -active
                active -= bit
                added |= adjacency[bit.bit_length() - 1] & selection & ~reached
            frontier = added
            reached |= frontier
        return reached == selection

    out = Counter()
    for selection in range(1, 1 << size):
        if not connected_dominating(selection):
            continue
        active = selection
        minimal = True
        while active:
            bit = active & -active
            active -= bit
            if connected_dominating(selection - bit):
                minimal = False
                break
        if minimal:
            out[selection.bit_count()] += 1
    return dict(out)


def surjections(length, colors):
    """Enumerate column-label words directly rather than using Stirling2."""
    if length < colors:
        return 0
    full = set(range(colors))
    return sum(set(word) == full for word in product(range(colors), repeat=length))


def main():
    instances = [(2, n) for n in range(2, 8)]
    instances += [(3, n) for n in range(2, 7)]
    instances += [(4, n) for n in range(2, 6)]
    instances += [(5, 2), (6, 2)]
    examined = 0
    for m, n in instances:
        if m * n > 20:
            continue
        expected = formula(m, n)
        observed = direct(m, n)
        assert expected == observed, (m, n, expected, observed)
        examined += (1 << (m * n)) - 1
        q = min(m - 1, n - 1)
        expected_support = set(range(m, m + q)) | set(range(n, n + q))
        assert set(expected) == expected_support
        assert min(expected) == min(m, n)
        assert max(expected) == m + n - 2
    for a in range(1, 7):
        for b in range(1, a + 1):
            assert surjections(a, b) == factorial(b) * stirling2(a, b)
    assert formula(3, 3) == {3: 6, 4: 36}
    assert formula(3, 4) == {3: 4, 4: 39, 5: 72}
    assert formula(4, 4) == {4: 8, 5: 288, 6: 768}
    print('VERIFY_OK: {} graph orders; {} nonempty subsets; Prüfer surjection checks through length 6'.format(
        len([1 for m, n in instances if m*n <= 20]), examined))
    for m,n in [(3,3),(3,4),(4,4),(3,6),(4,5)]:
        print('M({},{}): {}'.format(m,n, sorted(formula(m,n).items())))


if __name__ == '__main__':
    main()
