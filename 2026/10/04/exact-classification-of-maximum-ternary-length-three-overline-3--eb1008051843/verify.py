#!/usr/bin/env python3
from itertools import combinations, permutations, product
from math import comb

Q = range(3)
WORDS = list(product(Q, repeat=3))
INDEX = {w:i for i,w in enumerate(WORDS)}

# A descendant signature records, for each coordinate, the set of symbols
# occurring in the selected coalition.  Three 3-bit masks are packed into
# one integer.
SINGLE = [sum((1 << w[j]) << (3*j) for j in range(3)) for w in WORDS]
PAIR = {(a,b): SINGLE[a] | SINGLE[b] for a,b in combinations(range(27),2)}
TRIPLE = {(a,b,c): SINGLE[a] | SINGLE[b] | SINGLE[c]
          for a,b,c in combinations(range(27),3)}

def is_overline3_separable(code):
    seen = set()
    for x in code:
        s = SINGLE[x]
        if s in seen:
            return False
        seen.add(s)
    for a,b in combinations(code,2):
        s = PAIR[(a,b)]
        if s in seen:
            return False
        seen.add(s)
    for a,b,c in combinations(code,3):
        s = TRIPLE[(a,b,c)]
        if s in seen:
            return False
        seen.add(s)
    return True

def transform(code, coord_perm, symbol_perms):
    out = []
    for idx in code:
        w = WORDS[idx]
        nw = tuple(symbol_perms[j][w[coord_perm[j]]] for j in range(3))
        out.append(INDEX[nw])
    return frozenset(out)

def distance_profile(code):
    prof = {1:0,2:0,3:0}
    for a,b in combinations(code,2):
        d = sum(x != y for x,y in zip(WORDS[a],WORDS[b]))
        prof[d] += 1
    return prof

def multiplicity_profile(code):
    ans=[]
    for j in range(3):
        ans.append(tuple(sorted((sum(WORDS[i][j] == a for i in code) for a in Q), reverse=True)))
    return tuple(ans)

maxima=[]
for C in combinations(range(27),6):
    if is_overline3_separable(C):
        maxima.append(frozenset(C))

seven_count=0
for C in combinations(range(27),7):
    if is_overline3_separable(C):
        seven_count += 1

assert len(maxima) == 135
assert seven_count == 0
assert comb(27,6) == 296010
assert comb(27,7) == 888030

coord_perms=list(permutations(range(3)))
symbol_perms=list(permutations(range(3)))
G_order=len(coord_perms)*(len(symbol_perms)**3)
assert G_order == 1296

maxset=set(maxima)
unseen=set(maxima)
orbits=[]
while unseen:
    C=min(unseen, key=lambda x: tuple(sorted(x)))
    orb=set()
    for cp in coord_perms:
        for p0 in symbol_perms:
            for p1 in symbol_perms:
                for p2 in symbol_perms:
                    T=transform(C, cp, (p0,p1,p2))
                    if T in maxset:
                        orb.add(T)
    orbits.append(orb)
    unseen -= orb

orbits.sort(key=lambda o: len(o))
assert [len(o) for o in orbits] == [27,108]
assert sum(map(len,orbits)) == 135

reps=[]
for orb in orbits:
    rep=min(orb, key=lambda x: tuple(sorted(x)))
    reps.append(rep)

expected_a=frozenset(INDEX[tuple(map(int,s))] for s in ["000","001","012","022","102","202"])
expected_b=frozenset(INDEX[tuple(map(int,s))] for s in ["000","011","101","122","212","220"])
assert reps[0] == expected_a
assert reps[1] == expected_b
assert multiplicity_profile(reps[0]) == ((4,1,1),(4,1,1),(4,1,1))
assert multiplicity_profile(reps[1]) == ((2,2,2),(2,2,2),(2,2,2))
assert distance_profile(reps[0]) == {1:3,2:12,3:0}
assert distance_profile(reps[1]) == {1:0,2:9,3:6}
assert G_order//len(orbits[0]) == 48
assert G_order//len(orbits[1]) == 12

print("VERIFY_OK maximum=6 labeled_maxima=135 orbits=2 orbit_sizes=27,108 stabilizers=48,12 checked6=296010 checked7=888030")
