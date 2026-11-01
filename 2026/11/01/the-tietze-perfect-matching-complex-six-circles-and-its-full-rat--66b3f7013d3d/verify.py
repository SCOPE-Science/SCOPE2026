#!/usr/bin/env python3
"""Reproducible exact checks for the perfect-matching complex of the Tietze graph.
All algorithms use only the Python standard library and integer arithmetic.
Run: python3 verify.py
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations

# Petersen graph: vertices are 2-subsets of {0,...,4}, with disjointness edges.
# Inflate vertex (0,1) into a triangle and attach its three former neighbors.
BASE = list(combinations(range(5), 2))
V = [a for a in BASE if a != (0, 1)] + [('triangle', j) for j in range(3)]
vi = {a: i for i, a in enumerate(V)}
pe = [(a, b) for a, b in combinations(BASE, 2) if set(a).isdisjoint(b)]
nei = sorted(b if a == (0,1) else a for a, b in pe if (0,1) in (a,b))
edges = [(vi[a], vi[b]) for a,b in pe if a != (0,1) and b != (0,1)]
edges += [(vi[('triangle', j)], vi[nei[j]]) for j in range(3)]
edges += [(vi[('triangle', j)], vi[('triangle', (j + 1) % 3)]) for j in range(3)]
edges = sorted(tuple(sorted(e)) for e in edges)
assert len(V) == 12 and len(edges) == 18 and len(set(edges)) == 18
adj = [[0] * 12 for _ in V]
inc = [[] for _ in V]
for i, (a,b) in enumerate(edges):
    adj[a][b] = adj[b][a] = 1
    inc[a].append((b,i)); inc[b].append((a,i))
assert all(sum(x) == 3 for x in adj)

@lru_cache(None)
def dp_pm(free):
    if not free: return (0,)
    v = (free & -free).bit_length() - 1
    return tuple((1 << e) | rem for w,e in inc[v]
                 if free & (1 << w)
                 for rem in dp_pm(free ^ (1 << v) ^ (1 << w)))

pms = sorted(set(dp_pm((1 << 12) - 1)))
# Independent enumeration using all 2^18 edge subsets, incident masks and popcount.
vertex_masks = [sum(1 << e for _,e in inc[v]) for v in range(12)]
pms_brute = [s for s in range(1 << 18) if s.bit_count() == 6
             and all((s & mask).bit_count() == 1 for mask in vertex_masks)]
assert pms == pms_brute and len(pms) == 8

# Whole simplicial face set, independently reconstructed as union of powersets.
faces = {0}
for p in pms:
    sub = p
    while sub:
        faces.add(sub)
        sub = (sub - 1) & p
assert len(faces) == 444
assert Counter(s.bit_count() - 1 for s in faces) == {-1:1,0:18,1:96,2:153,3:120,4:48,5:8}

# Nerve of the 8 facet simplices. Each graph-edge corresponds to the subset
# of perfect matchings containing that edge. The maximal such subsets give
# precisely the maximal faces of the nerve.
S = [frozenset(j for j,p in enumerate(pms) if p & (1 << e)) for e in range(18)]
nerve_max = sorted({s for s in S if s and not any(s < t for t in S)},
                   key=lambda s: (-len(s), tuple(sorted(s))))
expected_max = [
    {0,1,2,3}, {0,1,4,5}, {0,1,6,7},
    {0,3,4},{0,3,7},{0,4,7},{1,2,5},{1,2,6},{1,5,6},
    {2,4},{2,7},{3,5},{3,6},{4,6},{5,7}
]
assert {frozenset(s) for s in expected_max} == set(nerve_max)
nerve = {frozenset()}
for s in nerve_max:
    for n in range(1,len(s)+1):
        nerve.update(frozenset(x) for x in combinations(sorted(s),n))
assert Counter(len(s)-1 for s in nerve) == {-1:1,0:8,1:28,2:18,3:3}
full_nerve = nerve.copy()

# Explicit free face collapse list. Every pair is (free face, unique coface).
collapse = [
  ((1,2,3),(0,1,2,3)), ((1,4,5),(0,1,4,5)), ((1,6,7),(0,1,6,7)),
  ((1,3),(0,1,3)), ((1,4),(0,1,4)), ((1,7),(0,1,7)),
  ((2,3),(0,2,3)), ((0,2),(0,1,2)), ((3,4),(0,3,4)),
  ((3,7),(0,3,7)), ((4,5),(0,4,5)), ((0,5),(0,1,5)),
  ((0,1),(0,1,6)), ((4,7),(0,4,7)), ((6,7),(0,6,7)),
  ((2,5),(1,2,5)), ((2,6),(1,2,6)), ((5,6),(1,5,6))
]
for free, coface in collapse:
    a, b = frozenset(free), frozenset(coface)
    assert a in nerve and b in nerve and a < b and len(b) == len(a) + 1
    assert {f for f in nerve if a < f} == {b}, (free,coface)
    nerve.remove(a); nerve.remove(b)
assert Counter(len(s)-1 for s in nerve) == {-1:1,0:8,1:13}
remaining_edges = [tuple(sorted(f)) for f in nerve if len(f)==2]
assert len(remaining_edges)==13
# Connectivity on 8 vertices
reach={0}
while True:
    nxt=reach|{v for a,b in remaining_edges for u,v in [(a,b),(b,a)] if u in reach}
    if nxt==reach: break
    reach=nxt
assert reach == set(range(8))
assert 13-8+1 == 6

# Independent acyclic matching on 443 nonempty original simplices.
remaining = faces-{0}
matched=[]
for e in range(18):
    bit=1<<e
    for f in list(remaining):
        if f in remaining and f&bit==0 and f|bit in remaining:
            remaining.remove(f);remaining.remove(f|bit)
            matched.append((f,f|bit))
assert len(matched)==218 and Counter(f.bit_count()-1 for f in remaining)=={0:1,1:6}
matched_pairs=set(matched)
# Orient the whole Hasse diagram; acyclicity is equivalent to a topological sort.
from collections import deque
neighbors={s:[] for s in faces-{0}}
indegree={s:0 for s in faces-{0}}
for top in faces-{0}:
    for e in range(18):
        bit=1<<e
        if top & bit:
            low=top^bit
            if not low:continue
            if (low,top) in matched_pairs: u,v=low,top
            else: u,v=top,low
            neighbors[u].append(v);indegree[v]+=1
queue=deque(s for s in indegree if indegree[s]==0)
count=0
while queue:
    u=queue.popleft(); count+=1
    for v in neighbors[u]:
        indegree[v]-=1
        if indegree[v]==0:queue.append(v)
assert count==443

# Automorphisms by adjacency-constrained backtracking. For efficiency, respect
# the graph theoretic invariant 'participates in the unique triangle'.
triangles=[tuple(c) for c in combinations(range(12),3)
           if all(adj[x][y] for x,y in combinations(c,2))]
assert len(triangles)==1
in_triangle=set(triangles[0])
classes={v: int(v in in_triangle) for v in range(12)}
order=sorted(range(12),key=lambda v: (0 if v in in_triangle else 1,v))
autos=[]
def extend(mapping,used):
    k=len(mapping)
    if k==12:
        autos.append(tuple(mapping[v] for v in range(12)));return
    u=order[k]
    for x in range(12):
        if x in used or classes[x]!=classes[u]: continue
        if all(adj[u][v]==adj[x][y] for v,y in mapping.items()):
            mapping[u]=x;used.add(x)
            extend(mapping,used)
            used.remove(x);del mapping[u]
extend({},set())
assert len(autos)==12
pm_lookup={p:i for i,p in enumerate(pms)}

# Compute homology trace via *original* complex's oriented chain Lefschetz
# number; independent of nerve/collapse and independent of an equivariant nerve lemma.
def cycle_type(p):
    seen=set();r=[]
    for i in range(len(p)):
        if i not in seen:
            j=i;k=0
            while j not in seen:
                seen.add(j); k+=1;j=p[j]
            r.append(k)
    return tuple(sorted(r))
def character(g):
    emap=[]
    lookup={e:i for i,e in enumerate(edges)}
    for a,b in edges: emap.append(lookup[tuple(sorted((g[a],g[b])) )])
    trace=0
    for f in faces-{0}:
        el=[i for i in range(18) if f&(1<<i)]
        image=[emap[i] for i in el]
        if set(image)!=set(el): continue
        parity=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))%2
        trace+=(-1)**(len(el)-1+parity)
    return 1-trace
def nerve_character(g):
    lookup={e:i for i,e in enumerate(edges)}
    emap=[lookup[tuple(sorted((g[a],g[b])))] for a,b in edges]
    perm=tuple(pm_lookup[sum(1 << emap[e] for e in range(18) if p & (1 << e))]
               for p in pms)
    lefschetz=0
    for f in full_nerve-{frozenset()}:
        a=sorted(f); b=[perm[j] for j in a]
        if set(a)==set(b):
            parity=sum(b[i]>b[j] for i in range(len(b)) for j in range(i+1,len(b)))%2
            lefschetz+=(-1)**(len(a)-1+parity)
    return 1-lefschetz
chr_by_type=defaultdict(list)
for g in autos:
    assert character(g)==nerve_character(g)
    chr_by_type[cycle_type(g)].append(character(g))
expected={
 (1,)*12:[6],
 (1,)*4+(2,)*4:[-2]*3,
 (1,)*6+(2,)*3:[0],
 (1,)*2+(2,)*5:[0]*3,
 (3,)*4:[0]*2,
 (3,)*2+(6,):[0]*2,
}
assert dict(chr_by_type)==expected,(chr_by_type,expected)
assert sum(x for values in chr_by_type.values() for x in values)==0

print('PASS: graph has 12 vertices, 18 edges, one triangle, 12 automorphisms')
print('PASS: eight perfect matchings by independent dynamic-programming and brute-force enumerations')
print('PASS: 443 nonempty simplices, face histogram 18,96,153,120,48,8')
print('PASS: nerve f-vector 8,28,18,3, 15 facets; 18 explicit free-face collapses')
print('PASS: collapse target connected, eight vertices, thirteen edges, cycle rank six')
print('PASS: independent 218-pair acyclic Morse matching, one critical vertex and six critical edges')
print('PASS: complete oriented original-face Hasse diagram acyclic')
print('PASS: complete integral homotopy wedge of six circles')
print('PASS: original-simplex and nerve-chain Lefschetz characters agree on all 12 symmetries')
print('PASS: rational H1 character: identity 6, 3 four-fixed-vertex involutions -2, remaining eight 0')
print('PASS: invariant rational H1 dimension zero')
