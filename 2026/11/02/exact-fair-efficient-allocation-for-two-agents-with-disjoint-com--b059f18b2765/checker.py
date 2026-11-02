#!/usr/bin/env python3
"""Exact reachable-signature DP for two additive disjoint-pair valuations.
Only standard-library Python. Run `python3 checker.py` for standalone tests.
"""
from collections import defaultdict
from itertools import combinations
import random


def pairs_to_edges(n, A, B):
    edges=[]
    for color, pairs in [('A',A),('B',B)]:
        used=set()
        for x,y in pairs:
            assert 0<=x<n and 0<=y<n and x!=y
            assert x not in used and y not in used
            used.add(x);used.add(y)
            edges.append((x,y,color))
    return edges


def components(n, A, B):
    edges=pairs_to_edges(n,A,B)
    adj=[[] for _ in range(n)]
    for j,(x,y,col) in enumerate(edges):
        adj[x].append(j);adj[y].append(j)
    seen=set(); comps=[]
    for start in range(n):
        if start in seen: continue
        block=[]; todo=[start];seen.add(start)
        while todo:
            x=todo.pop();block.append(x)
            for eid in adj[x]:
                a,b,_=edges[eid];y=a^b^x
                if y not in seen:seen.add(y);todo.append(y)
        block.sort()
        ids={eid for x in block for eid in adj[x]}
        cyc = bool(ids) and len(ids)==len(block)
        st=block[0] if cyc or not ids else next(x for x in block if len(adj[x])==1)
        path=[st]; walk=[]; visited=set(); at=st
        while True:
            avail=[eid for eid in adj[at] if eid in ids and eid not in visited]
            if not avail: break
            eid=min(avail); visited.add(eid)
            a,b,col=edges[eid]; nxt=a^b^at
            walk.append(col)
            if nxt==st:
                assert cyc and len(visited)==len(ids)
                break
            path.append(nxt);at=nxt
        assert set(path)==set(block)
        assert len(walk)==len(ids)
        assert len(walk)==len(path) if cyc else len(walk)==len(path)-1
        comps.append((path,walk,cyc))
    return comps


def increment(v, col, x, y):
    if x!=y: return v
    a,b,c,d=v
    if col=='A':
        return (a+1,b,c,d) if x==0 else (a,b,c+1,d)
    return (a,b+1,c,d) if x==1 else (a,b,c,d+1)


def exact_signatures(n,A,B):
    """Map (own A,own B,cross A,cross B) to a representative assignment mask.

    At every point retain just the four integer statistics, the first and
    previous colors of the current path/cycle, and one representative.
    This is a streaming transfer DP; it never multiplies component tables.
    Bit 0 means A receives the item, bit 1 means B receives it.
    """
    states={(0,0,0,0):0}
    for vertices,cols,cyc in components(n,A,B):
        layer={}
        vertex=vertices[0]
        for (a,b,c,d),mask in states.items():
            for bit in (0,1):
                layer.setdefault((bit,bit,a,b,c,d),mask|(bit<<vertex))
        for j in range(1,len(vertices)):
            nxt={}; vertex=vertices[j]
            for (first,prev,a,b,c,d),mask in layer.items():
                for bit in (0,1):
                    nv=increment((a,b,c,d),cols[j-1],prev,bit)
                    key=(first,bit,*nv)
                    nxt.setdefault(key,mask|(bit<<vertex))
            layer=nxt
        nextglobal={}
        for (first,last,a,b,c,d),mask in layer.items():
            signature=increment((a,b,c,d),cols[-1],last,first) if cyc else (a,b,c,d)
            nextglobal.setdefault(signature,mask)
        states=nextglobal
    return states


def direct_signature(n, A, B, mask):
    a=sum(not(mask>>x&1) and not(mask>>y&1) for x,y in A)
    c=sum((mask>>x&1) and (mask>>y&1) for x,y in A)
    b=sum((mask>>x&1) and (mask>>y&1) for x,y in B)
    d=sum(not(mask>>x&1) and not(mask>>y&1) for x,y in B)
    return (a,b,c,d)


def fair(v):
    a,b,c,d=v
    return a+1>=c and b+1>=d


def frontier(states):
    vals={(a,b) for a,b,_,_ in states}
    return {pair for pair in vals if not any(x>=pair[0] and y>=pair[1] and (x>pair[0] or y>pair[1]) for x,y in vals)}


def report(n,A,B):
    states=exact_signatures(n,A,B)
    f=frontier(states)
    valid={v:m for v,m in states.items() if fair(v) and v[:2] in f}
    welfare=max((v[0]+v[1] for v in states if fair(v)),default=None)
    witness=next(iter(valid.values()),None)
    return bool(valid),welfare,witness,states


def matching_cycle(length):
    n=2*length
    return n,[(2*i,2*i+1) for i in range(length)],[(2*i+1,(2*i+2)%n) for i in range(length)]


def brute(n,A,B):
    states={direct_signature(n,A,B,mask) for mask in range(1<<n)}
    f=frontier(states)
    valid=any(fair(v) and v[:2] in f for v in states)
    best=max((a+b for a,b,c,d in states if fair((a,b,c,d))),default=0)
    return states,valid,best


def rand_matching(n,rng):
    vs=list(range(n));rng.shuffle(vs)
    stop=rng.randint(0,n//2)
    return list(zip(vs[0:2*stop:2],vs[1:2*stop:2]))


def selftest():
    tests=0
    for length in range(1,9):
        n,A,B=matching_cycle(length)
        ok,w,mask,states=report(n,A,B)
        assert ok==(length!=2),(length,ok)
        assert w==({1:1}.get(length,length-1)),(length,w)
        if 3<=length<=7:
            d,ok0,w0=brute(n,A,B)
            assert set(states)==d and ok==ok0 and w==w0
        tests+=1
    rng=random.Random(0xCE51)
    for n,rep in [(2,100),(4,300),(6,600),(8,450),(10,200),(12,50)]:
        for _ in range(rep):
            A=rand_matching(n,rng);B=rand_matching(n,rng)
            dp=report(n,A,B)
            s,ok,w=brute(n,A,B)
            assert set(dp[3])==s,('SIGNATURE',n,A,B)
            assert dp[0]==ok and dp[1]==w,('FAIR',n,A,B)
            if dp[2] is not None:assert direct_signature(n,A,B,dp[2]) in s
            tests+=1
    print('VERIFY_OK complete_signature_and_PO_EF1_cases=',tests,'single_cycle_lengths=1..8','independent_full_allocation_comparison=1700')

if __name__=='__main__':selftest()
