#!/usr/bin/env python3
"""Independent three-step excitation dynamics on several labelled cacti."""
from itertools import product

def make_graph(cycles, bridges=()):
    edges=set()
    for cyc in cycles:
        if len(cyc)<3 or len(set(cyc))!=len(cyc):
            raise ValueError('invalid cycle')
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            edges.add(tuple(sorted((a,b))))
    for a,b in bridges:
        edges.add(tuple(sorted((a,b))))
    n=max(max(e) for e in edges)+1
    assert set().union(*(set(e) for e in edges))==set(range(n))
    adjacency=[set() for _ in range(n)]
    for a,b in edges:
        adjacency[a].add(b);adjacency[b].add(a)
    return tuple(tuple(sorted(z)) for z in adjacency)

def step(state,adj):
    return tuple(2 if s==1 else 0 if s==2 else int(any(state[w]==1 for w in adj[v]))
                 for v,s in enumerate(state))

def census(adj):
    answer=0
    local_answer=0
    fixed=0
    for state in product(range(3),repeat=len(adj)):
        f=step(state,adj)
        f3=step(step(f,adj),adj)
        is_primitive=(f3==state and f!=state)
        is_local=all(any(state[w]==(state[v]+1)%3 for w in adj[v]) for v in range(len(adj)))
        assert is_primitive==is_local,(state,is_primitive,is_local)
        answer+=is_primitive
        fixed+=(f==state)
        local_answer+=is_local
    assert fixed==1
    assert answer==local_answer
    return answer

def predicted(cycles):
    resonant=[c for c in cycles if len(c)%3==0]
    if len(resonant)!=1: return None
    result=6
    for cycle in cycles:
        if len(cycle)%3: result*=2*((len(cycle)-1)//3)+1
    return result

cases=[
    ('single triangle',[[0,1,2]],[],6),
    ('triangle with square petal',[[0,1,2],[2,3,4,5]],[],18),
    ('triangle with pentagon petal',[[0,1,2],[0,3,4,5,6]],[],18),
    ('triangle with heptagon petal',[[0,1,2],[2,3,4,5,6,7,8]],[],30),
    ('two square petals at different core vertices',[[0,1,2],[0,3,4,5],[2,6,7,8]],[],54),
    ('nested square and pentagon',[[0,1,2],[2,3,4,5],[5,6,7,8,9]],[],54),
    ('nested squares with a bridge',[[0,1,2],[2,3,4,5],[5,6,7,8]],[(8,9)],54),
    ('hexagon and square',[[0,1,2,3,4,5],[5,6,7,8]],[],18),
    ('triangle, square and path of two',[[0,1,2],[2,3,4,5]],[(5,6),(6,7)],18),
    ('no resonant cycle',[[0,1,2,3],[3,4,5,6,7]],[],0),
]
total=0
for name,cycles,bridges,expected in cases:
    adj=make_graph(cycles,bridges)
    actual=census(adj)
    assert actual==expected,(name,actual,expected)
    if predicted(cycles) is not None:assert actual==predicted(cycles)
    total+=3**len(adj)
    print(f'{name}: n={len(adj)} count={actual}, expected={expected}')
print(f'PASS: {len(cases)} independent graphs, {total} exhaustively checked configurations, all three-step and successor-neighbor checks agree')
