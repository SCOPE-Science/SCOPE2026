#!/usr/bin/env python3
"""Reproduce a finite simple-homotopy certificate for the 4x4 Sudoku graph."""
from collections import Counter, defaultdict, deque

V = tuple(range(16))

def conflict(i,j):
    r,c = divmod(i,4)
    s,d = divmod(j,4)
    return i != j and (r==s or c==d or (r//2==s//2 and c//2==d//2))

ADJ = [sum(1<<j for j in V if conflict(i,j)) for i in V]
assert [a.bit_count() for a in ADJ] == [7]*16

def bits(x):
    return tuple(i for i in V if x>>i & 1)

def boundary(x):
    return tuple(x^(1<<i) for i in bits(x))

# Increasing integer masks ensure every proper nonempty subface was visited.
FACES = {0}
for x in range(1,1<<16):
    i = (x & -x).bit_length() - 1
    rest = x ^ (1 << i)
    if rest in FACES and not (ADJ[i] & rest):
        FACES.add(x)
assert len(FACES)==161
assert dict(sorted(Counter(x.bit_count() for x in FACES if x).items())) == {1:16,2:64,3:64,4:16}
assert all(x.bit_count()<=4 for x in FACES)
assert len({(i,j) for i in V for j in V if i<j and conflict(i,j)}) == 56

# A codimension-one free pair (S,T) means S lies in exactly one
# remaining simplex T covering S. Every removal is a simplicial collapse.
faces = FACES - {0}
certificate=[]
while True:
    free=[]
    for S in faces:
        up=[S|(1<<i) for i in V if not(S>>i & 1) and S|(1<<i) in faces]
        if len(up)==1:
            free.append((S,up[0]))
    if not free: break
    # First highest-dimensional coface, then least lower-mask, then coface.
    S,T=min(free,key=lambda st:(-st[1].bit_count(),st[0],st[1]))
    assert T.bit_count()==S.bit_count()+1
    assert all(not((S&U)==S and U.bit_count()>S.bit_count() and U!=T) for U in faces)
    faces.remove(S)
    faces.remove(T)
    certificate.append((S,T))

EXPECTED_PAIRS = [
(292,33060), (296,16680), (322,33090), (386,16770),
(532,33300), (536,16920), (577,33345), (641,17025),
(1048,9240), (1064,5160), (1153,9345), (1154,5250),
(2068,10260), (2084,6180), (2113,10305), (2114,6210),
(260,33028), (264,16648), (320,33088), (384,16768),
(516,33284), (520,16904), (576,33344), (640,17024),
(1025,9217), (1026,5122), (1040,9232), (1056,5152),
(2049,10241), (2050,6146), (2064,10256), (2080,6176),
]
assert certificate == EXPECTED_PAIRS

size_counts = dict(sorted(Counter(x.bit_count() for x in faces).items()))
assert size_counts == {1:16,2:48,3:32},size_counts
assert Counter(T.bit_count() for S,T in certificate) == {4:16,3:16}
assert len(certificate)==32
assert set(faces)==set(FACES-{0}).difference({x for pair in certificate for x in pair})

verts={x for x in faces if x.bit_count()==1}
edges={x for x in faces if x.bit_count()==2}
triangles={x for x in faces if x.bit_count()==3}
assert all(e in edges for t in triangles for e in boundary(t))
assert all(v in verts for e in edges for v in boundary(e))

edge_tris={e:tuple(sorted(t for t in triangles if (t&e)==e)) for e in edges}
assert all(len(ts)==2 for ts in edge_tris.values())

def connected(nodes,edges_u_v):
    A={n:set() for n in nodes}
    for u,v in edges_u_v:
        A[u].add(v); A[v].add(u)
    todo=[min(nodes)]; visited={todo[0]}
    while todo:
        for x in A[todo.pop()]:
            if x not in visited:
                visited.add(x);todo.append(x)
    return visited==set(nodes)

assert connected(verts, ((1<<bits(e)[0],1<<bits(e)[1]) for e in edges))
for v in verts:
    link_edges=[t^v for t in triangles if t&v]
    link_vertices={e^v for e in edges if e&v}
    assert all((t & v)==0 for t in link_edges)
    assert all(sum(1 for e in link_edges if e&u)==2 for u in link_vertices)
    assert connected(link_vertices, ((1<<bits(e)[0],1<<bits(e)[1]) for e in link_edges))

# Global coherent orientation: every edge must cancel in a fundamental 2-cycle.
def signed_incidence(t,e):
    assert e in boundary(t)
    return (-1)**next(k for k,i in enumerate(bits(t)) if (t^(1<<i))==e)

orientation={min(triangles):1}
queue=deque(orientation)
triangle_edges={t:boundary(t) for t in triangles}
while queue:
    t=queue.popleft()
    for e in triangle_edges[t]:
        a,b=edge_tris[e];other=b if a==t else a
        val=-orientation[t]*signed_incidence(t,e)*signed_incidence(other,e)
        if other in orientation:
            assert orientation[other]==val
        else:
            orientation[other]=val
            queue.append(other)
assert set(orientation)==triangles
assert all(sum(orientation[t]*signed_incidence(t,e) for t in edge_tris[e])==0 for e in edges)
assert len(verts)-len(edges)+len(triangles)==0

print('Sudoku graph: 16 vertices, 56 conflict edges, degree 7')
print('Independence complex faces by dimension:',{k-1:v for k,v in sorted(Counter(x.bit_count() for x in FACES if x).items())})
print('Elementary collapse pairs:',Counter((T.bit_count()-1) for S,T in certificate))
print('Final closed connected orientable 2-manifold: (V,E,F)=(16,48,32), Euler=0')
print('Every edge has 2 triangles; every vertex link is one circle; orientations cancel')
print('Homotopy type: torus S^1 x S^1; integral homology H1=Z^2, H2=Z')
print('VERIFY_OK')
