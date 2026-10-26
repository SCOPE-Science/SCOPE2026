#!/usr/bin/env python3
"""Independent exact-rational verification of cycle equilibrium geometry.
No external dependencies. The mathematical proof is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product


def br(theta, x):
    return max(Q(0), Q(theta)-x)


def cycle_map(theta, t):
    x=t
    for a in reversed(theta):
        x=br(a,x)
    return x


def clamped_cycle(theta):
    m=max(theta)
    sign=1; offset=Q(0); lo=Q(0); hi=Q(m)
    for a in reversed(theta):
        newlo=br(a,hi)
        newhi=br(a,lo)
        sign=-sign; offset=Q(a)-offset
        lo,hi=newlo,newhi
    return sign,offset,lo,hi


def clip(x,lo,hi):
    return max(lo,min(hi,x))


def fixed_interval(theta):
    sign,b,lo,hi=clamped_cycle(theta)
    if sign==-1:
        z=clip(b/2,lo,hi)
        return z,z
    if b<0:
        return lo,lo
    if b>0:
        return hi,hi
    return lo,hi


def reconstructed(theta,t):
    # Solve x_i=BR_i(x_{i+1}) backward, checking cycle closure.
    x=[Q(0)]*len(theta)
    x[0]=t
    for i in range(len(theta)-1,0,-1):
        x[i]=br(theta[i],x[(i+1)%len(theta)])
    assert all(x[i]==br(theta[i],x[(i+1)%len(theta)]) for i in range(len(theta)))
    return x


def brute_pieces(theta):
    # Independent affine-piece propagation, not using the clipping recursion.
    M=Q(max(theta))
    pieces=[(Q(0),M,Q(1),Q(0))] # interval, slope, intercept
    for a in reversed(theta):
        nxt=[]
        for left,right,s,b in pieces:
            cuts={left,right}
            if s:
                crossing=(Q(a)-b)/s
                if left<crossing<right:
                    cuts.add(crossing)
            bounds=sorted(cuts)
            for l,r in zip(bounds,bounds[1:]):
                mid=(l+r)/2
                if Q(a)-s*mid-b>0:
                    nxt.append((l,r,-s,Q(a)-b))
                else:
                    nxt.append((l,r,Q(0),Q(0)))
        pieces=nxt
    return pieces


def roots_from_pieces(theta):
    pts=[]; intervals=[]
    for l,r,s,b in brute_pieces(theta):
        if s==1 and b==0:
            intervals.append((l,r))
        elif s!=1:
            z=b/(1-s)
            if l<=z<=r:pts.append(z)
    if intervals:
        return min(l for l,r in intervals),max(r for l,r in intervals)
    return min(pts),max(pts)


if __name__=='__main__':
    examined=0; checks=0; continuum=0; odd_unique=0; balanced_nocontinuum=0
    for m in range(2,8):
        for tup in product(range(1,4),repeat=m):
            theta=tuple(map(Q,tup))
            s,b,l,u=clamped_cycle(theta)
            assert s==(-1)**m
            low,high=fixed_interval(theta)
            assert (low,high)==roots_from_pieces(theta)
            for t in [Q(0),Q(max(theta)),Q(max(theta))/3,Q(max(theta))/2]:
                assert cycle_map(theta,t)==clip(s*t+b,l,u)
                checks+=1
            for t in set([low,high,(low+high)/2]):
                x=reconstructed(theta,t)
                assert all(0<=z<=max(theta) for z in x)
                checks+=1
            if low<high:
                continuum+=1
                assert m%2==0 and b==0
                x=reconstructed(theta,(low+high)/2)
                assert all(z>0 for z in x)
            elif m%2:
                odd_unique+=1
            elif b==0:
                balanced_nocontinuum+=1
            examined+=1
    assert fixed_interval((Q(1),Q(1)))==(Q(0),Q(1))
    assert fixed_interval((Q(2),Q(1)))==(Q(2),Q(2))
    assert fixed_interval((Q(1),Q(1),Q(1)))==(Q(1,2),Q(1,2))
    assert fixed_interval((Q(10),Q(1),Q(1),Q(10),Q(1),Q(1)))==(Q(9),Q(9))
    print(f'PASS exact: {examined} directed cycles, {checks} identities/reconstructions, {continuum} nondegenerate continua, {odd_unique} odd unique, {balanced_nocontinuum} balanced singleton cases')
