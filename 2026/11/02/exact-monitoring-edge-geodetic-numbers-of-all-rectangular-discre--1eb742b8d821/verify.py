"""Standalone check of balanced MEG sets on rectangular Cartesian cycle products.

Run: python3 verify_meg_rectangular_tori.py
Only the standard Python library is required.
"""
from collections import deque

SPECIAL_5_6 = [
    {0,2,4},{1,3,4},{0,2,4},{0,1,3},{1,2,4},{0,1,3}
]
SPECIAL_7_8 = [
    {0,2,5},{2,4,6},{1,3,5},{0,1,4},
    {2,3,6},{1,2,5},{0,1,4},{1,3,6}
]


def construct(m,n):
    assert 5 <= m <= n
    if (m,n)==(5,6):return [set(s) for s in SPECIAL_5_6]
    if (m,n)==(7,8):return [set(s) for s in SPECIAL_7_8]
    residues = {0,m//3,(2*m)//3}
    return [{(r+(m*j)//n)%m for r in residues} for j in range(n)]


def circular_gap_max(pos,n):
    if len(pos)<2:return n
    pos=sorted(pos)
    return max((b-a)%n for a,b in zip(pos,pos[1:]+pos[:1]))


def check_slices(m,n,columns):
    assert len(columns)==n
    for j in range(n):
        assert len(columns[j])==3
        assert 2*circular_gap_max(columns[j],m)<m, (m,n,j,columns[j])
    for i in range(m):
        pos=[j for j in range(n) if i in columns[j]]
        assert 2*circular_gap_max(pos,n)<n, (m,n,i,pos)


def make_graph(m,n):
    size=m*n
    edge_set=set()
    for j in range(n):
        for i in range(m):
            u=j*m+i
            for v in (j*m+(i+1)%m,((j+1)%n)*m+i):
                a,b=sorted((u,v));edge_set.add((a,b))
    edges=sorted(edge_set)
    adj=[set() for _ in range(size)]
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    return edges,adj


def bfs(adj,src,omit=None):
    dist=[-1]*len(adj);dist[src]=0;queue=deque([src])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if omit is not None and (min(u,v),max(u,v))==omit:continue
            if dist[v]<0:
                dist[v]=dist[u]+1;queue.append(v)
    return dist


def check_graph_independently(m,n,columns):
    edges,adj=make_graph(m,n)
    S=[j*m+i for j in range(n) for i in columns[j]]
    original={s:bfs(adj,s) for s in S}
    for e in edges:
        monitored=False
        for s in S:
            altered=bfs(adj,s,e)
            if any(altered[t]!=original[s][t] for t in S):
                monitored=True;break
        assert monitored,(m,n,e)
    return len(edges)


def check_forced_small_factor():
    cases=0
    for m in (3,4):
        for n in range(3,11):
            edges,adj=make_graph(m,n)
            S=[u for u in range(m*n) if u!=0]
            baseline={s:bfs(adj,s) for s in S}
            unmonitored=False
            for e in edges:
                detects=False
                for s in S:
                    altered=bfs(adj,s,e)
                    if any(altered[t]!=baseline[s][t] for t in S):
                        detects=True;break
                if not detects:
                    unmonitored=True;break
            assert unmonitored,(m,n)
            cases+=1
    return cases


def arithmetic_certificate():
    exceptions=[]
    checked=0
    for m in range(5,13):
        for n in range(m,13):
            d=(m-1)//3
            upper=(d*n+m-1)//m+1
            if 2*upper >= n:exceptions.append((m,n))
            checked+=1
    assert exceptions==[(5,6),(7,8)],exceptions
    for n in range(13,1000):
        assert 2*((n+2)//3+1)<n,n
    return checked


def run():
    finite=arithmetic_certificate()
    tested=0
    for m in range(5,71):
        for n in range(m,151):
            check_slices(m,n,construct(m,n));tested+=1
    independent=0;edge_tests=0
    forced=check_forced_small_factor()
    for m in range(5,9):
        for n in range(m,10):
            edge_tests+=check_graph_independently(m,n,construct(m,n))
            independent+=1
    print(f'VERIFY_OK: {finite} arithmetic small pairs; {tested} cycle-slice parameter pairs; '
          f'{independent} independent adjacency/BFS graph cases; {edge_tests} edge-deletion checks; '
          f'{forced} forced-small-factor graph cases')

if __name__=='__main__':run()
