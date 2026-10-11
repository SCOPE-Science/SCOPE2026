#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter

# Exact arithmetic in Q(phi), phi^2 = phi + 1.
# A pair (a,b) means a + b*phi.
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x; c,d=y
    return (a*c+b*d, a*d+b*c+b*d)
def sq(x): return mul(x,x)
def sign(x):
    # 2(a+b*phi) = (2a+b) + b*sqrt(5).
    a,b=x; p=2*a+b; q=b
    if q==0: return (p>0)-(p<0)
    if p==0: return (q>0)-(q<0)
    if p>0 and q>0: return 1
    if p<0 and q<0: return -1
    lhs=p*p; rhs=5*q*q
    if lhs==rhs: return 0
    if p>0: return 1 if lhs>rhs else -1
    return -1 if lhs>rhs else 1

def dist2(v,w):
    out=(0,0)
    for x,y in zip(v,w): out=add(out,sq(sub(x,y)))
    return out

def dot_int(n,v):
    out=(0,0)
    for k,x in zip(n,v): out=add(out,(k*x[0],k*x[1]))
    return out

Z=(0,0); O=(1,0); M=(-1,0); P=(0,1); J=(-1,1) # J = 1/phi
ico=[
 (Z,M,neg(P)),(Z,M,P),(Z,O,neg(P)),(Z,O,P),
 (M,neg(P),Z),(M,P,Z),(O,neg(P),Z),(O,P,Z),
 (neg(P),Z,M),(neg(P),Z,O),(P,Z,M),(P,Z,O)
]
dod=[
 (M,M,M),(M,M,O),(M,O,M),(M,O,O),(O,M,M),(O,M,O),(O,O,M),(O,O,O),
 (Z,neg(J),neg(P)),(Z,neg(J),P),(Z,J,neg(P)),(Z,J,P),
 (neg(J),neg(P),Z),(neg(J),P,Z),(J,neg(P),Z),(J,P,Z),
 (neg(P),Z,neg(J)),(neg(P),Z,J),(P,Z,neg(J)),(P,Z,J)
]

ico_faces=[
 (0,2,8),(0,2,10),(0,4,6),(0,4,8),(0,6,10),
 (1,3,9),(1,3,11),(1,4,6),(1,4,9),(1,6,11),
 (2,5,7),(2,5,8),(2,7,10),(3,5,7),(3,5,9),
 (3,7,11),(4,8,9),(5,8,9),(6,10,11),(7,10,11)
]
dod_faces=[
 (0,1,12,16,17),(0,2,8,10,16),(0,4,8,12,14),
 (1,3,9,11,17),(1,5,9,12,14),(2,3,13,16,17),
 (2,6,10,13,15),(3,7,11,13,15),(4,5,14,18,19),
 (4,6,8,10,18),(5,7,9,11,19),(6,7,15,18,19)
]
ico_pairs=[(0,3),(1,2),(4,7),(5,6),(8,11),(9,10)]
dod_pairs=[(0,7),(1,6),(2,5),(3,4),(8,11),(9,10),(12,15),(13,14),(16,19),(17,18)]

def edge_graph(V, edge_sq):
    adj=[set() for _ in V]
    for i,j in combinations(range(len(V)),2):
        d=dist2(V[i],V[j])
        assert sign(sub(d,edge_sq))>=0
        if d==edge_sq:
            adj[i].add(j); adj[j].add(i)
    return adj

ico_adj=edge_graph(ico,(4,0))
dod_adj=edge_graph(dod,(8,-4))
assert all(len(a)==5 for a in ico_adj)
assert all(len(a)==3 for a in dod_adj)

triangles=set()
for c in combinations(range(12),3):
    if all(j in ico_adj[i] for i,j in combinations(c,2)):
        triangles.add(c)
assert triangles==set(ico_faces)

cycles=set()
def canon(c):
    c=list(c); z=[]
    for seq in (c,list(reversed(c))):
        for k in range(5): z.append(tuple(seq[k:]+seq[:k]))
    return min(z)
def walk(start,path):
    if len(path)==5:
        if start in dod_adj[path[-1]]: cycles.add(canon(path))
        return
    for nb in dod_adj[path[-1]]:
        if nb not in path: walk(start,path+[nb])
for s in range(20): walk(s,[s])
assert {tuple(sorted(c)) for c in cycles}==set(dod_faces)

def transversal_face_sets(pairs,faces):
    out=[]
    for bits in product((0,1),repeat=len(pairs)):
        side={pairs[i][bits[i]] for i in range(len(pairs))}
        out.append(tuple(j for j,f in enumerate(faces) if set(f)<=side))
    return out

TI=transversal_face_sets(ico_pairs,ico_faces)
TD=transversal_face_sets(dod_pairs,dod_faces)
assert Counter(map(len,TI))==Counter({4:20,1:20,0:12,5:12})
assert Counter(map(len,TD))==Counter({0:740,1:204,2:60,3:20})
assert max(map(len,TI))==5
assert max(map(len,TD))==3

max5=list({s for s in TI if len(s)==5})
assert len(max5)==12
U=set(range(20))
assert not any(set().union(*(set(max5[i]) for i in c))==U
               for c in combinations(range(12),4))

def contained_faces(V,faces,n):
    sig=[sign(dot_int(n,v)) for v in V]
    assert all(s!=0 for s in sig)
    return tuple(i for i,f in enumerate(faces) if all(sig[j]>0 for j in f))

# Five positive halfspaces of the dual icosahedron cover all 20 facets.
d_normals=[(-5,-5,-5),(-5,-5,-3),(-5,4,-2),(1,0,-1),(1,0,2)]
d_sets=[contained_faces(ico,ico_faces,n) for n in d_normals]
assert [len(s) for s in d_sets]==[4,5,5,5,4]
assert set().union(*(set(s) for s in d_sets))==set(range(20))

# A consistency certificate for the known ordinary icosahedral cover.
i_normals=[(-5,-5,-5),(-5,2,4),(1,-2,2),(1,1,-1)]
i_sets=[contained_faces(dod,dod_faces,n) for n in i_normals]
assert [len(s) for s in i_sets]==[3,3,3,3]
assert set().union(*(set(s) for s in i_sets))==set(range(12))

print('VERIFY_OK')
print('icosa_transversals = 64')
print('icosa_facet_count_distribution =', dict(sorted(Counter(map(len,TI)).items())))
print('dodeca_transversals = 1024')
print('dodeca_facet_count_distribution =', dict(sorted(Counter(map(len,TD)).items())))
print('dodeca_four_maxset_quadruples_checked =', len(list(combinations(range(12),4))))
print('dodeca_five_halfspace_cover =', d_sets)
print('icosa_four_halfspace_cover =', i_sets)
