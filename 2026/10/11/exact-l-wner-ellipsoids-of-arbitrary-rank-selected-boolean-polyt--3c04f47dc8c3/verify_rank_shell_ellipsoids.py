#!/usr/bin/env python3
"""Standalone finite checks for Löwner ellipsoids of S-hypersimplices.
Run: python3 verify_rank_shell_ellipsoids.py [maximum_dimension]
Python standard library only. Numerical checks illustrate, not certify, the proof.
"""
from itertools import combinations
from fractions import Fraction
from math import comb, log, sqrt
import sys


def circle_feasible(n, s):
    a, b = s[0], s[-1]
    x = Fraction(n, 2)
    y = Fraction(n * (n + 1), 4)
    if x < a or x > b:
        return False
    upper = (a + b) * x - a * b
    lo, hi = max(u for u in s if u <= x), min(u for u in s if u >= x)
    lower = (lo + hi) * x - lo * hi
    return lower <= y <= upper


def edge_opt(n, a, b):
    a0, a1 = a * (n - a), b * (n - b)
    if a0 == 0 and a1 == 0:
        return None
    d = a1 - a0
    def der_sign(p):
        return a0 + (n*d - 2*a0)*p - (n+1)*d*p*p
    lo, hi = 0.0, 1.0
    for _ in range(90):
        md = (lo + hi)/2
        if der_sign(md) >= 0:
            lo = md
        else:
            hi = md
    p = (lo + hi)/2
    mu = a + p*(b-a)
    v = p*(1-p)*(b-a)**2
    t = (1-p)*a0 + p*a1
    if v <= 0 or t <= 0:
        raise AssertionError((n,a,b,p,v,t))
    logdet = log(v) + (n-1)*log(t/(n-1))
    return logdet,p,mu,v,t


def solve(n,s):
    if circle_feasible(n,s):
        return 'cube',n/2,n/4,n*(n-1)/4,None
    edges = list(zip(s[:-1],s[1:])) + [(s[0],s[-1])]
    candidates=[(edge_opt(n,a,b), (a,b)) for a,b in set(edges)]
    candidates=[(r,edge) for r,edge in candidates if r is not None]
    if not candidates:
        raise AssertionError((n,s,'no edge'))
    best, edge=max(candidates,key=lambda z:z[0][0]); _,p,mu,v,t=best
    return edge,mu,v,t,p


def leverage(n,j,mu,v,t):
    return ((j-mu)**2/v+(n-1)*j*(n-j)/t) if v*t>0 else float('inf')


def main():
    nmax=int(sys.argv[1]) if len(sys.argv)>1 else 10
    cases=0; checked_ranks=0; covered_vertices=0
    examples=[]
    for n in range(2,nmax+1):
        for mask in range(1,1<<(n+1)):
            s=tuple(j for j in range(n+1) if mask>>j&1)
            if len(s)<2 or s==(0,n):
                continue
            edge,mu,v,t,p=solve(n,s)
            cases+=1
            for j in s:
                checked_ranks+=1
                covered_vertices+=comb(n,j)
                if edge=='cube':
                    assert abs(mu-n/2)<1e-10
                    continue
                L=leverage(n,j,mu,v,t)
                assert L<=n+2e-7, (n,s,edge,j,L,n)
                if j in edge:
                    assert abs(L-n)<2e-7,(n,s,edge,j,L)
            if n==8 and s==(0,1,5):
                examples.append((n,s,edge,mu,v,t,p,leverage(n,0,mu,v,t)))
    assert examples and examples[0][2]==(1,5), examples
    print('PASS n=2..%d, %d full-dimensional S-hypersimplices; %d checked rank layers; %d vertex incidences.'%(nmax,cases,checked_ranks,covered_vertices))
    print('Nonextremal contact example n=8 S=(0,1,5):',examples[0])


if __name__=='__main__':
    main()
