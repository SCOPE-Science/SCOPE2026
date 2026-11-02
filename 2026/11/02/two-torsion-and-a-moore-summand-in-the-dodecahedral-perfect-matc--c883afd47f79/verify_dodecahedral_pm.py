#!/usr/bin/env python3
"""Exact finite proof checker for the dodecahedral perfect-matching complex.

Standard-library only. All face sets, gradient paths, and integer minors are
recomputed from the explicitly specified graph. With --emit-certificate PATH,
write the exact critical-cell and signed-boundary data for independent review.
"""
import collections
import functools
import json
import sys
from pathlib import Path

N = 20
ADJ = {v: set() for v in range(N)}
for i in range(10):
    for a, b in ((i, (i+1)%10), (i, 10+i), (10+i, 10+(i+2)%10)):
        ADJ[a].add(b)
        ADJ[b].add(a)
EDGES = sorted((a,b) for a in range(N) for b in ADJ[a] if a < b)
assert len(EDGES)==30 and all(len(ADJ[v])==3 for v in range(N))
EDGE_INDEX={e:k for k,e in enumerate(EDGES)}

perfect=[]
def rec(uncovered, matching):
    if not uncovered:
        perfect.append(tuple(sorted(matching)))
        return
    a = min(uncovered)
    for b in sorted(ADJ[a] & uncovered):
        e = (min(a,b),max(a,b))
        rec(uncovered-{a,b}, matching+(EDGE_INDEX[e],))
rec(frozenset(range(N)), ())
assert len(perfect)==36 and len(set(perfect))==36

# Each face occurs by downward closure of at least one complete matching.
faces=set()
for m in perfect:
    for t in range(1,1<<10):
        s=0
        for j in range(10):
            if (t>>j)&1:
                s|=1<<m[j]
        faces.add(s)
assert len(faces)==30503
expected_f=[30,375,2180,5790,8352,7440,4320,1620,360,36]
assert [sum(s.bit_count()==d+1 for s in faces) for d in range(10)]==expected_f

# Sequential toggle: match a lower and an upper face only while both unused.
free=set(faces)
low_to_high={}
match_stages=[]
for k in range(len(EDGES)):
    bit=1<<k
    todo=[s for s in free if not (s&bit) and (s|bit) in free]
    for s in todo:
        u=s|bit
        assert s in free and u in free
        low_to_high[s]=u
        free.remove(s)
        free.remove(u)
    match_stages.append(len(todo))
assert len(low_to_high)==15231
assert match_stages==[5455,4610,4070,184,155,178,131,108,93,52,71,39,42,8,11,5,3,2,0,0,2,4,1,1,0,2,2,0,1,1]
critical={d:sorted(s for s in free if s.bit_count()==d+1) for d in range(10)}
assert {d:len(c) for d,c in critical.items() if c}=={0:1,2:10,3:30}

# Inspect every nonempty Hasse incidence, reverse exactly the matched covers.
indegree=dict.fromkeys(faces,0)
out=collections.defaultdict(list)
cover_count=0
for s in faces:
    bits=s
    while bits:
        bit=bits&-bits
        bits^=bit
        t=s^bit
        if t==0:
            continue
        cover_count+=1
        if low_to_high.get(t)==s:
            out[t].append(s)
            indegree[s]+=1
        else:
            out[s].append(t)
            indegree[t]+=1
q=collections.deque(s for s,i in indegree.items() if i==0)
visited=0
while q:
    s=q.popleft()
    visited+=1
    for t in out[s]:
        indegree[t]-=1
        if indegree[t]==0:
            q.append(t)
assert visited==len(faces), 'Non-acyclic Morse pairing'

upper_to_lower={upper:lower for lower,upper in low_to_high.items()}
sys.setrecursionlimit(100000)
@functools.lru_cache(maxsize=None)
def projection(s):
    """Orientated gradient elimination onto critical cells of same dimension."""
    if s in upper_to_lower:
        return {}
    if s not in low_to_high:
        return {s:1}
    upper=low_to_high[s]
    sign_pivot=None
    terms=collections.Counter()
    bits=upper
    pos=0
    while bits:
        bit=bits&-bits
        bits^=bit
        lower=upper^bit
        inc=(-1)**pos
        pos+=1
        if lower==s:
            sign_pivot=inc
        else:
            for critface,coefficient in projection(lower).items():
                terms[critface]-=inc*coefficient
    assert sign_pivot in (-1,1)
    return {f:sign_pivot*v for f,v in terms.items() if v}

lowcrit=critical[2]
highcrit=critical[3]
lowindex={s:i for i,s in enumerate(lowcrit)}
B=[[0]*len(highcrit) for _ in lowcrit]
for j,s in enumerate(highcrit):
    bits=s
    pos=0
    while bits:
        bit=bits&-bits
        bits^=bit
        lower=s^bit
        inc=(-1)**pos
        pos+=1
        for c,v in projection(lower).items():
            B[lowindex[c]][j]+=inc*v
assert sum(bool(v) for row in B for v in row)==69
assert all(v in (-1,0,1) for row in B for v in row)

# Bitset Gaussian elimination directly on the original 30,503-face complex.
bydim={d:sorted(s for s in faces if s.bit_count()==d+1) for d in range(10)}
mod2_rank=[]
for d in range(1,10):
    index={s:j for j,s in enumerate(bydim[d-1])}
    basis={}
    for s in bydim[d]:
        bits=s
        column=0
        while bits:
            bit=bits&-bits
            bits^=bit
            column ^=1<<index[s^bit]
        while column:
            top=column.bit_length()-1
            if top not in basis:
                basis[top]=column
                break
            column^=basis[top]
    mod2_rank.append(len(basis))
assert mod2_rank==[29,346,1833,3936,4416,3024,1296,324,36]

# Independent mod-2 rank of the signed Morse 10x30 boundary.
basis={}
for j in range(len(highcrit)):
    column=sum((B[i][j]&1)<<i for i in range(len(lowcrit)))
    while column:
        k=column.bit_length()-1
        if k not in basis:
            basis[k]=column
            break
        column^=basis[k]
assert len(basis)==9

# Exact small determinant via rationally exact integer Bareiss elimination.
def det_exact(A):
    m=[list(row) for row in A]
    n=len(m)
    sign=1
    den=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if m[i][k]),None)
        if p is None:
            return 0
        if p!=k:
            m[k],m[p]=m[p],m[k]
            sign=-sign
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=m[i][j]*pivot-m[i][k]*m[k][j]
                assert numerator%den==0
                m[i][j]=numerator//den
            m[i][k]=0
        den=pivot
    return sign*m[n-1][n-1] if n else 1
rows9=[0,2,3,4,5,6,7,8,9]
cols9=[0,2,4,5,6,7,8,11,26]
cols10=[0,2,4,5,6,7,8,10,11,26]
minor9=det_exact([[B[i][j] for j in cols9] for i in rows9])
minor10=det_exact([[B[i][j] for j in cols10] for i in range(10)])
assert abs(minor9)==1 and abs(minor10)==2,(minor9,minor10)
# Rank mod 2 = 9 forces all 10x10 minors even; a 10x10 minor of magnitude
# two forces gcd of all maximal minors to be 2. Together with a unit
# 9x9 minor, the nonzero integral Smith invariant factors are 1^9,2.
assert [len(bydim[d]) - (mod2_rank[d-1] if d else 0) - (mod2_rank[d] if d<9 else 0)
        for d in range(10)] == [1,0,1,21,0,0,0,0,0,0]

certificate={
    'graph':'GP(10,2)', 'perfect_matching_count':36,
    'edge_order':[list(e) for e in EDGES],
    'face_vector':expected_f,
    'faces_nonempty':len(faces),
    'match_stage_pair_counts':match_stages,
    'morse_pairs':len(low_to_high),
    'critical_cells_bitmasks_by_dimension':{str(d):v for d,v in critical.items() if v},
    'all_nonempty_hasse_incidences':cover_count,
    'signed_morse_boundary_dim3_to_dim2':B,
    'nonzero_morse_boundary_entries':69,
    'minor_order9_rows':rows9, 'minor_order9_columns':cols9,
    'minor_order9_determinant':minor9,
    'minor_order10_rows':list(range(10)),
    'minor_order10_columns':cols10,
    'minor_order10_determinant':minor10,
    'original_boundary_ranks_mod2':mod2_rank,
    'original_betti_mod2':[1,0,1,21,0,0,0,0,0,0],
    'integral_morse_Smith_invariants':[1]*9+[2],
    'integral_homology':{'degree_0':'Z','degree_2':'Z/2','degree_3':'Z^20','else':'0'},
    'homotopy_type':'Moore(Z/2,2) wedge 20 S^3'
}
if len(sys.argv)==3 and sys.argv[1]=='--emit-certificate':
    Path(sys.argv[2]).write_text(json.dumps(certificate,sort_keys=True,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
elif len(sys.argv)!=1:
    raise SystemExit('usage: python3 verify_dodecahedral_pm.py [--emit-certificate PATH]')
print('Perfect matchings:',len(perfect),'Faces:',len(faces),'Hasse incidences:',cover_count)
print('Morse pairs:',len(low_to_high),'critical:',{d:len(c) for d,c in critical.items() if c})
print('Integer minors:',minor9,minor10,'Original mod2 ranks:',mod2_rank)
print('DODECAHEDRON_PERFECT_MATCHING_MOORE_2_TORSION_20_S3_OK')
