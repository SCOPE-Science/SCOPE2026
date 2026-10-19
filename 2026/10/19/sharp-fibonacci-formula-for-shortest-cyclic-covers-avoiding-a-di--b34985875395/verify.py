#!/usr/bin/env python3
"""Independent finite checks of an exact cyclic covering formula for 110-avoiding words."""
from collections import Counter
from itertools import product

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def levels(k):
    assert k>=3
    vertices=[''.join(v) for v in product('01',repeat=k-1) if '110' not in ''.join(v)]
    mandatory=[''.join(v) for v in product('01',repeat=k) if '110' not in ''.join(v)]
    deg={v:0 for v in vertices}
    edges=[]
    for w in mandatory:
        p,q=w[:-1],w[1:]
        edges.append((p,q));deg[p]+=1;deg[q]-=1
    excess_plus=sorted(v for v in vertices if deg[v]>0)
    excess_minus=sorted(v for v in vertices if deg[v]<0)
    assert all(abs(d)<=1 for d in deg.values())
    assert len(excess_plus)==len(excess_minus)==fib(k-1)
    assert all(v.startswith('10') and not v.endswith('11') for v in excess_plus)
    assert all(v.endswith('11') and not v.startswith('10') for v in excess_minus)
    for s,t in zip(excess_minus,excess_plus):
        here=s
        assert here[-1]==t[0]
        for bit in t[1:]:
            nxt=(here+bit)[1:]
            edges.append((here,nxt));here=nxt
        assert here==t
    assert len(edges)==fib(k+3)-1+(k-2)*fib(k-1)
    edgebalance=Counter()
    graph={}
    for u,v in edges:
        edgebalance[u]+=1;edgebalance[v]-=1
        graph.setdefault(u,[]).append(v)
    assert all(not d for d in edgebalance.values())
    # Hierholzer's algorithm, using each required or added edge exactly once.
    start='0'*(k-1)
    stack=[start]; tour=[]
    while stack:
        u=stack[-1]
        if graph.get(u): stack.append(graph[u].pop())
        else: tour.append(stack.pop())
    tour.reverse()
    assert len(tour)==len(edges)+1 and tour[0]==tour[-1]
    host=''.join(tour[i+1][-1] for i in range(len(edges)))
    seen=Counter(''.join(host[(j+t)%len(host)] for t in range(k)) for j in range(len(host)))
    assert all(seen[w]>=1 for w in mandatory)
    assert sum(seen.values())==len(edges)
    return len(mandatory),len(edges),sum('110' in w for w in seen)

if __name__=='__main__':
    expected=[(3,7,8),(4,12,16),(5,20,29),(6,33,53),(7,54,94),(8,88,166),(9,143,290),(10,232,504)]
    for k,n,c in expected:
        found=levels(k)
        assert found[:2]==(n,c),(k,found,(n,c))
    for k in range(11,17): levels(k)
    print('VERIFY_OK cyclic_hosts_k=3..16 exact_coverage_and_length')
