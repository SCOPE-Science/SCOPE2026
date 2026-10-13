#!/usr/bin/env python3
"""Exact rational supplementary checks for priced folded-hypercube mixing.

Uses only the Python standard library. The proof of arbitrary dimension and
uniqueness is mathematical; the tests here are finite independent checks.
"""
from fractions import Fraction as F
import random


def construct_edges(d):
    N=1<<d
    coord=[]
    anti=[]
    for x in range(N):
        for i in range(d):
            y=x^(1<<i)
            if x<y: coord.append((x,y,i))
        y=x^(N-1)
        if x<y: anti.append((x,y))
    assert len(coord)==N*d//2 and len(anti)==N//2
    return coord,anti


def opt(d,t):
    N=1<<d
    if t<d:
        b=a=F(2,N*(d+t))
        gap=4*b
    elif t>d:
        b=F(2,N*d)
        a=F(0)
        gap=2*b
    else:
        b=F(2,N*d)
        a=F(0)
        gap=2*b
    return b,a,gap


def walsh(s,x):
    return -1 if ((s&x).bit_count()&1) else 1


def test_spectrum(d,t,b,a):
    N=1<<d
    coord,anti=construct_edges(d)
    # Every Walsh character is checked as an exact eigenvector.
    tests=0
    for s in range(N):
        k=s.bit_count()
        eigen=2*k*b+(2*a if k%2 else 0)
        for x in range(N):
            lhs=F(0)
            for y,z,i in coord:
                if y==x: lhs+=b*(walsh(s,x)-walsh(s,z))
                if z==x: lhs+=b*(walsh(s,x)-walsh(s,y))
            for y,z in anti:
                if y==x: lhs+=a*(walsh(s,x)-walsh(s,z))
                if z==x: lhs+=a*(walsh(s,x)-walsh(s,y))
            assert lhs==eigen*walsh(s,x)
            tests+=1
    return tests


def bound_for_any_weights(d,cweights,aweights):
    coord,anti=construct_edges(d)
    N=1<<d
    assert len(cweights)==len(coord) and len(aweights)==len(anti)
    B=sum(cweights,F(0)); A=sum(aweights,F(0))
    # Two character test families bound the spectral gap globally.
    avg_one=F(4,N)*(B/F(d)+A)
    avg_two=F(8,N*d)*B
    # Independent direct sum of character Rayleigh quotients.
    rs_one=[]
    for i in range(d):
        val=F(4,N)*(sum((w for (x,y,j),w in zip(coord,cweights) if j==i),F(0))+A)
        rs_one.append(val)
    rs_two=[]
    for i in range(d):
        for j in range(i+1,d):
            val=F(4,N)*sum((w for (x,y,k),w in zip(coord,cweights) if k in (i,j)),F(0))
            rs_two.append(val)
    assert sum(rs_one,F(0))/d==avg_one
    assert sum(rs_two,F(0))/len(rs_two)==avg_two
    return min(avg_one,avg_two),len(rs_one)+len(rs_two)


def main():
    random.seed(36102026)
    spectral=0; upper=0; perturb=0; critical=0
    for d in range(4,7):
        N=1<<d
        coord,anti=construct_edges(d)
        for t in (F(1,4),F(d,2),F(d-1,2),F(d),F(d+1,3),F(2*d)):
            b,a,goal=opt(d,t)
            assert (N//2)*(d*b+t*a)==1
            eigen=[2*k*b+(2*a if k%2 else 0) for k in range(1,d+1)]
            assert min(eigen)==goal
            spectral+=test_spectrum(d,t,b,a)
            if t==d:
                K=F(2,N*d)
                for z in (F(0),F(1,8),F(1,4),F(1,2)):
                    a1=K*z; b1=K-a1
                    assert 0<=a1<=b1
                    assert (N//2)*d*(b1+a1)==1
                    assert min(2*k*b1+(2*a1 if k%2 else 0) for k in range(1,d+1))==goal
                    critical+=1
        if d<=5:
            for t in (F(1,3),F(d),F(d+2)):
                _,_,target=opt(d,t)
                for _ in range(100):
                    cw=[F(random.randint(0,17)) for _ in coord]
                    aw=[F(random.randint(0,17)) for _ in anti]
                    cost=sum(cw,F(0))+t*sum(aw,F(0))
                    assert cost>0
                    cw=[w/cost for w in cw]
                    aw=[w/cost for w in aw]
                    ub,cnt=bound_for_any_weights(d,cw,aw)
                    assert ub<=target, (d,t,ub,target)
                    upper+=cnt
                    perturb+=1
    print('VERIFY_OK',spectral,'exact Walsh component equations;',upper,
          'exact character Rayleigh computations;',perturb,
          'individually irregular feasible allocations;',critical,
          'critical-family spectra')

if __name__=='__main__':
    main()
