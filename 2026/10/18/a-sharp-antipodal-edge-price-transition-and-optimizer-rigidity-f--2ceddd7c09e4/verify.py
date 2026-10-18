"""Reproduce exact finite combinatorial identities and numerical spectral tests.
Run with: python3 verify.py   (requires numpy for spectral comparisons).
"""
from fractions import Fraction as F
from itertools import combinations
import numpy as np

checks = 0

def check(p):
    global checks
    assert p
    checks += 1

def lap(d, cube, matching):
    n=1<<d
    L=np.zeros((n,n), dtype=float)
    for x in range(n):
        for j in range(d):
            y=x^(1<<j)
            if x<y:
                w=float(cube[x,j])
                L[x,x]+=w; L[y,y]+=w
                L[x,y]-=w; L[y,x]-=w
        y=x^(n-1)
        if x<y:
            w=float(matching[x]); L[x,x]+=w; L[y,y]+=w
            L[x,y]-=w; L[y,x]-=w
    return L

def weights(d,a,b):
    n=1<<d
    return np.full((n,d),float(a)),np.full(n,float(b))

def test(d,B,t):
    m=1<<(d-1)
    if t<d:
        a=b=F(B,m*(d+t))
        gap=F(4*B,m*(d+t))
    else:
        a=F(B,m*d);b=F(0);gap=F(2*B,m*d)
    C,V=weights(d,a,b)
    l=lap(d,C,V)
    eig=np.linalg.eigvalsh(l)
    check(abs(eig[1]-float(gap))<1e-9)
    check(abs(sum(float(C[x,j]) for x in range(1<<d) for j in range(d) if x<(x^(1<<j)))+float(t)*sum(float(V[x]) for x in range(1<<d) if x<(x^((1<<d)-1)))-B)<1e-9)
    for k in range(1,d+1):
        mask=sum(1<<j for j in range(k))
        chi=np.array([(-1)**((x&mask).bit_count()) for x in range(1<<d)])
        lam=2*float(a)*k+(2*float(b) if k%2 else 0)
        check(np.linalg.norm(l@chi-lam*chi)<1e-8)
        check(lam+1e-9>=float(gap))
    if t==d:
        for step in range(11):
            b0=F(B*step,20*m*d)
            a0=F(B,m*d)-b0
            L=lap(d,*weights(d,a0,b0))
            check(abs(np.linalg.eigvalsh(L)[1]-float(gap))<1e-9)
        
    # Feasible perturbations of the optimizer cannot improve the gap.
    rng=np.random.default_rng(1000+d*13+int(t)*117)
    for _ in range(17):
        cube=rng.uniform(.01,1,(1<<d,d))
        match=rng.uniform(.01,1,1<<d)
        for x in range(1<<d):
            for j in range(d):
                cube[x,j]=cube[min(x,x^(1<<j)),j]
            match[x]=match[min(x,x^((1<<d)-1))]
        cost=sum(cube[x,j] for x in range(1<<d) for j in range(d) if x<(x^(1<<j)))+float(t)*sum(match[x] for x in range(1<<d) if x<(x^((1<<d)-1)))
        cube*=B/cost; match*=B/cost
        L=lap(d,cube,match)
        check(np.linalg.eigvalsh(L)[1]<=float(gap)+1e-8)
        T=sum(match[x] for x in range(1<<d) if x<(x^((1<<d)-1)))
        A=2*(B+(d-float(t))*T)/(m*d)
        C2=4*(B-float(t)*T)/(m*d)
        check(np.linalg.eigvalsh(L)[1]<=min(A,C2)+1e-8)

for d in range(2,7):
    for t in [F(1,3),F(d,2),F(d),F(d+1),F(3*d,2)]:
        for B in [1,5]:
            test(d,B,t)
print(f"PASS: {checks} checks on hypercubes of dimensions 2..6, multiple prices and budgets")
