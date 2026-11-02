"""Standalone reproducibility checks for perimeter-moment box identification.
Python 3 standard library only. This is diagnostic; the stated analytic proof
is independent of quadrature and finite tests.
"""
import math
import random
from fractions import Fraction


def consts(nz=200, np=512):
    # Equal-spaced midpoint integration over z=cos(theta), phi; dOmega/(4*pi) = dz*dphi/(4*pi).
    sxy=0.0
    sxyz=0.0
    for j in range(nz):
        z=-1+(j+0.5)*2/nz
        rho=math.sqrt(1-z*z)
        xz=math.sqrt(1-z*z)
        for k in range(np):
            phi=2*math.pi*(k+0.5)/np
            xx=math.sqrt(max(0,1-rho*rho*math.cos(phi)**2))
            yy=math.sqrt(max(0,1-rho*rho*math.sin(phi)**2))
            sxy+=xx*yy
            sxyz+=xx*yy*xz
    return sxy/(nz*np), sxyz/(nz*np)


def raw_formula(a, alpha, beta):
    p1=sum(a)
    p2=sum(t*t for t in a)
    p3=sum(t**3 for t in a)
    return (math.pi*p1/4,
            alpha*p1*p1+(2/3-alpha)*p2,
            beta*p1**3+3*(5*math.pi/32-beta)*p1*p2+(2*beta-9*math.pi/32)*p3)


def recover_power_sums(m, alpha, beta):
    mu1,mu2,mu3=m
    p1=mu1/(math.pi/4)
    p2=(mu2-alpha*p1*p1)/(2/3-alpha)
    p3=(mu3-beta*p1**3-3*(5*math.pi/32-beta)*p1*p2)/(2*beta-9*math.pi/32)
    return (p1,p2,p3)


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])


def dot(x,y):return sum(i*j for i,j in zip(x,y))


def hull_perimeter(points):
    pts=sorted(set(points))
    def area(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>=2 and area(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    hi=[]
    for p in pts[::-1]:
        while len(hi)>=2 and area(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    h=lo[:-1]+hi[:-1]
    return sum(math.dist(h[i],h[(i+1)%len(h)]) for i in range(len(h)))


def direct_perimeter(a,u):
    z=(0.,0.,1.) if abs(u[2])<.9 else (0.,1.,0.)
    v=cross(u,z); norm=math.sqrt(dot(v,v)); v=tuple(t/norm for t in v)
    w=cross(u,v)
    from itertools import product
    points=[(dot(v,q),dot(w,q)) for s in product((-1,1),repeat=3) for q in [[s[i]*a[i]/2 for i in range(3)]]]
    return hull_perimeter(points)


def main():
    alpha,beta=consts()
    assert 2/3-alpha>0
    assert 2*beta-9*math.pi/32<0
    assert Fraction(1,5)-Fraction(1,105)==Fraction(4,21)
    assert 4/math.sqrt(21)<9*math.pi/32
    assert abs(alpha-0.593)<0.002 and abs(beta-0.4215)<0.002
    for a in [(1.,1.,1.),(1.,2.,3.),(2.,2.,5.),(.6,1.7,4.1)]:
        m=raw_formula(a,alpha,beta)
        p=recover_power_sums(m,alpha,beta)
        assert max(abs(x-y) for x,y in zip(p,[sum(t**k for t in a) for k in range(1,4)]))<1e-10
        e2=(p[0]*p[0]-p[1])/2
        e3=(p[0]**3-3*p[0]*p[1]+2*p[2])/6
        assert abs(e2-sum(a[i]*a[j] for i in range(3) for j in range(i+1,3)))<1e-9
        assert abs(e3-math.prod(a))<1e-9
    a=(1.,2.,3.)
    b=(2.-1/math.sqrt(3),2.-1/math.sqrt(3),2.+2/math.sqrt(3))
    A=raw_formula(a,alpha,beta)
    B=raw_formula(b,alpha,beta)
    assert abs(A[0]-B[0])<1e-12 and abs(A[1]-B[1])<1e-12
    assert abs(A[2]-B[2])>.001
    rng=random.Random(20261025)
    n=0
    for a in [(1.,1.,1.),(1.,2.,3.),(2.,2.,5.),(.6,1.7,4.1)]:
        for k in range(80):
            u=[rng.gauss(0,1) for _ in range(3)]
            norm=math.sqrt(dot(u,u)); u=tuple(x/norm for x in u)
            direct=direct_perimeter(a,u)
            symbolic=2*sum(ai*math.sqrt(1-x*x) for ai,x in zip(a,u))
            assert abs(direct-symbolic)<2e-12*max(1,symbolic)
            n+=1
    print('VERIFY_OK', 'hull_checks', n, 'alpha', format(alpha,'.10f'), 'beta', format(beta,'.10f'), 'determinant', format(2*beta-9*math.pi/32,'.10f'), 'two_moment_counterexample_third_gap',format(B[2]-A[2],'.8f'))

if __name__=='__main__':main()
