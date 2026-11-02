#!/usr/bin/env python3
"""Finite independent checks for incidence learning of matroid bases.

Checks small matroids from the basis-exchange axiom, and complete graphic
matroids K_3, K_4, K_5. Only the Python standard library is required.
"""
from itertools import combinations
from functools import lru_cache
from collections import Counter


def is_matroid_bases(bases):
    if not bases:
        return False
    size = len(next(iter(bases)))
    if any(len(b) != size for b in bases):
        return False
    for b in bases:
        for c in bases:
            for e in b - c:
                if not any((b - {e}) | {f} in bases for f in c - b):
                    return False
    return True


def invariants(n, base_sets):
    """Four logically distinct constructions: VC, adaptive rank, primal-dual
    common independence, and the matroid-intersection minimum rank cut."""
    bases = [sum(1 << x for x in b) for b in base_sets]
    N = len(bases)
    all_elements = (1 << n) - 1
    dual = [all_elements ^ b for b in bases]
    projection_masks = [sum(1 << j for j, b in enumerate(bases) if (b >> i) & 1)
                        for i in range(n)]

    # Direct VC definition: for each S, all projections on S appear.
    vc = 0
    for s in range(1 << n):
        projections = {b & s for b in bases}
        if len(projections) == 1 << s.bit_count():
            vc = max(vc, s.bit_count())

    # Direct complete binary decision-tree recurrence on remaining bases.
    @lru_cache(None)
    def ldim(version_space):
        if version_space.bit_count() <= 1:
            return 0
        upper = version_space.bit_count().bit_length() - 1
        best = 0
        for mask in projection_masks:
            yes = version_space & mask
            no = version_space & ~mask
            if yes and no:
                best = max(best, 1 + min(ldim(yes), ldim(no)))
            if best == upper:
                break
        return best
    online = ldim((1 << N) - 1)

    # Direct common-independent-set test; bases of dual are complements.
    common = 0
    for s in range(1 << n):
        primal_independent = any(s & ~b == 0 for b in bases)
        dual_independent = any(s & ~b == 0 for b in dual)
        if primal_independent and dual_independent:
            common = max(common, s.bit_count())

    # Independent minimax cut test using the TWO rank functions.
    ranks = [max((b & s).bit_count() for b in bases) for s in range(1 << n)]
    dual_ranks = [max((b & s).bit_count() for b in dual) for s in range(1 << n)]
    cut_value = min(ranks[a] + dual_ranks[all_elements ^ a] for a in range(1 << n))
    assert vc == online == common == cut_value, (n, bases, vc, online, common, cut_value)
    return vc, online, common, cut_value


def all_matroids_small(max_n=5):
    counts = Counter()
    for n in range(max_n + 1):
        for rank in range(n + 1):
            candidates = [frozenset(s) for s in combinations(range(n), rank)]
            for nonempty in range(1, 1 << len(candidates)):
                bases = {candidates[j] for j in range(len(candidates)) if nonempty >> j & 1}
                if is_matroid_bases(bases):
                    invariants(n, bases)
                    counts[n] += 1
        print('EXHAUSTIVE_MATROID_BASE_FAMILIES_PASS n=%d count=%d' % (n, counts[n]))
    return counts


def complete_graph_trees(n):
    edges = list(combinations(range(n), 2))
    bases = []
    for pick in combinations(range(len(edges)), n - 1):
        parents = list(range(n))
        def find(x):
            while x != parents[x]:
                x = parents[x]
            return x
        good = True
        for eidx in pick:
            u, v = edges[eidx]
            a, b = find(u), find(v)
            if a == b:
                good = False
                break
            parents[a] = b
        if good and len({find(i) for i in range(n)}) == 1:
            bases.append(frozenset(pick))
    return edges, bases


def checks_complete_graphs():
    for n, expected_bases, expected_dimension in ((3, 3, 1), (4, 16, 3), (5, 125, 4)):
        edges, bases = complete_graph_trees(n)
        assert len(bases) == expected_bases
        result = invariants(len(edges), bases)
        assert result == (expected_dimension,) * 4
        print('GRAPHIC_MATROID_COMPLETE_GRAPH_PASS n=%d edges=%d bases=%d dimension=%d'
              % (n, len(edges), len(bases), result[0]))


if __name__ == '__main__':
    counts = all_matroids_small()
    assert counts[5] == 406, counts[5]
    checks_complete_graphs()
    print('ALL_MATROID_BASE_LEARNING_CHECKS_PASS total_matroids=%d'
          % sum(counts.values()))
