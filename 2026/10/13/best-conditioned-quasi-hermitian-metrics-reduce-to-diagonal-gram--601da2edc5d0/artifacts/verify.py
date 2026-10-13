#!/usr/bin/env python3
import math, random

def inv(A):
    n=len(A)
    M=[row[:] + [1.0 if i==j else 0.0 for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        p=max(range(k,n), key=lambda i: abs(M[i][k]))
        M[k],M[p]=M[p],M[k]
        piv=M[k][k]
        if abs(piv)<1e-12: raise ValueError('singular')
        M[k]=[x/piv for x in M[k]]
        for i in range(n):
            if i!=k:
                a=M[i][k]
                M[i]=[x-a*y for x,y in zip(M[i],M[k])]
    return [row[n:] for row in M]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mt(A): return [list(r) for r in zip(*A)]
def maxabs(A): return max(abs(x) for r in A for x in r)
def sub(A,B): return [[a-b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]

def jacobi_eigs(A):
    A=[r[:] for r in A]
    n=len(A)
    for _ in range(200*n*n):
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        if not pairs: break
        p,q=max(pairs, key=lambda ij: abs(A[ij[0]][ij[1]]))
        if abs(A[p][q])<1e-12: break
        phi=0.5*math.atan2(2*A[p][q], A[q][q]-A[p][p])
        c,s=math.cos(phi),math.sin(phi)
        for k in range(n):
            apk,aqk=A[p][k],A[q][k]
            A[p][k],A[q][k]=c*apk-s*aqk,s*apk+c*aqk
        for k in range(n):
            akp,akq=A[k][p],A[k][q]
            A[k][p],A[k][q]=c*akp-s*akq,s*akp+c*akq
    return sorted(A[i][i] for i in range(n))

def cond_spd(A):
    e=jacobi_eigs(A)
    return e[-1]/e[0]

def diag(vals):
    n=len(vals)
    return [[vals[i] if i==j else 0.0 for j in range(n)] for i in range(n)]

# Exact two-dimensional optimum across representative overlaps and a broad family of admissible metrics.
for c in [0.0,0.1,0.3,0.6,0.9,0.99]:
    s=math.sqrt(1-c*c)
    V=[[1.0,c],[0.0,s]]
    eta_star=inv(mm(V,mt(V)))
    target=(1+c)/(1-c)
    assert abs(cond_spd(eta_star)-target) < 2e-9*max(1,target)
    x=c/s if s else 0.0
    floor=x*x
    for k in range(-80,81):
        d=floor + math.exp(k/12)
        eta=[[1.0,-x],[-x,d]]
        assert cond_spd(eta) + 2e-9 >= target

# General-dimensional identity and pairwise lower bound on random real instances.
rng=random.Random(1729)
trials=0
for n in [3,4,6]:
    for _ in range(30):
        while True:
            V=[[rng.uniform(-1,1) for _ in range(n)] for __ in range(n)]
            for j in range(n):
                z=math.sqrt(sum(V[i][j]**2 for i in range(n)))
                for i in range(n): V[i][j]/=z
            try: Vi=inv(V); break
            except ValueError: pass
        weights=[math.exp(rng.uniform(-1.5,1.5)) for _ in range(n)]
        D=diag(weights)
        eta=mm(mt(Vi),mm(D,Vi))
        G=mm(mt(V),V)
        S=diag([w**-0.5 for w in weights])
        scaled=mm(S,mm(G,S))
        kappa=cond_spd(eta)
        assert abs(kappa-cond_spd(scaled)) < 3e-7*max(1,kappa)
        cmax=max(abs(G[i][j]) for i in range(n) for j in range(i+1,n))
        bound=(1+cmax)/(1-cmax)
        assert kappa + 2e-7 >= bound
        Lam=diag([i+1.0 for i in range(n)])
        H=mm(V,mm(Lam,Vi))
        lhs=mm(mt(H),eta); rhs=mm(eta,H)
        scale=max(1.0,maxabs(lhs),maxabs(rhs))
        assert maxabs(sub(lhs,rhs))/scale < 2e-11
        trials+=1
print(f'VERIFY_OK two_dim_overlaps=6 general_trials={trials}')
