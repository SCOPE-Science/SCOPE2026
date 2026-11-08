"""Exact census and quotient certificate using GP(10,2); standard library only."""
from itertools import combinations
from collections import Counter, deque
import json

N = 20
neighbors = [set() for _ in range(N)]
def edge(a,b):
    neighbors[a].add(b)
    neighbors[b].add(a)
for i in range(10):
    edge(i,(i+1)%10)
    edge(i,10+i)
    edge(10+i,10+(i+2)%10)
assert all(len(s)==3 for s in neighbors)
open_masks = [sum(1<<v for v in s) for s in neighbors]
full=(1<<N)-1

# Every subset with cardinality at most eight is tested, including zero.
small=[0]*9
states=[]
for k in range(9):
    for tup in combinations(range(N),k):
        mask=0
        dominated=0
        for v in tup:
            mask|=1<<v
            dominated|=open_masks[v]
        if dominated==full:
            small[k]+=1
            if k==8:states.append(mask)
assert small == [0,0,0,0,0,0,0,0,190]
lookup={s:i for i,s in enumerate(states)}
assert len(lookup)==190
J=[set() for _ in states]
S=[set() for _ in states]
for i,m in enumerate(states):
    for a in range(N):
        if m>>a&1:
            for b in range(N):
                if not m>>b&1:
                    j=lookup.get(m^(1<<a)^(1<<b))
                    if j is not None:
                        J[i].add(j)
                        if b in neighbors[a]:S[i].add(j)
assert all(i in J[j] for i,ls in enumerate(J) for j in ls)
assert all(not ls for ls in S)
assert sum(map(len,J))//2==360
assert Counter(map(len,J))==Counter({4:120,0:40,8:30})

def components(graph,nodes=None):
    remaining=set(range(len(graph)) if nodes is None else nodes)
    out=[]
    while remaining:
        c=[min(remaining)]
        remaining.remove(c[0])
        for i in c:
            for j in graph[i]:
                if j in remaining:
                    remaining.remove(j)
                    c.append(j)
        out.append(set(c))
    return out
cc=components(J)
assert Counter(map(len,cc))==Counter({1:40,150:1})
big=next(c for c in cc if len(c)==150)
# Exact all-source distances, rather than sampled BFS.
ecc=[]
for source in sorted(big):
    q=deque([source]);dist={source:0}
    while q:
        a=q.popleft()
        for b in J[a]:
            if b not in dist:
                dist[b]=dist[a]+1
                q.append(b)
    assert len(dist)==150
    ecc.append(max(dist.values()))
assert Counter(ecc)==Counter({10:150})

# The degree-four vertices induce twenty disjoint 6-cycles.
low=set(i for i in big if len(J[i])==4)
sub=[J[i]&low for i in range(len(J))]
hexes=sorted(tuple(sorted(c)) for c in components(sub,low))
assert len(hexes)==20 and all(len(h)==6 for h in hexes)
assert all(len(sub[i])==2 for i in low)
which={i:k for k,h in enumerate(hexes) for i in h}
hubs=sorted(i for i in big if len(J[i])==8)
assert len(hubs)==30
q_edges=set()
for i in hubs:
    incidences=Counter(which[j] for j in J[i])
    assert sorted(incidences.values())==[4,4]
    q_edges.add(frozenset(incidences))
assert len(q_edges)==30
assert Counter(x for edge_pair in q_edges for x in edge_pair)==Counter({i:3 for i in range(20)})

# Explicit 20-vertex bijection: quotient -> Desargues GP(10,3).
phi=[0,1,3,2,12,11,17,14,13,4,5,18,10,19,9,8,16,15,7,6]
assert sorted(phi)==list(range(20))
target={frozenset((i,(i+1)%10)) for i in range(10)}
target.update(frozenset((i,10+i)) for i in range(10))
target.update(frozenset((10+i,10+(i+3)%10)) for i in range(10))
assert {frozenset(phi[i] for i in e) for e in q_edges}==target

# Independently test an order-120 graph automorphism subgroup and its five set orbits.
p0=(9,0,1,2,3,4,5,6,7,8,19,10,11,12,13,14,15,16,17,18)
p1=(0,1,11,13,15,5,6,16,18,10,9,2,19,3,17,4,7,14,8,12)
gens=[p0,p1]
for p in gens:
    assert sorted(p)==list(range(N))
    assert all({p[v] for v in neighbors[i]} == neighbors[p[i]] for i in range(N))
identity=tuple(range(N));group={identity};todo=[identity]
for p in todo:
    for g in gens:
        t=tuple(p[g[i]] for i in range(N))
        if t not in group:
            group.add(t)
            todo.append(t)
assert len(group)==120
# Complete (not merely generated) automorphism group verification:
# enumerate every adjacency-preserving permutation with exact backtracking.
assigned={}
used=set()
all_automorphisms=0
def automorphism_backtrack():
    global all_automorphisms
    if len(assigned)==N:
        all_automorphisms+=1
        assert tuple(assigned[i] for i in range(N)) in group
        return
    v=max((z for z in range(N) if z not in assigned),
          key=lambda z:(len(neighbors[z]&assigned.keys()),-z))
    for w in range(N):
        if w in used:
            continue
        if any((q in neighbors[v])!=(assigned[q] in neighbors[w]) for q in assigned):
            continue
        assigned[v]=w
        used.add(w)
        automorphism_backtrack()
        used.remove(w)
        del assigned[v]
automorphism_backtrack()
assert all_automorphisms==120
unseen=set(states)
orbits=[]
while unseen:
    m=min(unseen)
    orbit={sum(1<<p[i] for i in range(N) if m>>i&1) for p in group}
    assert orbit<=unseen
    unseen-=orbit
    orbits.append((len(orbit),len(J[lookup[m]])))
assert Counter(orbits)==Counter({(60,4):2,(30,8):1,(30,0):1,(10,0):1})

result={
 'model':'GP(10,2)', 'total_domination_number':8,'minimum_total_domination_sets':190,
 'counts_by_size_up_to_8':small,
 'automorphism_group_order':120,'orbit_size_degree_pairs':sorted(orbits),
 'slide_edges':0,'jump_edges':360,'jump_degree_histogram':dict(sorted(Counter(map(len,J)).items())),
 'jump_component_size_histogram':dict(sorted(Counter(map(len,cc)).items())),
 'nontrivial_component_radius':min(ecc),'nontrivial_component_diameter':max(ecc),
 'six_cycle_count':len(hexes),'six_cycle_size':6,'hub_count':30,
 'hub_incidence_multiplicities':[4,4], 'quotient_isomorphic_to':'GP(10,3) = Desargues graph',
 'quotient_to_gp103_bijection':phi,
}
print(json.dumps(result,sort_keys=True))
