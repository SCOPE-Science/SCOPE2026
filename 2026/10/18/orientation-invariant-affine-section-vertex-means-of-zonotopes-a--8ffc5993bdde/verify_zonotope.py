#!/usr/bin/env python3
"""Independent finite checks of the zonotope section-vertex expectation law.
Requires Python 3, NumPy, SciPy. The theorem itself is proved without these packages.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb
import numpy as np
from scipy.spatial import ConvexHull


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def det(a,b,c): return dot(a,cross(b,c))

def zone_counts(v):
    k=[]
    for i,a in enumerate(v):
        planes=set()
        for j,b in enumerate(v):
            if j==i:continue
            n=cross(a,b)
            assert any(n)
            from math import gcd
            g=0
            for x in n:g=gcd(g,abs(x))
            n=tuple(x//g for x in n)
            if next(x for x in n if x)!=abs(next(x for x in n if x)):
                n=tuple(-x for x in n)
            planes.add(n)
        k.append(len(planes))
    return k

def geom_edges(v):
    points=sorted(set(tuple(sum(bits[i]*v[i][j] for i in range(len(v))) for j in range(3))
                      for bits in product((0,1),repeat=len(v))))
    hull=ConvexHull(np.array(points,dtype=float))
    # Triangles in a triangulated hull include facet diagonals; remove them by
    # testing whether adjacent triangle supporting planes genuinely differ.
    normals=[]
    for tri in hull.simplices:
        a,b,c=[points[int(i)] for i in tri]
        normals.append(cross(tuple(b[i]-a[i] for i in range(3)),tuple(c[i]-a[i] for i in range(3))))
    memberships={}
    for j,tri in enumerate(hull.simplices):
        for a,b in combinations(map(int,tri),2):
            memberships.setdefault(tuple(sorted((a,b))),[]).append(j)
    result=[]
    for (i,j),ids in memberships.items():
        if len(ids)<2:raise AssertionError(('hull-facet adjacency missing',i,j))
        if any(any(cross(normals[u],normals[w])) for u,w in combinations(ids,2)):
            a,b=points[i],points[j]
            result.append((a,b))
    return points,result

def eval_case(name,v,expected_counts):
    k=zone_counts(v)
    assert k==expected_counts,(name,k,expected_counts)
    points,edges=geom_edges(v)
    labels=[]
    for a,b in edges:
        e=tuple(b[i]-a[i] for i in range(3))
        found=[i for i,w in enumerate(v) if e==w or e==tuple(-x for x in w)]
        assert len(found)==1,(name,a,b,e,found)
        labels.append(found[0])
    cc=Counter(labels)
    assert [cc[i] for i in range(len(v))]==[2*x for x in k], (name,cc,k)
    normals=[(1,2,3),(2,3,7),(3,-2,5),(-5,7,2),(7,1,13),(0,0,1),(0,1,0)]
    for normal in normals:
        projections=sorted(set(dot(normal,x) for x in points))
        width=projections[-1]-projections[0]
        assert width==sum(abs(dot(normal,x)) for x in v)
        direct=Fraction(0)
        for l,r in zip(projections,projections[1:]):
            midpoint=Fraction(l+r,2)
            nsection=sum(1 for a,b in edges if min(dot(normal,a),dot(normal,b))<midpoint<max(dot(normal,a),dot(normal,b)))
            direct+=Fraction((r-l)*nsection,width)
        formula=Fraction(sum(2*k[i]*abs(dot(normal,v[i])) for i in range(len(v))),width)
        assert direct==formula,(name,normal,direct,formula)
        if len(set(k))==1:assert formula==2*k[0]
        if name=='unbalanced_prism' and normal==(0,0,1):assert formula==6
        if name=='unbalanced_prism' and normal==(0,1,0):assert formula==4
    print(name,'generators',len(v),'vertices',len(set(point for e in edges for point in e)),
          'edges',len(edges),'zone_r',[2*x for x in k],'normal_checks',len(normals))
    return len(normals)

if __name__=='__main__':
    generic=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]
    A=[(1,1,0),(1,2,0),(2,3,0)]
    B=[(1,0,1),(1,0,2),(2,0,3)]
    cases=[('generic_four',generic,[3]*4),
           ('balanced_two_planes',A+B,[4]*6),
           ('unbalanced_prism',A+[(0,0,1)],[2,2,2,3])]
    n=0
    for name,v,k in cases:n+=eval_case(name,v,k)
    for d,m in [(3,3),(3,4),(3,6),(4,4),(4,7),(5,8)]:
        regions=2*sum(comb(m-2,j) for j in range(d-1))
        assert regions>=2**(d-1)
        if d==m:assert regions==2**(d-1)
    print('ZONOTOPE_OFFSET_MEAN_OK cases=3 normals='+str(n)+' generic_region_checks=6')
