"""Independent finite checks for two locating-total domination counterexamples.

A prism has vertices (layer, index), indices modulo n, cycle edges on
both layers, and one rung per index. Codes label top/bottom 0/1.
"""
from itertools import combinations
from math import ceil


def graph(n):
    v = tuple((layer, j) for layer in range(2) for j in range(n))
    a = {u: set() for u in v}
    for l, i in v:
        u = (l, i)
        a[u].update(((l, (i-1)%n), (l, (i+1)%n), (1-l, i)))
    assert all(len(a[u]) == 3 for u in v)
    assert all(u in a[w] for w in v for u in a[w])
    return v, a


def check(n, top, bottom):
    v, a = graph(n)
    S = frozenset((0,i) for i in top) | frozenset((1,i) for i in bottom)
    assert len(S) == len(top) + len(bottom)
    assert len(S) == ceil(4*n/5), (n, len(S))
    signatures = {}
    for u in v:
        trace = frozenset(a[u] & S)
        assert trace, ('undominated',u)
        if u not in S:
            assert trace not in signatures.values(), ('collision',u,trace)
            signatures[u] = trace
    return len(signatures),S,signatures


def test_all_smaller(n, bound):
    """Check every candidate strictly below the claimed optimum.
    The theorem's lower bound makes this redundant, but it is an
    independently reconstructible finite sanity check.
    """
    v,a = graph(n)
    checked = 0
    for k in range(bound):
        for tup in combinations(v,k):
            checked += 1
            S = frozenset(tup)
            if any(not (a[u] & S) for u in v):
                continue
            traces = [frozenset(a[u] & S) for u in v if u not in S]
            assert len(traces) != len(set(traces)), ('smaller code',n,k,tup)
    return checked


def run():
    cases = ((8, (0,1,2,4,6), (4,6), 7,8),
             (11, (0,1,2,4,9), (4,6,7,9), 9,10))
    counts=[]
    for n,top,bottom,exact,conjecture in cases:
        signatures,S,detail=check(n,top,bottom)
        assert len(S)==exact and exact<conjecture
        assert exact == ceil(4*n/5) == ceil(2*(2*n)/5)
        counts.append((n,signatures,len(S),conjecture))
    brute8=test_all_smaller(8,7)
    # n=11 has 22 vertices; lower bound already rules out sets of size <=8.
    # A separate exhaustive search to size eight can be added but is not
    # necessary for the proved lower bound and the finite witness checks.
    print('VERIFICATION_OK cases='+str(counts)+' n8_smaller_subsets_checked='+str(brute8))


if __name__=='__main__':
    run()
