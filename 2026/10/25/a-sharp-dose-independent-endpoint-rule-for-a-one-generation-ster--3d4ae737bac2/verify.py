#!/usr/bin/env python3
"""Exact-rational checks for a single-generation sterile-male pulse in a Beverton--Holt baseline.

Python 3 standard library only. The analytical endpoint theorem is proved separately;
finite tests here are reproducibility and arithmetic checks, not an infinite proof.
"""
from fractions import Fraction as F
import random


def unforced(x, R):
    return R*x/(1+x)


def treated(x, R, s):
    return R*x*x/((1+x)*(x+s))


def terminal(x, R, s, n, t):
    for j in range(n):
        x = treated(x, R, s) if j == t else unforced(x, R)
    return x


def affine(z, R):
    return (z+1)/R


def f_power(z, R, j):
    for _ in range(j):
        z=affine(z,R)
    return z


def E(z0,R,t):
    zt=f_power(z0,R,t)
    return R**t*zt*(zt+1)


def closed_terminal(x,R,s,n,t):
    z0=1/x
    z=f_power(z0,R,n)+s*E(z0,R,t)/R**n
    return 1/z


def check(R,x,s,n):
    vals=[]
    vals_closed=[]
    H=[]
    for t in range(n):
        vals.append(terminal(x,R,s,n,t))
        vals_closed.append(closed_terminal(x,R,s,n,t))
        H.append(E(1/x,R,t))
    assert vals == vals_closed
    if n>=3:
        assert all(H[j-1]-2*H[j]+H[j+1]>0 for j in range(1,n-1))
        assert all(y>min(vals[0],vals[-1]) for y in vals[1:-1])
    if R <= 1:
        assert H == sorted(H) and len(set(H)) == n
        assert vals[-1]<vals[0]
    else:
        assert vals[0] == min(vals) or vals[-1] == min(vals)
    # Every target between zero and the untreated terminal density has
    # the same optimal time, independently of the required pulse amount.
    base=unforced(x,R)
    for _ in range(n-1):
        base=unforced(base,R)
    target=base/2
    hmax=max(H[0],H[-1])
    required=R**n*(1/target-1/base)/hmax
    assert required>0
    zbase=f_power(1/x,R,n)
    assert 1/base==zbase
    assert any(terminal(x,R,required,n,t)==target for t in (0,n-1))
    assert all(terminal(x,R,required,n,t)>=target for t in range(n))
    return len(vals)


def main():
    rng=random.Random(73421)
    trials=0
    placements=0
    for n in range(2,11):
        for a in range(1,9):
            for b in range(1,9):
                R=F(a*a,b*b)
                x=F(rng.randint(1,13),rng.randint(1,17))
                s=F(rng.randint(1,9),rng.randint(1,17))
                placements+=check(R,x,s,n)
                trials+=1
                if R>1:
                    # sqrt(R) is exactly a/b; check full threshold, including tie.
                    root=F(a,b)
                    xc=(R-1)/(1+root**n)
                    for mult in (F(1,2),F(1),F(2)):
                        xcur=xc*mult
                        placements+=check(R,xcur,s,n)
                        trials+=1
                        u=terminal(xcur,R,s,n,0)
                        v=terminal(xcur,R,s,n,n-1)
                        assert (u<v if mult<1 else u==v if mult==1 else u>v)
    for x in (F(1,10),F(1,5),F(3,10)):
        vals=[terminal(x,F(3),F(1),4,j) for j in range(4)]
        expected={F(1,10):0,F(1,5):None,F(3,10):3}[x]
        if expected is None:
            assert vals[0]==vals[-1]<min(vals[1:-1])
        else:
            assert vals[expected]==min(vals)
    print('PASS: %d exact rational parameter cases; %d placement identities; endpoint comparisons, convexity, exact target dose and ties.' % (trials,placements))
    print('R=3, n=4, s=1 threshold x=1/5; x=1/10: first; x=1/5: tied endpoints; x=3/10: last.')

if __name__=='__main__':
    main()
