from itertools import combinations
from collections import Counter

FACETS = [(1, 2, 4, 6, 9), (1, 2, 4, 6, 11), (1, 2, 4, 7, 10), (1, 2, 4, 7, 11), (1, 2, 4, 9, 10), (1, 2, 5, 7, 8), (1, 2, 5, 7, 11), (1, 2, 5, 8, 10), (1, 2, 5, 9, 10), (1, 2, 5, 9, 11), (1, 2, 6, 9, 11), (1, 2, 7, 8, 10), (1, 3, 4, 6, 8), (1, 3, 4, 6, 9), (1, 3, 4, 7, 9), (1, 3, 4, 7, 11), (1, 3, 4, 8, 11), (1, 3, 5, 6, 9), (1, 3, 5, 6, 10), (1, 3, 5, 9, 10), (1, 3, 6, 8, 10), (1, 3, 7, 8, 10), (1, 3, 7, 8, 11), (1, 3, 7, 9, 10), (1, 4, 6, 8, 11), (1, 4, 7, 9, 10), (1, 5, 6, 8, 10), (1, 5, 6, 8, 11), (1, 5, 6, 9, 11), (1, 5, 7, 8, 11), (2, 4, 6, 8, 10), (2, 4, 6, 8, 11), (2, 4, 6, 9, 10), (2, 4, 7, 8, 10), (2, 4, 7, 8, 12), (2, 4, 7, 11, 12), (2, 4, 8, 11, 12), (2, 5, 6, 8, 10), (2, 5, 6, 8, 12), (2, 5, 6, 10, 12), (2, 5, 7, 8, 12), (2, 5, 7, 9, 11), (2, 5, 7, 9, 12), (2, 5, 9, 10, 12), (2, 6, 8, 11, 12), (2, 6, 9, 10, 12), (2, 6, 9, 11, 12), (2, 7, 9, 11, 12), (3, 4, 6, 8, 10), (3, 4, 6, 9, 12), (3, 4, 6, 10, 12), (3, 4, 7, 9, 11), (3, 4, 8, 10, 12), (3, 4, 8, 11, 12), (3, 4, 9, 11, 12), (3, 5, 6, 9, 11), (3, 5, 6, 10, 12), (3, 5, 6, 11, 12), (3, 5, 7, 8, 11), (3, 5, 7, 8, 12), (3, 5, 7, 9, 10), (3, 5, 7, 9, 11), (3, 5, 7, 10, 12), (3, 5, 8, 11, 12), (3, 6, 9, 11, 12), (3, 7, 8, 10, 12), (4, 6, 9, 10, 12), (4, 7, 8, 10, 12), (4, 7, 9, 10, 12), (4, 7, 9, 11, 12), (5, 6, 8, 11, 12), (5, 7, 9, 10, 12)]
COCHAIN_A = {(2, 4, 8): 1, (2, 5, 6): -1, (2, 6, 8): 1, (2, 6, 10): 1, (2, 8, 11): -1, (3, 4, 10): -1, (3, 5, 12): 1, (3, 7, 12): 1, (3, 8, 12): 1, (3, 10, 12): 1, (4, 6, 10): 1, (4, 7, 8): -1, (4, 8, 10): 1, (4, 8, 12): 1, (5, 6, 12): -1, (5, 11, 12): -1, (6, 8, 12): 1, (6, 9, 10): -1, (6, 10, 12): 1, (8, 11, 12): -1}
COCHAIN_B = {(2, 7, 9): 1, (3, 5, 7): 1, (3, 5, 8): 1, (3, 5, 11): 1, (3, 5, 12): 1, (3, 6, 11): 1, (3, 6, 12): 1, (3, 9, 11): 1, (3, 9, 12): 1, (3, 10, 12): 1, (4, 6, 12): 1, (4, 9, 11): 1, (4, 9, 12): 1, (4, 10, 12): 1, (5, 7, 9): 1, (5, 7, 10): 1, (7, 9, 11): 1, (7, 9, 12): 1, (7, 10, 12): 1, (8, 10, 12): 1}
GENS = [(2, 4, 5, 10, 11, 9, 8, 12, 1, 7, 6, 3), (2, 7, 6, 12, 1, 9, 8, 10, 11, 4, 5, 3)]

FACETS = {tuple(sorted(x)) for x in FACETS}
faces = {k:set() for k in range(1,6)}
for f in FACETS:
    for k in range(1,6):
        faces[k].update(combinations(f,k))
assert tuple(len(faces[k]) for k in range(1,6)) == (12,60,160,180,72)
tris=faces[3]; tets=faces[4]
assert set(COCHAIN_A) <= tris and set(COCHAIN_B) <= tris

def val(c,t): return c.get(tuple(t),0)
def boundary_eval(c,s):
    s=tuple(sorted(s))
    return sum(((-1)**i)*val(c,s[:i]+s[i+1:]) for i in range(len(s)))
# The two displayed integer 2-cochains are cocycles: they vanish on every tetrahedral boundary.
for tet in tets:
    assert boundary_eval(COCHAIN_A,tet)==0
    assert boundary_eval(COCHAIN_B,tet)==0

missing=[]; spectrum=Counter()
for s in combinations(range(1,13),4):
    if all(t in tris for t in combinations(s,3)) and s not in tets:
        q=(boundary_eval(COCHAIN_A,s),boundary_eval(COCHAIN_B,s))
        assert q in {(1,0),(-1,0),(0,1),(0,-1)}
        missing.append(s); spectrum[q]+=1
assert len(missing)==60
assert spectrum==Counter({(0,1):25,(1,0):15,(-1,0):15,(0,-1):5})
assert spectrum[(1,0)]+spectrum[(-1,0)]==30
assert spectrum[(0,1)]+spectrum[(0,-1)]==30

# No nonzero 2-cycle can use fewer than four vertices. On four vertices the only possible
# nonzero integral 2-cycle is a multiple of the oriented boundary of the tetrahedron;
# hence the above exhaustive four-set sweep is the complete minimum-support layer.
for n in (1,2,3):
    for s in combinations(range(1,13),n):
        # There cannot be four distinct triangular faces on fewer than four vertices.
        assert len([t for t in tris if set(t)<=set(s)]) < 4

# Verify an explicit 240-element simplicial symmetry group and transitivity on the 60 supports.
idp=tuple(range(1,13))
def comp(p,q): return tuple(p[q[i]-1] for i in range(12))
def closure(gens):
    S={idp}; todo=[idp]
    while todo:
        a=todo.pop()
        for g in gens:
            b=comp(g,a)
            if b not in S: S.add(b); todo.append(b)
    return S
G=closure(GENS)
assert len(G)==240
for p in G:
    image={tuple(sorted(p[v-1] for v in f)) for f in FACETS}
    assert image==FACETS
mset=set(missing); rep=missing[0]
orb={tuple(sorted(p[v-1] for v in rep)) for p in G}
assert orb==mset

def order(p):
    a=idp
    for k in range(1,100):
        a=comp(p,a)
        if a==idp:return k
    raise AssertionError
assert order(GENS[0])==12
print("VERIFY_OK f=12,60,160,180,72 missing4=60 class_supports=30,30 cocycles=2 symmetry_group=240 support_orbit=60")
