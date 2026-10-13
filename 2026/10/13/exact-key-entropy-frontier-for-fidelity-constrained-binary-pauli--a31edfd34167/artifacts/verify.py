#!/usr/bin/env python3
import math


def h2(q):
    if q == 0.0 or q == 1.0:
        return 0.0
    return -q*math.log2(q)-(1-q)*math.log2(1-q)


def contractions(p):
    pI,pX,pY,pZ=p
    return pI+pX-pY-pZ, pI-pX-pY+pZ


def entropy(p):
    return -sum(x*math.log2(x) for x in p if x>0)


def source_params(theta,eta):
    C=math.cos(theta/2.0)**2
    V=math.sin(theta/2.0)**2
    tau=2.0*eta-1.0
    a=0.0 if tau<=C else (tau-C)/V
    return C,V,tau,a


def check_case(theta,eta,t):
    C,V,tau,_=source_params(theta,eta)
    feasible=tau<=C+t*V+1e-12
    p=((1+t)/2.0,0.0,0.0,(1-t)/2.0)
    lx,lz=contractions(p)
    assert abs(lx-t)<1e-12 and abs(lz-1.0)<1e-12
    assert abs(entropy(p)-h2((1-t)/2.0))<1e-12
    util=(1+lz*C+lx*V)/2.0
    if feasible:
        assert util+1e-12>=eta
    # Finite corroborative simplex grid.
    N=40
    bound=h2((1-t)/2.0)
    for i in range(N+1):
        for j in range(N+1-i):
            for k in range(N+1-i-j):
                l=N-i-j-k
                q=(i/N,j/N,k/N,l/N)
                qx,qz=contractions(q)
                qutil=(1+qz*C+qx*V)/2.0
                if abs(qx)<=t+1e-12 and qutil+1e-12>=eta:
                    assert entropy(q)+1e-10>=bound


for deg,eta,t in [
    (60,0.90,0.20),
    (90,0.80,0.20),
    (120,0.70,0.20),
    (180,0.80,0.60),
    (180,0.40,0.00),
    (75,0.55,0.65),
]:
    check_case(math.radians(deg),eta,t)

for deg,eta in [(60,0.9),(90,0.8),(120,0.7),(180,0.8),(180,0.4)]:
    C,V,tau,a=source_params(math.radians(deg),eta)
    p=((1+a)/2.0,0.0,0.0,(1-a)/2.0)
    lx,lz=contractions(p)
    assert abs(lx-a)<1e-12 and abs(lz-1.0)<1e-12
    assert (1+lz*C+lx*V)/2.0+1e-12>=eta
    assert abs(entropy(p)-h2((1-a)/2.0))<1e-12

print('VERIFY_OK')
