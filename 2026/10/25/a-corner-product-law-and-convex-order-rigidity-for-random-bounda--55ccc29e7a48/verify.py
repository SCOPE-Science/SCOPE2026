"""Reproducibility checks for random boundary polygons; standard library only.

Finite checks support, but cannot establish, limiting probabilistic assertions.
"""
from math import comb, cos, sin, pi, hypot, factorial
from fractions import Fraction
import random


def exact_square_corner(N):
    a=b=Fraction(1)
    L=Fraction(4)
    direct=sum(
        Fraction(comb(N,k)*(-1)**k,L**k)*
        sum(Fraction(comb(k,j), (j+1)*(k-j+1)) for j in range(k+1))
        for k in range(N+1)
    )
    expression=L**2/Fraction((N+1)*(N+2))*(1-2*(1-a/L)**(N+2)+(1-(a+b)/L)**(N+2))
    assert direct==expression,(N,direct,expression)
    return 1


def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(pts):
    pts=sorted(set(pts))
    if len(pts)<=1:return pts
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0:up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]

def area(poly):return abs(sum(poly[j][0]*poly[(j+1)%len(poly)][1]-poly[j][1]*poly[(j+1)%len(poly)][0] for j in range(len(poly)))/2)


def check_hull_formula(poly,N,rng):
    m=len(poly)
    lengths=[hypot(poly[(j+1)%m][0]-p[0],poly[(j+1)%m][1]-p[1]) for j,p in enumerate(poly)]
    L=sum(lengths)
    cuts=[0.]
    for v in lengths:cuts.append(cuts[-1]+v)
    points=[]; sides=[[] for _ in range(m)]
    for k in range(N):
        t=rng.random()*L
        j=next(j for j in range(m) if cuts[j]<=t<cuts[j+1]);u=(t-cuts[j])/lengths[j]
        pt=((1-u)*poly[j][0]+u*poly[(j+1)%m][0],(1-u)*poly[j][1]+u*poly[(j+1)%m][1])
        points.append(pt);sides[j].append(u*lengths[j])
    if not all(sides):return 0
    predicted=0.
    for j in range(m):
        before=max(sides[(j-1)%m]);after=min(sides[j])
        U=lengths[(j-1)%m]-before;V=after
        v0=poly[(j-1)%m];v1=poly[j];v2=poly[(j+1)%m]
        cos_theta=((v0[0]-v1[0])*(v2[0]-v1[0])+(v0[1]-v1[1])*(v2[1]-v1[1]))/(lengths[(j-1)%m]*lengths[j])
        sin_theta=(1-cos_theta*cos_theta)**.5
        predicted+=0.5*sin_theta*U*V
    direct=area(poly)-area(hull(points))
    assert abs(predicted-direct)<3e-8,(predicted,direct)
    return 1


def main():
    rng=random.Random(512729)
    exact=sum(exact_square_corner(k) for k in range(0,16))
    tests=0
    examples=[[(0.,0.),(2.,0.),(2.2,1.3),(0.1,1.1)],[(0.,0.),(3.,0.),(1.,2.)],[(0.,0.),(1.,0.),(1.2,1.1),(0.2,1.7),(-0.3,1.)]]
    for poly in examples:
        assert area(poly)>0
        for n in (9,30,90,150):
            for _ in range(90): tests+=check_hull_formula(poly,n,rng)
    samples=140000
    vals=[]
    for _ in range(samples):
        vals.append(sum(.5*(-__import__('math').log(max(1e-16,rng.random())))*(-__import__('math').log(max(1e-16,rng.random()))) for j in range(4)))
    mu=sum(vals)/len(vals);var=sum((x-mu)**2 for x in vals)/(len(vals)-1)
    assert abs(mu-2)<.035,(mu,var)
    assert abs(var-3)<.16,(mu,var)
    print(f'VERIFY_OK exact_integrals={exact} hull_geometry={tests} product_samples={samples} moment_estimates=({mu:.5f},{var:.5f})')

if __name__=='__main__':main()
