#!/usr/bin/env python3
"""Finite independent checks for weighted antipodal-cycle controllability.

Dependencies: numpy and sympy. The general claims have analytic proofs;
these finite tests are reproducibility checks, not an infinite proof.
"""
import math
import numpy as np
import sympy as sp

checks = 0

def check(condition, detail):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(detail)

def laplacian(n, g):
    size = 2*n
    L = np.zeros((size, size), dtype=float)
    # Construct edges directly, without using the Fourier eigenvalue formula.
    edges = [(j, (j+1) % size, 1.0) for j in range(size)]
    edges.extend((j, j+n, float(g)) for j in range(n))
    for a,b,w in edges:
        L[a,a] += w
        L[b,b] += w
        L[a,b] -= w
        L[b,a] -= w
    return L

def resonance_counts(n, g, tol=2e-8):
    t=math.pi/n
    four = sum(abs(g-(math.cos(o*t)-math.cos(e*t))) < tol
               for e in range(2,n,2) for o in range(1,e,2))
    three = sum(abs(g-(1+math.cos(o*t))) < tol for o in range(1,n,2)) if n%2==0 else 0
    return four,three

def exact_q(n,g):
    four,three=resonance_counts(n,g)
    return 4 if four else (3 if three else 2)

def spectral_blocks(vals, tol=5e-8):
    i=0
    while i<len(vals):
        j=i+1
        while j<len(vals) and abs(vals[j]-vals[i])<tol:
            j+=1
        yield i,j
        i=j

# Every resonant rate plus generic rates, through 48 vertices.
tested=0
for n in range(2,25):
    t=math.pi/n
    rates=[0.01, 0.13, 0.37, 0.71, 1.23, 1.8]
    if n%2==0:
        rates.extend(1+math.cos(o*t) for o in range(1,n,2))
    rates.extend(math.cos(o*t)-math.cos(e*t)
                 for e in range(2,n,2) for o in range(1,e,2))
    rates=sorted(set(round(g,12) for g in rates if g>0))
    for g in rates:
        N=2*n
        L=laplacian(n,g)
        check(np.max(np.abs(L-L.T))<1e-12 and
              np.max(np.abs(L.sum(axis=1)))<1e-12,(n,g,'L construction'))
        spectral=np.linalg.eigvalsh(L)
        reference=np.array(sorted(2-2*math.cos(math.pi*k/n) +
                                  (2*g if k%2 else 0)
                                  for k in range(N)))
        check(np.max(np.abs(spectral-reference))<1e-8,(n,g,'eigenvalues'))
        q=exact_q(n,g)
        check(q==max(j-i for i,j in spectral_blocks(spectral)),(n,g,'max multiplicity'))
        # PBH evaluated using independent Fourier modes at each eigenlevel.
        for i,j in spectral_blocks(spectral):
            ks=[k for k in range(N)
                if abs(2-2*math.cos(math.pi*k/n) +
                       (2*g if k%2 else 0)-spectral[i])<5e-8]
            check(len(ks)==j-i,(n,g,'mode count'))
            rows=np.array([[np.exp(1j*math.pi*k*s/n) for k in ks]
                            for s in range(q)])
            check(np.linalg.matrix_rank(rows,tol=1e-8)==len(ks),
                  (n,g,'PBH consecutive leaders',ks))
        tested+=1

# Independently evaluate projected eigenspace ranks for the two fixed inputs.
for n in range(2,21):
    t=math.pi/n
    first=(1-math.cos(t)) if n%2==0 else (math.cos(t)-math.cos(2*t))
    g=first
    L=laplacian(n,g)
    vals,V=np.linalg.eigh(L)
    reached=sum(np.linalg.matrix_rank(V[:2,i:j],tol=1e-8)
                for i,j in spectral_blocks(vals))
    n4,n3=resonance_counts(n,g)
    check(reached==2*n-2*n4-n3,(n,'two-input rank'))
    if n%2==0:
        check(n4==0 and n3==1 and reached==2*n-1,(n,'even first loss'))
    else:
        expected=1 if n==3 else 2
        check(n4==expected and n3==0 and reached==2*n-2*expected,
              (n,'odd first loss'))

# Direct rational Kalman matrix reconstruction (no spectral decomposition).
for n,g,expected in [(2,sp.Integer(1),3),(3,sp.Integer(1),4),
                     (4,sp.Rational(1,2),2)]:
    N=2*n
    L=sp.zeros(N)
    for j in range(N):
        k=(j+1)%N
        L[j,j]+=1;L[k,k]+=1;L[j,k]-=1;L[k,j]-=1
    for j in range(n):
        k=j+n
        L[j,j]+=g;L[k,k]+=g;L[j,k]-=g;L[k,j]-=g
    for q in (1,2,3,4):
        B=sp.eye(N)[:,:q]
        C=B
        A=B
        for _ in range(1,N):
            A=-L*A
            C=C.row_join(A)
        rank=C.rank()
        check((rank==N)==(q>=expected),(n,g,q,'exact Kalman rank',rank))

print(f'PASS {checks} checks; {tested} weighted graphs, direct eigenanalysis, Fourier PBH, direct Kalman ranks')
