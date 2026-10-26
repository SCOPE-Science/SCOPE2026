"""Independent finite verification of type counts for an infinite two-equivalence grid.

Finite orbit words are canonical representatives for row/column permutations
fixing the named coordinate classes. Uses only Python's standard library.
"""
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb

@lru_cache(None)
def signed_first(n, k):
    if n == k == 0: return 1
    if n == 0 or k == 0: return 0
    return signed_first(n - 1, k - 1) - (n - 1) * signed_first(n - 1, k)

@lru_cache(None)
def second(n, k):
    if n == k == 0: return 1
    if n == 0 or k == 0: return 0
    return second(n - 1, k - 1) + k * second(n - 1, k)

def bell(n): return sum(second(n, k) for k in range(n + 1))
def one_coordinate(n, r):
    return sum(comb(n, j) * (r ** j) * bell(n-j) for j in range(n+1))
def unrestricted(n, r, c):
    return one_coordinate(n, r) * one_coordinate(n, c)
def forbidden(n, r, c, m):
    return sum(comb(n, j) * (-m)**j * unrestricted(n-j,r,c)
               for j in range(n+1))
def type_count(n, r, c, m):
    return sum(signed_first(n, j)*forbidden(j,r,c,m) for j in range(n+1))

@lru_cache(None)
def canonical_coordinate_words(k, named):
    words=[()]
    for _ in range(k):
        updated=[]
        for word in words:
            next_novel=max((t for t in word if t>=named),default=named-1)+1
            updated.extend(word+(x,) for x in range(next_novel+1))
        words=updated
    return tuple(words)

def direct_orbit_count(k, r, c, occupied):
    count=0
    for rows in canonical_coordinate_words(k,r):
        for cols in canonical_coordinate_words(k,c):
            cells=tuple(zip(rows,cols))
            if len(set(cells))==k and not (set(cells)&occupied):
                count+=1
    return count

def graph_canonical(r,c,edges):
    candidates=[]
    for rp in permutations(range(r)):
        for cp in permutations(range(c)):
            candidates.append(tuple(sorted((rp[i],cp[j]) for i,j in edges)))
    return min(candidates)

witness1={(0,0),(0,1),(0,2),(1,0)}
witness2={(0,0),(0,1),(1,1),(1,2)}
assert graph_canonical(2,3,witness1)!=graph_canonical(2,3,witness2)
for k in range(5):
    formula=type_count(k,2,3,4)
    assert direct_orbit_count(k,2,3,witness1)==formula
    assert direct_orbit_count(k,2,3,witness2)==formula
    print(f'witness k={k}: {formula}')

# Independently exhaust smaller patterns with fixed named-row/column counts.
for m in range(1,5):
    for r in range(1,m+1):
        for c in range(1,m+1):
            if r*c<m: continue
            classes=set()
            for edges in combinations(product(range(r),range(c)),m):
                occupied=set(edges)
                if len({x for x,y in edges})<r or len({y for x,y in edges})<c:
                    continue
                classes.add(graph_canonical(r,c,occupied))
            if m<=3: assert len(classes)<=1,(m,r,c,len(classes))
            if (m,r,c)==(4,2,3): assert len(classes)==2
print('minimal fixed-support collision: m=4, (r,c)=(2,3)')

for r,c,m in [(1,1,1),(2,3,4),(3,2,4),(2,5,6),(4,3,7)]:
    x=type_count(1,r,c,m);y=type_count(2,r,c,m)
    u,v=r+1,c+1
    assert x+m==u*v
    assert y-x*(x-1)-1==u*u+v*v
    assert (u+v)**2==(y-x*(x-1)-1)+2*(x+m)
print('first-two-type reconstruction: PASS')
print('ALL_CHECKS_PASS')
