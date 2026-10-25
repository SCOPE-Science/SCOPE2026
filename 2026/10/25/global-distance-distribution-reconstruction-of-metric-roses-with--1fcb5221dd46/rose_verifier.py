"""Standalone exact-arithmetic checks of the rose-with-leaves inverse formula.
Scientific proof is in RESULT.md; finite checks do not certify an infinite statement.
Run: python3 rose_verifier.py
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from collections import defaultdict

def atom_formula(arms, halfloops):
    k, m = len(arms), len(halfloops)
    result = defaultdict(int)
    coefficient = 4 - 2*k - 4*m
    for a in arms:
        result[a] += coefficient
    for i in range(k):
        for j in range(i+1, k):
            result[arms[i]+arms[j]] += 2
    for a in arms:
        for b in halfloops:
            result[a+b] += 4
    return {p:mass for p,mass in result.items() if mass}

def reconstruct(k, halfloops, atoms):
    m = len(halfloops)
    coefficient = 4 - 2*k - 4*m
    assert coefficient < 0
    found = []
    while len(found) < k:
        residual = defaultdict(int, atoms)
        for a in found:
            residual[a] -= coefficient
        for i in range(len(found)):
            for j in range(i+1, len(found)):
                residual[found[i]+found[j]] -= 2
        for a in found:
            for b in halfloops:
                residual[a+b] -= 4
        residual = {p:v for p,v in residual.items() if v}
        smallest = min(residual)
        mass = residual[smallest]
        assert mass < 0 and mass % coefficient == 0
        count = mass // coefficient
        assert count >= 1
        found.extend([smallest]*count)
    assert len(found) == k
    assert atom_formula(found, halfloops) == atoms
    return found

alphabet = [Q(1,2), Q(1), Q(3,2), Q(2)]
tests = 0
for m in range(4):
    for k in range(6):
        if m == 0 and k < 3:
            continue
        if m > 0 and k == 0:
            continue
        for leaves in combinations_with_replacement(alphabet, k):
            for halfloops in combinations_with_replacement(alphabet, m):
                found = reconstruct(k, halfloops, atom_formula(leaves,halfloops))
                assert found == list(leaves)
                tests += 1
assert tests > 1000
print('PASS exact reconstruction',tests,'positive configurations including collisions')

# Integrated unnormalized pair-distance density is exactly T^2:
# same pendant: integral 2(a-t)_+ dt = a^2;
# same loop: integral (2c)1_[0,c/2] dt = c^2;
# different edges: ordered cross-convolution integrates twice product lengths.
for arms, halfloops in [([Q(1),Q(3)],[Q(1),Q(2)]),
                        ([Q(1)]*3,[Q(1,2)]),
                        ([],[Q(1)]),
                        ([Q(2)],[Q(2),Q(3)]),
                        ([Q(1,2),Q(3,2)],[])]:
    lengths = list(arms) + [2*b for b in halfloops]
    same = sum(x*x for x in lengths)
    distinct = 2*sum(lengths[i]*lengths[j] for i in range(len(lengths)) for j in range(i+1,len(lengths)))
    total = sum(lengths)
    assert same + distinct == total*total
print('PASS exact probability normalization')
