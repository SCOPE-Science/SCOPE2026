"""Exact rational finite verification for Hilbert embeddings of even-rim wheels.

Scientific input: for m>=7 the wheel K_1 join C_(2m) has squared
embedding distances described by its proposed 2m-by-2m Gram matrix.
The infinite-dimensional PSD argument is analytical (Fourier modes), not
certified by this finite program.
"""
from fractions import Fraction as F
from collections import deque


def rim_gram(m):
    T = F(2) - F(2,m)
    G = [[F(0) for _ in range(2*m)] for _ in range(2*m)]
    for i in range(m):
        for j in range(m):
            G[2*i][2*j] = T if i==j else -F(2,m)
            G[2*i+1][2*j+1] = T if i==j else -F(2,m)
            off = (j-i)%m
            if off in (0,m-1):
                c=F(1)-F(1,m)
            elif off in (1,m-2):
                c=-F(3,m)
            else:
                c=-F(2,m)
            G[2*i][2*j+1]=G[2*j+1][2*i]=c
    return G


def check_psd_exact(A):
    # Schur complement using nonnegative pivots; a zero diagonal in any PSD
    # matrix forces the corresponding entire row/column to vanish.
    a=[r[:] for r in A]
    n=len(a)
    for k in range(n):
        p=a[k][k]
        assert p>=0, ('negative rational pivot', k, p)
        if not p:
            assert all(a[k][j]==0 for j in range(k+1,n)), ('zero pivot nonzero row',k)
            continue
        for i in range(k+1,n):
            for j in range(i,n):
                a[i][j]-=a[i][k]*a[k][j]/p
                a[j][i]=a[i][j]
        for i in range(k+1,n):
            a[i][k]=a[k][i]=F(0)
    return True


def graph_distances(m):
    n=2*m+1
    adj=[set() for _ in range(n)]
    for i in range(2*m):
        u=i+1
        for v in (0, ((i+1)%(2*m))+1):
            adj[u].add(v);adj[v].add(u)
    ds=[]
    for start in range(n):
        d=[-1]*n; d[start]=0; q=deque([start])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==-1: d[v]=d[u]+1;q.append(v)
        ds.append(d)
    return ds


def verify(m):
    T=F(2)-F(2,m)
    G=rim_gram(m)
    check_psd_exact(G)
    d=graph_distances(m)
    sqdist=lambda i,j: G[i][i]+G[j][j]-2*G[i][j]
    ne=0;nf=0
    for a in range(2*m+1):
        for b in range(a+1,2*m+1):
            S=G[b-1][b-1] if a==0 else sqdist(a-1,b-1)
            lo=F(d[a][b]**2)
            assert lo<=S<=T*lo, (m,a,b,lo,S,T)
            ne+=d[a][b]==1
            nf+=d[a][b]==2
    assert all(G[2*i][2*j]==(T if i==j else -F(2,m)) for i in range(m) for j in range(m))
    assert all(G[2*i+1][2*j+1]==(T if i==j else -F(2,m)) for i in range(m) for j in range(m))
    assert all(sum(row)==0 for row in G)
    return ne,nf

if __name__=='__main__':
    edges=far=0
    for m in range(7,19):
        e,f=verify(m); edges+=e;far+=f
    print(f'CHECK_OK exact_rational_PSD_and_pair_bounds=12 rim_orders=14..36 edges={edges} nonedges={far}')
