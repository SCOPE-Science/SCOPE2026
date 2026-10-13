#!/usr/bin/env python3
"""Exact verification of generalized Petersen maximal-independent-set enumerator.
Requires only the Python standard library. All formulas are checked over integers.
"""
from itertools import product
from collections import defaultdict
from math import comb

states=list(product(range(3),repeat=4))
index={s:i for i,s in enumerate(states)}
edges=[]
for i,(a,b,c,d) in enumerate(states):
    for e in range(3):
        if c==1 and (b==1 or d==1):continue
        if c==2 and (a==2 or e==2):continue
        if c==0 and not ((b==1 or d==1) and (a==2 or e==2)):continue
        edges.append((i,index[b,c,d,e],int(e!=0)))

# Compute the cyclic strongly connected core independently (Tarjan algorithm).
adj=[[] for _ in states]
for a,b,w in edges:adj[a].append((b,w))
clock=0;disc={};low={};stack=[];on=set();scc=[]
def dfs(v):
    global clock
    disc[v]=low[v]=clock;clock+=1;stack.append(v);on.add(v)
    for w,_ in adj[v]:
        if w not in disc:dfs(w);low[v]=min(low[v],low[w])
        elif w in on:low[v]=min(low[v],disc[w])
    if low[v]==disc[v]:
        comp=[]
        while True:
            w=stack.pop();on.remove(w);comp.append(w)
            if w==v:break
        scc.append(comp)
for i in range(len(states)):
    if i not in disc:dfs(i)
core=sorted(max(scc,key=len)); assert len(core)==27
other=set(range(81))-set(core)
# Any cycle outside the core would contribute to traces: exclude explicitly.
for component in scc:
    if set(component)==set(core):continue
    assert len(component)==1
    v=component[0]
    assert all(u!=v for u,_ in adj[v])
ix={s:i for i,s in enumerate(core)}
cedges=[(ix[a],ix[b],w) for a,b,w in edges if a in ix and b in ix]
assert len(cedges)==47
minpots=[-2,-2,-2,-5,0,0,-2,-3,-3,0,-4,-4,0,-4,0,0,-3,-3,-3,0,-4,-1,-6,-1,-1,-1,-3]
maxpots=[-2,-1,-1,0,-3,-3,-1,0,0,-3,-1,0,-2,0,-2,-2,-1,0,0,-4,0,-2,0,-1,-1,-1,0]
for a,b,w in cedges:
    assert minpots[b]<=minpots[a]+5*w-3
    assert maxpots[b]<=maxpots[a]+4-5*w

# Explicit closed walks realize each residue at both extrema. Concatenation
# with the five-step loop at the same marked state handles all n>=5.
witnesses={
 "min":((0,1,2,1),["00121","010121","0120121","00120121","001210121"]),
 "max":((0,1,2,2),["10122","010122","0120122","01210122","012210122"]),
}
edge_lookup={(a,b):w for a,b,w in edges}
for kind,(anchor,words) in witnesses.items():
    start=index[anchor]
    for r,word in enumerate(words):
        assert len(word)==5+r
        cur=start;weight=0
        for c in word:
            nxt=index[states[cur][1:]+(int(c),)]
            assert (cur,nxt) in edge_lookup
            weight+=edge_lookup[cur,nxt]
            cur=nxt
        assert cur==start
        assert weight == ((3*(5+r)+4)//5 if kind=="min" else 4*(5+r)//5)

# Integer polynomial operations, list of coefficients indexed by z-exponent.
def plus(a,b):
    c=[0]*max(len(a),len(b))
    for j,v in enumerate(a):c[j]+=v
    for j,v in enumerate(b):c[j]+=v
    return c
def times(a,b):
    c=[0]*(len(a)+len(b)-1)
    for j,v in enumerate(a):
        if v:
            for k,w in enumerate(b):
                if w:c[j+k]+=v*w
    return c

def get_traces(nmax):
    out=[[0]]+[[0]*(i+1) for i in range(1,nmax+1)]
    ca=[[] for _ in core]
    for a,b,w in cedges:ca[a].append((b,w))
    for initial in range(27):
        dp={initial:[1]}
        for step in range(1,nmax+1):
            nd={}
            for a,p in dp.items():
                for b,w in ca[a]:
                    if b not in nd:nd[b]=[0]*(step+1)
                    for k,v in enumerate(p):
                        if v:nd[b][k+w]+=v
            dp=nd
            if initial in dp:
                for k,v in enumerate(dp[initial]):out[step][k]+=v
    return out

tr=get_traces(27)
d=[[1]]
for n in range(1,28):
    s=[0]
    for j in range(1,n+1):s=plus(s,times(d[n-j],tr[j]))
    assert all(v%n==0 for v in s)
    d.append([-v//n for v in s])
expected={0:{0:1},3:{2:-2},4:{3:-3},5:{3:-2,4:-1},6:{4:-4},7:{5:-1},8:{5:2},9:{6:1},10:{6:1}}
for i,p in enumerate(d):
    got={k:v for k,v in enumerate(p) if v}
    assert got==expected.get(i,{}),(i,got)

# Higher exact coefficients from Newton's reciprocal-logarithm recurrence.
for n in range(28,71):
    s=[0]
    for j in range(1,min(10,n)+1):
        s=plus(s,times(d[j],tr[n-j]))
    assert all(v%n==0 for v in [0])
    tr.append([-v for v in s])

def extremal(n):
    k,r=divmod(n,5)
    mins=[10,6*k*(5*k+1),k*(5*k+2)*(14*k*k+6*k+1)//3,2*(5*k+3),(5*k+4)*(16*k*k+22*k+9)//3]
    maxs=[5,(5*k+1)*(27*k**3-9*k*k+22*k+8)//8,(5*k+2)*(9*k*k+3*k+2)//2,(5*k+3)*(9*k+4)//2,3*(5*k+4)]
    return mins[r],maxs[r]

for n in range(5,71):
    poly=tr[n]
    nonzero=[k for k,v in enumerate(poly) if v]
    assert min(nonzero)==(3*n+4)//5 and max(nonzero)==4*n//5
    lo,hi=extremal(n)
    assert poly[(3*n+4)//5]==lo,(n,'min',poly[(3*n+4)//5],lo)
    assert poly[4*n//5]==hi,(n,'max',poly[4*n//5],hi)

# Independently enumerate each vertex subset, avoiding transfer-local rules.
def brute(n):
    neighbors=[0]*(2*n)
    def connect(a,b):neighbors[a]|=1<<b;neighbors[b]|=1<<a
    for i in range(n):
        connect(i,(i+1)%n)
        connect(i,i+n)
        connect(i+n,n+(i+2)%n)
    counts=[0]*(2*n+1)
    for s in range(1<<(2*n)):
        active=s;independent=True
        while active:
            a=(active&-active).bit_length()-1
            active&=active-1
            if neighbors[a]&s:independent=False;break
        if independent and all(((s>>a)&1) or (neighbors[a]&s) for a in range(2*n)):
            counts[s.bit_count()]+=1
    return counts
for n in range(5,9):
    b=brute(n)
    assert b[:n+1]==tr[n] and all(x==0 for x in b[n+1:]),(n,b,tr[n])

print('VERIFY_OK transfer_states=81 core_states=27 core_edges=47 determinant_degree_t=10 exact_newton_orders=1..27 recurrence_orders=28..70 extremal_formulas=5..70 brute_orders=5..8 all_checks=passed')
