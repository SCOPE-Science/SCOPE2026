#!/usr/bin/env python3
"""Numerical and LP cross-checks for the antipodal-cycle fastest-mixing theorem.
Dependencies: Python 3, NumPy, SciPy. Run `python verify.py`.
"""
import json
import math
import random
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog


def formula(m):
    if not isinstance(m, int) or m < 3:
        raise ValueError("m must be an integer >= 3")
    u = 2.0 * (1.0 - math.cos(math.pi / m))
    v = 2.0 * (1.0 - math.cos(2.0 * math.pi / m))
    delta = v - u
    eta = 4.0 - u if m % 2 == 0 else 4.0
    a = 2.0 / (eta + delta + v)
    b = 0.5 * delta * a
    mu = 1.0 - v * a
    weight = v / (2.0 * v + eta - u)
    middle = (eta - u) / (2.0 * v + eta - u)
    return a, b, mu, (weight, middle, weight), (u, v, eta)


def matrix(m, a, b):
    n = 2 * m
    P = np.zeros((n, n))
    for i in range(n):
        P[i, i] = 1.0 - 2.0 * a - b
        P[i, (i + 1) % n] = a
        P[i, (i - 1) % n] = a
        P[i, (i + m) % n] = b
    return P


def lp(m):
    n = 2*m
    ks = np.arange(1, n)
    tt = 2.0 * (1.0 - np.cos(np.pi*ks / m))
    uu = 1.0 - np.where(ks % 2 == 0, 1.0, -1.0)
    # Variables (a,b,s), inequalities +- eigenvalue <= s, 2a+b <= 1.
    A = np.concatenate([np.column_stack([-tt, -uu, -np.ones(n-1)]),
                        np.column_stack([tt, uu, -np.ones(n-1)]),
                        [[2.0, 1.0, 0.0]]], axis=0)
    B = np.concatenate([-np.ones(n-1), np.ones(n-1), [1.0]])
    r = linprog([0.0, 0.0, 1.0], A_ub=A, b_ub=B,
                bounds=[(0, None), (0, None), (0, None)], method="highs")
    assert r.success, r.message
    return r.x

checks = {"full_matrix_vs_fourier":0,"independent_LP_optima":0,
          "dual_certificates":0,"asymmetric_feasible_trials":0,
          "candidate_feasible_and_all_modes":0}
max_error = 0.0
for m in range(3, 101):
    n = 2*m
    a,b,mu,(w1,w2,w3),(u,v,eta)=formula(m)
    assert a>0 and b>0 and 2*a+b < 1.0
    ks=np.arange(1,n)
    eig=1-a*2*(1-np.cos(np.pi*ks/m))-b*(1-(-1.)**ks)
    assert abs(np.max(np.abs(eig))-mu)<2e-12
    assert all(-mu-2e-12<=e<=mu+2e-12 for e in eig)
    checks["candidate_feasible_and_all_modes"]+=1
    assert w1>0 and w2>0 and w3>0 and abs(w1+w2+w3-1)<1e-12
    assert abs(w1*(-u)+w2*(-v)+w3*eta)<2e-12
    assert abs(w1*(-2)+w3*2)<2e-12
    assert abs(w2-mu)<2e-12
    checks["dual_certificates"]+=1
    sol=lp(m)
    assert np.max(np.abs(sol-[a,b,mu]))<2e-7,(m,sol,[a,b,mu])
    checks["independent_LP_optima"]+=1
    if m<=18:
        P=matrix(m,a,b)
        assert np.max(np.abs(P-P.T))<1e-14
        assert np.min(P)>-1e-14
        assert np.max(np.abs(P.sum(axis=1)-1))<1e-13
        eig1=np.linalg.eigvalsh(P)
        eig2=np.r_[1.0, eig]
        err=np.max(np.abs(np.sort(eig1)-np.sort(eig2)))
        max_error=max(max_error,float(err))
        assert err<1e-12
        assert abs(max(abs(eig1[0]),abs(eig1[-2]))-mu)<1e-12
        checks["full_matrix_vs_fourier"]+=1

rng=random.Random(20261025)
# Independent random edge-specific feasible allocations on Möbius ladder, no orbit invariance.
for m in range(3,8):
    n=2*m
    a,b,mu,_,_=formula(m)
    for j in range(240):
        rawcycle=[rng.random() for _ in range(n)]
        rawrungs=[rng.random() for _ in range(m)]
        scale=rng.random()/3.0
        P=np.zeros((n,n))
        for i in range(n):
            x=scale*rawcycle[i]
            P[i,(i+1)%n]+=x
            P[(i+1)%n,i]+=x
        for i in range(m):
            x=scale*rawrungs[i]
            P[i,i+m]+=x
            P[i+m,i]+=x
        np.fill_diagonal(P,1.0-P.sum(axis=1))
        assert np.min(P)>=-1e-14
        ev=np.linalg.eigvalsh(P)
        s=max(abs(ev[0]),abs(ev[-2]))
        assert s>=mu-3e-12,(m,j,s,mu)
        checks["asymmetric_feasible_trials"]+=1

# Exact characteristic eigenvalues and exact SLEM for the edge-transitive case m=3:
# a=b=2/9, eigenvalues 1, 1/3 (mult.4), -1/3 (mult.1).
assert Fraction(2,9)*3 < 1
assert Fraction(1,3) == Fraction(1,1)-Fraction(2,9)*3
assert Fraction(-1,3) == Fraction(1,1)-Fraction(2,9)*6

# Both parity subsequences have n^-2 matching weights and 4x cycle spectral gap.
for m in (200,201,400,401,800,801):
    a,b,mu,_,(u,v,eta)=formula(m)
    mu_cycle=(4-u)/(4+u)
    ratio=(1-mu)/(1-mu_cycle)
    assert 3.995 < ratio < 4.001,(m,ratio)
    assert abs(m*m*b-3*math.pi**2/4)<0.005

print(json.dumps({"status":"VERIFY_OK","checks":checks,
                  "largest_matrix_fourier_absolute_error":max_error,
                  "m_range_for_LP_and_certificate":[3,100],
                  "m_range_full_spectrum":[3,18],
                  "asymmetric_trials_seed":20261025,
                  "scope":"Finite corroboration only; infinite-family and asymptotic statements require the supplied proof."},
                 sort_keys=True,indent=2))
