#!/usr/bin/env python3
from itertools import combinations
from hashlib import sha256
from math import gcd

N = 19

def canon_pair(A, B):
    A = tuple(sorted(A)); B = tuple(sorted(B))
    return (A, B) if A < B else (B, A)

def is_perfect(A, B, n=N):
    if set(A) & set(B):
        return False
    diffs = []
    for a in A:
        for b in B:
            diffs.append((a-b) % n)
            diffs.append((b-a) % n)
    return sorted(diffs) == list(range(1, n))

def enumerate_unordered(n, m):
    blocks = list(combinations(range(n), m))
    ans = []
    for i, A in enumerate(blocks):
        SA = set(A)
        for B in blocks[i+1:]:
            if SA.isdisjoint(B) and is_perfect(A, B, n):
                ans.append(canon_pair(A, B))
    return sorted(set(ans))

def affine_pair(F, u, t, n=N):
    A, B = F
    return canon_pair(tuple((u*x+t) % n for x in A),
                      tuple((u*x+t) % n for x in B))

def affine_ordered(F, u, t, swap, n=N):
    A, B = F
    A = tuple(sorted((u*x+t) % n for x in A))
    B = tuple(sorted((u*x+t) % n for x in B))
    return (B, A) if swap else (A, B)

S = enumerate_unordered(19, 3)
assert len(S) == 1482
ordered = {(A, B) for A, B in S} | {(B, A) for A, B in S}
assert len(ordered) == 2964

# A completely specified census digest: each line is A|B, blocks and entries lexicographically sorted.
raw = ''.join(','.join(map(str, A)) + '|' + ','.join(map(str, B)) + '\n' for A, B in S).encode('utf-8')
census_sha = sha256(raw).hexdigest()
assert census_sha == '2c153b1f18f4891ec972fcd7110635049b278dfcbac66820726fd774ef7b5e89'

# Unordered affine classes under AGL(1,19).
seen = set(); affine_orbits = []
for F in S:
    if F in seen:
        continue
    orb = {affine_pair(F, u, t) for u in range(1,19) for t in range(19)}
    assert orb <= set(S)
    stab = sum(affine_pair(F,u,t) == F for u in range(1,19) for t in range(19))
    affine_orbits.append((F, len(orb), stab))
    seen |= orb
assert len(seen) == len(S)
assert affine_orbits == [
    (((0,1,2),(3,6,9)),342,1),
    (((0,1,2),(3,6,12)),342,1),
    (((0,1,2),(3,12,15)),342,1),
    (((0,1,4),(3,8,14)),342,1),
    (((0,1,8),(2,11,15)),114,3),
]

# Ordered classes under AGL(1,19) times independent interchange of the two block labels.
seen = set(); ordered_orbits = []
for F in sorted(ordered):
    if F in seen:
        continue
    orb = {affine_ordered(F,u,t,s) for u in range(1,19) for t in range(19) for s in (0,1)}
    assert orb <= ordered
    stab = sum(affine_ordered(F,u,t,s) == F for u in range(1,19) for t in range(19) for s in (0,1))
    ordered_orbits.append((F, len(orb), stab))
    seen |= orb
assert len(seen) == len(ordered)
assert ordered_orbits == [
    (((0,1,2),(3,6,9)),684,1),
    (((0,1,2),(3,6,12)),684,1),
    (((0,1,2),(3,12,15)),684,1),
    (((0,1,4),(3,8,14)),684,1),
    (((0,1,8),(2,11,15)),228,3),
]

special = ((0,1,8),(2,11,15))
special_stab = [(u,t) for u in range(1,19) for t in range(19) if affine_pair(special,u,t) == special]
assert special_stab == [(1,0),(7,1),(11,8)]

# Context for value: the preceding equality cases n=2m^2+1, m=1 and m=2, each have one affine class.
small = []
for m in (1,2):
    n = 2*m*m + 1
    sols = enumerate_unordered(n,m)
    units = [u for u in range(1,n) if gcd(u,n) == 1]
    def af(F,u,t):
        A,B=F
        A=tuple(sorted((u*x+t)%n for x in A)); B=tuple(sorted((u*x+t)%n for x in B))
        return canon_pair(A,B)
    seen0=set(); sizes=[]
    for F in sols:
        if F in seen0: continue
        orb={af(F,u,t) for u in units for t in range(n)}
        assert orb <= set(sols)
        seen0 |= orb; sizes.append(len(orb))
    small.append((m,n,len(sols),tuple(sorted(sizes))))
assert small == [(1,3,3,(3,)),(2,9,54,(54,))]

print('VERIFY_OK unordered=1482 ordered=2964 ordered_group=684 orbits=5 orbit_sizes=684,684,684,684,228 stabilizers=1,1,1,1,3 special_generator=u7_t1 census_sha256=' + census_sha + ' small_m1_m2_orbits=1,1')
