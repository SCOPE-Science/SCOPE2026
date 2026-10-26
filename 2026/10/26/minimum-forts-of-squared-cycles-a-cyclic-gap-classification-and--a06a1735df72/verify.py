"""Standalone exact-integer checks for the minimum forts of squared cycles.
Run: python3 verify.py. Uses only the Python standard library.
"""
from itertools import combinations
from math import comb


def neighbors(n):
    return [sum(1 << ((v + t) % n) for t in (-2, -1, 1, 2)) for v in range(n)]


def is_fort(mask, nb):
    if mask == 0:
        return False
    return all((nb[v] & mask).bit_count() != 1
               for v in range(len(nb)) if not (mask >> v & 1))


def gap_pattern(mask, n):
    positions = [i for i in range(n) if mask >> i & 1]
    if not positions:
        return None
    return [(positions[(j+1) % len(positions)]-positions[j]) % n
            for j in range(len(positions))]


def gap_test(mask,n):
    if mask == 0:
        return False
    gs = gap_pattern(mask,n)
    if len(gs) == 1:
        return False
    return all(1 <= g <= 4 and (g != 4 or (gs[(j-1)%len(gs)] == 1
                           and gs[(j+1)%len(gs)] == 1))
               for j,g in enumerate(gs))


def predicted(n):
    if n%3 == 0:
        return 3
    if n%3 == 2:
        return n
    return n*(n+5)//6 + (5 if n==10 else 0)


full_subsets_checked = 0
for n in range(6,15):
    nb = neighbors(n)
    for mask in range(1,1<<n):
        assert is_fort(mask,nb) == gap_test(mask,n), (n,mask)
        full_subsets_checked += 1
print('gap_criterion_exhaustive_n6_to14', full_subsets_checked, 'PASS')

size_restricted_checked=0
for n in range(6,25):
    nb=neighbors(n)
    k=(n+2)//3
    count=0
    for sz in range(1,k+1):
        for inds in combinations(range(n),sz):
            mask=sum(1<<u for u in inds)
            ok=is_fort(mask,nb)
            if sz<k:
                assert not ok, ('lower size fort',n,inds)
            elif ok:
                count+=1
            size_restricted_checked += 1
    assert count == predicted(n),(n,count,predicted(n))
    print('n=',n,'minimum_size=',k,'minimum_forts=',count,'PASS')
print('minimum_enumeration_subsets', size_restricted_checked,'PASS')

# Dihedral label-free pattern census at n=10: five equally spaced adjacent pairs.
n=10; nb=neighbors(n)
patterns=[]
for inds in combinations(range(n),4):
    mask=sum(1<<u for u in inds)
    if is_fort(mask,nb) and 4 in gap_pattern(mask,n):
        patterns.append(inds)
assert len(patterns)==5
assert all(sorted(gap_pattern(sum(1<<i for i in p),n))==[1,1,4,4]
           for p in patterns)
print('exceptional_n10_patterns', len(patterns),'PASS')
print('ALL_CHECKS_PASS')
