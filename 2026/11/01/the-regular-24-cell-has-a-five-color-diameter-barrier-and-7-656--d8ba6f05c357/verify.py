#!/usr/bin/env python3
"""Exact exhaustive certificate for diameter partitions of D4 roots.
Run with Python 3.9+ using only the standard library.
"""
from functools import lru_cache
from itertools import combinations, product

R = []
for i, j in combinations(range(4), 2):
    for s, t in product((-1, 1), repeat=2):
        r = [0]*4
        r[i], r[j] = s, t
        R.append(tuple(r))
assert len(R) == len(set(R)) == 24
FULL = (1 << 24) - 1

def dot(x, y):
    return sum(a*b for a, b in zip(x, y))

D = [[dot(x,y) for y in R] for x in R]
assert sorted({4-2*D[i][j] for i in range(24) for j in range(i+1,24)}) == [2,4,6,8]

# Every maximal size-six independent class for forbidden inner product <= -1.
# Its roots must have all pairwise inner products >= 0.
six = []
for cls in combinations(range(24), 6):
    if all(D[i][j] >= 0 for i,j in combinations(cls, 2)):
        six.append(frozenset(cls))
assert len(six) == 24
assert len(set(six)) == 24
# Every size-seven class would contain a size-six class, but no six-class extends.
assert all(not any(all(D[i][j] >= 0 for i in cls) for j in set(range(24))-cls)
           for cls in six)

coordinate_facets = []
for i in range(4):
    for s in (-1,1):
        coordinate_facets.append(frozenset(j for j,r in enumerate(R) if r[i] == s))
assert len(coordinate_facets) == 8 and all(len(x)==6 for x in coordinate_facets)
diagonal_facets = []
for signs in product((-1,1),repeat=4):
    diagonal_facets.append(frozenset(j for j,r in enumerate(R) if dot(r, signs) == 2))
assert len(diagonal_facets) == 16 and all(len(x)==6 for x in diagonal_facets)
assert set(six) == set(coordinate_facets + diagonal_facets)

# No four disjoint six-facets: checked independently of the combinatorial argument.
assert not any(not a&b and not a&c and not a&d and not b&c and not b&d and not c&d
               for a,b,c,d in combinations(six,4))
# Five facet covers exist by assigning any four wrong-sign coordinate facets,
# and assigning all remaining points to the diagonal facet.
for sigma in product((-1,1),repeat=4):
    cover = set(j for j,r in enumerate(R) if dot(r,sigma)==2)
    for i in range(4):
        cover.update(j for j,r in enumerate(R) if r[i]==-sigma[i])
    assert len(cover)==24

# An all-pairwise-positive set has <=3 roots; its triples are precisely the
# 96 triangular faces, of two signed-coordinate types (64 stars, 32 cycles).
assert not any(all(D[i][j]>0 for i,j in combinations(cls,2))
               for cls in combinations(range(24),4))
triangles=[]
byvertex=[[] for _ in range(24)]
for inds in combinations(range(24),3):
    if not all(D[i][j]>0 for i,j in combinations(inds,2)):
        continue
    star = any(all(R[k][j]==s for k in inds)
               for j in range(4) for s in (-1,1))
    mask=sum(1<<i for i in inds)
    triangles.append((mask,int(star)))
    for i in inds:
        byvertex[i].append((mask,int(star)))
assert len(triangles) == 96
assert sum(star for _,star in triangles)==64

# A canonical eight-star-triangle cover, one class for each signed coordinate.
classes={(i,s):[] for i in range(4) for s in (-1,1)}
for r in R:
    i,j=[k for k in range(4) if r[k]!=0]
    if r[i]==r[j]:
        classes[(i,r[i])].append(r)
    else:
        classes[(j,r[j])].append(r)
assert sorted(len(c) for c in classes.values()) == [3]*8
assert all(dot(x,y)>0 for c in classes.values() for x,y in combinations(c,2))

# Exact-cover recurrence: choose smallest unused vertex to count each
# unordered eight-class partition exactly once, weighted by star triangles.
@lru_cache(None)
def poly(used):
    if used==FULL:
        return (1,) + (0,)*8
    first=next(i for i in range(24) if not (used >> i)&1)
    out=[0]*9
    for triangle,star in byvertex[first]:
        if used & triangle:
            continue
        child=poly(used|triangle)
        for k,v in enumerate(child):
            if k+star<=8:
                out[k+star]+=v
    return tuple(out)
coeffs=poly(0)
assert coeffs == (8,0,0,0,2848,0,4480,0,320), coeffs
assert sum(coeffs)==7656
assert poly.cache_info().currsize==12367
print('PASS: 24 roots, distance squares 2,4,6,8; exactly 24 six-facets; no 4 disjoint')
print('PASS: five-facet cover for all 16 sign vectors; 8 positive triples cover 24')
print('PASS: 96 triangles (64 stars/32 cycles); 7656 unordered eight-face partitions')
print('partition polynomial: 8 + 2848*z^4 + 4480*z^6 + 320*z^8')
print('exact-cover recursion states:',poly.cache_info().currsize)
