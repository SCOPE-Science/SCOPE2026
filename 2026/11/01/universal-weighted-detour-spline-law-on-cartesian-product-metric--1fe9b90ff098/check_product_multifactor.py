"""Exact rational consistency checks of the all-factor metric and law."""
from fractions import Fraction as F
from itertools import product
from check_product_detour import distances, point_dist


def product_family(factors):
    ranges=[range(n) for n,e in factors]
    vertices=list(product(*ranges))
    idx={a:i for i,a in enumerate(vertices)}
    ee=[]
    for i,(n,edges) in enumerate(factors):
        for j,(u,v,w) in enumerate(edges):
            for layer in product(*[range(q) for k,(q,_) in enumerate(factors) if k!=i]):
                aa=list(layer);bb=list(layer);aa.insert(i,u);bb.insert(i,v)
                ee.append((idx[tuple(aa)],idx[tuple(bb)],F(w),i,j,layer))
    return ee

def amb(ex,x,ey,y,factors,ds):
    di,ei,ly=ex[3:6];dj,ej,lo=ey[3:6]
    ans=F(0)
    for i,((n,edges),dd) in enumerate(zip(factors,ds)):
        if i==di and i==dj:
            ans+=point_dist(edges[ei],x,edges[ej],y,dd)
        elif i==di:
            vv=lo[i if i<dj else i-1]
            ans+=point_dist(edges[ei],x,(vv,vv,F(0)),F(0),dd)
        elif i==dj:
            vv=ly[i if i<di else i-1]
            ans+=point_dist(edges[ej],y,(vv,vv,F(0)),F(0),dd)
        else:
            av=ly[i if i<di else i-1]
            bv=lo[i if i<dj else i-1]
            ans+=dd[av][bv]
    return ans

def check(factors):
    vv=1
    for n,e in factors:vv*=n
    ee=product_family(factors)
    d=distances(vv,[(u,v,w) for u,v,w,*_ in ee]);ds=[distances(n,e) for n,e in factors]
    q=(F(1,6),F(1,3),F(3,5),F(4,5))
    c=0
    for ex,ey in product(ee,repeat=2):
        for a,b in product(q,repeat=2):
            x=a*ex[2];y=b*ey[2]
            got=point_dist(ex[:3],x,ey[:3],y,d)
            ambient=amb(ex,x,ey,y,factors,ds)
            delta=2*min(min(x,y),min(ex[2]-x,ex[2]-y)) if ex[3]==ey[3] and ex[4]==ey[4] and ex[5]!=ey[5] else F(0)
            assert got==ambient+delta,(ex,ey,x,y,got,ambient,delta)
            c+=1
    return c,len(ee)

if __name__=='__main__':
    P2=(2,[(0,1,1)])
    P3=(3,[(0,1,1),(1,2,2)])
    T3=(3,[(0,1,1),(1,2,1),(0,2,2)])
    cases=[[P2,P2,P2],[P2,P3,P2],[P2,T3,P2],[P3,P3,P2],[P2,P2,P2,P2]]
    total=0
    for fs in cases:
        c,m=check(fs);total+=c
        print('PASS factors:',[len(x[1]) for x in fs], 'edges=',m, 'comparisons=',c)
    print('TOTAL:',total,'exact-rational full-product comparisons')
