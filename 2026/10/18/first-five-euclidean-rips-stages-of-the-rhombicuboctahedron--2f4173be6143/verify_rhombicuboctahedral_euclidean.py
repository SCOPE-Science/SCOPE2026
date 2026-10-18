#!/usr/bin/env python3
"""Exact finite topological certificates for the Euclidean rhombicuboctahedron.

Run beside rhombicuboctahedron_certificates.json with Python 3 (standard library).
Distances are computed in the integer ring Z[sqrt(2)], and all elementary
collapses and integer row/column operations are checked without floating point.
"""
import itertools
import json
from collections import Counter, deque
from pathlib import Path

CERT=Path(__file__).with_name('rhombicuboctahedron_certificates.json')
SHELLS=((4,0),(8,0),(8,4),(12,4),(12,8),(16,8),(20,8))
SIGNS=list(itertools.product((-1,1),repeat=3))
ORDER={(-1,-1):0,(-1,0):1,(1,0):2,(1,1):3}
POINTS=sorted((tuple((s[j], s[j] if j==i else 0) for j in range(3))
        for i in range(3) for s in SIGNS),
        key=lambda pt:tuple(ORDER[z] for z in pt))
assert len(POINTS)==24 and len(set(POINTS))==24

def sqnorm(x,y):
    u=v=0
    for (a,b),(c,d) in zip(x,y):
        e=a-c;f=b-d
        u+=e*e+2*f*f;v+=2*e*f
    return (u,v)

DIST={p:sqnorm(POINTS[p[0]],POINTS[p[1]])
      for p in itertools.combinations(range(24),2)}
assert Counter(DIST.values())==Counter({(4,0):48,(8,0):36,(8,4):48,
                     (12,4):48,(12,8):36,(16,8):48,(20,8):12})
SHELL_INDEX={s:i for i,s in enumerate(SHELLS)}
assert set(DIST.values())==set(SHELLS)

def clique_faces(stage):
    edges={p for p,d in DIST.items() if SHELL_INDEX[d]<=stage}
    nbr={i:set() for i in range(24)}
    for a,b in edges:
        nbr[a].add(b);nbr[b].add(a)
    out=set()
    def visit(prefix,candidates):
        for j,v in enumerate(candidates):
            face=prefix+(v,)
            out.add(face)
            visit(face,[w for w in candidates[j+1:] if w in nbr[v]])
    visit((),list(range(24)))
    return out

STAGES=[clique_faces(j) for j in range(5)]
EXPECTED=((24,48,8),(24,84,80,18),(24,132,248,186,48),
          (24,180,576,906,744,304,48),
          (24,216,944,2202,2904,2236,960,192,8))
for fs,vec in zip(STAGES,EXPECTED):
    assert tuple(Counter(len(f) for f in fs).get(j,0) for j in range(1,len(vec)+1))==vec

# Relate the finer Euclidean filtration to the coarser graph-power stages.
GRAPH_NEIGHBORS={v:set() for v in range(24)}
for (a,b),d in DIST.items():
    if d==(4,0):GRAPH_NEIGHBORS[a].add(b);GRAPH_NEIGHBORS[b].add(a)
GDIST={}
for root in range(24):
    levels={root:0};todo=deque([root])
    while todo:
        v=todo.popleft()
        for w in GRAPH_NEIGHBORS[v]:
            if w not in levels:levels[w]=levels[v]+1;todo.append(w)
    assert len(levels)==24
    for dest in range(root+1,24):GDIST[(root,dest)]=levels[dest]
assert all((GDIST[e]<=2)==(SHELL_INDEX[d]<=2) for e,d in DIST.items())
assert all((GDIST[e]<=3)==(SHELL_INDEX[d]<=4) for e,d in DIST.items())


def subfaces(t):
    return (t[:i]+t[i+1:] for i in range(len(t)))

def close_facets(facets):
    fs=set()
    for f in facets:
        for r in range(1,len(f)+1):fs.update(itertools.combinations(f,r))
    return fs

ORIGINAL_TRIANGLES=sorted(f for f in STAGES[0] if len(f)==3)
assert len(ORIGINAL_TRIANGLES)==8
SQUARES=sorted(f for f in STAGES[1] if len(f)==4)
assert len(SQUARES)==18
SURFACE_TRIANGLES=set(ORIGINAL_TRIANGLES)
for square in SQUARES:
    diagonals=sorted(e for e in itertools.combinations(square,2) if DIST[e]==(8,0))
    assert len(diagonals)==2
    diagonal=diagonals[0]
    other=sorted(set(square)-set(diagonal))
    for x in other:SURFACE_TRIANGLES.add(tuple(sorted(diagonal+(x,))))
SURFACE=close_facets(SURFACE_TRIANGLES)
assert (len(SURFACE),len(SURFACE_TRIANGLES))==(134,44)
assert Counter(len(f) for f in SURFACE)==Counter({1:24,2:66,3:44})
assert len(SURFACE & STAGES[1])==134

# Verify the triangulated polyhedral boundary is a connected closed 2-manifold
# with Euler characteristic two (hence a triangulated 2-sphere).
face_edges={e for e in SURFACE if len(e)==2}
assert all(sum(set(e).issubset(t) for t in SURFACE_TRIANGLES)==2 for e in face_edges)
for v in range(24):
    lk_edges={tuple(sorted(set(t)-{v})) for t in SURFACE_TRIANGLES if v in t}
    lk_verts={w for e in lk_edges for w in e}
    assert all(sum(w in e for e in lk_edges)==2 for w in lk_verts)
    q=[next(iter(lk_verts))];seen={q[0]}
    for w in q:
        for e in lk_edges:
            if w in e:
                z=e[0] if e[1]==w else e[1]
                if z not in seen:seen.add(z);q.append(z)
    assert seen==lk_verts
q=[0];seen={0}
for v in q:
    for e in face_edges:
        if v in e:
            w=e[0] if e[1]==v else e[1]
            if w not in seen:seen.add(w);q.append(w)
assert len(seen)==24 and 24-66+44==2


def convert_pairs(raw):
    pairs=[]
    for a,b in raw:
        u=tuple(a);v=tuple(b)
        assert tuple(sorted(set(u)))==u and tuple(sorted(set(v)))==v
        pairs.append((u,v))
    return pairs


def verify_collapses(original,pairs,expected=None,dimension_limit=None):
    active=set(original)
    co={f:set() for f in active}
    for simplex in active:
        if len(simplex)>1:
            for face in subfaces(simplex):
                assert face in active
                co[face].add(simplex)
    for tau,sigma in pairs:
        assert tau in active and sigma in active
        assert len(sigma)==len(tau)+1 and tau in set(subfaces(sigma))
        assert co[tau]=={sigma} and not co[sigma]
        for f in (tau,sigma):
            active.remove(f)
        for f in (tau,sigma):
            if len(f)>1:
                for h in subfaces(f):
                    if h in active:co[h].remove(f)
    if expected is not None:
        assert active==expected
    if dimension_limit is not None:
        assert all(len(f)-1<=dimension_limit for f in active)
    return active

certificate=json.loads(CERT.read_text(encoding='utf-8'))
assert tuple(map(tuple,certificate['distance_squared_shells']))==SHELLS
FIRST_PAIRS=convert_pairs(certificate['first_stage_to_graph'])
assert len(FIRST_PAIRS)==8
GRAPH=STAGES[0].difference(set(itertools.chain.from_iterable(FIRST_PAIRS)))
assert GRAPH==verify_collapses(STAGES[0],FIRST_PAIRS)
assert all(len(f)<=2 for f in GRAPH)
assert Counter(len(f) for f in GRAPH)==Counter({1:24,2:40})
# Verify connectivity of the graph to compute the free fundamental group rank.
q=deque([0]);seen={0}
while q:
    v=q.popleft()
    for e in GRAPH:
        if len(e)==2 and v in e:
            w=e[0] if e[1]==v else e[1]
            if w not in seen:seen.add(w);q.append(w)
assert len(seen)==24

SECOND_PAIRS=convert_pairs(certificate['second_stage_to_surface'])
THIRD_PAIRS=convert_pairs(certificate['third_stage_to_second'])
FOURTH_PAIRS=convert_pairs(certificate['fourth_stage_to_second'])
assert len(SECOND_PAIRS)==36
assert len(THIRD_PAIRS)==216
assert len(FOURTH_PAIRS)==1288
verify_collapses(STAGES[1],SECOND_PAIRS,SURFACE)
verify_collapses(STAGES[2],THIRD_PAIRS,STAGES[1])
verify_collapses(STAGES[3],FOURTH_PAIRS,STAGES[1])

# Every edge added at the fifth distance shell is nullhomotopic relative to
# the previous, simply connected complex, via an explicitly existing triangle.
NEW_EDGES=[e for e in STAGES[4]-STAGES[3] if len(e)==2]
assert len(NEW_EDGES)==36
for a,b in NEW_EDGES:
    assert any(tuple(sorted((a,c))) in STAGES[3] and
               tuple(sorted((b,c))) in STAGES[3] and
               tuple(sorted((a,b,c))) in STAGES[4]
               for c in range(24) if c not in (a,b))

FIFTH_PAIRS=convert_pairs(certificate['fifth_stage_dimension_three'])
assert len(FIFTH_PAIRS)==3872
REDUCED=verify_collapses(STAGES[4],FIFTH_PAIRS,dimension_limit=3)
assert Counter(len(f) for f in REDUCED)==Counter({1:24,2:216,3:944,4:758})

# Integer-unimodular elimination of the 944 x 758 third boundary matrix.
# Each pivot is +/-1 and so gives invertible integer row/column operations.
TRIANGLES=sorted(f for f in REDUCED if len(f)==3)
TETRAHEDRA=sorted(f for f in REDUCED if len(f)==4)
index={f:i for i,f in enumerate(TRIANGLES)}
rows=[{} for _ in TRIANGLES];cols=[{} for _ in TETRAHEDRA]
for j,sigma in enumerate(TETRAHEDRA):
    for i,face in enumerate(subfaces(sigma)):
        a=index[face];sign=(-1)**i
        rows[a][j]=sign;cols[j][a]=sign
pivots=certificate['boundary_three_unit_pivots']
assert len(pivots)==751
for i,j in pivots:
    assert i in range(len(rows)) and j in range(len(cols))
    assert rows[i].get(j) in (-1,1)
    a=rows[i][j]
    for r,x in list(cols[j].items()):
        if r==i:continue
        coeff=x//a
        for c,y in list(rows[i].items()):
            z=rows[r].get(c,0)-coeff*y
            if z:
                rows[r][c]=z;cols[c][r]=z
            else:
                rows[r].pop(c,None);cols[c].pop(r,None)
    assert cols[j]=={i:a}
    for c,x in list(rows[i].items()):
        if c==j:continue
        # Integral column operation: C_c -> C_c - (x/a) C_j.
        assert x%a==0 and cols[c].get(i)==x
        rows[i].pop(c);cols[c].pop(i)
    assert rows[i]=={j:a}
    rows[i].pop(j);cols[j].pop(i)
    assert not rows[i] and not cols[j]
assert all(not row for row in rows) and all(not col for col in cols)
# The third boundary is integrally equivalent to 751 copies of (1), and
# seven zero columns. Its image is primitive, and kernel = Z^7.
# The connected, simply connected 3-dimensional reduced complex has E-V+1
# =193 independent 1-cycles; this equals 944-751. Hence H2=0 over Z.
assert 944-751==216-24+1 and 758-751==7
print('VERIFY_OK')
print('FACE_VECTORS',EXPECTED)
print('SIMPLE_COLLAPSES',len(FIRST_PAIRS),len(SECOND_PAIRS),len(THIRD_PAIRS),len(FOURTH_PAIRS),len(FIFTH_PAIRS))
print('INTEGRAL_BOUNDARY_UNIT_PIVOTS',len(pivots),'H3_RANK',758-751)
