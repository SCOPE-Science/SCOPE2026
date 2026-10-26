#!/usr/bin/env python3
"""Independent exhaustive checker for the minimum-independent-domination reconfiguration theorem."""
from itertools import combinations
from collections import deque


def graph(s,t):
    # Vertices: c=0, long-arm a_i=1+2*i, b_i=2+2*i,
    # short-arm d_j=1+2*s+j.
    n=1+2*s+t
    edges=set()
    for i in range(s):
        a,b=1+2*i,2+2*i
        edges.add((0,a));edges.add((a,b))
    for j in range(t):edges.add((0,1+2*s+j))
    adj=[0]*n
    for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
    return n,adj,edges


def minimum_sets(n,adj):
    universe=(1<<n)-1
    by_size={}
    checked=0
    for x in range(1<<n):
        checked+=1
        if any((x&(1<<i)) and (adj[i]&x) for i in range(n)): continue
        cover=x
        for i in range(n):
            if x&(1<<i): cover|=adj[i]
        if cover==universe:by_size.setdefault(x.bit_count(),[]).append(x)
    k=min(by_size)
    return k,set(by_size[k]),checked


def expected(s,t):
    n=1+2*s+t
    # All cases described using distinct bitmask encodings
    verts=[]
    for mask in range(1<<s):
        if t==0 and mask==0:continue
        if t>=2:continue
        x=0
        for i in range(s):x|=1<<(1+2*i if mask>>i&1 else 2+2*i)
        for j in range(t):x|=1<<(1+2*s+j)
        verts.append(x)
    if t>=1:
        v=1
        for i in range(s):v|=1<<(2+2*i)
        verts.append(v)
    return set(verts)


def edges_of(sets,adj):
    es=set()
    for a,b in combinations(sorted(sets),2):
        d=a^b
        if d.bit_count()!=2:continue
        rem=a&~b
        add=b&~a
        ia=rem.bit_length()-1;ib=add.bit_length()-1
        if (adj[ia]>>ib)&1:es.add((a,b))
    return es


def expected_edges(s,t,sets):
    es=set()
    for a,b in combinations(sorted(sets),2):
        d=a^b
        if d.bit_count()!=2:continue
        ids={i for i in range(s) if (d>>(1+2*i))&1 or (d>>(2+2*i))&1}
        if len(ids)==1 and all(not(d>>(1+2*s+j)&1) for j in range(t)) and not(d&1):
            es.add((a,b))
        if t==1 and (a&1 or b&1):
            if (a&1) and d==(1|(1<<(1+2*s))):es.add((a,b))
            if (b&1) and d==(1|(1<<(1+2*s))):es.add((a,b))
    return es


def run():
    cases=0;inspected=0;sets_checked=0;edges_checked=0
    for s in range(2,7):
      for t in range(4):
        if 1+2*s+t>17:continue
        n,adj,_=graph(s,t)
        i,actual,checked=minimum_sets(n,adj)
        desired=expected(s,t)
        assert i==s+(1 if t else 0),(s,t,'independent domination',i)
        assert actual==desired,(s,t,'sets',actual^desired)
        e=edges_of(actual,adj)
        ee=expected_edges(s,t,desired)
        assert e==ee,(s,t,'edges',e^ee)
        if t==0:assert len(actual)==(1<<s)-1 and len(e)==s*(1<<(s-1))-s
        if t==1:assert len(actual)==(1<<s)+1 and len(e)==s*(1<<(s-1))+1
        if t>=2:assert len(actual)==1 and len(e)==0
        cases+=1;inspected+=checked;sets_checked+=len(actual);edges_checked+=len(e)
    print('VERIFICATION_OK graph_instances=%d independent_candidate_subsets=%d minimum_sets=%d token_slide_edges=%d'%(cases,inspected,sets_checked,edges_checked))
if __name__=='__main__':run()
