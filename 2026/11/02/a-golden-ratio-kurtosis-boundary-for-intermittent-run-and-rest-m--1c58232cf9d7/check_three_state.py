#!/usr/bin/env python3
"""Independent finite-matrix and convolution checks for a three-velocity run/rest process."""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def state_moments(a, b, v, t):
    """Differentiate the Markov-additive Feynman--Kac semigroup via a block lift."""
    Q = np.array([[-a, a, 0], [b / 2, -b, b / 2], [0, a, -a]], float)
    V = np.diag([v, 0., -v])
    B = np.zeros((15, 15))
    for j in range(5):
        B[3*j:3*j+3, 3*j:3*j+3] = Q
        if j: B[3*j:3*j+3, 3*(j-1):3*j] = j*V
    u0 = np.zeros(15)
    u0[:3] = 1.
    u = expm(t*B) @ u0
    pi = np.array([b/(2*(a+b)), a/(a+b), b/(2*(a+b))])
    return float(pi@u[6:9]), float(pi@u[12:15])


def positive_kernel(a, b, t):
    """Compute H and H' from an independent six-stage positive linear cascade."""
    M = np.zeros((6, 6))
    M[0, 0] = -2*a
    M[1, 0], M[1, 1] = 1., -(a+b)
    M[2, 1], M[2, 2] = 1., -a
    M[3, 2], M[3, 3] = 1., -a
    M[4, 3] = 1.
    M[5, 4] = 1.
    u = expm(t*M) @ np.array([1.,0.,0.,0.,0.,0.])
    return float(u[5]), float(u[4])


def theorem_cumulant(a,b,v,t):
    H, Hp = positive_kernel(a,b,t)
    return 24*b*v**4/(a+b)**2*((a-2*b)*Hp+2*(a*a-a*b-b*b)*H)


def unique_time(a,b):
    phi=(1+math.sqrt(5))/2
    assert phi < a/b < 2
    def f(t):
        H,Hp=positive_kernel(a,b,t)
        return Hp/H-2*(a*a-a*b-b*b)/(2*b-a)
    lo=0.02/max(a,b)
    hi=1/max(a,b)
    while f(hi)>0: hi*=2
    return brentq(f,lo,hi,xtol=1e-11)


def run():
    n=0
    cases=[]
    for ratio in (0.4, 0.8, 1., 1.4, 1.6, (1+math.sqrt(5))/2, 1.65, 1.8, 1.95, 2., 2.4, 4.):
        for b in (0.7, 1., 1.9):
            a=ratio*b
            for v in (0.5, 1.7):
                for bt in (.15,.3,.7,1.5,3.,6.,12.):
                    t=bt/b
                    m2,m4=state_moments(a,b,v,t)
                    k=m4-3*m2*m2
                    kt=theorem_cumulant(a,b,v,t)
                    tol=2e-8*(1+abs(m4)+abs(3*m2*m2))
                    assert abs(k-kt)<tol,(a,b,v,t,k,kt,tol)
                    n+=1
    phi=(1+math.sqrt(5))/2
    for r in (.4,1.,1.4,phi,1.65,1.8,1.95,2.,3.):
        a,b=r,1.
        for t in (.15,.5,1.,4.,10.):
            val=theorem_cumulant(a,b,1.,t)
            if r<=phi:assert val<0,(r,t,val)
            if r>=2:assert val>0,(r,t,val)
            n+=1
    roots=[]
    for r in (1.63,1.65,1.75,1.8,1.95,1.99):
        rt=unique_time(r,1.)
        roots.append((r,rt))
        for t in (.5*rt, 1.5*rt):
            val=theorem_cumulant(r,1.,1.,t)
            assert val <0 if t<rt else val>0
            n+=1
    for a,b in ((1.8,1.),(2.,1.),(1.,1.),(4.,2.)):
        t=.0002/max(a,b)
        small=theorem_cumulant(a,b,1.,t)/t**4
        expected=b*(a-2*b)/(a+b)**2
        # For a=2b, leading t^4 vanishes, otherwise use t=.03 to avoid cancellation
        if a!=2*b:
            t=.03/max(a,b)
            small=theorem_cumulant(a,b,1.,t)/t**4
            assert abs(small-expected)<.12*max(.1,abs(expected))
            n+=1
        t=200/max(a,b)
        long=theorem_cumulant(a,b,1.,t)/t
        expected=24*b*(a*a-a*b-b*b)/(a**3*(a+b)**3)
        assert abs(long-expected)<.02*(1+abs(expected))
        n+=1
    print('PASS',n,'independent full-Feynman-Kac and positive-kernel checks')
    print('roots (b=1, dimensionless time):',roots)
    print('example a=1.8, b=v=1 crossing:',unique_time(1.8,1.))

if __name__=='__main__':run()
