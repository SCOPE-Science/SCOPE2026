"""Independent finite checks for boundary-sampled polygon area-loss formulas.
All calculations use Python's standard library; geometric hulls use monotone chain.
"""
import bisect
import math
import random


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1] -
                   poly[i][1]*poly[(i+1)%len(poly)][0]
                   for i in range(len(poly)))/2) if len(poly)>=3 else 0.


def hull(points):
    points = sorted(set(points))
    if len(points)<3:
        return points
    low=[]; high=[]
    for p in points:
        while len(low)>=2 and cross(low[-2],low[-1],p)<=0:low.pop()
        low.append(p)
    for p in reversed(points):
        while len(high)>=2 and cross(high[-2],high[-1],p)<=0:high.pop()
        high.append(p)
    return low[:-1]+high[:-1]


def setup(v):
    m=len(v)
    assert m>=3 and all(cross(v[i],v[(i+1)%m],v[(i+2)%m])>0 for i in range(m))
    lengths=[math.dist(v[i],v[(i+1)%m]) for i in range(m)]
    b=[0.]
    for L in lengths:b.append(b[-1]+L)
    P=b[-1]
    ss=[cross(v[(i-1)%m],v[i],v[(i+1)%m])/(lengths[i-1]*lengths[i]) for i in range(m)]
    assert all(s>0 for s in ss)
    return lengths,b,P,ss


def draw(v,lengths,b,P,rng,N):
    m=len(v)
    pts=[]
    mins=[math.inf]*m; maxs=[-math.inf]*m
    for _ in range(N):
        u=rng.random()*P
        i=min(m-1,bisect.bisect_right(b,u)-1)
        x=u-b[i]
        t=x/lengths[i]
        pts.append((v[i][0]*(1-t)+v[(i+1)%m][0]*t,
                    v[i][1]*(1-t)+v[(i+1)%m][1]*t))
        mins[i]=min(mins[i],x);maxs[i]=max(maxs[i],x)
    return pts,mins,maxs


def rational_mean(v,lengths,P,ss,N):
    total=0.
    m=len(v)
    for i in range(m):
        a=lengths[i-1]/P;b=lengths[i]/P
        bracket=1-(1-a)**(N+2)-(1-b)**(N+2)+max(0.,1-a-b)**(N+2)
        total+=ss[i]*bracket
    return P*P*total/(2*(N+1)*(N+2))


def check():
    rng=random.Random(20261019)
    polygons=[[(0.,0.),(3.,0.),(.4,2.)],
              [(0.,0.),(2.,0.),(3.,1.),(2.,2.),(0.,1.5)],
              [(math.cos(t*2*math.pi/7),math.sin(t*2*math.pi/7)) for t in range(7)]]
    geometric=0
    for v in polygons:
        L,b,P,ss=setup(v)
        full=area(v)
        for N in [max(3,len(v)),len(v)+3,30,60]:
            for _ in range(500):
                pts,mins,maxs=draw(v,L,b,P,rng,N)
                deficit=full-area(hull(pts))
                assert -1e-9<=deficit<=full+1e-9
                if all(x!=math.inf for x in mins):
                    caps=sum(.5*ss[i]*(L[i-1]-maxs[i-1])*mins[i]
                             for i in range(len(v)))
                    assert abs(caps-deficit)<2e-9,(v,N,caps,deficit)
                    geometric+=1
    assert geometric>3000
    print('INDEPENDENT_MONOTONE_CHAIN_AND_CORNER_TRIANGLES_OK',geometric)

    # Independent finite-N Monte Carlo of actual missing areas, not capped-gap surrogates.
    for v,N,B in [(polygons[0],100,12000),(polygons[1],120,12000),(polygons[2],140,12000)]:
        L,b,P,ss=setup(v)
        full=area(v)
        observed=[]
        for _ in range(B):
            pts,_,_=draw(v,L,b,P,rng,N)
            observed.append(full-area(hull(pts)))
        exact_proxy=rational_mean(v,L,P,ss,N)
        analytic=P*P*sum(ss)/(2*(N+1)*(N+2))
        mean=sum(observed)/B
        error_bound=P*P*sum(ss[i]*((1-L[i-1]/P)**(N+2)+(1-L[i]/P)**(N+2)) for i in range(len(v)))/(2*(N+1)*(N+2))
        assert abs(exact_proxy-analytic)<=error_bound+1e-14
        assert abs(mean-analytic)/analytic<0.06,(mean,analytic)
        weights=[P*P*s/2 for s in ss]
        asymp_var=3*sum(w*w for w in weights)
        norm=[N*N*d for d in observed]
        samplevar=sum((x-sum(norm)/B)**2 for x in norm)/(B-1)
        assert abs(samplevar-asymp_var)/asymp_var<0.19,(samplevar,asymp_var)
        print('FINITE_MEAN_AND_LIMIT_VARIANCE_MONTE_CARLO_OK',len(v),N,B,round(mean/analytic,5),round(samplevar/asymp_var,5))

    # Independent probability check for the product of two unit exponentials.
    Z=[]
    for _ in range(140000):
        e=-math.log(rng.random());f=-math.log(rng.random())
        Z.append(e*f)
    mean=sum(Z)/len(Z)
    var=sum((z-mean)**2 for z in Z)/(len(Z)-1)
    assert abs(mean-1)<0.03 and abs(var-3)<0.18,(mean,var)
    print('UNIT_EXPONENTIAL_PRODUCT_MOMENTS_OK',round(mean,5),round(var,5))
    print('ALL_BOUNDARY_HULL_AREA_CHECKS_OK')

if __name__=='__main__':check()
