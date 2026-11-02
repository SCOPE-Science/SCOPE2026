"""Standalone finite checks of closed-neighborhood shattering on ancestor-incidence graphs.

Run: python3 verify_binary_ancestor_neighborhoods.py
Standard library only; exhaustive on the stated finite ranges. Infinite statements
require the mathematical proof and are not inferred from these computations.
"""
from itertools import combinations
from functools import lru_cache
from math import comb


def graph(h):
    leaves = 1 << h
    count = 2 * leaves - 1
    neighbors = [1 << v for v in range(count)]
    # Internal heap index q is represented by graph index leaves+q-1.
    for a in range(leaves):
        q = leaves + a
        while q > 1:
            q //= 2
            u = leaves + q - 1
            neighbors[a] |= 1 << u
            neighbors[u] |= 1 << a
    assert all(bool(neighbors[v] >> w & 1) == bool(neighbors[w] >> v & 1)
               for v in range(count) for w in range(count))
    return neighbors


def shatters(neighborhoods, support):
    needed = 1 << len(support)
    traces = set()
    for neighborhood in neighborhoods:
        traces.add(sum((1 << j) for j, x in enumerate(support)
                       if neighborhood >> x & 1))
        if len(traces) == needed:
            return True
    return False


def is_ancestor(q, r):
    while r >= q:
        if r == q:
            return True
        r //= 2
    return False


def expected_support(h, supp):
    size = len(supp)
    leaves = 1 << h
    if not size:
        return True
    if size == 1:
        return h >= 2 or supp[0] < leaves
    if size == 2:
        if h == 1:
            return False
        a, b = sorted(supp)
        if b < leaves:
            return h >= 2
        if a >= leaves:
            q, r = a - leaves + 1, b - leaves + 1
            return is_ancestor(q, r) or is_ancestor(r, q)
        return is_ancestor(b - leaves + 1, leaves + a)
    if size != 3 or h < 3:
        return False
    actual_leaves = [x for x in supp if x < leaves]
    actual_internal = [x for x in supp if x >= leaves]
    if len(actual_leaves) != 2 or len(actual_internal) != 1:
        return False
    a, b = actual_leaves
    q, r = leaves + a, leaves + b
    da, db = h, h
    while q != r:
        q //= 2
        r //= 2
        da -= 1
        db -= 1
    lca = q
    if not (1 <= da <= h - 2):
        return False
    u = actual_internal[0] - leaves + 1
    return is_ancestor(u, lca)


def coefficients(h):
    leaves = 1 << h
    if h == 1:
        return [1, 2]
    return [1, 2 * leaves - 1,
            comb(leaves, 2) + (2*h - 2)*leaves + 2,
            3 * (1 << (2*h - 2)) - (h+1)*leaves]


def ldim(neighborhoods):
    n = len(neighborhoods)
    query_masks = [sum(1 << i for i, c in enumerate(neighborhoods) if c >> v & 1)
                   for v in range(n)]
    @lru_cache(None)
    def rank(state):
        if state.bit_count() < 2:
            return 0
        best = 0
        for query in query_masks:
            yes, no = state & query, state & ~query
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best
    output = rank((1 << n) - 1)
    return output, rank.cache_info().currsize


def main():
    for h in range(1, 6):
        neighborhoods = graph(h)
        n = len(neighborhoods)
        target = coefficients(h)
        actual = [1]
        max_k = 4 if h <= 4 else 3
        for k in range(1, max_k+1):
            count = 0
            for support in combinations(range(n), k):
                observed = shatters(neighborhoods, support)
                predicted = expected_support(h, support)
                if observed != predicted:
                    raise AssertionError((h, k, support, observed, predicted))
                count += observed
            actual.append(count)
        assert actual[:len(target)] == target, (h, actual, target)
        assert all(v == 0 for v in actual[4:]), (h, actual)
        print('EXHAUSTIVE_SUPPORTS_PASS', 'h=', h, 'N=', n, 'counts=', actual, flush=True)
        if h <= 4:
            ld, states = ldim(neighborhoods)
            assert ld == h, (h, ld)
            print('EXACT_ONLINE_RANK_PASS', 'h=', h, 'rank=', ld,
                  'visited_states=', states, flush=True)
    print('ALL_ANCESTOR_INCIDENCE_NEIGHBORHOOD_CHECKS_PASS', flush=True)


if __name__ == '__main__':
    main()
