#!/usr/bin/env python3
"""Independent adjacency construction and graph-state spectral checks."""
from itertools import product
from math import isclose
import numpy as np


def gf2_rank_rows(rows):
    piv={}
    for row in rows:
        while row:
            bit=row.bit_length()-1
            if bit not in piv:
                piv[bit]=row
                break
            row ^= piv[bit]
    return len(piv)


def vertices(d):
    return list(product(range(3),repeat=d))


def matrix_rows(d):
    vs=vertices(d)
    a=[v for v in vs if sum(v)%3==0]
    b=[v for v in vs if sum(v)%3!=0]
    b_index={v:i for i,v in enumerate(b)}
    rows=[]
    for v in a:
        mask=0
        for j in range(d):
            for delta in (1,2):
                z=list(v)
                z[j]=(z[j]+delta)%3
                mask ^= 1<<b_index[tuple(z)]
        rows.append(mask)
    return a,b,rows


def test_ranks():
    total=0
    for d in range(1,9):
        a,b,rows=matrix_rows(d)
        actual=gf2_rank_rows(rows)
        expected=(3**d+(-1)**(d-1))//4
        assert actual==expected,(d,actual,expected)
        total+=len(rows)
        print(f'd={d}: |A|={len(a)}, |B|={len(b)}, binary_rank={actual}, deficit={len(a)-actual}')
    print(f'RANK_VERIFIED: 8 dimensions, {total} independently built cut rows')


def direct_partial_trace(d):
    vs=vertices(d)
    n=len(vs)
    a,b,rows=matrix_rows(d)
    assert n<=9
    ids={v:i for i,v in enumerate(vs)}
    edges=[]
    for i,v in enumerate(vs):
        for j,w in enumerate(vs[:i]):
            if sum(u!=t for u,t in zip(v,w))==1:edges.append((j,i))
    N=1<<n
    psi=np.ones(N,dtype=np.float64)/np.sqrt(N)
    for s in range(N):
        parity=0
        for i,j in edges:
            if (s>>i)&1 and (s>>j)&1:parity^=1
        if parity: psi[s]=-psi[s]
    a_ids=[ids[v] for v in a]
    b_ids=[ids[v] for v in b]
    W=np.zeros((1<<len(a),1<<len(b)),dtype=float)
    for ai in range(1<<len(a)):
        for bi in range(1<<len(b)):
            s=sum(((ai>>i)&1)<<ind for i,ind in enumerate(a_ids))
            s+=sum(((bi>>j)&1)<<ind for j,ind in enumerate(b_ids))
            W[ai,bi]=psi[s]
    rho=W@W.T
    vals=np.linalg.eigvalsh(rho)
    expected=(3**d+(-1)**(d-1))//4
    positives=vals[vals>1e-10]
    assert len(positives)==1<<expected
    assert np.max(np.abs(positives-2.0**(-expected)))<1e-12
    assert np.min(vals)>-1e-12
    print(f'd={d}: reduced spectrum has {len(positives)} positive eigenvalues all {2.0**(-expected):.12f}')


if __name__=='__main__':
    test_ranks()
    for d in (1,2): direct_partial_trace(d)
    print('ALL_CHECKS_PASSED')

# The additional exhaustive affine-hyperplane checks are intentionally
# independent of the Fourier proof.
def affine_cut_rows(d,normal,c):
    vs=vertices(d)
    groups=[[v for v in vs if sum((normal[i]*v[i]) for i in range(d))%3==k] for k in range(3)]
    a=groups[c]
    b=[v for k in range(3) if k!=c for v in groups[k]]
    idx={v:j for j,v in enumerate(b)}
    rows=[]
    for v in a:
        bits=0
        for i in range(d):
            for dx in (1,2):
                t=list(v);t[i]=(t[i]+dx)%3;t=tuple(t)
                if t in idx:bits^=1<<idx[t]
        rows.append(bits)
    return rows

def test_all_affine():
    tests=0
    for d in range(1,6):
        for normal in product(range(3),repeat=d):
            s=sum(x!=0 for x in normal)
            if not s:continue
            predicted=3**(d-s)*(3**s+(-1)**(s-1))//4
            for c in range(3):
                actual=gf2_rank_rows(affine_cut_rows(d,normal,c))
                assert predicted==actual,(d,normal,c,predicted,actual)
                tests+=1
    for d in (6,7):
        for s in range(1,d+1):
            for phase in (0,1,2):
                normal=tuple((1 if j%2==0 else 2) if j<s else 0 for j in range(d))
                predicted=3**(d-s)*(3**s+(-1)**(s-1))//4
                actual=gf2_rank_rows(affine_cut_rows(d,normal,phase))
                assert actual==predicted
                tests+=1
    print(f'AFFINE_VERIFIED: {tests} normal-and-offset cut matrices, including all for d<=5')

if __name__=='__main__':
    test_all_affine()
    print('AFFINE_CHECKS_PASSED')
