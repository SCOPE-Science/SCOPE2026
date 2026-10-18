"""Exact finite verifier for patch survival and connected-pair protection on trees.

Python >=3.9, standard library only. Run: python vertex_criticality_verify.py
"""
from collections import deque
from fractions import Fraction
from itertools import product
from math import comb
from heapq import heappush, heappop


def tree_from_prufer(n, code):
    adj = [[] for _ in range(n)]
    if n == 1:
        return adj
    degrees = [1]*n
    for v in code:
        degrees[v] += 1
    leaves = []
    for v,deg in enumerate(degrees):
        if deg == 1:
            heappush(leaves,v)
    for v in code:
        u = heappop(leaves)
        adj[u].append(v); adj[v].append(u)
        degrees[u] -= 1; degrees[v] -= 1
        if degrees[v] == 1:
            heappush(leaves,v)
    a=heappop(leaves); b=heappop(leaves)
    adj[a].append(b);adj[b].append(a)
    for x in adj:
        x.sort()
    return adj


def code_unrooted(adj):
    n=len(adj)
    if n <= 2:
        centers=list(range(n))
    else:
        deg=[len(x) for x in adj]
        leaves=deque(i for i,x in enumerate(deg) if x <= 1)
        remaining=n
        while remaining > 2:
            rem=len(leaves); remaining -= rem
            for _ in range(rem):
                v=leaves.popleft()
                for u in adj[v]:
                    deg[u]-=1
                    if deg[u]==1:
                        leaves.append(u)
        centers=list(leaves)
    def encode(v,parent):
        return '(' + ''.join(sorted(encode(u,v) for u in adj[v] if u!=parent)) + ')'
    if len(centers)==1:
        return encode(centers[0],-1)
    a,b=centers
    x,y=encode(a,b),encode(b,a)
    return min(x+y,y+x)


def path_polynomials(adj):
    n=len(adj)
    coeff=[[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            parents=[-1]*n
            parents[a]=a
            queue=deque([a])
            while queue and parents[b]<0:
                v=queue.popleft()
                for u in adj[v]:
                    if parents[u]<0:
                        parents[u]=v;queue.append(u)
            path=[]
            v=b
            while v!=a:
                path.append(v);v=parents[v]
            path.append(a)
            d=len(path)-1
            for v in path:
                coeff[v][d]+=1
    return coeff


def bernstein_nonnegative(poly):
    """Exact sufficient certificate P(p)>=0 for all 0<=p<=1."""
    d=len(poly)-1
    return all(sum(poly[k]*comb(d-k,j-k) for k in range(j+1))>=0
               for j in range(d+1))


def dominate_all(coeff,v):
    return all(bernstein_nonnegative([x-y for x,y in zip(coeff[v],c)])
               for c in coeff)


def winners(coeff,p):
    vals=[sum(Fraction(c)*p**k for k,c in enumerate(poly)) for poly in coeff]
    hi=max(vals)
    return frozenset(i for i,val in enumerate(vals) if val==hi)


def verify():
    all_shapes={}
    seen_totals={}
    exceptional=[]
    for n in range(1,9):
        shapes={}
        for seq in product(range(n),repeat=max(0,n-2)):
            adj=tree_from_prufer(n,seq)
            key=code_unrooted(adj)
            if key not in shapes:
                shapes[key]=adj
        all_shapes[n]=shapes
        seen_totals[n]=len(shapes)
        print('SHAPES',n,len(shapes),flush=True)
        for key,adj in shapes.items():
            coeff=path_polynomials(adj)
            universal=[v for v in range(n) if dominate_all(coeff,v)]
            if not universal:
                assert n == 8, (n,key,adj)
                assert winners(coeff,Fraction(1,2)).isdisjoint(winners(coeff,Fraction(9,10)))
                exceptional.append((key,adj,coeff))
    assert [seen_totals[n] for n in range(1,9)]==[1,1,1,2,3,6,11,23]
    assert len(exceptional)==2
    required=[
        ([(1,0),(1,2),(0,5),(2,3),(2,4),(5,6),(6,7)], (2,1), 1),
        ([(1,0),(1,2),(0,5),(2,3),(2,4),(5,6),(5,7)], (2,0), 2),
    ]
    # Explicit labelled witnesses are independently processed, rather than trusting class labels.
    for edges,(u,v),shape in required:
        adj=[[] for _ in range(8)]
        for a,b in edges:
            adj[a].append(b);adj[b].append(a)
        coeff=path_polynomials(adj)
        assert code_unrooted(adj) in {x[0] for x in exceptional}
        if shape==1:
            assert [x-y for x,y in zip(coeff[u],coeff[v])] == [0,2,0,-2,-2,0,0,0]
            assert all(bernstein_nonnegative([x-y for x,y in zip(coeff[u],coeff[k])]) for k in [2,3,4,5,6,7])
            assert all(bernstein_nonnegative([x-y for x,y in zip(coeff[v],coeff[k])]) for k in [0,1])
            assert winners(coeff,Fraction(1,2)) == frozenset([2])
            assert winners(coeff,Fraction(9,10)) == frozenset([1])
        else:
            assert [x-y for x,y in zip(coeff[u],coeff[v])] == [0,2,0,-4,0,0,0,0]
            assert coeff[2]==coeff[5] and coeff[0]==coeff[1]
            assert all(bernstein_nonnegative([x-y for x,y in zip(coeff[u],coeff[k])]) for k in [2,3,4,5,6,7])
            assert all(bernstein_nonnegative([x-y for x,y in zip(coeff[v],coeff[k])]) for k in [0,1])
            assert winners(coeff,Fraction(1,2)) == frozenset([2,5])
            assert winners(coeff,Fraction(9,10)) == frozenset([0,1])
    # Independent direct 2^8-state expectation check for labelled example 1.
    e=required[0][0]
    adj=[[] for _ in range(8)]
    for a,b in e:adj[a].append(b);adj[b].append(a)
    c=path_polynomials(adj)
    for p in (Fraction(1,3),Fraction(2,3)):
        def connectivity_expect(protect):
            value=Fraction(0)
            remaining=[v for v in range(8) if v!=protect]
            for flags in product((0,1),repeat=7):
                live={protect}|{v for v,on in zip(remaining,flags) if on}
                prob=1
                for on in flags: prob*=p if on else 1-p
                connected=0;seen=set()
                for v in live:
                    if v in seen:continue
                    stack=[v];seen.add(v);s=0
                    while stack:
                        z=stack.pop();s+=1
                        for u in adj[z]:
                            if u in live and u not in seen:
                                seen.add(u);stack.append(u)
                    connected+=s*s
                value+=prob*connected
            return value
        observed=connectivity_expect(2)-connectivity_expect(1)
        predicted=(1-p)*sum((x-y)*p**k for k,(x,y) in enumerate(zip(c[2],c[1])))
        assert observed==predicted,(observed,predicted)
    print('VERIFY_OK unlabeled_counts=1,1,1,2,3,6,11,23 exceptions=2 exact_bernstein=PASS witness_polynomials=PASS direct_state_count=PASS')

if __name__=='__main__':verify()
