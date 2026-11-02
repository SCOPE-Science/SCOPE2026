#!/usr/bin/env python3
"""Standalone exact Q(sqrt(5)) checker for the icosidodecahedron section law.

Python 3 standard library only. Run: python verify_icosidodecahedron.py
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter
from math import acos, pi

class Q:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=q(o); return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,o): return self+-q(o)
    def __rsub__(self,o): return q(o)+-self
    def __mul__(self,o):
        o=q(o);return Q(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=q(o)
        den=o.a*o.a-5*o.b*o.b
        if not den: raise ZeroDivisionError
        return Q((self.a*o.a-5*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=q(o);return self.a==o.a and self.b==o.b
    def __hash__(self): return hash((self.a,self.b))
    def sign(self):
        a,b=self.a,self.b
        if not b:return (a>0)-(a<0)
        if not a:return (b>0)-(b<0)
        if (a>0)==(b>0): return (a>0)-(a<0)
        if a>0:return 1 if a*a>5*b*b else -1
        return 1 if 5*b*b>a*a else -1
    def __repr__(self): return f'{self.a}+({self.b})*sqrt(5)'

def q(t):return t if isinstance(t,Q) else Q(t)
def vec(a,b,c):return (q(a),q(b),q(c))
def add(u,v):return tuple(x+y for x,y in zip(u,v))
def sub(u,v):return tuple(x-y for x,y in zip(u,v))
def mul(u,c):return tuple(x*c for x in u)
def dot(u,v):return sum((x*y for x,y in zip(u,v)),Q())
def cross(u,v):
    a,b,c=u;d,e,f=v
    return (b*f-c*e,c*d-a*f,a*e-b*d)
def sqdist(u,v):return dot(sub(u,v),sub(u,v))

def run():
    phi=Q(F(1,2),F(1,2))
    ico=[vec(0,a,b*phi) for a,b in product((-1,1),repeat=2)]
    ico += [vec(a,b*phi,0) for a,b in product((-1,1),repeat=2)]
    ico += [vec(a*phi,0,b) for a,b in product((-1,1),repeat=2)]
    assert len(ico)==12 and len(set(ico))==12
    ico_edges=[(i,j) for i,j in combinations(range(12),2) if sqdist(ico[i],ico[j])==4]
    assert len(ico_edges)==30
    assert Counter(k for e in ico_edges for k in e)==Counter({i:5 for i in range(12)})
    verts=[mul(add(ico[i],ico[j]),Q(F(1,2))) for i,j in ico_edges]
    assert len(verts)==30 and len(set(verts))==30
    # Equal-radii vertices and the unique shortest intervertex distance.
    r2=phi*phi
    assert all(dot(v,v)==r2 for v in verts)
    distances={sqdist(verts[i],verts[j]) for i,j in combinations(range(30),2)}
    assert all((t-1).sign()>=0 for t in distances) and Q(1) in distances
    # Verify the 20 triangular and 12 pentagonal supporting facets, so that
    # the shortest-distance graph is the actual boundary edge graph.
    original_faces=[]
    original_edge_set=set(ico_edges)
    for i,j,k in combinations(range(12),3):
        if all((min(a,b),max(a,b)) in original_edge_set for a,b in ((i,j),(i,k),(j,k))):
            original_faces.append((i,j,k))
    assert len(original_faces)==20
    faces=[]
    for a,b,c in original_faces:
        ids={ico_edges.index((min(i,j),max(i,j))) for i,j in ((a,b),(a,c),(b,c))}
        normal=add(add(ico[a],ico[b]),ico[c])
        vals=[dot(normal,v) for v in verts]
        mx=vals[next(iter(ids))]
        assert all(vals[i]==mx for i in ids)
        assert all((mx-vals[i]).sign()>0 for i in range(30) if i not in ids)
        faces.append(ids)
    for i,u in enumerate(ico):
        ids={k for k,(a,b) in enumerate(ico_edges) if i in (a,b)}
        assert len(ids)==5
        vals=[dot(u,v) for v in verts]
        mx=vals[next(iter(ids))]
        assert all(vals[k]==mx for k in ids)
        assert all((mx-vals[k]).sign()>0 for k in range(30) if k not in ids)
        faces.append(ids)
    assert len(faces)==32
    edges=[(i,j) for i,j in combinations(range(30),2) if sqdist(verts[i],verts[j])==1]
    for i,j in edges:
        assert sum(i in face and j in face for face in faces)==2
    assert all(sum(i in face and j in face for face in faces)<2 or (i,j) in edges
               for i,j in combinations(range(30),2))
    print('EXACT_TWENTY_TRIANGLE_TWELVE_PENTAGON_SUPPORTING_FACETS_PASSED')
    assert len(edges)==60
    neighbors=[set() for _ in verts]
    for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
    assert all(len(n)==4 for n in neighbors)
    print('EXACT_RECTIFIED_ICOSAHEDRON_30_VERTICES_60_EDGES_PASSED')
    for k,v in enumerate(verts):
        ws=[verts[j] for j in sorted(neighbors[k])]
        pairings=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
        good=[]
        for pairing in pairings:
            if all(all(t==0 for t in cross(v,add(ws[i],ws[j]))) for i,j in pairing):
                good.append(pairing)
        assert len(good)==1,(k,good)
    print('EXACT_RADIAL_OPPOSITE_NEIGHBOR_PAIRING_AT_ALL_30_VERTICES_PASSED')
    # Edge-endpoint central angle has cosine phi/2=cos(pi/5).
    assert Q(1)-Q(F(1,2))/r2==phi*Q(F(1,2))
    assert abs(acos((1+5**.5)/4)-pi/5)<1e-14
    assert 60*F(1,5)==12
    print('EXACT_EDGE_CROFTON_ANGLE_PI_OVER_FIVE_AND_MEAN_TWELVE_PASSED')
    witness_normals=[vec(1,2,7),vec(2,7,13),vec(3,11,23),vec(19,-13,7)]
    for normal in witness_normals:
        signs=[dot(v,normal).sign() for v in verts]
        assert all(s in (-1,1) for s in signs)
        assert sum(signs[i]!=signs[j] for i,j in edges)==12
    print('FOUR_EXACT_GENERIC_NORMAL_SECTION_COUNTS_TWELVE_PASSED')
    # Optional randomized diagnostic independent of the proof.
    import random
    rng=random.Random(20261030)
    for _ in range(15000):
        nn=[rng.gauss(0,1) for _ in range(3)]
        sg=[sum((float(t.a)+float(t.b)*5**.5)*nn[k] for k,t in enumerate(v))>0 for v in verts]
        assert sum(sg[i]!=sg[j] for i,j in edges)==12
    print('FIFTEEN_THOUSAND_INDEPENDENT_GAUSSIAN_NORMAL_DIAGNOSTICS_PASSED')
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':run()
