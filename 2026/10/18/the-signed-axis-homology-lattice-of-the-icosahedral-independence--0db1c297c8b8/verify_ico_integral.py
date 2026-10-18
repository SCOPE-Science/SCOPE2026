#!/usr/bin/env python3
"""Self-contained finite checks for a twelve-vertex graph independence-complex theorem.
Only Python's standard library is required.
"""
from collections import Counter, deque
from itertools import combinations

N = 12
E = set()
def edge(i,j):
    assert i != j
    E.add(tuple(sorted((i,j))))
for j in range(5):
    edge(10,j)
    edge(11,5+j)
    edge(j,(j+1)%5)
    edge(5+j,5+(j+1)%5)
    edge(j,5+j)
    edge(j,5+(j-1)%5)
assert len(E)==30
neighbors=[set() for _ in range(N)]
for a,b in E:neighbors[a].add(b);neighbors[b].add(a)
assert all(len(n)==5 for n in neighbors)

def dist(v):
    out={v:0};q=deque([v])
    while q:
        a=q.popleft()
        for b in neighbors[a]:
            if b not in out:
                out[b]=out[a]+1;q.append(b)
    return out
D=[dist(v) for v in range(N)]
assert all(Counter(row.values())==Counter({0:1,1:5,2:5,3:1}) for row in D)
op=tuple(next(w for w in range(N) if D[v][w]==3) for v in range(N))
assert all(op[op[v]]==v and op[v]!=v for v in range(N))
axis_edges=sorted({tuple(sorted((v,op[v]))) for v in range(N)})
assert len(axis_edges)==6
assert all(D[op[x]][y]==3-D[x][y] for x in range(N) for y in range(N))
E2={tuple(sorted((a,b))) for a,b in combinations(range(N),2) if D[a][b]==2}
assert len(E2)==30
# An explicit graph isomorphism: the original icosahedral graph maps to its distance-two graph.
phi=(0,2,4,1,3,8,5,7,9,6,11,10)
assert len(set(phi))==N
assert {tuple(sorted((phi[a],phi[b]))) for a,b in E}==E2
triangles=sorted(t for t in combinations(range(N),3)
                 if all(tuple(sorted(e)) in E2 for e in combinations(t,2)))
assert len(triangles)==20
assert all(sum(set(e).issubset(t) for t in triangles)==2 for e in E2)
K_edges=E2 | set(axis_edges)
assert len(K_edges)==36
assert all(not set(a).issubset(t) for a in axis_edges for t in triangles)
faces=[(v,) for v in range(N)]+sorted(K_edges)+triangles
assert Counter(map(len,faces))=={1:12,2:36,3:20}

# Propagate coherent orientations across the closed triangulated surface.
tindex={t:i for i,t in enumerate(triangles)}
edge_to_tri={e:[] for e in E2}
for i,t in enumerate(triangles):
    for j in range(3):
        e=tuple(sorted(t[:j]+t[j+1:]))
        # (Sorted triangle.) Oriented boundary coefficient of the omitted vertex.
        edge_to_tri[e].append((i,(-1)**j))
assert all(len(z)==2 for z in edge_to_tri.values())
coeff=[None]*20;coeff[0]=1;q=deque([0])
while q:
    i=q.popleft();t=triangles[i]
    for j in range(3):
        e=tuple(sorted(t[:j]+t[j+1:]));incident=edge_to_tri[e]
        (i1,s1),(i2,s2)=incident
        oi,other_sign=(i2,s2) if i1==i else (i1,s1)
        current_sign=s1 if i1==i else s2
        assert current_sign==(-1)**j
        # For coherent orientation the two incident boundary terms must cancel.
        value=-coeff[i]*current_sign*other_sign
        if coeff[oi] is None:coeff[oi]=value;q.append(oi)
        else:assert coeff[oi]==value
assert all(c in (-1,1) for c in coeff)

def inversion_sign(word):
    return -1 if sum(word[i]>word[j] for i in range(len(word)) for j in range(i+1,len(word)))%2 else 1

def action_on_surface(g):
    out=[0]*20
    for i,t in enumerate(triangles):
        raw=tuple(g[k] for k in t)
        j=tindex[tuple(sorted(raw))]
        out[j]+=coeff[i]*inversion_sign(raw)
    scalar=out[0]*coeff[0]
    assert scalar in (-1,1)
    assert out==[scalar*x for x in coeff]
    return scalar

# Enumerate every graph automorphism, matching adjacency AND nonadjacency.
# Choose each next vertex with most already-assigned neighbors to prune early.
order=(10,0,1,4,2,3,5,6,7,8,9,11)
assign={};used=set();automorphisms=[]
def extend(k):
    if k==N:
        automorphisms.append(tuple(assign[i] for i in range(N)))
        return
    v=order[k]
    for w in range(N):
        if w in used:continue
        if any(((u in neighbors[v]) != (assign[u] in neighbors[w])) for u in assign):continue
        assign[v]=w;used.add(w);extend(k+1);used.remove(w);del assign[v]
extend(0)
assert len(set(automorphisms))==120
G=set(automorphisms)
ident=tuple(range(N))
def compose(p,q):return tuple(p[q[i]] for i in range(N))
def permutation_order(p):
    t=ident;count=0
    while True:
        t=compose(p,t);count+=1
        if t==ident:return count
assert ident in G
assert all(compose(g,tuple(op))==compose(tuple(op),g) for g in G)
rotations5=[g for g in G if permutation_order(g)==5]
assert len(rotations5)==24
rotation_group={ident};q=deque([ident])
while q:
    h=q.popleft()
    for gen in rotations5:
        t=compose(h,gen)
        if t not in rotation_group:
            rotation_group.add(t);q.append(t)
assert len(rotation_group)==60
axis_stabilizer=[g for g in rotation_group if {g[10],g[11]}=={10,11}]
assert len(axis_stabilizer)==10
assert sum((g[10],g[11])==(10,11) for g in axis_stabilizer)==5
assert sum((g[10],g[11])==(11,10) for g in axis_stabilizer)==5
assert G==rotation_group | {compose(tuple(op),g) for g in rotation_group}

def signed_axes_trace(g):
    trace=0
    for u,v in axis_edges:
        a,b=g[u],g[v]
        if tuple(sorted((a,b)))==(u,v):
            trace+=1 if (a,b)==(u,v) else -1
    return trace

rot_classes=Counter();coset_classes=Counter();character_sq=0
for g in G:
    h1=signed_axes_trace(g)
    h2=action_on_surface(g)
    isrotation=g in rotation_group
    expected_h2=1 if isrotation else -1
    assert h2==expected_h2
    if isrotation:
        o=permutation_order(g)
        assert h1=={1:6,2:-2,3:0,5:1}[o]
        rot_classes[(o,h1)]+=1
    else:
        r=compose(tuple(op),g)
        o=permutation_order(r)
        assert h1=={1:-6,2:2,3:0,5:-1}[o]
        coset_classes[(o,h1)]+=1
    character_sq+=h1*h1
assert rot_classes=={(1,6):1,(2,-2):15,(3,0):20,(5,1):24}
assert coset_classes=={(1,-6):1,(2,2):15,(3,0):20,(5,-1):24}
assert character_sq==240
assert sum(n*t for (o,t),n in rot_classes.items())==0
assert sum(n*t for (o,t),n in coset_classes.items())==0
print('ICOSAHEDRAL_SIGNED_HOMOLOGY_PASS')
print('face vector (12,36,20); 6 antipodal edges; 20 coherent sphere triangles')
print('120 full automorphisms; 60 rotations; character inner product 2')
print('rotation character',sorted(rot_classes.items()))
print('inverted rotation character',sorted(coset_classes.items()))
