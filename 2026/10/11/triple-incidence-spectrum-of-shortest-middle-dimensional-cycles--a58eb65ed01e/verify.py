from itertools import combinations
from collections import Counter, deque

V=tuple(range(1,16))
SEEDS=[
(1,2,3,4,5,6,7,8,12),
(1,2,3,4,5,6,7,8,13),
(1,2,3,4,5,6,7,12,14),
(1,2,3,4,5,6,7,13,15),
(1,2,3,4,5,6,7,14,15),
(1,2,3,4,5,6,8,9,12),
(1,2,3,4,5,6,8,9,13),
(1,2,3,4,5,6,9,13,15),
(1,2,3,4,5,6,9,14,15),
(1,2,3,4,5,7,8,10,11),
(1,2,3,4,5,9,10,13,15),
(1,2,3,4,5,9,10,14,15),
(1,2,3,4,6,8,9,10,12),
(1,2,3,4,7,9,11,14,15),
]
EXPECTED_ORBIT_SIZES=[60,60,60,15,15,30,30,60,60,20,10,30,30,10]

def perm_from_cycles(cycles):
    p={i:i for i in V}
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]): p[a]=b
    return tuple(p[i] for i in V)

def compose(p,q): # p after q
    return tuple(p[q[i]-1] for i in range(15))

def apply(p,S):
    return tuple(sorted(p[i-1] for i in S))

g1=perm_from_cycles([(1,9,10,3,14),(2,15,7,12,6),(4,5,11,13,8)])
g2=perm_from_cycles([(1,4,10),(2,5,8),(3,7,11),(6,9,15),(12,14,13)])
idp=tuple(V)
G={idp}; Q=deque([idp])
while Q:
    a=Q.popleft()
    for g in (g1,g2):
        b=compose(g,a)
        if b not in G: G.add(b); Q.append(b)
assert len(G)==60

orbits=[]
facets=set()
for s in SEEDS:
    o={apply(g,s) for g in G}
    orbits.append(o); facets |= o
assert [len(o) for o in orbits]==EXPECTED_ORBIT_SIZES
assert len(facets)==490

faces={k:set() for k in range(1,10)}
for F in facets:
    for k in range(1,10): faces[k].update(combinations(F,k))
fvec=[len(faces[k]) for k in range(1,10)]
assert fvec==[15,105,455,1365,3003,4515,4230,2205,490]

all6=set(combinations(V,6))
missing6=all6-faces[6]
comp_facets={tuple(sorted(set(V)-set(F))) for F in facets}
assert missing6==comp_facets and len(missing6)==490

# GF(2) rank and membership, vectors stored as Python integers.
def xor_basis(vectors):
    basis={}
    for x in vectors:
        while x:
            p=x.bit_length()-1
            if p in basis: x ^= basis[p]
            else:
                basis[p]=x
                break
    return basis

def in_span(x,basis):
    while x:
        p=x.bit_length()-1
        if p not in basis: return False
        x ^= basis[p]
    return True

C3=sorted(faces[4]); C4=sorted(faces[5]); C5=sorted(faces[6])
i3={s:i for i,s in enumerate(C3)}; i4={s:i for i,s in enumerate(C4)}

def bd4(simplex5):
    x=0
    for t in combinations(simplex5,4): x ^= 1<<i3[t]
    return x

def bd5(simplex6):
    x=0
    for t in combinations(simplex6,5): x ^= 1<<i4[t]
    return x

B4=xor_basis(bd4(s) for s in C4)
B5=xor_basis(bd5(s) for s in C5)
rank_d4=len(B4); rank_d5=len(B5)
h4=len(C4)-rank_d4-rank_d5
assert (rank_d4,rank_d5,h4)==(1001,2001,1)
assert all(not in_span(bd5(S),B5) for S in missing6)

# Minimum-support argument is structural: <=5 vertices cannot support a nonzero 4-cycle;
# on exactly 6 vertices the only nonzero 4-cycle is the full boundary of a 5-simplex.
# Since K is 5-neighborly and every missing 6-set has nonbounding boundary, the 490
# missing 6-sets are exactly the minimum-support nonzero H4(F2) cycles.

vertex_counts=Counter(v for B in missing6 for v in B)
pair_counts=Counter(T for B in missing6 for T in combinations(B,2))
triple_counts=Counter(T for B in missing6 for T in combinations(B,3))
assert set(vertex_counts.values())=={196}
assert len(pair_counts)==105 and set(pair_counts.values())=={70}
spectrum=Counter(triple_counts.values())
assert spectrum==Counter({4:5,13:30,16:60,19:150,22:60,25:60,28:10,31:80})
mins=sorted(T for T,c in triple_counts.items() if c==4)
expected_mins=[(1,6,8),(2,4,9),(3,7,11),(5,10,15),(12,13,14)]
assert mins==expected_mins
assert set().union(*(set(T) for T in mins))==set(V)
assert sum(map(len,mins))==15
assert all(set(a).isdisjoint(b) for i,a in enumerate(mins) for b in mins[i+1:])
# The five minimum triples are invariant under G and form a single orbit.
minset=set(mins)
assert all({apply(g,T) for T in minset}==minset for g in G)
assert len({apply(g,mins[0]) for g in G})==5

print('VERIFY_OK group=60 orbit_sizes='+','.join(map(str,EXPECTED_ORBIT_SIZES))+
      ' f='+','.join(map(str,fvec))+
      ' H4_F2=1 ranks_d4_d5=%d,%d missing6=490 design=2-(15,6,70) '%(rank_d4,rank_d5)+
      'triple_spectrum='+','.join(f'{k}:{spectrum[k]}' for k in sorted(spectrum))+
      ' min_triples='+';'.join('-'.join(map(str,T)) for T in mins))
