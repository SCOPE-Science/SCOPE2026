"""Standalone finite checks for the triangle normal-multiplicity area formula.
The analytic proof, not these tests, establishes the theorem.
"""
import math
import random
from fractions import Fraction

def halfplane_clip(poly, point, normal):
    def f(p):return (p[0]-point[0])*normal[0]+(p[1]-point[1])*normal[1]
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        fa,fb=f(a),f(b)
        if fa>=-1e-13:out.append(a)
        if (fa>1e-13 and fb<-1e-13) or (fa<-1e-13 and fb>1e-13):
            w=fa/(fa-fb)
            out.append((a[0]+w*(b[0]-a[0]),a[1]+w*(b[1]-a[1])))
    return out

def polygon_area(poly):
    return abs(sum(x1*y2-y1*x2 for (x1,y1),(x2,y2) in zip(poly,poly[1:]+poly[:1])))/2

def analytic_fraction(A,b,c):
    k=-math.cos(A)
    return (1-k*k)/(1+k*k+k*(b/c+c/b)) if k>0 else 1.

def numerical_fraction(A,b,c):
    B=(c,0.0)
    C=(b*math.cos(A),b*math.sin(A))
    T=[(0.0,0.0),B,C]
    # orthogonal projections onto AB and AC must lie beyond the obtuse vertex A
    P=halfplane_clip(T,(0.0,0.0),(1.0,0.0))
    P=halfplane_clip(P,(0.0,0.0),C)
    return polygon_area(P)/polygon_area(T)

def normal_count(y,vertices):
    minima=0
    for a,b in zip(vertices,vertices[1:]+vertices[:1]):
        vx,vy=b[0]-a[0],b[1]-a[1]
        t=((y[0]-a[0])*vx+(y[1]-a[1])*vy)/(vx*vx+vy*vy)
        if 1e-10<t<1-1e-10:minima+=1
    assert minima in (2,3)
    return 2*minima

assert Fraction(1,1)-Fraction(9,25)==Fraction(16,25)
k=Fraction(3,5)
q=Fraction(2,3)
assert (1-k*k)/(1+k*k+k*(q+1/q)) == Fraction(32,133)
assert (1-k*k)/(1+k*k+2*k) == Fraction(1,4)

rng=random.Random(3427199)
N=0
for Adeg in [90,94,101,117,138,169]:
    A=math.radians(Adeg)
    for b,c in [(1.,1.),(2.,3.),(5.,1.),(.5,10.)]:
        theory=analytic_fraction(A,b,c)
        numeric=numerical_fraction(A,b,c)
        assert abs(theory-numeric)<2e-12,(Adeg,b,c,theory,numeric)
        k=-math.cos(A)
        if k>0:
            fmax=(1-k)/(1+k)
            discrepancy=fmax/theory-1
            exact_stability=4*k/((1+k)**2)*math.sinh(.5*math.log(b/c))**2
            assert abs(discrepancy-exact_stability)<1e-11
        if Adeg in (90,117,169) and (b,c) in ((1.,1.),(2.,3.)):
            tri=[(0.,0.),(c,0.),(b*math.cos(A),b*math.sin(A))]
            n=12000; count6=0
            for _ in range(n):
                r,s=rng.random(),rng.random()
                if r+s>1: r,s=1-r,1-s
                y=(r*tri[1][0]+s*tri[2][0],r*tri[1][1]+s*tri[2][1])
                count6 += (normal_count(y,tri)==6)
            assert abs(count6/n-theory)<.025,(Adeg,b,c,count6/n,theory)
        N+=1
for k in [1e-2,1e-3,1e-4]:
    expected={"bounded":1.0,"intermediate":0.5,"extreme":0.0}
    for name,q in [("bounded",1.0),("intermediate",1/k),("extreme",1/k**2)]:
        f=(1-k*k)/(1+k*k+k*(q+1/q))
        assert abs(f-expected[name])<.025,(k,name,f)
print('PASSED:',N,'angle-ratio profiles, exact rational case checks, direct clipped-area integration, 72000 independent normal counts and 9 boundary-layer cases')
