"""Exact verification of the Euclidean Vietoris--Rips filtration on fourteen rhombic-dodecahedral vertices."""
from itertools import product, permutations, combinations
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json

AXES = [tuple(2*s if i == j else 0 for j in range(3)) for i in range(3) for s in (-1, 1)]
CUBES = list(product((-1, 1), repeat=3))
VERTICES = sorted(AXES + CUBES)
AXIS_IDS = {i for i, v in enumerate(VERTICES) if v in AXES}
CUBE_IDS = set(range(14)) - AXIS_IDS
INDEX = {v:i for i,v in enumerate(VERTICES)}


def sq(i,j):
    return sum((x-y)**2 for x,y in zip(VERTICES[i],VERTICES[j]))


def faces(threshold):
    return {tuple(i for i in range(14) if (mask>>i)&1)
            for mask in range(1, 1<<14)
            if all(sq(i,j)<=threshold for i,j in combinations([i for i in range(14) if (mask>>i)&1],2))}


def subsimplices(max_faces):
    return {f for facet in max_faces for r in range(1,len(facet)+1) for f in combinations(facet,r)}


def sign_perm(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


def transform(v,perm,signs):
    return tuple(signs[i]*v[perm[i]] for i in range(3))


def lefschetz(F,mapping):
    result = -1  # augmented empty face, subtract 1 from ordinary Lefschetz trace
    for face in F:
        im = [mapping[i] for i in face]
        if sorted(im) == list(face):
            result += (-1)**(len(face)-1)*sign_perm(im)
    return result


def det3(rows):
    a,b,c=rows
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def verify_convex_facets():
    # The twelve supporting halfspaces |x_i|+|x_j| <= 2.
    normals=[]
    for i,j in combinations(range(3),2):
        for a,b in product((-1,1),repeat=2):
            normals.append(tuple(a if t==i else b if t==j else 0 for t in range(3)))
    assert len(normals)==12
    for v in VERTICES:
        assert all(sum(a*b for a,b in zip(n,v))<=2 for n in normals)
    vertices=set()
    for rows in combinations(normals,3):
        determinant=det3(rows)
        if determinant==0:continue
        p=tuple(Fraction(det3(tuple(tuple(2 if col==i else v for col,v in enumerate(row)) for row in rows)),determinant) for i in range(3))
        if all(sum(a*b for a,b in zip(n,p))<=2 for n in normals):vertices.add(p)
    assert vertices==set(VERTICES)
    for n in normals:
        face={v for v in VERTICES if sum(a*b for a,b in zip(n,v))==2}
        assert len(face)==4
    return True


def check():
    verify_convex_facets()
    assert len(VERTICES)==14 and len(set(VERTICES))==14
    pairs=Counter(sq(i,j) for i in range(14) for j in range(i+1,14))
    assert pairs == {3:24, 4:12, 8:24, 11:24, 12:4, 16:3}
    F3,F4,F8,F11,F12,F16=(faces(k) for k in (3,4,8,11,12,16))
    assert [len(F) for F in (F3,F4,F8,F11,F12,F16)] == [38,74,240,2186,6911,16383]
    assert Counter(map(len,F4))=={1:14,2:36,3:24}
    # Every supporting face plane s*x_i+t*x_j=2 gives a rhombus,
    # subdivided along the cube-to-cube diagonal.
    triangles=[]
    for i,j in combinations(range(3),2):
        for s,t in product((-1,1),repeat=2):
            cube=[a for a in CUBE_IDS if VERTICES[a][i]==s and VERTICES[a][j]==t]
            axes=[INDEX[tuple(2*s if b==i else 0 for b in range(3))],
                  INDEX[tuple(2*t if b==j else 0 for b in range(3))]]
            assert len(cube)==2
            triangles.extend(tuple(sorted(cube+[a])) for a in axes)
    assert len(set(triangles))==24 and F4==subsimplices(triangles)
    # First nonzero scale is the connected bipartite polytope edge graph.
    assert Counter(map(len,F3))=={1:14,2:24}
    seen={0};frontier=[0]
    while frontier:
        v=frontier.pop()
        for edge in [e for e in F3 if len(e)==2 and v in e]:
            other=next(x for x in edge if x!=v)
            if other not in seen:seen.add(other);frontier.append(other)
    assert len(seen)==14
    # Cubes form the boundary of the four-dimensional crosspolytope at squared scale eight.
    target={f for f in F8 if set(f)<=CUBE_IDS}
    antipodal_cube={frozenset((i,INDEX[tuple(-x for x in VERTICES[i])])) for i in CUBE_IDS}
    assert len(antipodal_cube)==4
    assert target=={f for f in subsimplices([tuple(sorted(p)) for p in product(*[tuple(p) for p in sorted(antipodal_cube,key=lambda x:min(x))])])}
    # Reproduce and check every elementary free-face deletion.
    cert_path=Path(__file__).with_name('collapse_pairs.json')
    certificate=json.loads(cert_path.read_text(encoding='utf-8'))
    assert certificate['vertices']==[list(x) for x in VERTICES]
    assert len(certificate['pairs'])==80
    present=set(F8)
    for lo,hi in certificate['pairs']:
        lo,hi=tuple(lo),tuple(hi)
        assert lo in present and hi in present and lo not in target and hi not in target
        assert set(lo)<set(hi) and len(hi)==len(lo)+1
        cofaces=[tuple(sorted(lo+(v,))) for v in range(14) if v not in lo and tuple(sorted(lo+(v,))) in present]
        assert cofaces==[hi],('not free',lo,hi,cofaces)
        present.remove(lo);present.remove(hi)
    assert present==target
    # At squared radius 11: every simplex avoids all seven antipodal pairs.
    antipodal_all={frozenset((i,INDEX[tuple(-x for x in VERTICES[i])])) for i in range(14)}
    assert len(antipodal_all)==7
    expected11={f for f in F16 if all(not p<=set(f) for p in antipodal_all)}
    assert F11==expected11
    # Squared radius 12: only three axis-antipodal pairs remain forbidden.
    antipodal_axis={p for p in antipodal_all if p<=AXIS_IDS}
    assert len(antipodal_axis)==3
    assert F12=={f for f in F16 if all(not p<=set(f) for p in antipodal_axis)}
    assert all(f in F12 for f in F11)
    # At radius 12 the full cube simplex is a join factor, so complex is contractible.
    assert tuple(sorted(CUBE_IDS)) in F12
    # Full 48-element signed-permutation group and three homology character tests.
    reps=sorted((v for v in CUBES if v[0]*v[1]*v[2]==1))
    rep_index={v:i for i,v in enumerate(reps)}
    tests=0
    for perm in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            mapping={i:INDEX[transform(v,perm,signs)] for i,v in enumerate(VERTICES)}
            det=sign_perm(perm)*signs[0]*signs[1]*signs[2]
            dperm=[]
            for rep in reps:
                im=transform(rep,perm,signs)
                if im not in rep_index:im=tuple(-x for x in im)
                dperm.append(rep_index[im])
            chi3=sign_perm(dperm)
            chi2=det
            chi6=det*chi3
            assert lefschetz(F4,mapping)==chi2
            assert lefschetz(F8,mapping)==-chi3
            assert lefschetz(F11,mapping)==chi6
            fixed_vertices=sum(mapping[i]==i for i in range(14))
            fixed_edges=sum(mapping[e[0]]==e[0] and mapping[e[1]]==e[1] for e in F3 if len(e)==2)
            chi1=1+fixed_edges-fixed_vertices
            assert lefschetz(F3,mapping)==-chi1
            tests+=1
    assert tests==48
    print('VERIFY_OK DISTANCE_SHELLS 3:24 4:12 8:24 11:24 12:4 16:3')
    print('FACES 38 74 240 2186 6911 16383; RELATIVE_COLLAPSES 80')
    print('CHARACTER_CHECKS 48_ELEMENTS_X_4_STAGES')
    print('HOMOTOPY_AND_INTEGRAL_BARCODE_BY_GEOMETRIC_JOIN_COLLAPSE')


if __name__=='__main__':
    check()
