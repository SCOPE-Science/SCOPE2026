"""Exhaustive matching-based proof certificate for a Tutte--Coxeter trade graph.
Run with python3 verify_matchings.py; standard library only.
"""
from collections import Counter, deque
from itertools import combinations

DUADS=list(combinations(range(6),2))
def partitions(a):
    if not a:
        yield (); return
    u=min(a)
    for v in sorted(a-{u}):
        for tail in partitions(a-{u,v}):
            yield tuple(sorted(((u,v),)+tail))
SYNTHEMES=sorted(set(partitions(set(range(6)))))
assert len(DUADS)==len(SYNTHEMES)==15
EDGES=sorted((i,15+j) for i,d in enumerate(DUADS) for j,s in enumerate(SYNTHEMES) if d in s)
assert len(EDGES)==45
NEIGH=[set() for _ in range(30)]
for i,(u,v) in enumerate(EDGES): NEIGH[u].add((v,i)); NEIGH[v].add((u,i))

def all_matchings(unmatched, mask=0):
    if not unmatched:
        yield mask; return
    u=min(unmatched)
    for v,e in sorted(NEIGH[u]):
        if v in unmatched:
            yield from all_matchings(unmatched-{u,v},mask | (1<<e))

MATCHINGS=list(all_matchings(set(range(30))))
assert len(MATCHINGS)==288 and len(set(MATCHINGS))==288

def factor_components(mask):
    adjacency=[[] for _ in range(30)]
    for e,(u,v) in enumerate(EDGES):
        if not(mask>>e)&1:
            adjacency[u].append(v); adjacency[v].append(u)
    assert all(len(row)==2 for row in adjacency)
    unseen=set(range(30)); sizes=[]
    while unseen:
        start=min(unseen); stack=[start]; unseen.remove(start); size=0
        while stack:
            u=stack.pop();size+=1
            for v in adjacency[u]:
                if v in unseen: unseen.remove(v);stack.append(v)
        sizes.append(size)
    return tuple(sorted(sizes))

FACTORS=Counter(factor_components(m) for m in MATCHINGS)
assert FACTORS=={(30,):144,(10,20):144}, FACTORS
H=sorted(m for m in MATCHINGS if factor_components(m)==(30,))
assert len(H)==144

def is_single_cycle(delta):
    adj={}
    for e,(u,v) in enumerate(EDGES):
        if (delta>>e)&1:
            adj.setdefault(u,[]).append(v);adj.setdefault(v,[]).append(u)
    if not adj or any(len(row)!=2 for row in adj.values()): return False
    root=next(iter(adj));seen={root};todo=[root]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    return len(seen)==len(adj)

ADJ=[set() for _ in H]
for i in range(len(H)):
    for j in range(i+1,len(H)):
        delta=H[i]^H[j]
        if delta.bit_count()==10:
            assert is_single_cycle(delta), ('noncycle',i,j)
            ADJ[i].add(j);ADJ[j].add(i)
        elif delta.bit_count()<10:
            raise AssertionError('shorter move between distinct Hamiltonian cycles')
assert all(len(row)==7 for row in ADJ)
assert sum(map(len,ADJ))//2==504
for root in range(144):
    dist={root:0};todo=deque([root])
    while todo:
        u=todo.popleft()
        for v in ADJ[u]:
            if v not in dist: dist[v]=dist[u]+1;todo.append(v)
    assert len(dist)==144
    assert tuple(Counter(dist.values())[k] for k in range(5))==(1,7,36,85,15)
print('MATCHING_ENUM_288_COMPLEMENT_144_HAMILTONIAN_PASS')
print('DECAGON_TRADE_504_EDGES_7_REGULAR_144_ALL_ROOTS_PASS')
print('DISTANCE_PROFILE_1_7_36_85_15_DIAMETER_4_PASS')
