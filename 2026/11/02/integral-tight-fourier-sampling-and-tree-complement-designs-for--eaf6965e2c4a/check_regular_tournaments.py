"""Exact finite checks for regular-tournament first-band frame formulas.
Independent of the general proof, which applies to all odd n >= 3.
"""
from itertools import combinations
from fractions import Fraction
from sympy import Matrix, Rational

def enumerate_tournaments(n):
    edges=list(combinations(range(n),2)); m=len(edges)
    out=[]
    for mask in range(1<<m):
        balance=[0]*n
        vec=[]
        for j,(u,v) in enumerate(edges):
            a=1 if mask>>j&1 else -1
            vec.append(a); balance[u]+=a; balance[v]-=a
        if all(b==0 for b in balance):out.append(tuple(vec))
    return edges,out

def run(n):
    edges,words=enumerate_tournaments(n)
    m=len(edges); d=(n-1)*(n-2)//2; N=len(words)
    assert N>0
    B=Matrix([[int(u==i)-int(v==i) for u,v in edges] for i in range(n)])
    X=Matrix(words)
    assert X*B.T==Matrix.zeros(N,n)
    assert (Matrix.ones(1,N)*X)==Matrix.zeros(1,m)
    assert (X.T*X)/N == Rational(n,n-2)*(Matrix.eye(m)-B.T*B/n)
    assert X.rank()==d
    for a,b,c in combinations(range(n),3):
        triangle={tuple(sorted((a,b))),tuple(sorted((a,c))),tuple(sorted((b,c)))}
        assert any((w[edges.index((a,b))],w[edges.index((a,c))],w[edges.index((b,c))])==(1,-1,1) for w in words)
    # Triangular circulations generate the rank-d integral lattice.
    if n==5:
        # all spanning trees by Prüfer enumerating subsets and rank of B_T
        trees=[]; non_trees=[]
        for T in combinations(range(m),n-1):
            if B[:,T].rank()==n-1: trees.append(set(T))
            else: non_trees.append(set(T))
        assert len(trees)==n**(n-2)
        for seed in [None,tuple(range(1,N+1))]:
            if seed is None: C=(X.T*X)/N
            else:
                den=sum(seed)
                mu=Matrix([[sum(seed[i]*words[i][e] for i in range(N)) / Rational(den) for e in range(m)]])
                C=(X.T*Matrix.diag(*seed)*X)/den-mu.T*mu
            vals=[]
            for T in trees:
                S=sorted(set(range(m))-T)
                vals.append(C.extract(S,S).det())
            assert len(set(vals))==1 and vals[0]>0
            for T in non_trees:
                S=sorted(set(range(m))-T)
                assert C.extract(S,S).det()==0
            if seed is None:
                assert vals[0]==Rational(n,n-2)**d/Rational(n**(n-2))
    print('n=%d, total regular tournaments=%d, edges=%d, rank=%d, exact covariance PASS'%(n,N,m,d))

if __name__=='__main__':
    run(3)
    run(5)
    print('all exact finite checks PASS')
