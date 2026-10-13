#!/usr/bin/env python3
"""Independent executable exact census for the Tutte-Coxeter incidence graph.
Only Python 3 standard library is required.  Vertex labels: 0..14 denote
lexicographically ordered duads of {0,...,5}; 15..29 denote lexicographically
ordered perfect matchings (synthemes) of K6.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product

DUADS = list(combinations(range(6), 2))
DIX = {d:i for i,d in enumerate(DUADS)}
SYNTHEMES = []
def build_synthemes(left, partial):
    if not left:
        SYNTHEMES.append(tuple(sorted(partial)))
        return
    x = left[0]
    for y in left[1:]:
        build_synthemes(tuple(z for z in left[1:] if z != y), partial+[(x,y)])
build_synthemes(tuple(range(6)), [])
SIX = {s:i for i,s in enumerate(SYNTHEMES)}
assert len(DUADS)==len(SYNTHEMES)==15
N=30
ADJ=[set() for _ in range(N)]
for i,s in enumerate(SYNTHEMES):
    for d in s:
        v=DIX[d];w=15+i
        ADJ[v].add(w); ADJ[w].add(v)
EDGES=tuple((v,w) for v in range(15) for w in sorted(ADJ[v]))
assert len(EDGES)==45 and all(len(nb)==3 for nb in ADJ)
ALL=(1<<N)-1

@lru_cache(None)
def permanent_count(unmatched):
    if not unmatched: return 1
    v=(unmatched&-unmatched).bit_length()-1
    return sum(permanent_count(unmatched^(1<<v)^(1<<w)) for w in ADJ[v] if (unmatched>>w)&1)
assert permanent_count(ALL)==288

MATCHINGS=[]
def enumerate_matchings(left,chosen):
    if not left:
        MATCHINGS.append(frozenset(chosen))
        return
    v=(left&-left).bit_length()-1
    for w in sorted(ADJ[v]):
        if (left>>w)&1:
            enumerate_matchings(left^(1<<v)^(1<<w),chosen+[(min(v,w),max(v,w))])
enumerate_matchings(ALL,[])
assert len(MATCHINGS)==288 and len(set(MATCHINGS))==288
MATCHING_SET=set(MATCHINGS)

def complementary_cycles(m):
    rest=[ADJ[i].copy() for i in range(N)]
    for v,w in m:
        rest[v].remove(w); rest[w].remove(v)
    remaining=set(range(N)); cycles=[]
    while remaining:
        root=min(remaining);cur=root;prev=None;edges=[];verts=[]
        while True:
            remaining.remove(cur);verts.append(cur)
            choices=rest[cur]-({prev} if prev is not None else set())
            nxt=min(choices)
            edges.append((min(cur,nxt),max(cur,nxt)))
            prev,cur=cur,nxt
            if cur==root: break
        assert len(verts)==len(edges) and len(edges)%2==0
        cycles.append(tuple(edges))
    assert sum(map(len,cycles))==N
    return cycles

MTYPE={m:tuple(sorted(map(len,complementary_cycles(m)))) for m in MATCHINGS}
assert Counter(MTYPE.values())==Counter({(10,20):144,(30,):144})

# Automorphisms preserving the bipartition arise from relabeling K6.
PRESERVING=[]
for sigma in permutations(range(6)):
    dperm=[DIX[tuple(sorted((sigma[a],sigma[b])))] for a,b in DUADS]
    sperm=[15+SIX[tuple(sorted(tuple(sorted((sigma[a],sigma[b]))) for a,b in s))] for s in SYNTHEMES]
    PRESERVING.append(tuple(dperm+sperm))
assert len(set(PRESERVING))==720
# An explicit incidence duality interchanging the two sides.
DUAL=(15,22,20,28,24,27,25,19,23,16,26,18,21,29,17,
      0,9,14,11,7,2,12,1,8,4,6,10,5,3,13)
AUT=PRESERVING+[tuple(DUAL[p[v]] for v in range(N)) for p in PRESERVING]
assert len(set(AUT))==1440
for p in AUT:
    assert sorted(p)==list(range(N))
EDGE_SET={frozenset(e) for e in EDGES}
assert all(frozenset((p[v],p[w])) in EDGE_SET for p in AUT for v,w in EDGES)

def act_matching(p,m):
    return frozenset((min(p[v],p[w]),max(p[v],p[w])) for v,w in m)

MSEEN=set(); MORBITS=[]
for m in MATCHINGS:
    if m in MSEEN:continue
    orbit={act_matching(p,m) for p in AUT}
    assert orbit<=MATCHING_SET and not orbit&MSEEN
    MSEEN.update(orbit)
    MORBITS.append((len(orbit),MTYPE[m],m))
assert MSEEN==MATCHING_SET
assert Counter((size,typ) for size,typ,_ in MORBITS)==Counter({(144,(30,)):1,(144,(10,20)):1})

# On each complementary even cycle, the remaining two colors alternate.
FACTORIZATIONS=set()
for m in MATCHINGS:
    cycles=complementary_cycles(m)
    complement=set(EDGES)-set(m)
    for parity in product((0,1),repeat=len(cycles)):
        other=frozenset(e for C,bit in zip(cycles,parity)
                        for j,e in enumerate(C) if j%2==bit)
        third=frozenset(complement-other)
        assert other in MATCHING_SET and third in MATCHING_SET
        f=frozenset((m,other,third))
        assert len(f)==3
        FACTORIZATIONS.add(f)
assert len(FACTORIZATIONS)==144
assert all(Counter(MTYPE[m] for m in f)==Counter({(30,):1,(10,20):2}) for f in FACTORIZATIONS)

# Every factorization is one orbit under the full 1,440 automorphisms.
f=next(iter(FACTORIZATIONS))
ORBIT={frozenset(act_matching(p,m) for m in f) for p in AUT}
assert ORBIT==FACTORIZATIONS
members=Counter(m for f in FACTORIZATIONS for m in f)
assert all(members[m]==(1 if MTYPE[m]==(30,) else 2) for m in MATCHINGS)
assert len(FACTORIZATIONS)*6==864

# Certificate: a representative factorization and the two matching orbit representatives.
with open(__file__.rsplit('/',1)[0]+'/representatives.csv','w',encoding='utf8',newline='') as out:
    out.write('kind,orbit_size,cycle_profile,edges_duad_to_syntheme\n')
    for size,typ,m in sorted(MORBITS, key=lambda a:a[1]):
        out.write('perfect_matching,%d,%s,%s\n'%(size,'+'.join(map(str,typ)),
                   ';'.join('%d-%d'%(v,w) for v,w in sorted(m))))
    key=lambda m:tuple(sorted(m))
    chosen=min(FACTORIZATIONS,key=lambda fac:tuple(sorted(map(key,fac))))
    for i,m in enumerate(sorted(chosen,key=key)):
        out.write('factorization_color_%d,144,%s,%s\n'%(i,'+'.join(map(str,MTYPE[m])),
                   ';'.join('%d-%d'%(v,w) for v,w in sorted(m))))

print('VERIFY_OK construction=K6_duads_synthemes vertices=30 edges=45 cubic=true')
print('VERIFY_OK independently_counted_perfect_matchings=288 recursive_count=288')
print('VERIFY_OK two_factor_spectrum=30:144,10+20:144')
print('VERIFY_OK full_automorphism_group=1440 matching_orbits=144+144')
print('VERIFY_OK distinct_one_factorizations=144 proper_named_3_edge_colorings=864')
print('VERIFY_OK each_factorization_contains=one_30_cycle_pair_and_two_10+20_pairs')
print('VERIFY_OK factorization_orbits=one_of_size_144 stabilizer=10')
print('VERIFY_OK membership_per_matching=hamilton:1,nonhamilton:2')
