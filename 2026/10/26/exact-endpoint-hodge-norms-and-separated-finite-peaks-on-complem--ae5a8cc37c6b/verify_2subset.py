#!/usr/bin/env python3
"""Exact-rational independent incidence-matrix checks of two-subset graph cut/cycle norms.

Only Python's standard library is required. The proof for all n is analytic and
is not inferred from these finite tests.
"""
from fractions import Fraction as F
from itertools import combinations


def inverse(M):
    n=len(M)
    A=[[F(M[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next(k for k in range(j,n) if A[k][j])
        A[j],A[p]=A[p],A[j]
        c=A[j][j]
        A[j]=[v/c for v in A[j]]
        for i in range(n):
            if i!=j and A[i][j]:
                c=A[i][j]
                A[i]=[x-c*y for x,y in zip(A[i],A[j])]
    return [a[n:] for a in A]


def graph(n,kind):
    vs=list(combinations(range(n),2))
    es=[]
    for a,b in combinations(range(len(vs)),2):
        overlap=len(set(vs[a])&set(vs[b]))
        if overlap==(1 if kind=='triangular' else 0): es.append((a,b))
    return vs,es


def formula(n,kind):
    if kind=='triangular':
        return (F((n-2)*(3*n-1),n*(n-1)), F(2*(2*n-5),n-1))
    return (F(2*(n-3)*(n+6),n*(n-1)),
            F(3*n**3-4*n**2-59*n+100,n*(n-3)*(n-1)))


def check(n,kind):
    vs,es=graph(n,kind)
    N=len(vs)
    L=[[0]*(N-1) for _ in range(N-1)]
    for a,b in es:
        for u,v in ((a,a),(b,b)):
            if u<N-1:L[u][v]+=1
        if a<N-1 and b<N-1:
            L[a][b]-=1;L[b][a]-=1
    R=inverse(L)
    qexpected,cexpected=formula(n,kind)
    assert qexpected>0 and cexpected>=0
    values=[]
    for a,b in es:
        rhs=[F(int(i==a)-int(i==b)) for i in range(N-1)]
        v=[sum((R[i][j]*rhs[j] for j in range(N-1)),F(0)) for i in range(N-1)]+[F(0)]
        qcol=[v[i]-v[j] for i,j in es]
        diagonal=v[a]-v[b]
        assert F(0)<=diagonal<=F(1)
        qsum=sum(map(abs,qcol),F(0))
        csum=qsum+1-2*diagonal
        assert qsum==qexpected,(n,kind,'cut',qsum,qexpected)
        assert csum==cexpected,(n,kind,'cycle',csum,cexpected)
        values.append((qsum,csum))
    assert len(values)==len(es)
    print(f'PASS {kind} n={n} vertices={N} edges={len(es)} cut={qexpected} cycle={cexpected}')
    return len(es)


def check_orbit_counts():
    # Directly enumerate absolute potential differences, independently of graph Laplacians.
    for kind in ('triangular','kneser'):
        for n in range(5,21):
            vs,es=graph(n,kind)
            if kind=='triangular':
                plus=(0,1); minus=(0,2); other=range(3,n)
                U=F(n+1,2*n*(n-1)); V=F(1,2*n*(n-1))
                h={plus:U,minus:-U}
                for k in other:h[(1,k)]=V;h[(2,k)]=-V
                expected=[(2*U,1), (U,2*(n-2)), (U-V,2*(n-3)), (V,2*(n-3)*(n-2)), (2*V,n-3)]
            else:
                plus=(0,1);minus=(2,3);other=range(4,n)
                U=F(2*(n+1),n*(n-3)*(n-1));V=F(4,n*(n-4)*(n-3)*(n-1))
                h={plus:U,minus:-U}
                for k in other:
                    for j in (0,1):h[(j,k)]=-V
                    for j in (2,3):h[(j,k)]=V
                expected=[(2*U,1), (U-V,4*(n-4)), (U,(n-4)*(n-5)),
                          (V,2*(n-4)*((n-5)*(n-6)+4)),(2*V,4*(n-4)*(n-5))]
            from collections import Counter
            actual=Counter(abs(h.get(vs[a],F(0))-h.get(vs[b],F(0))) for a,b in es)
            merged=Counter()
            for val,k in expected:merged[val]+=k
            for val,k in merged.items(): assert actual[val]==k,(kind,n,val,actual[val],k)
            assert sum(merged.values())==sum(k for val,k in actual.items() if val)
    print('PASS 32 exact orbit-multiplicity comparisons across parameters 5..20')


if __name__=='__main__':
    ncolumns=0
    for n in range(3,9):ncolumns+=check(n,'triangular')
    for n in range(5,9):ncolumns+=check(n,'kneser')
    check_orbit_counts()
    print('ALL PASS:',ncolumns,'independent edge-column comparisons, 10 graphs; 32 orbit-count comparisons')
