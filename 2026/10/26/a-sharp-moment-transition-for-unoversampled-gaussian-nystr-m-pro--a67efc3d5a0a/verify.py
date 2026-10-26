#!/usr/bin/env python3
"""Independent finite arithmetic diagnostics for the stated Gaussian projection identities.
No finite test proves the population moment or small-parameter limit."""
import math
import random

def diagnostic(h, k, rng):
    w1,w2=rng.gauss(0,1),rng.gauss(0,1)
    psi=[(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(k)]
    col=(w1,h*w2)
    den=sum(a*col[0]+b*col[1] for a,b in psi) # intentionally unused aggregate
    gs=[a*col[0]+b*col[1] for a,b in psi]
    g2=sum(x*x for x in gs)
    scalar=[sum(gs[i]*psi[i][j] for i in range(k))/g2 for j in (0,1)]
    y=((col[0]*scalar[0],col[0]*scalar[1]*h),
       (col[1]*scalar[0],col[1]*scalar[1]*h))
    direct=( (1-y[0][0])**2+y[0][1]**2+y[1][0]**2+(h-y[1][1])**2 )**0.5
    n=math.hypot(*col)
    q=(col[0]/n,col[1]/n)
    v=(-q[1],q[0]); G=[a*q[0]+b*q[1] for a,b in psi]
    H=[a*v[0]+b*v[1] for a,b in psi]
    zeta=sum(x*y for x,y in zip(G,H))/sum(x*x for x in G)
    residual=h*math.hypot(w1,w2)/n
    analytic=residual*math.sqrt(1+zeta*zeta)
    return direct,analytic

def simpson(f,a,b,n):
    step=(b-a)/n
    return step/3*(f(a)+f(b)+4*sum(f(a+i*step) for i in range(1,n,2))+2*sum(f(a+i*step) for i in range(2,n,2)))

def angular(h,q,n=12000):
    return 2*h**q/math.pi*simpson(lambda t:(math.cos(t)**2+h*h*math.sin(t)**2)**(-q/2),0,math.pi/2,n)

def B(q,k):
    return math.exp(math.lgamma((k+1)/2)+math.lgamma((k-q)/2)-math.lgamma(k/2)-math.lgamma((k+1-q)/2))

if __name__=='__main__':
    r=random.Random(23143)
    counter=0
    for k in (1,2,3,5,14):
        for h in (0.00002,0.01,0.4,0.9):
            for _ in range(65):
                a,b=diagnostic(h,k,r)
                assert math.isclose(a,b,rel_tol=8e-9,abs_tol=5e-10),(a,b,h,k)
                counter+=1
    for k in (3,4,7,12):
        assert math.isclose(B(2,k),(k-1)/(k-2),rel_tol=1e-12)
        for h in (0.04,0.3,0.8):
            assert math.isclose(B(2,k)*angular(h,2),(k-1)/(k-2)*h,rel_tol=1e-8)
            counter+=1
    for k in (2,5,9):
        h=0.0005
        ratio=angular(h,1)/(2*h/math.pi*math.log(4/h))
        assert abs(ratio-1)<0.03,ratio
        counter+=1
    print('VERIFY_OK',counter)
