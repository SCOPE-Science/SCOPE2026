#!/usr/bin/env python3
"""Exact reproducibility check for optimal signed-double-Roman prism labelings.
Uses only Python's standard library and exact integer arithmetic.
"""
from itertools import product
from collections import Counter
from math import prod

LABELS=(-1,1,2,3)
COLS=tuple(product(LABELS,repeat=2))
N=len(COLS)

def original_vertex(value, neighbors):
    if value == -1 and not (3 in neighbors or neighbors.count(2)>=2):
        return False
    if value == 1 and not any(x>=2 for x in neighbors):
        return False
    return value+sum(neighbors)>=1

def original_local(a,b,c):
    return all(original_vertex(b[r],[a[r],c[r],b[1-r]]) for r in (0,1))

def tight_vertex(value,neighbors):
    positive=[x for x in neighbors if x != -1]
    if value == -1:
        return len(positive)==2 and sum(positive)==4
    return len(positive)==1 and (value!=1 or positive[0]>=2)

def tight_local(a,b,c):
    return all(tight_vertex(b[r],[a[r],c[r],b[1-r]]) for r in (0,1))

def discharge_four(value, neighbors):
    if value==-1:
        return -4+sum(2*x-1 for x in neighbors if x!=-1)
    return 4*value-(2*value-1)*neighbors.count(-1)

def tarjan(adj):
    # adjacency indexed by integer 0..255, with no multiedges
    time=[0];num={};low={};stack=[];on=set();components=[]
    def visit(v):
        num[v]=low[v]=time[0];time[0]+=1
        stack.append(v);on.add(v)
        for w in adj[v]:
            if w not in num:
                visit(w);low[v]=min(low[v],low[w])
            elif w in on: low[v]=min(low[v],num[w])
        if low[v]==num[v]:
            comp=[]
            while True:
                w=stack.pop();on.remove(w);comp.append(w)
                if w==v:break
            components.append(sorted(comp))
    for v in range(N*N):
        if v not in num:visit(v)
    return components

def mmul(a,b):
    n=len(a)
    # Exact dense matrix product, skipping zeros.
    c=[[0]*n for _ in range(n)]
    for i in range(n):
        for j,aj in enumerate(a[i]):
            if aj:
                for k,bjk in enumerate(b[j]):
                    if bjk:c[i][k]+=aj*bjk
    return c

def charpoly_integer(A):
    n=len(A);P=[[int(i==j) for j in range(n)] for i in range(n)]
    traces=[]; coeff=[1]
    for k in range(1,n+1):
        P=mmul(P,A)
        traces.append(sum(P[i][i] for i in range(n)))
        numerator=-sum(coeff[k-i]*traces[i-1] for i in range(1,k+1))
        assert numerator%k==0,(k,numerator)
        coeff.append(numerator//k)
    return coeff

def formula(m):
    assert m>=4 and m%2==0
    if m%4==2:return 2
    k=m//4
    a,b=2,7
    if k==0:return 14+4*a
    for _ in range(1,k):a,b=b,7*b-a
    return 14+4*b

def original_min_count(m,edges):
    # Exact min-cost-and-multiplicity DP, unconstrained labels, closing cycles.
    best=None;number=0
    outs=[[] for _ in range(N*N)]
    for v,w,c in edges:outs[v].append((w,c))
    for root in range(N*N):
        active={root:(0,1)}
        for _ in range(m):
            nxt={}
            for v,(d,multiplicity) in active.items():
                for w,c in outs[v]:
                    newcost=d+c
                    old=nxt.get(w)
                    if old is None or newcost<old[0]:nxt[w]=(newcost,multiplicity)
                    elif newcost==old[0]:nxt[w]=(newcost,old[1]+multiplicity)
            active=nxt
        if root in active:
            cost,multiplicity=active[root]
            if best is None or cost<best:best,number=cost,multiplicity
            elif cost==best:number+=multiplicity
    return best,number

def main():
    A=[[] for _ in range(N*N)]
    original_edges=[]
    triplecount=0
    for i,a in enumerate(COLS):
        for j,b in enumerate(COLS):
            for k,c in enumerate(COLS):
                nei=[[a[r],c[r],b[1-r]] for r in range(2)]
                direct=(original_local(a,b,c) and all(discharge_four(b[r],nei[r])==2 for r in range(2)))
                tight=tight_local(a,b,c)
                assert direct==tight,(a,b,c)
                if tight:
                    A[i*N+j].append(j*N+k)
                    triplecount+=1
                if original_local(a,b,c):original_edges.append((i*N+j,j*N+k,sum(b)))
    comps=tarjan(A)
    recurring=[]
    for comp in comps:
        s=set(comp)
        if len(comp)>1 or comp[0] in A[comp[0]]:recurring.append(comp)
    recurring.sort(key=lambda c:-len(c))
    sizes=[len(x) for x in recurring]
    assert sizes==[22,4,4,4,2],sizes
    assert triplecount==81,triplecount
    core=recurring[0];lookup={v:i for i,v in enumerate(core)}
    matrix=[[0]*len(core) for _ in core]
    for v in core:
        for w in A[v]:
            if w in lookup:matrix[lookup[v]][lookup[w]]=1
    assert sum(map(sum,matrix))==32
    coeff=charpoly_integer(matrix)
    expected=[1]+[0]*21+[0]
    expected[4]=-7;expected[8]=1
    assert coeff==expected,(coeff,expected)
    for comp in recurring[1:]:
        # Each remaining recurring component is one isolated directed cycle.
        s=set(comp)
        assert all(len([w for w in A[v] if w in s])==1 for v in comp)
    assert len(original_edges)==3230,len(original_edges)
    for n in (4,6,8):
        minimum,count=original_min_count(n,original_edges)
        assert minimum==n and count==formula(n),(n,minimum,count,formula(n))
    for n in (4,6,8,10,12,16,20,24,28,32,36,40):
        # Closed-walk trace in each recurrent component, exact integer DP.
        total=0
        for comp in recurring:
            s=set(comp)
            for root in comp:
                active={root:1}
                for _ in range(n):
                    nxt={}
                    for v,times in active.items():
                        for w in A[v]:
                            if w in s:nxt[w]=nxt.get(w,0)+times
                    active=nxt
                total+=active.get(root,0)
        assert total==formula(n),(n,total,formula(n))
    # Independent straightforward enumeration on four-column prisms.
    brute=0
    for choice in product(range(N),repeat=4):
        arr=[COLS[i] for i in choice]
        if all(original_local(arr[(i-1)%4],arr[i],arr[(i+1)%4]) for i in range(4)) and sum(map(sum,arr))==4:
            brute+=1
    assert brute==42,brute
    print('CERTIFICATE_OK labels=4 columns=16 pair_states=256 tight_edges=81 original_edges=3230')
    print('SCC_OK nontrivial_sizes=22,4,4,4,2 core_edges=32 core_charpoly=t^14*(t^8-7*t^4+1)')
    print('MINIMUM_DP_OK m=4,6,8 counts=42,2,202')
    print('TRACE_OK even_orders=4,6,8,10,12,16,20,24,28,32,36,40')
    print('BRUTE_OK m=4 count=42')

if __name__=='__main__':main()
