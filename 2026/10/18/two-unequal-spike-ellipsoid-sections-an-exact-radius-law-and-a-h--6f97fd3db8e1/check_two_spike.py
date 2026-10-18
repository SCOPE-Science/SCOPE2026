#!/usr/bin/env python3
"""Independent finite-dimensional checks of two-unequal-axis ellipsoid section laws.
Only Python's standard library is required. These tests are not substitutes for proofs.
"""
import math
import random

RNG = random.Random(20261016)


def eigen2_small(a, b, c):
    return (a + c - math.hypot(a-c, 2*b))/2


def predicted_radius(u, a, b):
    d1, d2 = a**-2, b**-2
    z1 = math.sqrt(1-d1)*u[0]
    z2 = math.sqrt(1-d2)*u[1]
    lam = eigen2_small(d1+z1*z1, z1*z2, d2+z2*z2)
    return lam**-0.5


def basis_in_h(u):
    n=len(u)
    out=[]
    for j in range(n):
        v=[float(i==j)-u[j]*u[i] for i in range(n)]
        for w in out:
            c=sum(x*y for x,y in zip(v,w))
            v=[x-c*y for x,y in zip(v,w)]
        nn=math.sqrt(sum(x*x for x in v))
        if nn>1e-7:
            out.append([x/nn for x in v])
        if len(out)==n-1:
            return out
    raise AssertionError("No hyperplane basis")


def smallest_symmetric_eigenvalue(mat):
    m=len(mat)
    a=[row[:] for row in mat]
    for iteration in range(100*m*m):
        p,q=max(((i,j) for i in range(m) for j in range(i+1,m)),
                key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1e-13:
            return min(a[i][i] for i in range(m))
        t=(a[q][q]-a[p][p])/(2*a[p][q])
        tau=math.copysign(1.0,t)/(abs(t)+math.sqrt(1+t*t)) if t!=0 else 1.0
        c=1/math.sqrt(1+tau*tau)
        s=tau*c
        app=a[p][p];aqq=a[q][q];apq=a[p][q]
        a[p][p]=app-tau*apq
        a[q][q]=aqq+tau*apq
        a[p][q]=a[q][p]=0.0
        for k in range(m):
            if k not in (p,q):
                akp,akq=a[k][p],a[k][q]
                a[k][p]=a[p][k]=c*akp-s*akq
                a[k][q]=a[q][k]=s*akp+c*akq
    raise AssertionError('Jacobi did not converge')


def direct_radius(u, a, b):
    h=basis_in_h(u)
    diag=[a**-2,b**-2]+[1.]*(len(u)-2)
    mat=[[sum(h[i][k]*diag[k]*h[j][k] for k in range(len(u)))
          for j in range(len(h))] for i in range(len(h))]
    return smallest_symmetric_eigenvalue(mat)**-0.5


def normal(n):
    x=[RNG.gauss(0,1) for _ in range(n)]
    t=math.sqrt(sum(y*y for y in x))
    return [y/t for y in x]


def conditional_event(u,a,b,r):
    d1,d2=a**-2,b**-2
    s=r**-2
    return (1-d1)*u[0]**2 >= (s-d1)*(1+(1-d2)*u[1]**2/(d2-s))


def expectation_on_normal(f, m=8000):
    # Simpson quadrature for E[f(G)] with G standard Gaussian
    # Restriction to [-10,10] leaves < 2e-23 Gaussian probability.
    lo,hi=-10.0,10.0
    step=(hi-lo)/m
    v=0.0
    for i in range(m+1):
        x=lo+i*step
        weight=1 if i in (0,m) else (4 if i%2 else 2)
        v+=weight*f(x)*math.exp(-x*x/2)/math.sqrt(2*math.pi)
    return v*step/3


def run():
    count=0; worst=0.0
    for n in (3,4,6,8):
        for a,b in ((5.,2.),(3.,1.25),(20.,3.2)):
            for _ in range(35):
                u=normal(n)
                x=predicted_radius(u,a,b)
                y=direct_radius(u,a,b)
                worst=max(worst,abs(x-y))
                assert abs(x-y)<2e-8,(n,a,b,x,y)
                assert b-1e-9 <= x <= a+1e-9
                r=(a+b)/2
                assert (x<=r)==conditional_event(u,a,b,r)
                count+=1
    for a,b in ((4.,2.),(10.,1.5)):
        assert abs(predicted_radius([1.,0.,0.],a,b)-b)<1e-12
        assert abs(predicted_radius([0.,0.,1.],a,b)-a)<1e-12
    c1,c2=3.,1.4
    g1,g2=1.2,-0.7
    for n in (100,1000,10000):
        # Gaussian representation of the first two spherical coordinates.
        rest=sum(RNG.gauss(0,1)**2 for _ in range(n-2))
        nn=math.sqrt(g1*g1+g2*g2+rest)
        u=[g1/nn,g2/nn]
        real=predicted_radius(u,c1*math.sqrt(n),c2*math.sqrt(n))/math.sqrt(n)
        target=eigen2_small(c1**-2+g1*g1,g1*g2,c2**-2+g2*g2)**-0.5
        print('N',n,'critical radius',round(real,6),'limit at fixed Gaussian pair',round(target,6))
    c2=1.4; q=c2**-2
    const=math.sqrt(2/math.pi)*expectation_on_normal(lambda g:math.sqrt(1+c2*c2*g*g))
    for t in (20.,80.,320.):
        ss=t**-2
        p=expectation_on_normal(lambda g:math.erf(math.sqrt(ss*(1+g*g/(q-ss)))/math.sqrt(2)))
        print('t',t,'t*tail',round(t*p,8),'asymptotic constant',round(const,8))
        assert abs(t*p/const-1)<0.01
    print('VERIFY_OK',count,'direct eigenvalue, event, and boundary checks; maximum absolute error',worst)


if __name__=='__main__':
    run()
