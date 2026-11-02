"""Independent Hamiltonian-path enumeration of the Tutte--Coxeter decagon moves.
Run with python3 verify_cycles.py; standard library only.
"""
from itertools import combinations
from collections import Counter, deque

DUADS=list(combinations(range(6),2))
def synthemes(items):
    if not items:
        yield frozenset();return
    a=items[0]
    for b in items[1:]:
        for rest in synthemes(tuple(x for x in items if x!=a and x!=b)):
            yield rest|{frozenset((a,b))}
S=sorted(set(synthemes(tuple(range(6)))),key=lambda s:tuple(sorted(map(lambda x:tuple(sorted(x)),s))))
assert len(S)==15
ADJ=[set() for _ in range(30)]
for i,d in enumerate(DUADS):
    for j,s in enumerate(S):
        if frozenset(d) in s:
            ADJ[i].add(15+j); ADJ[15+j].add(i)
assert all(len(row)==3 for row in ADJ)

# Each undirected spanning cycle occurs twice as an oriented path beginning at vertex zero.
CYCLES=set()
def walk(path,seen):
    last=path[-1]
    if len(path)==30:
        if 0 in ADJ[last]:
            route=path
            forward=tuple(route)
            reverse=(0,)+tuple(reversed(route[1:]))
            CYCLES.add(min(forward,reverse))
        return
    for v in ADJ[last]:
        if v not in seen:
            seen.add(v);path.append(v)
            walk(path,seen)
            path.pop();seen.remove(v)
walk([0],{0})
assert len(CYCLES)==144,len(CYCLES)
EDGES=sorted((i,j) for i in range(30) for j in ADJ[i] if i<j)
INDEX={edge:k for k,edge in enumerate(EDGES)}

def edge_set(path):
    mask=0
    for a,b in zip(path,path[1:]+path[:1]):
        mask |= 1<<INDEX[(a,b) if a<b else (b,a)]
    return mask

MASKS=sorted(edge_set(list(c)) for c in CYCLES)
assert len(MASKS)==len(set(MASKS))==144
G=[set() for _ in MASKS]
for i in range(144):
    for j in range(i+1,144):
        delta=MASKS[i]^MASKS[j]
        if delta.bit_count()==10:
            degrees=Counter()
            boundary=[set() for _ in range(30)]
            for k,(a,b) in enumerate(EDGES):
                if delta>>k&1:
                    boundary[a].add(b);boundary[b].add(a)
            support={u for u in range(30) if boundary[u]}
            assert len(support)==10 and all(len(boundary[u])==2 for u in support)
            seen={next(iter(support))};todo=list(seen)
            while todo:
                for v in boundary[todo.pop()]:
                    if v not in seen:seen.add(v);todo.append(v)
            assert seen==support
            G[i].add(j);G[j].add(i)
        else:
            assert delta.bit_count()>10
assert all(len(nbrs)==7 for nbrs in G)
assert sum(len(nbrs) for nbrs in G)//2==504
for s in range(144):
    d={s:0};q=deque([s])
    while q:
        u=q.popleft()
        for v in G[u]:
            if v not in d:d[v]=d[u]+1;q.append(v)
    assert len(d)==144
    assert [Counter(d.values())[k] for k in range(5)]==[1,7,36,85,15]
print('HAMILTONIAN_DFS_144_UNDIRECTED_CYCLES_PASS')
print('INDEPENDENT_EDGESET_TEN_FLIP_504_EDGES_PASS')
print('INDEPENDENT_DISTANCES_1_7_36_85_15_DIAMETER_4_PASS')
