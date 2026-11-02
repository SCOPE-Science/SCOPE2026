#!/usr/bin/env python3
"""Independent restricted-growth/profile certification for Schur partitions of a 3x3 band."""
from itertools import permutations
from collections import Counter

N=9

def enumerate_partitions():
    p=[0]*N
    def visit(i,high):
        if i==N:
            yield tuple(p);return
        for c in range(high+2):
            p[i]=c
            yield from visit(i+1,max(high,c))
    yield from visit(1,0)

def passing(p):
    k=max(p)+1
    row=[[0,0,0] for _ in range(k)]
    col=[[0,0,0] for _ in range(k)]
    for x,v in enumerate(p):
        row[v][x//3]+=1
        col[v][x%3]+=1
    for x in range(9):
        for y in range(x+1,9):
            if p[x]==p[y]:
                if any(row[c][x//3]!=row[c][y//3] or col[c][x%3]!=col[c][y%3] for c in range(k)):
                    return False
    return True

def stabilizer_orbits(p):
    orbit={}
    for a in permutations(range(3)):
        for b in permutations(range(3)):
            perm=[3*a[i//3]+b[i%3] for i in range(9)]
            if all(p[x]==p[perm[x]] for x in range(9)):
                for x in range(9): orbit.setdefault(x,set()).add(perm[x])
    for x in range(9):
        if orbit[x]!={y for y in range(9) if p[y]==p[x]}:return False
    return True

n=ok=non_auto=0; ranks=Counter()
for p in enumerate_partitions():
    n+=1
    if passing(p):
        ok+=1;ranks[max(p)+1]+=1
        if not stabilizer_orbits(p):non_auto+=1
assert (n,ok,non_auto)==(21147,42,0)
assert ranks=={1:1,2:12,3:4,4:9,5:9,6:6,9:1}
print('RGS_partitions=21147')
print('Profile_equation_solutions=42')
print('Nonautomorphic=0')
print('Rank_counts='+str(dict(sorted(ranks.items()))))

# Construct orbit-isomorphism classes without subgroup enumeration.
autos=[tuple(3*a[x//3]+b[x%3] for x in range(9))
       for a in permutations(range(3)) for b in permutations(range(3))]
def canonical(p):
    lookup={};q=[]
    for x in p:
        if x not in lookup:lookup[x]=len(lookup)
        q.append(lookup[x])
    return tuple(q)
iso={}
for p in enumerate_partitions():
    if passing(p):
        rep=min(canonical(tuple(p[g[x]] for x in range(9))) for g in autos)
        iso[rep]=iso.get(rep,0)+1
expected={'000000000':1,'000000111':3,'001001001':3,'001010100':6,
          '000111222':1,'012012012':1,'012120201':2,'001001223':9,
          '001234324':9,'001223445':3,'012012345':3,'012345678':1}
assert {''.join(map(str,k)):v for k,v in iso.items()}==expected
print('Isomorphism_types='+str(len(iso)))
print('VERIFY_OK')
