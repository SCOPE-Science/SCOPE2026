#!/usr/bin/env python3
"""Standalone, finite corroboration of the matching-stretched balanced biclique theorem.

The mathematical proof is in RESULT.md. This script checks independent
shortest paths, exact quadratic-form identities, critical Gram ranks,
and high-precision asymptotics on finite test sets.
"""
from fractions import Fraction as F
from itertools import product
from heapq import heappush, heappop
from random import Random
from math import log, log2
import numpy as np
from scipy.optimize import brentq
import mpmath as mp


def dijkstra(n, s, src):
    mat = [[None] * (2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            w = s if i == j else F(1)
            mat[i][n+j] = mat[n+j][i] = w
    out = [None] * (2*n)
    out[src] = F(0)
    heap = [(F(0), src)]
    while heap:
        d, u = heappop(heap)
        if d != out[u]:
            continue
        for v in range(2*n):
            if mat[u][v] is None:
                continue
            new = d + mat[u][v]
            if out[v] is None or new < out[v]:
                out[v] = new
                heappush(heap, (new, v))
    assert all(x is not None for x in out)
    return out


def formula(n, s, i, j):
    if i == j:
        return F(0)
    if i//n == j//n:
        return F(2)
    return s if i%n == j%n else F(1)


def exact_identity(n, s, p, z):
    assert sum(z) == 0
    v = [x for x in z]
    Q = sum(v[i]*v[j]*formula(n,s,i,j)**p for i in range(2*n) for j in range(2*n))
    a = sum(v[:n], F(0))/n
    b = sum(v[n:], F(0))/n
    assert a+b == 0
    u = [v[i]-a for i in range(n)]
    w = [v[i+n]-b for i in range(n)]
    A = F(2)**p
    B = s**p
    E0 = (n-1)*(A-1)-B
    Eplus = B-A-1
    Eminus = 1-A-B
    S = sum((u[i]+w[i])**2 for i in range(n))/F(2)
    T = sum((u[i]-w[i])**2 for i in range(n))/F(2)
    rhs = 2*n*a*a*E0 + S*Eplus + T*Eminus
    assert Q == rhs, (n,s,p,Q,rhs)


def critical(n, s):
    if s > 2:
        g = brentq(lambda p:(s/2)**p - 1 - 2**(-p), .00001, 150, xtol=2e-14)
    else:
        g = float('inf')
    if np.isfinite(g):
        F_at_g = (n-2)*2**g - n
        if F_at_g <= 1e-10:
            return g, 'both' if abs(F_at_g)<1e-10 else 'plus'
        high = g
    else:
        high = 80
    f = brentq(lambda p:(n-1)*np.expm1(p*log(2)) - s**p, 1e-10, high, xtol=2e-14)
    return f, 'radial'


def mat_float(n,s,p):
    return np.array([[float(formula(n,F(str(s)),i,j))**p for j in range(2*n)] for i in range(2*n)])


def main():
    random=Random(24317)
    distance_cases=0
    exact_cases=0
    for n in range(3,9):
        for s in [F(1), F(5,4),F(3,2),F(2),F(9,4),F(5,2),F(11,4),F(3)]:
            for src in range(2*n):
                ds=dijkstra(n,s,src)
                assert all(ds[j] == formula(n,s,src,j) for j in range(2*n))
                distance_cases += 1
            for p in (1,2,3):
                for _ in range(6):
                    z=[F(random.randint(-7,7)) for k in range(2*n-1)]
                    z.append(-sum(z))
                    exact_identity(n,s,p,z)
                    exact_cases+=1
    print('EXACT_SHORTEST_PATH_METRIC_OK', distance_cases)
    print('EXACT_ZERO_SUM_DECOMPOSITION_OK', exact_cases)

    sstar = 4**(1/log2(3))
    pstar = log2(3)
    for n, s, p, expected_rank in [(3,sstar,pstar,2),(4,3,1,3)]:
        # Special cases admit exact powered distance matrices without irrational powers.
        A, B = (3,4) if n==3 else (2,3)
        D = np.zeros((2*n,2*n),dtype=float)
        for i in range(2*n):
            for j in range(2*n):
                if i==j: val=0
                elif i//n==j//n: val=A
                elif i%n==j%n: val=B
                else: val=1
                D[i,j]=val
        J=np.eye(2*n)-np.ones((2*n,2*n))/(2*n)
        ev=np.linalg.eigvalsh(-J@D@J/2)
        assert sum(x>1e-8 for x in ev)==expected_rank, (n,ev)
        assert max(abs(x) for x in ev[:2*n-expected_rank]) < 1e-8, (n,ev)
        print('EXACT_POWERED_RESONANCE_RANK_OK',n,'rank',expected_rank)

    mode_tests = 0
    for n in range(3,20):
        for s in [1,1.4,2,2.2,2.35,sstar,2.5,2.9,3]:
            p, mode = critical(n,s)
            E0 = (n-1)*(2**p-1) - s**p
            Eplus = s**p - 2**p - 1
            Eminus=1-2**p-s**p
            assert Eminus<0 and E0<1e-9 and Eplus<1e-9, (n,s,p,mode,E0,Eplus)
            assert abs(E0)<1e-8 or abs(Eplus)<1e-8
            if n==3:
                expected='radial' if s < sstar-1e-10 else ('plus' if s > sstar+1e-10 else 'both')
            elif n==4:
                expected='both' if s==3 else 'radial'
            else:
                expected='radial'
            assert mode==expected, (n,s,p,mode,expected)
            Q=mat_float(n,s,p)
            J=np.eye(2*n)-np.ones((2*n,2*n))/(2*n)
            E=np.linalg.eigvalsh(-J@Q@J/2)
            k=2*n-1-({'radial':1,'plus':n-1,'both':n}[mode])
            assert sum(E>1e-7)==k, (n,s,mode,k,E)
            mode_tests+=1
    print('POWERED_DISTANCE_CRITICAL_PHASES_AND_RANKS_OK',mode_tests)

    mp.mp.dps=75
    asym_cases=0
    for n in [100,250,600,1200]:
        N=mp.mpf(n-1); L2=mp.log(2)
        for s in [mp.mpf(1),mp.mpf(3)/2,mp.mpf(2),mp.mpf(3)]:
            pred=1/(N*L2) +(mp.log(s)/L2**2-1/(2*L2))/N**2
            p=mp.findroot(lambda x:(n-1)*mp.expm1(x*L2)-mp.exp(x*mp.log(s)),(pred*.95,pred*1.05))
            assert abs((p-pred)*N**3) < 10
            asym_cases+=1
    print('HIGH_PRECISION_ASYMPTOTIC_DIAGNOSTICS_OK',asym_cases)
    print('ALL_MATCHING_STRETCH_CHECKS_OK')

if __name__=='__main__':
    main()
