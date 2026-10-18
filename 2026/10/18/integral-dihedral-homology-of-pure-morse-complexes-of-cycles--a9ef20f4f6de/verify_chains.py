#!/usr/bin/env python3
"""Chain-level test for pure cycle Morse complexes, independent formulation.

Faces are generated as size-(n-1) matchings on the 2n-cycle obtained by
removing two opposite-parity vertices and matching the remaining paths.
Uses sparse Gaussian elimination over two distinct fields for homology ranks.
"""
from itertools import combinations


def facets(n):
    # For any two missing vertices of opposite bipartite parity,
    # each complementary path of the incidence cycle is perfectly matched.
    result=set()
    N=2*n
    for u in range(N):
        for v in range(u+1,N):
            if (v-u)%2!=1:
                continue
            curr=[]
            for a,b in ((u,v),(v,u+N)):
                for x in range(a+1,b-1,2):
                    curr.append(x%N)
            assert len(curr)==n-1
            result.add(tuple(sorted(curr)))
    assert len(result)==n*n,(n,len(result))
    return sorted(result)


def rank_mod_p(columns,p):
    pivots={}
    for col in columns:
        col={i:v%p for i,v in col.items() if v%p}
        while col:
            k=max(col)
            v=col[k]
            if k not in pivots:
                iv=pow(v,-1,p)
                pivots[k]={t:(x*iv)%p for t,x in col.items()}
                break
            base=pivots[k]
            col={t:(col.get(t,0)-v*base.get(t,0))%p
                 for t in set(col)|set(base)}
            col={t:x for t,x in col.items() if x}
    return len(pivots)


def chain_complex(n,p):
    fs=facets(n)
    graded=[sorted(set(face for F in fs for face in combinations(F,k)))
            for k in range(n)]
    counts=[len(a) for a in graded]
    ranks=[]
    for k in range(1,n):
        rows={face:i for i,face in enumerate(graded[k-1])}
        cols=[{rows[tuple(f[:i]+f[i+1:])]:1 if i%2==0 else p-1
                for i in range(k)} for f in graded[k]]
        ranks.append(rank_mod_p(cols,p))
    # augmented boundary C_0 -> C_{-1} has rank 1.
    betti=[counts[k]-(ranks[k-1] if k>0 else 0)-
           (ranks[k] if k<len(ranks) else 0) for k in range(n)]
    return counts,ranks,betti


def check_top_cycle(n):
    fs=set(facets(n))
    for parity in (0,1):
        simplex=tuple(range(parity,2*n,2))
        boundary=[tuple(simplex[:j]+simplex[j+1:]) for j in range(n)]
        assert all(f in fs for f in boundary)
        # Consecutive deletions cancel along codimension-one faces.
        total={}
        for i,F in enumerate(boundary):
            for j in range(n-1):
                sub=tuple(F[:j]+F[j+1:])
                total[sub]=total.get(sub,0)+(-1)**(i+j)
        assert all(v==0 for v in total.values())


def run():
    for n in range(5,10):
        for p in (2,101):
            counts,ranks,betti=chain_complex(n,p)
            assert betti==[0,0,0,1]+[0]*(n-5)+[2],(n,p,counts,ranks,betti)
        check_top_cycle(n)
        print(f'n={n} mod-2 and mod-101 Betti={betti} top boundaries closed')
    print('PASS: independent top-chain and homology computations')

if __name__=='__main__':
    run()
