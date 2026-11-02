#!/usr/bin/env python3
"""Reproduce exact small-cycle checks for discounted hitting-source placements.
No network or external packages are needed. Run: python3 verify_biased_cycles.py
"""
from fractions import Fraction as F
from collections import defaultdict
from math import ceil, sqrt
from decimal import Decimal, localcontext


def solve(matrix, rhs):
    """Independent exact Gaussian elimination for a nonsingular linear system."""
    n = len(rhs)
    a = [[F(v) for v in row] + [F(rhs[i])] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(j for j in range(col, n) if a[j][col])
        a[col], a[pivot] = a[pivot], a[col]
        t = a[col][col]
        a[col] = [x/t for x in a[col]]
        for row in range(n):
            if row == col: continue
            t = a[row][col]
            if t:
                a[row] = [x-t*y for x, y in zip(a[row], a[col])]
    return [a[i][-1] for i in range(n)]


def direct_cycle_floor(n, selected, lam, p):
    q = 1-p
    other = [v for v in range(n) if v not in selected]
    if not other: return F(1)
    pos = {v:i for i,v in enumerate(other)}
    mat, rhs = [], []
    for v in other:
        row = [F(v == w) for w in other]
        r = F(0)
        for w, prob in (((v+1)%n, p), ((v-1)%n, q)):
            if w in pos:
                row[pos[w]] -= lam * prob
            else:
                r += lam * prob
        mat.append(row);rhs.append(r)
    return min(solve(mat, rhs))


def interval_floor(length, lam, p):
    if length == 1: return F(1)
    q = 1-p
    mat, rhs = [], []
    for j in range(1,length):
        row = [F(j == k) for k in range(1,length)]
        r=F(0)
        if j-1 == 0: r += lam*q
        else: row[j-2] -= lam*q
        if j+1 == length: r += lam*p
        else: row[j] -= lam*p
        mat.append(row);rhs.append(r)
    vals=solve(mat,rhs)
    # Characteristic-root formula is checked against a separate exact solver.
    d=sqrt(float(1-4*lam*lam*p*q))
    rlo=(1-d)/(2*float(lam*p))
    rhi=(1+d)/(2*float(lam*p))
    for j,z in enumerate(vals, 1):
        formula=((rhi**length-1)*rlo**j+(1-rlo**length)*rhi**j)/(rhi**length-rlo**length)
        assert abs(formula-float(z)) < 2e-10,(length,j,p,lam)
    return min(vals)


def gaps(n, selected):
    s=sorted(selected)
    return [((s[(j+1)%len(s)]-s[j]) % n) or n for j in range(len(s))]


def compositions_coefficient(n, k, radius):
    dp=[0]*(n+1);dp[0]=1
    for _ in range(k):
        nxt=[0]*(n+1)
        for m, ways in enumerate(dp):
            if ways:
                for d in range(1,min(radius,n-m)+1):
                    nxt[m+d]+=ways
        dp=nxt
    return dp[n]


def run_exact_checks():
    trials=0
    masks=0
    tested_classes=0
    for p,lam in ((F(1,2), F(1,2)),(F(1,3),F(1,2)),
                  (F(3,4),F(1,2)),(F(2,3),F(2,3))):
        for n in range(3,10):
            floors=[None]+[interval_floor(L,lam,p) for L in range(1,n+1)]
            assert all(floors[L]>floors[L+1] for L in range(1,n))
            subsets=[]
            for mask in range(1,1<<n):
                sel={v for v in range(n) if mask & (1<<v)}
                intervals=gaps(n,sel)
                actual=direct_cycle_floor(n,sel,lam,p)
                assert actual == min(floors[L] for L in intervals), (n,mask,p,lam)
                subsets.append((sel,intervals,actual))
                masks+=1
            for tau in (F(1,12),F(1,6),F(1,4),F(1,3),
                        F(1,2),F(3,4),F(1)):
                R=max(L for L in range(1,n+1) if floors[L]>=tau)
                hist=defaultdict(int)
                for sel,intervals,actual in subsets:
                    predicted=max(intervals)<=R
                    assert predicted == (actual>=tau)
                    if actual>=tau: hist[len(sel)] += 1
                for k in range(1,n+1):
                    c=compositions_coefficient(n,k,R)
                    assert (n*c)%k == 0
                    assert hist[k]==n*c//k, (n,k,p,lam,tau)
                assert min(k for k,v in hist.items() if v)>0 and min(k for k,v in hist.items() if v)==ceil(n/R)
                trials+=1;tested_classes+=len(hist)
    return trials,masks,tested_classes


def critical_bias_checks():
    with localcontext() as ctx:
        ctx.prec = 65
        root17=Decimal(17).sqrt()
        p=(root17-1)/4
        h1=(2*p*p-5*p+4)/(4*(p*p-p+2))
        h2=(2*p*p-2*p+1)/(2*(p*p-p+2))
        h3=(2*p*p+p+1)/(4*(p*p-p+2))
        threshold=(Decimal(7)-root17)/16
        assert abs(h1-h2)<Decimal('1e-60')
        assert abs(h1-threshold)<Decimal('1e-60')
        assert h3>h2>Decimal(1)/6
        h5_j2=(p**4-p**3+7*p*p-9*p+4)/(p**4-2*p**3+13*p*p-12*p+16)
        assert h5_j2<Decimal(1)/6
        # Strictly better than the unbiased four-gap threshold 1/7.
        assert threshold>Decimal(1)/7
        return p,threshold,h5_j2

if __name__=='__main__':
    runs, masks, classes=run_exact_checks()
    p, H4, h5=critical_bias_checks()
    print('VERIFY_OK rational_grid_instances=',runs,'independent_exact_cycle_subsets=',masks,
          'feasible_cardinality_checks=',classes)
    print('DRIFT_OPTIMUM_OK p=',p,'H4=',H4,'H5_interior_upper=',h5)
