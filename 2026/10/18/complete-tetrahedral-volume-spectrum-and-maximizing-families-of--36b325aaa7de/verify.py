#!/usr/bin/env python3
"""Exact determinant-spectrum certificate for a regular icosidodecahedron.

Requires only the Python 3 standard library. No floating-point calculations
are used. A pair (a,b) denotes the algebraic number a+b*phi, phi^2=phi+1.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product

ZERO=(0,0)
ONE=(1,0)

def add(x,y): return x[0]+y[0],x[1]+y[1]
def sub(x,y): return x[0]-y[0],x[1]-y[1]
def neg(x): return -x[0],-x[1]
def mul(x,y):
    a,b=x; c,d=y
    return a*c+b*d, a*d+b*c+b*d

def sign(x):
    """Exact sign in Q(sqrt(5)) by comparing integer squares."""
    a,b=x
    u=2*a+b
    if b==0: return (a>0)-(a<0)
    if u==0: return (b>0)-(b<0)
    if u>0 and b>0: return 1
    if u<0 and b<0: return -1
    s=u*u-5*b*b
    assert s!=0  # sqrt(5) irrational for b!=0
    if u>0: return (s>0)-(s<0)
    return (s<0)-(s>0)

def vecadd(x,y): return tuple(add(a,b) for a,b in zip(x,y))
def vecsub(x,y): return tuple(sub(a,b) for a,b in zip(x,y))
def dot(x,y):
    z=ZERO
    for a,b in zip(x,y):z=add(z,mul(a,b))
    return z

def cross(x,y):
    return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
            sub(mul(x[2],y[0]),mul(x[0],y[2])),
            sub(mul(x[0],y[1]),mul(x[1],y[0])))

def det3(x,y,z): return dot(x,cross(y,z))

def det4(points):
    """Independent 4-by-4 homogeneous determinant via all 24 permutations."""
    rows=[(ONE,)+tuple(p) for p in points]
    total=ZERO
    for pi in permutations(range(4)):
        term=ONE
        for i,j in enumerate(pi): term=mul(term,rows[i][j])
        inv=sum(pi[i]>pi[j] for i in range(4) for j in range(i+1,4))
        total=add(total,neg(term) if inv%2 else term)
    return total

def dist2(p,q):
    v=vecsub(p,q)
    return dot(v,v)

def original_vertices():
    S=set()
    for s,t in product((-1,1),repeat=2):
        S.add((ZERO,(s,0),(0,t)))
        S.add(((s,0),(0,t),ZERO))
        S.add(((0,s),ZERO,(t,0)))
    assert len(S)==12
    return sorted(S)

EXPECTED_HIST={
    (0,0):2235, (1,0):780, (0,1):1380, (1,1):2460,
    (0,2):240, (2,1):60, (1,2):3660, (2,2):1800,
    (1,3):840, (2,3):2460, (3,3):240, (2,4):3060,
    (3,4):1560, (2,5):120, (3,5):1380, (4,5):180,
    (3,6):420, (4,6):1800, (4,7):840, (5,7):180,
    (4,8):210, (5,8):780, (6,8):60, (5,9):120,
    (6,9):240, (6,10):240, (7,11):60,
}

def run():
    initial=original_vertices()
    edges=[(i,j) for i,j in combinations(range(12),2)
           if dist2(initial[i],initial[j])==(4,0)]
    assert len(edges)==30
    poly=sorted(set(vecadd(initial[i],initial[j]) for i,j in edges))
    assert len(poly)==30
    # poly consists of TWICE the actual unit-edge icosidodecahedron vertices.

    # Independent base icosahedron volume check: its 20 triangular facets,
    # each of Euclidean area sqrt(3), have determinant magnitude 2*phi^2.
    E=set(edges)
    faces=[t for t in combinations(range(12),3) if all(pair in E for pair in combinations(t,2))]
    assert len(faces)==20
    assert {tuple(det3(initial[i],initial[j],initial[k])) for i,j,k in faces}
    assert {absnum(det3(initial[i],initial[j],initial[k])) for i,j,k in faces}=={(2,2)}

    histogram=Counter(); winners=[]; maximum=ZERO; repetitions=0
    for ids in combinations(range(30),4):
        a,b,c,d=[poly[i] for i in ids]
        determinant=det3(vecsub(b,a),vecsub(c,a),vecsub(d,a))
        assert determinant==det4((a,b,c,d))
        q=determinant if sign(determinant)>=0 else neg(determinant)
        assert q[0]%4==0 and q[1]%4==0
        histogram[(q[0]//4,q[1]//4)]+=1
        comparison=sign(sub(q,maximum))
        if comparison>0: maximum=q;winners=[tuple(ids)]
        elif comparison==0: winners.append(tuple(ids))
        repetitions+=1

    assert repetitions==27405 and sum(histogram.values())==27405
    assert histogram==EXPECTED_HIST, ('histogram mismatch',histogram-EXPECTED_HIST)
    assert maximum==(28,44) and len(winners)==60
    assert (0,15,16,26) in winners

    maxsets=[set(w) for w in winners]
    paircodegrees=Counter(pair for w in winners for pair in combinations(w,2))
    assert max(paircodegrees.values())==3
    triple_to_apex=defaultdict(set)
    for w in winners:
        for tri in combinations(w,3):
            triple_to_apex[tri].add(next(x for x in w if x not in tri))
    assert Counter(map(len,triple_to_apex.values()))=={1:180,3:20}

    # The twenty variable-apex triangles are true faces of the polytope.
    families=[];used=set();face_set=set()
    for fixed,choices in sorted(triple_to_apex.items()):
        if len(choices)!=3:continue
        choices=tuple(sorted(choices))
        assert all(dist2(poly[x],poly[y])==(4,0) for x,y in combinations(choices,2))
        assert all(dist2(poly[x],poly[y])==(8,12) for x,y in combinations(fixed,2))
        a,b,c=[poly[i] for i in choices]
        normal=cross(vecsub(b,a),vecsub(c,a))
        sides={sign(dot(normal,vecsub(poly[j],a))) for j in range(30) if j not in choices}
        assert sides=={1} or sides=={-1}, (fixed,choices,sides)
        face_set.add(choices)
        for v in choices:
            w=tuple(sorted(fixed+(v,)))
            assert w in winners
            used.add(w)
        families.append((fixed,choices))
    assert len(families)==20 and len(face_set)==20 and used==set(winners)
    print('VERIFY_OK original_icosahedron=12_vertices_30_edges_20_faces',
          'midpoint_polyhedron=30_vertices', 'quadruples=27405',
          'volume_levels=27', 'max_det=(28,44)',
          'max_sets=60', 'facial_families=20', 'max_pair_codegree=3')

def absnum(x):return x if sign(x)>=0 else neg(x)

if __name__=='__main__':run()
