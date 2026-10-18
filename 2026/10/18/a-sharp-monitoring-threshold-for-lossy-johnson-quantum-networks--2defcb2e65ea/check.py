#!/usr/bin/env python3
"""Reproducibility checks for coordinate-monitored Johnson quantum walks.

Only small finite systems are sampled; mathematical generality comes from proof.
"""
from itertools import combinations
from math import comb
import numpy as np
from scipy.linalg import null_space, eigvals

rng=np.random.default_rng(41977)
checks=0
worst=0.0
for n in range(3,9):
 for k in range(1,n):
  for r in range(1,n-k+1):
   vertices=[frozenset(a) for a in combinations(range(n),k)]
   C=[v for v in vertices if not any(a<r for a in v)]
   F=[v for v in vertices if any(a<r for a in v)]
   m=n-r
   row=[frozenset(a) for a in combinations(range(r,n),k-1)]
   D=np.asarray([[float(u.issubset(v)) for v in C] for u in row])
   rank=np.linalg.matrix_rank(D,tol=1e-9)
   expected_rank=min(comb(m,k),comb(m,k-1))
   assert rank==expected_rank, ('rank',n,k,r,rank,expected_rank)
   checks+=1
   Q=null_space(D,rcond=1e-10)
   assert Q.shape[1]==max(comb(m,k)-comb(m,k-1),0)
   # Dark eigenmodes have eigenvalue -k in the unmonitored Johnson sector.
   A_C=np.array([[float(len(x^y)==2) for y in C] for x in C])
   e=np.max(np.abs(A_C@Q+k*Q)) if Q.size else 0.0
   worst=max(worst,e)
   assert e<1e-10,(n,k,r,e)
   checks+=1
   # All unmonitored starting vertices are equivalent under permutations.
   bright=np.eye(len(C))-Q@Q.conj().T
   pred=min(1., k/(n-r-k+1))
   e=float(np.max(np.abs(np.diag(bright)-pred)))
   worst=max(worst,e)
   assert e<1e-10,(n,k,r,pred,e)
   checks+=1
   # Every other mode of H_eff has strictly negative imaginary energy.
   A=np.array([[float(len(x^y)==2) for y in vertices] for x in vertices])
   loss=np.array([rng.uniform(.6,2.4) if v in F else 0 for v in vertices])
   H=A-.5j*np.diag(loss)
   lam=eigvals(H)
   real_count=np.count_nonzero(np.abs(lam.imag)<1e-7)
   assert real_count==Q.shape[1], ('spectrum',n,k,r,real_count,Q.shape[1],lam.imag.max())
   checks+=1
   # The dark-projector row on an absorbing vertex vanishes exactly.
   P=np.zeros_like(A)
   idx=[vertices.index(v) for v in C]
   P[np.ix_(idx,idx)]=Q@Q.T
   assert np.max(np.abs(P[[i for i,v in enumerate(vertices) if v in F],:]))<1e-10
   checks+=1
print('PASS',checks,'finite checks; maximum projector/invariance error',f'{worst:.3e}')
# Direct physical survival at late times for representative monitored faces.
from scipy.linalg import expm
for n,k,r in [(4,1,1),(5,2,1),(6,2,1),(6,2,2),(6,2,3),(7,3,1),(7,3,2),(7,3,3)]:
    vertices=[frozenset(v) for v in combinations(range(n),k)]
    C=[i for i,v in enumerate(vertices) if v.isdisjoint(range(r))]
    F=[i for i,v in enumerate(vertices) if not v.isdisjoint(range(r))]
    A=np.array([[float(len(x^y)==2) for y in vertices] for x in vertices])
    rates=np.zeros(len(vertices))
    rates[F]=rng.uniform(.8,2.1,size=len(F))
    H=A-.5j*np.diag(rates)
    damp=-np.linalg.eigvals(H).imag
    positive=damp[damp>1e-8]
    t=25/min(positive)
    U=expm(-1j*H*t)
    for idx,want in [(C[0],min(1.,k/(n-r-k+1))),(F[0],1.)]:
        probability=1.-sum(abs(U[:,idx])**2)
        e=abs(probability-want)
        worst=max(worst,e)
        assert e<1e-7,(n,k,r,idx,want,probability,e)
        checks+=1
    u=np.zeros(len(vertices),dtype=complex)
    u[C]=1/np.sqrt(len(C))
    probability=1.-sum(abs(U@u)**2)
    e=abs(probability-1)
    worst=max(worst,e)
    assert e<1e-7,(n,k,r,'uniform',probability,e)
    checks+=1
print('PASS',checks,'total independent finite checks; worst error',f'{worst:.3e}')
# Detector-side Hermitian dynamics can be arbitrary without changing dark modes.
for n,k,r in [(5,1,1),(5,2,1),(6,2,2),(7,3,2)]:
    vertices=[frozenset(v) for v in combinations(range(n),k)]
    C=[i for i,v in enumerate(vertices) if v.isdisjoint(range(r))]
    F=[i for i,v in enumerate(vertices) if not v.isdisjoint(range(r))]
    A=np.array([[float(len(x^y)==2) for y in vertices] for x in vertices])
    X=rng.normal(size=(len(F),len(F)))
    V=(X+X.T)*.05
    H=A.astype(complex)
    H[np.ix_(F,F)] += V
    H -= .5j*np.diag(np.array([rng.uniform(.6,1.8) if i in F else 0 for i in range(len(vertices))]))
    vals=np.linalg.eigvals(H)
    dark=np.count_nonzero(np.abs(vals.imag)<1e-8)
    m=n-r
    expected=max(comb(m,k)-comb(m,k-1),0)
    assert dark==expected,(n,k,r,dark,expected)
    checks+=1
print('PASS',checks,'finite checks including arbitrary detector-side Hermitian perturbations; worst numerical error',f'{worst:.3e}')
