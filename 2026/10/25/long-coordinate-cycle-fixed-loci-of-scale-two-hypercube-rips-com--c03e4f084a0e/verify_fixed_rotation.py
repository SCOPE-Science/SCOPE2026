#!/usr/bin/env python3
"""Finite, exhaustive consistency checks for cyclic fixed loci of binary Rips complexes.

This code is supplementary to the all-dimensions proof; no finite test certifies the
universal statement. No external dependencies are needed.
"""
from itertools import combinations


def hdist(x, y):
    return (x ^ y).bit_count()


def rotate(x, k, m):
    # first k low-order bits are cycled; other m bits remain unchanged
    mask = (1 << k) - 1
    b = x & mask
    moved = ((b << 1) & mask) | (b >> (k - 1))
    return (x & ~mask) | moved


def fixed_orbit_complex(k, m):
    n = k + m
    unused = set(range(1 << n))
    allowed = {}
    while unused:
        x = min(unused)
        orb = set()
        y = x
        while y not in orb:
            orb.add(y)
            y = rotate(y, k, m)
        unused.difference_update(orb)
        if all(hdist(a,b) <= 2 for a,b in combinations(orb,2)):
            base_weight = (x & ((1 << k) - 1)).bit_count()
            outside = x >> k
            if base_weight == 0:
                label = ('zero', outside)
            elif base_weight == k:
                label = ('one', outside)
            elif base_weight == 1:
                label = ('tip_zero', outside)
            elif base_weight == k-1:
                label = ('tip_one', outside)
            else:
                raise AssertionError(('unexpected admissible orbit', k, m, orb))
            if label in allowed:
                raise AssertionError(('duplicate admissible orbit type', k,m,label))
            allowed[label] = frozenset(orb)
    expected = {(kind, y) for kind in ('zero','one','tip_zero','tip_one')
                for y in range(1 << m)}
    assert set(allowed) == expected, (k,m, set(allowed)^expected)

    def edge_expected(a,b):
        ka,ya = a
        kb,yb = b
        d = hdist(ya,yb)
        if ka == kb and ka in ('zero','one'):
            return d <= 2
        if {ka,kb} == {'zero','tip_zero'} or {ka,kb} == {'one','tip_one'}:
            return d <= 1
        return False

    tested_pairs = 0
    for a,b in combinations(sorted(allowed),2):
        actual = all(hdist(x,y) <= 2 for x in allowed[a] for y in allowed[b])
        predicted = edge_expected(a,b)
        assert actual == predicted, (k,m,a,b,actual,predicted)
        tested_pairs += 1

    # Check that the proposed simplicial retraction preserves all edges;
    # the complexes are flag, so this suffices for all simplices.
    def retract(label):
        typ,y = label
        if typ == 'tip_zero':
            return ('zero', y)
        if typ == 'tip_one':
            return ('one', y)
        return label
    for a,b in combinations(sorted(allowed),2):
        if edge_expected(a,b):
            ra,rb = retract(a),retract(b)
            assert ra == rb or edge_expected(ra,rb)
            # Id and retraction are contiguous on each simplex.
            for c,d in combinations(set((a,b,ra,rb)),2):
                assert edge_expected(c,d), (k,m,a,b,c,d)
    return len(allowed),tested_pairs


def main():
    total_orbits=0
    total_pairs=0
    trials=0
    for k,mmax in ((4,4),(5,3),(6,3),(7,2),(8,2)):
        for m in range(mmax+1):
            o,p=fixed_orbit_complex(k,m)
            total_orbits+=o
            total_pairs+=p
            trials+=1
            print(f'k={k} m={m} allowed_orbits={o} checked_pairs={p}')
    print(f'CASE_COUNT={trials} ALLOWED_ORBITS_TOTAL={total_orbits} PAIRS_TOTAL={total_pairs}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
