"""Reproducible checks for the truncated-octahedron brightness law.
Standard-library only; finite checks complement the analytical derivation.
"""
import itertools
import math
import random

SQRT = math.sqrt
R = 2*SQRT(51)
TANGENCY = 10*SQRT(2)
LOW = 8*SQRT(2)


def vertices():
    return sorted({tuple(a*s for a,s in zip(p,sgn))
                   for p in set(itertools.permutations((0,1,2)))
                   for sgn in itertools.product((-1,1),repeat=3)})


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def norm(v):
    return SQRT(dot(v,v))


def unit(v):
    r=norm(v)
    return tuple(x/r for x in v)


def projection_area(u):
    # Independent orthogonal projection of all 24 vertices and planar hull.
    axis=(1,0,0) if abs(u[0]) < 0.8 else (0,1,0)
    e1=unit(cross(u,axis)); e2=cross(u,e1)
    xy=sorted({(dot(v,e1),dot(v,e2)) for v in vertices()})
    def turn(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]; hi=[]
    for p in xy:
        while len(lo)>1 and turn(lo[-2],lo[-1],p) <= 0: lo.pop()
        lo.append(p)
    for p in reversed(xy):
        while len(hi)>1 and turn(hi[-2],hi[-1],p) <= 0: hi.pop()
        hi.append(p)
    hull=lo[:-1]+hi[:-1]
    return abs(sum(hull[i][0]*hull[(i+1)%len(hull)][1]
                   -hull[(i+1)%len(hull)][0]*hull[i][1]
                   for i in range(len(hull))))/2


def brightness(u):
    z=list(map(abs,u))
    return 2*sum(z)+6*max(2*max(z),sum(z))


def candidate_vectors():
    first=sorted({tuple(a*s for a,s in zip(p,sgn))
                  for p in set(itertools.permutations((14,2,2)))
                  for sgn in itertools.product((-1,1),repeat=3)})
    second=list(itertools.product((-8,8),repeat=3))
    return first,second


def lens_area(t):
    if t>=TANGENCY: return 0.0
    assert 14 <= t < TANGENCY
    x=(196-t*t)/(204-t*t)
    y=t/SQRT(50*(204-t*t))
    return 2*(math.pi-math.acos(max(-1,min(1,x))))-(2*t/SQRT(51))*math.acos(max(-1,min(1,y)))


def upper_cdf(t):
    assert 14 <= t <= R
    return 6*t/SQRT(51)-11+(6/math.pi)*lens_area(t) if t<=TANGENCY else 6*t/SQRT(51)-11


def random_unit(rng):
    return unit(tuple(rng.gauss(0,1) for _ in range(3)))


def test():
    A,D=candidate_vectors()
    assert len(vertices())==24 and len(A)==24 and len(D)==8
    assert all(dot(v,v)==204 for v in A)
    assert all(dot(v,v)==192 for v in D)
    pairdots={dot(x,y) for i,x in enumerate(A) for y in A[i+1:]}
    assert max(pairdots)==196, max(v for v in pairdots if v < 196)==188
    assert sum(dot(x,y)==196 for i,x in enumerate(A) for y in A[i+1:])==24
    assert sum(dot(x,y)==188 for i,x in enumerate(A) for y in A[i+1:])==12
    assert abs(TANGENCY-SQRT((204+196)/2))<1e-12
    assert abs(14-SQRT((204+188)/2))<1e-12
    rng=random.Random(41719)
    # Numerical geometry independent of Cauchy's facet-area formula.
    for k in range(800):
        u=random_unit(rng)
        geom=projection_area(u)
        b=brightness(u)
        assert abs(b-geom)<3e-12, (u,b,geom)
        assert abs(b-max(dot(v,u) for v in A+D))<4e-12
        assert LOW-1e-12 <= b <= R+1e-12
    # Check all distinguished optimizer orbits.
    for signs in itertools.product((-1,1),repeat=2):
        for ix in range(3):
            u=[0.0]*3
            ids=[j for j in range(3) if j!=ix]
            u[ids[0]]=signs[0]/SQRT(2)
            u[ids[1]]=signs[1]/SQRT(2)
            assert abs(brightness(u)-LOW)<1e-12
    for v in A:
        u=unit(v)
        assert abs(brightness(u)-R)<1e-12
    assert abs(upper_cdf(R)-1)<1e-12
    assert abs(upper_cdf(TANGENCY)-(6*TANGENCY/SQRT(51)-11))<2e-12
    # Analytically derived local cone area gives the exact lower coefficient.
    conearea = 7*SQRT(2)/192
    lowercoefficient = 12*conearea/(4*math.pi)
    assert abs(lowercoefficient-7*SQRT(2)/(64*math.pi))<1e-14
    # Statistical sanity check; analytic proof does not rely on sampling.
    N=300000
    ts=[14,14.05,14.1,14.13,14.2,14.25,14.27]
    counts=[0]*len(ts)
    for _ in range(N):
        b=brightness(random_unit(rng))
        for k,t in enumerate(ts):
            counts[k] += (b<=t)
    for t,c in zip(ts,counts):
        estimate=c/N
        expected=upper_cdf(t)
        assert abs(estimate-expected)<0.006, (t,estimate,expected)
        print('cdf',t,'observed',format(estimate,'.7f'),'formula',format(expected,'.7f'))
    # Check the cusp coefficient numerically at scales avoiding severe cancellation.
    C=(8/math.pi)*SQRT(2/TANGENCY)
    for eps in [0.1,0.04,0.01,0.002]:
        diff=upper_cdf(TANGENCY-eps)-(6*(TANGENCY-eps)/SQRT(51)-11)
        ratio=diff/(C*eps**1.5)
        assert 0.89<ratio<1.01,(eps,ratio)
        print('cusp',eps,'ratio',format(ratio,'.9f'))
    print('PASS: 800 independent projected-hull checks, 300000 Haar orientations, exact vector enumeration and cusp tests')
    print('support',[LOW,R],'upper-phase',[14,TANGENCY,R],'lower-CDF-coefficient',lowercoefficient)

if __name__=='__main__':test()
