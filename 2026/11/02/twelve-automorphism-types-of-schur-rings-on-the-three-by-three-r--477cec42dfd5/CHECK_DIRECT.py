#!/usr/bin/env python3
"""Complete independent direct class-sum and group-orbit enumeration for 3x3 rectangular band."""
from itertools import permutations
from collections import Counter
from math import factorial

N=9

def canonical(p):
    names={};out=[]
    for x in p:
        if x not in names: names[x]=len(names)
        out.append(names[x])
    return tuple(out)

def partitions(n):
    buf=[0]*n
    def rec(i,m):
        if i==n:
            yield tuple(buf)
        else:
            for b in range(m+2):
                buf[i]=b
                yield from rec(i+1,max(m,b))
    yield from rec(1,0)

def is_schur_direct(p):
    k=max(p)+1
    blocks=[[] for _ in range(k)]
    for i,b in enumerate(p): blocks[b].append(i)
    for A in blocks:
        for B in blocks:
            coeff=[0]*N
            for x in A:
                for y in B:
                    coeff[(x//3)*3+(y%3)]+=1
            if any(len({coeff[z] for z in C})!=1 for C in blocks):return False
    return True

# Enumerate all subgroups of the 36-element direct-product automorphism group.
s=list(permutations(range(3)))
elements=[tuple(a[i//3]*3+b[i%3] for i in range(9)) for a in s for b in s]
index={e:i for i,e in enumerate(elements)}
identity=index[tuple(range(9))]
assert len(elements)==36 and identity>=0
mult=[[index[tuple(elements[i][elements[j][x]] for x in range(N))] for j in range(36)] for i in range(36)]

def expand(H,x):
    todo=list(H|{x}); seen=set(todo)
    while todo:
        a=todo.pop()
        for b in list(seen):
            for c in (mult[a][b],mult[b][a]):
                if c not in seen:
                    seen.add(c);todo.append(c)
    return frozenset(seen)

subgroups={frozenset({identity})}
front=[frozenset({identity})]
while front:
    H=front.pop()
    for x in range(36):
        if x not in H:
            K=expand(H,x)
            if K not in subgroups:
                subgroups.add(K);front.append(K)

def orbits(H):
    o=[None]*9; k=0
    for x in range(9):
        if o[x] is None:
            for h in H: o[elements[h][x]]=k
            k+=1
    return canonical(o)

orbit_partitions={orbits(H) for H in subgroups}
all_parts=set(partitions(N))
schur_parts={p for p in all_parts if is_schur_direct(p)}
assert len(all_parts)==21147
assert len(schur_parts)==42, len(schur_parts)
assert schur_parts == orbit_partitions, (len(orbit_partitions),len(schur_parts-orbit_partitions),len(orbit_partitions-schur_parts))
rank=Counter(max(p)+1 for p in schur_parts)
# Product block partitions count = Bell(3)^2 = 25.
# all single-factor partitions of [3]
three=set(partitions(3))
products={canonical(tuple((a[i],b[j]) for i in range(3) for j in range(3))) for a in three for b in three}
assert len(products)==25 and products.issubset(schur_parts)
assert len(schur_parts-products)==17
print('semigroup=B(3,3) order=9 |Aut|=36')
print('set_partitions=21147')
print('Schur_partitions=42')
print('Aut_subgroups='+str(len(subgroups)))
print('Distinct_aut_orbit_partitions='+str(len(orbit_partitions)))
print('Direct_product_partitions=25')
print('Non_direct_product_partitions=17')
print('Schur_by_number_of_blocks='+str(dict(sorted(rank.items()))))
print('All_Schur_are_aut_orbit_partitions=True')

# Full classification up to the natural automorphism action.
iso={}
for p in schur_parts:
    images={canonical(tuple(p[perm[x]] for x in range(9))) for perm in elements}
    iso.setdefault(min(images),[]).append(p)
representatives=sorted((max(rep)+1,len(orb),''.join(str(v) for v in rep)) for rep,orb in iso.items())
expected=[(1,1,'000000000'), (2,3,'000000111'),(2,3,'001001001'),(2,6,'001010100'),
          (3,1,'000111222'),(3,1,'012012012'),(3,2,'012120201'),
          (4,9,'001001223'),(5,9,'001234324'),(6,3,'001223445'),
          (6,3,'012012345'),(9,1,'012345678')]
assert representatives==expected,(representatives,expected)
print('Isomorphism_types='+str(len(iso)))
print('Orbit_representatives='+str(representatives))
print('VERIFY_OK')
