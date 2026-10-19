#!/usr/bin/env python3
"""Standalone checks for the two-junction discrete hopping theorem.

Requires Python 3, NumPy and SciPy. Reconstructs the finite truncation graph
without reading any external data. Matrix tests support but do not replace
infinite-volume analytic arguments.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def h_values(M, L, E):
    assert E > 2
    kappa = math.acosh(E/2)
    q = math.exp(-kappa)
    a = math.sinh((L-1)*kappa)/math.sinh(L*kappa)
    b = math.sinh(kappa)/math.sinh(L*kappa)
    return {s: E-M*(q+a+s*b) for s in (+1,-1)}


def graph_matrix(M,L,R):
    """Junctions 0,1, M internal rails and 2M exterior length-R rays."""
    edges=[]
    labels=[('u',0),('v',L)]
    for m in range(M):
        for j in range(1,L): labels.append(('i',m,j))
        for d in range(1,R+1): labels.append(('l',m,d))
        for d in range(1,R+1): labels.append(('r',m,d))
    ix={x:i for i,x in enumerate(labels)}
    for m in range(M):
        for j in range(L):
            x=('u',0) if j==0 else ('i',m,j)
            y=('v',L) if j+1==L else ('i',m,j+1)
            edges.append((ix[x],ix[y]))
        for d in range(1,R+1):
            x=('u',0) if d==1 else ('l',m,d-1)
            edges.append((ix[x],ix[('l',m,d)]))
            x=('v',L) if d==1 else ('r',m,d-1)
            edges.append((ix[x],ix[('r',m,d)]))
    rr=[];cc=[]
    for a,b in edges:
        rr.extend((a,b));cc.extend((b,a))
    mat=coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(len(labels),len(labels))).tocsr()
    return mat, ix


# Full positive out-of-band spectrum for finite truncations approaches formula.
for M,L in [(2,2),(2,3),(3,2),(3,3),(3,4),(4,5),(5,3)]:
    f_plus=lambda E:h_values(M,L,E)[1]
    plus=brentq(f_plus,2+1e-9,2*M+5,xtol=1e-13)
    check(plus>2,('plus',M,L))
    check(abs(f_plus(plus))<1e-10,('plus root',M,L))
    a_values=[h_values(M,L,E)[1] for E in (2+1e-7,2.1,2.5,3.0,4,6,12,20)]
    check(np.all(np.diff(a_values)>0),('plus monotone',M,L))
    has_minus=(M,L)!=(2,2)
    if has_minus:
        f_minus=lambda E:h_values(M,L,E)[-1]
        minus=brentq(f_minus,2+1e-9,2*M+5,xtol=1e-13)
        check(2<minus<plus,('ordered roots',M,L))
        check(abs(f_minus(minus))<1e-10,('minus root',M,L))
    else:
        minus=None
        check(abs(2-2*M*(1-1/L))<1e-12,('threshold edge',M,L))
    R=80
    mat,idx=graph_matrix(M,L,R)
    top=np.sort(eigsh(mat,k=4,which='LA',return_eigenvectors=False,tol=1e-12))
    check(abs(top[-1]-plus)<1e-6,('finite volume plus',M,L,top[-1],plus))
    if minus is not None:
        check(abs(top[-2]-minus)<2e-4,('finite volume minus',M,L,top[-2],minus))
    else:
        check(top[-2]<2+1e-7,('no second outside',M,L,top[-2]))
    bottom=np.sort(eigsh(mat,k=4,which='SA',return_eigenvectors=False,tol=1e-12))
    check(abs(bottom[0]+plus)<1e-6,('bipartite minus top',M,L))
    # Explicit compact eigenvectors on internal rails with zero hub/exteriors.
    for k in range(1,L):
        vec=np.zeros(mat.shape[0])
        Ek=2*math.cos(k*math.pi/L)
        for j in range(1,L):
            vec[idx[('i',0,j)]]=math.sin(k*math.pi*j/L)
            vec[idx[('i',1,j)]]=-math.sin(k*math.pi*j/L)
        check(np.linalg.norm(mat@vec-Ek*vec)<1e-10,('BIC residual',M,L,k))

# Junction Schur complement is an increasing matrix pencil: independent
# discrete sample stress test across parameters, not substituted for proof.
for M in range(2,9):
    for L in range(2,10):
        for s in (-1,+1):
            ens=(2+1e-6,2.01,2.1,2.5,3.5,6.,10.,18.)
            vals=[h_values(M,L,E)[s] for E in ens]
            check(all(b>a for a,b in zip(vals,vals[1:])),('monotonic grid',M,L,s))

print(f'PASS: {checks} checks; exact compact modes and independently reconstructed finite graph spectra.')
