"""BFS geodesics and opposite-parity walk distances, without colour refinement."""
from collections import deque
from math import comb


def edges(m,n):
    edges = [[] for _ in range(m*n)]
    for i in range(m):
        for j in range(n):
            k = i*n+j
            edges[k]=[((i+1)%m)*n+j,((i-1)%m)*n+j,
                      i*n+(j+1)%n,i*n+(j-1)%n]
    return edges


def distances_and_counts(adj):
    dist=[-1]*len(adj); ways=[0]*len(adj)
    dist[0]=0; ways[0]=1; Q=deque([0])
    while Q:
        u=Q.popleft()
        for v in adj[u]:
            if dist[v]<0:
                dist[v]=dist[u]+1
                Q.append(v)
            if dist[v]==dist[u]+1:
                ways[v]+=ways[u]
    return dist,ways


def parity_distances(adj):
    N=len(adj)
    dist=[[-1,-1] for _ in range(N)]
    dist[0][0]=0;Q=deque([(0,0)])
    while Q:
        u,p=Q.popleft()
        for v in adj[u]:
            if dist[v][1-p]<0:
                dist[v][1-p]=dist[u][p]+1
                Q.append((v,1-p))
    return dist


def check():
    cases=verts=0
    for m in range(5,24,2):
        for n in range(m+2,36,2):
            adj=edges(m,n)
            dist, ways=distances_and_counts(adj)
            both=parity_distances(adj)
            for x in range(m):
                for y in range(n):
                    i=x*n+y
                    a=min(x,m-x); b=min(y,n-y); d=a+b
                    assert dist[i]==d and ways[i]==comb(d,a), (m,n,x,y,'geodesic')
                    alternate=both[i][1-d%2]
                    assert alternate>=0, (m,n,i,'alt')
                    odd_gap=alternate-d
                    assert odd_gap==min(m-2*a,n-2*b), (m,n,x,y,odd_gap,'odd gap')
            cases+=1;verts+=m*n
    print(f'WALK_PASS cases={cases} vertices={verts}')


if __name__=='__main__':
    check()
