#!/usr/bin/env python3
"""Exact finite checks for online shattering of finite-poset order ideals.

Only the standard Python library is used.  These computations are finite
sanity checks; the unrestricted assertions require the separate proof.
"""
from functools import lru_cache
from itertools import combinations
from math import floor, log2


def all_natural_order_posets(n):
    """All posets whose natural label order is a linear extension."""
    edges = list(combinations(range(n), 2))
    seen = set()
    for a in range(1 << len(edges)):
        upper = [0] * n
        for bit, (i, j) in enumerate(edges):
            if (a >> bit) & 1:
                upper[i] |= 1 << j
        for i in reversed(range(n)):
            neighbors = upper[i]
            for j in range(i + 1, n):
                if (neighbors >> j) & 1:
                    upper[i] |= upper[j]
        sig = tuple(upper)
        if sig not in seen:
            seen.add(sig)
            yield sig


def rank_parameters(upper):
    n = len(upper)
    height = [1] * n
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            if (upper[i] >> j) & 1:
                height[i] = max(height[i], 1 + height[j])
    h = max(height, default=0)
    w = max((s.bit_count() for s in range(1 << n)
             if all(not((s >> i) & 1 and (s >> j) & 1)
                    for i in range(n) for j in range(i + 1, n)
                    if (upper[i] >> j) & 1)), default=0)
    return h, w


def ideals(upper):
    n = len(upper)
    return [s for s in range(1 << n)
            if all(not ((s >> j) & 1) or ((s >> i) & 1)
                   for i in range(n) for j in range(i + 1, n)
                   if (upper[i] >> j) & 1)]


def littlestone(concepts, n):
    masks = [sum((1 << j) for j, s in enumerate(concepts) if (s >> i) & 1)
             for i in range(n)]
    @lru_cache(maxsize=None)
    def rank(state):
        cap = state.bit_count().bit_length() - 1
        if cap == 0:
            return 0
        best = 0
        for q in masks:
            one = state & q
            zero = state ^ one
            if not one or not zero:
                continue
            if min(one.bit_count(), zero.bit_count()) < (1 << best):
                continue
            candidate = 1 + min(rank(one), rank(zero))
            best = max(best, candidate)
            if best == cap:
                break
        return best
    return rank((1 << len(concepts)) - 1)


def separate_chains(upper, h, w):
    n = len(upper)
    if n != h*w:
        return False
    vertices = set(range(n))
    groups = []
    while vertices:
        i = min(vertices)
        component = {i}
        changed = True
        while changed:
            old = set(component)
            component |= {j for j in vertices
                          if any(((upper[min(a,j)] >> max(a,j)) & 1)
                                 for a in component if a != j)}
            changed = component != old
        groups.append(component)
        vertices -= component
    return len(groups) == w and all(len(group) == h and all(
        ((upper[min(a,b)] >> max(a,b)) & 1)
        for a, b in combinations(sorted(group), 2)) for group in groups)


def direct_union_chains(h, w):
    n = h*w
    upper = [0]*n
    for b in range(w):
        for i in range(h):
            for j in range(i+1, h):
                upper[b*h+i] |= 1 << (b*h+j)
    return tuple(upper)


def main():
    total = 0
    by_order = {}
    for n in range(1, 7):
        count = 0
        for p in all_natural_order_posets(n):
            h, w = rank_parameters(p)
            c = ideals(p)
            ld = littlestone(c, n)
            assert ld >= w  # every maximum antichain is VC-shattered
            assert ld <= w * ((h+1).bit_length()-1)
            if h <= 2:
                assert ld == w
            if h == 3 and ld == 2*w:
                assert separate_chains(p, h, w)
            if h == 3 and separate_chains(p,h,w):
                assert ld == 2*w
            count += 1
        by_order[n] = count
        total += count
        print('EXHAUSTIVE_NATURAL_LABEL_POSETS_PASS', n, count, flush=True)
    for h, w in [(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(7,1),(7,2)]:
        p = direct_union_chains(h,w)
        c = ideals(p)
        d = littlestone(c, h*w)
        assert len(c) == (h+1)**w
        assert d == w*((h+1).bit_length()-1)
        print('EXTREMAL_CHAIN_PRODUCT_PASS',h,w,'ideals',len(c),'depth',d, flush=True)
    print('HEIGHT_WIDTH_SHATTERING_ALL_CHECKS_PASS',total,flush=True)

if __name__ == '__main__':
    main()
