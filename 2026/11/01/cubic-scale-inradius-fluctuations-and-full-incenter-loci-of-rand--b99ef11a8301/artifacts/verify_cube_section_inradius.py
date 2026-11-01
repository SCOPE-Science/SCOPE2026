"""Separate finite geometry and probability diagnostics for random cube slices.
Run: python3 artifacts/verify_cube_section_inradius.py (Python standard library).
Finite checks support, but do not prove, the all-dimensional statements.
"""
from itertools import product
from math import acos, asin, atan2, cos, erf, exp, gamma, hypot, isclose, pi, sin, sqrt
from random import Random


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def section_polygon(normal):
    # Literal intersections with all 12 cube edges; no use of inradius formula.
    u=normal
    points=[]
    for i in range(3):
        for signs in product((-1.0,1.0),repeat=2):
            v=[0.0]*3
            rem=[j for j in range(3) if j!=i]
            for j,s in zip(rem,signs): v[j]=s
            v[i]=-sum(u[j]*v[j] for j in rem)/u[i]
            if abs(v[i])<1-1e-9:
                points.append(tuple(v))
    anchor=(1.0,0.0,0.0)
    if abs(dot(anchor,u))>.9: anchor=(0.,1.,0.)
    v=[anchor[i]-dot(anchor,u)*u[i] for i in range(3)]
    vl=sqrt(dot(v,v));v=[x/vl for x in v]
    w=(u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
    p2=[(dot(p,v),dot(p,w)) for p in points]
    p2.sort(key=lambda p:atan2(p[1],p[0]))
    return p2


def centered_inradius_from_edges(poly):
    return min(abs(p[0]*q[1]-p[1]*q[0])/hypot(p[0]-q[0],p[1]-q[1]) for p,q in zip(poly,poly[1:]+poly[:1]))


def claimed_inradius(u):
    return 1.0/sqrt(1.0-min(x*x for x in u))


def d2_cdf(r):
    if r<=1: return 0.
    if r>=sqrt(2):return 1.
    return 1.-2./pi*asin(2./(r*r)-1.)


def survival_dirichlet_d2(r,panels=8000):
    a=1-1/(r*r)
    s=1-2*a
    f=lambda y: 1/sqrt((a+s*y)*(a+s*(1-y)))
    n=panels
    h=1/n
    acc=f(0)+f(1)
    for k in range(1,n):acc+=(4 if k%2 else 2)*f(k*h)
    return (s/pi)*h*acc/3


def gaussian_sample_inradius(d,rng):
    z=[rng.gauss(0,1) for _ in range(d)]
    return 1/sqrt(1-min(v*v for v in z)/sum(v*v for v in z))


def run():
    rng=Random(20261028)
    trials=0
    for _ in range(400):
        z=[rng.gauss(0,1) for _ in range(3)]
        n=sqrt(dot(z,z));u=tuple(v/n for v in z)
        if min(abs(v) for v in u)<.001:continue
        polygon=section_polygon(u)
        assert len(polygon) in (4,6),len(polygon)
        literal=centered_inradius_from_edges(polygon)
        claimed=claimed_inradius(u)
        assert abs(literal-claimed)<2e-10,(literal,claimed,u)
        trials+=1
    assert trials>=390

    # An independent quadrature of the Dirichlet integral in dimension 2.
    for r in (1.005,1.03,1.08,1.16,1.30,1.39):
        calc=survival_dirichlet_d2(r)
        exact=1-d2_cdf(r)
        assert abs(calc-exact)<3e-8,(r,calc,exact)

    # Measure the random radius directly from normal components.
    for d in (2,3,6,15):
        samples=9000
        values=sorted(gaussian_sample_inradius(d,rng) for _ in range(samples))
        assert 1 < values[0] and values[-1]<sqrt(d/(d-1))
        for p in (0.2,0.5,0.8):
            r=values[int(p*samples)]
            if d==2:
                assert abs(d2_cdf(r)-p)<.025

    # Scaling check of the cubic-order excess law and its first moment.
    d=800
    vals=[d**3*(gaussian_sample_inradius(d,rng)-1) for _ in range(5000)]
    mean=sum(vals)/len(vals)
    assert abs(mean-pi/2)<.16,(mean,pi/2)
    median=sorted(vals)[len(vals)//2]
    expected_median=pi/4*(0.6931471805599453)**2
    assert abs(median-expected_median)<.10,(median,expected_median)
    print('CUBE_SECTION_INRADIUS_CHECKS_OK', 'polygon_cases',trials,'d2_quadratures',6,'random_radii',36000,'asymptotic_samples',5000,'mean',round(mean,6),'median',round(median,6))

if __name__=='__main__':run()
