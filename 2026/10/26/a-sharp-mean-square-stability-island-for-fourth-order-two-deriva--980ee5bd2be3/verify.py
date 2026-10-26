#!/usr/bin/env python3
"""Exact-arithmetic and direct-matrix verification of a stochastic TDRK stability threshold.
Run with Python 3.10+; standard library only. All samples are deterministic.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, isclose

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b): c[i+j]+=ai*bj
    return c

def coeffs(q):
    # Re R_q(i sqrt(x)), Im R_q(i sqrt(x))/sqrt(x)
    real=[F(1),-q/2,q*q/24]
    imag=[F(1),-q/6]
    r=mul(real,real)
    j=mul(imag,imag)
    for i,ji in enumerate(j):r[i+1]+=ji
    r[0]-=1
    return r

def Q(e,x):
    s=e*e
    return (1+6*s+s*s)*x*x-(8+56*s)*x+192*s

def f(s): return 1+2*s-23*s*s-12*s*s*s

def roots(e):
    s=e*e
    v=f(s)
    if v<0: return None
    A=1+6*s+s*s
    return (4*(1+7*s-sqrt(v))/A,4*(1+7*s+sqrt(v))/A)

def amp(q,theta):
    x=theta*theta
    return complex(1-q*x/2+q*q*x*x/24,theta-q*theta*x/6)

def step(u,q,theta):
    # oscillator with h=1, omega=theta, J(x,y)=(-y,x)
    def J(v):return (-v[1],v[0])
    f=J(u)
    y=(u[0]+theta*f[0]/2-q*theta*theta*u[0]/8,
       u[1]+theta*f[1]/2-q*theta*theta*u[1]/8)
    return (u[0]+theta*f[0]-q*theta*theta*(u[0]+2*y[0])/6,
            u[1]+theta*f[1]-q*theta*theta*(u[1]+2*y[1])/6)

def main():
    checked=0
    for j in range(1,200):
        q=F(j,71)
        c=coeffs(q)
        assert c==[F(0), 1-q, q*(q-1)/3,q*q*(2-3*q)/72,q**4/576]
        checked+=1
    for i in range(0,101):
        e=F(i,101)
        a=coeffs(1+e);b=coeffs(1-e)
        c=[(u+v)/2 for u,v in zip(a,b)]
        assert c==[F(0), F(0),e*e/3,-(8+56*e*e)/576,(1+6*e*e+e**4)/576]
        checked+=1
    # Exact polynomial sign classification on a dense rational lattice.
    for j in range(0,51):
        e=F(j,100)
        for k in range(1,121):
            x=F(k,13)
            s=e*e
            # independently expand E|R|^2-1 and compare with x^2 Q /576
            a=coeffs(1+e);b=coeffs(1-e)
            expansion=sum((u+v)/2*x**i for i,(u,v) in enumerate(zip(a,b)))
            assert expansion==x*x*Q(e,x)/576
            checked+=1
    # Matrix implementation versus scalar complex amplification.
    for qi in range(0,30):
        q=qi/21.0
        for ti in range(1,85):
            theta=ti/20
            z0=complex(.73,-1.19)
            z1=z0*amp(q,theta)
            v=step((z0.real,z0.imag),q,theta)
            assert abs(complex(*v)-z1)<2e-12*(1+abs(z1))
            checked+=1
    # Direct independent products, not just a recurrence obtained from the claim.
    for e,theta in [(.1,.5),(.2,2.0),(.2,3.0),(.4,2.1),(.6,2.0)]:
        p=amp(1+e,theta); m=amp(1-e,theta)
        E=(abs(p)**2+abs(m)**2)/2
        for n in range(1,9):
            total=0.
            for signs in product((p,m), repeat=n):
                z=1+0j
                for w in signs:z*=w
                total+=abs(z)**2
            assert isclose(total/(2**n),E**n,rel_tol=3e-12,abs_tol=2e-11)
            checked+=1
    # Transverse crossing and global loss of the stable band.
    lo,hi=0.,1.
    for _ in range(70):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    sc=(lo+hi)/2
    ec=sqrt(sc)
    assert .4889<ec<.48892
    for e in [0.,.001,.04,.1,.2,.3,.4,.48]:
        rm=roots(e)
        assert rm is not None
        xm,xp=rm
        assert 0<=xm<xp
        assert Q(e,(xm+xp)/2)<0
        assert Q(e,xp+max(xp-xm,1))>0
        if e>0:assert Q(e,xm/2)>0
        checked+=4
    for e in [.49,.5,.55,.7,.9]:
        assert f(e*e)<0
        for k in range(1,200):
            assert Q(e,k/23)>0
            checked+=1
    print('VERIFY_OK',checked,'critical_epsilon',format(ec,'.15f'),'critical_theta',format(sqrt(4*(1+7*sc)/(1+6*sc+sc*sc)),'.15f'))

if __name__=='__main__':main()
