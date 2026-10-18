"""Exact finite consistency checks for chromatic villainy of friendship graphs.
Run using Python 3 standard library: python verify.py.
"""
from itertools import combinations, product


def all_sources(k):
    vertices = 2 * k + 1
    target = range(vertices)
    for c in target:
        rest = tuple(i for i in target if i != c)
        for aset in combinations(rest, k):
            w = [1] * vertices
            w[c] = 2
            for i in aset:
                w[i] = 0
            yield tuple(w)


def all_targets(k):
    # The hub is at vertex 0 and the blade edges are (1,2),...,(2k-1,2k).
    for hub_color in range(3):
        other = tuple(x for x in range(3) if x != hub_color)
        for choices in product(range(2), repeat=k):
            y = [hub_color]
            for choice in choices:
                y.extend((other[choice], other[1-choice]))
            yield tuple(y)


def local_agreements(w, k, hub_color):
    keep = int(w[0] == hub_color)
    for i in range(k):
        a, b = w[2 * i + 1], w[2 * i + 2]
        if a == b == hub_color:
            continue
        if a != b and a != hub_color and b != hub_color:
            keep += 2
        else:
            keep += 1
    return keep


def target_distances_explicit(w, targets):
    n = len(w)
    distances = [(sum(a != b for a, b in zip(w, y)), y[0]) for y in targets]
    weak = min(x for x, h in distances)
    ordinary = min(x for x, h in distances if h == 2)
    return ordinary, weak


def target_distances_local(w, k):
    a = tuple(local_agreements(w, k, h) for h in range(3))
    return 2*k+1-a[2], 2*k+1-max(a)


def witness(k):
    # Color 0 appears k times, color 1 k times, color 2 once.
    if k % 2 == 0:
        pairs = [(0, 2)] + [(0, 0)] * ((k-2)//2) + [(1, 1)] * (k//2)
    else:
        pairs = [(1, 2)] + [(0, 0)] * ((k-1)//2) + [(1, 1)] * ((k-1)//2)
    w = (0,) + tuple(v for pair in pairs for v in pair)
    assert len(w) == 2*k+1 and [w.count(i) for i in range(3)] == [k,k,1]
    return w


def main():
    print('Exact global source-and-target enumeration:')
    for k in range(1, 7):
        sources = all_sources(k)
        targets = tuple(all_targets(k))
        counts = 0
        ordinary = weak = -1
        for w in sources:
            explicit = target_distances_explicit(w, targets)
            if k == 1:
                explicit = (explicit[1], explicit[1])
            if k >= 2:
                local = target_distances_local(w, k)
                assert explicit == local, (k,w,explicit,local)
            ordinary = max(ordinary,explicit[0]); weak=max(weak,explicit[1])
            counts += 1
        assert (ordinary,weak) == ((0,0) if k==1 else (k+1, k if k<=3 else k+1)), (k,ordinary,weak)
        print(f'k={k} sources={counts} proper_targets={len(targets)} B={ordinary} Bw={weak} PASS')
    print('Analytic witnesses checked against all proper targets:')
    for k in range(2,19):
        w = witness(k)
        distance = target_distances_local(w, k)
        assert distance == (k+1, k if k<=3 else k+1), (k,distance)
        if k <= 8:
            assert distance == target_distances_explicit(w,tuple(all_targets(k)))
        print(k, distance)
    print('ALL_TESTS_PASSED')

if __name__ == '__main__': main()
