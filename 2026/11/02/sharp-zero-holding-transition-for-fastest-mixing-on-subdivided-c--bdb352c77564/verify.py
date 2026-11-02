"""Reproduce exact and numerical checks for optimal mixing on edge-subdivided bicliques.
Run with Python 3 and NumPy: python verify.py
"""
from fractions import Fraction
import math
import random
import numpy as np

CHECKS = 0

def check(cond, description):
    global CHECKS
    if not cond:
        raise AssertionError(description)
    CHECKS += 1

def spectral_formula(p, q, a, b):
    # Diagonal blocks for left/right vertex deviations and edge-interaction modes.
    d = 1-a-b
    Z = np.array([[1-q*a, 0, math.sqrt(q)*a],
                  [0, 1-p*b, math.sqrt(p)*b],
                  [math.sqrt(q)*a, math.sqrt(p)*b, d]], dtype=float)
    X = np.array([[1-q*a, math.sqrt(q)*a],
                  [math.sqrt(q)*a,d]], dtype=float)
    Y = np.array([[1-p*b, math.sqrt(p)*b],
                  [math.sqrt(p)*b,d]], dtype=float)
    val = list(np.linalg.eigvalsh(Z))
    val += list(np.linalg.eigvalsh(X))*(p-1)
    val += list(np.linalg.eigvalsh(Y))*(q-1)
    val += [d]*((p-1)*(q-1))
    return np.array(sorted(val))

def full_matrix(p,q,a,b):
    N=p+q+p*q
    P=np.zeros((N,N),dtype=float)
    for i in range(p):
        for j in range(q):
            k=p+q+i*q+j
            P[i,k]=P[k,i]=a
            P[p+j,k]=P[k,p+j]=b
    for v in range(N):
        P[v,v] = 1-P[v].sum()
    return P

def slem(vals):
    # For any stochastic matrix in these experiments, the top eigenvalue is 1.
    e=np.sort(vals)
    check(abs(e[-1]-1)<1e-10,'top eigenvalue must be 1')
    return max(abs(e[:-1]))

def f_opt(p,q):
    s=1/p+1/q
    d=1-s
    return (d+math.sqrt(d*d+4/p))/2

def is_good(p,q):
    return (p>=3 or q>=4)

# Exact arithmetic check of the decisive threshold and its complete classification.
for p in range(2,26):
    for q in range(p,41):
        s=Fraction(1,p)+Fraction(1,q)
        polynomial=2*s*s-s-Fraction(1,p)
        check((polynomial <=0)==is_good(p,q), f'exact threshold {p=} {q=}')

# The four invariant types exhaust the actual full symmetric transition matrix.
for p in range(2,9):
    for q in range(p,12):
        for a,b in [(1/q,1/p), (.37/q,.52/p),(.83/q,.67/p)]:
            P=full_matrix(p,q,a,b)
            ev=np.linalg.eigvalsh(P)
            blocks=spectral_formula(p,q,a,b)
            check(len(ev)==len(blocks),f'multiplicity {p,q}')
            check(np.max(np.abs(ev-blocks)) < 2e-12, f'eigenblocks {p,q,a,b}')
            check(np.max(abs(P.sum(axis=1)-1))<3e-14, 'row stochastic')
            check(np.min(P)>-1e-13,'entrywise nonnegative')

# The endpoint formula and randomized feasible symmetric-orbit comparisons.
rng=random.Random(21371)
for p in range(2,13):
    for q in range(p,15):
        sat=slem(np.linalg.eigvalsh(full_matrix(p,q,1/q,1/p)))
        target=f_opt(p,q)
        if is_good(p,q):
            check(abs(sat-target)<2e-12,f'saturated optimizer {p,q}')
            for j in range(20):
                a=rng.random()/q
                b=rng.random()/p
                mu=slem(np.linalg.eigvalsh(full_matrix(p,q,a,b)))
                check(mu>=target-1e-11,f'random orbit optimum {p,q,j}')
        else:
            check(sat>target+0.02, f'exception mismatch {p,q}')
            a,b=.99/q,.99/p
            check(slem(np.linalg.eigvalsh(full_matrix(p,q,a,b)))<sat-1e-3,
                  f'exception saturation must be improvable {p,q}')

# Random non-orbit-invariant feasible chains: randomly reduce each incidence weight
# from the saturating feasible matrix, then recompute the holding probabilities.
for p,q in [(2,4),(3,3),(3,6),(4,7),(6,9)]:
    target=f_opt(p,q)
    for j in range(35):
        N=p+q+p*q
        P=np.zeros((N,N))
        for i in range(p):
            for k in range(q):
                v=p+q+i*q+k
                aa=rng.random()/q
                bb=rng.random()/p
                P[i,v]=P[v,i]=aa
                P[p+k,v]=P[v,p+k]=bb
        for v in range(N): P[v,v]=1-P[v].sum()
        check(np.min(P)>=-2e-14, 'arbitrary feasibility')
        mu=slem(np.linalg.eigvalsh(P))
        check(mu>=target-1e-11,'arbitrary global lower bound')

# A direct check of the asymptotic coefficient for fixed p and large q.
for p in [2,3,5,10]:
    for q in [2000,5000,10000]:
        err=(1-f_opt(p,q))*q-p/(p+1)
        check(abs(err)<.004,'asymptotic fixed p')

print('PASS',CHECKS,'exact-arithmetic and numerical assertions')
