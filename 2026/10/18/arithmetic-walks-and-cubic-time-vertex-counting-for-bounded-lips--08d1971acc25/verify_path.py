#!/usr/bin/env python3
"""Exact dynamic counts for the bounded-Lipschitz unit ball on a finite path.

The program tests the finite walk formula independently via direct walk enumeration
and, if SciPy is installed, compares low-dimensional polytope vertex counts.
"""
from collections import defaultdict
from itertools import product


def boundary_mask(h, d):
    return (1 if h == 0 else 0) | (2 if h == d else 0)


def eligible(seq, d):
    if not seq or not (1 <= d <= len(seq)-1):
        return False
    if any(h < 0 or h > d for h in seq):
        return False
    if any(abs(v-u) > 1 for u,v in zip(seq, seq[1:])):
        return False
    run = [seq[0]]
    spans = False
    for u,v in zip(seq, seq[1:]):
        if v == u:
            if 0 not in run and d not in run:
                return False
            spans |= (0 in run and d in run)
            run = [v]
        else:
            run.append(v)
    if 0 not in run and d not in run:
        return False
    spans |= (0 in run and d in run)
    return spans


def layer_dp(n,d):
    dp = {(h,boundary_mask(h,d),False):1 for h in range(d+1)}
    for _ in range(n-1):
        nxt=defaultdict(int)
        for (h,mask,done),cnt in dp.items():
            for k in (h-1,h+1):
                if 0 <= k <= d:
                    newmask = mask | boundary_mask(k,d)
                    nxt[(k,newmask,done or newmask==3)] += cnt
            if mask:
                nxt[(h,boundary_mask(h,d),done or mask==3)] += cnt
        dp=nxt
    return sum(cnt for (h,mask,done),cnt in dp.items() if mask and (done or mask==3))


def layer_brute(n,d):
    total = 0
    for start in range(d+1):
        for steps in product((-1,0,1),repeat=n-1):
            seq = [start]
            for step in steps:
                seq.append(seq[-1]+step)
            total += eligible(seq,d)
    return total


def count_vertices(n):
    return 2 + sum(layer_dp(n,d) for d in range(1,n))


def check_hull(n):
    import numpy as np
    from scipy.spatial import HalfspaceIntersection
    hs=[]
    def add(vec,constant=0):
        hs.append(list(vec)+[constant])
    for i in range(n):
        for s in (-1,1):
            v=np.zeros(n+2); v[i]=s; v[n]=-1; add(v)
    for i in range(n-1):
        for s in (-1,1):
            v=np.zeros(n+2); v[i]=-s; v[i+1]=s; v[n+1]=-1; add(v)
    for i in (n,n+1):
        v=np.zeros(n+2); v[i]=-1; add(v)
    v=np.zeros(n+2); v[n]=v[n+1]=1; add(v,-1)
    interior=np.zeros(n+2); interior[n]=interior[n+1]=.3
    poly=HalfspaceIntersection(np.asarray(hs),interior,qhull_options='Qx')
    projections = set()
    for row in poly.intersections:
        f=tuple(np.round(row[:n],8))
        if max(map(abs,f))+max(abs(f[i+1]-f[i]) for i in range(n-1))>0.999999:
            projections.add(f)
    return len(projections)


def main():
    small_expected=[4,10,26,64,162,404,998,2454,6014,14632]
    for n,expected in enumerate(small_expected,start=2):
        got=count_vertices(n)
        assert got==expected,(n,got,expected)
    brute_checks=0
    for n in range(2,10):
        for d in range(1,n):
            assert layer_dp(n,d)==layer_brute(n,d),(n,d)
            brute_checks += 1
    print('exact brute-force layer comparisons:',brute_checks,'PASS')
    try:
        for n in range(2,7):
            assert check_hull(n)==count_vertices(n),n
        print('independent numerical polytope comparisons: 5 PASS')
    except ImportError:
        print('SciPy missing: optional numerical polytope comparisons SKIPPED')
    print('complete vertex totals n=2..20:',[count_vertices(n) for n in range(2,21)])
    print('all required checks PASS')

if __name__=='__main__':
    main()
