#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict


def canonical_pairs(r):
    # Equivalent parametrization: b=a+d, 0<=d<=r, 1<=a<=r+d.
    return [(a,a+d) for d in range(r+1) for a in range(1,r+d+1)]

def volume(r,a,b):
    return Fraction((r+a+b)**(r+1), a*b)

def collision_classes(r):
    d=defaultdict(list)
    for a,b in canonical_pairs(r):
        d[volume(r,a,b)].append((a,b))
    return {v:ps for v,ps in d.items() if len(ps)>1}

def assert_canonical_criterion_by_reidtai(r,a,b):
    # Check chart quotient ages for all nonidentity elements. Coordinates of weight 1 are smooth.
    if a>1:
        for k in range(1,a):
            age = Fraction(r*k + ((b*k) % a), a)
            assert age >= 1, (r,a,b,'a',k,age)
    if b>1:
        for k in range(1,b):
            age = Fraction(r*k + ((a*k) % b), b)
            assert age >= 1, (r,a,b,'b',k,age)

def direct_canonical(r,a,b):
    try:
        assert_canonical_criterion_by_reidtai(r,a,b)
        return True
    except AssertionError:
        return False

def check_parametrization(limit=40):
    for r in range(2,limit+1):
        predicted=set(canonical_pairs(r))
        brute=set()
        # The canonical bound derived from the criterion puts all solutions in b<=3r.
        for a in range(1,2*r+1):
            for b in range(a,3*r+1):
                if direct_canonical(r,a,b):
                    brute.add((a,b))
        assert predicted == brute, (r, predicted ^ brute)

def check_collisions(limit=200):
    expected2={Fraction(64):[(1,1),(2,4)], Fraction(72):[(1,3),(4,6)]}
    got2=collision_classes(2)
    assert got2 == expected2, got2
    for r in range(3,limit+1):
        assert not collision_classes(r), (r, collision_classes(r))

def proof_cutoff_check():
    # Infinite proof uses: canonical => ab <= 6r^2. If distinct sums occur,
    # coprime reduced sum ratio forces 2^(r+1) <= ab, impossible for r>=8.
    assert 2**9 > 6*8**2
    for r in range(8,1000):
        assert 2**(r+1) > 6*r*r

if __name__ == '__main__':
    check_parametrization(40)
    check_collisions(200)
    proof_cutoff_check()
    print('VERIFY_OK')
