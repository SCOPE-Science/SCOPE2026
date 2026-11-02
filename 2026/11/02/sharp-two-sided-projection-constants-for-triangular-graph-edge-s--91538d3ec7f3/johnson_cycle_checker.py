"""Exact small-order consistency checks for Johnson triangular-graph projections.
Usage: python3 johnson_cycle_checker.py
This program is finite verification; the all-order proof is mathematical.
"""
from fractions import Fraction as F
from itertools import combinations

def check(n):
    verts=list(combinations(range(n),2))
    index={v:i for i,v in enumerate(verts)}
    E=[(i,j) for i in range(len(verts)) for j in range(i+1,len(verts))
       if len(set(verts[i])&set(verts[j]))==1]
    N=len(verts); M=len(E)
    assert N==n*(n-1)//2 and M==N*(n-2)
    a=F(n+1,2*n*(n-1)); b=F(1,2*n*(n-1))
    Q=[[F(0) for _ in range(M)] for _ in range(M)]
    for j,(u,v) in enumerate(E):
        shared=next(iter(set(verts[u])&set(verts[v])))
        one=(set(verts[u])-{shared}).pop()
        two=(set(verts[v])-{shared}).pop()
        phi=[F(0) for _ in verts]
        phi[u]=a;phi[v]=-a
        for t in range(n):
            if t not in (shared,one,two):
                phi[index[tuple(sorted((one,t)))]]=b
                phi[index[tuple(sorted((two,t)))]]=-b
        assert sum(phi)==0
        # Laplacian of phi must equal the endpoint incidence vector.
        lap=[F(0) for _ in verts]
        for x,y in E:
            t=phi[x]-phi[y]
            lap[x]+=t;lap[y]-=t
        assert lap[u]==1 and lap[v]==-1
        assert all(lap[i]==0 for i in range(N) if i not in (u,v))
        for i,(x,y) in enumerate(E):Q[i][j]=phi[x]-phi[y]
    assert all(Q[i][j]==Q[j][i] for i in range(M) for j in range(M))
    # Orthogonal projection on cut gradients: divergence identity B Q = B.
    for j,(u,v) in enumerate(E):
        div=[F(0) for _ in verts]
        for i,(x,y) in enumerate(E):
            div[x]+=Q[i][j];div[y]-=Q[i][j]
        assert all(div[x]==(int(x==u)-int(x==v)) for x in range(N))
    cut=F((n-2)*(3*n-1),n*(n-1))
    cyc=F(2*(2*n-5),n-1)
    for j in range(M):
        assert sum(abs(Q[i][j]) for i in range(M))==cut
        assert sum(abs(F(i==j)-Q[i][j]) for i in range(M))==cyc
        assert Q[j][j]==F(n+1,n*(n-1))
    return N,M,cut,cyc

if __name__=='__main__':
    for n in range(3,10):
        print('n=%s vertices=%s edges=%s cut=%s circulation=%s'%((n,)+check(n)))
    print('CHECK_OK: exact incidence, potential, symmetry, and full column norms')
