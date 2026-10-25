#!/usr/bin/env python3
"""Exact finite regression checks for signed complete-bipartite path homology.

Run with Python 3 and SymPy. Finite tests are not a proof of the theorem.
"""
import itertools
import sympy as sp


def signs(m, n, mask):
    return [[-1 if i and j and ((mask >> ((i-1)*(n-1)+j-1)) & 1)
             else 1 for j in range(n)] for i in range(m)]


def twisted_rank_check(m, n, mat):
    edges = [(i, j) for i in range(m) for j in range(n)]
    idx = {e: k for k, e in enumerate(edges)}
    incidence = sp.zeros(m+n, m*n)
    for (i,j), k in idx.items():
        incidence[i, k] = -1
        incidence[m+j, k] = mat[i][j]
    squares = []
    for i,k in itertools.combinations(range(m), 2):
        for j,l in itertools.combinations(range(n), 2):
            if mat[i][j]*mat[k][j]*mat[k][l]*mat[i][l] != 1:
                continue
            vec = sp.zeros(m*n, 1)
            vec[idx[i,j]] = 1
            vec[idx[k,j]] = -mat[i][j]*mat[k][j]
            vec[idx[k,l]] = mat[i][j]*mat[k][j]
            vec[idx[i,l]] = -1
            assert incidence*vec == sp.zeros(m+n, 1)
            squares.append(vec)
    q = sp.Matrix.hstack(*squares) if squares else sp.zeros(m*n, 0)
    nullity = m*n - incidence.rank()
    assert q.rank() == nullity, (m,n,mat,nullity,q.rank())
    # In normalized gauge a signing is balanced exactly if all entries are +1.
    expected = (m-1)*(n-1) - (0 if all(x==1 for row in mat for x in row) else 1)
    assert nullity == expected, (m,n,mat,nullity,expected)


def direct_path_rank_check(m, n, mat):
    """Independent degree-0/1/2 anti-invariant chain calculation.

    Uses both orientations of each arc and the elementary regular two-path
    generators: backtracks and differences between paths with equal signed endpoints.
    """
    edge_sign = {(i, m+j):mat[i][j] for i in range(m) for j in range(n)}
    def sg(u,v):
        return edge_sign.get((u,v), edge_sign.get((v,u)))
    arcs = []
    for u,v in edge_sign:
        arcs.extend(((u,v),(v,u)))
    where = {a:k for k,a in enumerate(arcs)}
    d1 = sp.zeros(m+n, len(arcs))
    for a,(u,v) in enumerate(arcs):
        d1[u,a]=-1
        d1[v,a]=sg(u,v)
    relations=[]
    for u,v in edge_sign:
        a=sp.zeros(len(arcs),1)
        a[where[u,v]]=1
        a[where[v,u]]=sg(u,v)
        relations.append(a)
    for u in range(m+n):
        for w in range(m+n):
            if u==w:
                continue
            classes={}
            for v in range(m+n):
                if sg(u,v) is not None and sg(v,w) is not None:
                    classes.setdefault(sg(u,v)*sg(v,w),[]).append(v)
            for mids in classes.values():
                if len(mids)<2:
                    continue
                v=mids[0]
                for z in mids[1:]:
                    a=sp.zeros(len(arcs),1)
                    a[where[u,v]]+=1
                    a[where[v,w]]+=sg(u,v)
                    a[where[u,z]]-=1
                    a[where[z,w]]-=sg(u,z)
                    relations.append(a)
    d2=sp.Matrix.hstack(*relations)
    assert d1*d2 == sp.zeros(m+n,d2.cols)
    assert len(arcs)-d1.rank()-d2.rank()==0, (m,n,mat)


def main():
    count1=0
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        for mask in range(1 << ((m-1)*(n-1))):
            twisted_rank_check(m,n,signs(m,n,mask))
            count1+=1
    count2=0
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4)]:
        for mask in range(1 << ((m-1)*(n-1))):
            direct_path_rank_check(m,n,signs(m,n,mask))
            count2+=1
    print(f'PASS: {count1} normalized signing/rank checks; '
          f'{count2} independent anti-invariant degree-two checks.')

if __name__=='__main__':
    main()
