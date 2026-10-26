#!/usr/bin/env python3
"""Exact finite spot checks for the twin-blow-up evolution-algebra theorem.

The theorem for unbounded graphs is proved algebraically in RESULT.md; finite
spot checks only catch normalization and indexing errors in the displayed
rank and dilation identities. Requires Python 3.9+; no third-party packages.
"""
from fractions import Fraction
from itertools import product
from math import isclose


def rank(rows):
    M = [[Fraction(x) for x in row] for row in rows]
    if not M: return 0
    n, m, r = len(M), len(M[0]), 0
    for col in range(m):
        piv = next((i for i in range(r, n) if M[i][col]), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        z=M[r][col]; M[r]=[v/z for v in M[r]]
        for i in range(n):
            if i!=r and M[i][col]:
                z=M[i][col]
                M[i]=[a-z*b for a,b in zip(M[i],M[r])]
        r+=1
        if r==n: break
    return r


def connected(H):
    todo=[0]; seen={0}
    for i in todo:
        for j,v in enumerate(H[i]):
            if v and j not in seen:
                seen.add(j); todo.append(j)
    return len(seen)==len(H)


def bipartition(H):
    c={0:0}; queue=[0]
    for i in queue:
        for j,v in enumerate(H[i]):
            if not v: continue
            if j in c:
                if c[j]==c[i]: return None
            else:
                c[j]=1-c[i];queue.append(j)
    return c


def example(H, a, elaborate=False):
    k=len(a); n=sum(a)
    assert all(x>=1 for x in a)
    assert len(H)==k and all(len(row)==k for row in H)
    assert all(H[i][i]==0 and H[i][j]==H[j][i] and H[i][j] in (0,1)
               for i in range(k) for j in range(k))
    assert connected(H) and rank(H)==k
    block=list(i for i,v in enumerate(a) for _ in range(v))
    d=[sum(H[i][j]*a[j] for j in range(k)) for i in range(k)]
    U=[[H[i][block[t]] for t in range(n)] for i in range(k)]
    assert rank(U)==k
    # Squaring of a standard basis vector in its part gives U_i; for random
    # integer x, L_x has columns x_t U_{block(t)} (or /d_i in the RW case).
    sample=0
    for u in product((-1,0,1), repeat=min(n,7)):
        x=list(u)+[0]*max(0,n-7)
        nonzero=sum(any(x[t] for t in range(n) if block[t]==i) for i in range(k))
        M=[[x[t]*U[block[t]][s] for t in range(n)] for s in range(n)]
        assert rank(M)==nonzero
        sample+=1
        if sample>=30: break
    b=bipartition(H)
    predicted=(len(set(d))==1 or (b is not None and all(len({d[i] for i in range(k) if b[i]==t})==1 for t in (0,1))))
    if predicted:
        if len(set(d))==1:
            sc=[float(d[0])]*k
        else:
            dl=next(d[i] for i in range(k) if b[i]==0)
            dr=next(d[i] for i in range(k) if b[i]==1)
            sc=[(dl**2*dr)**(1/3) if b[i]==0 else (dl*dr**2)**(1/3) for i in range(k)]
        for i in range(k):
            for j in range(k):
                if H[i][j]:
                    assert isclose(sc[i]**2/d[i],sc[j],rel_tol=1e-12)
    if elaborate: print('graph',H,'sizes',a,'degrees',d,'rank',rank(U),'bipartite',b is not None,'predicted_iso',predicted)
    return sample


def main():
    K3=[[0,1,1],[1,0,1],[1,1,0]]
    P4=[[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]]
    K2=[[0,1],[1,0]]
    graphs=[K2,K3,P4]
    cases=0; spot_checks=0
    for H in graphs:
        for a in product(range(1,4), repeat=len(H)):
            spot_checks+=example(H,a)
            cases+=1
    for H,a in [(K3,(1,2,3)),(K3,(2,2,2)),(P4,(2,1,2,1)),(K2,(2,3))]:
        example(H,a,True)
    assert cases==9+27+81
    print('VERIFY_OK','cases=',cases,'rank_tests=',spot_checks)

if __name__=='__main__': main()
