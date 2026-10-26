#!/usr/bin/env python3
"""Exact finite-state certificate for edge open packings in cyclic prisms."""
from collections import Counter

PATTERNS = (0, 1, 2, 4, 5, 6)  # empty, upper, lower, rung, upper+rung, lower+rung

def forbidden1(a, b):
    return bool((a & 4 and b) or (a & 1 and b & 2) or (a & 2 and b & 1))

def forbidden2(a, b):
    return bool((a & 1 and b & 5) or (a & 2 and b & 6))

def prism_edges(n):
    top = [(i, (i+1)%n) for i in range(n)]
    bottom = [(n+i, n+(i+1)%n) for i in range(n)]
    rung = [(i, n+i) for i in range(n)]
    return top + bottom + rung

def pair_conflicts(edge1, edge2, edges):
    e, f = set(edge1), set(edge2)
    return any(g != edge1 and g != edge2 and
               ((g[0] in e and g[1] in f) or
                (g[0] in f and g[1] in e))
               for g in edges)

def direct_masks(n):
    edges = prism_edges(n)
    conflicts = [0]*len(edges)
    for i in range(len(edges)):
        for j in range(i+1,len(edges)):
            if pair_conflicts(edges[i],edges[j],edges):
                conflicts[i] |= 1<<j
                conflicts[j] |= 1<<i
    return conflicts

def validate_local_rules(n):
    assert n>=7
    conflicts = direct_masks(n)
    # Single-edge forbidden pairs exactly as the claimed radius-two local table.
    for i in range(3*n):
        for j in range(i+1,3*n):
            type_i,col_i = i//n, i%n
            type_j,col_j = j//n, j%n
            bit_i, bit_j = 1<<type_i, 1<<type_j
            delta=(col_j-col_i)%n
            if delta==0: pred={type_i,type_j}=={0,1}
            elif delta==1: pred=forbidden1(bit_i,bit_j)
            elif delta==n-1:pred=forbidden1(bit_j,bit_i)
            elif delta==2:pred=forbidden2(bit_i,bit_j)
            elif delta==n-2:pred=forbidden2(bit_j,bit_i)
            else:pred=False
            assert pred==bool(conflicts[i]>>j & 1),(n,i,j,pred)
    return conflicts

STATES = tuple((a,b) for a in PATTERNS for b in PATTERNS if not forbidden1(a,b))
STATE_INDEX={s:i for i,s in enumerate(STATES)}
POTENTIAL={ (0,5), (0,6), (1,5), (2,6) }
H=[-int(s in POTENTIAL) for s in STATES]
EDGES=[]
B0=[[0]*len(STATES) for _ in STATES]
B1=[[0]*len(STATES) for _ in STATES]
for i,(a,b) in enumerate(STATES):
    for c in PATTERNS:
        if forbidden1(b,c) or forbidden2(a,c):continue
        j=STATE_INDEX[(b,c)]
        raw=1-c.bit_count()
        adjusted=raw+H[i]-H[j]
        assert adjusted in (0,1)
        EDGES.append((i,j,adjusted))
        (B0 if adjusted==0 else B1)[i][j]+=1

def multiply(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    if B[k][j]:C[i][j]+=A[i][k]*B[k][j]
    return C

def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def trace(A):return sum(A[i][i] for i in range(len(A)))

assert len(STATES)==17 and len(EDGES)==37
assert sum(sum(row) for row in B0)==24 and sum(sum(row) for row in B1)==13
I=eye(len(STATES))
powers=[I]
for _ in range(8):powers.append(multiply(powers[-1],B0))
assert powers[8]==powers[2]  # Exact integer-matrix identity: all higher powers are six-periodic.
# The zero-cost digraph has exactly one directed cycle, of length six.
def enumerate_simple_cycles(A):
    adj=[[j for j,x in enumerate(row) if x] for row in A]
    found=set()
    def walk(start,cur,path,seen):
        for nxt in adj[cur]:
            if nxt==start:
                cyc=tuple(path)
                rotations=[cyc[i:]+cyc[:i] for i in range(len(cyc))]
                found.add(min(rotations))
            elif nxt>start and nxt not in seen:
                walk(start,nxt,path+(nxt,),seen|{nxt})
    for start in range(len(A)):
        walk(start,start,(start,),{start})
    return found
cycles=enumerate_simple_cycles(B0)
assert len(cycles)==1 and len(next(iter(cycles)))==6
assert [trace(multiply(B1,powers[n-1])) for n in range(1,9)]==[1,1,4,2,4,6,2,2]

def theoretical(n):
    if n%6==0:return n,6
    return n-1,(4*n if n%6 in (3,5) else 2*n)

def transfer_max_count(n):
    """Independent weighted cyclic-state dynamic program, no matrix reweighting."""
    best=-1;total=0
    for first in range(len(STATES)):
        curr={first:(0,1)}
        for step in range(n):
            nxt={}
            for i,(v,ways) in curr.items():
                for j,cost in [(j,c) for ii,j,c in EDGES if ii==i]:
                    gain=STATES[j][1].bit_count()
                    x=v+gain
                    if j not in nxt or x>nxt[j][0]:nxt[j]=(x,ways)
                    elif x==nxt[j][0]:nxt[j]=(x,nxt[j][1]+ways)
            curr=nxt
        if first in curr:
            v,w=curr[first]
            if v>best:best,total=v,w
            elif v==best:total+=w
    return best,total

def direct_max_count(conflicts):
    """Independent enumeration of every feasible set, from original third-edge condition."""
    n=len(conflicts)
    best=0;count=0;explored=0
    # Monotone sequential recursion enumerates all feasible sets exactly once.
    def rec(i, chosen, size):
        nonlocal best,count,explored
        if i==n:
            explored+=1
            if size>best:best,count=size,1
            elif size==best:count+=1
            return
        rec(i+1,chosen,size)
        if not (conflicts[i]&chosen):rec(i+1,chosen|(1<<i),size+1)
    rec(0,0,0)
    return best,count,explored

for n in range(7,15):validate_local_rules(n)
for n in range(7,12):
    actual=direct_max_count(direct_masks(n))
    assert actual[:2]==theoretical(n)==transfer_max_count(n),(n,actual)
    print('DIRECT',n,'maximum',actual[0],'optimal_sets',actual[1],'feasible_sets',actual[2])
for n in range(12,85):
    assert transfer_max_count(n)==theoretical(n),n
print('CERTIFICATE_OK states=17 transitions=37 zero=24 unit=13 B0^8=B0^2 unique_zero_cycle=6')
print('TRACES a[1..8]=1,1,4,2,4,6,2,2; transfer_orders=7..84; local_rules=7..14')
