#!/usr/bin/env python3
from itertools import permutations
from collections import defaultdict

GRAPH6 = ['@', 'A_', 'Bo', 'Bw', 'CF', 'Ck', 'CN', 'Cl', 'D?{', 'DBc', 'Dh_', 'D@{', 'Dx_', 'DJc', 'DbW', 'Dhc', 'E?Bw', 'EhP?', 'EsCO', 'EiGO', 'EBe?', 'E`EG', 'E?Fw', 'EC{O', 'E@dW', 'EG}?', 'E]a?', 'EYWO', 'E]_O', 'EQKo', 'EsCW', 'EJe?', 'EBy?', 'Ehd?', 'EhEG', 'F??Fw', 'FhG`?', 'FiO`?', 'FiOG_', 'FiO_G', 'FIo`?', 'Fk_`?', 'FaOH_', 'FEW`?', 'Fk_G_', 'FhCK?', 'FsaC_', 'FItA?', 'F?Bcw', 'FkoK?', 'FhG`G', 'FMpA?', 'FhoI?', 'FhoGO', 'FHAgg', 'FiG`G', 'FbW`?', 'FiO`G', 'FMoG_', 'Fg?hg', 'Fko`?', 'Fpq?_', 'FMoa?', 'Fpq?G', 'Fpa?g', 'FhoG_', 'FhD@G', 'FhoGG', 'FIo`G', 'Fh_gG', 'FpQO_', 'FXAGg', 'Fk_`G', 'FMo`?', 'FK_h_', 'FIc`G', 'FMo@G', 'FPq?g', 'FhCKG']

def decode_graph6(s):
    vals=[ord(c)-63 for c in s]
    n=vals[0]
    bits=[]
    for x in vals[1:]:
        bits.extend((x>>k)&1 for k in (5,4,3,2,1,0))
    adj=[[0]*n for _ in range(n)]
    t=0
    for j in range(1,n):
        for i in range(j):
            if bits[t]: adj[i][j]=adj[j][i]=1
            t+=1
    return adj

def edges(adj):
    return sum(sum(row) for row in adj)//2

def connected(adj):
    n=len(adj)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v,x in enumerate(adj[u]):
            if x and v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==n

def partition_from_colors(colors):
    d=defaultdict(set)
    for v,c in enumerate(colors): d[c].add(v)
    return frozenset(frozenset(s) for s in d.values())

def stable_partition(adj):
    n=len(adj); colors=[0]*n; prev=None
    for _ in range(n+3):
        part=partition_from_colors(colors)
        if part==prev: return part
        prev=part
        sig=[]
        for v in range(n):
            sig.append((colors[v], tuple(sorted(colors[w] for w in range(n) if adj[v][w]))))
        names={}; colors=[names.setdefault(s,len(names)) for s in sig]
    raise AssertionError('did not stabilize')

def orbit_partition(adj):
    n=len(adj)
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: parent[b]=a
    deg=[sum(row) for row in adj]
    for p in permutations(range(n)):
        if any(deg[i]!=deg[p[i]] for i in range(n)): continue
        ok=True
        for i in range(n):
            for j in range(i+1,n):
                if adj[i][j]!=adj[p[i]][p[j]]:
                    ok=False; break
            if not ok: break
        if ok:
            for i in range(n): union(i,p[i])
    d=defaultdict(set)
    for i in range(n): d[find(i)].add(i)
    return frozenset(frozenset(s) for s in d.values())

def barbell_3_2():
    n=8; adj=[[0]*n for _ in range(n)]
    def add(u,v): adj[u][v]=adj[v][u]=1
    for tri in ((0,1,2),(5,6,7)):
        a,b,c=tri; add(a,b); add(a,c); add(b,c)
    add(2,3); add(3,4); add(4,5)
    return adj

checked=0
for s in GRAPH6:
    adj=decode_graph6(s); n=len(adj)
    assert connected(adj)
    beta=edges(adj)-n+1
    assert beta in (0,1)
    assert stable_partition(adj)==orbit_partition(adj), (s,n,beta)
    checked+=1

B=barbell_3_2()
assert edges(B)-len(B)+1==2
sp=stable_partition(B); op=orbit_partition(B)
assert sp!=op
assert frozenset({0,1,3,4,6,7}) in sp
assert frozenset({3,4}) in op and frozenset({0,1,6,7}) in op
print(f'VERIFY_OK atlas_graphs={checked} n<=7 beta<=1 counterexample_beta2=PASS')
