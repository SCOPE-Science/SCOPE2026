#!/usr/bin/env python3
import itertools, hashlib, json
Q=range(3); N=4
ZERO=(0,0,0,0)
V=[x for x in itertools.product(Q, repeat=N) if x!=ZERO]
IDX={x:i for i,x in enumerate(V)}
ALL=(1<<len(V))-1

def sep3(a,b,c):
    return any(len({a[r],b[r],c[r]})==3 for r in range(N))

def is_phf(C):
    return all(sep3(a,b,c) for a,b,c in itertools.combinations(C,3))

def is_oa(C):
    if len(C)!=9: return False
    return all(len({(x[i],x[j]) for x in C})==9 for i in range(N) for j in range(i+1,N))

# Normalization: any nonempty family can be mapped so a chosen column is ZERO by
# independent symbol permutations. Thus a size >=10 family would yield one containing ZERO.
adj=[0]*len(V)
for i,x in enumerate(V):
    m=0
    for j,y in enumerate(V):
        if i!=j and sep3(ZERO,x,y): m|=1<<j
    adj[i]=m
pairmask={}
for i in range(len(V)):
    for j in range(i+1,len(V)):
        m=0
        for k,z in enumerate(V):
            if k!=i and k!=j and sep3(V[i],V[j],z): m|=1<<k
        pairmask[(i,j)]=m

best=0; maxima=[]; nodes=0

def search(chosen,cand):
    global best,maxima,nodes
    nodes += 1
    total=1+len(chosen)
    if total>best:
        best=total; maxima=[]
    if total==9:
        maxima.append(tuple(chosen))
        # no need to extend if a size-10 branch remains; continue below to rule it out
    if total + cand.bit_count() <= max(best,9):
        return
    while cand:
        if total + cand.bit_count() <= max(best,9):
            return
        bit=cand & -cand; v=bit.bit_length()-1; cand-=bit
        nc=cand & adj[v]
        for i in chosen:
            a,b=sorted((i,v)); nc &= pairmask[(a,b)]
        search(chosen+[v], nc)

# First pass to determine maximum and collect size-9 normalized solutions.
# Use a separate exact enumerator because pruning above tracks best.
best=1

def bound_search(chosen,cand):
    global best,nodes
    nodes += 1
    total=1+len(chosen)
    if total>best: best=total
    if total+cand.bit_count()<=best: return
    while cand:
        if total+cand.bit_count()<=best: return
        bit=cand&-cand; v=bit.bit_length()-1; cand-=bit
        nc=cand & adj[v]
        for i in chosen:
            a,b=sorted((i,v)); nc &= pairmask[(a,b)]
        bound_search(chosen+[v],nc)

bound_search([],ALL)
assert best==9, best
maxima=[]; nodes_enum=0

def enum9(chosen,cand):
    global nodes_enum
    nodes_enum+=1
    total=1+len(chosen)
    if total==9:
        maxima.append(tuple(chosen)); return
    if total+cand.bit_count()<9: return
    while cand:
        if total+cand.bit_count()<9: return
        bit=cand&-cand; v=bit.bit_length()-1; cand-=bit
        nc=cand & adj[v]
        for i in chosen:
            a,b=sorted((i,v)); nc &= pairmask[(a,b)]
        enum9(chosen+[v],nc)

enum9([],ALL)
normalized=[]
for s in maxima:
    C=tuple(sorted((ZERO,)+tuple(V[i] for i in s)))
    assert is_phf(C) and is_oa(C)
    normalized.append(C)
assert len(normalized)==8, len(normalized)
assert len(set(normalized))==8

rep=normalized[0]
perms=list(itertools.permutations(Q))
coord_perms=list(itertools.permutations(range(N)))

def transform(C, cps, rp):
    # first independent symbol maps on old coordinates, then permute coordinates
    out=[]
    for x in C:
        y=tuple(cps[i][x[i]] for i in range(N))
        z=tuple(y[rp[i]] for i in range(N))
        out.append(z)
    return tuple(sorted(out))

orbit=set(); stab=0
for cps in itertools.product(perms, repeat=N):
    for rp in coord_perms:
        T=transform(rep,cps,rp)
        orbit.add(T)
        if T==rep: stab+=1
assert len(orbit)==72, len(orbit)
assert stab==432, stab
assert all(is_phf(C) and is_oa(C) for C in orbit)
# Orbit contains all normalized maxima and incidence count forces total=72.
orb0={C for C in orbit if ZERO in C}
assert orb0==set(normalized)
# Direct OA->PHF lemma check on the orbit, plus distance consequence.
for C in orbit:
    for a,b in itertools.combinations(C,2):
        assert sum(x!=y for x,y in zip(a,b))>=3

census='\n'.join(' '.join(''.join(map(str,x)) for x in C) for C in sorted(orbit))+'\n'
sha=hashlib.sha256(census.encode()).hexdigest()
print('VERIFY_OK',
      f'maximum={best}',
      f'normalized_maxima={len(normalized)}',
      f'labeled_maxima={len(orbit)}',
      f'natural_group={len(perms)**N*len(coord_perms)}',
      f'orbits=1',
      f'orbit_size={len(orbit)}',
      f'stabilizer={stab}',
      f'all_maxima_OA={all(is_oa(C) for C in orbit)}',
      f'bound_nodes={nodes}',
      f'enum_nodes={nodes_enum}',
      f'census_sha256={sha}')
