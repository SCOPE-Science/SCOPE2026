#!/usr/bin/env python3
"""Independent seven-player tournament interchange graph from a published catalogue.
Enumerates all vertex relabelings of the three regular tournament isomorphism representatives.
Source: Brendan D. McKay, https://users.cecs.anu.edu.au/~bdm/data/rt7.txt
"""
from itertools import permutations, combinations
from collections import Counter

N=7
pairs=list(combinations(range(N),2))
pair_index={p:i for i,p in enumerate(pairs)}
SEEDS=("111000101101101011101", "111000101101011101101", "111000110011011111000")

def make_rows(s):
    assert len(s)==21
    rows=[0]*N
    for (u,v),b in zip(pairs,s):
        a,z=(u,v) if b=='1' else (v,u)
        rows[a] |= (1<<z)
    return tuple(rows)

def serial(rows):
    return ''.join('1' if rows[u]&(1<<v) else '0' for u,v in pairs)

def relabel(rows,p):
    out=[0]*N
    for u in range(N):
        for v in range(N):
            if rows[u] & (1<<v):
                out[p[u]] |= 1<<p[v]
    return tuple(out)

def cyclic(rows,a,b,c):
    return bool(rows[a]&(1<<b)) == bool(rows[b]&(1<<c)) == bool(rows[c]&(1<<a))

seed_rows=[make_rows(s) for s in SEEDS]
all_states={};orbit_states=[]
for tag,r in enumerate(seed_rows):
    orbit={relabel(r,p) for p in permutations(range(N))}
    assert not all_states.keys() & orbit
    orbit_states.append(orbit)
    for q in orbit:all_states[q]=tag
assert len(all_states)==2640, len(all_states)
counts=tuple(map(len,orbit_states))
print('CATALOGUE_LABELLED_ORBIT_SIZES',counts)
assert sorted(counts)==[240,720,1680]

tri=list(combinations(range(N),3))
def neighbor(r,t):
    a,b,c=t
    out=list(r)
    for u,v in ((a,b),(a,c),(b,c)):
        out[u]^=1<<v
        out[v]^=1<<u
    return tuple(out)

states=list(all_states)
index={r:k for k,r in enumerate(states)}
adj=[]
for r in states:
    assert all(x.bit_count()==3 for x in r)
    nei=[]
    for t in tri:
        if cyclic(r,*t):
            q=neighbor(r,t)
            assert q in index
            nei.append(index[q])
    assert len(nei)==14
    adj.append(tuple(nei))
assert all(i in adj[j] for i,ns in enumerate(adj) for j in ns)
assert sum(map(len,adj))//2==18480

def bfs(s):
    dist=[-1]*len(states)
    dist[s]=0
    queue=[s]
    for x in queue:
        for y in adj[x]:
            if dist[y]==-1:
                dist[y]=dist[x]+1
                queue.append(y)
    assert len(queue)==len(states)
    return tuple(Counter(dist)[i] for i in range(max(dist)+1))

orbit_profiles=[]
for i,seed in enumerate(seed_rows):
    p=bfs(index[seed]);orbit_profiles.append(p)
    print('CATALOGUE_ORBIT',i,'SIZE',counts[i],'AUT',5040//counts[i],'PROFILE',p)
assert Counter(zip(counts,orbit_profiles)) == Counter({
    (240,(1,14,91,343,749,871,476,92,3)):1,
    (720,(1,14,91,336,721,822,485,147,22,1)):1,
    (1680,(1,14,91,340,739,853,483,113,6)):1,
})
# All permutations preserve the transition graph. Their orbits are exactly orbit_states,
# so eccentricity is constant on each class.
assert min(len(p)-1 for p in orbit_profiles)==8
assert max(len(p)-1 for p in orbit_profiles)==9
assert sum(len(x) for x in orbit_states)==2640
# A triple reversal flips three bits: the graph is bipartite by inversion parity.
assert all((sum(bool(r[u]&(1<<v)) for u,v in pairs)%2) !=
           (sum(bool(states[j][u]&(1<<v)) for u,v in pairs)%2)
           for r,ns in zip(states,adj) for j in ns)
# The Fano planes are exactly the seven-triple pair-covers of K7.
edge_id={p:i for i,p in enumerate(pairs)}
triple_edge_masks=[sum(1<<edge_id[e] for e in combinations(tr,2)) for tr in tri]
fano_systems=[]
def exact_cover(remaining, selected):
    if remaining==0:
        fano_systems.append(tuple(selected))
        return
    low = remaining & -remaining
    for j, mask in enumerate(triple_edge_masks):
        if mask & low and mask & remaining == mask:
            exact_cover(remaining ^ mask, selected+[j])
exact_cover((1 << 21) - 1, [])
assert len(fano_systems)==30

def is_converse(s,r):
    return all((s[u]^r[u]) == ((1<<N)-1)^(1<<u) for u in range(N))

for i,seed in enumerate(seed_rows):
    good={j for j,tr in enumerate(tri) if cyclic(seed,*tr)}
    num_fano=sum(all(j in good for j in system) for system in fano_systems)
    assert num_fano==(0 if counts[i]==720 else 2)
    anti=tuple(((1<<N)-1)^row^(1<<u) for u,row in enumerate(seed))
    assert is_converse(seed,anti) and anti in index
    # BFS from an entire isomorphism-class representative suffices by relabeling symmetry.
    start=index[seed];dist=[-1]*len(states);dist[start]=0;q=[start]
    for x in q:
        for y in adj[x]:
            if dist[y]<0:dist[y]=dist[x]+1;q.append(y)
    assert len(q)==2640
    assert dist[index[anti]]==(9 if counts[i]==720 else 7)
    if counts[i]==720:
        assert [j for j,v in enumerate(dist) if v==9] == [index[anti]]
    print('CATALOGUE_ORBIT',counts[i],'CYCLIC_FANO',num_fano,'CONVERSE_DISTANCE',dist[index[anti]])
print('CATALOGUE_FANO_CONVERSE_AND_ORBIT_METRIC_PASS')
