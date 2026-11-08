#!/usr/bin/env python3
"""Exact finite verification of the perfect-matching complex of C_12^2.
Only Python's standard library is needed; no saved certificates are trusted.
"""
from collections import Counter, deque
from functools import lru_cache

n = 12
edges = tuple(sorted({tuple(sorted((i, (i+d) % n))) for i in range(n)
                      for d in (1, 2)}))
assert len(edges) == 24
edge_number = {e:i for i,e in enumerate(edges)}
neighbors = {i: set() for i in range(n)}
for u,v in edges:
    neighbors[u].add(v); neighbors[v].add(u)
assert {len(neighbors[i]) for i in range(n)} == {4}

@lru_cache(None)
def completions(remaining):
    if remaining == 0: return ((),)
    first = (remaining & -remaining).bit_length()-1
    result = []
    for other in sorted(neighbors[first]):
        if remaining & (1<<other):
            e = edge_number[tuple(sorted((first,other)))]
            for rest in completions(remaining ^ (1<<first) ^ (1<<other)):
                result.append(tuple(sorted((e,)+rest)))
    return tuple(result)

perfect = tuple(sorted(set(completions((1<<n)-1))))
assert len(perfect) == 36 and all(len(p)==6 for p in perfect)
faces = set()
for p in perfect:
    for subset in range(1,1<<len(p)):
        mask = 0
        for j,e in enumerate(p):
            if subset & (1<<j): mask |= 1<<e
        faces.add(mask)
expected = {0:24,1:180,2:476,3:480,4:216,5:36}
assert dict(Counter(f.bit_count()-1 for f in faces)) == expected
assert len(faces) == 1412

# Second enumeration: all disjoint-edge sets, then check independent
# perfect extendibility of the unused graph vertices.
used_by_edge = tuple((1<<u)|(1<<v) for u,v in edges)
matching_states = {(0, 0)}
for e,edge_used in enumerate(used_by_edge):
    matching_states |= {(mask|(1<<e), used|edge_used)
                        for mask,used in tuple(matching_states)
                        if used & edge_used == 0}
matching_faces = {mask for mask,_ in matching_states}
rechecked = {mask for mask,used in matching_states
             if mask and completions(((1<<n)-1)^used)}
assert rechecked == faces
minimal_bad = {f for f in matching_faces-faces-{0}
               if all((f^(1<<e)) in faces or (f^(1<<e))==0
                      for e in range(len(edges)) if f>>e&1)}
assert Counter(f.bit_count() for f in minimal_bad) == {2:24,3:84,4:12}

# Exhaustive directed-Hasse cycle test for two independent element orders.
def morse(order):
    unused = set(faces)
    partner = {}
    for e in order:
        pairs = [(f, f|(1<<e)) for f in sorted(unused)
                 if not f>>e&1 and (f|(1<<e)) in unused]
        for lo,hi in pairs:
            assert lo in unused and hi in unused
            partner[lo]=hi; partner[hi]=lo
            unused.remove(lo); unused.remove(hi)
    indeg = {f:0 for f in faces}
    out = {f:[] for f in faces}
    incidences = 0
    for hi in faces:
        if hi.bit_count() < 2: continue
        subset=hi
        while subset:
            bit=subset & -subset; subset-=bit
            lo=hi^bit
            a,b=(lo,hi) if partner.get(lo)==hi else (hi,lo)
            out[a].append(b);indeg[b]+=1;incidences+=1
    queue=deque(f for f in faces if not indeg[f]); total=0
    while queue:
        f=queue.popleft();total+=1
        for g in out[f]:
            indeg[g]-=1
            if indeg[g]==0:queue.append(g)
    assert total==len(faces)
    return (len(partner)//2, dict(Counter(f.bit_count()-1 for f in unused)), incidences)

first = morse(range(len(edges)))
second = morse(reversed(range(len(edges))))
assert first[:2] == (696, {0:1,2:19})
assert second[:2] == (695, {0:1,2:20,3:1})
assert first[2]==second[2]

# Independent reduced mod-two homology of all original boundary matrices.
by_dim = {d: sorted(f for f in faces if f.bit_count()==d+1) for d in range(6)}
ranks = {}
for d in range(1,6):
    rows={f:i for i,f in enumerate(by_dim[d-1])}
    pivots={}
    for f in by_dim[d]:
        boundary=0
        subset=f
        while subset:
            bit=subset & -subset;subset-=bit
            boundary ^= 1<<rows[f^bit]
        while boundary:
            pivot=boundary.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=boundary;break
            boundary ^= pivots[pivot]
    ranks[d]=len(pivots)
assert ranks == {1:23,2:157,3:300,4:180,5:36}, ranks
betti={d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(6)}
betti[0]-=1  # reduced degree zero
assert betti == {0:0,1:0,2:19,3:0,4:0,5:0},betti

# D_12 action on the oriented original simplicial chain groups.
def transform(f,k,is_reflection):
    mapped=[]
    for e,(u,v) in enumerate(edges):
        if f>>e&1:
            move=lambda x: (k-x)%n if is_reflection else (k+x)%n
            mapped.append(edge_number[tuple(sorted((move(u),move(v))))])
    inversion_count=sum(a>b for i,a in enumerate(mapped) for b in mapped[i+1:])
    sign=1 if inversion_count%2==0 else -1
    return (sum(1<<e for e in mapped),sign)

characters=[]
for reflection in (False,True):
    row=[]
    for k in range(n):
        signed_lefschetz=sum(((-1)**(f.bit_count()-1))*transform(f,k,reflection)[1]
                            for f in faces if transform(f,k,reflection)[0]==f)
        row.append(signed_lefschetz - 1)  # remove connected H_0
    characters.append(row)
assert characters == [[19,-1,1,-1,1,-1,-5,-1,1,-1,1,-1],
                      [1,-3,1,-3,1,-3,1,-3,1,-3,1,-3]]
assert sum(map(sum,characters)) == 0 # no invariant rational H_2 classes
assert sum(characters[0])==12 # rotation-invariant H_2 is one-dimensional
print('VERIFY_OK')
print('graph_vertices',n,'graph_edges',len(edges),'perfect_matchings',len(perfect))
print('nonempty_faces',len(faces),'f_vector',tuple(expected[d] for d in range(6)))
print('minimal_bad_by_size',sorted(Counter(f.bit_count() for f in minimal_bad).items()))
print('asc_morse',first,'desc_morse',second)
print('mod2_boundary_ranks',tuple(ranks.values()),'reduced_betti',betti)
print('D12_rotation_character',characters[0])
print('D12_reflection_character',characters[1])
print('D12_fixed_h2_dim',0,'C12_fixed_h2_dim',1)
