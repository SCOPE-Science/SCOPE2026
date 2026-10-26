#!/usr/bin/env python3
"""Independent exhaustive checks for paired domination of quadrilateral books.

Python 3.9+; standard library only. Run: python verify_paired_book.py
Vertices 0 and 1 are the spine; 2+2*i and 3+2*i form page i.
"""
from collections import Counter
from functools import lru_cache
from math import comb


def graph(r):
    n = 2 * r + 2
    neighbors = [0] * n
    edges = [(0, 1)]
    for i in range(r):
        a, b = 2 + 2*i, 3 + 2*i
        edges.extend(((0, a), (a, b), (b, 1)))
    for v, w in edges:
        neighbors[v] |= 1 << w
        neighbors[w] |= 1 << v
    return neighbors


def direct_paired_sets(neighbors):
    n = len(neighbors)

    @lru_cache(maxsize=None)
    def perfect_matching(mask):
        if not mask:
            return True
        if mask.bit_count() & 1:
            return False
        v = (mask & -mask).bit_length() - 1
        options = mask & neighbors[v]
        while options:
            bit = options & -options
            if perfect_matching(mask ^ (1 << v) ^ bit):
                return True
            options ^= bit
        return False

    out = set()
    for mask in range(1 << n):
        if mask.bit_count() & 1:
            continue
        if not perfect_matching(mask):
            continue
        if not all((mask & (neighbors[v] | (1 << v))) for v in range(n)):
            continue
        out.add(mask)
    return out


def proposed_paired_sets(r):
    n = 2*r + 2
    U, V = 1, 2
    page_pairs = [3 << (2+2*i) for i in range(r)]
    out = set()
    # Both hubs: only full pages, or exactly one singleton of each
    # orientation on distinct pages, with any remaining pages full.
    for subset in range(1 << r):
        full = 0
        for i in range(r):
            if subset & (1 << i):
                full |= page_pairs[i]
        out.add(U | V | full)
    for i in range(r):
        for j in range(r):
            if i == j:
                continue
            remain = [k for k in range(r) if k not in (i, j)]
            for subset in range(1 << len(remain)):
                S = U | V | (1 << (2 + 2*i)) | (1 << (3 + 2*j))
                for k, page in enumerate(remain):
                    if subset & (1 << k):
                        S |= page_pairs[page]
                out.add(S)
    # Exactly one hub: all leaves on that hub's side and all except
    # one leaf on the other side.
    for missing_page in range(r):
        S_u = U
        S_v = V
        for i in range(r):
            S_u |= (1 << (2+2*i))
            S_v |= (1 << (3+2*i))
            if i != missing_page:
                S_u |= (1 << (3+2*i))
                S_v |= (1 << (2+2*i))
        out.update((S_u, S_v))
    # Neither hub.
    out.add(sum(page_pairs))
    return out


def proposed_minimals(r):
    all_sets = proposed_paired_sets(r)
    result = set()
    # Lower family and upper family can be described without
    # inspecting the brute-force results.
    result.add(3)
    total_leaves = sum(3 << (2+2*i) for i in range(r))
    result.add(total_leaves)
    for i in range(r):
        result.add((total_leaves ^ (1 << (3+2*i))) | 1)
        result.add((total_leaves ^ (1 << (2+2*i))) | 2)
    assert result <= all_sets
    return result


def polynomial_predicted(r):
    ans = Counter()
    for t in range(r+1):
        ans[2+2*t] += comb(r,t)
    for t in range(r-1):
        ans[4+2*t] += r*(r-1)*comb(r-2,t)
    ans[2*r] += 2*r+1
    return {k:v for k,v in sorted(ans.items()) if v}


def run():
    checked = 0
    paired_count = 0
    minimal_count = 0
    for r in range(2, 9):
        n = 2*r+2
        checked += 1 << n
        all_sets = direct_paired_sets(graph(r))
        expected = proposed_paired_sets(r)
        assert all_sets == expected, (r, 'paired classification',len(all_sets),len(expected))
        counts = dict(sorted(Counter(s.bit_count() for s in all_sets).items()))
        assert counts == polynomial_predicted(r), (r, 'polynomial', counts)
        minimal = {s for s in all_sets if not any(t != s and (t & s) == t for t in all_sets)}
        assert minimal == proposed_minimals(r), (r,'minimal',len(minimal))
        expected_min_poly={2:1, 2*r:2*r+1}
        assert dict(sorted(Counter(s.bit_count() for s in minimal).items())) == expected_min_poly
        paired_count += len(all_sets)
        minimal_count += len(minimal)
        print('r=%d vertices=%d paired=%d minimal=%d polynomial=%s PASS' %
              (r,n,len(all_sets),len(minimal),counts))
    print('checked_subsets=%d paired_sets=%d minimal_sets=%d' %
          (checked, paired_count,minimal_count))
    print('PASS: original definitions, full polynomial, full membership classification, exact minimal family')


if __name__ == '__main__':
    run()
