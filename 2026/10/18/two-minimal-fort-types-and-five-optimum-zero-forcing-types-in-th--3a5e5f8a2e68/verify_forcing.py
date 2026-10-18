#!/usr/bin/env python3
"""Exact Heawood zero-forcing and full symmetry verifier; Python standard library."""
import itertools, collections, json, sys

P=range(1,8); n=14; full=(1<<n)-1
lines=sorted(set(tuple(sorted((a,b,a^b))) for a,b in itertools.combinations(P,2)))
assert len(lines)==7
line_index={a:i for i,a in enumerate(lines)}
nb=[0]*n
for k,line in enumerate(lines):
    for p in line:
        nb[p-1]|=1<<(7+k)
        nb[7+k]|=1<<(p-1)
assert all(x.bit_count()==3 for x in nb)

def closure(seed):
    seen=seed; depth=0
    while True:
        change=0
        for v in range(n):
            if seen & (1<<v):
                pending=nb[v] & (full^seen)
                if pending.bit_count()==1:change|=pending
        if not change:return seen==full,depth
        seen|=change;depth+=1

is_z=[closure(x)[0] for x in range(1<<n)]
poly=collections.Counter(x.bit_count() for x in range(1<<n) if is_z[x])
expected={6:700,7:1904,8:2401,9:1862,10:987,11:364,12:91,13:14,14:1}
assert dict(poly)==expected
minimal_z=[x for x in range(1<<n) if is_z[x] and all(not is_z[x^(1<<v)] for v in range(n) if x>>v&1)]
assert len(minimal_z)==700 and all(x.bit_count()==6 for x in minimal_z)
ptime=collections.Counter(closure(x)[1] for x in minimal_z)
assert dict(ptime)=={2:196,3:504}

# A fort has no outside vertex with precisely one neighbour inside.
def is_fort(x):
    return x!=0 and all((nb[v]&x).bit_count()!=1 for v in range(n) if not (x>>v&1))
fort=[is_fort(x) for x in range(1<<n)]
# Every smaller proper subset is contained in a one-vertex deletion;
# this recurrence is needed because forthood is NOT hereditary.
has_proper=[False]*(1<<n)
for x in range(1,1<<n):
    has_proper[x]=any(fort[x^(1<<v)] or has_proper[x^(1<<v)] for v in range(n) if x>>v&1)
minfort=[x for x in range(1,1<<n) if fort[x] and not has_proper[x]]
assert len(minfort)==70 and collections.Counter(x.bit_count() for x in minfort)=={4:14,7:56}
assert all(is_z[x]==(not any((f & (full^x))==f for f in minfort)) for x in range(1<<n))

# Enumerate all Fano-plane point permutations and construct induced line maps.
col=[]
for pi in itertools.permutations(P):
    image=tuple(pi[v-1]-1 for v in P)
    mapped=[]
    for L in lines:
        triple=tuple(sorted(pi[p-1] for p in L))
        if triple not in line_index:break
        mapped.append(7+line_index[triple])
    if len(mapped)==7:col.append(image+tuple(mapped))
assert len(col)==168
# Fano polarity: a nonzero vector p is mapped to the line {q: p.q=0}.
def dot(a,b):return (a&b).bit_count()%2
polar=[]
for p in P:
    triple=tuple(q for q in P if dot(p,q)==0)
    polar.append(7+line_index[triple])
for L in lines:
    normals=[p for p in P if all(dot(p,q)==0 for q in L)]
    assert len(normals)==1
    polar.append(normals[0]-1)
polar=tuple(polar)
autos=sorted(set(col+[tuple(g[polar[v]] for v in range(n)) for g in col]))
assert len(autos)==336
assert all(all(bool(nb[u]>>v&1)==bool(nb[g[u]]>>g[v]&1) for u in range(n) for v in range(n)) for g in autos)

def orbit_list(collection):
    unseen=set(collection);out=[]
    while unseen:
        rep=min(unseen)
        images={sum(1<<g[i] for i in range(n) if rep>>i&1) for g in autos}
        assert images<=unseen.union(set(collection)-unseen)
        unseen.difference_update(images)
        out.append({'representative_mask':rep,'orbit_size':len(images),
                    'points':[i+1 for i in range(7) if rep>>i&1],
                    'lines':[i for i in range(7) if rep>>(7+i)&1]})
    return sorted(out,key=lambda d:(d['orbit_size'],d['representative_mask']))

fort_orbits=orbit_list(minfort);zf_orbits=orbit_list(minimal_z)
assert [(x['orbit_size'],x['representative_mask']) for x in fort_orbits]==[(14,30),(56,1524)]
assert [(x['orbit_size'],x['representative_mask']) for x in zf_orbits]==[(28,1419),(168,1421),(168,1429),(168,1430),(168,1477)]
for x in zf_orbits:x['synchronous_rounds']=closure(x['representative_mask'])[1]
certificate={'graph':'Heawood incidence graph of PG(2,2)',
             'vertex_order':'points 1..7 as indices 0..6; lines in lex order as indices 7..13',
             'lines':lines,'automorphism_order':len(autos),
             'zero_forcing_polynomial_coefficients':dict(sorted(poly.items())),
             'minimal_fort_orbits':fort_orbits,'minimum_zero_forcing_orbits':zf_orbits,
             'minimum_propagation_times':dict(sorted(ptime.items()))}
if len(sys.argv)>1:
    with open(sys.argv[1],encoding='utf8') as fh:claimed=json.load(fh)
    assert claimed==json.loads(json.dumps(certificate))
print('VERIFY_DIRECT_OK masks=16384 forcing=8324 minimum_size=6 minimum_count=700')
print('VERIFY_DIRECT_OK polynomial=6:700,7:1904,8:2401,9:1862,10:987,11:364,12:91,13:14,14:1')
print('VERIFY_DIRECT_OK all_minimal_zero_forcing_sets_size_6=true propagation=2:196,3:504')
print('VERIFY_GEOMETRY_OK lines=7 bipartite_vertices=14 automorphisms=336 min_fort_orbits=14+56 min_forcing_orbits=28+168x4')
print('VERIFY_OBSTRUCTION_OK minimal_forts=70 all_16384_fort_hitting_decisions=true')
if len(sys.argv)==1:print(json.dumps(certificate,indent=2))
