"""Independently check the lifted Manhattan metric and state enumeration."""
from collections import deque, Counter
from hashlib import sha256
from itertools import combinations
import json


def brute_maximal(n):
    V=2*n
    neighbours=[{(i-1)%V,(i+1)%V,(i+n)%V} for i in range(V)]
    good=[]
    for vertices in combinations(range(V),n-2):
        group=set(vertices)
        if any(neighbours[x]&group for x in group):continue
        if any(x not in group and not(neighbours[x]&group) for x in range(V)):continue
        good.append(group)
    return good


def encoded_intervals(n):
    h=(n-1)//2
    out={}
    for b in range(1,n-2):
        for a in range(n):
            B={(2*(h*t%n)+1) for t in range(a,a+b)}
            blocked={(a-1+t)%n for t in range(b+2)}
            A={2*(h*(s-1)%n) for s in range(n) if s not in blocked}
            out[(a,b)]=A|B
    return out


def symbolic_graph(n):
    V={(a,b) for b in range(1,n-2) for a in range(n)}
    g={v:set() for v in V}
    for a,b in V:
        candidates=((a,b+1),(a-1,b+1),(a,b-1),(a+1,b-1))
        for x,c in candidates:
            v=(x%n,c)
            if v in V:
                g[(a,b)].add(v)
    return g


def formula(n,s,t):
    a,b=s;c,d=t
    q=c-a
    delta=d-b
    return min(abs(q+j*n)+abs(q+delta+j*n) for j in (-2,-1,0,1,2))


def verify():
    for n in (5,7,9,11):
        A=brute_maximal(n)
        B=encoded_intervals(n)
        assert {frozenset(z) for z in A}=={frozenset(z) for z in B.values()}
    for n in (5,7,9,11,13,15,17,19,21,25):
        adj=symbolic_graph(n)
        deg=Counter(map(len,adj.values()))
        assert len(adj)==n*(n-3)
        assert sum(deg[k]*k for k in deg)//2==2*n*(n-4)
        digest=sha256()
        eccentricities=[]
        for src in sorted(adj):
            dist={src:0};Q=deque([src])
            while Q:
                x=Q.popleft()
                for y in adj[x]:
                    if y not in dist:
                        dist[y]=dist[x]+1;Q.append(y)
            assert len(dist)==len(adj)
            eccentricities.append(max(dist.values()))
            for target in sorted(adj):
                actual=dist[target]
                predicted=formula(n,src,target)
                assert actual==predicted, (n,src,target,actual,predicted)
                digest.update(bytes((actual,)))
        assert min(eccentricities)==max(eccentricities)==n
        print(json.dumps({'n':n,'pairwise_distance_sha256':digest.hexdigest(),'vertices':len(adj),'diameter':n},sort_keys=True))
    print('VERIFY_OK')

if __name__=='__main__':verify()
