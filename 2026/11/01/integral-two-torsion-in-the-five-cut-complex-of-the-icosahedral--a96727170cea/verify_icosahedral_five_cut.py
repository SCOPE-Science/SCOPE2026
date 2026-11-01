#!/usr/bin/env python3
"""Exact integral homology certificate for the five-cut complex of the icosahedron.

Requires Python 3.10+ and SymPy (for exact integer Smith normal form).
All finite graphs, face decisions and chain complexes are generated here.
"""
import itertools
import json
from collections import Counter, defaultdict, deque
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

EDGES = [(0,1),(0,5),(0,7),(0,8),(0,11),
 (1,2),(1,5),(1,6),(1,8),(2,3),(2,6),(2,8),(2,9),
 (3,4),(3,6),(3,9),(3,10),(4,5),(4,6),(4,10),(4,11),
 (5,6),(5,11),(7,8),(7,9),(7,10),(7,11),(8,9),(9,10),(10,11)]
N=12; FULL=(1<<N)-1
adj=[0]*N
for a,b in EDGES:
    assert 0<=a<b<N
    adj[a]|=1<<b;adj[b]|=1<<a
assert len(EDGES)==30 and all(x.bit_count()==5 for x in adj)
assert len({(a,b) for a,b in EDGES})==30
# Distinct vertex-neighborhoods and 20 triangular faces characterize the standard graph.
assert len(set(adj))==N
assert sum(bool(adj[a]>>b&1 and adj[a]>>c&1 and adj[b]>>c&1)
    for a,b,c in itertools.combinations(range(N),3))==20


def connected_bits(mask):
    reached=mask&-mask
    while True:
        step=reached
        for i in range(N):
            if reached>>i&1:step |= adj[i]&mask
        if step==reached:return reached==mask
        reached=step


def connected_dfs(t):
    allowed=set(t); seen={t[0]};todo=[t[0]]
    while todo:
        v=todo.pop()
        for w in allowed:
            if w not in seen and (adj[v]>>w)&1:
                seen.add(w);todo.append(w)
    return len(seen)==len(t)


five=list(itertools.combinations(range(N),5))
Bad=[sum(1<<i for i in s) for s in five
     if not connected_bits(sum(1<<i for i in s))]
assert len(Bad)==300
# Method 1: generate all faces from the 300 maximal facets.
faces1={0}
for bad in Bad:
    facet=FULL^bad
    t=facet
    while t:
        faces1.add(t);t=(t-1)&facet
# Method 2: do not use the precomputed bad sets; enumerate candidates directly.
faces2=set()
for mask in range(1<<N):
    comp=[i for i in range(N) if not(mask>>i&1)]
    if any(not connected_dfs(t) for t in itertools.combinations(comp,5)):
        faces2.add(mask)
assert faces1==faces2
faces=faces1
fv={str(d):sum(s.bit_count()-1==d for s in faces) for d in range(-1,7)}
assert fv=={'-1':1,'0':12,'1':66,'2':220,'3':495,'4':792,'5':732,'6':300}


def mod2rank(columns):
    piv={}
    for x in columns:
        while x:
            i=x.bit_length()-1
            if i not in piv:piv[i]=x;break
            x^=piv[i]
    return len(piv)


def direct_mod2_ranks():
    by={d:sorted(s for s in faces if s.bit_count()==d+1) for d in range(7)}
    r={}
    for d in range(1,7):
        rowindex={s:i for i,s in enumerate(by[d-1])}
        cols=[]
        for face in by[d]:
            bit=0
            for v in range(N):
                if face>>v&1:bit^=1<<rowindex[face^(1<<v)]
            cols.append(bit)
        r[d]=mod2rank(cols)
    # Relative to F2 the ranks imply reduced Betti numbers 1,1,30 in degrees 4,5,6.
    assert r=={1:11,2:55,3:165,4:330,5:461,6:270},r
    return r


def matching(order):
    unpaired=set(faces)-{0};pairs=[]
    stage=[]
    for v in order:
        p=[(s,s|(1<<v)) for s in sorted(unpaired)
           if not(s>>v&1) and (s|(1<<v)) in unpaired]
        for a,b in p:unpaired.remove(a);unpaired.remove(b)
        pairs.extend(p);stage.append(len(p))
    assert sum(stage)==len(pairs)
    mate={a:b for a,b in pairs}
    indeg={s:0 for s in faces if s}
    adjdir=defaultdict(list);hasses=0
    for s in indeg:
        for v in range(N):
            if s>>v&1:
                t=s^(1<<v)
                if not t:continue
                a,b=(t,s) if mate.get(t)==s else (s,t)
                adjdir[a].append(b);indeg[b]+=1;hasses+=1
    q=deque(s for s,d in indeg.items() if d==0);visited=0
    while q:
        x=q.popleft();visited+=1
        for y in adjdir[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert visited==len(faces)-1 and hasses==13224
    return pairs,unpaired,stage,hasses


def cancel(pairs,critical):
    # Every original column is the oriented simplicial boundary, omitting empty face.
    chain={s:{} for s in faces if s}
    for s in chain:
        idx=0
        for v in range(N):
            if s>>v&1:
                t=s^(1<<v)
                if t:chain[s][t]=1 if idx%2==0 else -1
                idx+=1
    rev=defaultdict(set)
    for s,d in chain.items():
        for t in d:rev[t].add(s)
    for low,high in pairs:
        c=chain[high].get(low)
        assert c in (-1,1),('non-unit pivot',low,high,c)
        for col in list(rev[low]):
            if col==high:continue
            e=chain[col].get(low,0)
            if not e:continue
            for row,val in list(chain[high].items()):
                new=chain[col].get(row,0)-e*c*val
                if new:chain[col][row]=new;rev[row].add(col)
                else:
                    if row in chain[col]:del chain[col][row]
                    rev[row].discard(col)
        for row in list(chain[high]):rev[row].discard(high)
        for col in list(rev[high]):chain[col].pop(high,None)
        for row in list(chain[low]):rev[row].discard(low)
        del rev[high];del rev[low];del chain[high];del chain[low]
    assert set(chain)==critical
    for s,bd in chain.items():
        assert all(t in critical and t.bit_count()==s.bit_count()-1 for t in bd)
        twice=defaultdict(int)
        for t,a in bd.items():
            for u,b in chain[t].items():twice[u]+=a*b
        assert all(x==0 for x in twice.values())
    by={d:sorted(s for s in critical if s.bit_count()-1==d) for d in range(7)}
    mats={}
    for d in (5,6):
        mats[d]=Matrix([[chain[c].get(low,0) for c in by[d]] for low in by[d-1]])
    return by,mats


def invariants(A):
    B=smith_normal_form(A,domain=ZZ)
    inv=[abs(int(B[i,i])) for i in range(min(B.shape)) if B[i,i]]
    return inv


def verify_one(order):
    pairs,critical,stage,hasses=matching(order)
    by,mats=cancel(pairs,critical)
    d5,d6=mats[5],mats[6]
    assert d5*d6==Matrix.zeros(d5.rows,d6.cols)
    assert invariants(d5)==[1,1,1,1,2]
    assert invariants(d6)==[1]*(len(by[5])-5)
    assert len(by[4])==5 and len(by[6])-len(by[5])+5==30
    return {
      'matching_pairs':len(pairs),
      'stage_pair_counts':stage,
      'critical_cells':{str(d):len(s) for d,s in by.items() if s},
      'hasse_incidences_checked':hasses,
      'Morse_d5_shape':[d5.rows,d5.cols],
      'Morse_d5_nonzero_smith_factors':invariants(d5),
      'Morse_d6_shape':[d6.rows,d6.cols],
      'Morse_d6_nonzero_smith_factors':invariants(d6),
      'Morse_d5_dense':[[int(d5[i,j]) for j in range(d5.cols)] for i in range(d5.rows)],
      'Morse_d6_dense':[[int(d6[i,j]) for j in range(d6.cols)] for i in range(d6.rows)]
    }


def main():
    mod2=direct_mod2_ranks()
    forward=verify_one(list(range(N)))
    reverse=verify_one(list(reversed(range(N))))
    assert forward['matching_pairs']==1286 and reverse['matching_pairs']==1285
    print(json.dumps({'graph_vertices':N,'graph_edges':len(EDGES),
       'disconnected_five_subsets':len(Bad),'facets':len(Bad),
       'total_faces_including_empty':len(faces),'f_vector':fv,
       'full_simplicial_mod2_boundary_ranks':mod2,
       'forward':forward,'reverse':reverse,
       'reduced_integral_homology':{'degree_4':'Z/2','degree_6':'Z^30','else':'0'},
       'status':'ICOSAHEDRAL_FIVE_CUT_INTEGRAL_TORSION_EXACT_VERIFIED'},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
