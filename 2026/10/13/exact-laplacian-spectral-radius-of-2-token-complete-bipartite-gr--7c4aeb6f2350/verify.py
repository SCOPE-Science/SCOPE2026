#!/usr/bin/env python3
from itertools import combinations
from collections import deque

def matvec3(B, z):
    return [sum(B[i][j]*z[j] for j in range(3)) for i in range(3)]

def token_graph(m, n):
    N = m+n
    verts = list(combinations(range(N), 2))
    index = {v:i for i,v in enumerate(verts)}
    adj = [set() for _ in verts]
    def cross(u,v):
        return (u < m) != (v < m)
    for i,s in enumerate(verts):
        ss=set(s)
        for u in s:
            for v in range(N):
                if v in ss or not cross(u,v):
                    continue
                t=tuple(sorted((ss-{u})|{v}))
                j=index[t]
                adj[i].add(j)
    return verts, adj

def cell(v,m):
    a=sum(x<m for x in v)
    return {2:0,1:1,0:2}[a]

def check_full(m,n):
    verts,adj=token_graph(m,n)
    N=len(verts)
    # connectivity
    seen={0}
    q=deque([0])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    assert len(seen)==N
    # parity bipartition and exact local cell counts
    expected = {
        0:(2*n,(0,2*n,0)),
        1:(m+n-2,(m-1,0,n-1)),
        2:(2*m,(0,2*m,0)),
    }
    zcell=[n*(n-1),(m-1)*(n-1),m*(m-1)]
    lam=2*(m+n-1)
    for i,v in enumerate(verts):
        c=cell(v,m)
        deg=len(adj[i])
        assert deg==expected[c][0]
        counts=[0,0,0]
        for j in adj[i]:
            cj=cell(verts[j],m)
            counts[cj]+=1
            assert (c==1) != (cj==1)
        assert tuple(counts)==expected[c][1]
        # Q=D+A applied to the lifted vector.
        lhs=deg*zcell[c] + sum(zcell[cell(verts[j],m)] for j in adj[i])
        assert lhs==lam*zcell[c]

def main():
    exact=0
    for m in range(2,101):
        for n in range(2,101):
            B=[[2*n,2*n,0],
               [m-1,m+n-2,n-1],
               [0,2*m,2*m]]
            z=[n*(n-1),(m-1)*(n-1),m*(m-1)]
            lam=2*(m+n-1)
            assert min(z)>0
            assert matvec3(B,z)==[lam*x for x in z]
            exact+=1
    full=0
    maxv=0
    for m in range(2,7):
        for n in range(m,7):
            check_full(m,n)
            full+=1
            maxv=max(maxv,(m+n)*(m+n-1)//2)
    print(
        "ALL CHECKS PASSED; "
        f"exact_quotient_cases={exact}; "
        f"full_graph_cases={full}; "
        f"full_graph_max_vertices={maxv}; "
        "exact_parameter_range=2<=m,n<=100; "
        "full_graph_range=2<=m<=n<=6"
    )

if __name__=="__main__":
    main()
