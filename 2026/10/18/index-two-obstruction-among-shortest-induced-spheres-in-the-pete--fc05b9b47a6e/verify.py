#!/usr/bin/env python3
"""Exact finite certificate for induced H_2 carriers in the Petersen matching complex.
Requires sympy 1.14.0. Run: python3 verify.py
"""
from itertools import combinations, permutations, product
from collections import Counter
from sympy import zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

PVERT = tuple(combinations(range(5),2))
PVID = {v:i for i,v in enumerate(PVERT)}
EDGES = tuple((i,j) for i,a in enumerate(PVERT) for j,b in enumerate(PVERT)
              if i<j and not set(a).intersection(b))
assert len(PVERT)==10 and len(EDGES)==15
EID = {e:i for i,e in enumerate(EDGES)}

def compatible(e,f):
    return set(EDGES[e]).isdisjoint(EDGES[f])

FACES={k:tuple(c for c in combinations(range(15),k)
                 if all(compatible(e,f) for e,f in combinations(c,2)))
       for k in range(1,6)}
assert [len(FACES[k]) for k in range(1,6)]==[15,75,145,90,6]

INDEX={k:{c:i for i,c in enumerate(FACES[k])} for k in range(1,6)}
def boundary_cols(k):
    return [{INDEX[k-1][c[:j]+c[j+1:]]:(-1)**j for j in range(k)}
            for c in FACES[k]]
B2=boundary_cols(3)
B3=boundary_cols(4)

# Every induced six-vertex octahedron is the join of three two-point sets.
CARRIERS=[]
for c in combinations(range(15),6):
    bad=[(a,b) for a,b in combinations(c,2) if not compatible(a,b)]
    if len(bad)==3 and len(set(sum((list(x) for x in bad),[])))==6:
        CARRIERS.append((c,tuple(sorted(bad))))
assert len(CARRIERS)==110

# Oriented join cycle: product of the three elementary differences.
def sphere_chain(pairs):
    terms=Counter()
    for bits in product((0,1),repeat=3):
        selected=[pairs[j][bits[j]] for j in range(3)]
        inv=sum(selected[i]>selected[j] for i in range(3) for j in range(i+1,3))
        terms[INDEX[3][tuple(sorted(selected))]]+=(-1)**(sum(bits)+inv)
    return dict(terms)
CYCLES=[sphere_chain(pairs) for _,pairs in CARRIERS]
for z in CYCLES:
    assert len(z)==8 and set(z.values())=={-1,1}
    dz=Counter()
    for ci,m in z.items():
        for ri,sgn in B2[ci].items():dz[ri]+=m*sgn
    assert all(v==0 for v in dz.values())

# Symmetric group on the five Kneser ground-set coordinates.
ACTION=[]
for perm in permutations(range(5)):
    vp={i:PVID[tuple(sorted(perm[t] for t in subset))]
        for i,subset in enumerate(PVERT)}
    ACTION.append(tuple(EID[tuple(sorted((vp[u],vp[v])))] for u,v in EDGES))
assert len(ACTION)==len(set(ACTION))==120
CID={c:i for i,(c,pairs) in enumerate(CARRIERS)}
unseen=set(range(len(CARRIERS)))
ORBITS=[]
while unseen:
    s=min(unseen)
    orbit={CID[tuple(sorted(action[v] for v in CARRIERS[s][0]))]
           for action in ACTION}
    assert orbit.issubset(unseen)
    ORBITS.append(sorted(orbit))
    unseen.difference_update(orbit)
assert [len(o) for o in ORBITS]==[10,60,40]

# Each carrier decomposes original P into three disjoint two-edge paths.
# The omitted graph vertex and its adjacency to path centers distinguish orbits.
ORBIT_TYPE=[]
for orbit in ORBITS:
    types=set()
    omitted_counts=Counter()
    for cid in orbit:
        c,pairs=CARRIERS[cid]
        touched=set()
        centers=[]
        for i,j in pairs:
            e=set(EDGES[i]);f=set(EDGES[j])
            common=e.intersection(f)
            assert len(common)==1
            centers.append(next(iter(common)))
            touched.update(e|f)
        assert len(touched)==9 and len(set(centers))==3
        omitted=next(iter(set(range(10))-touched))
        omitted_counts[omitted]+=1
        types.add(sum(omitted in EDGES[ei] and centers[k] in EDGES[ei]
                      for k in range(3) for ei in range(15)))
    assert len(types)==1
    assert sorted(omitted_counts.values())==[len(orbit)//10]*10
    ORBIT_TYPE.append(next(iter(types)))
assert ORBIT_TYPE==[3,1,0], ORBIT_TYPE

# Sparse exact rank over fields, separate from SNF integer calculation.
def rank_mod(cols,mod):
    pivot={}
    for col in cols:
        x={i:v%mod for i,v in col.items() if v%mod}
        while x:
            i=min(x)
            if i not in pivot:
                scalar=pow(x[i],-1,mod)
                pivot[i]={j:(a*scalar)%mod for j,a in x.items()}
                break
            scalar=x[i]
            for j,a in pivot[i].items():
                r=(x.get(j,0)-scalar*a)%mod
                if r:x[j]=r
                else:x.pop(j,None)
    return len(pivot)
for mod in [2,3,101]:
    assert rank_mod(B2,mod)==61
    assert rank_mod(B3,mod)==79
    assert rank_mod(B3+CYCLES,mod)==84

# Primitive image and saturation are established by exact integral Smith invariants.
def smith_factors(columns):
    mat=zeros(len(FACES[3]),len(columns))
    for j,c in enumerate(columns):
        for i,z in c.items():mat[i,j]=z
    snf=smith_normal_form(mat,domain=ZZ)
    return [abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]

base=smith_factors(B3)
assert len(base)==79 and set(base)=={1}
print('B3_INTEGER_RANK_79_ALL_UNIT',flush=True)
for orbit,typ in zip(ORBITS,ORBIT_TYPE):
    rep=smith_factors(B3+[CYCLES[orbit[0]]])
    assert len(rep)==80 and set(rep)=={1}
    ds=smith_factors(B3+[CYCLES[i] for i in orbit])
    assert len(ds)==84
    extras=[v for v in ds if v!=1]
    assert extras==([2] if len(orbit)==10 else []),(len(orbit),extras)
    print('ORBIT',len(orbit),'OMITTED_CENTER_ADJACENCY',typ,
          'PRIMITIVE_REP','NONUNIT_SMITH',extras,flush=True)
all_ds=smith_factors(B3+CYCLES)
assert len(all_ds)==84 and set(all_ds)=={1}
print('VERIFY_OK_PETERSEN_SHORTEST_110_OCTAHEDRAL_CARRIERS_10_60_40_INDEX_2_1_1',flush=True)
