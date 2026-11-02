"""Exact finite checks for the high-threshold binary value-probe theorem.

No external packages or inputs are needed. Run: python checker.py
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, length - 1):
                yield (first,) + tail


def high_threshold_signature(weights, total):
    # For rational thresholds eta = k/total > 1/2, which resolve every
    # maximum-fibre mass occurring on this grid. Terms t_S are binary.
    n = len(weights)
    admissible = [k for k in range(total + 1) if 2*k > total]
    out = []
    for mask in range(1 << n):
        mass = sum(weights[i] for i in range(n) if mask & (1 << i))
        out.append(tuple(int(max(mass, total - mass) >= k)
                         for k in admissible))
    return tuple(out)


def singletons_signature(weights, total):
    admissible = [k for k in range(total + 1) if 2*k > total]
    return tuple(tuple(int(max(v, total-v) >= k) for k in admissible)
                 for v in weights)


def products_signature(weights):
    return tuple(weights[i]*weights[j]
                 for i, j in combinations(range(len(weights)), 2))


def verify():
    grid_instances = 0
    measures = 0
    for n in range(1, 6):
        for d in range(1, 8):
            bins = defaultdict(set)
            reduced = defaultdict(set)
            pairwise = defaultdict(set)
            for weights in compositions(d, n):
                weights = tuple(weights)
                bins[high_threshold_signature(weights, d)].add(weights)
                reduced[singletons_signature(weights, d)].add(weights)
                pairwise[products_signature(weights)].add(weights)
                measures += 1
            fibers = {frozenset(v) for v in bins.values()}
            assert fibers == {frozenset(v) for v in reduced.values()}
            assert fibers == {frozenset(v) for v in pairwise.values()}
            assert len(fibers) == (comb(d+n-1, n-1) - (n-1)
                                   - comb(n, 2) * ((d-1)//2))
            for f in fibers:
                if len(f) == n and all(sum(int(w > 0) for w in p) == 1 for p in f):
                    continue
                if len(f) > 1:
                    assert len(f) == 2
                    p, q = tuple(f)
                    assert sum(int(w > 0) for w in p) == 2
                    assert sum(int(w > 0) for w in q) == 2
                    assert sorted(p) == sorted(q)
            grid_instances += 1
    # A proper subset of singleton probes does not suffice for n>=3.
    for n in range(3, 10):
        for omitted in range(n):
            j, k = [i for i in range(n) if i != omitted][:2]
            p = [0]*n; q = [0]*n
            p[j], p[omitted], p[k] = 6, 3, 1
            q[j], q[omitted], q[k] = 4, 5, 1
            a = singletons_signature(p, 10)
            b = singletons_signature(q, 10)
            assert all(a[i] == b[i] for i in range(n) if i != omitted)
            assert high_threshold_signature(p, 10) != high_threshold_signature(q, 10)
    # Numerically check the quadratic Walsh recovery for rational masses.
    walsh_instances = 0
    for n in range(2, 6):
        for d in range(1, 6):
            for w in compositions(d, n):
                for i, j in combinations(range(n), 2):
                    accum = 0
                    for mask in range(1 << n):
                        signed = sum((1 if mask & (1 << a) else -1)*w[a]
                                     for a in range(n))
                        chi = (1 if mask & (1 << i) else -1) * (1 if mask & (1 << j) else -1)
                        accum += signed*signed*chi
                    assert accum == (1 << n)*2*w[i]*w[j]
                    walsh_instances += 1
    print('grid_instances', grid_instances, 'grid_measures', measures)
    print('walsh_pair_instances', walsh_instances)
    print('missing_singleton_witnesses', sum(range(3,10)))
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    verify()
