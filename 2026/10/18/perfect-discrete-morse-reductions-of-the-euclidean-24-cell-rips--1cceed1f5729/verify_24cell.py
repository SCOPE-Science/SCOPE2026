#!/usr/bin/env python3
"""Exact reproducible Morse certificate for the Euclidean 24-cell Rips filtration.

Usage: python verify_24cell.py [24cell_certificate.json]
Only the Python standard library is required. All comparisons use integer arithmetic.
"""
import collections
import itertools
import json
import os
import sys


def points():
    out = []
    for i, j in itertools.combinations(range(4), 2):
        for si, sj in itertools.product((-1, 1), repeat=2):
            p = [0] * 4
            p[i], p[j] = si, sj
            out.append(tuple(p))
    return out


def dist2(a, b):
    return sum((x-y)**2 for x, y in zip(a, b))


def simplices(P, threshold_squared):
    # Enumerate all cliques, and not just maximal cliques. This recursion is
    # exhaustive because each increasing vertex sequence occurs exactly once.
    adjacency = []
    for p in P:
        adjacency.append(sum(1 << j for j, q in enumerate(P)
                             if p != q and dist2(p, q) <= threshold_squared))
    all_faces = set()

    def rec(mask, candidates):
        if mask:
            all_faces.add(mask)
        while candidates:
            bit = candidates & -candidates
            j = bit.bit_length()-1
            candidates ^= bit
            rec(mask | bit, candidates & adjacency[j])

    rec(0, (1 << len(P)) - 1)
    for face in all_faces:
        indices = [i for i in range(len(P)) if face & (1 << i)]
        assert all(dist2(P[a], P[b]) <= threshold_squared
                   for a, b in itertools.combinations(indices, 2))
    return all_faces


def check_operations(all_faces, operations, expected_critical):
    active = set(all_faces)
    upper = {f: set() for f in all_faces}
    for face in all_faces:
        tmp = face
        while tmp:
            bit = tmp & -tmp
            tmp ^= bit
            facet = face ^ bit
            if facet:
                upper[facet].add(face)

    critical = []
    pairs = 0
    for step, op in enumerate(operations):
        assert isinstance(op, list) and 1 <= len(op) <= 2, step
        if len(op) == 2:
            low, high = op
            assert low in active and high in active, step
            # An elementary collapse is legal if low is a codimension-one
            # face of a maximal high with no other immediate coface.
            assert (high & low) == low and (high ^ low).bit_count() == 1, step
            assert upper[low] == {high}, step
            assert upper[high] == set(), step
            remove = (low, high)
            pairs += 1
        else:
            high = op[0]
            assert high in active and upper[high] == set(), step
            critical.append(high)
            remove = (high,)
        for face in remove:
            active.remove(face)
            x = face
            while x:
                bit = x & -x
                x ^= bit
                facet = face ^ bit
                if facet in active:
                    upper[facet].remove(face)
    assert not active, len(active)
    observed = collections.Counter(z.bit_count()-1 for z in critical)
    assert dict(observed) == expected_critical, (observed, expected_critical)
    assert 2 * pairs + len(critical) == len(all_faces)
    return pairs, dict(observed)


def main():
    path = (sys.argv[1] if len(sys.argv) > 1
            else os.path.join(os.path.dirname(__file__), '24cell_certificate.json'))
    with open(path, encoding='utf-8') as f:
        certificate = json.load(f)
    P = points()
    assert len(P) == 24 and len(set(P)) == 24
    assert [list(p) for p in P] == certificate['vertices']
    histogram = collections.Counter(dist2(p,q)
                                    for i,p in enumerate(P) for q in P[i+1:])
    assert dict(histogram) == {2:96, 4:72, 6:96, 8:12}
    expected = {2:({0:24,1:96,2:96}, {0:1,2:23}, 96),
                4:({0:24,1:168,2:480,3:600,4:288,5:24}, {0:1,3:1}, 791)}
    for cutoff in (2, 4):
        entry = certificate['scales'][str(cutoff)]
        actual_faces = simplices(P, cutoff)
        expected_f, expected_critical, expected_pairs = expected[cutoff]
        fvec = dict(collections.Counter(z.bit_count()-1 for z in actual_faces))
        assert fvec == expected_f
        assert {int(k):v for k,v in entry['face_counts'].items()} == expected_f
        assert entry['critical'] == [op[0] for op in entry['operations'] if len(op)==1]
        pairs, crit = check_operations(actual_faces,entry['operations'],expected_critical)
        assert pairs == expected_pairs
        print('squared scale:', cutoff, 'faces:', len(actual_faces),
              'f-vector:', fvec, 'free pairs:', pairs, 'critical:', crit)
    # At squared threshold six, precisely the twelve antipodal pairs are
    # absent. The clique complex is therefore the join of 12 copies of S^0.
    for i, p in enumerate(P):
        assert -sum(x*x for x in p) == sum(x*y for x,y in zip(p,tuple(-x for x in p)))
        assert sum(dist2(p,q)==8 for q in P) == 1
    assert all(dist2(p,q) in (2,4,6,8) for i,p in enumerate(P) for q in P[i+1:])
    print('squared scale 6: 12 antipodal pairs, sphere S^11')
    print('squared scale 8: full simplex')
    print('CERTIFICATE VERIFIED')

if __name__ == '__main__':
    main()
