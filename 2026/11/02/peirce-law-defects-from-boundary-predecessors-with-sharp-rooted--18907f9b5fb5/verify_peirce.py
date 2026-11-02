#!/usr/bin/env python3
"""Direct finite checks of Peirce's law in downset Heyting algebras.

Runs with the Python standard library. The exact mathematical theorem does not
rest on exhaustive evidence beyond the enumerated finite ranges.
"""
from itertools import combinations


def naturally_labeled_posets(n):
    edges = list(combinations(range(n), 2))
    seen = set()
    for mask in range(1 << len(edges)):
        below = [1 << i for i in range(n)]
        for j, (a, b) in enumerate(edges):
            if mask >> j & 1:
                below[b] |= 1 << a
        for b in range(n):
            for a in range(b):
                if below[b] >> a & 1:
                    below[b] |= below[a]
        key = tuple(below)
        if key not in seen:
            seen.add(key)
            yield key


def downsets(below):
    n = len(below)
    return [a for a in range(1 << n)
            if all((not (a >> i & 1)) or below[i] & a == below[i]
                   for i in range(n))]


def implications(below, ideals):
    n = len(below)
    return {(a, b): sum(1 << p for p in range(n)
                         if (below[p] & a & ~b) == 0)
            for a in ideals for b in ideals}


def minimal_excluded_predecessors(below, a):
    s = 0
    for p, d in enumerate(below):
        predecessor = d & ~(1 << p)
        if not (a >> p & 1) and predecessor & ~a == 0:
            s |= predecessor
    return s


def check(below):
    ideals = downsets(below)
    h = len(ideals)
    arrow = implications(below, ideals)
    brute = {(a, b) for a in ideals for b in ideals
             if arrow[arrow[a, b], a] != a}
    exact = {(a, b) for a in ideals for b in ideals
             if minimal_excluded_predecessors(below, a) & ~b}
    assert brute == exact, (below, brute ^ exact)
    formula = 0
    for a in ideals:
        s = minimal_excluded_predecessors(below, a)
        # J(P \ S) counts downsets B containing the downset S.
        j_complement = sum(1 for b in ideals if (b & s) == s)
        formula += h - j_complement
    assert len(brute) == formula
    n = len(below)
    full = (1 << n) - 1
    least = [i for i in range(n) if all(below[j] >> i & 1 for j in range(n))]
    greatest = [i for i in range(n) if below[i] == full]
    if n >= 2 and (least or greatest):
        assert len(brute) >= h - 2, (below, h, len(brute))
        if least:
            r = least[0]
            star = all(below[i] == ((1 << i) | (1 << r))
                       for i in range(n) if i != r)
            assert (len(brute) == h - 2) == star, (below, h, len(brute))
        if greatest:
            t = greatest[0]
            star = all(below[i] == (1 << i) for i in range(n) if i != t)
            assert (len(brute) == h - 2) == star, (below, h, len(brute))
    return h, len(brute), bool(least), bool(greatest)


def star(k, upward):
    # upward=True: singleton least below k pairwise incomparable maxima.
    # upward=False: k minima below a singleton greatest.
    n = k + 1
    if upward:
        return tuple([1] + [(1 << i) | 1 for i in range(1, n)])
    return tuple([1 << i for i in range(k)] + [(1 << n) - 1])


def two_level(r, s):
    return tuple([1 << i for i in range(r)] +
                 [(1 << j) | ((1 << r) - 1) for j in range(r, r + s)])


def main():
    total = 0
    total_ideals = 0
    rooted = 0
    corooted = 0
    for n in range(1, 7):
        count = 0
        for below in naturally_labeled_posets(n):
            h, failures, lo, hi = check(below)
            count += 1
            total_ideals += h
            rooted += lo
            corooted += hi
        total += count
        print('POSSET_SIZE', n, 'CHECKED', count)
    assert total == 5231
    print('ROOTED_AND_COROOTED_CHECK_PASS total_posets=', total,
          'antecedents=', total_ideals, 'rooted=', rooted, 'corooted=', corooted)
    for k in range(1, 10):
        expected = (1 << k) - 1
        for upward in (True, False):
            h, failures, _, _ = check(star(k, upward))
            assert h == (1 << k) + 1 and failures == expected
    print('BOTH_STAR_FAMILIES_PASS k=1..9')
    for r in range(1, 6):
        for s in range(1, 6):
            h, failures, _, _ = check(two_level(r, s))
            assert h == (1 << r) + (1 << s) - 1
            assert failures == ((1 << r) - 1) * ((1 << s) - 1)
    print('COMPLETE_BIPARTITE_LEVEL_FORMULA_PASS r,s=1..5')
    print('ALL_PEIRCE_CHECKS_PASS')


if __name__ == '__main__':
    main()
