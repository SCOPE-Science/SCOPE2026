#!/usr/bin/env python3
"""Independent finite checks of commuting two-local qubit-Pauli Gibbs classification.
Run: python3 verify.py (requires numpy).
Universal proof is algebraic; checks are finite corroboration only.
"""
from itertools import combinations
from math import log,asinh,exp
from random import Random
import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.diag([1,-1]).astype(complex)
P=[I,X,Y,Z]

def paulistr(n):
    for i in range(n):
        for a in (1,2,3):
            p=[0]*n;p[i]=a;yield tuple(p)
    for i,j in combinations(range(n),2):
        for a in (1,2,3):
            for b in (1,2,3):
                p=[0]*n;p[i]=a;p[j]=b;yield tuple(p)

def commutes(a,b):
    return sum(x*y!=0 and x!=y for x,y in zip(a,b))%2==0

def verify_structural(terms):
    n=len(terms[0])
    dual=[]
    for v in range(n):
        alph={p[v] for p in terms if p[v]}
        if len(alph)>=2:dual.append(v)
    for v in dual:
        witness=[p for p in terms if p[v]]
        if len(witness)>3:return False
        partners={tuple(i for i,x in enumerate(p) if x!=0) for p in witness}
        if len(partners)!=1:return False
        uv=next(iter(partners))
        if len(uv)!=2:return False
        if any(i not in dual for i in uv):return False
        if len({p[uv[0]] for p in witness})!=len(witness):return False
        if len({p[uv[1]] for p in witness})!=len(witness):return False
    return True

count=0
for n,lim in [(3,4),(4,3)]:
    terms=list(paulistr(n));
    for k in range(1,lim+1):
        for group in combinations(terms,k):
            if all(commutes(a,b) for a,b in combinations(group,2)):
                assert verify_structural(group),(n,group)
                count+=1

rng=Random(1551)
# Each Bell projector (I + c1 XX + c2 YY + c3 ZZ)/4, eigen-sign triples product=-1.
BELL_SIGNS=[(-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1)]
assert all(a*b*c==-1 for a,b,c in BELL_SIGNS)
XX=np.kron(X,X); YY=np.kron(Y,Y); ZZ=np.kron(Z,Z)
partial_checks=0
for k in [1,2,3]:
    for _ in range(2200):
        h=[rng.uniform(-1,1) for j in range(k)]+[0.0]*(3-k)
        beta=rng.uniform(0,1.5)
        H=h[0]*XX+h[1]*YY+h[2]*ZZ
        E,U=np.linalg.eigh(H)
        weights=np.exp(-beta*E)
        rho=(U*weights)@U.conj().T/weights.sum()
        pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
        ptvals=np.sort(np.linalg.eigvalsh(pt).real)
        pmax=weights.max()/weights.sum()
        assert abs(ptvals[0]-(0.5-pmax))<1e-11,(k,h,beta,ptvals,pmax)
        if k<=2:
            assert pmax <= (1+np.tanh(beta))**2/4+1e-11
        else:
            assert pmax <= 1/(1+3*exp(-4*beta))+1e-11
        partial_checks+=1

# The nontrivial gap in thresholds is strict.
assert log(3)/4<asinh(1)/2
# Edge attainers: XX+ZZ and XX+YY+ZZ.
for k,bc in [(2,asinh(1)/2),(3,log(3)/4)]:
    h=[1.0]*k+[0.0]*(3-k)
    for sign in [-1,0,1]:
        beta=bc+sign*1e-6
        E=[sum(s[j]*h[j] for j in range(3)) for s in BELL_SIGNS]
        w=[exp(-beta*e) for e in E]
        pmax=max(w)/sum(w)
        assert (pmax>0.5)==(sign>0) if sign else abs(pmax-0.5)<1e-13,(k,beta,pmax)

# Cross-cut logarithmic negativity factorization for independent Bell dimers
# and classical Z-diagonal interactions; all cuts are sampled.
def full_pauli(word):
    r=np.array([[1]],dtype=complex)
    for j in word:
        r=np.kron(r,P[j])
    return r

def logneg(rho,n,cut):
    sh=[2]*(2*n)
    perm=list(range(2*n))
    for v in cut:
        perm[v],perm[n+v]=perm[n+v],perm[v]
    pt=rho.reshape(sh).transpose(perm).reshape(2**n,2**n)
    return np.log2(np.sum(np.abs(np.linalg.eigvalsh(pt))))

def bell_pmax(h,beta):
    energies=[sum(s[j]*h[j] for j in range(3)) for s in BELL_SIGNS]
    ws=[exp(-beta*e) for e in energies]
    return max(ws)/sum(ws)

cut_checks=0
for n in [4,5]:
    for _ in range(90):
        beta=rng.uniform(0.01,1.4)
        # Distinct Bell sectors (0,1) and when possible (2,3);
        # one-body classical field on remaining qubits.
        blocks=[(0,1)] + ([(2,3)] if n==5 else [])
        H=np.zeros((2**n,2**n),dtype=complex)
        contributions=[]
        used=set()
        for a,b in blocks:
            used|={a,b}
            hs=[rng.uniform(-1,1) for j in range(3)]
            for j,pa in enumerate([1,2,3]):
                w=[0]*n;w[a]=pa;w[b]=pa
                H+=hs[j]*full_pauli(w)
            contributions.append((a,b,bell_pmax(hs,beta)))
        for v in range(n):
            if v not in used:
                w=[0]*n;w[v]=3
                H+=rng.uniform(-1,1)*full_pauli(w)
        E,U=np.linalg.eigh(H)
        ws=np.exp(-beta*E)
        rho=(U*ws)@U.conj().T/ws.sum()
        for cutmask in range(1,(1<<n)-1):
            cut={i for i in range(n) if (cutmask>>i)&1}
            target=sum(np.log2(max(1,2*pmax)) for a,b,pmax in contributions if ((a in cut)!=(b in cut)))
            got=logneg(rho,n,cut)
            assert abs(got-target)<1e-10,(n,cut,target,got)
            cut_checks+=1
print('VERIFY_OK',count,'commuting-subset structure checks;',partial_checks,'matrix-PPT checks;',cut_checks,'bipartition log-negativity checks; sharp beta thresholds')

