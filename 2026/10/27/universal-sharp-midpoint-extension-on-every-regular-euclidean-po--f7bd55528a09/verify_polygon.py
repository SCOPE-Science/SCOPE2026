#!/usr/bin/env python3
"""Finite numerical corroboration for regular-polygon midpoint extension theorem.

Requires Python 3, numpy, scipy. This is not an infinite-n proof.
"""
import math
import numpy as np
from scipy.optimize import linprog

def verify(n):
    a = math.pi / n
    c = math.cos(a)
    v = np.array([[math.cos(2*j*a), math.sin(2*j*a)] for j in range(n)])
    m = (v + np.roll(v,-1,axis=0))/2
    D = np.linalg.norm(v[:,None,:]-v[None,:,:],axis=2)
    d = np.linalg.norm(v-m[0],axis=1)
    S = D[0].sum()
    L = S/d.sum()
    t = (np.roll(d,1)+np.roll(d,-1)-2*c*d)
    w = L*t/(4*math.sin(a))
    assert np.min(w)>-3e-10,(n,'negative weight',np.min(w))
    assert abs(w.sum()-1)<3e-9,(n,'normalization')
    assert np.max(np.abs(D@w-L*d))<1e-8,(n,'distance identity')
    # Unimodal shells; the midpoint axis passes between vertices 0 and 1.
    shells=[]
    if n%2:
        h=n//2
        for k in range(h):
            shells.append(w[(k+1)%n])
            assert abs(w[(k+1)%n]-w[-k%n])<1e-8
        shells.append(w[(h+1)%n])
    else:
        h=n//2
        for k in range(h):
            shells.append(w[(k+1)%n]);assert abs(w[(k+1)%n]-w[-k%n])<1e-8
    assert all(shells[k]>=shells[k+1]-3e-10 for k in range(len(shells)-1)),(n,'unimodal')
    # Explicit nonnegative probability rho, with w=rho*(delta_0+delta_1)/2.
    rho=np.zeros(n)
    if n%2:
        rho[h]=shells[h]
        for k in range(h-1,-1,-1):rho[k]=2*shells[k]-rho[k+1]
        for k in range(1,h+1):rho[-k]=rho[k]
    else:
        rho[h]=0
        for k in range(h-1,-1,-1):rho[k]=2*shells[k]-rho[k+1]
        for k in range(1,h):rho[-k]=rho[k]
    assert min(rho)>-4e-9,(n,'negative mixing',min(rho))
    assert abs(sum(rho)-1)<1e-8
    assert np.max(np.abs((rho+np.roll(rho,1))/2-w))<1e-8
    # Independent test of all distinct midpoint orbits by earth-mover LP.
    A=np.zeros((n,n*n))
    for j in range(n):
        A[j,j*n:(j+1)*n]=1
        A[j,j::n]-=1
    worst_pair=0
    for k in range(1,n//2+1):
        diff=w-np.roll(w,k)
        lp=linprog(D.flatten(),A_eq=A,b_eq=diff,bounds=(0,None),method='highs')
        assert lp.success,(n,k,lp.message)
        ratio=lp.fun/np.linalg.norm(m[0]-m[k])
        worst_pair=max(worst_pair,ratio)
        assert ratio <=1+2e-8,(n,k,ratio)
    assert L>1
    return L, min(w), min(rho), worst_pair

def main():
    cases=0;pair_classes=0
    for n in range(3,31):
        lam,wmin,rhomin,pair=verify(n)
        cases+=1;pair_classes+=n//2
        if n in (3,4,5,6,7,8,12,20,30):
            print('n=%d lambda=%.12f min_weight=%.3e min_mixer=%.3e maximum_midpair=%.12f' %
                  (n,lam,wmin,rhomin,pair))
    print('POLYGON_MIDPOINT_EXACT_FORMULA_NUMERIC_OK n_cases=%d midpoint_orbits=%d' % (cases,pair_classes))
if __name__ == '__main__': main()
