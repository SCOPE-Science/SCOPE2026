#!/usr/bin/env python3
"""Exact cyclotomic-support checks for the three-tap matched-aperture theorem.

Only finite corroboration; the general claim is proved separately.
Run: python3 checker.py
"""
from itertools import combinations
from math import comb


def add(a,b,scale=1):
    out=dict(a)
    for e,v in b.items():
        out[e]=out.get(e,0)+scale*v
    return {e:v for e,v in out.items() if v}

def mul(a,b):
    out={}
    for e,v in a.items():
        for f,w in b.items():
            out[e+f]=out.get(e+f,0)+v*w
    return {e:v for e,v in out.items() if v}

def zero_at_primitive_root(a,p):
    coeff=[0]*p
    for e,v in a.items():coeff[e%p]+=v
    return len(set(coeff))==1

def shift(a,e):return {k+e:v for k,v in a.items()}

def stft_holes(f,g,p):
    holes=set()
    active={ (u-v)%p for u in f for v in g }
    for t in sorted(active):
        for k in range(p):
            v={}
            for u,fu in f.items():
                gu=g.get((u-t)%p)
                if gu is None: continue
                v=add(v,shift(mul(fu,{ -e:c for e,c in gu.items()}),-k*u))
            if zero_at_primitive_root(v,p):holes.add((t,k))
    return holes

def arithmetic_progression(A,p):
    return any((x+z-2*y)%p==0 for x,y,z in (
        (A[i],A[j],A[k]) for i in range(3) for j in range(3) for k in range(3)
        if len({i,j,k})==3))

def check(p):
    X={0:1}
    ff={0:{1:1,3:1},1:{0:-1,2:-1},2:{0:1}}
    C={1:1,-1:1}
    gg={0:X,1:C,2:C}
    holes=stft_holes(ff,gg,p)
    assert holes=={(0,0),(0,p-2),(1,p-1),(p-1,p-1)}, (p,holes)
    # Exhaustively realize every permitted four-hole geometry (alpha,beta,gamma,delta).
    patterns=set()
    for gamma,delta in combinations(range(p),2):
        gd={gamma:1,delta:1}
        for alpha in range(p):
            prod=mul({(gamma+delta)%p:1},gd)
            ff_family={0:shift(prod,-alpha),1:{e:-v for e,v in gd.items()},2:X}
            gg_family={0:{-alpha:1},1:{-gamma:1,-delta:1},2:{-gamma:1,-delta:1}}
            holes_family=stft_holes(ff_family,gg_family,p)
            beta=(gamma+delta-alpha)%p
            expected={(0,(-gamma)%p),(0,(-delta)%p),
                      (1,(-alpha)%p),(p-1,(-beta)%p)}
            assert holes_family==expected, (p,gamma,delta,alpha,holes_family,expected)
            patterns.add(frozenset(holes_family))
    assert len(patterns)==p*comb(p,2)
    sums={}
    for A in combinations(range(p),3):
        AP=arithmetic_progression(A,p)
        D={(a-b)%p for a in A for b in A}
        assert len(D)==(5 if AP else 7), (p,A,D,AP)
        sums[AP]=sums.get(AP,0)+1
        if not AP:
            a,b,c=A
            E0={-a:1}; E1={-b:1}; E2={-c:1}
            f={a:add(E2,E1,-1),b:add(E0,E2,-1),c:add(E1,E0,-1)}
            g={a:X,b:X,c:X}
            assert all(not zero_at_primitive_root(u,p) for u in f.values())
            hs=stft_holes(f,g,p)
            assert hs=={(0,0),(0,1)},(p,A,hs)
    assert sums.get(True,0)==p*(p-1)//2
    assert sums.get(False,0)==comb(p,3)-p*(p-1)//2
    print('PASS p=',p,'AP=',sums.get(True,0),'nonAP=',sums.get(False,0),'AP-holes=',len(holes))

for p in (5,7,11,13):check(p)
print('CHECK_PASS')
