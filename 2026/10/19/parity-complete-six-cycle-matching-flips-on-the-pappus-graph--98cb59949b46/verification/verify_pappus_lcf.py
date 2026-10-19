#!/usr/bin/env python3
"""Self-contained exhaustive certificate: the Pappus graph's 6-cycle-flip graph."""
from collections import Counter, deque

N = 18
shifts = (5, 7, -7, 7, -7, -5) * 3
E = {tuple(sorted((i, (i+1)%N))) for i in range(N)}
E.update(tuple(sorted((i, (i+shifts[i])%N))) for i in range(N))
assert len(E) == 27
adj = [set() for _ in range(N)]
for i,j in E:
    adj[i].add(j); adj[j].add(i)
assert set(map(len,adj)) == {3}

# Exhaustive perfect matchings by the least-unmatched-vertex recurrence.
def complete(mask, edges):
    if not mask:
        yield frozenset(edges); return
    i=(mask & -mask).bit_length()-1
    for j in sorted(adj[i]):
        if mask & (1<<j):
            yield from complete(mask^(1<<i)^(1<<j), edges+((i,j),))
matchings=sorted(set(complete((1<<N)-1, ())), key=lambda m: tuple(sorted(m)))
assert len(matchings) == 42
index = {m:i for i,m in enumerate(matchings)}

# Exhaustive simple six-cycles, represented without orientation or start-point.
cycles=set()
def extend(path):
    if len(path)==6:
        if path[-1] in adj[path[0]]:
            cycles.add(frozenset(tuple(sorted((path[k],path[(k+1)%6]))) for k in range(6)))
        return
    for v in sorted(adj[path[-1]]):
        if v not in path:
            extend(path+[v])
for u in range(N):extend([u])
assert len(cycles)==18

G=[set() for _ in matchings]
for i,m in enumerate(matchings):
    for cycle in cycles:
        if len(m&cycle)==3:
            j=index[m^cycle]
            G[i].add(j)
assert all(i in G[j] for i,a in enumerate(G) for j in a)
assert sum(map(len,G))//2==72
assert Counter(map(len,G)) == Counter({3:36,6:6})

# A component must consist of three hubs plus a six-cycle on each hub-pair.
# Each low-degree cycle alternates which hub its vertices attach to.
def comp_structure(vertices):
    hubs={u for u in vertices if len(G[u])==6}
    assert len(vertices)==21 and len(hubs)==3
    low=set(vertices)-hubs
    assert len(low)==18 and all(len(G[u])==3 for u in low)
    assert all(not (G[u]&hubs) for u in hubs)
    labels={u:next(iter(G[u]&hubs)) for u in low}
    assert all(len(G[u]&hubs)==1 and len(G[u]&low)==2 for u in low)
    chunks=[];unseen=set(low)
    while unseen:
        start=min(unseen);reach={start};todo=[start]
        while todo:
            u=todo.pop()
            for v in G[u]&low:
                if v not in reach:reach.add(v);todo.append(v)
        unseen.difference_update(reach)
        assert len(reach)==6
        assert all(len(G[u]&reach)==2 for u in reach)
        hubpair=frozenset(labels[u] for u in reach)
        assert len(hubpair)==2
        assert all(labels[u]!=labels[v] for u in reach for v in G[u]&reach)
        chunks.append(hubpair)
    assert Counter(chunks)==Counter(frozenset(p) for p in __import__('itertools').combinations(hubs,2))
    # Exact eccentricity via all-vertex BFS, not sampling.
    distances=[]
    for s in vertices:
        d={s:0};q=deque([s])
        while q:
            u=q.popleft()
            for v in G[u]:
                if v not in d:d[v]=d[u]+1;q.append(v)
        assert set(d)==vertices
        distances.extend(d.values())
    assert max(distances)==4
    return Counter(distances)

remaining=set(range(42)); components=[]
while remaining:
    s=min(remaining);seen={s};stack=[s]
    while stack:
        u=stack.pop()
        for v in G[u]:
            if v not in seen:seen.add(v);stack.append(v)
    remaining.difference_update(seen)
    components.append(seen)
assert sorted(map(len,components))==[21,21]
assert comp_structure(components[0])==comp_structure(components[1])

# Parity of bijection between the two graph bipartition classes is flip-invariant.
color={0:0};queue=deque([0])
while queue:
    u=queue.popleft()
    for v in adj[u]:
        if v not in color:color[v]=1-color[u];queue.append(v)
        else:assert color[v]!=color[u]
left=sorted(u for u in color if color[u]==0);right=sorted(u for u in color if color[u]==1)
assert len(left)==len(right)==9
right_position={u:i for i,u in enumerate(right)}
def parity(m):
    bij=[right_position[next(v for v in adj[u] if tuple(sorted((u,v))) in m)] for u in left]
    return (-1)**sum(bij[i]>bij[j] for i in range(9) for j in range(i+1,9))
signs=[parity(m) for m in matchings]
assert Counter(signs)=={1:21,-1:21}
assert all(signs[i]==signs[j] for i,ng in enumerate(G) for j in ng)
assert {frozenset(c) for c in components}=={frozenset(i for i,v in enumerate(signs) if v==s) for s in [-1,1]}
print('LCF_VERIFY_OK vertices=18 edges=27 six_cycles=18 perfect_matchings=42')
print('LCF_VERIFY_OK flips=72 components=21+21 each_component_diameter=4')
print('LCF_VERIFY_OK degree_distribution=3:36,6:6 each_component=three_hubs_with_alternating_hexagons_on_hub_pairs')
print('LCF_VERIFY_OK permutation_sign_classes=21+21 exact_reachability_by_sign=true')
