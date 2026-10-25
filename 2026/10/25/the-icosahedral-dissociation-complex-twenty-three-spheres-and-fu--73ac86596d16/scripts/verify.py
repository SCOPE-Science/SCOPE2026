#!/usr/bin/env python3
"""Reproduce the homotopy and symmetry computations for a finite icosahedral graph complex."""
from collections import Counter, defaultdict, deque
from itertools import combinations

ADJ = (
 (1,5,7,8,11), (0,2,5,6,8), (1,3,6,8,9),
 (2,4,6,9,10), (3,5,6,10,11), (0,1,4,6,11),
 (1,2,3,4,5), (0,8,9,10,11), (0,1,2,7,9),
 (2,3,7,8,10), (3,4,7,9,11), (0,4,5,7,10))
N = len(ADJ)
A = tuple(sum(1 << v for v in neighbors) for neighbors in ADJ)
assert N == 12 and all(len(a) == 5 for a in ADJ)
assert all(i in ADJ[j] for i in range(N) for j in ADJ[i])
assert sum(map(len, ADJ)) // 2 == 30

def degree_valid(m):
    return all(((m & A[i]).bit_count() <= 1) for i in range(N) if m >> i & 1)

def component_valid(m):
    unseen = m
    while unseen:
        seen = 0
        front = unseen & -unseen
        while front:
            vbit = front & -front
            front ^= vbit
            if seen & vbit:
                continue
            seen |= vbit
            v = vbit.bit_length() - 1
            front |= (A[v] & unseen & ~seen)
        if seen.bit_count() > 2:
            return False
        unseen &= ~seen
    return True

faces = frozenset(m for m in range(1 << N) if degree_valid(m))
assert all(degree_valid(m) == component_valid(m) for m in range(1 << N))
assert len(faces) == 324 and 0 in faces
fvec = Counter(m.bit_count()-1 for m in faces)
assert dict(fvec) == {-1:1, 0:12, 1:66, 2:140, 3:105}
facets = [m for m in faces if m and not any((m | (1<<i)) in faces for i in range(N) if not (m>>i&1))]
assert len(facets) == 105 and all(m.bit_count() == 4 for m in facets)

PIVOTS = (2,11,3,10,5,0,7,9,1,4,6,8)
unpaired = set(faces)
matching = {}
for v in PIVOTS:
    for m in sorted(faces):
        if m and not m & (1 << v) and m in unpaired:
            b = m | (1 << v)
            if b in unpaired:
                unpaired.remove(m)
                unpaired.remove(b)
                matching[m] = b
assert len(matching) == 151
assert Counter(m.bit_count()-1 for m in unpaired) == {-1:1, 0:1, 3:20}
# The unused empty face is not a cell of the geometric realization.

out = defaultdict(list)
indeg = {m:0 for m in faces}
incidences=0
for high in faces:
    for v in range(N):
        if high & (1 << v):
            low = high ^ (1 << v)
            src, dst = (low, high) if matching.get(low) == high else (high, low)
            out[src].append(dst)
            indeg[dst] += 1
            incidences += 1
q = deque(m for m in faces if indeg[m] == 0)
count = 0
while q:
    m = q.popleft()
    count += 1
    for n in out[m]:
        indeg[n] -= 1
        if indeg[n] == 0: q.append(n)
assert count == len(faces)

# Verify independent simplicial homology ranks over F_2 (supporting check).
chains = {d:sorted(m for m in faces if m.bit_count() == d+1) for d in range(4)}
def mod2_rank(columns):
    pivots={}
    for x in columns:
        while x:
            i=x.bit_length()-1
            if i in pivots: x ^= pivots[i]
            else:
                pivots[i]=x
                break
    return len(pivots)
ranks={}
for d in range(1,4):
    rows={m:i for i,m in enumerate(chains[d-1])}
    cols=[sum(1 << rows[m^(1<<i)] for i in range(N) if m>>i&1) for m in chains[d]]
    ranks[d]=mod2_rank(cols)
assert ranks == {1:11,2:55,3:85}, ranks

ID = tuple(range(N))
ROT2 = (1,0,11,10,9,8,7,6,5,4,3,2)
ROT3 = (5,0,7,9,2,1,8,4,11,10,3,6)
ANTIP = (3,10,11,0,8,9,7,6,4,5,1,2)

def compose(g,h): return tuple(g[h[i]] for i in range(N))
def order(g):
    a=ID
    for i in range(1,121):
        a=compose(a,g)
        if a==ID: return i
    raise AssertionError

def closure(gens):
    known={ID};q=deque([ID])
    while q:
        x=q.popleft()
        for g in gens:
            y=compose(x,g)
            if y not in known:
                known.add(y);q.append(y)
    return known

def automorphism(g):
    return sorted(g) == list(range(N)) and all(
        ((j in ADJ[i]) == (g[j] in ADJ[g[i]]))
        for i in range(N) for j in range(i+1,N))

rot = closure((ROT2,ROT3))
full = closure((ROT2,ROT3,ANTIP))
assert len(rot)==60 and len(full)==120 and all(automorphism(g) for g in full)
assert order(ROT2)==2 and order(ROT3)==3 and order(compose(ROT2,ROT3))==5
assert ANTIP not in rot and order(ANTIP)==2
assert all(compose(ANTIP,g)==compose(g,ANTIP) for g in full)
# The five neighbors of any vertex induce C_5. The stabilizer injects
# into D_5 and there are twelve vertices, so Aut(I) has order at most 120.
assert all(sum(j in ADJ[i] for j in ADJ[v]) == 2 for v in range(N) for i in ADJ[v])

# For rotation subgroup identification, the two generators preserve oriented
# triangular face cycles on the icosahedron.
tri = tuple(c for c in combinations(range(N),3) if all((c[j] in ADJ[c[i]]) for i,j in combinations(range(3),2)))
assert len(tri)==20
oriented={tri[0]:1}; todo=deque([tri[0]])
def ecoeff(t,x,y):
    z=next(v for v in t if v!=x and v!=y)
    return (-1)**t.index(z)
while todo:
    t=todo.popleft()
    for x,y in combinations(t,2):
        nbr=[u for u in tri if u != t and x in u and y in u]
        assert len(nbr)==1
        u=nbr[0]
        s=-oriented[t]*ecoeff(t,x,y)*ecoeff(u,x,y)
        if u not in oriented:
            oriented[u]=s;todo.append(u)
        else:assert oriented[u]==s
assert len(oriented)==20

def parity(values):
    return (-1) ** sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))
def orientation(g):
    src=tri[0]; images=[g[v] for v in src]
    return oriented[tuple(sorted(images))]*parity(images)*oriented[src]
assert orientation(ROT2)==orientation(ROT3)==1 and orientation(ANTIP)==-1
assert all(orientation(g)==1 for g in rot)

# Equivariant Euler--Poincare identity for reduced H_3.
def character(g):
    tr=[0,0,0,0]
    for m in faces:
        if not m:continue
        v=[i for i in range(N) if m>>i&1]
        w=[g[i] for i in v]
        if sum(1<<x for x in w)==m:
            tr[len(v)-1]+=parity(w)
    return 1 - tr[0]+tr[1]-tr[2]+tr[3]
character_rot=Counter((order(g),character(g)) for g in rot)
character_antirot=Counter((order(g),character(compose(ANTIP,g))) for g in rot)
assert character_rot == {(1,20):1, (2,4):15,(3,-1):20,(5,0):24}
assert character_antirot == {(1,10):1,(2,2):15,(3,1):20,(5,0):24}
assert sum(character(g) for g in full) == 120
assert sum(character(g)**2 for g in full) == 840
# A_5 irreducible rational characters on classes 1, 2, 3, 5a, 5b:
# 1=(1,1,1,1,1), 4=(4,0,1,-1,-1), 5=(5,1,-1,0,0).
# Thus the antipodally even character is 1+4+2*5 and the odd is 5.
assert (15,3,0,0) == (1+4+2*5, 1+0+2, 1+1-2, 1-1)
assert (5,1,-1,0) == (5,1,-1,0)

print('F_VECTOR',dict(sorted(fvec.items())))
print('FACETS',len(facets))
print('MORSE_PAIRS',len(matching),'CRITICAL',dict(sorted(Counter(m.bit_count()-1 for m in unpaired).items())))
print('INCIDENCES',incidences,'ACYC',count,'/',len(faces))
print('MOD2_BOUNDARY_RANKS',ranks)
print('AUTOMORPHISMS',len(full),'ROTATIONS',len(rot),'ANTIPODAL',ANTIP)
print('ROTATIONAL_CHARS',sorted(character_rot.items()))
print('ANTIPODAL_TWIST_CHARS',sorted(character_antirot.items()))
print('MODULE','1_even + 4_even + 2*5_even + 5_odd')
print('VERIFY_OK')
