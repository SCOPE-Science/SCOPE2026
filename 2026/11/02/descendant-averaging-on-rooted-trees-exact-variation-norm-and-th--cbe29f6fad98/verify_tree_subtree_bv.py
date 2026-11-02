"""Exact rational tests for descendant-subtree averaging in edge total variation.

Only finite diagnostics. The proof of the unrestricted statements is analytic.
Run with Python 3.9+; standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import e, sqrt
from random import Random


def prufer_edges(seq):
    n=len(seq)+2
    degree=[1]*n
    for x in seq: degree[x]+=1
    out=[]
    for x in seq:
        leaf=next(i for i,v in enumerate(degree) if v==1)
        out.append((leaf,x))
        degree[leaf]-=1; degree[x]-=1
    leaves=[i for i,v in enumerate(degree) if v==1]
    out.append(tuple(leaves))
    return out


def rooted(parent):
    n=len(parent); children=[[] for _ in parent]
    root=parent.index(-1)
    for v,p in enumerate(parent):
        if p>=0: children[p].append(v)
    order=[root]
    for v in order: order.extend(children[v])
    assert len(order)==n
    desc=[set([i]) for i in range(n)]
    for v in reversed(order):
        for c in children[v]: desc[v].update(desc[c])
    return root,children,desc


def formula(parent):
    n=len(parent); root,children,desc=rooted(parent)
    if n==1: return F(0),{}
    sums={}
    for v in range(n):
        if v==root: continue
        t=len(desc[v]); x=parent[v]; weight=F(-1,n)
        while x!=-1:
            weight+=F(len(children[x])-1,len(desc[x]))
            x=parent[x]
        sums[v]=1+t*weight
    return max(sums.values()),sums


def brute(parent):
    n=len(parent);root,children,desc=rooted(parent)
    if n==1: return F(0),{}
    vals={}
    for v in range(n):
        if v==root: continue
        f=[int(u in desc[v]) for u in range(n)]
        tf=[F(sum(f[u] for u in desc[x]),len(desc[x])) for x in range(n)]
        vals[v]=sum(abs(tf[x]-tf[parent[x]]) for x in range(n) if x!=root)
    return max(vals.values()),vals


def build_parent(n,root,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    parent=[-2]*n;parent[root]=-1
    order=[root]
    for u in order:
        for v in adj[u]:
            if parent[v]==-2: parent[v]=u;order.append(v)
    assert len(order)==n
    return parent


def stretched_broom(n):
    # A chain of h ancestors with near-equally many leaf siblings,
    # ending in a path subtree with t vertices.
    h=max(1,int(sqrt(n)))
    t=max(1,min(n-h,int(n/e)))
    q,r=divmod(n-t-h,h)
    parent=[-1]
    previous=0
    for i in range(h):
        for _ in range(q+(i<r)):
            parent.append(previous)
        new=len(parent);parent.append(previous);previous=new
    for _ in range(t-1):
        new=len(parent);parent.append(previous);previous=new
    assert len(parent)==n
    # Terminal subtree starts at the last main-chain vertex, of size t.
    return parent


def main():
    tests=0;noncontractive=0
    for n in range(2,7):
        for seq in product(range(n),repeat=n-2):
            edges=prufer_edges(seq)
            for root in range(n):
                p=build_parent(n,root,edges)
                k,form=formula(p);kb,direct=brute(p)
                assert k==kb and form==direct,(n,seq,root,form,direct)
                degree=[0]*n
                for u,v in edges: degree[u]+=1;degree[v]+=1
                iff=(max(degree)<=2)
                assert (k<=1)==iff,(n,seq,root,k,iff)
                tests+=1
                noncontractive+=(k>1)
    rnd=Random(20261025)
    for n in (7,8,12,25,70):
        for _ in range(50):
            edges=prufer_edges(tuple(rnd.randrange(n) for _ in range(n-2)))
            p=build_parent(n,rnd.randrange(n),edges)
            k,form=formula(p);kb,direct=brute(p)
            assert k==kb and form==direct,(n,p,form,direct)
            assert k<=F(1)+F(n,1),('crude upper',n,k)
            assert float(k)<=1+n/e+1e-12,('sharp upper',n,k)
            tests+=1
    samples=[]
    for n in (100,400,1600,6400):
        p=stretched_broom(n)
        k,_=formula(p)
        assert float(k)<=1+n/e+1e-12
        samples.append((n,round(float(k)/n,8)))
    print('PASS',tests,'exact rooted-tree tests;',noncontractive,'noncontractive cases; ratio samples:',samples)

if __name__=='__main__':main()
