"""Checks for the rank-two spectrum of independent directed successor paths.
Run with: python3 checker.py (standard library only).
These finite checks are consistency tests, not a proof of weak convergence.
"""
from itertools import permutations, combinations
from collections import Counter
from fractions import Fraction
from math import comb, prod
from random import Random


def edges(order):
    return {(order[i], order[i + 1]) for i in range(len(order) - 1)}


def collision_counts(orderings):
    es = [edges(p) for p in orderings]
    vals = []
    for i, j in combinations(range(len(es)), 2):
        vals.extend((len(es[i] & es[j]), len(es[i] & {(b, a) for a, b in es[j]})))
    return tuple(vals)


def collision_types(orderings):
    n = len(orderings[0]); k = len(orderings)
    out = []
    for i, j in combinations(range(k), 2):
        same = 0; reverse = 0
        for x in range(n):
            for y in range(n):
                if x == y: continue
                s = int((x, y) in edges(orderings[i]))
                if s:
                    same += int((x, y) in edges(orderings[j]))
                    reverse += int((y, x) in edges(orderings[j]))
        out.extend((same, reverse))
    return tuple(out)


def exact_enumeration():
    for n in (3, 4, 5):
        fixed = tuple(range(n))
        orders = list(permutations(range(n)))
        c = Counter()
        for a in orders:
            for b in orders:
                o = (fixed, a, b)
                t = collision_counts(o)
                assert t == collision_types(o)
                c[t] += 1
        total = len(orders) ** 2
        assert sum(c.values()) == total
        for h in range(6):
            mean = Fraction(sum(v * t[h] for t, v in c.items()), total)
            assert mean == Fraction(n - 1, n), (n, h, mean)
        # The exact finite law differs from the limiting independent Poisson law.
        zeros = Fraction(c[(0,) * 6], total)
        print('EXACT_K3', n, 'models', total, 'states', len(c),
              'mean_each', str(Fraction(n - 1, n)), 'zero_vector', str(zeros))


def profiles(orderings):
    n = len(orderings[0]); k = len(orderings)
    es = [edges(o) for o in orderings]
    z = (0,) * k
    sigs = []
    for x in range(n):
        sig = set()
        for y in range(n):
            if x == y: continue
            sig.add(tuple(1 if (x, y) in E else -1 if (y, x) in E else 0 for E in es))
        sigs.append(frozenset(sig))
    return sigs, es, z


def clean_and_expected(orderings):
    n = len(orderings[0]); k = len(orderings)
    sigs, es, z = profiles(orderings)
    endpoints = [o[0] for o in orderings] + [o[-1] for o in orderings]
    if len(set(endpoints)) < 2*k: return None
    # Each shared geometric edge is required in exactly two relations,
    # and distinct shared edges must be vertex-disjoint and interior.
    undirected = {}
    for i, E in enumerate(es):
        for x, y in E:
            undirected.setdefault(frozenset((x, y)), []).append((i, x, y))
    coll = [records for records in undirected.values() if len(records) >= 2]
    if any(len(c) != 2 for c in coll): return None
    touched = [v for c in coll for _, x, y in c[:1] for v in (x, y)]
    if len(set(touched)) != len(touched) or (set(touched) & set(endpoints)):
        return None
    assert n >= 2*k + 2
    expected = []
    collision_v = {}
    cats = set()
    for c in coll:
        (i, x, y), (j, u, v) = sorted(c)
        assert {x, y} == {u, v}
        cat = (i, j, 1 if (x,y)==(u,v) else -1)
        cats.add(cat)
        collision_v[x] = (i, j, +1, +1 if cat[2] == 1 else -1)
        collision_v[y] = (i, j, -1, -1 if cat[2] == 1 else +1)
    for x in range(n):
        b = {z}
        for i in range(k):
            a = [0]*k; a[i] = 1; b.add(tuple(a))
            a = [0]*k; a[i] = -1; b.add(tuple(a))
        for i, o in enumerate(orderings):
            if x == o[0]:
                a=[0]*k; a[i] = -1; b.remove(tuple(a))
            if x == o[-1]:
                a=[0]*k; a[i] = 1; b.remove(tuple(a))
        if x in collision_v:
            i,j,s,t=collision_v[x]
            a=[0]*k; a[i]=s; b.remove(tuple(a))
            a=[0]*k; a[j]=t; b.remove(tuple(a))
            a=[0]*k; a[i]=s; a[j]=t; b.add(tuple(a))
        expected.append(frozenset(b))
    assert sigs == expected
    assert len(set(sigs)) == 1 + 2*k + 2*len(cats)
    return len(cats)


def sample_clean_profiles():
    rng=Random(20261026)
    hits=0; observed=Counter()
    for t in range(2200):
        n=50; k=3
        orderings=[]
        for i in range(k):
            a=list(range(n)); rng.shuffle(a); orderings.append(tuple(a))
        result=clean_and_expected(orderings)
        if result is not None:
            hits+=1; observed[result]+=1
    assert hits >= 10, hits
    print('CLEAN_PROFILE_TESTS', hits, 'collision_types_distribution', sorted(observed.items()))


def exact_spectrum_counts():
    expected = {0:2,2:12,6:1053696}
    for m,val in expected.items():
        count=prod(comb(m, j)+1 for j in range(m+1))
        assert count == val, (m,count,val)
    print('SPECTRUM_COUNTS', expected)


if __name__ == '__main__':
    exact_enumeration()
    sample_clean_profiles()
    exact_spectrum_counts()
    print('ALL_CHECKS_OK')
