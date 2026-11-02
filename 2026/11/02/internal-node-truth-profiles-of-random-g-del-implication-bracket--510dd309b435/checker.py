"""Finite checks for Gödel-implication internal-pair generating functions."""
from functools import lru_cache
from itertools import product
from math import comb, sqrt

@lru_cache(None)
def trees(n):
    if n == 1:
        return (None,)
    return tuple((left, right) for i in range(1,n) for left in trees(i) for right in trees(n-i))

def evaluate(tree, it, m, counts):
    if tree is None:
        return next(it)
    a=evaluate(tree[0],it,m,counts)
    b=evaluate(tree[1],it,m,counts)
    counts[a][b]+=1
    return m-1 if a <= b else b

def recurrence(m,N):
    G=[[0]*(N+1) for _ in range(m)]
    E=[[[0]*(N+1) for _ in range(m)] for _ in range(m)]
    for v in range(m): G[v][1]=1
    for n in range(2,N+1):
        for size in range(1,n):
            for a in range(m):
                for b in range(m):
                    c=G[a][size]*G[b][n-size]
                    E[a][b][n]+=c
                    G[m-1 if a<=b else b][n]+=c
        # all pairs already aggregated at root; E arrays below are all-node counts
    A=[[[0]*(N+1) for _ in range(m)] for _ in range(m)]
    for n in range(2,N+1):
        for a in range(m):
            for b in range(m):
                A[a][b][n]=E[a][b][n]
                for size in range(1,n):
                    A[a][b][n]+=sum(G[c][size] for c in range(m))*A[a][b][n-size]
                    A[a][b][n]+=A[a][b][size]*sum(G[c][n-size] for c in range(m))
    return G,A

def verify():
    checks=0
    for m in range(2,5):
        N=6 if m<=3 else 5
        G,A=recurrence(m,N)
        for n in range(1,N+1):
            observedG=[0]*m
            observedA=[[0]*m for _ in range(m)]
            for t in trees(n):
                for vals in product(range(m),repeat=n):
                    counts=[[0]*m for _ in range(m)]
                    ans=evaluate(t,iter(vals),m,counts)
                    observedG[ans]+=1
                    for a in range(m):
                        for b in range(m):
                            observedA[a][b]+=counts[a][b]
            assert observedG==[G[a][n] for a in range(m)], (m,n,'root')
            assert observedA==[[A[a][b][n] for b in range(m)] for a in range(m)], (m,n,'internal')
            assert sum(sum(row) for row in observedA)==(n-1)*m**n*len(trees(n)),(m,n,'total')
            checks+=m*m
            print('PASS m=',m,'n=',n,'pairs=',sum(sum(row) for row in observedA))
    q0=(sqrt(3)-1)/2
    p0=q0*(1-q0)
    assert abs(p0-(sqrt(3)-1.5))<1e-12
    print('BINARY_CRITICAL_FALSE',p0)
    print('ALL_CHECKS_OK',checks)
if __name__=='__main__': verify()
