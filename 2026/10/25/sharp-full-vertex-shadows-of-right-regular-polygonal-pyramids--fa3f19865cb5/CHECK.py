"""Independent reproducibility checks for regular-pyramid silhouette probabilities.

Run: python CHECK.py  (Python >=3.10; no third-party dependencies).
These finite computations supplement, but do not replace, the analytical proof.
"""
import math
import random


def terms(n):
    assert isinstance(n, int) and n >= 5
    beta = math.pi/n
    a = math.cos(beta)
    s = math.sin(beta)
    q = math.cos(2*beta)
    d = a/q
    return a, s, q, d


def denominator(n,x):
    c, s, q, d=terms(n)
    return (1+q+2*x)*math.sqrt(x+d*d)+2*(c*d+x)*math.sqrt(x+1)


def H(n,x):
    c,s,q,d=terms(n)
    return (4*x*x+2*d*d*x-(1+q)*d*d)/math.sqrt(x+d*d) + (4*x*x+2*x-2*c*d)/math.sqrt(x+1)


def optimum(n):
    lo,hi=0.0,10.0
    assert H(n,lo)<0<H(n,hi)
    for _ in range(90):
        mid=(lo+hi)/2
        if H(n,mid)<0: lo=mid
        else: hi=mid
    return math.sqrt((lo+hi)/2)


def formula(n,h):
    c,s,q,d=terms(n)
    return n/math.pi*math.atan(2*s*h*(d-c)/denominator(n,h*h))


def direct_solid_angle(n,h):
    c,s,q,d=terms(n)
    va=(c,s,-h); vb=(c,-s,-h); vc=(d,0.,-h)
    dot=lambda a,b:sum(u*v for u,v in zip(a,b))
    norm=lambda a:math.sqrt(dot(a,a))
    cross=lambda a,b:(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    num=abs(dot(va,cross(vb,vc)))
    den=norm(va)*norm(vb)*norm(vc)+dot(va,vb)*norm(vc)+dot(vb,vc)*norm(va)+dot(vc,va)*norm(vb)
    return n/(2*math.pi)*2*math.atan2(num,den)


def polygon_hull_size(points):
    points=sorted(points)
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[]; up=[]
    for p in points:
        while len(low)>=2 and cross(low[-2],low[-1],p)<=0:low.pop()
        low.append(p)
    for p in reversed(points):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0:up.pop()
        up.append(p)
    return len(low)+len(up)-2


def full_shadow(n,h,u):
    ux,uy,uz=u
    # An independent orthonormal basis for the plane perpendicular to u.
    v=(-uy,ux,0.)
    vn=math.hypot(v[0],v[1]);v=(v[0]/vn,v[1]/vn,0.)
    w=(uy*v[2]-uz*v[1],uz*v[0]-ux*v[2],ux*v[1]-uy*v[0])
    pts=[(math.cos(2*j*math.pi/n),math.sin(2*j*math.pi/n),0.) for j in range(n)]+[(0.,0.,h)]
    projected=[(p[0]*v[0]+p[1]*v[1]+p[2]*v[2],p[0]*w[0]+p[1]*w[1]+p[2]*w[2]) for p in pts]
    return polygon_hull_size(projected)==n+1


def only_one_support_line(n,h,u):
    qx,qy=(-h*u[0]/u[2],-h*u[1]/u[2])
    c=math.cos(math.pi/n)
    return sum(qx*math.cos((2*j+1)*math.pi/n)+qy*math.sin((2*j+1)*math.pi/n)>c for j in range(n))==1


def run():
    for n in (5,6,7,8,10,12,50):
        h=optimum(n)
        assert H(n,0)<0<H(n,10)
        assert abs(H(n,h*h))<1e-9
        assert formula(n,.98*h)<formula(n,h)>formula(n,1.02*h)
        for rh in (.1,.5,h,1.,2.,10.):
            assert abs(formula(n,rh)-direct_solid_angle(n,rh))<1e-12
    print('INDEPENDENT_TRIANGLE_SOLID_ANGLE_IDENTITY_OK')
    print('UNIQUE_CRITICAL_HEIGHT_NUMERIC_ROOTS_OK')
    assert abs(optimum(6)-math.sqrt(3/5))<1e-12
    assert abs(formula(6,optimum(6))-6/math.pi*math.atan(math.sqrt(2)/22))<1e-12
    print('HEXAGONAL_EXACT_BENCHMARK_NUMERIC_CHECK_OK')
    rng=random.Random(847296)
    count=0
    for n in (5,6,7,8,10,12):
        h=optimum(n)
        hits=0
        for i in range(3500):
            z=2*rng.random()-1
            t=2*math.pi*rng.random()
            q=math.sqrt(1-z*z)
            u=(q*math.cos(t),q*math.sin(t),z)
            a=full_shadow(n,h,u)
            b=only_one_support_line(n,h,u)
            assert a==b,(n,u)
            hits+=int(a)
            count+=1
        assert abs(hits/3500-formula(n,h))<0.04
    print('INDEPENDENT_PROJECTED_HULLS_AND_SUPPORT_COUNT_OK',count)
    lim=2*math.pi*math.pi/(3*math.sqrt(3))
    assert abs(optimum(10000)-1/math.sqrt(2))<3e-7
    assert abs(10000**2*formula(10000,optimum(10000))-lim)<1e-5
    print('DIMENSIONLESS_ASYMPTOTIC_CHECK_OK')
    print('ALL_PYRAMID_SILHOUETTE_REPRODUCTION_CHECKS_OK')
if __name__=='__main__':run()
