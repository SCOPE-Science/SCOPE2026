"""Reproducibility checks for a uniform lossy termination with a tunable end link.

Requires Python 3 and NumPy. Invoke: python verify_bridge_absorption.py
Checks are finite diagnostics and are not a substitute for the proof.
"""
import math
import numpy as np


def b_closed(n, u):
    assert n >= 1 and u > 0
    t = math.exp(-2 * n * u)
    tnext = math.exp(-2 * (n + 1) * u)
    if n % 2:
        return math.exp(-u) * (1+t) / (-math.expm1(-2*(n+1)*u))
    return math.exp(-u) * (1-t) / (1+tnext)


def b_direct(n, u):
    y = 2*math.sinh(u)
    b = 0.0
    for _ in range(n):
        b = 1/(y+b)
    return b


def direct_reflection(n, u, h, k=math.pi/2):
    """Solve the n+1 stationarity equations, not the Green-function fraction."""
    J = 1.0
    gamma = 4*math.sinh(u)
    E = -2*math.cos(k)
    M = np.zeros((n+1,n+1), dtype=complex)
    rhs = np.zeros(n+1, dtype=complex)
    M[0,0] = E + np.exp(1j*k)
    M[0,1] = h
    rhs[0] = -E - np.exp(-1j*k)
    M[1,0] = h
    M[1,1] = E + 0.5j*gamma
    if n > 1: M[1,2] = J
    rhs[1] = -h
    for j in range(2,n+1):
        M[j,j-1] = J
        M[j,j] = E + 0.5j*gamma
        if j<n: M[j,j+1] = J
    sol = np.linalg.solve(M,rhs)
    residual = np.max(np.abs(M@sol-rhs))
    # Flux balance, lead group speed = 2 J sin k.
    outgoing = abs(sol[0])**2
    absorbed = gamma*np.sum(np.abs(sol[1:])**2)/(2*math.sin(k))
    return sol[0],residual,outgoing+absorbed


def analytic_reflection(n,u,h):
    v = h*h*b_closed(n,u)
    return (1-v)/(1+v)


def bisect(f, lo,hi):
    flo=f(lo)
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)*flo>0:
            lo=mid;flo=f(mid)
        else:
            hi=mid
    return (lo+hi)/2


def peak(n):
    assert n%2==0
    def dlog(u):
        return n/math.tanh(n*u)-(n+1)*math.tanh((n+1)*u)
    u = bisect(dlog,1e-8,12)
    return u,b_closed(n,u)


def run():
    count=0
    for n in range(1,19):
        for u in (0.07, 0.21, 0.8, 1.5):
            assert abs(b_closed(n,u)-b_direct(n,u)) < 2e-12
            count+=1
            for h in (0.6,1.0,1.8):
                r,res,flux=direct_reflection(n,u,h)
                assert abs(r-analytic_reflection(n,u,h)) < 3e-11, (n,u,h,r)
                assert res<1e-11 and abs(flux-1)<1e-10,(n,u,h,flux)
                count+=3
    for n in range(1,20):
        if n%2:
            u=bisect(lambda u:b_closed(n,u)-1,1e-8,10)
            r,_,_=direct_reflection(n,u,1)
            assert abs(r)<1e-10 and abs(b_closed(n,u)-1)<1e-10
            count+=2
        else:
            u,bm=peak(n);hcrit=1/math.sqrt(bm)
            assert 0<bm<1 and hcrit>1
            # At threshold: one double root; on strong side: two simple roots.
            assert abs(analytic_reflection(n,u,hcrit))<1e-10
            h=1.01*hcrit
            left=bisect(lambda x:b_closed(n,x)-1/h**2,1e-10,u)
            right=bisect(lambda x:b_closed(n,x)-1/h**2,u,10)
            assert 0<left<u<right
            for x in (left,right):
                r,_,_=direct_reflection(n,x,h)
                assert abs(r)<1e-10
                count+=1
            # Below threshold there is no root because b <= bmax.
            assert (0.99*hcrit)**2*bm<1
            count+=5
    for n in (50,100,200,500,1000):
        u,bm=peak(n)
        hcrit=1/math.sqrt(bm)
        est=1+(math.log(4*n)+1)/(4*n)
        assert abs(hcrit-est) < 15*(math.log(n)**2)/n**2
        assert abs(4*math.sinh(u)-2*math.log(4*n)/n)<10*math.log(n)/n**2
        count+=2
    print('PASS:',count,'checks; direct linear equations, flux, roots and large-n scaling')

if __name__=='__main__': run()
