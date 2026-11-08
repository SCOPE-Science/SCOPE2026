"""Exact finite checks for the 24-cell Euclidean Rips collapse.

Run with Python 3: python verify.py
The coordinate and collapse data are exact integers.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json


def roots():
    return sorted({tuple(s if k == i else t if k == j else 0 for k in range(4))
                   for i, j in combinations(range(4), 2)
                   for s, t in product((-1, 1), repeat=2)})

V = roots()
assert len(V) == 24

def sq(i, j):
    return sum((V[i][k] - V[j][k]) ** 2 for k in range(4))


def cliques(bound):
    """Enumerate all nonempty cliques using increasing vertex indices."""
    adj = {(i, j) for i in range(24) for j in range(i+1,24) if sq(i, j) <= bound}
    faces = {(i,) for i in range(24)}
    layer = [(i,) for i in range(24)]
    while layer:
        nxt = []
        for face in layer:
            for j in range(face[-1]+1, 24):
                if all((i, j) in adj for i in face):
                    nxt.append(face+(j,))
        faces.update(nxt)
        layer = nxt
    return faces


def fvector(faces):
    c = Counter(len(x)-1 for x in faces)
    return tuple(c[i] for i in range(max(c)+1))


def check_first_stage(F1):
    assert fvector(F1) == (24, 96, 96)
    # Eight coordinate-normal octahedra and sixteen half-diagonal octahedra.
    facet_vertices = []
    for k in range(4):
        for s in (-1, 1):
            facet_vertices.append(frozenset(i for i,v in enumerate(V) if s*v[k] == 1))
    for signs in product((-1,1), repeat=4):
        facet_vertices.append(frozenset(i for i,v in enumerate(V)
                                         if sum(signs[k]*v[k] for k in range(4)) == 2))
    assert len(set(facet_vertices)) == 24
    triangles = {f for f in F1 if len(f)==3}
    coverage = Counter()
    for cell in facet_vertices:
        assert len(cell)==6
        edges = [p for p in combinations(sorted(cell),2) if sq(*p)==2]
        tri = [t for t in combinations(sorted(cell),3)
               if all(sq(i,j)==2 for i,j in combinations(t,2))]
        assert len(edges)==12 and len(tri)==8
        for t in tri:coverage[t]+=1
    assert set(coverage) == triangles
    assert set(coverage.values())=={2}
    print('scale sqrt(2):',fvector(F1),'24 octahedral facets; each of 96 triangles occurs twice')


def check_collapse(F2):
    assert fvector(F2) == (24,168,480,600,288,24)
    U = {(1,1,0,0), (1,-1,0,0), (0,0,1,1), (0,0,1,-1)}
    W = {i for i,v in enumerate(V) if v in U or tuple(-x for x in v) in U}
    assert len(W) == 8
    pairs = {(i,j) for i,j in combinations(sorted(W),2) if sq(i,j)==8}
    assert len(pairs)==4 and all(sum(j in p for p in pairs)==1 for j in W)
    target = {f for f in F2 if set(f)<=W}
    assert fvector(target) == (8,24,32,16)
    assert all(not (set(f)>=set(p)) for f in target for p in pairs)
    assert len(target)==80
    seq = json.loads(Path(__file__).with_name('collapse_pairs.json').read_text(encoding='utf-8'))
    assert len(seq)==752
    alive = set(F2)
    # Verify every alleged elementary collapse, not merely a Morse matching.
    for q, pair in enumerate(seq):
        assert isinstance(pair,list) and len(pair)==2
        small,large = map(tuple,pair)
        assert small == tuple(sorted(set(small)))
        assert large == tuple(sorted(set(large)))
        assert small in alive and large in alive
        assert small not in target and large not in target
        assert len(large)==len(small)+1 and set(small)<set(large)
        cofaces = [f for f in alive if len(f)==len(large) and set(small)<=set(f)]
        assert cofaces==[large], (q,small,cofaces)
        alive.remove(small)
        alive.remove(large)
    assert alive == target
    assert 1584-2*len(seq)==80
    print('scale 2:',fvector(F2),'752 certified elementary collapses; remaining 16-cell',fvector(target))
    print('marked 16-cell vertices:',sorted(W))



def mod_two_betti(faces):
    groups = {}
    for f in faces:
        groups.setdefault(len(f)-1, []).append(f)
    ranks = {}
    for d in range(1,max(groups)+1):
        ix = {f:i for i,f in enumerate(groups[d-1])}
        pivots = {}
        for f in groups[d]:
            z = 0
            for i in range(len(f)):
                z ^= 1 << ix[f[:i]+f[i+1:]]
            while z:
                h = z.bit_length()-1
                if h in pivots:
                    z ^= pivots[h]
                else:
                    pivots[h] = z
                    break
        ranks[d] = len(pivots)
    return {d:len(cs)-ranks.get(d,0)-ranks.get(d+1,0) for d,cs in groups.items()}

def check_last_stages():
    pair_squares=Counter(sq(i,j) for i,j in combinations(range(24),2))
    assert pair_squares == {2:96,4:72,6:96,8:12},pair_squares
    antipodal={(i,j) for i,j in combinations(range(24),2)
               if all(V[i][k]==-V[j][k] for k in range(4))}
    assert len(antipodal)==12
    assert antipodal=={(i,j) for i,j in combinations(range(24),2) if sq(i,j)>6}
    assert set().union(*[set(p) for p in antipodal]) == set(range(24))
    print('distance shells (squared):',dict(sorted(pair_squares.items())))
    print('scale sqrt(6): 12 antipodal pairs, hence a 12-fold join of S^0 = S^11')
    print('scale 2 sqrt(2): all 24 vertices span a simplex')

if __name__=='__main__':
    check_last_stages()
    F1 = cliques(2)
    F2 = cliques(4)
    check_first_stage(F1)
    check_collapse(F2)
    b1=mod_two_betti(F1);b2=mod_two_betti(F2)
    assert b1=={0:1,1:0,2:23},b1
    assert b2=={0:1,1:0,2:0,3:1,4:0,5:0},b2
    print('independent F2 Betti ranks:',b1,b2)
    print('VERIFY_OK')
