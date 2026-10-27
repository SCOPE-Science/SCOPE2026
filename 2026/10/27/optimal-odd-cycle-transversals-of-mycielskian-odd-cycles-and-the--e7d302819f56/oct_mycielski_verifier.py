#!/usr/bin/env python3
"""Reproduce finite checks for minimum odd-cycle transversals of Mycielskian odd cycles.

Proof for the complete infinite family is given in RESULT.md; these finite
checks are independent computational checks, not the source of the universal claim.
Run: python oct_mycielski_verifier.py
"""
from collections import Counter, deque
from itertools import combinations


def graph(n):
    assert n >= 3 and n % 2 == 1
    edges = set()
    def add(i, j):
        assert i != j
        edges.add((min(i, j), max(i, j)))
    for i in range(n):
        j = (i + 1) % n
        add(i, j)
        add(i, n + j)
        add(n + i, j)
        add(n + i, 2 * n)
    adj = [set() for _ in range(2*n+1)]
    for i, j in edges:
        adj[i].add(j); adj[j].add(i)
    return sorted(edges), adj


def bip_bfs(nv, adj, deleted):
    d = set(deleted)
    col = [-1] * nv
    for i in range(nv):
        if i in d or col[i] >= 0:
            continue
        col[i] = 0
        queue = deque([i])
        while queue:
            a = queue.popleft()
            for b in adj[a]:
                if b in d:
                    continue
                if col[b] == -1:
                    col[b] = 1 - col[a]
                    queue.append(b)
                elif col[b] == col[a]:
                    return False
    return True


def bip_unionfind(nv, edges, deleted):
    d = set(deleted)
    parent = list(range(nv))
    rank = [0]*nv
    parity = [0]*nv
    def find(x):
        if x != parent[x]:
            p = parent[x]
            z = find(p)
            parity[x] ^= parity[p]
            parent[x] = z
        return parent[x]
    for i,j in edges:
        if i in d or j in d:
            continue
        a,b = find(i),find(j)
        if a == b:
            if (parity[i]^parity[j]) != 1:
                return False
        else:
            if rank[a] < rank[b]:
                a,b = b,a
                i,j = j,i
            parent[b] = a
            parity[b] = parity[i]^parity[j]^1
            if rank[a] == rank[b]: rank[a] += 1
    return True


def predicted(n):
    w = 2*n
    S = [frozenset((w,i,(i+1)%n)) for i in range(n)]
    T = [frozenset((w,i,n+i)) for i in range(n)]
    R = []
    if n == 5:
        R = [frozenset((i,(i+1)%n,(i+3)%n)) for i in range(n)]
    return S,T,R


def exchange_graph(sets):
    res=[set() for _ in sets]
    for a,b in combinations(range(len(sets)),2):
        if len(sets[a]&sets[b]) == len(sets[a])-1:
            res[a].add(b)
            res[b].add(a)
    return res


def template(n, sets, S,T,R):
    idx={s:i for i,s in enumerate(sets)}
    adj=[set() for _ in sets]
    def connect(a,b):
        u,v=idx[a],idx[b]
        adj[u].add(v);adj[v].add(u)
    for i in range(n):
        connect(S[i], S[(i+1)%n])
        connect(T[i], S[i])
        connect(T[i], S[(i-1)%n])
    if n==5:
        for i in range(n):
            connect(R[i],R[(i+2)%n])
            connect(R[i],S[i])
    return adj


def distances(adjacency):
    N=len(adjacency)
    ecc=[];counts=Counter()
    for a in range(N):
        dd={a:0}
        q=deque([a])
        while q:
            i=q.popleft()
            for j in adjacency[i]:
                if j not in dd:
                    dd[j]=dd[i]+1
                    q.append(j)
        assert len(dd)==N
        ecc.append(max(dd.values()))
        for b,v in dd.items():
            if b>a:
                counts[v]+=1
    assert sum(counts.values())==N*(N-1)//2
    return ecc,counts


def verify(n):
    edges,adj=graph(n)
    nv=len(adj)
    expected_min = 2 if n == 3 else 3
    optimal=[]
    for k in range(expected_min+1):
        for t in combinations(range(nv), k):
            a=bip_bfs(nv,adj,t)
            b=bip_unionfind(nv,edges,t)
            assert a==b, (n,t,a,b)
            if a:
                assert k==expected_min, (n,k,t)
                optimal.append(frozenset(t))
    if n==3:
        assert set(optimal)=={frozenset(x) for x in combinations(range(3),2)}
        return {'n':n,'minimum':2,'count':3}
    S,T,R=predicted(n)
    expected=set(S+T+R)
    assert len(expected)==2*n+(5 if n==5 else 0)
    assert set(optimal)==expected, (n,set(optimal)^expected)
    if n in (5,7,9,11,13):
        sets=sorted(optimal,key=lambda x:tuple(sorted(x)))
        brute=exchange_graph(sets)
        structural=template(n,sets,S,T,R)
        assert brute==structural, n
        ecc, dist=distances(brute)
        assert sum(len(a) for a in brute)//2 == (3*n+(2*n if n==5 else 0))
        assert len(set(ecc))==1
        assert ecc[0] == (3 if n==5 else (n+1)//2)
        return {'n':n,'minimum':3,'count':len(optimal),'edges':sum(map(len,brute))//2,
                'diameter':ecc[0],'distances':dict(sorted(dist.items()))}
    return {'n':n,'minimum':3,'count':len(optimal)}


def main():
    for n in range(3,26,2):
        record=verify(n)
        print(record)
    print('VERIFY_OK')

if __name__=='__main__':main()
