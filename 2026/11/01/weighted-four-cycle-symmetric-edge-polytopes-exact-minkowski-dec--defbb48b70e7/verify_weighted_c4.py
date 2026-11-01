from fractions import Fraction as F
from itertools import combinations
import sympy as S

def poly_facets(a,b,c):
    v=[(1,0,0),(0,1,0),(0,0,1),(a,b,c),(-1,0,0),(0,-1,0),(0,0,-1),(-a,-b,-c)]
    v=[S.Matrix(tuple(map(S.Rational,p))) for p in v]
    facets=set()
    for t in combinations(range(8),3):
        x,y,z=[v[i] for i in t]
        n=(y-x).cross(z-x)
        if n==S.zeros(3,1): continue
        d=n.dot(x)
        for sig in [1,-1]:
            vals=[sig*(n.dot(w)-d) for w in v]
            if all(r<=0 for r in vals):
                f=frozenset(i for i,r in enumerate(vals) if r==0)
                if len(f)>=3: facets.add(f)
    return v,facets

def rank_summands(v,faces):
    edges=[]
    for i,j in combinations(range(8),2):
        if sum((i in f and j in f) for f in faces)>=2: edges.append((i,j))
    A=[]
    for i,j in edges:
        d=v[j]-v[i]
        # Cross product linear equations for unknown q_i (24 variables)
        for k in range(3):
            # (q_j-q_i)x d = 0
            row=[S.Integer(0)]*24
            u,w=(k+1)%3,(k+2)%3
            row[3*j+u]+=d[w]; row[3*i+u]-=d[w]
            row[3*j+w]-=d[u]; row[3*i+w]+=d[u]
            A.append(row)
    M=S.Matrix(A)
    return len(edges),24-M.rank()

def check_case(a,b,c,expected_vertices,expected_faces,expected_deformation_dim=None):
    v,faces=poly_facets(a,b,c)
    active=set().union(*faces)
    assert len(active)==expected_vertices
    assert len(faces)==expected_faces
    if expected_deformation_dim is not None:
        assert expected_vertices==8
        edges,dim=rank_summands(v,faces)
        assert dim==expected_deformation_dim,(a,b,c,dim)
    return v,faces

for params in [
    (F(1),F(1),F(1),8,6,6),
    (F(1),F(1,2),F(1,2),8,8,5),
    (F(1),F(2),F(2),8,8,5),
    (F(4,5),F(7,10),F(1,2),8,10,4),
    (F(3,4),F(3,4),F(3,4),8,12,4),
    (F(3,2),F(3,4),F(4,5),8,12,4),
    (F(5),F(1),F(1),6,8,None),
    (F(1,5),F(1,5),F(1,5),6,8,None),
]:
    check_case(*params)

for t in [F(1,2),F(2)]:
    _,faces=check_case(F(1),t,t,8,8,5)
    expected_quads={frozenset(i-1 for i in f) for f in
        ((1,2,4,7),(1,3,4,6),(2,5,7,8),(3,5,6,8))}
    if t<1:
        triples=((1,6,7),(6,7,8),(2,3,4),(2,3,5))
    else:
        triples=((1,6,8),(1,7,8),(2,4,5),(3,4,5))
    expected_tris={frozenset(i-1 for i in f) for f in triples}
    assert faces==expected_quads|expected_tris

print('PASS: exact supporting faces, deformation ranks and two-equality face tables')
