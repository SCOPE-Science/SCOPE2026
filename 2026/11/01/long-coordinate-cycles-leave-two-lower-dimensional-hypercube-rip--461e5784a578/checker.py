#!/usr/bin/env python3
"""Finite exact checks for cyclic-coordinate fixed Rips orbit models."""
from itertools import combinations
from math import comb

def rot(a,k):
    return ((a << 1) & ((1 << k) - 1)) | (a >> (k - 1))

def orbit(a,k):
    seq={a}; b=rot(a,k)
    while b not in seq:
        seq.add(b); b=rot(b,k)
    return frozenset(seq)

def diff(a,b):
    return (a^b).bit_count()

def test(k,f):
    seen=set(); verts=[]
    for y in range(1<<f):
        for z in range(1<<k):
            O=orbit(z,k)
            if (y,O) in seen: continue
            seen.add((y,O))
            if all(diff(a,b)<=2 for a,b in combinations(O,2)):
                verts.append((y,O))
    assert len(verts)==4*(1<<f), (k,f,len(verts))
    def typ(O):
        w=next(iter(O)).bit_count()
        if w==0:return 'A'
        if w==k:return 'B'
        if w==1:return 'C'
        if w==k-1:return 'D'
        raise AssertionError((k,f,'unexpected orbit',O))
    assert sorted({typ(O) for y,O in verts}) == list('ABCD')
    edges=set()
    for i,j in combinations(range(len(verts)),2):
        y,O=verts[i]; z,P=verts[j]
        if all(diff(a,b)+diff(y,z)<=2 for a in O for b in P):
            edges.add((i,j))
        t,u=typ(O),typ(P)
        want = ((t==u=='A' or t==u=='B') and diff(y,z)<=2)
        want |= (t=='A' and u=='C' or t=='C' and u=='A' or t=='B' and u=='D' or t=='D' and u=='B') and diff(y,z)<=1
        assert ((i,j) in edges)==bool(want),(k,f,i,j,t,u,diff(y,z),((i,j) in edges),want)
    for i,(y,O) in enumerate(verts):
        if typ(O) not in ('C','D'): continue
        partner='A' if typ(O)=='C' else 'B'
        j=next(j for j,(z,P) in enumerate(verts) if z==y and typ(P)==partner)
        ni={v for v in range(len(verts)) if v==i or (min(i,v),max(i,v)) in edges}
        nj={v for v in range(len(verts)) if v==j or (min(j,v),max(j,v)) in edges}
        assert ni <= nj,(k,f,i,j)
    return len(verts),len(edges)

if __name__=='__main__':
    count=0; vcount=ecount=0
    for k in range(4,9):
        for f in range(5):
            v,e=test(k,f)
            count+=1;vcount+=v;ecount+=e
    for k,f in [(9,2),(10,1),(11,0)]:
        v,e=test(k,f);count+=1;vcount+=v;ecount+=e
    print('PASS',count,'parameter instances,',vcount,'admissible orbit vertices,',ecount,'orbit compatibility edges')
    print('Predicted each fixed component collapses to VR_<=2(Q_f); f=0,1,2 contractible, f>=3 wedge of c_f three-spheres.')
    print('c_3..c_7:',[sum(2**j*comb(j+3,3) for j in range(f-2)) for f in range(3,8)])
