"""Exact reproducible enumeration for Petersen line-graph maximum-matching flips.
Pure finite algorithms; requires Python 3 and SciPy for independent shortest-path check.
"""
from itertools import combinations, permutations
from collections import Counter, deque
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

P_VERTS=tuple(combinations(range(5),2))
P_EDGES=tuple((u,v) for u in range(10) for v in range(u+1,10)
              if set(P_VERTS[u]).isdisjoint(P_VERTS[v]))
assert len(P_EDGES)==15
N=len(P_EDGES)
L_EDGES=tuple((a,b) for a in range(N) for b in range(a+1,N)
              if len(set(P_EDGES[a])&set(P_EDGES[b]))==1)
assert len(L_EDGES)==30
ADJ=tuple(frozenset(v for u,v in L_EDGES if u==x) |
          frozenset(u for u,v in L_EDGES if v==x) for x in range(N))

# Enumeration A: choose one exposed vertex, then recursively pair the smallest
# remaining vertex. This partitions the set of near-perfect matchings by hole.
def build_A():
    out=set()
    def dfs(remaining, chosen):
        if not remaining:
            out.add(frozenset(chosen));return
        v=min(remaining)
        for w in ADJ[v]&remaining:
            M=tuple(sorted((v,w)))
            dfs(remaining-{v,w}, chosen+(M,))
    for h in range(N):
        dfs(set(range(N))-{h}, ())
    return out

# Enumeration B: independent 7-subsets of L(P)'s 30 edges, selected directly
# among 30 choose 7 distinct candidate combinations. Tests incidence masks.
def build_B():
    out=set()
    for comb in combinations(range(len(L_EDGES)),7):
        mask=0
        for k in comb:
            u,v=L_EDGES[k]
            new=(1<<u)|(1<<v)
            if mask&new:break
            mask|=new
        else:
            assert mask.bit_count()==14
            out.add(frozenset(L_EDGES[k] for k in comb))
    return out

A=build_A(); B=build_B()
assert A==B and len(A)==480
states=tuple(sorted(A,key=lambda M:tuple(sorted(M))))
ix={M:i for i,M in enumerate(states)}
H=lambda M:(set(range(N))-set().union(*map(set,M))).pop()
assert Counter(H(M) for M in states)==Counter({h:32 for h in range(N)})

# Adjacency A: slide an edge through the single exposed vertex.
nbrs=[set() for M in states]
for i,M in enumerate(states):
    hole=H(M)
    for v in ADJ[hole]:
        matched_edge=next(e for e in M if v in e)
        other=next(w for w in matched_edge if w!=v)
        flipped=(M-{matched_edge})|{tuple(sorted((hole,v)))}
        nbrs[i].add(ix[flipped])
assert {len(x) for x in nbrs}=={4}
assert all(i in nbrs[j] for i,neigh in enumerate(nbrs) for j in neigh)

# Adjacency B: compare all 480 choose 2 pairs, no graph-generation dependence.
other=set()
for i in range(480):
    for j in range(i+1,480):
        M,T=states[i],states[j]
        if len(M-T)==len(T-M)==1:
            e=next(iter(M-T));f=next(iter(T-M))
            if bool(set(e)&set(f)):
                other.add((i,j))
ours={(i,j) for i in range(480) for j in nbrs[i] if i<j}
assert ours==other and len(ours)==960

# Exhaustive distances by BFS from every state, with independent SciPy check.
D=[]; ecc=Counter(); dist_h=Counter(); detour=Counter(); far=[set() for i in range(480)]
level_hist=Counter()
for i,M in enumerate(states):
    row=[-1]*480;row[i]=0;q=deque([i])
    while q:
        u=q.popleft()
        for v in nbrs[u]:
            if row[v]<0:row[v]=row[u]+1;q.append(v)
    assert -1 not in row
    D.append(row)
    ecc[max(row)]+=1
    counts=Counter(row)
    level_hist[tuple(counts[k] for k in range(10))]+=1
    far[i]={j for j,x in enumerate(row) if x==9}
    for j in range(i+1,480):
        d=row[j]; dist_h[d]+=1
        detour[d-len(M-states[j])]+=1
assert ecc=={9:480}
assert all(len(x)==2 for x in far)
assert dist_h=={1:960,2:2400,3:6120,4:13080,5:23310,6:32730,7:26550,8:9330,9:480}
assert detour=={0:81120,1:32340,2:900,3:600}
mat=csr_matrix(([1]*len(ours)*2,
       ([i for i,j in ours]+[j for i,j in ours],
        [j for i,j in ours]+[i for i,j in ours])),shape=(480,480))
Ds=shortest_path(mat,directed=False,unweighted=True)
assert all(int(Ds[i,j])==D[i][j] for i in range(480) for j in range(480))

# Distance-nine graph consists of 120 induced four-cycles, each same exposed vertex.
seen=set();comps=[]
for i in range(480):
    if i in seen:continue
    comp={i};q=[i];seen.add(i)
    for u in q:
        for v in far[u]:
            if v not in seen:seen.add(v);comp.add(v);q.append(v)
    comps.append(comp)
assert len(comps)==120
assert all(len(c)==4 for c in comps)
assert all(len({H(states[i]) for i in c})==1 for c in comps)
assert all(sum(j in far[i] for j in c)==2 for c in comps for i in c)

# The 120 natural automorphisms S5 on the ground 5-set yield exactly 6 orbits.
perms=list(permutations(range(5)))
maps=[]
for p in perms:
    vmap={i:P_VERTS.index(tuple(sorted(p[t] for t in v))) for i,v in enumerate(P_VERTS)}
    edge_map={i:P_EDGES.index(tuple(sorted((vmap[u],vmap[v])))) for i,(u,v) in enumerate(P_EDGES)}
    s_map=[]
    for M in states:
        transformed=frozenset(tuple(sorted((edge_map[u],edge_map[v]))) for u,v in M)
        s_map.append(ix[transformed])
    assert all(set(s_map[j] for j in nbrs[i])==nbrs[s_map[i]] for i in range(480))
    maps.append(s_map)
seen=set();orbits=[]
for i in range(480):
    if i in seen:continue
    orb={smap[i] for smap in maps};seen.update(orb);orbits.append(orb)
assert len(orbits)==6
assert Counter(map(len,orbits))=={120:2,60:4}
assert sum(level_hist.values())==480
assert len(level_hist)==6
print('VERIFY_OK')
print('Base: Petersen 10 vertices 15 edges; its line graph 15 vertices 30 edges.')
print('Max matchings 480, exposed-vertex count 32 each; 4-regular slide graph edges 960.')
print('Connected, every eccentricity 9. Exactly 2 distance-nine vertices per state.')
print('Distance-nine graph: 120 disjoint C4, same exposed vertex on each C4.')
print('Distance histograms unordered pairs:',sorted(dist_h.items()))
print('Distance-minus-set-difference histograms unordered pairs:',sorted(detour.items()))
print('S5 orbit sizes:',sorted(map(len,orbits)))
print('Source distance profile multiplicities:', sorted(level_hist.items()))
# Finite witness of a Hamilton cycle in the full matching graph.
with open('hamcycle.txt',encoding='ascii') as hf:
    cyc=[int(x) for x in hf.read().strip().split(',')]
assert len(cyc)==480 and sorted(cyc)==list(range(480))
assert all(cyc[(i+1)%480] in nbrs[cyc[i]] for i in range(480))
print('Hamilton cycle certificate verified (480 distinct vertices, including closing edge).')
