#!/usr/bin/env python3
"""Standalone finite-cycle covering CDF and asymptotic identity checks.

Python 3.10+ and mpmath required; enumerations use exact rational arithmetic.
"""
import itertools
import math
import random
from fractions import Fraction
import mpmath as mp


def mul(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def matpow(a, L):
    n = len(a)
    v = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    while L:
        if L & 1:
            v = mul(v, a)
        a = mul(a, a)
        L //= 2
    return v


def transfer(n, ell, q):
    a = [[Fraction(0) for _ in range(ell)] for _ in range(ell)]
    for i in range(ell):
        a[i][0] = 1-q
        if i + 1 < ell:
            a[i][i+1] = q
    v = matpow(a, n)
    return sum(v[i][i] for i in range(ell))


def brute(n, ell, q):
    p = Fraction(0)
    for bits in itertools.product((0, 1), repeat=n):
        if any(all(bits[(s+j) % n] == 0 for j in range(ell)) for s in range(n)):
            continue
        k = sum(bits)
        p += q**(n-k)*(1-q)**k
    return p


def lambda_dom(ell, q):
    q = mp.mpf(q)
    target = (1-q)*q**ell
    delta = target
    for _ in range(100):
        nxt = target/(1-delta)**ell
        if mp.fabs(nxt-delta) < mp.mpf('1e-85'):
            delta=nxt
            break
        delta=nxt
    return 1-delta


def p_analytic(n, ell, x):
    q=mp.exp(-mp.mpf(x)/ell)/mp.power(n, mp.mpf(1)/ell)
    if not 0<q<1:
        raise ValueError('q out of range')
    # Exact transfer trace via eigenvalue computation to guard the dominant-root approximation.
    ma=mp.matrix(ell)
    for j in range(ell):
        ma[j,0]=1-q
        if j+1<ell:
            ma[j,j+1]=q
    ev=mp.eig(ma,left=False,right=False)
    exact=mp.re(sum(z**n for z in ev))
    return exact,q


def run():
    checks=0
    for ell in range(2, 6):
        for n in range(ell, 11):
            for q in (Fraction(1, 3),Fraction(2, 5),Fraction(3, 7)):
                t = transfer(n,ell,q)
                b = brute(n,ell,q)
                assert t == b, (ell,n,q,t,b)
                checks+=1
    print('exact rational exhaustive checks:', checks)
    mp.mp.dps=95
    for ell in (2,3,4):
        for x in (-1,0,1):
            ratios=[]
            for n in (2**(ell*3),2**(ell*4),2**(ell*5)):
                if n>1048576:
                    continue
                P,q=p_analytic(n,ell,x)
                leading = mp.exp(-mp.exp(-x))
                ans = mp.power(n,mp.mpf(1)/ell)*(P/leading-1)
                goal=mp.exp(-(1+mp.mpf(1)/ell)*x)
                ratios.append((n, float(ans),float(goal)))
                # For the selected sizes root-only error must be tiny.
                root=lambda_dom(ell,q)
                assert mp.fabs(P-root**n) < mp.mpf('1e-20')
                checks+=1
            print('asymptotic correction', 'ell',ell,'x',x,ratios)
    # Check two-term log eigenvalue asymptotic, including sign of the q^(ell+1) coefficient.
    for ell in (2,3,4,5):
        for iq in range(3,7):
            q=mp.power(10,-iq)
            logdom=mp.log(lambda_dom(ell,q))
            remainder=logdom+q**ell-q**(ell+1)
            assert mp.fabs(remainder) < 50*q**(2*ell)
            checks+=1
    # Direct kinetic construction: attempts arrive at independent Exp(1) clocks,
    # and a proposed arc is retained only if it covers a previously uncovered site.
    rng=random.Random(40612026)
    for ell,n,t in ((2,12,1.0),(3,12,1.0),(2,20,1.5)):
        p=float(transfer(n,ell,Fraction(str(math.exp(-t)))))
        successes=0
        repetitions=40000
        for _ in range(repetitions):
            times=[rng.expovariate(1.0) for _ in range(n)]
            covered=[False]*n
            for i in sorted(range(n),key=lambda j:times[j]):
                if times[i]>t: break
                arc=[(i+k)%n for k in range(ell)]
                if any(not covered[j] for j in arc):
                    for j in arc: covered[j]=True
            successes+=int(all(covered))
        est=successes/repetitions
        assert abs(est-p)<0.017, (ell,n,t,est,p)
        checks+=1
        print('independent kinetic Monte Carlo',ell,n,t, 'estimate',round(est,5),'theory',round(p,5))
    print('TOTAL PASS ASSERTIONS:', checks)


if __name__=='__main__':
    run()
