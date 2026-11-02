"""Exact-rational independent verification of degree-two fractional hedonic optimization."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import random

def dp_path(n, weights):
    f = [Q(0)] + [None] * n
    choices = [None] * (n+1)
    for j in range(1,n+1):
        opts=[(f[j-1],1)]
        if j>=2: opts.append((f[j-2]+weights[j-2],2))
        if j>=3: opts.append((f[j-3]+Q(2,3)*(weights[j-3]+weights[j-2]),3))
        f[j],choices[j]=max(opts)
    ans=[];j=n
    while j:
        k=choices[j];ans.append(tuple(range(j-k,j)));j-=k
    return f[n],ans[::-1]

def dp_cycle(n, weights):
    """Six interval cases; O(n) arithmetic operations including witness extraction."""
    if n==3:
        edges=[(i,(i+1)%3,weights[i]) for i in range(3)]
        return max(((value_partition(3,edges,p),p) for p in partitions(3)), key=lambda x:x[0])
    opts=[]
    tiles=(
        ((0,),1,n-1,Q(0)),
        ((0,1),2,n-1,weights[0]),
        ((n-1,0),1,n-2,weights[n-1]),
        ((0,1,2),3,n-1,Q(2,3)*(weights[0]+weights[1])),
        ((n-1,0,1),2,n-2,Q(2,3)*(weights[n-1]+weights[0])),
        ((n-2,n-1,0),1,n-3,Q(2,3)*(weights[n-2]+weights[n-1])),
    )
    for tile,lo,hi,tileval in tiles:
        if lo<=hi:
            restval,restparts=dp_path(hi-lo+1,weights[lo:hi])
            partition=[tile]+[tuple(lo+i for i in p) for p in restparts]
        else:
            restval=Q(0)
            partition=[tile]
        opts.append((tileval+restval,partition))
    return max(opts,key=lambda t:t[0])

def solve_graph(n, edges):
    """Return optimum and partition on a simple graph of maximum degree two.

    Vertex labels are 0,...,n-1; each edge is (u, v, rational_weight).
    Operation count O(n+|E|) apart from rational integer-bit arithmetic.
    """
    adj=[[] for _ in range(n)]
    for u,v,w in edges:
        if not (0<=u<n and 0<=v<n and u!=v):
            raise ValueError('invalid edge')
        if any(x==v for x,_ in adj[u]):
            raise ValueError('parallel edge')
        adj[u].append((v,Q(w)))
        adj[v].append((u,Q(w)))
    if any(len(a)>2 for a in adj):
        raise ValueError('maximum degree exceeds two')
    seen=set()
    answer=Q(0); allparts=[]
    for root in range(n):
        if root in seen: continue
        comp=[]; stack=[root]; seen.add(root)
        while stack:
            u=stack.pop(); comp.append(u)
            for v,w in adj[u]:
                if v not in seen:
                    seen.add(v); stack.append(v)
        if len(comp)==1:
            allparts.append((root,));continue
        degree1=[u for u in comp if len(adj[u])==1]
        start=degree1[0] if degree1 else comp[0]
        sequence=[start];parent=-1
        while len(sequence)<len(comp):
            u=sequence[-1]
            nxt=[v for v,w in adj[u] if v!=parent]
            if len(nxt)==2 and parent==-1:
                nxt=nxt[:1]
            if len(nxt)!=1:
                raise AssertionError('unexpected component')
            parent,u=u,nxt[0]
            sequence.append(u)
        m=[{v:w for v,w in adj[u]} for u in sequence]
        weights=[m[j][sequence[j+1]] for j in range(len(sequence)-1)]
        if degree1:
            val,localparts=dp_path(len(sequence),weights)
        else:
            weights.append(m[-1][sequence[0]])
            val,localparts=dp_cycle(len(sequence),weights)
        answer+=val
        allparts += [tuple(sequence[x] for x in p) for p in localparts]
    return answer,allparts

def value_partition(n,edges,partition):
    t=Q(0)
    for p in partition:
        P=set(p)
        W=sum((w for i,j,w in edges if i in P and j in P),Q(0))
        t+=Q(2,len(P))*W
    return t

def partitions(n):
    b=[]
    def rec(i):
        if i==n:
            yield tuple(tuple(z) for z in b)
            return
        for j in range(len(b)):
            b[j].append(i)
            yield from rec(i+1)
            b[j].pop()
        b.append([i])
        yield from rec(i+1)
        b.pop()
    yield from rec(0)

def brute(n, edges):
    return max((value_partition(n,edges,p) for p in partitions(n)),default=Q(0))

def validate():
    rng=random.Random(314159)
    comparisons=0
    for n in range(1,9):
        for kind in ('path','cycle'):
            if kind=='cycle' and n<3: continue
            edges_index=[(i,i+1) for i in range(n-1)]
            if kind=='cycle': edges_index.append((n-1,0))
            # All {-1,0,1} weights up to 6 edges, random thereafter
            if len(edges_index)<=6:
                weights_cases=list(product((-1,0,1),repeat=len(edges_index)))
            else:
                weights_cases=[tuple(rng.randrange(-4,5) for _ in edges_index) for __ in range(12)]
            for weights in weights_cases:
                edges=[(u,v,Q(w)) for (u,v),w in zip(edges_index,weights)]
                if kind=='path':
                    value,partition=dp_path(n,[Q(w) for w in weights])
                else:
                    value,partition=dp_cycle(n,[Q(w) for w in weights])
                actual=value_partition(n,edges,partition)
                assert value==actual,('witness',kind,n,weights,value,actual)
                expected=brute(n,edges)
                assert value==expected,('optimality',kind,n,weights,value,expected)
                comparisons+=1
    # Arbitrary disconnected unions of paths and cycles (including isolates).
    mixed_cases=0
    for n in range(1,9):
        repetitions=80 if n<=7 else 20
        for _ in range(repetitions):
            ordering=list(range(n));rng.shuffle(ordering)
            parts=[];pos=0
            while pos<n:
                size=rng.randrange(1,min(5,n-pos)+1)
                parts.append(ordering[pos:pos+size]);pos+=size
            edges=[]
            for comp in parts:
                for i in range(len(comp)-1):
                    edges.append((comp[i],comp[i+1],Q(rng.randrange(-4,5))))
                if len(comp)>=3 and rng.randrange(2):
                    edges.append((comp[-1],comp[0],Q(rng.randrange(-4,5))))
            opt,partition=solve_graph(n,edges)
            assert opt==value_partition(n,edges,partition)
            assert opt==brute(n,edges),('disconnected',n,edges,opt,brute(n,edges))
            mixed_cases+=1
    # structural sharpness
    path=[(0,1,Q(1)),(1,2,Q(1))]
    assert brute(3,path)==Q(4,3)
    assert max(value_partition(3,path,p) for p in partitions(3) if max(map(len,p))<=2)==Q(1)
    claw=[(0,1,Q(1)),(0,2,Q(1)),(0,3,Q(1))]
    assert brute(4,claw)==Q(3,2)
    assert max(value_partition(4,claw,p) for p in partitions(4) if max(map(len,p))<=3)==Q(4,3)
    print('PASS',comparisons,'connected path/cycle cases;',mixed_cases,'disconnected cases; sharpness P3/K1,3')

if __name__=='__main__':validate()
