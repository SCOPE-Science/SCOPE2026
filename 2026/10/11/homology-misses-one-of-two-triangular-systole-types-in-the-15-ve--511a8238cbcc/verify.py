#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict

FACETS = [(1, 2, 3, 4),
 (1, 2, 3, 5),
 (1, 2, 4, 6),
 (1, 2, 5, 6),
 (1, 3, 4, 7),
 (1, 3, 5, 7),
 (1, 4, 6, 8),
 (1, 4, 7, 8),
 (1, 5, 6, 9),
 (1, 5, 7, 10),
 (1, 5, 9, 10),
 (1, 6, 8, 11),
 (1, 6, 9, 11),
 (1, 7, 8, 12),
 (1, 7, 10, 13),
 (1, 7, 12, 13),
 (1, 8, 11, 12),
 (1, 9, 10, 13),
 (1, 9, 11, 14),
 (1, 9, 13, 14),
 (1, 11, 12, 14),
 (1, 12, 13, 14),
 (2, 3, 4, 15),
 (2, 3, 5, 8),
 (2, 3, 8, 15),
 (2, 4, 6, 12),
 (2, 4, 12, 15),
 (2, 5, 6, 13),
 (2, 5, 8, 11),
 (2, 5, 11, 13),
 (2, 6, 12, 13),
 (2, 7, 10, 13),
 (2, 7, 10, 14),
 (2, 7, 12, 13),
 (2, 7, 12, 15),
 (2, 7, 14, 15),
 (2, 8, 10, 11),
 (2, 8, 10, 14),
 (2, 8, 14, 15),
 (2, 10, 11, 13),
 (3, 4, 7, 11),
 (3, 4, 11, 13),
 (3, 4, 13, 15),
 (3, 5, 7, 14),
 (3, 5, 8, 12),
 (3, 5, 12, 14),
 (3, 6, 7, 11),
 (3, 6, 7, 14),
 (3, 6, 10, 11),
 (3, 6, 10, 12),
 (3, 6, 12, 14),
 (3, 8, 9, 12),
 (3, 8, 9, 13),
 (3, 8, 13, 15),
 (3, 9, 10, 12),
 (3, 9, 10, 13),
 (3, 10, 11, 13),
 (4, 5, 10, 14),
 (4, 5, 10, 15),
 (4, 5, 11, 13),
 (4, 5, 11, 14),
 (4, 5, 13, 15),
 (4, 6, 8, 10),
 (4, 6, 10, 12),
 (4, 7, 8, 9),
 (4, 7, 9, 11),
 (4, 8, 9, 14),
 (4, 8, 10, 14),
 (4, 9, 11, 14),
 (4, 10, 12, 15),
 (5, 6, 9, 15),
 (5, 6, 13, 15),
 (5, 7, 10, 14),
 (5, 8, 11, 12),
 (5, 9, 10, 15),
 (5, 11, 12, 14),
 (6, 7, 9, 11),
 (6, 7, 9, 15),
 (6, 7, 14, 15),
 (6, 8, 10, 11),
 (6, 12, 13, 14),
 (6, 13, 14, 15),
 (7, 8, 9, 12),
 (7, 9, 12, 15),
 (8, 9, 13, 14),
 (8, 13, 14, 15),
 (9, 10, 12, 15)]
TREE = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (2, 15)]
EDGE_WORDS = {(2, 3): [],
 (2, 4): [],
 (2, 5): [],
 (2, 6): [],
 (2, 7): [-2, -2, -1, 2],
 (2, 8): [-2, 1, 2],
 (2, 10): [-2, -2, -1, 2],
 (2, 11): [-2, 1, 2],
 (2, 12): [-2, -2, -1, 2],
 (2, 13): [-2, -2, -1, 2],
 (2, 14): [-2],
 (3, 4): [],
 (3, 5): [],
 (3, 6): [-2, -1],
 (3, 7): [],
 (3, 8): [-2, 1, 2],
 (3, 9): [-2],
 (3, 10): [-2],
 (3, 11): [-2, -1],
 (3, 12): [-2, 1, 2],
 (3, 13): [-2],
 (3, 14): [-2, 1, 2],
 (3, 15): [],
 (4, 5): [1],
 (4, 6): [],
 (4, 7): [],
 (4, 8): [],
 (4, 9): [-2, -1],
 (4, 10): [1],
 (4, 11): [-2, -1],
 (4, 12): [-2, -2, -1, 2],
 (4, 13): [-2],
 (4, 14): [-2, -1],
 (4, 15): [],
 (5, 6): [],
 (5, 7): [],
 (5, 8): [-2, 1, 2],
 (5, 9): [],
 (5, 10): [],
 (5, 11): [-2, 1, 2],
 (5, 12): [-2, 1, 2],
 (5, 13): [-2, -2, -1, 2],
 (5, 14): [-2, 1, 2],
 (5, 15): [-1],
 (6, 7): [1, 2],
 (6, 8): [],
 (6, 9): [],
 (6, 10): [1],
 (6, 11): [],
 (6, 12): [-2, -2, -1, 2],
 (6, 13): [-2, -2, -1, 2],
 (6, 14): [-2, -2, -1, 2],
 (6, 15): [-1],
 (7, 8): [],
 (7, 9): [-2, -1],
 (7, 10): [],
 (7, 11): [-2, -1],
 (7, 12): [],
 (7, 13): [],
 (7, 14): [-2, 1, 2],
 (7, 15): [-2, 1, 2, 2],
 (8, 9): [-2, -1],
 (8, 10): [1],
 (8, 11): [],
 (8, 12): [],
 (8, 13): [-2, -1],
 (8, 14): [-2, -1],
 (8, 15): [-2, -1, 2],
 (9, 10): [],
 (9, 11): [],
 (9, 12): [1, 2],
 (9, 13): [],
 (9, 14): [],
 (9, 15): [-1],
 (10, 11): [-1],
 (10, 12): [1, 2],
 (10, 13): [],
 (10, 14): [-2, 1, 2],
 (10, 15): [-1],
 (11, 12): [],
 (11, 13): [1],
 (11, 14): [],
 (12, 13): [],
 (12, 14): [],
 (12, 15): [-2, 1, 2, 2],
 (13, 14): [],
 (13, 15): [2],
 (14, 15): [2]}
A = (1, 5, 0, 11, 14, 13, 16, 18, 2, 20, 22, 15, 3, 8, 12, 4, 19, 6, 17, 7, 23, 9, 21, 10)
B = (3, 6, 9, 13, 0, 10, 8, 1, 7, 5, 2, 21, 18, 4, 23, 16, 12, 20, 15, 22, 19, 14, 17, 11)
N = 24
ID = tuple(range(N))

def comp(p,q):
    # Group product matching right-action array convention: (p*q)(i)=q(p(i)).
    return tuple(q[p[i]] for i in range(N))

def inv(p):
    r=[0]*N
    for i,j in enumerate(p):
        r[j]=i
    return tuple(r)

def ppow(p,n):
    if n < 0:
        return ppow(inv(p), -n)
    r=ID
    b=p
    while n:
        if n&1:
            r=comp(r,b)
        b=comp(b,b); n//=2
    return r

def order(p):
    r=ID
    for n in range(1, 49):
        r=comp(r,p)
        if r==ID:
            return n
    raise AssertionError("order > 48")

AINV, BINV = inv(A), inv(B)
GEN={1:A, -1:AINV, 2:B, -2:BINV}

def word_eval(w):
    r=ID
    for x in w:
        r=comp(r, GEN[x])
    return r

def word_inv(w):
    return [-x for x in reversed(w)]

TREE=set(map(tuple,TREE))

def edge_word(u,v):
    if u==v:
        return []
    e=tuple(sorted((u,v)))
    if e in TREE:
        return []
    w=EDGE_WORDS[e]
    return w if u<v else word_inv(w)

def tri_word(t):
    a,b,c=sorted(t)
    return edge_word(a,b)+edge_word(b,c)+edge_word(c,a)

def closure(gens):
    S={ID}
    stack=[ID]
    gs=list(gens)+[inv(g) for g in gens]
    while stack:
        x=stack.pop()
        for g in gs:
            y=comp(x,g)
            if y not in S:
                S.add(y); stack.append(y)
    return S

G=closure([A,B])
assert len(G)==24
assert order(A)==6 and order(B)==4

# Reconstruct the exact simplicial complex.
faces_by_dim=[set() for _ in range(4)]
for tet in FACETS:
    assert len(set(tet))==4
    for k in range(1,5):
        for s in combinations(tet,k):
            faces_by_dim[k-1].add(tuple(sorted(s)))
f=tuple(len(s) for s in faces_by_dim)
assert f==(15,102,174,87)
V=sorted(v[0] for v in faces_by_dim[0])
E=faces_by_dim[1]
F=faces_by_dim[2]

# The edge labels define a homomorphism from the standard spanning-tree
# presentation of pi_1(K) because every triangular 2-face relator maps to 1.
assert set(EDGE_WORDS)==set(E)-TREE
assert EDGE_WORDS[(11,13)]==[1]
assert EDGE_WORDS[(13,15)]==[2]
for tri in F:
    assert word_eval(tri_word(tri))==ID

# Enumerate every simple 3-edge cycle. Facial triangles are null; the
# remaining clique triples are the candidate shortest noncontractible cycles.
cliques=[]
empty=[]
for t in combinations(V,3):
    if all(tuple(sorted(e)) in E for e in combinations(t,2)):
        cliques.append(t)
        if t not in F:
            empty.append(t)
assert len(cliques)==417
assert len(empty)==243

# Exact group element represented by each empty-triangle boundary.
elt_for={t:word_eval(tri_word(t)) for t in empty}
assert all(g!=ID for g in elt_for.values())
ord_counts=Counter(order(g) for g in elt_for.values())
assert ord_counts==Counter({6:215,4:28})

# Compute conjugacy classes and unoriented free-homotopy classes
# (conjugacy classes modulo inversion).
def conjugacy_class(g):
    return frozenset(comp(comp(inv(h),g),h) for h in G)

classes={conjugacy_class(g) for g in G}
class_data=sorted((len(C), order(next(iter(C)))) for C in classes)
assert class_data==[(1,1),(1,2),(4,3),(4,3),(4,6),(4,6),(6,4)]

used_classes=Counter()
for g in elt_for.values():
    C=conjugacy_class(g)
    used_classes[C]+=1
assert sorted((order(next(iter(C))),n,len(C)) for C,n in used_classes.items())==[(4,28,6),(6,105,4),(6,110,4)]
order6_classes=[C for C in used_classes if order(next(iter(C)))==6]
assert len(order6_classes)==2
assert frozenset(inv(g) for g in order6_classes[0])==order6_classes[1]
order4_class=[C for C in used_classes if order(next(iter(C)))==4][0]
assert frozenset(inv(g) for g in order4_class)==order4_class

# Derived subgroup of the 24-element image. Because the source identifies
# pi_1(K) with the binary tetrahedral group of order 24 and the displayed
# representation is surjective onto a 24-element group, it is faithful.
comm_gens=[]
for x in G:
    for y in G:
        comm_gens.append(comp(comp(comp(inv(x),inv(y)),x),y))
D=closure(comm_gens)
assert len(D)==8
assert Counter(order(x) for x in D)==Counter({4:6,1:1,2:1})

nullhom=0
nonzerohom=0
joint=Counter()
for t,g in elt_for.items():
    inD=g in D
    if inD: nullhom+=1
    else: nonzerohom+=1
    joint[(order(g),inD)]+=1
assert nullhom==28 and nonzerohom==215
assert joint==Counter({(6,False):215,(4,True):28})

print("VERIFY_OK")
print("f=15,102,174,87")
print("simple_3cycles=417 facial=174 empty=243")
print("fundamental_group_image_order=24")
print("empty_triangle_orders=6:215,4:28")
print("empty_triangle_homology=nonzero:215,null:28")
print("used_conjugacy_classes=order6:110+105,order4:28")
print("unoriented_free_homotopy_types=2")
print("derived_subgroup_order=8 element_orders=1:1,2:1,4:6")
print("simple_noncontractible_1_systole_edges=3 minimizers=243")
