#!/usr/bin/env python3
"""Independent numerical spectral tests for finite-partition fractional heat theorem.
Requires numpy and scipy; symbolic analytical proof is in RESULT.md.
"""
import math
import random
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq


def spectral_matrix(parts, exponent, t):
    N = sum(parts)
    L = np.zeros((N, N), dtype=float)
    cuts = [0]
    for k in parts: cuts.append(cuts[-1] + k)
    for i in range(N):
        for j in range(N):
            if i != j and not any(cuts[g] <= i < cuts[g+1] and cuts[g] <= j < cuts[g+1] for g in range(len(parts))):
                L[i,j] = -1.
        L[i,i] = -sum(L[i,:])
    eigs, Q = eigh(L)
    assert min(eigs) > -2e-10
    eigs[np.abs(eigs)<1e-8] = 0.0  # Exact combinatorial zero eigenvalue.
    weights = np.exp(-t * np.maximum(eigs, 0)**exponent)
    return (Q * weights) @ Q.T


def formula_matrix(parts, exponent, t):
    N = sum(parts)
    z = math.exp(-t * N**exponent)
    T = np.full((N, N), (1-z)/N, dtype=float)
    offset = 0
    for k in parts:
        x = math.exp(-t * (N-k)**exponent)
        off = (1-z)/N + (z-x)/k
        T[offset:offset+k, offset:offset+k] = off
        for i in range(offset, offset+k): T[i,i] += x
        offset += k
    return T


def row_formula(parts, exponent, t):
    N = sum(parts)
    z = math.exp(-t * N**exponent)
    return 1 + 2*max((k-1)*max(0., -((1-z)/N + (z-math.exp(-t*(N-k)**exponent))/k)) for k in parts)


def shape(parts, exponent):
    N = sum(parts)
    out = []
    for k in parts:
        if k < 2: continue
        u = k/N
        q = 1-u
        a = q**exponent
        if exponent <= 1: continue
        speak = math.log(q/a)/(1-a)
        h = lambda s: u + q*math.exp(-s)-math.exp(-a*s)
        assert h(speak) < 0
        high = max(2*speak, 1.)
        while h(high) <= 0: high *= 2
        szero = brentq(h, speak, high, xtol=1e-13)
        peak = math.exp(-a*speak)-u-q*math.exp(-speak)
        out.append((k, speak/N**exponent, szero/N**exponent, 2*(1-1/k)*peak))
    return out


def run():
    total=0
    rng = random.Random(3022)
    cases = [[2,2], [4,1,3], [2,3,4], [1,1,2], [5,2,1], [6,3,2,1], [3,3,3], [1,1,1,1], [1,7,2]]
    cases += [[rng.randint(1,5) for _ in range(rng.randint(2,5))] for _ in range(36)]
    for parts in cases:
        for a in [0.35, 1., 1.035, 1.3, 2., 3.]:
            data = shape(parts, a)
            times = [0., 0.00013, 0.002, 0.04, 0.3, 2.]
            for _, theta,tau,_ in data:
                times.extend([0.3*theta,theta,(theta+tau)/2,tau*1.15])
            for t in times:
                T=formula_matrix(parts,a,t)
                Q=spectral_matrix(parts,a,t)
                assert np.max(np.abs(T-Q)) < 2e-9, (parts,a,t,np.max(np.abs(T-Q)))
                total += 1
                val=float(np.abs(Q).sum(axis=1).max())
                val2=row_formula(parts,a,t)
                assert abs(val-val2) < 2e-9, (parts,a,t,val,val2)
                total += 1
                assert np.max(np.abs(Q.sum(axis=1)-1))<2e-10
                total+=1
                if a <= 1 and t>0:
                    assert np.min(Q)>-1e-9
                    total+=1
            if a>1 and data:
                threshold=max(z[2] for z in data)
                theta,amp=max(((z[1],z[3]) for z in data),key=lambda o:o[1])
                assert row_formula(parts,a,theta)>1.00000001
                total+=1
                assert all(z[2] > z[1] >0 for z in data)
                total+=1
                assert row_formula(parts,a,threshold*1.001)<1+1e-10
                total+=1
    # Near-critical quantitative limits on several nonbalanced graphs.
    for parts in [[4,1,3],[2,3,4],[6,3,2,1]]:
        N=sum(parts)
        nondiag=[k for k in parts if k>=2]
        delay_coefficient=(2/N)*max((-math.log(1-k/N))/(k/N) for k in nondiag)
        amp_coefficient=max((1-1/k)*((1-k/N)*math.log(1-k/N)**2)/(k/N) for k in nondiag)
        for eps in [.02,.01,.005]:
            data=shape(parts,1+eps)
            tau=max(z[2] for z in data)
            excess=max(z[3] for z in data)
            assert abs(tau/eps/delay_coefficient-1)<0.11
            assert abs(excess/eps**2/amp_coefficient-1)<0.11
            total+=2
    print('PASS',total,'spectral, norm, positivity and critical-scale assertions')

if __name__=='__main__':run()
