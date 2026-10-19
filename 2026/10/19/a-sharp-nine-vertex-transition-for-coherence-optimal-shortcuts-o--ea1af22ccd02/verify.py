#!/usr/bin/env python3
"""Exact reproducibility tests for path single-edge coherence placement."""
from fractions import Fraction as F

def v(n,d,i):
    # ||L_path^+ (e_i-e_{i+d})||_2^2, exact.
    return (F(n*d*d,4)-F(d**3,6)+F(d,6)
            - F(d*d*(d+2*i-n+1)**2,4*n))

def best_v(n,d):
    i=(n-1-d)//2
    return v(n,d,i)

def gain(n,d,i,w):
    return w*v(n,d,i)/(1+w*d)

def threshold(n):
    assert n>=9
    return F(12*(n-2), (n-3)*(n-1)*(n-8))

def inverse_exact(A):
    n=len(A)
    E=[list(r)+[F(i==j) for j in range(n)] for i,r in enumerate(A)]
    for c in range(n):
        k=next(r for r in range(c,n) if E[r][c])
        E[k],E[c]=E[c],E[k]
        p=E[c][c]
        E[c]=[x/p for x in E[c]]
        for r in range(n):
            if r!=c:
                t=E[r][c]
                if t: E[r]=[x-t*y for x,y in zip(E[r],E[c])]
    return [row[n:] for row in E]

def direct_trace(n,i,j,w):
    A=[[F(1,n) for _ in range(n)] for __ in range(n)]
    for x,y,z in [(k,k+1,F(1)) for k in range(n-1)]+[(i,j,w)]:
        A[x][x]+=z; A[y][y]+=z
        A[x][y]-=z; A[y][x]-=z
    B=inverse_exact(A)
    return sum(B[k][k] for k in range(n))-1

def run():
    exact_checks=0
    for n in range(3,11):
        weights=[F(1,2),F(3)]
        if n>=9: weights+=[threshold(n)]
        for w in weights:
            for i in range(n):
                for j in range(i+2,n):
                    direct=direct_trace(n,i,j,w)
                    formula=F(n*n-1,6)-gain(n,j-i,i,w)
                    assert direct==formula,(n,i,j,w,direct,formula)
                    exact_checks+=1
    placement_checks=0
    for n in range(3,81):
        weights=[F(1,100),F(1),F(100),F(10000)] if n<=8 else [threshold(n)/4,threshold(n),4*threshold(n)]
        for w in weights:
            ep=gain(n,n-1,0,w)
            best=ep
            best_pairs=[]
            for d in range(2,n):
                for i in range(n-d):
                    g=gain(n,d,i,w)
                    if g>best:
                        best=g; best_pairs=[(i,i+d)]
                    elif g==best:
                        best_pairs.append((i,i+d))
                    placement_checks+=1
            if n<=8 or (n>=9 and w<=threshold(n)):
                assert best==ep,(n,w,'endpoint-not-optimal')
            if n>=9 and w==threshold(n):
                assert set(best_pairs)=={(0,n-1),(1,n-2)},(n,best_pairs)
            if n>=9 and w>threshold(n):
                assert best>ep,(n,w,'endpoint-still-optimal')
    # Fixed-conductance large-size limit for optimal span and central placement.
    ratios=[]
    for n in (100,200,400,800):
        w=F(1)
        d=max(range(2,n),key=lambda z:w*best_v(n,z)/(1+w*z))
        i=(n-1-d)//2
        ratios.append((n,d,i))
        assert abs(F(d,n)-F(3,4))<F(2,n)
        assert abs(F(i,n)-F(1,8))<F(2,n)
    print('VERIFY_OK direct_rational_inverses=',exact_checks,'global_exact_chord_comparisons=',placement_checks,'macroscopic=',ratios)

if __name__=='__main__':run()
