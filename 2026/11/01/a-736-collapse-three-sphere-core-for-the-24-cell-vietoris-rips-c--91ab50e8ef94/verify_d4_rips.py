"""Exact finite verification of a 24-cell Vietoris--Rips simple collapse.

Requires Python 3.9+ standard library only. Run in the directory containing
collapse_certificate.json. Geometry uses squared Euclidean distance exactly.
"""
import itertools
import json
from collections import Counter
from pathlib import Path


def roots():
    points = set()
    for i, j in itertools.combinations(range(4), 2):
        for a, b in itertools.product((-1, 1), repeat=2):
            x = [0]*4
            x[i], x[j] = a, b
            points.add(tuple(x))
    return sorted(points)


def distance2(u,v):
    return sum((a-b)**2 for a,b in zip(u,v))


def flag_faces(points, threshold):
    n = len(points)
    neighbors = [sum(1<<j for j in range(n)
                     if j != i and distance2(points[i],points[j]) <= threshold)
                 for i in range(n)]
    faces = set()
    def rec(face, available):
        if face:
            faces.add(face)
        while available:
            bit = available & -available
            available -= bit
            i = bit.bit_length()-1
            rec(face+(i,), available & neighbors[i])
    rec((),(1<<n)-1)
    return faces


def fvec(faces):
    return tuple(Counter(len(s) for s in faces)[k] for k in range(1,7) if any(len(s)==k for s in faces))


def is_complex(F):
    return all(s[:i]+s[i+1:] in F for s in F for i in range(len(s)) if len(s)>1)


def replay(F, steps, name):
    F = set(F)
    assert is_complex(F), name+' starts with a noncomplex'
    for k, pair in enumerate(steps, 1):
        assert len(pair)==2, (name,k,'pair count')
        a,b = tuple(pair[0]),tuple(pair[1])
        assert a in F and b in F, (name,k,'missing face')
        assert len(a)+1==len(b) and set(a).issubset(b), (name,k,'not codimension one')
        cofaces=[c for c in F if len(c)==len(a)+1 and set(a).issubset(c)]
        assert cofaces==[b],(name,k,'not a free face',len(cofaces))
        F.remove(a)
        F.remove(b)
    assert is_complex(F), name+' not closed at end'
    return F


def shelling_ball(F, tetra_order):
    tetra_order=[tuple(t) for t in tetra_order]
    assert len(tetra_order)==15 and len(set(tetra_order))==15
    assert set(tetra_order)=={s for s in F if len(s)==4}
    def subs(t):
        return {u for k in range(1,len(t)+1) for u in itertools.combinations(t,k)}
    visited=set()
    triangle_counts=Counter()
    for k,t in enumerate(tetra_order):
        sub=subs(t)
        if k:
            common=visited&sub
            common_triangles={a for a in common if len(a)==3}
            assert 1<=len(common_triangles)<=3,('not disk facet collection',k)
            generated=set().union(*(subs(a) for a in common_triangles))
            assert common==generated,('lower-dimensional spurious attachment',k)
            assert all(triangle_counts[a]==1 for a in common_triangles),('not boundary',k)
        visited|=sub
        triangle_counts.update(itertools.combinations(t,3))
    assert visited==F,'uncovered deletion faces'
    assert set(triangle_counts.values())<={1,2}
    return {triangle for triangle,n in triangle_counts.items() if n==1}


def main():
    c=json.loads(Path(__file__).with_name('collapse_certificate.json').read_text('utf-8'))
    assert c['schema_version']==1 and c['threshold_squared']==4
    P=roots()
    assert len(P)==24 and c['root_vertices']==[list(a) for a in P]
    assert Counter(distance2(P[i],P[j]) for i in range(24) for j in range(i+1,24))=={2:96,4:72,6:96,8:12}
    first=flag_faces(P,2)
    assert fvec(first)==(24,96,96)
    K=flag_faces(P,4)
    assert fvec(K)==(24,168,480,600,288,24) and len(K)==1584
    assert len(c['first_collapses'])==736
    R=replay(K,c['first_collapses'],'scale-two collapse')
    assert fvec(R)==(10,33,46,23) and len(R)==112
    assert set(map(tuple,c['remaining_tetrahedra']))=={s for s in R if len(s)==4}
    pivot=c['pivot_vertex']
    assert pivot==2 and (pivot,) in R
    link={tuple(y for y in s if y!=pivot) for s in R if pivot in s and len(s)>=2}
    assert fvec(link)==(6,12,8)
    link_verts=sorted(s[0] for s in link if len(s)==1)
    link_edges={s for s in link if len(s)==2}
    missing=[(a,b) for a,b in itertools.combinations(link_verts,2) if (a,b) not in link_edges]
    assert missing==[(3,20),(6,17),(9,14)]
    # The link is the full join of three 0-spheres, hence S^2.
    assert {s for s in link if len(s)==3}=={tuple(sorted(c)) for c in itertools.combinations(link_verts,3)
        if all(not set(pair).issubset(c) for pair in missing)}
    deletion={s for s in R if pivot not in s}
    assert len(deletion)==85 and len(c['deletion_collapses'])==42
    reduced=replay(deletion,c['deletion_collapses'],'vertex deletion')
    assert len(reduced)==1 and all(len(s)==1 for s in reduced)
    boundary=shelling_ball(deletion,c['deletion_tetra_shelling'])
    assert boundary=={s for s in link if len(s)==3},'3-ball boundary != cone boundary'
    # The certified shelling makes deletion a PL 3-ball; the cone on the
    # octahedral link is another PL 3-ball. Their common boundary is S^2.
    # Thus R is a triangulated S^3; K collapses to it simplicially.
    antipodal={tuple(sorted((i,P.index(tuple(-a for a in P[i]))))) for i in range(24)}
    assert len(antipodal)==12
    assert {(i,j) for i in range(24) for j in range(i+1,24) if distance2(P[i],P[j])==8}==antipodal
    assert c['expected_summary']=={'full_faces':1584,'collapse_pairs':736,'reduced_faces':112,'reduced_tetrahedra':23,'deletion_shelling_tetrahedra':15,'deletion_collapse_pairs':42}
    print('DISTANCE_CLASSES 2:96 4:72 6:96 8:12')
    print('SMALL_SCALE_FVECTOR 24 96 96')
    print('SCALE_TWO_FVECTOR 24 168 480 600 288 24')
    print('COLLAPSE_PAIRS 736 REMAINDER_FVECTOR 10 33 46 23')
    print('OCTAHEDRAL_LINK 6 12 8; SHELLABLE_BALL 15 TETRAHEDRA; DELETION_PAIRS 42')
    print('LARGER_SCALE CROSS_POLYTOPE_S11 THEN CONTRACTIBLE')
    print('VERIFY_OK')

if __name__=='__main__':main()
