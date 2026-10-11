#!/usr/bin/env python3
"""Exact finite checks for the three-cycle standard-Fourier concentration spectrum.

Only Python's standard library is required. This is a check for n=4,...,8,
not a substitute for the algebraic proof valid for all n>=4.
"""
from itertools import combinations
from math import comb


def cycles3(n):
    for a,b,c in combinations(range(n),3):
        p=list(range(n))
        p[a],p[b],p[c]=b,c,a
        yield tuple(p)
        p=list(range(n))
        p[a],p[c],p[b]=c,b,a
        yield tuple(p)


def gram(n):
    C=list(cycles3(n))
    assert len(C)==2*comb(n,3)
    return [[sum(x==y for x,y in zip(a,b))-1 for b in C] for a in C]


def spectrum(n):
    # Nontrivial Fourier-block conjugation sectors.
    return [(n*(n-2)*(n-4)**2//3,1),
            (n*(n-3),n-1),
            (n-4,n*(n-3)//2),
            (n,(n-1)*(n-2)//2)]


def mul(A,B):
    N=len(A)
    bt=list(zip(*B))
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in A]


def trace(A):
    return sum(row[i] for i,row in enumerate(A))


def check(n):
    K=gram(n)
    M=len(K)
    pred=spectrum(n)
    assert sum(d for _,d in pred)==(n-1)**2
    nonzero=sum(d for e,d in pred if e)
    assert nonzero<=M
    dims={e:sum(d for v,d in pred if v==e) for e,d in pred}
    dims[0]=M-nonzero
    pred_tr=[sum(d*e**j for e,d in dims.items()) for j in range(5)]
    assert pred_tr[0]==M
    A=K
    for j in range(1,5):
        assert trace(A)==pred_tr[j], (n,j,trace(A),pred_tr[j])
        if j<4:
            A=mul(A,K)
    # Check the minimal-polynomial annihilation directly by exact arithmetic.
    factors=sorted(set([0]+[e for e,d in pred if e]))
    # Horner multiplication: P <- P K - z P.
    P=[[int(i==j) for j in range(M)] for i in range(M)]
    for z in factors:
        Q=mul(P,K)
        P=[[Q[i][j]-z*P[i][j] for j in range(M)] for i in range(M)]
    assert all(v==0 for row in P for v in row), ('annihilator',n)
    return M,nonzero,len(factors),pred_tr[1],pred_tr[2]


def main():
    results=[]
    for n in range(4,9):
        results.append((n,*check(n)))
    print('VERIFY_OK exact_conjugacy_gram_n=4..8')
    for r in results:print('n=%d samples=%d rank=%d distinct_levels_including_zero=%d trace=%d trace2=%d'%r)

if __name__=='__main__':
    main()
