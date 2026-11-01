#!/usr/bin/env python3
"""Small exact integer-boundary checks for two-overlapping-clique complexes."""
from itertools import combinations
from collections import defaultdict
from math import comb
from sympy import ZZ, zeros
from sympy.matrices.normalforms import smith_normal_form


def make_faces(a,b,s,t):
    A=set(range(a)); B=set(range(a,a+b)); C=set(range(a+b,a+b+s))
    groups=[A|C,B|C]
    forbid={sum(1<<i for i in c) for block in groups for c in combinations(sorted(block),t)}
    F=defaultdict(list)
    for mask in range(1,1<<(a+b+s)):
        if all((mask&bad)!=bad for bad in forbid): F[mask.bit_count()-1].append(mask)
    return F


def snf_rank_and_torsion(M):
    D=smith_normal_form(M,domain=ZZ)
    entries=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]!=0]
    return len(entries), [v for v in entries if v!=1]


def check(a,b,s,t):
    F=make_faces(a,b,s,t); ranks={}; torsion={}
    for dim in range(1,max(F)+1):
        low={mask:i for i,mask in enumerate(F[dim-1])}
        M=zeros(len(F[dim-1]),len(F[dim]))
        for col,mask in enumerate(F[dim]):
            vs=[i for i in range(a+b+s) if mask>>i&1]
            for ix,v in enumerate(vs):M[low[mask^(1<<v)],col]=(-1)**ix
        ranks[dim],torsion[dim-1]=snf_rank_and_torsion(M)
    measured={dim:len(fs)-ranks.get(dim,0)-ranks.get(dim+1,0)-(dim==0)
              for dim,fs in F.items()}
    measured={k:v for k,v in measured.items() if v}
    k=t-1
    predicted={2*k-j-1:comb(s,j)*comb(a-1,k-j)*comb(b-1,k-j)
               for j in range(min(k,s)+1) if 0<=k-j<=min(a-1,b-1)}
    predicted={k:v for k,v in predicted.items() if v}
    assert measured==predicted,(measured,predicted)
    assert not any(torsion.values()),torsion
    print(f'INTEGRAL SNF a={a} b={b} s={s} t={t}: Betti={measured}, all nonzero invariant factors=1')

if __name__=='__main__':
    for p in [(2,2,2,3),(3,3,2,3),(3,4,2,3),(3,3,3,3)]: check(*p)
    print('INTEGRAL TESTS PASS')
