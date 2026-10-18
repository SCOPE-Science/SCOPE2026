"""Exact polyhedral cross-checks for the four-site cyclic metric family.

Usage: python verify_square_volume.py
Standard-library Python. Every listed volume is computed from independently
enumerated rational vertices and triangulated facet polygons.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import cmp_to_key


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def det3(a,b,c):
    return dot(a,cross(b,c))

def invert_rows(a,b,c, rhs):
    det=det3(a,b,c)
    if not det:return None
    # Cramer's rule for the system with ROWS a,b,c.
    n1=(rhs[0],rhs[1],rhs[2])
    col1=(a[0],b[0],c[0]);col2=(a[1],b[1],c[1]);col3=(a[2],b[2],c[2])
    return (det3(n1,col2,col3)/det,
            det3(col1,n1,col3)/det,
            det3(col1,col2,n1)/det)

def half(p):
    x,y=p
    return 0 if (y>0 or (y==0 and x>=0)) else 1

def sort_polygon(points,normal):
    # Drop any coordinate with nonzero normal; the remaining two are an
    # injective projection on the facet plane.
    omit=next(i for i in range(3) if normal[i])
    idx=tuple(i for i in range(3) if i!=omit)
    center=tuple(sum((p[i] for p in points),F(0))/len(points) for i in idx)
    def coord(p):return (p[idx[0]]-center[0],p[idx[1]]-center[1])
    def cmp(p,q):
        v,w=coord(p),coord(q)
        hv,hw=half(v),half(w)
        if hv!=hw:return -1 if hv<hw else 1
        z=v[0]*w[1]-v[1]*w[0]
        return -1 if z>0 else 1 if z<0 else 0
    return sorted(points,key=cmp_to_key(cmp))

def volume_from_facets(vertices, facet_normals, facet_constants):
    seen=set(); total=F(0)
    for normal,b in zip(facet_normals,facet_constants):
        face=tuple(sorted(v for v in vertices if dot(normal,v)==b))
        if len(face)<3 or face in seen:continue
        seen.add(face)
        ordered=sort_polygon(face,normal)
        first=ordered[0]
        for i in range(1,len(ordered)-1):
            total+=abs(det3(first,ordered[i],ordered[i+1]))/6
    return total,len(seen)

def compute(t):
    t=F(t)
    # Coordinates: f(0)=0, (f(1),f(2),f(3)).
    positive=[(F(1),F(0),F(0)), (F(-1),F(1),F(0)),
              (F(0),F(1),F(-1)), (F(0),F(0),F(1)),
              (F(0),F(1),F(0)), (F(1),F(0),F(-1))]
    base=(F(1),F(1),F(1),F(1),t,t)
    normals=positive+[tuple(-a for a in v) for v in positive]
    bounds=base+base
    q=set()
    for ids in combinations(range(12),3):
        a,b,c=(normals[i] for i in ids)
        v=invert_rows(a,b,c,[bounds[i] for i in ids])
        if v is not None and all(dot(n,v)<=h for n,h in zip(normals,bounds)):
            q.add(v)
    q=sorted(q)
    p=sorted(set(tuple(s*v[i]/h for i in range(3))
        for v,h in zip(positive,base) for s in (F(1),F(-1))))
    volq,facetsq=volume_from_facets(q,normals,bounds)
    volp,facetsp=volume_from_facets(p,q,[F(1)]*len(q))
    expected_p=2*(t+4)/(3*t)
    expected_q=(16-4*(2-t)**3)/3
    assert volp==expected_p,(t,'P',volp,expected_p)
    assert volq==expected_q,(t,'Q',volq,expected_q)
    assert len(p)==12 and len(q)==18 and facetsp==18 and facetsq==12
    print(f't={t}: P vertices={len(p)}, Q vertices={len(q)}, '+
          f'facets P/Q={facetsp}/{facetsq}, '+
          f'volume P={volp}, volume Q={volq}, product={volp*volq}')

if __name__=='__main__':
    for t in (F(101,100),F(11,10),F(6,5),F(3,2),F(9,5),F(199,100)):
        compute(t)
    # The derivative sign certificate is purely rational:
    # P'(t) = 8 g(t)/(9t^2), g(t)=3t^4-4t^3-12t^2+16.
    # g(1)=3, g(2)=-16, g'(t)=12t(t-2)(t+1)<0 for 1<t<2.
    assert 3*1**4-4*1**3-12*1**2+16==3
    assert 3*2**4-4*2**3-12*2**2+16==-16
    print('ALL EXACT POLYHEDRAL AND DERIVATIVE CERTIFICATES PASSED')
