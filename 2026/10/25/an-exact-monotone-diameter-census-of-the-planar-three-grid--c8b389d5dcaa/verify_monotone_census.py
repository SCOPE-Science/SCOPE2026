"""Exact complete enumeration of planar lattice polygon monotone diameter for [0,3]^2."""
from collections import Counter
from math import gcd
POINTS=tuple((x,y) for x in range(4) for y in range(4))

def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(points):
    points=sorted(points)
    if len(points)<3:return ()
    low=[]; high=[]
    for p in points:
        while len(low)>=2 and cross(low[-2],low[-1],p)<=0:low.pop()
        low.append(p)
    for p in points[::-1]:
        while len(high)>=2 and cross(high[-2],high[-1],p)<=0:high.pop()
        high.append(p)
    return tuple(low[:-1]+high[:-1]) if len(low)+len(high)>=5 else ()

def primitive(u):
    d=gcd(*u)
    return (u[0]//d,u[1]//d)

def half(u): return u[1]>0 or (u[1]==0 and u[0]>0)

def cmp_angle(u,v):
    hu,hv=half(u),half(v)
    if hu!=hv:return -1 if hu else 1
    det=u[0]*v[1]-u[1]*v[0]
    if det>0:return -1
    if det<0:return 1
    return 0

from functools import cmp_to_key

def monotone_diameter(poly,generic_only=False):
    n=len(poly)
    if n<3:return (0,None)
    dirs=set()
    for i in range(n):
        a,b=poly[i],poly[(i+1)%n]
        diff=(b[0]-a[0],b[1]-a[1])
        normal=primitive((diff[1],-diff[0]))
        dirs.add(normal);dirs.add((-normal[0],-normal[1]))
    dirs=sorted(dirs,key=cmp_to_key(cmp_angle))
    best=-1; witness=None
    for j,u in enumerate(dirs):
        v=dirs[(j+1)%len(dirs)]
        su=abs(u[0])+abs(u[1]); sv=abs(v[0])+abs(v[1])
        interior=(u[0]*sv+v[0]*su,u[1]*sv+v[1]*su)
        assert interior!=(0,0) and u[0]*v[1]-u[1]*v[0]>0
        for c in ((interior,) if generic_only else (u,interior)):
            heights=[c[0]*p[0]+c[1]*p[1] for p in poly]
            d=[None]*n
            for i in sorted(range(n),key=lambda i:heights[i],reverse=True):
                out=[d[k]+1 for k in ((i-1)%n,(i+1)%n) if heights[k]>heights[i]]
                if not out: assert heights[i]==max(heights)
                d[i]=min(out) if out else 0
            m=max(d)
            if m>best:best=m; witness=(c,d,poly)
    return best,witness

if __name__ == '__main__':
    polygons=set()
    for mask in range(1<<len(POINTS)):
        if mask.bit_count()<3:continue
        poly=hull(POINTS[i] for i in range(16) if (mask>>i)&1)
        if len(poly)>=3:polygons.add(poly)
    assert len(polygons)==2719,len(polygons)
    counts=Counter();by_n=Counter();generic_counts=Counter();bests=[]
    for poly in polygons:
        diam,w=monotone_diameter(poly)
        generic=monotone_diameter(poly,True)[0]
        assert diam==generic,(poly,diam,generic)
        generic_counts[generic]+=1
        counts[diam]+=1;by_n[(len(poly),diam)]+=1
        if diam>=4:bests.append((poly,w))
    assert counts=={1:516,2:1686,3:516,4:1},counts
    assert by_n=={(3,1):516,(4,2):1038,(5,2):648,(5,3):200,(6,3):292,(7,3):24,(8,4):1},by_n
    assert generic_counts==counts
    assert len(bests)==1,bests
    assert bests[0][0]==((0,1),(1,0),(2,0),(3,1),(3,2),(2,3),(1,3),(0,2))
    print('CERT_OK polygons',len(polygons),'diameters',sorted(counts.items()),'by_vertices',sorted(by_n.items()))
    print('UNIQUE_EXTREMAL',bests[0])
