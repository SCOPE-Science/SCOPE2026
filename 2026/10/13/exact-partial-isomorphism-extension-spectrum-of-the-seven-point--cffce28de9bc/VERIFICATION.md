---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem is finite and was replayed by exhaustive exact enumeration. The checker uses only Python's standard library. It verifies that the fourteen listed edges are invariant under all 42 affine maps, checks every one of the \(7!=5040\) vertex permutations and recovers no additional automorphisms, then exhausts every bijection between equal-size vertex subsets and tests both induced-hypergraph isomorphism and extendibility to a recovered global automorphism.

Expected terminal summary:

```text
AUT 42
TOTAL_PARTIAL_ISOMORPHISMS 8912
TOTAL_EXTENDIBLE 5090
VERIFY_OK 154786 exact assertions
```

The complete replay script is included below so that the calculation is reproducible from the public edge list alone.

```python
from itertools import combinations, permutations
from collections import defaultdict

V=tuple(range(7))
E={tuple(sorted(map(int,s))) for s in [
    '013','026','023','045','015','046','124','235','346','156','134','245','356','126'
]}
A=0

def check(cond, msg='assertion failed'):
    global A
    A += 1
    if not cond:
        raise AssertionError(msg)

def edge_on(tri):
    return tuple(sorted(tri)) in E

def preserves_full(p):
    for tri in combinations(V,3):
        im=tuple(sorted(p[x] for x in tri))
        if edge_on(tri) != edge_on(im):
            return False
    return True

# The affine maps x |-> ax+b (mod 7).
aff=[]
for a in range(1,7):
    for b in range(7):
        p=tuple((a*x+b)%7 for x in V)
        check(p not in aff)
        check(preserves_full(p))
        aff.append(p)
check(len(aff)==42)

# Exhaustively recover Aut(M) from all 7! permutations.
aut=[]
for p in permutations(V):
    ok=preserves_full(p)
    check(ok == (p in aff))
    if ok:
        aut.append(p)
check(len(aut)==42)
check(set(aut)==set(aff))

subs={k:list(combinations(V,k)) for k in range(8)}

def induced_edges(U):
    S=set(U)
    return tuple(e for e in sorted(E) if set(e)<=S)

def type_key(U):
    k=len(U)
    m=len(induced_edges(U))
    if k==3:
        return 'edge' if m==1 else 'nonedge'
    if k==4:
        return 'one-edge' if m==1 else 'two-edge'
    return 'unique'

def is_iso(U,W,img):
    f=dict(zip(U,img))
    for tri in combinations(U,3):
        im=tuple(sorted(f[x] for x in tri))
        if edge_on(tri) != edge_on(im):
            return False
    return True

def extends(U,img):
    return any(all(g[x]==y for x,y in zip(U,img)) for g in aut)

# Exact induced automorphism orders of representatives.
rep_expected={
    (0,1,2):6,
    (0,1,3):6,
    (0,1,2,3):4,
    (0,1,2,4):6,
    (0,1,2,3,4):2,
    (0,1,2,3,4,5):6,
}
for U,want in rep_expected.items():
    got=0
    for img in permutations(U):
        z=is_iso(U,U,img)
        check(isinstance(z,bool))
        got += z
    check(got==want,(U,got,want))

# Exhaust all partial isomorphisms between equally-sized subsets.
stats=defaultdict(lambda:[0,0]) # isomorphisms, extendible
subset_type_counts=defaultdict(int)
for k,US in subs.items():
    for U in US:
        subset_type_counts[(k,type_key(U))]+=1
    for U in US:
        for W in US:
            for img in permutations(W):
                iso=is_iso(U,W,img)
                check(isinstance(iso,bool))
                if not iso:
                    continue
                key=(k,type_key(U))
                check(type_key(W)==key[1])
                ext=extends(U,img)
                check(isinstance(ext,bool))
                stats[key][0]+=1
                stats[key][1]+=int(ext)

expected_subset_counts={
    (0,'unique'):1,(1,'unique'):7,(2,'unique'):21,
    (3,'nonedge'):21,(3,'edge'):14,
    (4,'one-edge'):14,(4,'two-edge'):21,
    (5,'unique'):21,(6,'unique'):7,(7,'unique'):1,
}
check(dict(subset_type_counts)==expected_subset_counts,(dict(subset_type_counts),expected_subset_counts))

expected_stats={
    (0,'unique'):(1,1),
    (1,'unique'):(49,49),
    (2,'unique'):(882,882),
    (3,'nonedge'):(2646,882),
    (3,'edge'):(1176,588),
    (4,'one-edge'):(1176,588),
    (4,'two-edge'):(1764,882),
    (5,'unique'):(882,882),
    (6,'unique'):(294,294),
    (7,'unique'):(42,42),
}
check({k:tuple(v) for k,v in stats.items()}==expected_stats,(dict(stats),expected_stats))

# Direct all-or-not all extension spectrum.
all_extend={}
for k in range(8):
    entries=[v for (kk,t),v in stats.items() if kk==k]
    iso=sum(x[0] for x in entries); ext=sum(x[1] for x in entries)
    all_extend[k]=(iso==ext)
check(all_extend=={0:True,1:True,2:True,3:False,4:False,5:True,6:True,7:True},all_extend)

# Check the advertised per-type fractions exactly.
fraction_expected={
    (3,'nonedge'):(1,3),
    (3,'edge'):(1,2),
    (4,'one-edge'):(1,2),
    (4,'two-edge'):(1,2),
}
for key,(num,den) in fraction_expected.items():
    iso,ext=stats[key]
    check(ext*den==iso*num,(key,iso,ext))

print('AUT',len(aut))
print('SUBSET_TYPES',dict(sorted(subset_type_counts.items())))
print('STATS', {str(k):tuple(v) for k,v in sorted(stats.items())})
print('ALL_EXTEND',all_extend)
print('TOTAL_PARTIAL_ISOMORPHISMS',sum(v[0] for v in stats.values()))
print('TOTAL_EXTENDIBLE',sum(v[1] for v in stats.values()))
print(f'VERIFY_OK {A} exact assertions')
```
