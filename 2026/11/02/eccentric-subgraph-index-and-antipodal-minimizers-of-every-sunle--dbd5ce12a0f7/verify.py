"""Independent enumeration of all connected edge-subgraphs of a labelled sunlet."""
from collections import defaultdict

def brute(n):
    edges=[(i,(i+1)%n) for i in range(n)]+[(i,n+i) for i in range(n)]
    counts=[[0]*(2*n) for _ in range(2*n)]
    # Each nonempty connected edge set represents a unique connected subgraph.
    for mask in range(1,1<<(2*n)):
        involved=0
        adj=[0]*(2*n)
        for k,(a,b) in enumerate(edges):
            if (mask>>k)&1:
                involved|=(1<<a)|(1<<b)
                adj[a]|=1<<b;adj[b]|=1<<a
        reach=(involved&-involved)
        while True:
            neighbors=reach
            for i in range(2*n):
                if (reach>>i)&1:neighbors|=adj[i]
            if neighbors==reach:break
            reach=neighbors
        if reach!=involved:continue
        verts=[i for i in range(2*n) if involved>>i&1]
        for a in verts:
            for b in verts:counts[a][b]+=1
    # plus singleton connected subgraphs for diagonal entries
    for a in range(2*n):counts[a][a]+=1
    eps=[min(row) for row in counts]
    return eps,counts

def formula(n):
    if n%2==0:return (2*n-3)*2**(n-2)+2**(n//2)
    return (2*n-3)*2**(n-2)+3*2**((n-3)//2)

for n in range(3,9):
    eps,counts=brute(n);L=formula(n)
    assert eps==[2*L]*n+[L]*n, (n,eps,L)
    assert sum(eps)==3*n*L
    d=n//2
    assert counts[n][n+d]==L,(n,'minfar',counts[n][n+d],L)
    assert counts[0][n+d]==2*L
    print('n=',n,'leaf_eps=',L,'core_eps=',2*L,'ES=',3*n*L,'CHECK_OK')
print('INDEPENDENT_EDGE_SUBGRAPH_CENSUS_OK')
