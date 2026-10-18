#!/usr/bin/env python3
"""Independent finite checks for equal-cycle fixed-point directed-forest complexes.

Run: python3 verify_equal_cycle_fixed.py
Only Python's standard library is needed.
"""
from itertools import product
from collections import defaultdict
from math import comb

def is_acyclic(parent):
    n=len(parent)
    for v in range(n):
        seen=set();u=v
        while u>=0:
            if u in seen: return False
            seen.add(u);u=parent[u]
    return True

def colored_faces(k,d):
    # An arc (u,v) has d independent choices of phase.
    edges=[(u,v,h) for v in range(k) for u in range(k) if u!=v for h in range(d)]
    index={e:i for i,e in enumerate(edges)}
    choice=[[( -1,-1)]+[(u,h) for u in range(k) if u!=v for h in range(d)] for v in range(k)]
    faces=defaultdict(set)
    for selection in product(*choice):
        parent=tuple(u for u,h in selection)
        if not is_acyclic(parent): continue
        f=tuple(sorted(index[(u,v,h)] for v,(u,h) in enumerate(selection) if u!=-1))
        faces[len(f)].add(f)
    return edges,faces

def rank_mod2(rows):
    pivots={};rank=0
    for r in rows:
        while r:
            pivot=r.bit_length()-1
            if pivot in pivots: r^=pivots[pivot]
            else:
                pivots[pivot]=r;rank+=1;break
    return rank

def betti_mod2(faces):
    # Reduced augmented chain ranks; empty simplex has dimension -1.
    maxsz=max(faces)
    ranks={0:1 if faces.get(1) else 0}
    for z in range(2,maxsz+1):
        old={f:i for i,f in enumerate(sorted(faces[z-1]))}
        columns=[]
        for f in faces[z]:
            mask=0
            for j in range(z): mask ^=1<<old[f[:j]+f[j+1:]]
            columns.append(mask)
        ranks[z-1]=rank_mod2(columns)
    return {z-1:len(faces[z])-ranks.get(z-1,0)-ranks.get(z,0)
            for z in range(1,maxsz+1) if len(faces[z])-ranks.get(z-1,0)-ranks.get(z,0)}

def orbit_fixed_faces(k,d):
    m=k*d
    # g maps position a in every equal-length block to a+1 mod d.
    perm=tuple(i//d*d+(i+1)%d for i in range(m))
    arc_orbits={};groups=[]
    for child in range(m):
        for parent in range(m):
            if parent==child or (parent,child) in arc_orbits:continue
            orbit=[];a,b=parent,child
            while (a,b) not in orbit:
                orbit.append((a,b));a,b=perm[a],perm[b]
            if (a,b)!=(parent,child): raise AssertionError('orbit collision')
            ix=len(groups)
            for e in orbit:arc_orbits[e]=ix
            groups.append(tuple(orbit))
    faces=defaultdict(set)
    for p in product(range(-1,m),repeat=m):
        if any(p[v]==v for v in range(m)):continue
        if not is_acyclic(p):continue
        if any(p[perm[v]]!=(perm[p[v]] if p[v]>=0 else -1) for v in range(m)):continue
        ids=tuple(sorted({arc_orbits[(p[v],v)] for v in range(m) if p[v]>=0}))
        faces[len(ids)].add(ids)
    return groups,faces

def simple_profile(faces):return tuple(len(faces.get(i,())) for i in range(max(faces)+1))

def main():
    checks=0
    for k,d in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3)]:
        edges,faces=colored_faces(k,d)
        f=simple_profile(faces)
        # All-forest alternating face sum includes the empty face.
        signed=sum((-1)**z*len(faces[z]) for z in faces)
        target=(1-k*d)**(k-1)
        assert signed==target,(k,d,signed,target)
        assert max(faces)==k-1
        if k<=4 and d<=2 or (k==3 and d==3):
            betti=betti_mod2(faces)
            assert betti=={k-2:(k*d-1)**(k-1)},(k,d,betti)
        print('COLORED',k,d,'face_numbers',f,'signed',signed,'expected_top_rank',(k*d-1)**(k-1))
        checks+=1
    # Independently enumerate *original* invariant forests, without using quotient-colored rules.
    for k,d in [(2,2),(3,2)]:
        arcs,check=colored_faces(k,d)
        original_orbits,actual=orbit_fixed_faces(k,d)
        assert simple_profile(check)==simple_profile(actual),(k,d,simple_profile(check),simple_profile(actual))
        print('DIRECT_FIXED',k,d,'orbit_arc_count',len(original_orbits),'invariant_face_numbers',simple_profile(actual))
        checks+=1
    print('VERIFY_OK',checks)
if __name__=='__main__':main()
