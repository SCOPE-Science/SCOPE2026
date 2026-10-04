#!/usr/bin/env python3
import cmath
import math
import numpy as np

TOL = 2e-9

def windows(N, s=None):
    if s is None:
        s = N//2
    out=[]
    if N % 2:
        ds=list(range(1,(N-1)//2+1))
        for d in ds[:min(s,len(ds))]:
            g=np.zeros(N,dtype=complex); g[0]=1; g[d]=2; g/=np.linalg.norm(g); out.append(g)
        while len(out)<s:
            out.append(out[0].copy())
    else:
        nonant=list(range(1,N//2))
        take=min(s,len(nonant))
        for d in nonant[:take]:
            g=np.zeros(N,dtype=complex); g[0]=1; g[d]=2; g/=np.linalg.norm(g); out.append(g)
        if len(out)<s:
            d=N//2
            g=np.zeros(N,dtype=complex); g[0]=1; g[d]=2*cmath.exp(1j*math.pi/4); g/=np.linalg.norm(g); out.append(g)
        while len(out)<s:
            out.append(out[0].copy())
    return out

def ambiguity(g,a,b):
    N=len(g); w=cmath.exp(2j*math.pi/N)
    total=0j
    # (T_a g)[j] = g[j-a], (M_b h)[j] = w^(bj) h[j]
    for j in range(N):
        total += g[j].conjugate() * (w**(b*j)) * g[(j-a)%N]
    return total

def joint_nonzero_count(gs):
    N=len(gs[0]); c=0
    for a in range(N):
        for b in range(N):
            if any(abs(ambiguity(g,a,b))>TOL for g in gs): c+=1
    return c

def gabor_projector_span_rank(gs):
    N=len(gs[0]); w=cmath.exp(2j*math.pi/N)
    rows=[]
    for g in gs:
        for a in range(N):
            Tg=np.roll(g,a)
            for b in range(N):
                phase=np.array([w**(b*j) for j in range(N)])
                h=phase*Tg
                P=np.outer(h,h.conjugate())
                rows.append(P.reshape(-1))
    A=np.stack(rows,axis=0)
    return int(np.linalg.matrix_rank(A,tol=1e-8))

def predicted(N,s):
    return N*min(N,1+2*s)

def support_size(g):
    return int(np.count_nonzero(np.abs(g)>TOL))

cases=0
rank_cases=0
for N in range(2,21):
    threshold=N//2
    for s in range(1,threshold+2):
        gs=windows(N,s)
        assert all(support_size(g)==2 for g in gs)
        c=joint_nonzero_count(gs)
        assert c==predicted(N,s),(N,s,c,predicted(N,s))
        cases += 1
        if N<=10:
            r=gabor_projector_span_rank(gs)
            assert r==c,(N,s,r,c)
            rank_cases += 1
    gs=windows(N,threshold)
    assert joint_nonzero_count(gs)==N*N

# independent combinatorial lower-bound replay: with s support-pairs, no union of
# difference rows can exceed 1+2s, and an even antipodal difference only contributes 1.
# Exhaust all support-pair subsets for N<=9 and compare their best row coverage.
from itertools import combinations
for N in range(2,10):
    pairs=list(combinations(range(N),2))
    threshold=N//2
    for s in range(1,min(threshold,len(pairs))+1):
        best=0
        for fam in combinations(pairs,s):
            rows={0}
            for u,v in fam:
                d=(v-u)%N
                rows.add(d); rows.add((-d)%N)
            best=max(best,len(rows))
        assert best==min(N,1+2*s),(N,s,best)

print(f"VERIFY_OK ambiguity_cases={cases} projector_rank_cases={rank_cases} exhaustive_support_N=2..9")
