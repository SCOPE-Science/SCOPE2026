#!/usr/bin/env python3
"""Exact three-round EF fingerprints of powers of finite cycles.

No external packages. All cyclic distances and all possible 3rd moves are
enumerated for each ordered pair up to the cyclic automorphism.
"""
import sys

def adjacent(n, r, a, b):
    delta = (a-b) % n
    return a != b and min(delta,n-delta) <= r

def spectrum(n, r, d):
    return tuple(sorted(set((int(adjacent(n,r,0,z)), int(adjacent(n,r,d,z)))
                     for z in range(n) if z not in (0,d))))

def fingerprint(n, r):
    assert r>=1 and n>=2*r+2
    # Under rotations, every chosen first vertex is equivalent.
    return frozenset((int(adjacent(n,r,0,d)), spectrum(n,r,d))
                     for d in range(1,n))

def theorem_fingerprint(r):
    # This should equal the actual fingerprint whenever n>=4*r+3.
    both = ((0,0),(0,1),(1,0),(1,1))
    no_both = ((0,0),(0,1),(1,0))
    return frozenset({(1,both if r>=2 else no_both),(0,both),(0,no_both)})

def main():
    for r in range(1,16):
        n0 = 4*r+3
        actual = fingerprint(n0,r)
        assert actual == theorem_fingerprint(r), (r,actual)
        for n in range(n0,n0+50):
            assert fingerprint(n,r)==actual,(r,n)
        previous = fingerprint(n0-1,r)
        assert previous != actual,(r,previous)
        # The universal domination sentence is witnessed at n=4r+2,
        # and false for all tested graphs beyond.
        def dominates(n):
            return any(all(z in (x,y) or adjacent(n,r,x,z) or adjacent(n,r,y,z)
                           for z in range(n)) for x in range(n) for y in range(x+1,n))
        assert dominates(n0-1)
        for n in range(n0,n0+6): assert not dominates(n)
        print(f'r={r:2d} boundary_n={n0-1:3d} stable_n={n0:3d} fingerprint_types={len(actual)} PASS')
    print('ALL_CHECKS_PASS')

if __name__=='__main__': main()
