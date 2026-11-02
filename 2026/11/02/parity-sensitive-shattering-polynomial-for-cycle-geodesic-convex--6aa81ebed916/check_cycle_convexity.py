#!/usr/bin/env python3
"""Independent finite checks for cycle-geodesic convexity and its trace polynomial."""
import itertools
from collections import Counter
from functools import lru_cache
from math import comb, log2


def arc_concepts(n):
    half = (n - 1) // 2
    masks = {0, (1 << n) - 1}
    for start in range(n):
        for length in range(half + 1):
            masks.add(sum(1 << ((start + j) % n) for j in range(length + 1)))
    return masks


def shortest_path_interval(n, u, v):
    cw = (v - u) % n
    ccw = (u - v) % n
    z = 0
    if cw <= ccw:
        for j in range(cw + 1):
            z |= 1 << ((u + j) % n)
    if ccw <= cw:
        for j in range(ccw + 1):
            z |= 1 << ((u - j) % n)
    return z


def actual_convex_concepts(n):
    intervals = {(u, v): shortest_path_interval(n, u, v)
                 for u in range(n) for v in range(u + 1, n)}
    convex = set()
    for mask in range(1 << n):
        vertices = [u for u in range(n) if mask >> u & 1]
        if all(intervals[u, v] & ~mask == 0
               for u, v in itertools.combinations(vertices, 2)):
            convex.add(mask)
    return convex


def count_shattered(n, concepts, k):
    totals = 0
    for support in itertools.combinations(range(n), k):
        traces = set()
        for mask in concepts:
            trace = sum((bool(mask >> vertex & 1) << j)
                        for j, vertex in enumerate(support))
            traces.add(trace)
        if len(traces) == (1 << k):
            totals += 1
    return totals


def triple_count(n):
    if n % 2:
        return n * (n * n - 1) // 24
    return n * (n - 2) * (n - 4) // 24


def triple_gap_criterion(n, support):
    a, b, c = support
    return max(b-a, c-b, n-c+a) <= (n - 1) // 2


def rank(n, concepts):
    concepts = tuple(sorted(concepts))
    pos = tuple(sum(1 << j for j, concept in enumerate(concepts)
                    if concept >> v & 1) for v in range(n))
    universe = (1 << len(concepts)) - 1

    @lru_cache(None)
    def recurse(version_space):
        if version_space.bit_count() <= 1:
            return 0
        best = 0
        for mask in pos:
            yes = version_space & mask
            no = version_space & (universe ^ mask)
            if yes and no:
                value = 1 + min(recurse(yes), recurse(no))
                if value > best:
                    best = value
        return best

    answer = recurse(universe)
    return answer, recurse.cache_info().currsize


def lower_bound(n):
    length = (n - 1)//2
    left = length // 2
    right = length - left
    return (left+1).bit_length()-1 + (right+1).bit_length()-1


def verify_online_lower_tree(n):
    length = (n-1)//2
    p = length//2
    q = length-p
    a = (p+1).bit_length()-1
    b = (q+1).bit_length()-1
    # A state contains the query path, plus ranges of still possible endpoints.
    states = [([], (0,p), (0,q))]
    for side, rounds in (('left', a), ('right', b)):
        for _ in range(rounds):
            children = []
            for path, ls, rs in states:
                low, high = ls if side == 'left' else rs
                split = low + (high-low+1)//2
                assert low < split <= high
                query = (-split)%n if side == 'left' else split
                for label, restriction in ((0,(low,split-1)),(1,(split,high))):
                    if side == 'left':
                        children.append((path+[(query,label)],restriction,rs))
                    else:
                        children.append((path+[(query,label)],ls,restriction))
            states = children
    witnesses = set()
    allowed = arc_concepts(n)
    for path, ls, rs in states:
        left, right = ls[0], rs[0]
        mask = sum(1<<((-j)%n) for j in range(left+1))
        mask |= sum(1<<(j%n) for j in range(right+1))
        assert mask in allowed, (n,left,right)
        assert all(((mask>>query)&1)==label for query,label in path)
        witnesses.add(mask)
    assert len(states)==2**(a+b)==len(witnesses)
    return len(witnesses)


def run():
    checked = 0
    for n in range(3, 14):
        predicted = arc_concepts(n)
        actual = actual_convex_concepts(n)
        assert actual == predicted, (n, len(actual), len(predicted), actual ^ predicted)
        assert len(actual) == n * (((n - 1)//2) + 1) + 2
        checked += 1
    print('GRAPH_GEODESIC_CONVEXITY_BRUTE_FORCE_PASS n=3..13')

    for n in range(3, 18):
        concepts = arc_concepts(n)
        for k in (1, 2, 3, 4):
            result = count_shattered(n, concepts, k)
            expected = {1:n, 2:comb(n,2), 3:triple_count(n), 4:0}[k]
            assert result == expected, (n, k, result, expected)
        for support in itertools.combinations(range(n),3):
            traces = {tuple((concept >> u)&1 for u in support)
                      for concept in concepts}
            is_shattered = len(traces) == 8
            assert is_shattered == triple_gap_criterion(n,support), (n,support)
        print('TRACE_AND_GAP_CHECK_PASS n=%d triples=%d' % (n,triple_count(n)))
    print('ALL_STATIC_SHATTERING_COUNTS_PASS n=3..17')

    for n in range(3, 16):
        concepts = arc_concepts(n)
        answer, states = rank(n,concepts)
        low=lower_bound(n)
        high=(len(concepts)).bit_length()-1
        assert low <= answer <= high, (n, low, answer, high)
        print('ONLINE_RANK_CHECK_PASS n=%d ldim=%d lower=%d upper=%d states=%d' %
              (n,answer,low,high,states))
    for n in range(3,101):
        verify_online_lower_tree(n)
    print('ONLINE_LOWER_TREE_CERTIFICATES_PASS n=3..100')
    print('ALL_CYCLE_CONVEXITY_CHECKS_PASS')

if __name__=='__main__':
    run()
