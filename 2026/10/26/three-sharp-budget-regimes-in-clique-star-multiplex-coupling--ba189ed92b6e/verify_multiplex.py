"""Reproducibility checks for optimal weighted clique--star matching multiplex.

Run: python verify_multiplex.py
Requires Python >= 3.9, standard library only.
Finite checks support, but do not replace, the all-parameter proof.
"""
import math
from fractions import Fraction


def lo_mu(n, x, y):
    return (n + 2*x + 2*y - math.hypot(n-2+2*x-2*y, 2*math.sqrt(n-1)))/2


def lo_nu(n, y):
    return (n+1+2*y - math.hypot(n-1, 2*y))/2


def optimum(n, B):
    assert n >= 3 and B >= 0
    m = n-1
    b1 = n*n/(n+1)
    b2 = math.inf if n == 3 else m*(n-2)/(n-3)
    if B <= b1:
        return B/n, B/n, 2*B/n, "uniform"
    if B >= b2:
        return 0., B/m, lo_nu(n, B/m), "hub-off"
    left, right = B/n, B/m
    for _ in range(80):
        y = (left+right)/2
        d = lo_mu(n, B-m*y, y) - lo_nu(n, y)
        if d > 0: left=y
        else: right=y
    y=(left+right)/2
    return B-m*y, y, lo_nu(n, y), "balanced"


def make_laplacian(n, x, weights):
    p=2*n
    L=[[0.0]*p for _ in range(p)]
    def edge(i,j,w):
        L[i][i]+=w
        L[j][j]+=w
        L[i][j]-=w
        L[j][i]-=w
    for i in range(n):
        for j in range(i+1,n): edge(i,j,1.0)
    for j in range(1,n): edge(n,n+j,1.0)
    edge(0,n,x)
    for j,y in enumerate(weights,start=1): edge(j,n+j,y)
    return L


def jacobi_spectrum(A):
    a=[row[:] for row in A]
    n=len(a)
    for sweep in range(100):
        largest=0.
        for i in range(n-1):
            for j in range(i+1,n):
                v=a[i][j]
                largest=max(largest,abs(v))
                if abs(v)<1e-15: continue
                theta=(a[j][j]-a[i][i])/(2*v)
                t=math.copysign(1.,theta)/(abs(theta)+math.sqrt(1+theta*theta)) if theta else 1.
                c=1/math.sqrt(1+t*t)
                s=t*c
                aii,ajj=a[i][i],a[j][j]
                a[i][i]=aii-t*v
                a[j][j]=ajj+t*v
                a[i][j]=a[j][i]=0.
                for k in range(n):
                    if k==i or k==j: continue
                    aki,akj=a[k][i],a[k][j]
                    a[k][i]=a[i][k]=c*aki-s*akj
                    a[k][j]=a[j][k]=s*aki+c*akj
        if largest<1e-12: break
    return sorted(a[i][i] for i in range(n))


def verify():
    checks=0
    for n in range(3,25):
        b1=Fraction(n*n,n+1)
        t1=Fraction(2*n,n+1)
        x1=y1=Fraction(n,n+1)
        assert x1+(n-1)*y1==b1
        assert (n-1+2*x1-t1)*(1+2*y1-t1)==n-1
        assert (n+y1-t1)*(1+y1-t1)==y1*y1
        checks+=3
        if n>=4:
            t2=Fraction(2)
            y2=Fraction(n-2,n-3)
            b2=(n-1)*y2
            assert (n+y2-t2)*(1+y2-t2)==y2*y2
            assert (n-1-t2)*(1+2*y2-t2)==n-1
            assert b1<b2
            checks+=3
        for B in [b1/4,b1,b1+Fraction(1,100),b1+Fraction(1,4),b1+Fraction(1,2),
                  (Fraction(n-1)*Fraction(n-2,n-3) if n>=4 else b1+10),
                  (Fraction(2*(n-1))*Fraction(n-2,n-3) if n>=4 else b1+100)]:
            B=float(B)
            x,y,t,phase=optimum(n,B)
            assert x >=-1e-10 and y>=0 and abs(x+(n-1)*y-B)<1e-8
            assert abs(t-min(lo_mu(n,x,y),lo_nu(n,y)))<1e-8
            checks+=2
    for n in range(3,12):
        b1=n*n/(n+1)
        b2=math.inf if n==3 else (n-1)*(n-2)/(n-3)
        budgets=[0.7*b1,b1,1.02*b1,1.22*b1,b2*1.1 if n>3 else 30.]
        for B in budgets:
            x,y,t,phase=optimum(n,B)
            ev=jacobi_spectrum(make_laplacian(n,x,[y]*(n-1)))
            assert abs(ev[0])<1e-8
            assert abs(ev[1]-t)<2e-8,(n,B,ev[1],t)
            # Independent feasible symmetric perturbations cannot improve.
            for offset in [-0.08,-0.01,0.01,0.08]:
                yy=max(0.,min(B/(n-1),y+offset*B/n))
                xx=B-(n-1)*yy
                ev2=jacobi_spectrum(make_laplacian(n,xx,[yy]*(n-1)))
                assert ev2[1]<=t+2e-8,(n,B,ev2[1],t)
            checks+=6
    print('PASS:', checks, 'finite exact-identity, direct-spectrum, and neighboring-design checks')

if __name__=='__main__': verify()
