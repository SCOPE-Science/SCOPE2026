#!/usr/bin/env python3
"""Verify exact mutual-visibility token-slide distances on complete bicliques.

Use: python verifier.py
The first check uses the original all-geodesics definition, rather than the
known type characterization. It constructs the slide graph and performs BFS.
The second checks all feasible type/intersection patterns in larger hosts.
"""
from collections import deque
from itertools import combinations


def visible(mask, m, n):
    # For any selected pair, explicitly test for a selected-avoiding shortest path.
    N=m+n
    adj=[set(range(m,N)) if v<m else set(range(m)) for v in range(N)]
    vertices=[v for v in range(N) if mask >> v & 1]
    for v,w in combinations(vertices,2):
        # These complete-bipartite graphs have diameter 2.
        if w in adj[v]:
            continue
        if not any(z not in vertices and z in adj[v] and w in adj[z] for z in range(N)):
            return False
    return True


def formula(s,t,m):
    A=(1<<m)-1
    return max(((s^t)&A).bit_count(), ((s^t)&~A).bit_count())


def ok_type(a,b,m,n):
    return (a<=1 or b<n) and (b<=1 or a<m)


def type_diameter(m,n,k):
    allowed=[a for a in range(max(0,k-n),min(k,m)+1) if ok_type(a,k-a,m,n)]
    answer=0
    for a in allowed:
        b=k-a
        for c in allowed:
            d=k-c
            for shared_A in range(max(0,a+c-m),min(a,c)+1):
                for shared_B in range(max(0,b+d-n),min(b,d)+1):
                    answer=max(answer, a+c-2*shared_A, b+d-2*shared_B)
    return answer


def verify_BFS(m,n,k):
    N=m+n
    vertices=[sum(1<<v for v in c) for c in combinations(range(N),k)]
    vertices=[v for v in vertices if visible(v,m,n)]
    V=set(vertices)
    adj={s:[] for s in vertices}
    for s in vertices:
        for a in range(m):
            for b in range(m,N):
                if ((s>>a)&1)!=((s>>b)&1):
                    nxt=s^(1<<a)^(1<<b)
                    if nxt in V:adj[s].append(nxt)
    if k==m+n-2 and m>=4 and n>=4:
        assert all(len(adj[s])==0 for s in vertices)
        assert len(vertices)==m*n
        return len(vertices),0
    actual_diameter=0
    total_pairs=0
    for source in vertices:
        d={source:0};todo=deque([source])
        while todo:
            s=todo.popleft()
            for t in adj[s]:
                if t not in d:
                    d[t]=d[s]+1;todo.append(t)
        assert len(d)==len(vertices),(m,n,k,source,len(d),len(vertices))
        for t,steps in d.items():
            assert steps==formula(source,t,m),(m,n,k,source,t,steps,formula(source,t,m))
            actual_diameter=max(actual_diameter,steps)
            total_pairs+=1
    if k==m+n-2:
        predicted=3
    else:
        predicted=min(2*k,2*(m+n-k-1),max(m,n))
    assert actual_diameter==predicted,(m,n,k,actual_diameter,predicted)
    return len(vertices),total_pairs


def main():
    bfs_cases=0;bfs_pairs=0;bfs_configurations=0
    for m in range(3,8):
        for n in range(m,8):
            if m+n>10:continue
            for k in range(0,m+n-1):
                num,pairs=verify_BFS(m,n,k)
                bfs_cases+=1;bfs_pairs+=pairs;bfs_configurations+=num
    enumeration_cases=0
    for m in range(3,18):
        for n in range(m,18):
            for k in range(0,m+n-1):
                if k==m+n-2 and m>3:continue
                expected=3 if k==m+n-2 else min(2*k,2*(m+n-k-1),n)
                assert type_diameter(m,n,k)==expected,(m,n,k)
                enumeration_cases+=1
    print(f'VERIFY_OK bfs_cases={bfs_cases} bfs_pairs={bfs_pairs} bfs_configurations={bfs_configurations} type_extrema={enumeration_cases}')

if __name__=='__main__':
    main()
