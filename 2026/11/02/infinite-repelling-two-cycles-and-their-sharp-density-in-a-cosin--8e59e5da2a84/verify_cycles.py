#!/usr/bin/env python3
"""Numerical cross-checks for the cosine-memory logistic map.

Requires Python 3.10+ standard library only. These are independent
finite checks of explicit identities, not a proof of the asymptotic theorem.
"""
import cmath
import math

PI = math.pi

def f(x, w, a, k, q):
    return (a*x*(1-x*x*math.cos(q+k*w)), w+x)

def jac(x, w, a, k, q):
    c = math.cos(q+k*w)
    s = math.sin(q+k*w)
    return ((a*(1-3*x*x*c),a*k*x**3*s),(1.0,1.0))

def mul(A,B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],
             A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0],
             A[1][0]*B[0][1]+A[1][1]*B[1][1]))

def spectral(A):
    t=A[0][0]+A[1][1]
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    disc=cmath.sqrt(t*t-4*d)
    return ((t+disc)/2,(t-disc)/2),t,d

def bisection(g,left,right,positive_left):
    assert (g(left)>0 and g(right)<0) if positive_left else (g(left)<0 and g(right)>0)
    for _ in range(65):
        mid=(left+right)*0.5
        if (g(mid)>0)==positive_left: left=mid
        else: right=mid
    return (left+right)*0.5

def type_b(a,k,n,sgn):
    C=1+1/a
    z=(2*n+1)*PI/k
    half=PI/(3*k)
    g=lambda u:u*u*abs(math.cos(k*u*0.5))-C
    assert g(z-half)>0 and g(z)<0 and g(z+half)>0
    u=(bisection(g,z-half,z,True) if sgn<0 else bisection(g,z,z+half,False))
    j=int(math.cos(k*u/2)<0)
    th=-k*u/2+j*PI
    return u,th,z

def verify_case(a,k,q):
    C=1+1/a
    d=-2*a-3
    cycles=0
    for m in range(6,12):
        u=2*PI*m/k
        assert u*u>C
        for sig in [-1,1]:
            th=sig*math.acos(C/u**2)
            w=(th-q)/k
            x1,w1=f(u,w,a,k,q)
            x2,w2=f(x1,w1,a,k,q)
            assert abs(x1+u)<1e-7*max(1,u)
            assert abs(x2-u)<2e-7*max(1,u)
            assert abs(w2-w)<1e-7*max(1,u)
            A=mul(jac(x1,w1,a,k,q),jac(u,w,a,k,q))
            eig,t,det=spectral(A)
            b=a*k*u**3*math.sin(th)
            assert math.isclose(t,d*d+1,rel_tol=1e-6,abs_tol=1e-5)
            assert math.isclose(det,d*d-b*b,rel_tol=1e-6,abs_tol=1e-3)
            assert det<0 and min(abs(z) for z in eig)>1
            assert all(abs(abs(z)/(a*k*u**3)-1)<0.20 for z in eig)
            cycles+=1
    for n in range(6,12):
        for sig in [-1,1]:
            u,th,z=type_b(a,k,n,sig)
            assert abs(u-z-sig*2*C/(k*z*z))<5e-4*max(1,abs(u-z))
            w=(th-q)/k
            x1,w1=f(u,w,a,k,q)
            x2,w2=f(x1,w1,a,k,q)
            assert abs(x1+u)<1e-7*max(1,u)
            assert abs(x2-u)<2e-7*max(1,u)
            assert abs(w2-w)<1e-7*max(1,u)
            J0=jac(u,w,a,k,q)
            J1=jac(x1,w1,a,k,q)
            A=mul(J1,J0)
            eig,t,det=spectral(A)
            b=a*k*u**3*math.sin(th)
            assert math.isclose(t,(d+1)**2-2*(d-b),rel_tol=1e-5,abs_tol=1e-4)
            assert math.isclose(det,(d-b)**2,rel_tol=1e-5,abs_tol=1e-3)
            assert det>0 and min(abs(z) for z in eig)>1
            assert all(abs(abs(z)/(a*k*u**3)-1)<0.20 for z in eig)
            cycles+=1
    return cycles

def verify_inner_strip():
    a,k,q=0.45,0.71,1.31
    rho=math.sqrt(1/a-1)
    count=0
    for frac in (0.2,0.75,0.97):
        for xsign in (-1,1):
            x=xsign*frac*rho
            for w in (-11,0,2.7):
                rat=a*(1+x*x)
                base=abs(x)
                for n in range(90):
                    assert abs(x)<=base*rat**n+1e-14
                    x,w=f(x,w,a,k,q)
                assert abs(x)<1e-10
                count+=1
    return count

if __name__=='__main__':
    total=sum(verify_case(*v) for v in ((0.45,0.7,0.3),(1.7,3.2,0.2),(2.9,1.0,-0.8)))
    tubes=verify_inner_strip()
    print(f'PASS: {total} analytic-cycle witnesses (both families), {tubes} attraction-strip orbits; return equations, full Jacobians, determinant signs, and growth law checked.')
