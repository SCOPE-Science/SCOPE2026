#!/usr/bin/env python3
"""Finite checks for renewal-escape coherence identities; no infinite proof is claimed."""
import math
import cmath
import numpy as np

def age_vector(hazards, steps):
    state = np.array([1.0])
    out = [state]
    for t in range(steps):
        r = np.array([hazards(j) for j in range(t+1)])
        nxt = np.empty(t+2)
        nxt[0] = np.dot(state,r)
        nxt[1:] = state*(1-r)
        state = nxt
        out.append(state)
    return out

def square_hazard(n):
    return 1.0/(n+2)**2

def G_square(z):
    if abs(z-1)<1e-12:
        return 1.0
    F=0.5*(1+(1-z)/z*cmath.log(1-z))
    return 0.5/(1-F)

def check():
    checks=0
    # Exact partial survival telescoping and exact reset mass.
    for k in range(1,80):
        prod=math.prod(1-square_hazard(n) for n in range(k))
        assert abs(prod-(k+2)/(2*(k+1)))<2e-14
        checks+=1
        fk=math.prod(1-square_hazard(n) for n in range(k-1))*square_hazard(k-1)
        assert abs(fk-1/(2*k*(k+1)))<2e-14
        checks+=1
    # Compare renewal Fourier transform with direct finite power series.
    for z in [-1,1j,cmath.exp(0.71j),cmath.exp(2.03j)]:
        truncated=sum((z**k)/(2*k*(k+1)) for k in range(1,30001))
        exact=.5*(1+(1-z)/z*cmath.log(1-z))
        assert abs(truncated-exact)<2.5e-9
        assert abs(G_square(z)-0.5/(1-exact))<1e-13
        checks+=2
    p=0.5
    for z in [-1,1j,cmath.exp(0.71j),cmath.exp(2.03j)]:
        g=G_square(z)
        assert p/(2-p)-1e-12<=abs(g)<=1+1e-12
        checks+=1
    assert abs(G_square(-1)-1/(1+2*math.log(2)))<1e-13
    checks+=1
    # Show sharpness of the universal lower/upper bounds for finite-support defects.
    for p in [0.15,0.35,0.5,0.9]:
        flo=-(1-p)
        fhi=1-p
        assert abs(p/(1-flo)-p/(2-p))<1e-14
        assert abs(p/(1-fhi)-1)<1e-14
        checks+=2
    # Direct age distribution recursion (independent of last-renewal transform).
    horizon=3500
    state=np.array([1.0]); snapshots={}
    for t in range(horizon+1):
        if t in [100,300,1000,2000,3500]:
            snapshots[t]=state.copy()
            assert abs(state.sum()-1)<1e-12
            checks+=1
        if t == horizon: break
        r=1.0/np.square(np.arange(2,t+3,dtype=float))
        nxt=np.empty(t+2)
        nxt[0]=np.dot(state,r)
        nxt[1:]=state*(1-r)
        state=nxt
    angles=[math.pi,math.pi/2,0.71,2.03]
    errtable=[]
    for ang in angles:
        z=cmath.exp(1j*ang)
        g=G_square(1/z)
        errors=[]
        for t,p_age in snapshots.items():
            idx=np.arange(len(p_age))
            ampl=np.dot(p_age,np.exp(1j*ang*(idx-t)))
            err=abs(ampl-g)
            errors.append((t,err))
            if t==3500:
                assert err<0.003
                checks+=1
        assert errors[-1][1]<errors[0][1]
        checks+=1
        errtable.append((ang, errors))
    # Direct trace-norm distinction in the 2x2 example.
    g=1/(1+2*math.log(2))
    assert 0.8 < 2*g < 0.9
    # Defect-ensemble example is not a finite-simulation argument for general U.
    print('CHECKS_PASSED',checks)
    print('NO_RESET_MASS',0.5)
    print('EFFECTIVE_COHERENCE',format(g,'.15f'))
    print('SUCCESSIVE_TRACE_NORM',format(2*g,'.15f'))
    for ang, errs in errtable:
        print('PHASE',round(ang,9),'ERRORS',[(t,round(e,8)) for t,e in errs])
    print('FINITE_CHECKS_ONLY; analytic proof establishes infinite claim')

if __name__=='__main__':
    check()
