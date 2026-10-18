#!/usr/bin/env python3
"""Exact finite checks for the Pólya-urn total-run likelihood-ratio theorem.
Run: python3 polya_runs_checker.py. Uses Python standard library only.
Finite checks supplement, and do not replace, the theorem's proof.
"""
from fractions import Fraction as F
from math import comb
from itertools import product


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def rise(a, k):
    y = F(1)
    for j in range(k):
        y *= a + j
    return y


def count(n, b, r):
    if b == 0:
        return 2 if r == 1 else 0  # two constant words
    if r == 1:
        return 0
    s = r // 2
    t = choose(b - 1, s - 1) * choose(n - b - 1, s - 1)
    if r % 2 == 0:
        return 2 * t * (2 if b < n-b else 1)  # folded b, both compositions
    return (n - 2*s) * t // s * (2 if b < n-b else 1)


def composition_count(n, b, r):
    if b == 0:
        return 1 if r == 1 else 0
    if r == 1:
        return 0
    s = r // 2
    x = choose(b-1, s-1) * choose(n-b-1, s-1)
    if r % 2 == 0:
        return 2*x
    return (n-2*s)*x//s


def run_distribution(n, a):
    denom = rise(2*a, n)
    return [sum(F(2 if b < n-b else 1) * choose(n,b) * rise(a,b)*rise(a,n-b)/denom
                * F(composition_count(n,b,r), choose(n,b))
                for b in range(n//2+1)) for r in range(1,n+1)]


def check():
    checks = 0
    for n in range(2, 12):
        counts = [[0]*(n+1) for _ in range(n//2+1)]
        for word in product((0,1), repeat=n):
            b = min(sum(word),n-sum(word))
            r = 1 + sum(word[j]!=word[j-1] for j in range(1,n))
            counts[b][r] += 1
        for b in range(n//2+1):
            for r in range(1,n+1):
                assert counts[b][r] == count(n,b,r), (n,b,r)
                checks+=1
    for n in range(2,36):
        for b in range(n//2):
            for r in range(1,n):
                a=F(composition_count(n,b,r),choose(n,b))
                d=F(composition_count(n,b+1,r),choose(n,b+1))
                x=F(composition_count(n,b,r+1),choose(n,b))
                y=F(composition_count(n,b+1,r+1),choose(n,b+1))
                assert a*y >= x*d, ('kernel not TP2',n,b,r)
                checks+=1
    alphas = (F(1,4), F(1,2), F(1), F(3,2), F(3), F(8))
    for n in range(2,29):
        probs=[run_distribution(n,a) for a in alphas]
        for i in range(len(alphas)-1):
            f,g=probs[i],probs[i+1]
            assert sum(f)==sum(g)==1
            for r in range(n-1):
                assert f[r]*g[r+1]>=f[r+1]*g[r], ('mixture not TP2',n,i,r)
                checks+=1
                if r%2==1:  # r index 1 means r=2, plateau (2,3)
                    assert f[r]*g[r+1]==f[r+1]*g[r], ('plateau',n,i,r)
                    checks+=1
                else:
                    assert f[r]*g[r+1]>f[r+1]*g[r], ('strict step',n,i,r)
                    checks+=1
            E=sum((r+1)*f[r] for r in range(n))
            assert E==1+F(n-1)*alphas[i]/(2*alphas[i]+1)
            checks+=1
    return checks

if __name__=='__main__':
    print('Exact checks passed:',check())
