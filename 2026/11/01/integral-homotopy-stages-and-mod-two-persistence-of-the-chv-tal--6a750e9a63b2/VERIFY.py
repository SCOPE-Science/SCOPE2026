#!/usr/bin/env python3
"""Exact finite combinatorial verification for the Chvatal higher-independence filtration.
Run: python3 VERIFY.py (standard-library only). All orientations use increasing vertex labels.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import hashlib
import json

N = 12
EDGES = ((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
         (2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
         (5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11))
NEIGH = [0]*N
for u,v in EDGES:
    assert u<v and 0<=u and v<N
    NEIGH[u] |= 1<<v
    NEIGH[v] |= 1<<u
assert len(EDGES)==24 and all(x.bit_count()==4 for x in NEIGH)
assert not any((NEIGH[i]&NEIGH[j]) for i,j in EDGES)  # triangle-free


def exact_coloring(k):
    colors=[-1]*N
    searched=0
    def dfs():
        nonlocal searched
        searched+=1
        uncolored=[v for v in range(N) if colors[v]<0]
        if not uncolored:return tuple(colors)
        v=max(uncolored,key=lambda x:(len({colors[u] for u in range(N)
                                 if NEIGH[x]>>u&1 and colors[u]>=0}),4,-x))
        for color in range(k):
            if all(colors[u]!=color for u in range(N) if NEIGH[v]>>u&1):
                colors[v]=color
                answer=dfs()
                if answer is not None:return answer
                colors[v]=-1
        return None
    return dfs(),searched


def maximal_component_size(mask):
    rest=mask; largest=0
    while rest:
        seed=rest & -rest
        comp=front=seed
        while front:
            bit=front & -front
            front ^= bit
            v=bit.bit_length()-1
            nxt=NEIGH[v]&mask&~comp
            comp |= nxt
            front |= nxt
        largest=max(largest, comp.bit_count())
        rest &= ~comp
    return largest

LEVEL=[max(1,maximal_component_size(m)) for m in range(1<<N)]
assert LEVEL[0]==1 and LEVEL[(1<<N)-1]==12
assert LEVEL==[max(1,maximal_component_size(m)) for m in range(1<<N)]

# Independently check vertex connectivity: deleting <=3 vertices stays connected,
# while the displayed four-vertex deletion disconnects the graph.
FULL=(1<<N)-1
for removed_count in (1,2,3):
    for deleted in combinations(range(N),removed_count):
        remaining=FULL ^ sum(1<<v for v in deleted)
        assert maximal_component_size(remaining)==N-removed_count
assert maximal_component_size(FULL ^ sum(1<<v for v in (0,2,5,7))) < 8


def boundary(s):
    """Integer simplicial boundary of an oriented increasing-label simplex."""
    return [(s^(1<<v), (-1)**j) for j,v in
            enumerate(v for v in range(N) if s & (1<<v))]


def matching_for(r):
    faces={m for m in range(1<<N) if LEVEL[m]<=r}
    left=set(faces)
    pairs=[]
    for v in range(N):
        for a in sorted(left):
            b=a|(1<<v)
            if not (a&(1<<v)) and a in left and b in left:
                left.remove(a);left.remove(b)
                pairs.append((a,b))
    return faces,pairs,left


def check_acyclic(faces,pairs):
    """Full Hasse-diagram topological sort, matched cover edges reversed."""
    up=dict(pairs)
    indeg={m:0 for m in faces}
    out={m:[] for m in faces}
    hasse=0
    for b in faces:
        for a,_ in boundary(b):
            if a not in faces:
                assert a == 0 and 0 not in faces
                continue
            # Reverse edge a<b if it is matched. Otherwise b->a.
            u,v=(a,b) if up.get(a)==b else (b,a)
            out[u].append(v)
            indeg[v]+=1
            hasse+=1
    q=deque(m for m in faces if indeg[m]==0)
    covered=0
    while q:
        m=q.popleft();covered+=1
        for nxt in out[m]:
            indeg[nxt]-=1
            if indeg[nxt]==0:q.append(nxt)
    assert covered==len(faces), ('cycle',covered,len(faces))
    return hasse


def morse_matrix(j,pairs,critical):
    """Exact gradient-path differential critical dimension j -> j-1."""
    up=dict(pairs)
    down={b:a for a,b in pairs}
    @lru_cache(None)
    def project(a):
        if a in critical:return {a:1}
        if a in down:return {}
        if a not in up:raise AssertionError(('unclassified',a))
        b=up[a]
        inc=next(c for x,c in boundary(b) if x==a)
        ans=defaultdict(int)
        for t,c in boundary(b):
            if t==a:continue
            for x,z in project(t).items():
                ans[x]-=inc*c*z
        return {x:z for x,z in ans.items() if z}
    cols=sorted(x for x in critical if x.bit_count()==j+1)
    rows=sorted(x for x in critical if x.bit_count()==j)
    if not cols or not rows:return rows,cols,[]
    result=[]
    for b in cols:
        ans=defaultdict(int)
        for a,c in boundary(b):
            for x,z in project(a).items():ans[x]+=c*z
        result.append([ans[x] for x in rows])
    return rows,cols,[[result[c][r] for c in range(len(cols))] for r in range(len(rows))]


def determinant(M):
    """Exact determinant, Bareiss fraction-free elimination with row swaps."""
    size=len(M)
    if size==0:return 1
    a=[list(x) for x in M]
    assert all(len(row)==size for row in a)
    sign=1;prev=1
    for k in range(size-1):
        if a[k][k]==0:
            pivot=next((t for t in range(k+1,size) if a[t][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        val=a[k][k]
        for i in range(k+1,size):
            for j in range(k+1,size):
                val2=a[i][j]*val-a[i][k]*a[k][j]
                assert val2%prev==0
                a[i][j]=val2//prev
        for i in range(k+1,size):a[i][k]=0
        prev=val
    return sign*a[-1][-1]

# Rows/columns of explicit unimodular minors, derived from exact matrices.
MINORS={
 (2,3):([0,1,2],[0,1,2],-1),
 (3,3):([0,1,2],[0,1,2],-1),
 (3,4):([0],[0],-1),
 (4,4):([1,8,10,12,14,16,18,26],list(range(8)),-1),
 (5,5):([3,14,31,43,121],list(range(5)),-1),
}
EXPECTED_CRITICAL={
 1:{2:1},2:{2:3,3:4},3:{2:3,3:5,4:1},4:{3:72,4:8},
 5:{4:257,5:5},6:{5:382},7:{6:318},8:{7:165},
 9:{8:55},10:{9:11},11:{10:1},12:{},
}
EXPECTED_FACES={1:127,2:425,3:729,4:1176,5:1804,6:2590,
                7:3314,8:3797,9:4017,10:4083,11:4095,12:4096}


def f2_barcode():
    """Independent ordinary simplicial mod-two persistent boundary reduction."""
    simplices=sorted(range(1,1<<N),key=lambda a:(LEVEL[a],a.bit_count(),a))
    position={m:i for i,m in enumerate(simplices)}
    pivot_cols={};zero_cols=set();bars=[]
    for i,s in enumerate(simplices):
        b=0
        for t,_ in boundary(s):
            if t:b ^=1<<position[t]
        while b:
            p=b.bit_length()-1
            if p not in pivot_cols:break
            b ^=pivot_cols[p]
        if b:
            p=b.bit_length()-1
            pivot_cols[p]=b
            birth=LEVEL[simplices[p]]
            death=LEVEL[s]
            dim=simplices[p].bit_count()-1
            bars.append((dim,birth,death))
        else:zero_cols.add(i)
    # omit zero-length bars; the final H_0 class is infinite
    positive=Counter(x for x in bars if x[1]<x[2])
    infin=[(simplices[i].bit_count()-1,LEVEL[simplices[i]]) for i in zero_cols if i not in pivot_cols]
    return positive,infin

EXPECTED_BARS={
 (2,1,2):1,(3,2,5):1,(3,4,5):63,(4,5,6):252,
 (5,6,7):382,(6,7,8):318,(7,8,9):165,(8,9,10):55,
 (9,10,11):11,(10,11,12):1,
}


def main():
    col3,three_nodes=exact_coloring(3)
    col4,four_nodes=exact_coloring(4)
    assert col3 is None and col4==(0,1,0,1,2,0,1,0,1,2,3,3)
    totals={'hasse':0,'matching_pairs':0,'faces_across_levels':0}
    matrices={}

    details=[]
    for r in range(1,13):
        faces,pairs,crit=matching_for(r)
        assert len(faces)==EXPECTED_FACES[r]
        observed=dict(sorted(Counter(m.bit_count()-1 for m in crit).items()))
        assert observed==EXPECTED_CRITICAL[r]
        assert len(pairs)*2+len(crit)==len(faces)
        incidence_count=check_acyclic(faces,pairs)
        # The empty face is paired with vertex 0; deleting this pair yields
        # an ordinary acyclic matching with one critical base vertex.
        assert (0,1) in pairs
        assert check_acyclic(faces-{0}, [(a,b) for a,b in pairs if a != 0]) == incidence_count-N
        D={}
        for j in range(1,N):
            rows,cols,M=morse_matrix(j,pairs,crit)
            if not M:continue
            D[j]=M
            matrices[f'{r},{j}']=hashlib.sha256(json.dumps(M,separators=(',',':')).encode()).hexdigest()
            if (r,j) in MINORS:
                ir,ic,want=MINORS[(r,j)]
                minor=[[M[t][u] for u in ic] for t in ir]
                assert determinant(minor)==want
            else:
                assert not any(z for row in M for z in row)
        for j,M in D.items():
            if j+1 not in D:continue
            Nxt=D[j+1]
            assert len(M[0])==len(Nxt)
            assert all(sum(M[a][b]*Nxt[b][c] for b in range(len(Nxt)))==0
                       for a in range(len(M)) for c in range(len(Nxt[0])))
        details.append({'r':r,'face_count':len(faces),'pairs':len(pairs),
                        'critical':{str(i):x for i,x in observed.items()},
                        'hasse_incidences':incidence_count})
        totals['faces_across_levels']+=len(faces)
        totals['matching_pairs']+=len(pairs)
        totals['hasse']+=incidence_count
    bars,inf=f2_barcode()
    assert bars==Counter(EXPECTED_BARS)
    assert inf==[(0,1)]
    assert set(MINORS)=={(2,3),(3,3),(3,4),(4,4),(5,5)}
    print('CHVATAL_HIGHER_INDEPENDENCE_FILTRATION_VERIFIED')
    print('CHROMATIC_EXACT', json.dumps({'no_three_coloring_nodes':three_nodes,
                                        'four_coloring_nodes':four_nodes,
                                        'four_coloring':col4},sort_keys=True))
    print('MORSE_MATRIX_SHA256',json.dumps(matrices,sort_keys=True))

    print('GRAPH 12 vertices 24 edges triangle_free 4_regular graph6=KhdLA_hc?L_y')
    print('VERTEX_CONNECTIVITY_EXACT 4')
    print('TOTALS',json.dumps(totals,sort_keys=True))
    print('MORSE_LEVELS',json.dumps(details,sort_keys=True,separators=(',',':')))
    print('UNIT_MINORS',json.dumps({f'{r},{j}':{'rows':x,'columns':y,'determinant':z}
                                    for (r,j),(x,y,z) in MINORS.items()},sort_keys=True))
    print('F2_PERSISTENCE_BARS',json.dumps({f'{d},{a},{b}':k for (d,a,b),k in sorted(bars.items())},sort_keys=True))
    print('F2_PERSISTENCE_INFINITY',inf)

if __name__=='__main__':main()
