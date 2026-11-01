#!/usr/bin/env python3
"""Exact 12-stage higher-independence computation for the Tietze graph.

No third-party modules. Optional argument: path to a JSON certificate containing
all 12 complete gradient pairings, critical masks and signed Morse matrices.
"""
import json
import sys
from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

N = 12
# Canonical Tietze graph: remove vertex 0 from a Petersen graph, replace it
# by a triangle attached to the former neighbors 1,4,5, and relabel
# the remaining vertices 1,...,12 as bit positions 0,...,11.
ORIGINAL_EDGES = [(1,2),(1,6),(1,10),(2,3),(2,7),(3,4),(3,8),
                  (4,9),(4,11),(5,7),(5,8),(5,12),(6,8),(6,9),
                  (7,9),(10,11),(10,12),(11,12)]
EDGES = [(a-1,b-1) for a,b in ORIGINAL_EDGES]
assert len(EDGES)==len(set(EDGES))==18
adj = [0]*N
for a,b in EDGES:
    assert 0<=a<b<N
    adj[a]|=1<<b
    adj[b]|=1<<a
assert all(a.bit_count()==3 for a in adj)

# Independent membership implementation 1: exhaustive BFS on induced components.
def largest_component(mask):
    remaining=mask
    largest=0
    while remaining:
        queue=[(remaining&-remaining).bit_length()-1]
        comp=0
        while queue:
            v=queue.pop()
            bit=1<<v
            if comp&bit:continue
            comp |= bit
            next_bits=adj[v]&mask&~comp
            while next_bits:
                b=next_bits&-next_bits
                queue.append(b.bit_length()-1)
                next_bits^=b
        largest=max(largest,comp.bit_count())
        remaining &= ~comp
    return largest

# Independent membership implementation 2: brute-force reachability closure.
def largest_component_v2(mask):
    rem=mask
    best=0
    while rem:
        component=rem&-rem
        while True:
            reach=component
            for v in range(N):
                if component>>v&1:reach|=adj[v]&mask
            if reach==component:break
            component=reach
        best=max(best,component.bit_count())
        rem&=~component
    return best

large1=[largest_component(m) for m in range(1<<N)]
large2=[largest_component_v2(m) for m in range(1<<N)]
assert large1==large2
assert large1[0]==0

def signed_faces(cell):
    count=0
    for v in range(N):
        if cell>>v&1:
            face=cell^(1<<v)
            if face:yield (face,-1 if count%2 else 1)
            count+=1

def rank_q(matrix):
    if not matrix or not matrix[0]:return 0
    rows=[[Fraction(v) for v in row] for row in matrix]
    m,n=len(rows),len(rows[0]);rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,m) if rows[i][col]),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        p=rows[rank][col]
        for j in range(col,n):rows[rank][j]/=p
        for i in range(rank+1,m):
            if rows[i][col]:
                c=rows[i][col]
                for j in range(col,n):rows[i][j]-=c*rows[rank][j]
        rank+=1
        if rank==m:break
    return rank

def det_bareiss(mat):
    a=[list(row) for row in mat]
    n=len(a)
    if n==0:return 1
    sign=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def unit_minor(matrix,rank):
    if rank==0:return ([],[],1)
    m,n=len(matrix),len(matrix[0])
    cols=[]
    for col in range(n):
        trial=cols+[col]
        if rank_q([[row[j] for j in trial] for row in matrix])>len(cols):cols.append(col)
        if len(cols)==rank:break
    assert len(cols)==rank
    rows=[]
    for row in range(m):
        trial=rows+[row]
        if rank_q([[matrix[i][j] for j in cols] for i in trial])>len(rows):rows.append(row)
        if len(rows)==rank:break
    assert len(rows)==rank
    d=det_bareiss([[matrix[i][j] for j in cols] for i in rows])
    assert abs(d)==1,(rank,rows,cols,d)
    return rows,cols,d

def rank_mod2(columns):
    pivots={}
    for col in columns:
        while col:
            p=col.bit_length()-1
            if p in pivots:col^=pivots[p]
            else:pivots[p]=col;break
    return len(pivots)

cert=None
if len(sys.argv)>1:
    with open(sys.argv[1],encoding='utf-8') as fp:cert=json.load(fp)
    assert cert['graph_edges_1_based']==[list(x) for x in ORIGINAL_EDGES]
    assert len(cert['cases'])==12

report=[]
for r in range(1,13):
    faces={m for m in range(1,1<<N) if large1[m]<=r}
    assert all(face in faces for cell in faces for face,s in signed_faces(cell))
    live=set(faces);pairs=[]
    for v in range(N):
        bit=1<<v
        for lo in sorted(live):
            hi=lo|bit
            if not lo&bit and hi in live:
                live.remove(lo);live.remove(hi);pairs.append([lo,hi])
    critical=sorted(live)
    mate={}
    for lo,hi in pairs:
        assert hi^lo in (1<<i for i in range(N))
        assert lo not in mate and hi not in mate
        mate[lo]=hi;mate[hi]=lo
    assert set(mate)|set(critical)==faces and not (set(mate)&set(critical))
    out={m:[] for m in faces};indeg={m:0 for m in faces};incidences=0
    for hi in faces:
        for lo,s in signed_faces(hi):
            incidences+=1
            a,b=(lo,hi) if mate.get(lo)==hi else (hi,lo)
            out[a].append(b);indeg[b]+=1
    queue=deque(m for m in faces if indeg[m]==0);seen=0
    while queue:
        m=queue.popleft();seen+=1
        for nxt in out[m]:
            indeg[nxt]-=1
            if indeg[nxt]==0:queue.append(nxt)
    assert seen==len(faces),(r,seen,len(faces))
    dims=Counter(m.bit_count()-1 for m in critical)
    assert dims.get(0)==1 and all(d==0 or d>=2 for d in dims)
    lower={lo:hi for lo,hi in pairs};upper={hi:lo for lo,hi in pairs}
    @lru_cache(None)
    def reduce_face(m):
        if m in live:return {m:1}
        if m in upper:return {}
        hi=lower[m]
        inc=next(s for f,s in signed_faces(hi) if f==m)
        total={}
        for face,s in signed_faces(hi):
            if face==m:continue
            for k,c in reduce_face(face).items():
                total[k]=total.get(k,0)-s*inc*c
        return {k:c for k,c in total.items() if c}
    morse={};rank_bdry={}
    for d in range(1,max(dims)+1):
        cells=[m for m in critical if m.bit_count()-1==d]
        targets=[m for m in critical if m.bit_count()-1==d-1]
        if not cells or not targets:continue
        M=[[sum(s*reduce_face(face).get(target,0) for face,s in signed_faces(cell)) for cell in cells] for target in targets]
        rr=rank_q(M)
        row_idx,col_idx,det=unit_minor(M,rr)
        morse[str(d)]={'matrix':M,'rank':rr,'unit_minor_rows':row_idx,'unit_minor_cols':col_idx,'unit_minor_determinant':det}
        rank_bdry[d]=rr
    reduced_betti={d:dims[d]-rank_bdry.get(d,0)-rank_bdry.get(d+1,0) for d in range(1,max(dims)+1) if dims[d]}
    assert all(b>=0 for b in reduced_betti.values())
    # Independent full simplicial boundary reductions over GF(2).
    by={d:sorted(m for m in faces if m.bit_count()==d+1) for d in range(max(m.bit_count() for m in faces))}
    ranks={}
    for d in range(1,len(by)):
        face_index={m:i for i,m in enumerate(by[d-1])}
        columns=[]
        for m in by[d]:
            bits=0
            for f,s in signed_faces(m):bits^=1<<face_index[f]
            columns.append(bits)
        ranks[d]=rank_mod2(columns)
    betti2={0:len(by[0])-1-ranks.get(1,0)}
    for d in range(1,len(by)):
        betti2[d]=len(by[d])-ranks[d]-ranks.get(d+1,0)
    assert betti2[0]==0
    assert {d:b for d,b in betti2.items() if b}=={d:b for d,b in reduced_betti.items() if b},(r,betti2,reduced_betti)
    assert sum((-1)**d*len(by[d]) for d in by)==1+sum((-1)**d*b for d,b in reduced_betti.items())
    item={'r':r,'face_count':len(faces),'f_vector':[len(by[d]) for d in by],
          'pairs':pairs,'critical_masks':critical,'critical_dimensions':{str(k):v for k,v in sorted(dims.items())},
          'hasse_incidences':incidences,'morse_differentials':morse,
          'reduced_integral_betti':{str(d):b for d,b in reduced_betti.items() if b},
          'mod2_ranks':{str(k):v for k,v in ranks.items()}}
    if cert is not None:
        a=cert['cases'][r-1]
        assert a==item,('saved mismatch',r)
    report.append(item)
    print('r=%02d faces=%d pairs=%d critical=%s beta=%s incidences=%d'%(r,len(faces),len(pairs),dict(sorted(dims.items())),item['reduced_integral_betti'],incidences))

assert [x['reduced_integral_betti'] for x in report]==[
    {'2':2},{'4':3},{'5':1},{'5':1},{'4':6,'5':1},{'5':89},
    {'6':193},{'7':149},{'8':55},{'9':11},{'10':1},{}]
if len(sys.argv)==1:
    with open('/mnt/data/tietze_higher_independence_certificate.json','w',encoding='utf-8') as fp:
        json.dump({'graph_edges_1_based':ORIGINAL_EDGES,'cases':report},fp,separators=(',',':'),ensure_ascii=False)
else:
    print('SAVED_CERTIFICATE_FULL_REPLAY_PASS')
print('TIETZE_COMPLETE_HIGHER_INDEPENDENCE_HOMOTOPY_VERIFIED')
