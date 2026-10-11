#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, deque

FACETS = [
(1,2,3,7),(1,4,7,9),(2,3,4,8),(2,5,8,10),(3,6,7,10),
(1,2,3,11),(1,4,7,10),(2,3,4,11),(2,5,9,10),(3,6,8,9),
(1,2,6,9),(1,4,8,9),(2,3,7,8),(2,6,9,10),(3,6,9,10),
(1,2,6,11),(1,4,8,10),(2,4,6,10),(3,4,5,9),(4,5,6,7),
(1,2,7,9),(1,5,6,8),(2,4,6,11),(3,4,5,11),(4,5,6,11),
(1,3,5,10),(1,5,6,11),(2,4,8,10),(3,4,8,9),(4,5,7,9),
(1,3,5,11),(1,5,8,10),(2,5,7,8),(3,5,9,10),(4,6,7,10),
(1,3,7,10),(1,6,8,9),(2,5,7,9),(3,6,7,8),(5,6,7,8)]
V=tuple(range(1,12))

# Every simplex is a subset of a facet.
simp=[set() for _ in range(4)]
for f in FACETS:
    for r in range(1,5):
        for s in combinations(f,r):
            simp[r-1].add(tuple(sorted(s)))
assert [len(x) for x in simp] == [11,51,80,40]
edges=sorted(simp[1]); triangles=sorted(simp[2]); facets=set(simp[3])
edge_index={e:i for i,e in enumerate(edges)}

# GF(2) bit-vector linear algebra.
def rank(rows):
    rows=[int(x) for x in rows if x]
    piv={}
    for x in rows:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv: y ^= piv[p]
            else:
                piv[p]=y
                break
    return len(piv)

def nullspace(rows,ncols):
    # Nullspace of matrix whose rows are bit masks of length ncols.
    rows=[int(x) for x in rows if x]
    piv=[]; rr=[]
    for col in range(ncols):
        j=next((j for j in range(len(rows)) if ((rows[j]>>col)&1) and all(((rows[j]>>p)&1)==0 for p in piv)),None)
        if j is None: continue
        x=rows[j]
        for q,y in enumerate(rr):
            if (y>>col)&1: rr[q]=y^x
        for q,y in enumerate(rows):
            if q!=j and ((y>>col)&1): rows[q]=y^x
        rr.append(x); piv.append(col)
    free=[c for c in range(ncols) if c not in piv]
    basis=[]
    for f in free:
        x=1<<f
        for p,y in zip(piv,rr):
            if (y>>f)&1: x |= 1<<p
        basis.append(x)
    # independent sanity
    assert len(basis)==ncols-len(piv)
    return basis

def dot(a,b): return (a & b).bit_count() & 1

# Boundary d1: edge -> endpoints. Its transpose equations characterize cycles.
d1_rows=[]
for v in V:
    row=0
    for i,e in enumerate(edges):
        if v in e: row |= 1<<i
    d1_rows.append(row)
Z1 = nullspace(d1_rows,len(edges))

# Triangle boundaries span B1.
B1=[]
for t in triangles:
    m=0
    for e in combinations(t,2): m |= 1<<edge_index[tuple(sorted(e))]
    B1.append(m)
rB=rank(B1)
assert len(Z1)-rB==1

# Explicit nonzero H^1 cocycle certificate.
W_EDGES={(1,4),(1,8),(1,10),(2,5),(3,6),(3,9),(3,10),(4,7),(4,9),
         (5,7),(5,8),(5,9),(5,10),(6,7),(6,8),(7,10),(8,9)}
w=0
for e in W_EDGES:
    e=tuple(sorted(e)); assert e in edge_index; w |= 1<<edge_index[e]
# Cocycle: it vanishes on every triangle boundary.
assert all(dot(w,b)==0 for b in B1)
# Not a coboundary: vertex-cut row space has rank 10, adding w gives rank 11.
vertex_cob=[]
for v in V:
    m=0
    for i,e in enumerate(edges):
        if v in e: m |= 1<<i
    vertex_cob.append(m)
assert rank(vertex_cob)==10
assert rank(vertex_cob+[w])==11

# Minimal 3-vertex supports: empty triangles, all evaluating nontrivially.
generators=[]
for t in combinations(V,3):
    if all(tuple(sorted(e)) in edge_index for e in combinations(t,2)) and tuple(t) not in simp[2]:
        z=0
        for e in combinations(t,2): z |= 1<<edge_index[tuple(sorted(e))]
        if dot(w,z): generators.append(tuple(t))
        else: raise AssertionError('trivial empty triangle')
assert len(generators)==55

def local_cycles(S):
    le=[e for e in edges if set(e)<=S]
    li={e:i for i,e in enumerate(le)}
    rows=[]
    for v in S:
        row=0
        for i,e in enumerate(le):
            if v in e: row |= 1<<i
        rows.append(row)
    bas=nullspace(rows,len(le))
    out=[]
    for z in bas:
        m=0
        for i,e in enumerate(le):
            if (z>>i)&1: m |= 1<<edge_index[e]
        out.append(m)
    return out

support=Counter(); independent=Counter(); direct_support=Counter()
exceptional5=[]
for mask in range(1<<11):
    S={i+1 for i in range(11) if (mask>>i)&1}
    k=len(S)
    zloc=local_cycles(S)
    by_cocycle=any(dot(w,z) for z in zloc)
    direct=rank(B1+zloc)-rB
    assert direct in (0,1)
    assert by_cocycle==(direct==1)
    contains=any(set(t)<=S for t in generators)
    assert by_cocycle==contains
    if by_cocycle:
        support[k]+=1; direct_support[k]+=1
    else:
        independent[k]+=1
        if k==5: exceptional5.append(tuple(sorted(S)))

expected_support={3:55,4:242,5:442,6:462,7:330,8:165,9:55,10:11,11:1}
assert dict(support)==expected_support
assert [independent[i] for i in range(12)] == [1,11,55,110,88,20,0,0,0,0,0,0]
assert len(exceptional5)==20

# Lutz's stated automorphism generators.
def perm_from_cycles(cycles):
    p={i:i for i in V}
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]): p[a]=b
    return tuple(p[i] for i in V)
Gens=[
 perm_from_cycles([(1,2,3,4,5,6),(7,8,9)]),
 perm_from_cycles([(1,2),(3,6),(4,5),(7,9)]),
 perm_from_cycles([(3,6),(7,9),(8,10)])]
ID=tuple(V)
def compose(p,q): return tuple(p[q[i]-1] for i in range(11))
def act_tuple(p,t): return tuple(sorted(p[x-1] for x in t))
for p in Gens:
    assert {act_tuple(p,f) for f in facets}==facets
group={ID}; q=deque([ID])
while q:
    a=q.popleft()
    for g in Gens:
        b=compose(g,a)
        if b not in group: group.add(b); q.append(b)
assert len(group)==48

def orbit_partition(items):
    rem=set(items); sizes=[]; reps=[]
    while rem:
        x=min(rem); orb={act_tuple(g,x) for g in group}
        assert orb<=set(items)
        sizes.append(len(orb)); reps.append(x); rem-=orb
    return sorted(sizes), reps
sizesG,repsG=orbit_partition(generators)
sizes5,reps5=orbit_partition(exceptional5)
assert sizesG==[3,4,12,12,24]
assert sizes5==[8,12]

print('VERIFY_OK f=11,51,80,40 H1=1 generator_triangles=55 '
      'support=3:55,4:242,5:442,6:462,7:330,8:165,9:55,10:11,11:1 '
      'independent=0:1,1:11,2:55,3:110,4:88,5:20 '
      'aut=48 gen_orbits=3,4,12,12,24 exceptional5_orbits=8,12')
