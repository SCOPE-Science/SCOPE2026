#!/usr/bin/env python3
"""Check topology of independence complexes of two classical strongly regular graphs.
Only Python standard library is required; no external data is used.
"""
from collections import Counter,deque
from itertools import combinations

N=16

def graph(kind):
    a=[0]*N
    steps={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    for i in range(4):
        for j in range(4):
            u=4*i+j
            for x in range(4):
                for y in range(4):
                    v=4*x+y
                    adjacent=((x-i)%4,(y-j)%4) in steps if kind=='shri' else ((i==x or j==y) and u!=v)
                    if adjacent:a[u]|=1<<v
    for u in range(N):
        assert (a[u]>>u)&1==0
        assert a[u].bit_count()==6
        for v in range(N):
            assert bool(a[u]>>v&1)==bool(a[v]>>u&1)
            if u!=v:assert (a[u]&a[v]).bit_count()==2
    return a

def simplices(a):
    faces={0}
    for f in range(1,1<<N):
        v=(f&-f).bit_length()-1
        rest=f^(1<<v)
        if rest in faces and not (rest&a[v]):faces.add(f)
    return faces

def match(faces,order):
    unmatched=faces-{0}
    pairs=[]
    for v in order:
        bit=1<<v
        for face in sorted(unmatched,key=lambda x:(x.bit_count(),x)):
            larger=face|bit
            if not face&bit and face in unmatched and larger in unmatched:
                unmatched.remove(face);unmatched.remove(larger)
                pairs.append((face,larger))
    return pairs,unmatched

def check_acyclic(faces,pairs):
    # Orient every codimension-one cover from higher to lower,
    # except matched covers which point from lower to higher.
    matchset=set(pairs); edges=[]; deg={f:0 for f in faces if f}
    outs={f:[] for f in deg}
    for f in faces:
        if not f:continue
        for v in range(N):
            if f>>v&1:
                g=f^(1<<v)
                if not g:continue
                lo,hi=(g,f)
                a,b=(lo,hi) if (lo,hi) in matchset else (hi,lo)
                outs[a].append(b);deg[b]+=1
                edges.append((a,b))
    q=deque(sorted(f for f,d in deg.items() if d==0));processed=0
    while q:
        u=q.popleft();processed+=1
        for v in outs[u]:
            deg[v]-=1
            if deg[v]==0:q.append(v)
    assert processed==len(deg), (processed,len(deg))
    return len(edges),processed

def boundary_ranks(faces):
    buckets={k:sorted(f for f in faces if f.bit_count()==k) for k in range(1,5)}
    ranks={}
    for k in range(2,5):
        rows={f:i for i,f in enumerate(buckets[k-1])}
        basis={}
        for f in buckets[k]:
            col=0
            for v in range(N):
                if f>>v&1:col^=1<<rows[f^(1<<v)]
            while col:
                p=col.bit_length()-1
                if p in basis:col^=basis[p]
                else:basis[p]=col;break
        ranks[k]=len(basis)
    # Ordinary boundary C1->C0 rank ncomponents-1,
    # via mod-two elimination of edge incidence columns.
    basis={};rows={f:i for i,f in enumerate(buckets[1])}
    for f in buckets[2]:
        col=0
        for v in range(N):
            if f>>v&1:col^=1<<rows[f^(1<<v)]
        while col:
            p=col.bit_length()-1
            if p in basis:col^=basis[p]
            else:basis[p]=col;break
    ranks[2]=len(basis)
    # simplicial boundary C_0 -> 0; C_1 -> C_0 is ranks[2]
    # for reduced homology, subtract 1 from degree zero.
    dims=[len(buckets[k]) for k in (1,2,3,4)]
    rankC=[0,ranks[2],ranks[3],ranks[4],0]
    betti=[dims[k]-rankC[k]-rankC[k+1] for k in range(4)]
    assert betti[0]==1
    return {i:betti[i] for i in range(4)}

if __name__=='__main__':
    outputs=[]
    for kind in ('shri','rook'):
        a=graph(kind);faces=simplices(a);pairs,critical=match(faces,range(N) if kind=='shri' else [7, 9, 5, 6, 14, 10, 12, 8, 1, 2, 13, 15, 4, 11, 0, 3])
        counts=Counter(f.bit_count()-1 for f in faces if f)
        critical_counts=Counter(f.bit_count()-1 for f in critical)
        arcs,nodes=check_acyclic(faces,pairs)
        betti=boundary_ranks(faces)
        assert counts==({0:16,1:72,2:96,3:16} if kind=='shri' else {0:16,1:72,2:96,3:24})
        assert critical_counts==({0:1,2:23} if kind=='shri' else {0:1,2:15})
        assert betti==({0:1,1:0,2:23,3:0} if kind=='shri' else {0:1,1:0,2:15,3:0})
        assert 2*len(pairs)+len(critical)==len(faces)-1
        outputs.append((kind, counts, len(pairs),critical_counts,arcs,nodes,betti))
    for x in outputs:print(x)
    print('SHRIKHANDE_ROOK_INDEPENDENCE_VERIFY_OK')
