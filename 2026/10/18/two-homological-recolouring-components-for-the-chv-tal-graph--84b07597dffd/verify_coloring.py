#!/usr/bin/env python3
"""Exact standard-library certificate for four-color recoloring on the Chvatal graph."""
from collections import Counter, defaultdict, deque
from itertools import combinations

EDGES = [(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
         (2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
         (5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
N = [set() for _ in range(12)]
for u,v in EDGES:
    N[u].add(v); N[v].add(u)
assert all(len(n)==4 for n in N)
assert not any(u in N[v] and v in N[w] and w in N[u]
               for u,v,w in combinations(range(12),3))

# An explicit signed 2-cycle in the ordinary open-neighborhood complex.
Z = {
 (0,2,7):1, (0,2,10):-1, (0,3,8):-1, (0,3,11):1,
 (0,5,7):-1, (0,5,8):1, (0,10,11):-1, (1,3,8):1,
 (1,3,11):-1, (1,4,9):-1, (1,4,10):1, (1,6,8):-1,
 (1,6,9):1, (1,10,11):1, (2,4,9):1, (2,4,10):-1,
 (2,7,9):-1, (5,6,8):1, (5,6,9):-1, (5,7,9):1}
faces = [set() for _ in range(4)]
for neigh in N:
    for k in range(1,5):
        faces[k-1].update(combinations(sorted(neigh),k))
assert tuple(len(layer) for layer in faces)==(12,42,44,12)
assert set(Z).issubset(faces[2])
edge_boundary = Counter()
for (a,b,c),co in Z.items():
    edge_boundary[b,c]+=co
    edge_boundary[a,c]-=co
    edge_boundary[a,b]+=co
assert all(x==0 for x in edge_boundary.values())

START=(0,1,0,1,2,0,1,0,1,2,3,3)
def proper(c):
    return all(c[u]!=c[v] for u,v in EDGES)
assert proper(START)

def enumerate_colorings(q):
    cur=[-1]*12
    result=[]
    def visit(v):
        if v==12:
            result.append(tuple(cur));return
        forbidden={cur[w] for w in N[v] if cur[w]>=0}
        for x in range(q):
            if x not in forbidden:
                cur[v]=x;visit(v+1)
        cur[v]=-1
    visit(0)
    return result
assert enumerate_colorings(3)==[]
colors=enumerate_colorings(4)
assert len(colors)==18024 and len(set(colors))==18024
color_set=set(colors)

def one_site_neighbours(c):
    for v in range(12):
        prohibited={c[w] for w in N[v]}
        for x in range(4):
            if x!=c[v] and x not in prohibited:
                nxt=list(c);nxt[v]=x
                yield tuple(nxt)

def breadth_first(seed):
    seen={seed}
    todo=deque([seed])
    while todo:
        v=todo.popleft()
        for nxt in one_site_neighbours(v):
            assert nxt in color_set
            if nxt not in seen:
                seen.add(nxt);todo.append(nxt)
    return seen

C0=breadth_first(START)
TRANSPOSED=tuple(1 if x==0 else 0 if x==1 else x for x in START)
C1=breadth_first(TRANSPOSED)
assert len(C0)==len(C1)==9012
assert not (C0 & C1)
assert C0 | C1 == color_set

# Induced map to the tetrahedral boundary: signed coefficient of [1,2,3].
def degree_on_Z(c):
    image=Counter()
    for tri,co in Z.items():
        values=tuple(c[v] for v in tri)
        if len(set(values))!=3:
            continue
        sgn=(-1)**sum(values[i]>values[j] for i in range(3)
                       for j in range(i+1,3))
        image[tuple(sorted(values))]+=co*sgn
    tetra={ (0,1,2):-1,(0,1,3):1,(0,2,3):-1,(1,2,3):1 }
    d=image[1,2,3]
    assert all(image[t]==d*a for t,a in tetra.items())
    return d
assert degree_on_Z(START)==1
assert degree_on_Z(TRANSPOSED)==-1
signcounts=Counter(degree_on_Z(c) for c in colors)
assert signcounts=={1:9012,-1:9012}
assert all(degree_on_Z(c)==1 for c in C0)
assert all(degree_on_Z(c)==-1 for c in C1)

# The 0/1 bichromatic subgraph is connected, so the global swap is one Kempe switch.
target={i for i in range(12) if START[i] in (0,1)}
reached={next(iter(target))}
Q=deque(reached)
while Q:
    v=Q.popleft()
    for w in N[v] & target:
        if w not in reached:
            reached.add(w);Q.append(w)
assert target==reached and len(target)==8

print('GRAPH 12 vertices, 24 edges; NERVE_FACES (12,42,44,12)')
print('CHAIN 20 oriented triangles; BOUNDARY_ZERO; DEGREE_INITIAL +1, TRANSPOSED -1')
print('COLORINGS_3 0; COLORINGS_4 18024')
print('ONE_VERTEX_COMPONENT_SIZES 9012 9012')
print('DEGREE_SPECTRUM -1:9012 +1:9012')
print('KEMPE_BRIDGE_SEEDS via connected 0/1 bichromatic swap')
print('VERIFY_OK')
