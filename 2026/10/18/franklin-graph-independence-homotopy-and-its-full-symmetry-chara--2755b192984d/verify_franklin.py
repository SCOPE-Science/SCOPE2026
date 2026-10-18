"""Exact combinatorial certificate for the Franklin independence complex."""
from collections import Counter, deque
from itertools import combinations

N=12
OFFSETS=(5,-5)
EDGES=set()
for i in range(N):
    EDGES.add(tuple(sorted((i,(i+1)%N))))
    EDGES.add(tuple(sorted((i,(i+OFFSETS[i%2])%N))))
assert len(EDGES)==18
ADJ=[set() for _ in range(N)]
for a,b in EDGES:
    ADJ[a].add(b);ADJ[b].add(a)
assert all(len(z)==3 for z in ADJ)
FACES=sorted(m for m in range(1,1<<N)
             if all(not (m>>a&1 and m>>b&1) for a,b in EDGES))
FACESET=set(FACES)
FVECTOR=Counter(m.bit_count()-1 for m in FACES)
assert [FVECTOR[d] for d in range(6)]==[12,48,76,45,12,2]
assert len(FACES)==195

# An explicit elementary-collapse / critical-facet sequence.
UP={m:[] for m in FACES}
DOWN={m:[] for m in FACES}
for high in FACES:
    for i in range(N):
        if high>>i&1:
            low=high^(1<<i)
            if low:
                UP[low].append(high)
                DOWN[high].append(low)
remaining=set(FACES)
upcount={m:len(UP[m]) for m in FACES}
PAIRS=[]
CRITICAL=[]
while remaining:
    free=[m for m in remaining if upcount[m]==1]
    if free:
        top_dim=max(m.bit_count() for m in free)
        low=min(m for m in free if m.bit_count()==top_dim)
        high=next(x for x in UP[low] if x in remaining)
        assert high.bit_count()==low.bit_count()+1
        removed=(low,high)
        PAIRS.append((low,high))
    else:
        facets=[m for m in remaining if upcount[m]==0]
        assert facets
        top_dim=max(m.bit_count() for m in facets)
        critical=min(m for m in facets if m.bit_count()==top_dim)
        CRITICAL.append(critical)
        removed=(critical,)
    for face in removed:
        remaining.remove(face)
    for face in removed:
        for subface in DOWN[face]:
            if subface in remaining:
                upcount[subface]-=1
assert len(PAIRS)==95
assert Counter(m.bit_count()-1 for m in CRITICAL)=={0:1,2:4}
assert CRITICAL==[328,577,578,1168,2048]

# Independently verify acyclicity in the reversed-matched Hasse diagram.
matched=set(PAIRS)
out={m:[] for m in FACES}
indeg={m:0 for m in FACES}
for high in FACES:
    for low in DOWN[high]:
        u,v=(low,high) if (low,high) in matched else (high,low)
        out[u].append(v)
        indeg[v]+=1
q=deque(x for x in FACES if indeg[x]==0)
visited=0
while q:
    u=q.popleft();visited+=1
    for v in out[u]:
        indeg[v]-=1
        if indeg[v]==0:q.append(v)
assert visited==len(FACES)

# Exhaustive graph-automorphism enumeration by all adjacency-preserving bijections.
def automorphisms():
    mapping={}
    used=set()
    def visit():
        if len(mapping)==N:
            yield tuple(mapping[i] for i in range(N))
            return
        left=[v for v in range(N) if v not in mapping]
        vertex=min(left,key=lambda v:(-len(ADJ[v]&mapping.keys()),v))
        for image in range(N):
            if image in used:continue
            if any((v in ADJ[vertex]) != (mapping[v] in ADJ[image]) for v in mapping):
                continue
            mapping[vertex]=image
            used.add(image)
            yield from visit()
            used.remove(image)
            del mapping[vertex]
    return list(visit())
AUT=automorphisms()
assert len(AUT)==48 and len(set(AUT))==48
IDENTITY=tuple(range(N))
CENTER=tuple((i+6)%N for i in range(N))
def compose(a,b):return tuple(a[b[i]] for i in range(N))
assert IDENTITY in AUT and CENTER in AUT
assert all(compose(CENTER,g)==compose(g,CENTER) for g in AUT)
assert {g for g in AUT if all(compose(g,h)==compose(h,g) for h in AUT)}=={IDENTITY,CENTER}

def permutation_order(g):
    h=IDENTITY
    for j in range(1,49):
        h=compose(h,g)
        if h==IDENTITY:return j
    raise AssertionError('order must divide 48')

def trace_on_h2(g):
    alternating_sum=0
    for m in [0]+FACES:
        active=[i for i in range(N) if m>>i&1]
        if sum(1<<g[i] for i in active)!=m:continue
        permuted=[g[i] for i in active]
        inversions=sum(permuted[i]>permuted[j]
                       for i in range(len(permuted)) for j in range(i+1,len(permuted)))
        alternating_sum+=(-1)**(len(active)+inversions)
    return -alternating_sum

CHI={g:trace_on_h2(g) for g in AUT}
assert CHI[IDENTITY]==4 and CHI[CENTER]==-2
assert Counter((permutation_order(g),CHI[g]) for g in AUT)==Counter({
    (1,4):1, (2,-2):1, (2,0):9, (2,2):9,
    (3,1):8, (4,0):6, (4,2):6, (6,1):8})
assert sum(CHI.values())==48
assert sum(t*t for t in CHI.values())==96
assert sum((t-1)**2 for t in CHI.values())==48

# Independent cellular boundary ranks over two finite fields.
def boundary_rank(dim,p):
    cols=[m for m in FACES if m.bit_count()==dim+1]
    rows=[m for m in FACES if m.bit_count()==dim]
    idx={m:i for i,m in enumerate(rows)}
    vectors=[]
    for face in cols:
        v={}
        active=[i for i in range(N) if face>>i&1]
        for k,i in enumerate(active):
            r=idx[face^(1<<i)]
            v[r]=1 if k%2==0 else p-1
        vectors.append(v)
    pivots={}
    for col in vectors:
        while col:
            i=min(col)
            if i not in pivots:
                inv=pow(col[i],-1,p)
                pivots[i]={r:(x*inv)%p for r,x in col.items() if x%p}
                break
            fac=col[i]
            for r,v in pivots[i].items():
                w=(col.get(r,0)-fac*v)%p
                if w:col[r]=w
                else:col.pop(r,None)
    return len(pivots)
for prime in (2,1009):
    assert [boundary_rank(d,prime) for d in range(1,6)]==[11,37,35,10,2]

print('Franklin LCF [5,-5]^6: 12 vertices, 18 edges')
print('nonempty f-vector:',tuple(FVECTOR[i] for i in range(6)))
print('Morse pairs:',len(PAIRS),'critical masks:',CRITICAL,'acyclic nodes:',visited)
print('full automorphism group:',len(AUT),'center:',CENTER)
print('order/trace counts:',sorted(Counter((permutation_order(g),CHI[g]) for g in AUT).items()))
print('invariant dimension: 1; character squared norm: 2; residual irreducible dimension: 3')
print('boundary ranks (degrees 1..5):',(11,37,35,10,2),'moduli: 2, 1009')
print('PASS')
