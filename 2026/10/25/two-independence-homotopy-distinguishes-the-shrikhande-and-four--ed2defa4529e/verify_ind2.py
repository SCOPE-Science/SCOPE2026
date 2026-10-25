#!/usr/bin/env python3
"""Standalone exact verification of two finite 2-independence homotopy types.

Uses integer bitsets only; no external dependencies.
"""
from collections import Counter,deque

ORDERS={
 'rook':(6,13,1,5,9,8,12,0,10,3,4,14,7,2,11,15),
 'shrikhande':(1,5,7,6,3,11,2,4,13,8,15,9,14,10,12,0),
}
EXPECTED={
 'rook':((16,120,384,528,144),105,1192),
 'shrikhande':((16,120,384,544,240,32),57,1336),
}

def adjacency(which):
    adj=[0]*16
    for a in range(16):
        x,y=divmod(a,4)
        for b in range(a+1,16):
            X,Y=divmod(b,4)
            if which=='rook':
                edge=(x==X or y==Y)
            else:
                dx=(X-x)%4;dy=(Y-y)%4
                edge=(dx,dy) in ((1,0),(3,0),(0,1),(0,3),(1,1),(3,3))
            if edge:
                adj[a]|=1<<b
                adj[b]|=1<<a
    assert all(a.bit_count()==6 for a in adj)
    assert sum(a.bit_count() for a in adj)//2==48
    # Verify strongly-regular parameters and distinguish the local graphs.
    for a in range(16):
        for b in range(a+1,16):
            assert (adj[a]&adj[b]).bit_count()==2
    for a in range(16):
        neighborhood=[v for v in range(16) if adj[a]>>v&1]
        local_deg=[(adj[v]&adj[a]).bit_count() for v in neighborhood]
        assert local_deg==[2]*6
        seen={neighborhood[0]};stack=[neighborhood[0]]
        while stack:
            v=stack.pop()
            for w in neighborhood:
                if w not in seen and adj[v]>>w&1:
                    seen.add(w);stack.append(w)
        assert len(seen)==(6 if which=='shrikhande' else 3)
    return adj

def is_face(mask,adj):
    # Directly inspect every connected component of the induced graph.
    unseen=mask
    while unseen:
        start=unseen&-unseen;unseen-=start
        seen=start;frontier=start
        while frontier:
            nxt=0
            work=frontier
            while work:
                v=work&-work;work-=v
                nxt|=adj[v.bit_length()-1]&unseen
            if not nxt:break
            seen|=nxt;unseen&=~nxt;frontier=nxt
            if seen.bit_count()>2:return False
    return True

def enumerate_faces(adj):
    # Recurrence independently derived from the defining component condition.
    good=bytearray(1<<16);good[0]=1
    for m in range(1,1<<16):
        first=m&-m
        i=first.bit_length()-1
        base=m^first
        if not good[base]:continue
        neighbors=adj[i]&base
        if neighbors and (neighbors&(neighbors-1)):continue
        if neighbors:
            j=neighbors.bit_length()-1
            if adj[j]&base:continue
        good[m]=1
    # Independent direct check of all 65,536 vertex subsets.
    assert all(bool(good[m])==is_face(m,adj) for m in range(1<<16))
    return {m for m in range(1,1<<16) if good[m]}

def matching(faces,order):
    assert set(order)==set(range(16))
    remaining=set(faces)
    pairs=[]
    for i in order:
        bit=1<<i
        batch=[(m,m|bit) for m in sorted(remaining)
               if not(m&bit) and (m|bit) in remaining]
        touched=set()
        for a,b in batch:
            assert a in remaining and b in remaining and a not in touched and b not in touched
            assert b.bit_count()==a.bit_count()+1 and b^a==bit
            touched.add(a);touched.add(b)
        remaining-=touched
        pairs+=batch
    assert len(remaining)+2*len(pairs)==len(faces)
    return remaining,pairs

def directed_hasse_acyclic(faces,pairs):
    matched={(a,b) for a,b in pairs}
    indeg={m:0 for m in faces}
    outs={m:[] for m in faces}
    count=0
    for bigger in faces:
        w=bigger
        while w:
            bit=w&-w;w-=bit
            smaller=bigger^bit
            if smaller==0:continue
            assert smaller in faces
            if (smaller,bigger) in matched:
                src,dst=smaller,bigger
            else:
                src,dst=bigger,smaller
            outs[src].append(dst)
            indeg[dst]+=1
            count+=1
    todo=deque(m for m in faces if indeg[m]==0)
    seen=0
    while todo:
        m=todo.popleft();seen+=1
        for b in outs[m]:
            indeg[b]-=1
            if indeg[b]==0:todo.append(b)
    assert seen==len(faces),(seen,len(faces))
    return count

def homology_mod2(faces):
    bydim={d:[] for d in range(6)}
    for m in sorted(faces):bydim[m.bit_count()-1].append(m)
    ranks={}
    for d in range(1,6):
        lower={m:i for i,m in enumerate(bydim[d-1])}
        pivots={};rank=0
        for m in bydim[d]:
            vector=0;v=m
            while v:
                bit=v&-v;v-=bit
                vector^=1<<lower[m^bit]
            while vector:
                high=vector.bit_length()-1
                if high not in pivots:
                    pivots[high]=vector;rank+=1;break
                vector^=pivots[high]
        ranks[d]=rank
    betti={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(6)}
    assert betti[0]==1
    return betti

def verify():
    for name in ('rook','shrikhande'):
        adj=adjacency(name)
        fs=enumerate_faces(adj)
        count=Counter(m.bit_count()-1 for m in fs)
        assert tuple(count[k] for k in range(max(count)+1))==EXPECTED[name][0]
        crit,pairs=matching(fs,ORDERS[name])
        c=Counter(m.bit_count()-1 for m in crit)
        assert c=={0:1,3:EXPECTED[name][1]},c
        relations=directed_hasse_acyclic(fs,pairs)
        betti=homology_mod2(fs)
        assert betti[3]==EXPECTED[name][1]
        assert all(v==0 for i,v in betti.items() if i not in (0,3))
        assert len(fs)==EXPECTED[name][2]
        print(f'{name}: faces={len(fs)} f_vector={EXPECTED[name][0]} match_pairs={len(pairs)} critical={dict(c)} hasse_relations={relations} mod2_betti={betti}')
    print('VERIFY_OK')
if __name__=='__main__':verify()
