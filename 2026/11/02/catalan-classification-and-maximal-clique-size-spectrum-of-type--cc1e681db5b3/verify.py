#!/usr/bin/env python3
"""Independent finite checks for maximal commuting monoid-idempotent families.

Standard-library only. The first computation uses actual 0-Hecke multiplication
on symmetric-group permutations, not the connected-component criterion. The
second constructs labeled binary search trees and their ideal sets recursively.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import comb


def reduced_word(w):
    p = list(range(len(w)))
    word = []
    for pos, wanted in enumerate(w):
        j = p.index(wanted)
        while j > pos:
            word.append(j - 1)
            p[j - 1], p[j] = p[j], p[j - 1]
            j -= 1
    assert tuple(p) == w
    return word


def star(x, y):
    p = list(x)
    for i in reduced_word(y):
        if p[i] < p[i + 1]:
            p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def parabolic(mask, m):
    p = list(range(m + 1))
    i = 0
    while i < m:
        if not (mask >> i) & 1:
            i += 1
            continue
        j = i
        while j < m and (mask >> j) & 1:
            j += 1
        p[i:j + 1] = reversed(p[i:j + 1])
        i = j
    return tuple(p)


def component_criterion(a, b, m):
    mask = a | b
    i = 0
    while i < m:
        if not (mask >> i) & 1:
            i += 1
            continue
        j = i
        while j < m and (mask >> j) & 1:
            j += 1
        component = ((1 << (j - i)) - 1) << i
        if a & component != component and b & component != component:
            return False
        i = j
    return True


def maximal_cliques(adjacency):
    answer = []
    def visit(R, P, X):
        if not P and not X:
            answer.append(frozenset(R))
            return
        pivot = max(P | X, key=lambda u: len(P & adjacency[u])) if (P or X) else None
        for v in list(P - (adjacency[pivot] if pivot is not None else set())):
            visit(R | {v}, P & adjacency[v], X & adjacency[v])
            P.remove(v)
            X.add(v)
    visit(set(), set(adjacency), set())
    return set(answer)


@lru_cache(None)
def trees(lo, hi):
    if lo > hi:
        return (None,)
    return tuple((r, left, right)
                 for r in range(lo, hi + 1)
                 for left in trees(lo, r - 1)
                 for right in trees(r + 1, hi))


def ideal_sets(tree):
    if tree is None:
        return {0}
    root, left, right = tree
    proper = {a | b for a in ideal_sets(left) for b in ideal_sets(right)}
    # Full support is an ideal; it is the unique ideal containing the root.
    full = 1 << root
    for a in proper:
        full |= a
    return proper | {full}


def recursive_sizes(m):
    spectra = [Counter({1: 1})]
    for n in range(1, m + 1):
        cur = Counter()
        for i in range(n):
            for a, ca in spectra[i].items():
                for b, cb in spectra[n - 1 - i].items():
                    cur[1 + a*b] += ca*cb
        spectra.append(cur)
    return spectra


def main():
    expected_sizes = recursive_sizes(10)
    for m in range(1, 8):
        n = 1 << m
        p = {s: parabolic(s, m) for s in range(n)}
        assert len(set(p.values())) == n
        assert all(star(p[s], p[s]) == p[s] for s in p)
        adjacency = {s: set() for s in p}
        for a, b in combinations(range(n), 2):
            actual = star(p[a], p[b]) == star(p[b], p[a])
            assert actual == component_criterion(a, b, m), (m, a, b)
            if actual:
                adjacency[a].add(b)
                adjacency[b].add(a)
        exact = maximal_cliques(adjacency)
        expected = {frozenset(ideal_sets(t)) for t in trees(0, m - 1)}
        assert exact == expected, (m, len(exact), len(expected))
        observed_spectrum = Counter(map(len, exact))
        assert observed_spectrum == expected_sizes[m]
        catalan = comb(2*m, m) // (m + 1)
        assert len(exact) == catalan
        assert min(observed_spectrum) == m + 1
        assert observed_spectrum[m + 1] == 2**(m - 1)
        print('HECKE_BST_OK', m, 'Catalan', catalan,
              'size_spectrum', sorted(observed_spectrum.items()))

    # A separate group-wide idempotent test, without relying on the theorem.
    for m in range(1, 6):
        S = tuple(permutations(range(m + 1)))
        idempotents = {w for w in S if star(w, w) == w}
        assert idempotents == {parabolic(mask, m) for mask in range(1 << m)}
        print('ALL_IDEMPOTENTS_OK', m, len(idempotents), 'among', len(S))

    for m in range(1, 11):
        spectrum = expected_sizes[m]
        assert sum(spectrum.values()) == comb(2*m, m) // (m + 1)
        assert spectrum[m + 1] == 2**(m - 1)
    print('SPECTRA_RECURRENCE_OK 1..10')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
