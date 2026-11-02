#!/usr/bin/env python3
"""Exact finite-state and subset-identity checks for clumsy coupon collection.

Uses only Python's standard library; all asserted quantities are rational.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb

CHECKS = 0

def check(x, message):
    global CHECKS
    assert x, message
    CHECKS += 1

def subset_sum(w, p, s):
    """Green-function numerator and denominator for s>0."""
    r = p / (1-p)
    u = v = Q(0)
    for k in range(len(w)+1):
        for sub in combinations(range(len(w)), k):
            denom = s + sum((w[j] for j in sub), Q(0))
            u += (-1)**k / denom
            v += r**k / denom
    return u, v

def mean_formula(w, p):
    r = p/(1-p)
    out = Q(0)
    for k in range(1,len(w)+1):
        for sub in combinations(range(len(w)), k):
            out += (r**k-(-1)**k) / sum(w[j] for j in sub)
    return out

def pgf_formula(w, p, z):
    s = (1-z)/z
    a,b = subset_sum(w,p,s)
    return a/b

def solve(a,b):
    n = len(b)
    a = [row[:] + [b_i] for row,b_i in zip(a,b)]
    for c in range(n):
        pivot = next(i for i in range(c,n) if a[i][c] != 0)
        a[c],a[pivot] = a[pivot],a[c]
        fac = a[c][c]
        a[c] = [v/fac for v in a[c]]
        for i in range(n):
            if i != c and a[i][c]:
                mul = a[i][c]
                a[i] = [u-mul*v for u,v in zip(a[i],a[c])]
    return [row[-1] for row in a]

def transitions(mask,w,p):
    t={}
    for i,rate in enumerate(w):
        for suc,pr in ((False,p),(True,1-p)):
            y=(mask | (1<<i)) if suc else (mask & ~(1<<i))
            t[y] = t.get(y,Q(0)) + rate*pr
    return t

def markov_exact(w,p,z=None):
    n=len(w); last=(1<<n)-1
    a=[];rhs=[]
    for x in range(last):
        row=[Q(int(x==y)) for y in range(last)]
        t=transitions(x,w,p)
        mult=z if z is not None else Q(1)
        for y,pr in t.items():
            if y==last: continue
            row[y]-=mult*pr
        a.append(row)
        rhs.append(mult*t.get(last,Q(0)) if z is not None else Q(1))
    return solve(a,rhs)[0]

def pair_gap(w,p,i,j):
    r = p/(1-p)
    a,b=w[i],w[j]
    other=[k for k in range(len(w)) if k not in (i,j)]
    gap=Q(0)
    for k in range(len(other)+1):
        for ss in combinations(other,k):
            h=sum((w[t] for t in ss),Q(0))
            gap += (r**(k+1)+(-1)**k)*(1/(a+h)+1/(b+h)-2/((a+b)/2+h))
    return gap

def curvature(m,p):
    r=p/(1-p)
    return sum((Q(2*m**3*comb(m-2,k),(k+1)**3)*(r**(k+1)+(-1)**k)
                for k in range(m-1)),Q(0))

def test():
    # Direct full-state transition systems (no Green function used here).
    for m in range(1,5):
        uniform=[Q(1,m)]*m
        tilted=[Q(i+1,m*(m+1)//2) for i in range(m)]
        for w in (uniform, tilted):
            for p in (Q(0),Q(1,5),Q(1,2),Q(4,5)):
                check(mean_formula(w,p)==markov_exact(w,p),"mean vs full Markov")
                for z in (Q(1,5),Q(1,2),Q(4,5)):
                    check(pgf_formula(w,p,z)==markov_exact(w,p,z),"PGF vs full Markov")
    # Independent published equal-weight mean and explicit two-coupon case.
    for m in range(1,9):
        w=[Q(1,m)]*m
        for p in (Q(0),Q(1,6),Q(1,2),Q(3,4)):
            q=1-p
            known=m*sum((1/(k*q**k) for k in range(1,m+1)),Q(0))
            check(mean_formula(w,p)==known,"published equal-weight formula")
    for p in (Q(0),Q(1,7),Q(1,2),Q(9,10)):
        for a in (Q(1,8),Q(1,3),Q(1,2)):
            b=1-a
            check(mean_formula([a,b],p)-mean_formula([Q(1,2)]*2,p)
                  ==(a-b)**2/((1-p)*a*b),"two-type exact gap")
    # Exact pairwise transfer: arbitrary other coordinates, independent formula.
    for m in range(2,8):
        w=[Q(i+1,m*(m+1)//2) for i in range(m)]
        for p in (Q(0),Q(1,5),Q(1,2),Q(4,5)):
            for i,j in ((0,1),(0,m-1)):
                bal=w[:]
                bal[i]=bal[j]=(w[i]+w[j])/2
                g=mean_formula(w,p)-mean_formula(bal,p)
                check(g==pair_gap(w,p,i,j),"pairwise smoothing gap")
                if w[i]!=w[j]:
                    check(g>0,"strict expected optimality")
                    for z in (Q(1,4),Q(3,4)):
                        check(pgf_formula(bal,p,z)>pgf_formula(w,p,z),"PGF order")
    # The curvature matches the two-coordinate finite difference at small epsilon.
    for m in range(2,7):
        for p in (Q(0),Q(1,3),Q(3,4)):
            d=Q(1,20000)
            base=[Q(1,m)]*m
            w=base[:];w[0]+=d;w[1]-=d
            ratio=(mean_formula(w,p)-mean_formula(base,p))/d**2
            h=curvature(m,p)
            check(h>0,"strict local curvature")
            check(abs(ratio-h)/h<Q(1,100),"second-order curvature")
    print(f"PASS: {CHECKS} exact-rational assertions (the curvature tolerance check is a rational inequality).")

if __name__ == '__main__':
    test()
