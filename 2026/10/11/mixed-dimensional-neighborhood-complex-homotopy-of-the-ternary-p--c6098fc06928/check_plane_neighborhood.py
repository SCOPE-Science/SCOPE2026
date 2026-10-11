#!/usr/bin/env python3
"""Standalone exact certificate for the point/line nonincidence neighborhood complex of PG(2,3).
Requires only Python 3 standard library. Execution: python check_plane_neighborhood.py
"""
from itertools import product
from collections import Counter, defaultdict, deque
from functools import lru_cache

Q=3
P=[]
for xyz in product(range(Q), repeat=3):
    if not any(xyz):continue
    first=next(c for c in xyz if c)
    norm=tuple((t*pow(first,-1,Q))%Q for t in xyz)
    if norm not in P:P.append(norm)
P.sort()
assert len(P)==13
LINES=[frozenset(j for j,p in enumerate(P) if sum(a*b for a,b in zip(u,p))%Q==0) for u in P]
assert len(set(LINES))==13 and all(len(line)==4 for line in LINES)
assert all(sum(j in L for L in LINES)==4 for j in range(13))
assert all(sum({a,b}<=L for L in LINES)==1 for a in range(13) for b in range(a+1,13))

F={0}
for line in LINES:
    mask=sum(1<<k for k in range(13) if k not in line)
    sub=mask
    while sub:
        F.add(sub)
        sub=(sub-1)&mask
assert len(F)==3862
fvector=tuple(sum(z.bit_count()==k+1 for z in F) for k in range(9))
assert fvector==(13,78,286,702,1170,1014,468,117,13),fvector

# Repeated vertex toggles: every matching pair differs by the smallest currently
# available pivot vertex. One legal face cannot enter two pairs.
remaining=set(F)
pairs=[]
for pivot in range(13):
    for s in sorted(tuple(remaining),key=lambda x:(x.bit_count(),x)):
        t=s|(1<<pivot)
        if s in remaining and t!=s and t in remaining:
            pairs.append((s,t))
            remaining.remove(s)
            remaining.remove(t)
# Delete the auxiliary empty face and its pair: the corresponding singleton
# is the unique critical 0-cell in the ordinary (unaugmented) complex.
empty_pair=next((s,t) for s,t in pairs if s==0)
base=empty_pair[1]
pairs.remove(empty_pair)
F.remove(0)
remaining.add(base)
assert len(pairs)==1910 and len(remaining)==41
critical=Counter(s.bit_count()-1 for s in remaining)
assert critical=={0:1,4:39,5:1},critical

# Enumerate the entire directed nonempty-face Hasse diagram; reverse exactly
# the paired incidence edges. Topological sorting proves full acyclicity.
paired=set(pairs)
deg={s:0 for s in F}
out=defaultdict(list)
incidences=0
for t in F:
    for i in range(t.bit_length()):
        if not ((t>>i)&1):continue
        s=t^(1<<i)
        if not s:continue
        u,v=(s,t) if (s,t) in paired else (t,s)
        out[u].append(v)
        deg[v]+=1
        incidences+=1
queue=deque(s for s in F if deg[s]==0)
order=[]
while queue:
    s=queue.popleft(); order.append(s)
    for t in out[s]:
        deg[t]-=1
        if deg[t]==0:queue.append(t)
assert len(order)==len(F)
assert incidences==sum((i+1)*fvector[i] for i in range(1,9))

lower=dict(pairs)
upper={t:s for s,t in pairs}
C4=sorted(s for s in remaining if s.bit_count()==5)
C5=sorted(s for s in remaining if s.bit_count()==6)
index={s:i for i,s in enumerate(C4)}
@lru_cache(None)
def projection(s):
    assert s.bit_count()==5
    if s in index:return {index[s]:1}
    if s in upper:return {}
    assert s in lower
    t=lower[s]
    assert t.bit_count()==6
    bits=[i for i in range(13) if t>>i&1]
    idx=bits.index((t^s).bit_length()-1)
    coeff=(-1)**idx
    acc=defaultdict(int)
    for pos,b in enumerate(bits):
        if pos==idx:continue
        child=t^(1<<b)
        for k,v in projection(child).items():acc[k]-=coeff*((-1)**pos)*v
    return {k:v for k,v in acc.items() if v}
assert len(C5)==1
boundary=defaultdict(int)
for j,b in enumerate(i for i in range(13) if C5[0]>>i&1):
    for k,v in projection(C5[0]^(1<<b)).items():boundary[k]+=(-1)**j*v
assert [boundary[k] for k in range(39)]==[0]*39,dict(boundary)
print('PASS: PG(2,3), faces=3861 nonempty, fvector=',fvector)
print('PASS: pairs=1910, critical=1 vertex + 39 four-cells + 1 five-cell, acyclic directed incidences=',incidences)
print('PASS: entire integer Morse boundary from C5 to C4 is zero, 39 entries')
print('PASS: topological consequence is wedge of 39 S4 and one S5 (per component).')
