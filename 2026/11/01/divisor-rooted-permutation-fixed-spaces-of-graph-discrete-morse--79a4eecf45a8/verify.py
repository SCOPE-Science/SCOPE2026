#!/usr/bin/env python3
"""Finite independent checks of divisor-rooted fixed-forest homotopy formulas.

Requires only Python 3 standard library. The computation enumerates original directed
edge orbits under vertex permutations, not a preconstructed quotient multidigraph.
Finite checks corroborate, but do not establish, the unrestricted theorem.
"""
from itertools import combinations
from math import prod
from collections import Counter

CASES = [(1,2),(2,4),(2,4,6),(2,4,8),(2,2,4),(2,4,4),
         (3,3,6),(3,6,9),(2,2,2,4),(2,2,4,4),(1,2,4),
         (1,1,4),(1,2,2,4),(2,2,6)]


def perm_and_blocks(lengths):
    p=[]; blocks=[]
    for d in lengths:
        start=len(p); block=list(range(start,start+d)); blocks.append(block)
        p.extend(block[1:]+block[:1])
    return p, blocks


def forest(arcs,n):
    targets={}
    for s,t in arcs:
        if s in targets and targets[s]!=t:
            return False
        targets[s]=t
    if len(targets)!=len(arcs):
        return False
    for s in targets:
        seen=set();v=s
        while v in targets:
            if v in seen: return False
            seen.add(v);v=targets[v]
    return True


def original_orbits(p):
    n=len(p); pending={(i,j) for i in range(n) for j in range(n) if i!=j}
    good=[]
    while pending:
        a=min(pending); orbit=[];edge=a
        while edge not in orbit:
            orbit.append(edge)
            pending.remove(edge)
            edge=(p[edge[0]],p[edge[1]])
        if forest(orbit,n): good.append(tuple(orbit))
    return good


def mod2_rank(cols):
    pivots={}
    for col in cols:
        x=col
        while x:
            b=x.bit_length()-1
            if b in pivots: x ^= pivots[b]
            else:
                pivots[b]=x;break
    return len(pivots)


def homology(faces):
    ranks={}
    for k in range(1,len(faces)):
        prev={f:i for i,f in enumerate(faces[k-1])}
        cols=[]
        for face in faces[k]:
            mask=0
            for i in range(len(face)):
                sub=face[:i]+face[i+1:]
                mask ^= 1<<prev[sub]
            cols.append(mask)
        ranks[k]=mod2_rank(cols)
    out={}
    for k in range(len(faces)):
        rk=ranks.get(k,0);rk_next=ranks.get(k+1,0)
        val=len(faces[k])-rk-rk_next-(1 if k==0 else 0)
        if val: out[k]=val
    return out


def predicted(lengths):
    mult=Counter(lengths); size=sum(mult.values())
    poly=[1]
    for d in sorted(mult):
        m=mult[d]; L=sum(e*c for e,c in mult.items() if e!=d and d%e==0)
        for alpha in [L]+[L+d*m]*(m-1):
            nxt=[0]*(len(poly)+1)
            for j,v in enumerate(poly):nxt[j]+=v;nxt[j+1]+=alpha*v
            poly=nxt
    while len(poly)>1 and poly[-1]==0: poly.pop()
    B=abs(sum((-1)**j*c for j,c in enumerate(poly)))
    return poly,B,size-2


def test(lengths):
    p,blocks=perm_and_blocks(lengths)
    n=len(p);orbits=original_orbits(p)
    vertex_to_block={v:i for i,b in enumerate(blocks) for v in b}
    directed=Counter()
    for orbit in orbits:
        a,b=orbit[0]; directed[(vertex_to_block[a],vertex_to_block[b])]+=1
    for i,A in enumerate(blocks):
        for j,B in enumerate(blocks):
            want=len(B) if i!=j and len(A)%len(B)==0 else 0
            assert directed[(i,j)]==want, (lengths,i,j,directed[(i,j)],want)
    c=len(blocks)
    faces=[]
    for k in range(1,c):
        here=[]
        for selected in combinations(range(len(orbits)),k):
            arcs=[arc for o in selected for arc in orbits[o]]
            good=forest(arcs,n)
            # Independently check orbit-quotient criterion.
            selected_pairs=[(vertex_to_block[o[0][0]],vertex_to_block[o[0][1]]) for o in (orbits[i] for i in selected)]
            quotient_good=forest(selected_pairs,c)
            assert good==quotient_good,(lengths,selected,good,quotient_good)
            if good:here.append(selected)
        faces.append(here)
    poly,B,dim=predicted(lengths)
    assert len(poly)==c
    assert [len(f) for f in faces]==poly[1:],(lengths,[len(f) for f in faces],poly)
    betti=homology(faces)
    assert betti==({dim:B} if B else {}),(lengths,betti,dim,B)
    print('PASS',lengths, 'n=',n,'orbit_vertices=',len(orbits),
          'f_vector=',[len(f) for f in faces],'reduced_F2_betti=',betti,
          'predicted_wedge=',B, 'dim=',dim)

if __name__=='__main__':
    for case in CASES:test(case)
    print('VERIFY_OK',len(CASES),'cases')
