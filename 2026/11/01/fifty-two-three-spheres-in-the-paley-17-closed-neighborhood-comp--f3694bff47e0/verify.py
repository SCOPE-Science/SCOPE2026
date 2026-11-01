#!/usr/bin/env python3
"""Reconstruct the integral homotopy certificate for the Paley-17 closed-neighborhood complex.

Standard-library-only exact computation; run: python3 verify.py
"""
from collections import Counter, deque
from itertools import combinations
from hashlib import sha256

P = 17
PIVOTS = (5,1,10,3,9,12,14,15,8,16,6,4,2,0,11,13,7)
F_VECTOR = (17,136,680,1734,2074,1428,612,153,17)


def construct():
    qr = {i*i % P for i in range(1,P)}
    assert qr == {1,2,4,8,9,13,15,16}
    adj = [set((v+s) % P for s in qr) for v in range(P)]
    assert all(len(x)==8 for x in adj)
    for u in range(P):
        for v in range(u+1,P):
            assert len(adj[u]&adj[v]) == (3 if v in adj[u] else 4)
    neighborhood_masks = [sum(1<<w for w in (adj[v]|{v})) for v in range(P)]
    assert all(m.bit_count()==9 for m in neighborhood_masks)
    faces = set()
    for nbr in neighborhood_masks:
        vs = [j for j in range(P) if nbr & (1<<j)]
        for k in range(1,10):
            for c in combinations(vs,k):
                faces.add(sum(1<<j for j in c))
    # Independent brute-force membership check, all 2^17 subsets.
    assert faces == {m for m in range(1,1<<P)
                     if any(m & n == m for n in neighborhood_masks)}
    assert tuple(sum(m.bit_count()==k+1 for m in faces) for k in range(9)) == F_VECTOR
    assert len(faces) == 6851
    print('FACES_OK',F_VECTOR,'simplices',len(faces))
    return faces


def match(faces):
    rem=set(faces); paired={}
    for v in PIVOTS:
        bit=1<<v
        for low in sorted(rem):
            high=low|bit
            if not (low&bit) and low in rem and high in rem:
                paired[low]=high
                rem.remove(low);rem.remove(high)
    assert len(paired)==3399
    assert len(rem)==53
    assert Counter(m.bit_count()-1 for m in rem)=={0:1,3:52}
    assert all(l in faces and h in faces and l&h==l and h.bit_count()==l.bit_count()+1
               for l,h in paired.items())
    print('MATCHING_OK','pairs',len(paired),'critical',dict(Counter(m.bit_count()-1 for m in rem)))
    return paired,rem


def check_acyclic(faces,paired):
    indeg={m:0 for m in faces}
    out={m:[] for m in faces}
    incidence=0
    for high in faces:
        x=high
        while x:
            bit=x&-x
            low=high^bit
            if low: # omit incidences with the empty simplex
                if paired.get(low)==high:
                    a,b=low,high
                else:
                    a,b=high,low
                out[a].append(b);indeg[b]+=1
                incidence+=1
            x-=bit
    queue=deque(v for v in faces if indeg[v]==0)
    count=0
    while queue:
        u=queue.popleft();count+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0:queue.append(v)
    assert count==len(faces),f'acyclicity failure: visited {count}/{len(faces)}'
    print('ACYCLIC_OK','nodes',count,'incidences',incidence)
    return incidence


def mod2_ranks(faces):
    layers={k:sorted(f for f in faces if f.bit_count()==k+1) for k in range(9)}
    ranks={}
    for k in range(1,9):
        index={x:i for i,x in enumerate(layers[k-1])}
        basis={}
        for high in layers[k]:
            v=0
            t=high
            while t:
                bit=t&-t
                v ^= 1 << index[high^bit]
                t-=bit
            while v:
                pivot=v.bit_length()-1
                if pivot in basis:v^=basis[pivot]
                else:
                    basis[pivot]=v
                    break
        ranks[k]=len(basis)
    betti={k:len(layers[k])-ranks.get(k,0)-ranks.get(k+1,0)-(k==0) for k in range(9)}
    assert betti=={k: (52 if k==3 else 0) for k in range(9)},betti
    print('RAW_MOD2_OK','ranks',ranks,'reduced_betti',betti)


def main():
    assert len(PIVOTS)==P and set(PIVOTS)==set(range(P))
    faces=construct()
    pairs,critical=match(faces)
    check_acyclic(faces,pairs)
    mod2_ranks(faces)
    # Forman's integral CW theorem: only one 0-cell and 52 three-cells.
    # Hence all higher differentials and attaching maps are trivial.
    assert len([f for f in critical if f.bit_count()==1])==1
    assert len([f for f in critical if f.bit_count()==4])==52
    print('HOMOTOPY_OK wedge_of_52_3_spheres')
    print('ALL_VERIFY_OK')

if __name__=='__main__':main()
