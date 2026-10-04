#!/usr/bin/env python3
from itertools import permutations

def rotations(t):
    n=len(t)
    return {t[i:]+t[:i] for i in range(n)}

def dihedral_orbit(t):
    t=tuple(t)
    return rotations(t) | rotations(tuple(reversed(t)))

# For three distinct parameters, cyclic shifts and reversal exhaust all permutations.
t3=(1,2,3)
o3=dihedral_orbit(t3)
assert o3 == set(permutations(t3))

# For four and five distinct positions, the dihedral orbit is proper in the full symmetric orbit.
for m in (4,5,6):
    t=tuple(range(m))
    o=dihedral_orbit(t)
    assert len(o)==2*m
    assert len(o)<len(set(permutations(t)))

# Published four-strand nonisotopy witness: this reordering is not one of the universal dihedral symmetries.
k4=(3,5,7,2)
k4p=(3,7,5,2)
assert sorted(k4)==sorted(k4p)
assert k4p not in dihedral_orbit(k4)

# Published five-strand fibered/nonfibered witness: also outside the universal dihedral symmetry.
k5=(3,-7,5,-5,8)
k5p=(3,5,-7,-5,8)
assert sorted(k5)==sorted(k5p)
assert k5p not in dihedral_orbit(k5)

print('VERIFY_OK D3=S3; D4=8<24; D5=10<120; both published reordered witnesses lie outside their dihedral orbits')
