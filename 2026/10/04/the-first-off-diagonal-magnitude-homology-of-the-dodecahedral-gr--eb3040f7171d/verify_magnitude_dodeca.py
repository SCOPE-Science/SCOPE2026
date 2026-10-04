#!/usr/bin/env python3
from collections import deque, defaultdict

N=20
adj=[set() for _ in range(N)]
for i in range(10):
    for a,b in [(i,(i+1)%10),(i,10+i),(10+i,10+((i+2)%10))]:
        adj[a].add(b); adj[b].add(a)
assert sum(map(len,adj))==60 and all(len(x)==3 for x in adj)

D=[[99]*N for _ in range(N)]
for s in range(N):
    D[s][s]=0; q=deque([s])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if D[s][v]==99:
                D[s][v]=D[s][u]+1; q.append(v)
assert max(max(r) for r in D)==5
# G(10,2) is not geodetic: vertices 0 and 4 admit two shortest paths of length four.
def shortest_path_count(s,t):
    ds=[99]*N; cnt=[0]*N; ds[s]=0; cnt[s]=1; q=deque([s])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if ds[v]==99:
                ds[v]=ds[u]+1; cnt[v]=cnt[u]; q.append(v)
            elif ds[v]==ds[u]+1:
                cnt[v]+=cnt[u]
    return ds[t],cnt[t]
assert shortest_path_count(0,4)==(4,2)

def chains(k,l):
    out=[]
    def rec(t, rem):
        if len(t)==k+1:
            if rem==0: out.append(tuple(t))
            return
        u=t[-1]
        for v in range(N):
            if v==u: continue
            d=D[u][v]
            if d<=rem:
                rec(t+[v], rem-d)
    for s in range(N): rec([s],l)
    return out

def dp_count(k,l):
    state={(s,0):1 for s in range(N)}
    for _ in range(k):
        nxt=defaultdict(int)
        for (u,w),c in state.items():
            for v in range(N):
                if v!=u and w+D[u][v]<=l:
                    nxt[(v,w+D[u][v])]+=c
        state=nxt
    return sum(c for (v,w),c in state.items() if w==l)

C={k:chains(k,4) for k in (2,3,4)}
assert {k:len(C[k]) for k in C}=={2:1440,3:3240,4:1620}
assert all(len(C[k])==dp_count(k,4) for k in C)
idx={k:{x:i for i,x in enumerate(C[k])} for k in C}

def boundary_columns(k):
    cols=[]
    for x in C[k]:
        bits=0
        for i in range(1,k):
            if D[x[i-1]][x[i+1]]==D[x[i-1]][x[i]]+D[x[i]][x[i+1]]:
                y=x[:i]+x[i+1:]
                bits ^= 1 << idx[k-1][y]
        cols.append(bits)
    return cols

def rank_bits(cols):
    piv={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x; break
    return len(piv)

def rank_rows(cols,nrows):
    rows=[0]*nrows
    for j,c in enumerate(cols):
        while c:
            lb=c & -c; i=lb.bit_length()-1
            rows[i] |= 1<<j; c ^= lb
    return rank_bits(rows)

d3=boundary_columns(3); d4=boundary_columns(4)
# Verify d^2=0 by composing each d4 column through d3.
for c in d4:
    z=0; y=c
    while y:
        lb=y & -y; i=lb.bit_length()-1; z ^= d3[i]; y ^= lb
    assert z==0
r3=rank_bits(d3); r4=rank_bits(d4)
assert r3==rank_rows(d3,len(C[2]))
assert r4==rank_rows(d4,len(C[3]))
assert (r3,r4)==(1320,1560)
betti=len(C[3])-r3-r4
assert betti==360
print('graph_vertices=20 graph_edges=30 diameter=5 nongeodetic_witness_0_4=(distance4,paths2)')
print('chain_dimensions C_2,4=1440 C_3,4=3240 C_4,4=1620')
print('boundary_ranks_mod2 d3=1320 d4=1560')
print('MH_3,4_mod2_dimension=360')
print('VERIFY_OK')
