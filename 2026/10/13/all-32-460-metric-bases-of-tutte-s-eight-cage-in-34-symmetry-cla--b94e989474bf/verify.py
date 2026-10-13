#!/usr/bin/env python3
"""Exact census of Tutte--Coxeter metric bases; Python 3 standard library."""
from itertools import combinations, permutations
from collections import Counter

N=6
edges=list(combinations(range(N), 2))
edge_index={e:i for i,e in enumerate(edges)}
matchings=[]
def extend(remaining, acc):
    if not remaining:
        matchings.append(tuple(sorted(acc)))
        return
    a=remaining[0]
    for b in remaining[1:]:
        extend(tuple(x for x in remaining if x not in (a,b)), acc+(edge_index[a,b],))
extend(tuple(range(N)),())
matchings=sorted(matchings)
assert len(edges)==len(matchings)==15
matching_index={f:i for i,f in enumerate(matchings)}
V=30
neighbors=[set() for _ in range(V)]
for i,F in enumerate(matchings):
    for j in F:
        neighbors[i].add(15+j)
        neighbors[15+j].add(i)
assert len({tuple(sorted(a)) for a in neighbors})==30
assert all(len(a)==3 for a in neighbors)

def geometric_distance(u,v):
    if u==v:return 0
    if u>=15 and v>=15:
        e=edges[u-15];f=edges[v-15]
        return 2 if len(set(e)&set(f))==0 else 4
    if u<15 and v<15:
        return 2 if set(matchings[u])&set(matchings[v]) else 4
    if u<15:return 1 if v-15 in matchings[u] else 3
    return 1 if u-15 in matchings[v] else 3
D=[[geometric_distance(u,v) for v in range(V)] for u in range(V)]
# Independent graph-distance reconstruction
for u in range(V):
    d=[-1]*V;d[u]=0;queue=[u]
    for x in queue:
        for y in neighbors[x]:
            if d[y]<0:d[y]=d[x]+1;queue.append(y)
    assert d==D[u],(u,d,D[u])
assert max(map(max,D))==4

# Every cross-class vertex pair is resolved by every landmark (parity).
assert all(D[w][i]!=D[w][j] for w in range(V) for i in range(15) for j in range(15,30))
pair_masks=[]
for u,v in combinations(range(V),2):
    if (u<15)!=(v<15):continue
    mask=sum(1<<w for w in range(V) if D[w][u]!=D[w][v])
    pair_masks.append(mask)
assert len(pair_masks)==210 and len(set(pair_masks))==210

def hit(mask):return all(mask&m for m in pair_masks)
assert sum(hit(sum(1<<i for i in C)) for C in combinations(range(V),5))==0
bases=[];profile=Counter()
for C in combinations(range(V),6):
    mask=sum(1<<i for i in C)
    if hit(mask):
        bases.append(mask)
        n_match=sum(i<15 for i in C)
        internal=sum(v in neighbors[u] for u in C for v in C)//2
        profile[n_match,internal]+=1
assert len(bases)==32460
assert dict(sorted(profile.items()))=={
    (2,0):4230,(2,1):2880,(2,2):360,
    (3,0):3840,(3,1):7920,(3,2):5760,
    (4,0):4230,(4,1):2880,(4,2):360}
# Symmetric group on the six symbols induces 720 automorphisms of the Levi graph.
within=[]
for p in permutations(range(N)):
    e_map=[edge_index[tuple(sorted((p[a],p[b])))] for a,b in edges]
    f_map=[matching_index[tuple(sorted(e_map[e] for e in F))] for F in matchings]
    within.append(tuple(f_map+[15+x for x in e_map]))
assert len(set(within))==720
# Explicit duality. Verify all 45 incidences, rather than trusting its origin.
dual=(15,24,29,25,19,21,28,20,18,22,17,26,16,23,27,0,13,9,7,5,4,8,12,10,2,11,6,3,14,1)
assert len(set(dual))==V and all((u<15)!=(dual[u]<15) for u in range(V))
aut=within+[tuple(dual[q[i]] for i in range(V)) for q in within]
assert len(set(aut))==1440
for p in aut:
    for u in range(V):
        assert {p[v] for v in neighbors[u]}==neighbors[p[u]]

def image(mask,p):
    out=0
    while mask:
        low=mask&-mask
        out|=1<<p[low.bit_length()-1]
        mask-=low
    return out
remaining=set(bases);orbits=[]
while remaining:
    rep=min(remaining)
    O={image(rep,p) for p in aut}
    assert O<=remaining
    orbits.append((rep,len(O)))
    remaining.difference_update(O)
assert len(orbits)==34
sizes=Counter(size for _,size in orbits)
assert sizes=={180:1,240:1,360:1,720:18,1440:13}
assert sum(k*v for k,v in sizes.items())==len(bases)
print('VERIFY_OK graph=K6_edges_vs_1factors vertices=30 edges=45 diameter=4')
print('VERIFY_OK distance_models=incidence_formula+independent_BFS match')
print('VERIFY_OK distinguishing_constraints=210 distinct_cross_pairs_all_auto_resolved')
print('VERIFY_OK tested_5_subsets=142506 zero_resolving; tested_6_subsets=593775 bases=32460')
print('VERIFY_OK subgroup=S6_extended_by_verified_duality automorphisms=1440')
print('VERIFY_OK orbits=34 sizes=180x1+240x1+360x1+720x18+1440x13')
print('VERIFY_OK side_splits=2+4:7470,3+3:17520,4+2:7470')
