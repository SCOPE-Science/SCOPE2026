#!/usr/bin/env python3
"""Finite exact certificate for distance-three domination of two-row strips.
No external packages required. Run: python3 support/verify.py
"""
from collections import deque
import json
from pathlib import Path
import sys

V = 4 ** 6
P = json.loads(Path(__file__).with_name('potential.json').read_text(encoding='utf-8'))
assert len(P) == V and all(isinstance(x, int) for x in P)
assert min(P) == -18 and max(P) == 0

# Each state encodes six successive columns, least significant digit first.
def digits(s):
    return [(s // 4**i) % 4 for i in range(6)]

def admissible(a, b):
    # Center is the fourth of the seven columns. Exact-distance-three
    # partners are at horizontal displacement +/-3 on the same row,
    # or +/-2 on the opposite row.
    return all(((a[3] >> r) & 1) or ((a[0] >> r) & 1)
               or ((b >> r) & 1) or ((a[1] >> (1-r)) & 1)
               or ((a[5] >> (1-r)) & 1) for r in (0, 1))

edges=[]
tight=[[] for _ in range(V)]
reverse=[[] for _ in range(V)]
for s in range(V):
    a=digits(s)
    for b in range(4):
        if not admissible(a,b):
            continue
        t=s//4+b*4**5
        w=a[3].bit_count()
        cost=7*w-3
        assert P[t]-P[s] <= cost, (s,t,w)
        edges.append((s,t,w))
        if P[t]-P[s] == cost:
            tight[s].append(t)
            reverse[t].append(s)
assert len(edges)==15376
assert sum(map(len,tight))==3583

# Independently identify ALL directed cyclic components of the tight graph.
sys.setrecursionlimit(30000)
seen=[False]*V
order=[]
def visit(v):
    seen[v]=True
    for w in tight[v]:
        if not seen[w]: visit(w)
    order.append(v)
for v in range(V):
    if not seen[v]: visit(v)
seen=[False]*V
components=[]
def visit_reverse(v, comp):
    seen[v]=True
    comp.append(v)
    for w in reverse[v]:
        if not seen[w]: visit_reverse(w,comp)
for v in reversed(order):
    if not seen[v]:
        comp=[]
        visit_reverse(v,comp)
        if len(comp)>1 or v in tight[v]:
            components.append(set(comp))
assert sorted(len(comp) for comp in components)==[7,7]
for comp in components:
    assert sum(v in comp for u in comp for v in tight[u])==7
    for u in comp:
        assert sum(v in comp for v in tight[u])==1
        assert sum(v==u for x in comp for v in tight[x])==1

# Verify the exact seven-column packing and its distinct 14 translates.
word=(0,0,1,0,0,2,2)
def covers(word):
    n=len(word)
    for i in range(n):
        for r in range(2):
            if not ( ((word[i]>>r)&1)
                or ((word[(i-3)%n]>>r)&1)
                or ((word[(i+3)%n]>>r)&1)
                or ((word[(i-2)%n]>>(1-r))&1)
                or ((word[(i+2)%n]>>(1-r))&1)):
                return False
    return True
assert sum(x.bit_count() for x in word)==3
assert covers(word)
def swap_rows(word):
    return tuple(((x&1)<<1)|((x&2)>>1) for x in word)
optimal_words={tuple(w[(i+j)%7] for j in range(7)) for w in (word,swap_rows(word)) for i in range(7)}
assert len(optimal_words)==14
assert all(covers(w) and sum(x.bit_count() for x in w)==3 for w in optimal_words)

# Independent original-graph distance check for the local formula.
def primal_neighborhoods(n):
    graph=[set() for _ in range(2*n)]
    for r in range(2):
        for i in range(n):
            v=r*n+i
            for z in [r*n+(i-1)%n,r*n+(i+1)%n,(1-r)*n+i]:
                graph[v].add(z)
    masks=[]
    for u in range(2*n):
        distance=[-1]*(2*n)
        distance[u]=0
        q=deque([u])
        while q:
            v=q.popleft()
            for z in graph[v]:
                if distance[z]<0:
                    distance[z]=distance[v]+1
                    q.append(z)
        mask=1<<u
        for v in range(2*n):
            if distance[v]==3:
                mask|=1<<v
        masks.append(mask)
    return masks

for n in range(7,11):
    N=primal_neighborhoods(n)
    for r in range(2):
        for i in range(n):
            mask=1<<(r*n+i)
            for s in (-3,3): mask|=1<<(r*n+(i+s)%n)
            for s in (-2,2): mask|=1<<((1-r)*n+(i+s)%n)
            assert mask==N[r*n+i]

# Completely separate brute-force check for the first three circumferences.
small=[]
for n in (7,8,9):
    N=primal_neighborhoods(n)
    best=2*n+1
    solutions=0
    for S in range(1<<(2*n)):
        m=S.bit_count()
        if m>best: continue
        if all(S & mask for mask in N):
            if m<best:
                best=m
                solutions=0
            solutions+=1
    assert best >= (3*n+6)//7
    if n==7: assert (best,solutions)==(3,14)
    small.append((n,best,solutions))
print('VERIFY_OK', 'states=',V, 'arcs=',len(edges),
      'tight_arcs=',sum(map(len,tight)),
      'cyclic_SCCs=',sorted(len(c) for c in components),
      'witnesses_per_period=',len(optimal_words),
      'primal_metric_n=7..10', 'bruteforce=',small)
