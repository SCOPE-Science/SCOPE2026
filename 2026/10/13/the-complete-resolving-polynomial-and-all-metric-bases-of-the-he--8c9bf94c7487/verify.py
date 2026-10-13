#!/usr/bin/env python3
"""Exact finite verification for metric resolving sets of the Fano incidence graph.

Only Python's standard library is required. No external data files are used.
"""
from collections import Counter, deque
from itertools import combinations, permutations, product
from math import comb

P = tuple(range(7))
LINES = tuple(frozenset({i, (i+1) % 7, (i+3) % 7}) for i in P)
assert len(set(LINES)) == 7
assert all(sum({a,b} <= ell for ell in LINES)==1 for a,b in combinations(P,2))
assert all(sum(p in ell for ell in LINES)==3 for p in P)
N=14
adj=[set() for _ in range(N)]
for j, line in enumerate(LINES):
    for p in line:
        adj[p].add(7+j)
        adj[7+j].add(p)
assert sum(map(len,adj))//2 == 21

def distance_matrix():
    all_dist=[]
    for root in range(N):
        dist=[-1]*N
        dist[root]=0
        que=deque([root])
        while que:
            v=que.popleft()
            for w in adj[v]:
                if dist[w]<0:
                    dist[w]=dist[v]+1
                    que.append(w)
        assert -1 not in dist
        all_dist.append(tuple(dist))
    return all_dist
D=distance_matrix()
assert max(max(d) for d in D) == 3

def resolves_by_distance(mask):
    seen=set()
    vertices=[j for j in range(N) if mask>>j & 1]
    for x in range(N):
        signature=tuple(D[x][j] for j in vertices)
        if signature in seen:
            return False
        seen.add(signature)
    return True

# Geometry-only construction of all maximal equidistance sets.
# Any pair on opposite sides has different distance parity to every vertex.
equal_sets=[]
for x,y in combinations(range(7),2):
    same_points=set(P)-{x,y}
    same_lines={7+j for j,ell in enumerate(LINES) if (x in ell)==(y in ell)}
    E=same_points|same_lines
    assert len(E)==8
    equal_sets.append(sum(1<<e for e in E))
for i,j in combinations(range(7),2):
    same_lines={7+k for k in P if k not in (i,j)}
    same_points={p for p in P if (p in LINES[i])==(p in LINES[j])}
    E=same_lines|same_points
    assert len(E)==8
    equal_sets.append(sum(1<<e for e in E))
assert len(equal_sets)==42 and len(set(equal_sets))==42
for x,y in combinations(range(N),2):
    mask=sum(1<<v for v in range(N) if D[x][v] == D[y][v])
    if (x<7) == (y<7):
        assert mask in equal_sets
    else:
        assert mask == 0

# Form every nonresolving set as a subset of one of 42 equidistance sets.
nonresolving=set()
for E in equal_sets:
    T=E
    while True:
        nonresolving.add(T)
        if T==0:break
        T=(T-1)&E
assert len(nonresolving)==4796
hist=Counter()
optimal=[]
for mask in range(1<<N):
    geometric = mask not in nonresolving
    direct = resolves_by_distance(mask)
    assert geometric == direct, mask
    if direct:
        hist[mask.bit_count()] += 1
        if mask.bit_count()==5:
            optimal.append(mask)
assert sorted(hist.items()) == [(5,168),(6,1890),(7,3096),(8,2961),
    (9,2002),(10,1001),(11,364),(12,91),(13,14),(14,1)]
assert sum(hist.values()) == 11588
assert sum(v for k,v in hist.items()) == len(range(1<<N))-4796
assert all(hist.get(k,0)==0 for k in range(5))
assert hist[9] == comb(14,9)
assert sum(m.bit_count() == 8 for m in nonresolving)==42

# Finite-geometric description of minimum sets with three points and two lines.
three_points_two_lines=set()
for r,s in combinations(P,2):
    I=LINES[r] & LINES[s]
    assert len(I)==1
    A=tuple(LINES[r]-I)
    B=tuple(LINES[s]-I)
    C=tuple(set(P) - (LINES[r]|LINES[s]))
    assert len(A)==len(B)==len(C)==2
    local=[]
    for a,b,c in product(A,B,C):
        if frozenset((a,b,c)) not in LINES:
            mask=(1<<a)|(1<<b)|(1<<c)|(1<<(7+r))|(1<<(7+s))
            assert resolves_by_distance(mask)
            local.append(mask)
    assert len(local)==4
    three_points_two_lines.update(local)
assert len(three_points_two_lines)==84
assert all((m & 127).bit_count()==3 for m in three_points_two_lines)

# Explicitly construct the entire incidence-preserving group, including dualities.
line_index={frozenset(ell):i for i,ell in enumerate(LINES)}
collineations=[]
for p in permutations(P):
    image_lines=[frozenset(p[x] for x in ell) for ell in LINES]
    if set(image_lines)==set(LINES):
        collineations.append(tuple(p)+tuple(7+line_index[L] for L in image_lines))
assert len(collineations)==168
polarity=None
for p in permutations(P):
    values=[]
    for ell in LINES:
        common=set.intersection(*(set(LINES[p[x]]) for x in ell))
        if len(common)!=1:
            break
        values.append(next(iter(common)))
    if len(values)==7 and len(set(values))==7:
        polarity=tuple(7+p[x] for x in P)+tuple(values)
        break
assert polarity is not None
perms=collineations+[tuple(polarity[x] for x in g) for g in collineations]
assert len(set(perms))==336
for g in perms:
    assert all({g[u] for u in adj[v]}==adj[g[v]] for v in range(N))

def act(mask,g):
    return sum(1<<g[v] for v in range(N) if mask>>v&1)

three_lines_two_points={act(m,polarity) for m in three_points_two_lines}
assert len(three_lines_two_points)==84
assert all((m & 127).bit_count()==2 for m in three_lines_two_points)
assert set(optimal)==three_points_two_lines|three_lines_two_points
orbit={act(optimal[0],g) for g in perms}
assert len(orbit)==168 and orbit==set(optimal)
assert all(act(m,g) in nonresolving for m in list(nonresolving)[:20] for g in perms)

print('VERIFY_OK Heawood vertices=14 edges=21 42_equidistance_8_sets')
print('VERIFY_OK all_masks=16384 nonresolving=4796 resolving=11588')
print('VERIFY_OK polynomial='+','.join(f'{k}:{hist[k]}' for k in range(5,15)))
print('VERIFY_OK metric_dimension=5 bases=168 split=84+84 full_automorphism_group=336 base_orbits=1')
