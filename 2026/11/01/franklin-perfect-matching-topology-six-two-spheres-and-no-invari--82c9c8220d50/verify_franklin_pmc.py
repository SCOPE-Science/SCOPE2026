"""Self-contained exact finite certificates for the Franklin perfect-matching complex.
Requires standard Python 3 only. Run: python3 verify_franklin_pmc.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import random

N=12
E=tuple(sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)}|
               {tuple(sorted((i,(i+(5 if i%2==0 else -5))%N))) for i in range(N)}))
assert len(E)==18
adj=[[] for _ in range(N)]
for j,(a,b) in enumerate(E):
    adj[a].append((b,j));adj[b].append((a,j))
assert set(len(x) for x in adj)=={3}

@lru_cache(None)
def perfect(rem):
    if not rem:return (0,)
    a=(rem&-rem).bit_length()-1
    return tuple((rest | 1<<j) for b,j in adj[a] if rem>>b&1
                 for rest in perfect(rem^(1<<a)^(1<<b)))
P=tuple(sorted(perfect((1<<N)-1)))
assert len(P)==len(set(P))==17
assert all(x.bit_count()==6 for x in P)

F={0}
for facet in P:
    x=facet
    while x:
        F.add(x); x=(x-1)&facet
assert len(F)==762
assert tuple(Counter(x.bit_count() for x in F)[k] for k in range(7))==(1,18,117,264,243,102,17)
# Independent exhaustive edge-subset test: every full-cover matching is one of P.
P2=[]
for x in range(1<<len(E)):
    covered=0;valid=True
    for j,(a,b) in enumerate(E):
        if x>>j&1:
            pair=(1<<a)|(1<<b)
            if covered&pair:valid=False;break
            covered|=pair
    if valid and covered==(1<<N)-1:P2.append(x)
assert tuple(P2)==P

# Deterministic sequence of genuine elementary simplicial collapses.
active=set(F-{0});collapse=[]
while True:
    cofaces=defaultdict(list)
    for hi in active:
        for j in range(hi.bit_length()):
            if hi>>j&1:
                lo=hi^(1<<j)
                if lo and lo in active:cofaces[lo].append(hi)
    options=((lo,ls[0]) for lo,ls in cofaces.items() if len(ls)==1)
    chosen=min(options,key=lambda p:(-p[0].bit_count(),p[0]), default=None)
    if chosen is None:break
    lo,hi=chosen
    # Check that hi is the unique coface of lo among all cells still active:
    assert cofaces[lo]==[hi]
    assert not any((z != hi and z & hi == hi) for z in active)
    active.remove(lo);active.remove(hi);collapse.append(chosen)
assert len(collapse)==321
assert Counter(x.bit_count()-1 for x in active)==Counter({0:17,1:56,2:46})

# A second (coreduction) matching on the actual residual subcomplex.
# At each step, pair a cell with its only remaining boundary, or choose a
# critical cell of lowest available dimension. The fixed seed makes the
# entire matching reproducible.
remaining=set(active);rng=random.Random(0);more=[];critical=[]
while remaining:
    options=[]
    for hi in sorted(remaining):
        bd=[hi^(1<<j) for j in range(hi.bit_length())
            if hi>>j&1 and (hi^(1<<j)) in remaining]
        if len(bd)==1:options.append((hi,bd[0]))
    if options:
        d=min(x.bit_count() for x,y in options)
        hi,lo=rng.choice(sorted(x for x in options if x[0].bit_count()==d))
        remaining.remove(lo);remaining.remove(hi);more.append((lo,hi))
    else:
        d=min(x.bit_count() for x in remaining)
        cell=rng.choice(sorted(x for x in remaining if x.bit_count()==d))
        remaining.remove(cell);critical.append(cell)
M=collapse+more
assert len(more)==56 and len(M)==377
assert Counter(x.bit_count()-1 for x in critical)==Counter({0:1,2:6})
assert len({x for pair in M for x in pair})==2*len(M)
assert len(F-{0})==2*len(M)+len(critical)

# Full directed-Hasse verification (matched cover edges point upward;
# all other cover edges point downward).
up=set(M)
nodes=F-{0};succ={x:[] for x in nodes};indeg={x:0 for x in nodes}
incidences=0
for hi in nodes:
    for j in range(hi.bit_length()):
        if hi>>j&1:
            lo=hi^(1<<j)
            if lo not in nodes:continue
            a,b=(lo,hi) if (lo,hi) in up else (hi,lo)
            succ[a].append(b);indeg[b]+=1;incidences+=1
Q=deque(x for x in nodes if indeg[x]==0);seen=0
while Q:
    a=Q.popleft();seen+=1
    for b in succ[a]:
        indeg[b]-=1
        if indeg[b]==0:Q.append(b)
assert seen==len(nodes)

# All adjacency-preserving permutations, exhaustive injective backtracking.
S=[{b for b,j in adj[a]} for a in range(N)]
# BFS ordering of the vertices for strong pruning.
order=[0];observed={0}
for a in order:
    for b in sorted(S[a]):
        if b not in observed:observed.add(b);order.append(b)
assert len(order)==N
perms=[]
def visit(idx,m,used):
    if idx==N:
        perm=tuple(m[i] for i in range(N));perms.append(perm);return
    a=order[idx]
    for b in range(N):
        if used>>b&1:continue
        if all(((v in S[a])==(m[v] in S[b])) for v in m):
            m[a]=b;visit(idx+1,m,used|1<<b);del m[a]
visit(0,{},0)
assert len(perms)==48 and len(set(perms))==48
edge_index={e:j for j,e in enumerate(E)}

def image_edge_perm(perm):
    return tuple(edge_index[tuple(sorted((perm[a],perm[b])))] for a,b in E)

def sign_on_fixed_face(face,p):
    ids=[i for i in range(len(E)) if face>>i&1]
    dest=[p[i] for i in ids]
    if set(dest)!=set(ids):return 0
    return -1 if sum(dest[i]>dest[j] for i in range(len(dest)) for j in range(i+1,len(dest)))%2 else 1

traces=[];orbit_edges=[set() for _ in range(len(E))]
for perm in perms:
    ep=image_edge_perm(perm)
    assert sorted(ep)==list(range(len(E)))
    for j in range(len(E)):orbit_edges[j].add(ep[j])
    # simplicial alternating chain trace minus H_0=1 equals H_2 trace
    L=sum(((-1)**(x.bit_count()-1))*sign_on_fixed_face(x,ep) for x in nodes)
    traces.append(L-1)
assert traces[perms.index(tuple(range(N)))]==6
assert sum(traces)%48==0
invariants=sum(traces)//48
print('graph_vertices',N,'graph_edges',len(E),'perfect_matchings',len(P))
print('face_counts_by_size',[sum(x.bit_count()==k for x in F) for k in range(7)])
print('elementary_collapses',len(collapse),'coreduction_pairs',len(more))
print('critical_by_dimension',sorted(Counter(x.bit_count()-1 for x in critical).items()))
print('Hasse_incidences',incidences,'acyclicity','PASS')
print('automorphisms',len(perms),'edge_orbit_sizes',sorted(set(map(len,orbit_edges))))
print('H2_trace_distribution',sorted(Counter(traces).items()),'invariant_rank',invariants)
print('halfturn_trace',traces[perms.index(tuple((i+6)%N for i in range(N)))])
print('FRANKLIN_PMC_COMPLETE_ACYCLIC_MORSE_AND_CHARACTER_VERIFIED')
