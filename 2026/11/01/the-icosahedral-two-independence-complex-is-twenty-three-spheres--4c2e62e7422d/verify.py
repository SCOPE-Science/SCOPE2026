"""Exact 2-independence and automorphism-character verification for the icosahedral graph.

Run with Python 3.10 or newer: python verify.py
No external packages are required.
"""
from collections import Counter, defaultdict, deque

N = 12
EDGES = [
    (0,1),(0,5),(0,7),(0,8),(0,11),
    (1,2),(1,5),(1,6),(1,8),
    (2,3),(2,6),(2,8),(2,9),
    (3,4),(3,6),(3,9),(3,10),
    (4,5),(4,6),(4,10),(4,11),
    (5,6),(5,11),
    (7,8),(7,9),(7,10),(7,11),
    (8,9),(9,10),(10,11)
]
CW = [
    [1,5,11,7,8], [0,8,2,6,5], [1,8,9,3,6],
    [2,9,10,4,6], [3,10,11,5,6], [4,11,0,1,6],
    [5,1,2,3,4], [11,10,9,8,0], [7,9,2,1,0],
    [8,7,10,3,2], [9,7,11,4,3], [5,4,10,7,0]
]
PIVOTS = [4,8,2,9,11,5,3,6,0,1,7,10]

neighbors = [0] * N
for a,b in EDGES:
    assert a<b and 0 <= a < N and 0 <= b < N
    neighbors[a] |= 1 << b
    neighbors[b] |= 1 << a
assert len(set(EDGES)) == 30
assert all(x.bit_count() == 5 for x in neighbors)
for v in range(N):
    assert set(CW[v]) == {w for w in range(N) if neighbors[v] >> w & 1}
    for j in range(5):
        a,b=CW[v][j],CW[v][(j+1)%5]
        assert neighbors[a] >> b & 1
# A consistent spherical rotation system has opposite boundary orientations
# along the two triangles meeting each graph edge.
for a,b in EDGES:
    i=CW[a].index(b);p=CW[a][(i+1)%5];q=CW[a][(i-1)%5]
    j=CW[b].index(a)
    assert {CW[b][(j+1)%5],CW[b][(j-1)%5]} == {p,q}
    assert CW[b][(j+1)%5] == q

# Identify the twenty coherently oriented triangular faces. Each graph edge
# lies in two triangles; Euler characteristic is that of a sphere.
triangles = {frozenset((v, CW[v][j], CW[v][(j+1)%5]))
             for v in range(N) for j in range(5)}
assert len(triangles) == 20
assert all(len(t) == 3 for t in triangles)
assert all(sum({a,b} <= t for t in triangles) == 2 for a,b in EDGES)
assert N - len(EDGES) + len(triangles) == 2

# A subset induces components of size at most two iff its induced
# maximum degree is at most one. Enumerate all 2-independence faces.
faces = {
    s for s in range(1 << N)
    if all((s & neighbors[v]).bit_count() <= 1
           for v in range(N) if s >> v & 1)
}
assert 0 in faces
hist = Counter(s.bit_count()-1 for s in faces)
assert hist == {-1:1, 0:12, 1:66, 2:140, 3:105}
facets = [s for s in faces if all(s | (1 << v) not in faces
                                    for v in range(N) if not (s >> v & 1))]
assert Counter(s.bit_count()-1 for s in facets) == {3:105}

# Sequential element matching, including the augmented empty face.
# Every vertex-toggle step matches presently unmatched faces differing
# exactly at that vertex. This is the published elementary Morse scheme;
# below we additionally verify the entire resulting directed Hasse graph.
remaining = set(faces)
matching = []
for v in PIVOTS:
    for s in sorted(remaining, key=lambda z:(z.bit_count(),z)):
        if not (s >> v & 1) and s | (1 << v) in remaining and s in remaining:
            t=s | (1 << v)
            matching.append((s,t))
            remaining.remove(s); remaining.remove(t)
assert len(matching)==152
assert Counter(s.bit_count()-1 for s in remaining)=={3:20}
assert len(remaining)==20

# Orient the face-poset Hasse edges down, except paired edges up.
paired=set(matching)
adj={s:[] for s in faces}
indeg={s:0 for s in faces}
incidences=0
for t in faces:
    bits=t
    while bits:
        bit=bits & -bits;bits-=bit
        s=t ^ bit
        assert s in faces
        if (s,t) in paired:
            u,w=s,t
        else:
            u,w=t,s
        adj[u].append(w);indeg[w]+=1
        incidences+=1
assert incidences==984
queue=deque(s for s in faces if indeg[s]==0)
visited=0
while queue:
    s=queue.popleft();visited+=1
    for t in adj[s]:
        indeg[t]-=1
        if indeg[t]==0:queue.append(t)
assert visited==len(faces), 'Morse matching has a directed cycle'

# Independent simplicial mod-2 boundary ranks (not needed for the
# integral homotopy conclusion from acyclic Morse theory).
bydim=defaultdict(list)
for s in sorted(faces):bydim[s.bit_count()-1].append(s)
ranks={}
for d in (1,2,3):
    rowindex={s:i for i,s in enumerate(bydim[d-1])}
    basis={}
    for s in bydim[d]:
        col=0; bits=s
        while bits:
            bit=bits & -bits;bits-=bit
            col ^= 1 << rowindex[s ^ bit]
        while col:
            pivot=col.bit_length()-1
            if pivot in basis:col ^= basis[pivot]
            else:
                basis[pivot]=col
                break
    ranks[d]=len(basis)
assert ranks=={1:11,2:55,3:85}

# Exhaustively enumerate graph automorphisms via adjacency-constrained DFS.
# The mapping order exposes neighbors of vertex zero early for pruning.
assign_order=[0,1,5,11,7,8,6,2,4,10,9,3]
permutation=[-1]*N
used=set()
automorphisms=[]
def search(k):
    if k==N:
        automorphisms.append(tuple(permutation));return
    src=assign_order[k]
    for dst in range(N):
        if dst in used:continue
        if any(bool(neighbors[src] >> u & 1) != bool(neighbors[dst] >> permutation[u] & 1)
               for u in assign_order[:k]):continue
        used.add(dst);permutation[src]=dst
        search(k+1)
        used.remove(dst);permutation[src]=-1
search(0)
assert len(automorphisms)==120
assert len(set(automorphisms))==120
ident=tuple(range(N))

def compose(f,g):
    return tuple(f[g[i]] for i in range(N))

def group_order(g):
    h=ident
    for j in range(1,21):
        h=compose(h,g)
        if h==ident:return j
    raise AssertionError('order greater than twenty')

def orient(g):
    # The ordered links around all vertices give a spherical orientation.
    # An automorphism preserves or reverses this orientation everywhere.
    types=set()
    for v in range(N):
        seq=[g[t] for t in CW[v]]
        target=CW[g[v]]
        rot=any(seq==target[i:]+target[:i] for i in range(5))
        rev=target[::-1]
        ref=any(seq==rev[i:]+rev[:i] for i in range(5))
        assert rot != ref
        types.add(1 if rot else -1)
    assert len(types)==1
    return next(iter(types))

def cycle_type(g):
    seen=set();lengths=[]
    for v in range(N):
        if v in seen:continue
        w=v;k=0
        while w not in seen:
            seen.add(w);k+=1;w=g[w]
        lengths.append(k)
    return tuple(sorted(lengths))

def permutation_sign(seq):
    inversions=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return (-1)**(inversions%2)

def character(g):
    # Oriented fixed simplex contribution in the alternating Lefschetz sum.
    lef=0
    for s in faces:
        if not s:continue
        vertices=[v for v in range(N) if s>>v & 1]
        images=[g[v] for v in vertices]
        if set(images)==set(vertices):
            lef += (-1)**(len(vertices)-1) * permutation_sign(images)
    # Only H_0=Z and H_3=Z^20 survive, so Lef(g)=1-tr(g|H_3).
    return 1-lef

classes=defaultdict(list)
for g in automorphisms:
    classes[(orient(g),group_order(g),cycle_type(g),character(g))].append(g)
assert sorted((t[0],t[1],len(aut)) for t,aut in classes.items()) == [
   (-1,2,1),(-1,2,15),(-1,6,20),(-1,10,24),
   (1,1,1),(1,2,15),(1,3,20),(1,5,24)
]
expected={
 ( 1,1,(1,)*12):20,
 ( 1,2,(2,)*6):4,
 ( 1,3,(3,)*4):-1,
 ( 1,5,(1,1,5,5)):0,
 (-1,2,(2,)*6):10,
 (-1,2,(1,1,1,1,2,2,2,2)):2,
 (-1,6,(6,6)):1,
 (-1,10,(2,10)):0,
}
assert len(classes)==len(expected)
for (ori,ordr,ct,tr),group in classes.items():
    assert expected[(ori,ordr,ct)]==tr

# The unique central involution, denoted z, reverses sphere orientation.
zlist=[g for g in automorphisms if g!=ident and compose(g,g)==ident and
       all(compose(g,h)==compose(h,g) for h in automorphisms)]
assert len(zlist)==1
z=zlist[0]
assert orient(z)==-1 and character(z)==10
for g in automorphisms:
    if orient(g)==1:
        assert orient(compose(z,g))==-1
        # Character pairs give the antipodal eigenspace characters.
        a=character(g);b=character(compose(z,g))
        assert (a+b)%2==0 and (a-b)%2==0
        plus=(a+b)//2;minus=(a-b)//2
        op=group_order(g)
        assert plus=={1:15,2:3,3:0,5:0}[op]
        assert minus=={1:5,2:1,3:-1,5:0}[op]

print('ICOSAHEDRAL_TWO_INDEPENDENCE_EXACT_MORSE_AND_SYMMETRY_OK')
print('faces_including_empty=',len(faces),'f_vector=',[hist[d] for d in range(4)])
print('facets_dimensions=',dict(sorted(Counter(s.bit_count()-1 for s in facets).items())))
print('matched_pairs=',len(matching),'critical_threed_cells=',len(remaining))
print('directed_incidences=',incidences,'acyclic_vertices_visited=',visited)
print('mod2_boundary_ranks=',[ranks[d] for d in (1,2,3)])
print('automorphisms=',len(automorphisms),'central_involution=',z)
print('class_key_orientation_order_cycle_type_trace_count:')
for key,group in sorted(classes.items()):print((key,len(group)))
print('rational H3 as A5 x C2: (+): trivial + 4 + 2*5, (-): 5')
