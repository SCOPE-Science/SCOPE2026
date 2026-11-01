"""Exact-rational, standalone checks of the two-vertex tetrahedral cap formula.

Usage: python verify_double_caps.py. Python 3 standard library only.
This is a finite test, not a replacement for the analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd


def lcm(a,b):
    return a*b//gcd(a,b)


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0])


def sub(x,y):
    return tuple(a-b for a,b in zip(x,y))


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def det(a,b,c):
    return dot(a,cross(b,c))


def convex_hull_2d(points):
    # Points are tuples ((x,y), original_integer_3d_vertex).
    pts=sorted({xy:v for xy,v in points}.items())
    if len(pts)<3:
        raise AssertionError('degenerate facet')
    def z(o,a,b):
        return (a[0][0]-o[0][0])*(b[0][1]-o[0][1])-(a[0][1]-o[0][1])*(b[0][0]-o[0][0])
    lower=[]
    for p in pts:
        while len(lower)>=2 and z(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>=2 and z(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    poly=lower[:-1]+upper[:-1]
    return [v for _,v in poly]


def exact_polytope_volume(vertices):
    # Integer coordinates; origin must be strictly interior.
    vertices=sorted(set(vertices));m=len(vertices)
    faces={}
    for ia,ib,ic in combinations(range(m),3):
        a,b,c=vertices[ia],vertices[ib],vertices[ic]
        n=cross(sub(b,a),sub(c,a))
        if n==(0,0,0):continue
        h=dot(n,a)
        vals=[dot(n,v)-h for v in vertices]
        if min(vals)<0 and max(vals)>0:continue
        I=tuple(j for j,w in enumerate(vals) if w==0)
        if len(I)<3:continue
        faces[I]=n
    if not faces:raise AssertionError('No facets')
    num6=0
    for I,n in faces.items():
        k=max(range(3),key=lambda k:abs(n[k]))
        axes=[i for i in range(3) if i!=k]
        poly=convex_hull_2d([((vertices[j][axes[0]],vertices[j][axes[1]]),vertices[j]) for j in I])
        p0=poly[0]
        for j in range(1,len(poly)-1):
            di=abs(det(p0,poly[j],poly[j+1]))
            if di==0:raise AssertionError('zero triangle determinant')
            num6+=di
    return F(num6,6),len(faces)


def vertices_of_cap(s,t):
    assert s>=0 and t>=0 and s+t<=1
    s,t=F(s),F(t)
    v=[(F(0),F(0),F(0)),(F(0),F(0),F(1)),
       (1-s,F(0),F(0)),(1-s,s,F(0)),(1-s,F(0),s),
       (F(0),1-t,F(0)),(t,1-t,F(0)),(F(0),1-t,t)]
    return sorted(set(v))


def difference_volume(s,t):
    vert=vertices_of_cap(s,t)
    D=sorted(set(tuple(a[i]-b[i] for i in range(3)) for a in vert for b in vert))
    den=1
    for v in D:
        for x in v:
            den=lcm(den,x.denominator)
    integer=[tuple(int(x*den) for x in v) for v in D]
    vol,facets=exact_polytope_volume(integer)
    return vol/den**3,facets,len(integer)


def expected(s,t):
    c=s**3+t**3
    V=(1-c)/6
    N=(1-t*t)*(1-s)+(1-s*s)*(1-t)+(1-s*s-t*t)
    R=N/(1-c)
    DK=2*V+6*(R*V)
    return V,R,DK


def run():
    cases=[(F(0),F(0)),(F(1,5),F(3,10)),(F(1,4),F(1,4)),
           (F(1,2),F(1,2)),(F(1,3),F(2,3)),(F(1,10),F(9,10)),
           (F(0),F(2,3)),(F(1,2),F(0)),(F(1,7),F(2,7)),
           (F(1,6),F(1,3)),(F(3,8),F(1,4))]
    for s,t in cases:
        V,R,DK=expected(s,t)
        checked,facets,n= difference_volume(s,t)
        assert checked==DK,(s,t,checked,DK)
        # Exact lower-bound factorization at the physical cap parameters.
        u,v=s+t,s*t;c=s**3+t**3
        identity=(R-F(5,3))-(1-u)*((1-u)*(5*u+4)+12*v)/(3*(1-c))
        assert identity==0
        # Direct reconstruction of ratio from the difference-body identity.
        assert R==(checked-2*V)/(6*V)
        print('CAP',str(s),str(t),'vertices_DK',n,'facets_DK',facets,'ratio',str(R))
    # Exact equal-volume endpoint comparisons for rational pairs in a bounded grid.
    comparisons=0
    for i in range(1,12):
        for j in range(0,12-i):
            s,t=F(i,12),F(j,12)
            if s+t>1:continue
            c=s**3+t**3
            V,R,DK=expected(s,t)
            u=s+t
            assert F(5,3)<=R
            # For fixed c, monotonicity in u proven analytically; here
            # check the algebraic derivative numerator and its bound.
            dN= -1-F(4,3)*u+u*u+4*c/(3*u*u)
            assert dN<=u*u-1
            assert dN<0
            comparisons+=1
    print('VERIFY_OK exact difference-body polytope reconstruction:',len(cases),
          'independent instances;',comparisons,'monotonicity/identity instances')

if __name__=='__main__':run()
