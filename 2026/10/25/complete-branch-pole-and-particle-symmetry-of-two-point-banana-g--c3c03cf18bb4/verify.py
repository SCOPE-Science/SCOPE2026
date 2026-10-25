"""Exact finite checks of two-particle banana-graph cellular characters.

Graph with m paths p-a_i-b_i-q. All calculations use integer signs.
This program checks, but does not substitute for, the universal proof.
"""
from itertools import permutations,combinations
from math import comb

def cells(m):
    vertices=range(2+2*m)
    edges=[]
    for i in range(m):
        a,b=2+2*i,3+2*i
        edges.extend([(0,a),(a,b),(b,1)])
    v0=[(u,v) for u in vertices for v in vertices if u!=v]
    v1=[]
    for k,(a,b) in enumerate(edges):
        for v in vertices:
            if v!=a and v!=b:
                v1.extend([(k,v,0),(k,v,1)])
    v2=[(i,j) for i,e in enumerate(edges) for j,f in enumerate(edges) if not set(e).intersection(f)]
    return edges,v0,v1,v2

def relabel_vertex(v,p,h):
    if v<2: return 1-v if h else v
    i=(v-2)//2; typ=(v-2)%2
    return 2+2*p[i]+(1-typ if h else typ)

def direct_traces(m,p,h,b):
    e,z,o,t=cells(m)
    e_id={tuple(sorted(a)):i for i,a in enumerate(e)}
    def perm_v(v):return relabel_vertex(v,p,h)
    def perm_e(k):
        u,v=e[k];return e_id[tuple(sorted((perm_v(u),perm_v(v))))]
    eperm=[perm_e(k) for k in range(len(e))]
    tr0=0
    for u,v in z:
        w=(perm_v(v),perm_v(u)) if b else (perm_v(u),perm_v(v))
        if w==(u,v):tr0+=1
    tr1=0
    for k,v,side in o:
        w=(eperm[k],perm_v(v),1-side if b else side)
        if w==(k,v,side): tr1+=(-1 if h else 1)
    tr2=0
    for k,l in t:
        w=(eperm[l],eperm[k]) if b else (eperm[k],eperm[l])
        if w==(k,l):tr2+=(-1 if b else 1) # pole reverses BOTH edges
    return tr0,tr1,tr2

def verify():
    total=0
    for m in range(3,7):
        group=list(permutations(range(m)))
        if m==6: group=[group[j] for j in [0,1,2,3,7,12,20,30,61,89,100,120,250,319,400,500,600,701]]
        for p in group:
            f=sum(i==p[i] for i in range(m))
            t=sum(i<p[i] and p[p[i]]==i for i in range(m))
            for h in (0,1):
                for b in (0,1):
                    tr0,tr1,tr2=direct_traces(m,p,h,b)
                    pred=((f*(f-1)-1) if not b else (1-2*t))*(-1 if h else 1)
                    calc=1-tr0+tr1-tr2
                    assert calc==pred,(m,p,h,b,calc,pred,(tr0,tr1,tr2))
                    total+=1
    print('BANANA_TWO_POINT_EQUIVARIANT_CHARACTERS_VERIFIED',total)

if __name__=='__main__': verify()

def _gf2_rank(columns):
    pivots={}
    for column in columns:
        while column:
            pivot=column.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=column
                break
            column^=pivots[pivot]
    return len(pivots)

def verify_boundary_ranks():
    for m in range(3,7):
        edges,z,o,t=cells(m)
        edgeverts=set(range(2+2*m))
        index0={a:j for j,a in enumerate(z)}
        index1={a:j for j,a in enumerate(o)}
        one_columns=[]
        for k,v,side in o:
            a,b=edges[k]
            chain= ((a,v),(b,v)) if not side else ((v,a),(v,b))
            one_columns.append((1<<index0[chain[0]])^(1<<index0[chain[1]]))
        two_columns=[]
        for k,l in t:
            a,b=edges[k];c,d=edges[l]
            face_indices=[index1[(k,c,0)],index1[(k,d,0)],
                          index1[(l,a,1)],index1[(l,b,1)]]
            two_columns.append(sum(1<<j for j in face_indices))
        rank1=_gf2_rank(one_columns)
        rank2=_gf2_rank(two_columns)
        assert rank1==len(z)-1,(m,'connectivity',rank1,len(z))
        assert rank2==len(t),(m,'second_boundary_injectivity',rank2,len(t))
        assert len(o)-rank1-rank2==m*(m-1)-1
    print('BANANA_TWO_POINT_BOUNDARIES_VERIFIED m_3_to_6')

if __name__=='__main__':
    verify_boundary_ranks()
