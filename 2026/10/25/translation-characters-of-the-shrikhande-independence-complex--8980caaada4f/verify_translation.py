#!/usr/bin/env python3
"""Reconstruct finite graph complexes and their integral homotopy and rational translation characters."""
from collections import Counter, deque
from itertools import combinations, permutations
from random import Random

MOD = 4
SIDE = 4
N = 16
SH_STEPS = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
EXPECTED_CHARS = {
    'Shrikhande': ((23,-1,-1,-1),(-1,-1,3,3),(-1,3,-1,3),(-1,3,3,-1)),
    'Rook': ((15,-1,-1,-1),(-1,3,-1,3),(-1,-1,-1,-1),(-1,3,-1,3)),
}
EXPECTED_MULT = {
    'Shrikhande': ((2,1,1,1),(1,2,2,1),(1,2,1,2),(1,1,2,2)),
    'Rook': ((1,1,0,1),(1,1,1,1),(0,1,2,1),(1,1,1,1)),
}

def graph(name):
    adj = [0]*N
    for u in range(N):
        x,y = divmod(u,SIDE)
        for v in range(N):
            if u == v:
                continue
            z,w = divmod(v,SIDE)
            if name == 'Shrikhande':
                edge = ((z-x)%MOD,(w-y)%MOD) in SH_STEPS
            else:
                edge = x==z or y==w
            if edge:
                adj[u] |= 1<<v
    assert all(m.bit_count()==6 for m in adj)
    assert all(not(adj[u]>>u&1) for u in range(N))
    assert all(bool(adj[u]>>v&1)==bool(adj[v]>>u&1) for u in range(N) for v in range(N))
    assert all((adj[u]&adj[v]).bit_count()==2 for u in range(N) for v in range(u+1,N))
    return adj

def independent_faces(adj):
    out=set()
    for mask in range(1,1<<N):
        rest=mask
        independent=True
        while rest:
            bit=rest&-rest
            rest^=bit
            if adj[bit.bit_length()-1] & rest:
                independent=False
                break
        if independent:
            out.add(mask)
    return out

def verify_morse(faces, expected):
    # Repeated elementary collapses or deletion of a current maximal face.
    # Every collapse gives a matched covering pair; maximal deletions are critical.
    active=set(faces)
    rng=Random(0)
    pairs=[]
    critical=[]
    while active:
        free=[]
        for low in sorted(active):
            covers=[low|(1<<v) for v in range(N)
                    if not low>>v&1 and low|(1<<v) in active]
            if len(covers)==1:
                high=covers[0]
                if not any(high|(1<<v) in active for v in range(N) if not high>>v&1):
                    free.append((low,high))
        if free:
            low,high=rng.choice(free)
            active.remove(low)
            active.remove(high)
            pairs.append((low,high))
        else:
            dimension=max(f.bit_count() for f in active)
            f=rng.choice(sorted(x for x in active if x.bit_count()==dimension))
            active.remove(f)
            critical.append(f)
    assert len(pairs)*2+len(critical)==len(faces)
    assert Counter(c.bit_count()-1 for c in critical)==Counter({0:1,2:expected})
    pair_set=set(pairs)
    matched=set()
    for low,high in pairs:
        assert low in faces and high in faces and high.bit_count()==low.bit_count()+1
        assert high & low==low
        assert low not in matched and high not in matched
        matched.add(low)
        matched.add(high)
    assert matched.isdisjoint(critical)
    # Full Hasse-graph acyclicity test; not inferred from greedy procedure.
    indeg={f:0 for f in faces}
    follows={f:[] for f in faces}
    edgecount=0
    for upper in faces:
        for v in range(N):
            if not upper>>v&1:
                continue
            lower=upper^(1<<v)
            if lower not in faces:
                continue
            edgecount+=1
            src,dst=(lower,upper) if (lower,upper) in pair_set else (upper,lower)
            indeg[dst]+=1
            follows[src].append(dst)
    Q=deque(x for x,deg in indeg.items() if deg==0)
    seen=0
    while Q:
        u=Q.popleft()
        seen+=1
        for v in follows[u]:
            indeg[v]-=1
            if indeg[v]==0:Q.append(v)
    assert seen==len(faces)
    return len(pairs),edgecount

def mod2_boundary_ranks(faces):
    groups={d:sorted(f for f in faces if f.bit_count()==d+1) for d in range(4)}
    ranks=[]
    for d in range(1,4):
        rows={f:i for i,f in enumerate(groups[d-1])}
        basis={}
        for upper in groups[d]:
            v=upper
            col=0
            while v:
                b=v&-v;v^=b
                col^=1<<rows[upper^b]
            while col:
                k=col.bit_length()
                if k in basis:col^=basis[k]
                else:
                    basis[k]=col
                    break
        ranks.append(len(basis))
    return tuple(ranks)

def translation(mask,a,b):
    image=[]
    for v in range(N):
        if mask>>v&1:
            x,y=divmod(v,SIDE)
            image.append(4*((x+a)%4)+(y+b)%4)
    newmask=sum(1<<v for v in image)
    inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
    return newmask,(-1)**inversions

def homology_character(faces):
    T={}
    statistics={}
    for a in range(4):
        for b in range(4):
            # Augmented chain complex includes the empty simplex in degree -1.
            trace=-1
            c=Counter()
            for face in faces:
                image,orient=translation(face,a,b)
                if image==face:
                    k=face.bit_count()
                    trace+=(-1)**(k-1)*orient
                    c[(k,orient)]+=1
            T[(a,b)]=trace
            statistics[(a,b)]=c
    return T,statistics

def fourier(T):
    # Exact discrete Fourier transform: fourth roots 1, i, -1, -i.
    roots=(1,1j,-1,-1j)
    mult={}
    for p in range(4):
        for q in range(4):
            total=sum(T[(a,b)]*roots[(-p*a-q*b)%4] for a in range(4) for b in range(4))
            assert abs(total.imag)<1e-9
            z=round(total.real)
            assert z==total.real and z%16==0
            mult[(p,q)]=z//16
            assert mult[(p,q)]>=0
    return mult

def all_cosets_of_shrikhande_maximals():
    directions=((1,2),(1,3),(2,1))
    cosets=set()
    for a,b in directions:
        H={((k*a)%4,(k*b)%4) for k in range(4)}
        assert len(H)==4
        for x in range(4):
            for y in range(4):
                mask=sum(1<<(4*((x+u)%4)+(y+v)%4) for u,v in H)
                cosets.add(mask)
    H2={(0,0),(2,0),(0,2),(2,2)}
    for x in range(4):
        for y in range(4):
            mask=sum(1<<(4*((x+u)%4)+(y+v)%4) for u,v in H2)
            cosets.add(mask)
    assert len(cosets)==16
    return cosets

def main():
    for name,target_betti in (('Shrikhande',23),('Rook',15)):
        adj=graph(name)
        faces=independent_faces(adj)
        fv=tuple(sum(f.bit_count()==k for f in faces) for k in range(1,5))
        assert fv==((16,72,96,16) if name=='Shrikhande' else (16,72,96,24))
        if name=='Shrikhande':
            assert {f for f in faces if f.bit_count()==4}==all_cosets_of_shrikhande_maximals()
        else:
            expected={sum(1<<(4*i+p[i]) for i in range(4)) for p in permutations(range(4))}
            assert {f for f in faces if f.bit_count()==4}==expected
        pairs,arcs=verify_morse(faces,target_betti)
        assert (pairs,arcs)==((88,496) if name=='Shrikhande' else (96,528))
        assert mod2_boundary_ranks(faces)==((15,57,16) if name=='Shrikhande' else (15,57,24))
        T,stats=homology_character(faces)
        M=fourier(T)
        assert tuple(tuple(T[(a,b)] for b in range(4)) for a in range(4))==EXPECTED_CHARS[name]
        assert tuple(tuple(M[(p,q)] for q in range(4)) for p in range(4))==EXPECTED_MULT[name]
        assert sum(M.values())==target_betti
        assert sum(T.values())//16==M[(0,0)]
        assert all((translation(f,a,b)[0] in faces) for f in faces for a in range(4) for b in range(4))
        # Independent check of fixed-simplex counts for all nonzero involutions.
        for a,b in ((2,0),(0,2),(2,2)):
            stat=stats[(a,b)]
            assert stat[(2,-1)]==stat[(4,1)]
        print(name,'faces',fv,'Morse-pairs',pairs,'Hasse-arcs',arcs)
        print('  character',EXPECTED_CHARS[name])
        print('  Fourier multiplicities',EXPECTED_MULT[name])
    print('VERIFY_OK')
if __name__=='__main__':main()
