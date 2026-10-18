"""Reproducible geometric and probabilistic checks for a polygon boundary-area law.

Dependencies: Python 3.9+ standard library. Run: python checker.py
The simulations corroborate but do not establish the infinite-sample theorem.
"""
import math
import random


def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def area(poly):
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1])))/2


def hull(points):
    a=sorted(set(points))
    if len(a)<3:return a
    lo=[]
    for p in a:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(a):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]


def setup(vertices):
    m=len(vertices)
    edges=[(vertices[(i+1)%m][0]-vertices[i][0],vertices[(i+1)%m][1]-vertices[i][1]) for i in range(m)]
    lengths=[math.hypot(*v) for v in edges]
    L=sum(lengths)
    unit=[(v[0]/s,v[1]/s) for v,s in zip(edges,lengths)]
    sin_theta=[abs(unit[(i-1)%m][0]*unit[i][1]-unit[(i-1)%m][1]*unit[i][0]) for i in range(m)]
    return m,lengths,L,unit,sin_theta


def sample(vertices,n,rng):
    m,lengths,L,unit,sines=setup(vertices)
    arrivals=[];points=[]
    for j in range(n):
        z=rng.random()*L
        for i,le in enumerate(lengths):
            if z<le or i==m-1:break
            z-=le
        points.append((vertices[i][0]+z*unit[i][0],vertices[i][1]+z*unit[i][1]))
        arrivals.append((i,z))
    return points,arrivals


def corner_area(vertices,arrivals):
    m,lengths,L,unit,sines=setup(vertices)
    bins=[[z for i,z in arrivals if i==j] for j in range(m)]
    if not all(bins):return None
    start=[min(b) for b in bins]
    end=[le-max(b) for le,b in zip(lengths,bins)]
    return sum(sines[i]*end[(i-1)%m]*start[i]/2 for i in range(m))


def check():
    rng=random.Random(740061)
    polygons=[[(0,0),(1,0),(1,1),(0,1)],
              [(0,0),(2,0),(1.3,1.1),(0.1,0.8)],
              [(0,0),(1.4,0),(1.6,0.7),(0.8,1.5),(-0.2,0.9)]]
    identities=0
    for v in polygons:
        original=area(v)
        m,lengths,L,unit,sin_theta=setup(v)
        assert original>0
        for _ in range(100):
            pts,arr=sample(v,200,rng)
            c=corner_area(v,arr)
            assert c is not None
            geom=original-area(hull(pts))
            assert abs(c-geom)<1e-9*max(1,original),(v,c,geom)
            identities+=1
        n=700
        replicates=600
        vals=[]
        for _ in range(replicates):
            pts,arr=sample(v,n,rng)
            vals.append(n*n*(original-area(hull(pts)))/(L*L))
        target=sum(sin_theta)/2
        assert abs(sum(vals)/replicates-target)<0.34,(target,sum(vals)/replicates)
        print('polygon m=%d; scaled empirical mean=%.5f; limit=%.5f'%(m,sum(vals)/replicates,target))
    # Product-exponential moment checks, independent of hull simulation.
    m,lengths,L,unit,sines=setup(polygons[0]); c=[s/2 for s in sines]
    vals=[]
    for _ in range(75000):
        vals.append(sum(w*(-math.log(rng.random()))*(-math.log(rng.random())) for w in c))
    mu=sum(c);var=3*sum(w*w for w in c)
    empirical=sum(vals)/len(vals)
    empirical_var=sum((x-empirical)**2 for x in vals)/len(vals)
    assert abs(empirical-mu)<.09
    assert abs(empirical_var-var)<.3
    print('independent product-exponential mean/variance',empirical,empirical_var,'targets',mu,var)
    print('PASS: %d exact corner-area identity tests, 3 large-sample mean checks, 2 limit moment checks'%identities)


if __name__=='__main__':check()
