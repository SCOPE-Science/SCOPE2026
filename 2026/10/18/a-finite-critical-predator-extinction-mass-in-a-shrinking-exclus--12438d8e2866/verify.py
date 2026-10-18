#!/usr/bin/env python3
"""Independent finite-difference checks of the explicitly stated Neumann resolvent.
Uses Python standard library only. Numerical checks do not substitute for proof.
"""
import math


def psi(x, L, a, du, lam):
    k = math.sqrt(lam / du)
    if x <= a:
        return (1.0 - math.sinh(k * (L-a)) * math.cosh(k * x) / math.sinh(k*L)) / lam
    return math.sinh(k*a) * math.cosh(k*(L-x)) / (lam * math.sinh(k*L))


def mean_psi(L, a, du, lam):
    k = math.sqrt(lam / du)
    return (1.0 - math.sinh(k*(L-a))*math.sinh(k*a)/(k*a*math.sinh(k*L))) / lam


def thomas(lo,diag,hi,b):
    n=len(b)
    c=[0.0]*n
    y=[0.0]*n
    c[0]=hi[0]/diag[0] if n>1 else 0
    y[0]=b[0]/diag[0]
    for i in range(1,n):
        q=diag[i]-lo[i]*c[i-1]
        c[i]=hi[i]/q if i<n-1 else 0
        y[i]=(b[i]-lo[i]*y[i-1])/q
    x=[0.0]*n
    x[-1]=y[-1]
    for i in range(n-2,-1,-1):
        x[i]=y[i]-c[i]*x[i+1]
    return x


def solve_finite_volume(L, a, du, lam, n):
    h=L/n
    assert abs(a/h-round(a/h)) < 1e-9, "put interface on a cell edge"
    off=-du/h**2
    diag=[lam+(1 if i in (0,n-1) else 2)*du/h**2 for i in range(n)]
    left=[0]+[off]*(n-1)
    right=[off]*(n-1)+[0]
    rhs=[1.0 if (i+0.5)*h<a else 0.0 for i in range(n)]
    u=thomas(left,diag,right,rhs)
    for i in range(n):
        reconstructed=diag[i]*u[i]
        if i>0: reconstructed+=off*u[i-1]
        if i<n-1: reconstructed+=off*u[i+1]
        assert abs(reconstructed-rhs[i])<1e-10, (n,i,reconstructed)
    return [(i+0.5)*h for i in range(n)],u


def run():
    count=0
    for L,a,du,lam in [(1,.5,.5,1.5),(1,.25,.5,1.5),(2,1,.3,.7),(3,.75,2,1.1),(.8,.2,.8,2.3)]:
        for n in (80,160):
            xx, values=solve_finite_volume(L,a,du,lam,n)
            error=max(abs(y-psi(x,L,a,du,lam)) for x,y in zip(xx,values))
            assert error < 0.0011, (L,a,du,lam,n,error)
            im=int(round(n*a/L))
            empirical=sum(values[:im])/im
            target=mean_psi(L,a,du,lam)
            assert abs(empirical-target)<0.0011, (L,a,empirical,target)
            assert 0<target<1/lam
            count+=1
    for L,du,lam in ((1,.5,1.5),(3,2,1.1),(.8,.8,2.3)):
        k=math.sqrt(lam/du)
        limit=lam*math.tanh(k*L)/k
        for a in (L/1000,L/2000):
            ratio=a/mean_psi(L,a,du,lam)
            assert abs(ratio/limit-1)<0.003, (a,ratio,limit)
            count+=1
    print('PASS: %d positive-resolvent/Neumann finite-volume and thin-zone checks.'%count)

if __name__=='__main__':
    run()
