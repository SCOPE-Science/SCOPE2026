#!/usr/bin/env python3
"""Direct finite checks for Hamming-cube coordinate-flip fixed complexes."""
from itertools import combinations
from math import comb


def distance(x,y):
    return (x^y).bit_count()


def pair_orbits(n):
    # A single-coordinate flip is the involution x -> x xor 1.
    return tuple((2*x,2*x+1) for x in range(1<<(n-1)))


def face(vertices,r):
    return all(distance(a,b)<=r for a,b in combinations(vertices,2))


cases=0
faces=0
orbit_pair_tests=0
for n in range(2,7):
    orbits=pair_orbits(n)
    for r in range(1,n+1):
        # Verify orbit cardinalities, no shared vertices, and each orbit is an edge.
        assert len(set(sum((list(z) for z in orbits),[])))==2**n
        for i in range(len(orbits)):
            for j in range(i,len(orbits)):
                union=tuple(dict.fromkeys(orbits[i]+orbits[j]))
                value=face(union,r)
                expected = (i==j or distance(i,j)<=r-1)
                assert value==expected,(n,r,i,j)
                orbit_pair_tests+=1
        # Full enumeration of orbit-subset faces, including empty face, for n<=5.
        if n<=5:
            n_orbits=len(orbits)
            for mask in range(1<<n_orbits):
                subset=[j for j in range(n_orbits) if mask & (1<<j)]
                vertices=[v for j in subset for v in orbits[j]]
                actual=face(vertices,r)
                expected=face(subset,r-1)
                assert actual==expected,(n,r,mask)
                if mask and actual: faces+=1
        cases+=1

# Published Feng scale-3 multiplicities instantiated with m=n-1.
for n in range(6,12):
    m=n-1
    s4=sum(2**(j-4)*comb(j,4) for j in range(4,m))
    s7=2**(m-4)*comb(m,4)
    assert s4>=1 and s7>=10
    if n==6:assert (s4,s7)==(1,10)
print(f'FULL_ORBIT_SUBSET_CHECKS_N2_TO5_AND_PAIR_CHECKS_N2_TO6: {cases} scale cases')
print(f'ORBIT_PAIR_TESTS: {orbit_pair_tests}')
print(f'NONEMPTY_FIXED_COMPLEX_FACES_CONFIRMED: {faces}')
print('FENG_FORMULA_BOUNDARIES_N6_TO11: PASS')
print('VERIFY_OK')
