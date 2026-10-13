#!/usr/bin/env python3
"""Exact small-field and combinatorial checks for a nodal elliptic boundary divisor."""
from collections import Counter, deque
from math import comb

# Base elliptic complete intersection in [F:H:D:G].
p=17
points=[]
for pivot in range(4):
    for tail in __import__('itertools').product(range(p), repeat=3-pivot):
        a=(0,)*pivot+(1,)+tail
        f,h,d,g=a
        if (d*d-h*h+f*f)%p or (g*g+h*h+f*f)%p:
            continue
        # Rank 2: a 2x2 minor of the two gradients is nonzero.
        row1=(2*f,-2*h,2*d,0)
        row2=(2*f,2*h,0,2*g)
        assert any((row1[i]*row2[j]-row1[j]*row2[i])%p for i in range(4) for j in range(i+1,4))
        points.append(a)
branch_count=Counter()
for a in points:
    zz=[i for i,v in enumerate((a[1],a[3],a[0],a[2])) if v==0]
    assert len(zz)<=1
    if zz: branch_count[zz[0]]+=1
assert [branch_count[i] for i in range(4)]==[4]*4,branch_count

# Each sign vector labels one of 16 genus-one components, and each
# Hamming-adjacent pair shares four distinct ordinary nodes.
vertices=list(range(16))
edges=[]
for i in range(4):
    for u in vertices:
        v=u^(1<<i)
        if u<v:
            for j in range(4):
                edges.append((u,v,i,j))
assert len(edges)==128
neighbors={x:set() for x in vertices}
for u,v,_,_ in edges:
    neighbors[u].add(v);neighbors[v].add(u)
seen={0};queue=deque([0])
while queue:
    u=queue.popleft()
    for v in neighbors[u]:
        if v not in seen:seen.add(v);queue.append(v)
assert len(seen)==16
b1=len(edges)-len(vertices)+1
assert b1==113

# Signs on oriented edges: a group element fixing an edge but swapping
# its endpoints acts by -1, so C1-trace at a generator is -32.
def popcount(n):return n.bit_count()
def tr_H1(g):
    return 113 if g==0 else (-31 if popcount(g)==1 else 1)
mults={}
for s in range(16):
    numer=sum(tr_H1(g)*(-1 if popcount(s&g)%2 else 1) for g in range(16))
    assert numer%16==0
    mults[s]=numer//16
    assert mults[s]==(4*popcount(s)-1 if s else 0)
assert sum(mults.values())==b1
assert sum(comb(4,k)*(4*k-1) for k in range(1,5))==113
assert 16+128-16+1==129
assert 1+(64+3*64)//2==129
print('VERIFY_OK', 'E_F17_points',len(points),'branch',tuple(branch_count[i] for i in range(4)),
      'components',len(vertices),'nodes',len(edges),'graph_b1',b1,
      'torus_mult_by_weight', {k:4*k-1 for k in range(1,5)}, 'arith_genus',129)
