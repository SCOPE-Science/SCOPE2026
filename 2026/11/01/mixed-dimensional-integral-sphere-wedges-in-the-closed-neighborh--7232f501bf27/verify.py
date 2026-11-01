"""Exact homotopy checker for the radius-one graph Cech complex of J(6,3).
Requires Python 3.10+ and sympy (for final integer Smith invariants).
"""
from itertools import combinations
from collections import Counter, deque
from functools import lru_cache
import random
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

V = tuple(map(frozenset,combinations(range(6),3)))
N = []
for s in V:
    nbr = sum(1 << i for i,t in enumerate(V) if len(s & t) >= 2)
    assert nbr.bit_count() == 10
    N.append(nbr)
assert len(set(N))==20  # 20 distinct maximal closed-neighborhood facets
faces={0}
for nbr in N:
    bits=[i for i in range(20) if nbr & (1<<i)]
    for s in range(1<<10):
        faces.add(sum(1<<bits[j] for j in range(10) if s & (1<<j)))
assert Counter(f.bit_count()-1 for f in faces) == {-1:1,0:20,1:180,2:960,3:2850,4:4500,5:4110,6:2400,7:900,8:200,9:20}

# First perform all available elementary simplicial collapses, in deterministic order.
up={f:set() for f in faces if f}
for f in up:
    if f.bit_count()<10:
        for bit in range(20):
            g=f | 1<<bit
            if g!=f and g in faces: up[f].add(g)
q=deque(sorted((f for f in up if len(up[f])==1),key=lambda f:(-f.bit_count(),f)))
active=set(faces)
pairs=[]
while q:
    f=q.popleft()
    if f not in active or len(up[f])!=1: continue
    g=next(iter(up[f]))
    assert g in active and g.bit_count()==f.bit_count()+1
    active.remove(f);active.remove(g)
    pairs.append((f,g))
    for u in (f,g):
        for bit in range(20):
            h=u & ~(1<<bit)
            if h and h in active:
                up[h].discard(u)
                if len(up[h])==1:q.append(h)
assert len(pairs)==6814
assert Counter(f.bit_count()-1 for f in active)=={-1:1,0:20,1:180,2:684,3:1066,4:562}

# Independent mod-two cellular boundary check on the collapsed simplicial core.
mod2ranks = []
bydim = {d:sorted(f for f in active if f.bit_count()==d+1) for d in range(5)}
for d in range(1,5):
    low_idx = {f:i for i,f in enumerate(bydim[d-1])}
    basis = {}
    for g in bydim[d]:
        col = 0
        for j in range(20):
            h = g & ~(1<<j)
            if h != g:
                assert h in low_idx
                col ^= (1 << low_idx[h])
        while col:
            pivot = col.bit_length()-1
            if pivot in basis:
                col ^= basis[pivot]
            else:
                basis[pivot] = col
                break
    mod2ranks.append(len(basis))
assert mod2ranks == [19,161,523,532],mod2ranks
assert bydim[3].__len__() - mod2ranks[2] - mod2ranks[3] == 11
assert bydim[4].__len__() - mod2ranks[3] == 30
print('MOD2_OK ranks',mod2ranks,'betti3=11 betti4=30',flush=True)

# Coordinate-toggle Morse matching of the uncollapsed core.
order=list(range(20)); random.Random(220).shuffle(order)
for bit in order:
    lower=sorted((f for f in active if f and not(f & (1<<bit)) and (f|(1<<bit)) in active),key=lambda f:(-f.bit_count(),f))
    for f in lower:
        g=f|(1<<bit)
        if f in active and g in active:
            active.remove(f);active.remove(g);pairs.append((f,g))
assert Counter(f.bit_count()-1 for f in active)=={-1:1,0:1,3:13,4:32},Counter(f.bit_count()-1 for f in active)
print('FACES_OK',dict(sorted(Counter(f.bit_count()-1 for f in faces).items())),flush=True)
print('MATCHING_OK',len(pairs),'critical',dict(sorted(Counter(f.bit_count()-1 for f in active).items())),flush=True)

low_to_high={f:g for f,g in pairs}
high_to_low={g:f for f,g in pairs}
assert len(low_to_high)==len(high_to_low)==len(pairs)
assert all(f.bit_count()>0 for f,g in pairs)

# Verify complete directed Hasse graph: reversed matched arrows, other arrows descending.
indegree={f:0 for f in faces if f}
out={f:[] for f in indegree}
incidence_count=0
for g in indegree:
    for bit in range(20):
        f=g & ~(1<<bit)
        if f!=g and f:
            incidence_count+=1
            if low_to_high.get(f)==g:
                out[f].append(g);indegree[g]+=1
            else:
                out[g].append(f);indegree[f]+=1
start=deque(f for f in indegree if indegree[f]==0)
count=0
while start:
    f=start.popleft(); count+=1
    for g in out[f]:
        indegree[g]-=1
        if indegree[g]==0:start.append(g)
assert count==len(indegree),('Cyclic matching',count,len(indegree))
print('ACYCLIC_OK',count,incidence_count,flush=True)

@lru_cache(maxsize=None)
def bdry(g):
    """Signed codimension-one facets (never the empty face)."""
    bits=[i for i in range(20) if g & (1<<i)]
    return [(g^(1<<bit),(-1)**j) for j,bit in enumerate(bits) if g.bit_count()>1]

@lru_cache(maxsize=None)
def reduce_3(f):
    """Exact Morse projection of a degree-three chain to critical degree-three cells."""
    if f in active:
        return {f:1}
    if f in high_to_low:
        return {}
    g=low_to_high[f]
    facets=bdry(g)
    a=next(c for h,c in facets if h==f)
    out={}
    for h,c in facets:
        if h==f:continue
        for x,v in reduce_3(h).items():
            out[x]=out.get(x,0)-a*c*v
    return {x:v for x,v in out.items() if v}

C3=sorted(f for f in active if f.bit_count()==4)
C4=sorted(f for f in active if f.bit_count()==5)
M=Matrix(13,32,lambda a,b:sum(c*reduce_3(f).get(C3[a],0) for f,c in bdry(C4[b])))
D=smith_normal_form(M,domain=ZZ)
diag=[abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i]!=0]
assert diag==[1,1], diag
print('SMITH_OK',diag,'matrix_shape',M.shape,'nonzero_entries',len([(i,j) for i in range(13) for j in range(32) if M[i,j]]),flush=True)
print('HOMOTOPY_OK wedge_11_S3_plus_30_S4')
print('ALL_VERIFY_OK')
