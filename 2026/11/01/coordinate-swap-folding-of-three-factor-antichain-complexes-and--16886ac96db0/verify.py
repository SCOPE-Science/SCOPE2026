#!/usr/bin/env python3
"""Finite, independent checks for the antichain-coordinate fixed-locus theorem.
All theorem-wide claims follow from the mathematical proof, not these tests.
"""
from itertools import combinations
from math import comb


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def poset_orbits(n):
    # First coordinates are binary; third coordinate runs from 0 to n-1.
    return ([((0, 0, i),) for i in range(n)]
            + [((0, 1, i), (1, 0, i)) for i in range(n)]
            + [((1, 1, i),) for i in range(n)])


def comparable(x, y):
    return all(a <= b for a, b in zip(x, y)) or all(a >= b for a, b in zip(x, y))


def antichain(points):
    return all(not comparable(x, y) for x, y in combinations(points, 2))


def predicted_simplex(indices, n):
    # Orbit types A, X, D are, respectively, index blocks 0, 1, 2.
    if len(set(i // n for i in indices)) < len(indices):
        return False
    return all((i % n) > (j % n)
               for i, j in combinations(indices, 2) if i // n < j // n)


def faces(n):
    orbits = poset_orbits(n)
    fs = []
    for r in (1, 2, 3):
        selected = []
        for simplex in combinations(range(3*n), r):
            expected = predicted_simplex(simplex, n)
            # This is a second independent derivation, via the actual product order.
            present = antichain([p for t in simplex for p in orbits[t]])
            if expected != present:
                raise AssertionError(('orbit-comparison', n, simplex, expected, present))
            if present:
                selected.append(simplex)
        fs.append(selected)
    return fs


def rank2_boundary_mod2(previous, following):
    lookup = {f: i for i, f in enumerate(previous)}
    pivot = {}
    rank = 0
    for sigma in following:
        mask = 0
        for omitted in range(len(sigma)):
            face = sigma[:omitted] + sigma[omitted+1:]
            mask ^= 1 << lookup[face]
        while mask:
            b = mask.bit_length() - 1
            if b in pivot:
                mask ^= pivot[b]
            else:
                pivot[b] = mask
                rank += 1
                break
    return rank


def main():
    orbit_cases = 0
    for n in range(1, 17):
        fs = faces(n)
        assert [len(x) for x in fs] == [3*n, 3*binom(n, 2), binom(n, 3)]
        r1 = rank2_boundary_mod2(fs[0], fs[1]); r2 = rank2_boundary_mod2(fs[1], fs[2])
        b0, b1, b2 = len(fs[0])-r1, len(fs[1])-r1-r2, len(fs[2])-r2
        expected = (3, 0, 0) if n <= 2 else (3, 3*n-7, binom(n-3, 3))
        assert (b0, b1, b2) == expected, (n, (b0, b1, b2), expected)
        # Chain-level consequence also checks higher homology is impossible.
        orbit_cases += binom(3*n, 1) + binom(3*n, 2) + binom(3*n, 3)
        print('n=%02d f=%s H(F_2)=%s' % (n, tuple(map(len, fs)), expected))
    print('PASS: %d exhaustive admissible-orbit checks, finite mod-two boundary ranks n=1..16.' % orbit_cases)
    print('Integral all-n result derives separately from the split graph-cycle lattice proof.')


if __name__ == '__main__':
    main()

# Independent finite checks of the arbitrary-poset (not merely chain) reduction.
def check_three_point_posets():
    pairs = tuple((a, b) for a in range(3) for b in range(3) if a != b)
    count = cases = 0
    for mask in range(1 << len(pairs)):
        rel = {(a,a) for a in range(3)} | {edge for bit, edge in enumerate(pairs) if mask & (1<<bit)}
        if any((b,a) in rel for a,b in rel if a != b):
            continue
        if any((a,c) not in rel for a,b in rel for d,c in rel if b==d):
            continue
        count += 1
        orbits = [((0,0,q),) for q in range(3)] + [((0,1,q),(1,0,q)) for q in range(3)] + [((1,1,q),) for q in range(3)]
        def comp(x,y):
            return ((x[0]<=y[0] and x[1]<=y[1] and (x[2],y[2]) in rel)
                    or (y[0]<=x[0] and y[1]<=x[1] and (y[2],x[2]) in rel))
        def comp3(x,y):
            return ((x[0]<=y[0] and (x[1],y[1]) in rel)
                    or (y[0]<=x[0] and (y[1],x[1]) in rel))
        for m in range(1<<9):
            ix=[i for i in range(9) if m&(1<<i)]
            actual=[p for i in ix for p in orbits[i]]
            folded=[(i//3,i%3) for i in ix]
            a=all(not comp(u,v) for u,v in combinations(actual,2))
            b=all(not comp3(u,v) for u,v in combinations(folded,2))
            assert a==b,(rel,ix,a,b)
            cases+=1
    assert count==19,count
    print('PASS: all 19 labeled three-point posets, all 512 orbit subsets each (%d cases).' % cases)

if __name__ == '__main__':
    check_three_point_posets()
