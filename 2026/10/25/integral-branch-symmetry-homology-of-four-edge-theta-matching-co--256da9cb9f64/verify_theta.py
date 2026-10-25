#!/usr/bin/env python3
"""Finite checks for matching complexes of four-edge multipath theta graphs.

Uses only Python's standard library. None of the finite tests replaces the
infinite-family proof based on an explicit simplicial collapse and a relative
homology calculation.
"""
from collections import defaultdict
from itertools import permutations


def graph_edges(m):
    # u = 0, v = 1; each branch has new vertices a_i,b_i,c_i.
    ed = []
    for layer in range(4):
        for i in range(m):
            a,b,c = 2+3*i, 3+3*i, 4+3*i
            ed.append([(0,a),(a,b),(b,c),(c,1)][layer])
    return ed


def enumerated_matching_faces(m):
    e=graph_edges(m)
    faces=[]
    def recurse(k,occupied,mask):
        if k==len(e):
            faces.append(mask)
            return
        recurse(k+1,occupied,mask)
        u,v=e[k]
        if u not in occupied and v not in occupied:
            recurse(k+1,occupied|{u,v},mask|(1<<k))
    recurse(0,set(),0)
    return set(faces)


def structural_faces(m):
    # Global end edges A_i and D_j are separately mutually incompatible.
    # For fixed choices a,d, the middle pair B_i,C_i has at most one member.
    result=[]
    for a in [-1]+list(range(m)):
        for d in [-1]+list(range(m)):
            opts=[]
            for i in range(m):
                if i==a and i==d:
                    choices=[0]
                elif i==a:
                    choices=[0,1<<(2*m+i)]
                elif i==d:
                    choices=[0,1<<(m+i)]
                else:
                    choices=[0,1<<(m+i),1<<(2*m+i)]
                opts.append(choices)
            base=(1<<a if a>=0 else 0)|(1<<(3*m+d) if d>=0 else 0)
            def rec(k,mask):
                if k==m:
                    result.append(mask)
                    return
                for item in opts[k]:
                    rec(k+1,mask|item)
            rec(0,base)
    return set(result)


def endpoints(m,mask):
    a=mask&((1<<m)-1)
    d=(mask>>(3*m))&((1<<m)-1)
    return (a.bit_length()-1 if a else -1, d.bit_length()-1 if d else -1)


def check_collapse(m,faces):
    alive=set(faces)
    # Cross-endpoint faces form an upward-closed collection. Every such
    # face without C_i is paired with the face obtained by adding C_i.
    bases=[]
    for mask in faces:
        i,j=endpoints(m,mask)
        if i>=0 and j>=0 and i!=j and not (mask>>(2*m+i)&1):
            bases.append((mask,i))
    bases.sort(key=lambda x:x[0].bit_count(),reverse=True)
    for mask,i in bases:
        up=mask|(1<<(2*m+i))
        assert mask in alive and up in alive
        immediate=[mask|(1<<v) for v in range(4*m)
                   if not(mask>>v&1) and (mask|(1<<v)) in alive]
        assert immediate == [up], (m,mask,immediate,up)
        alive.remove(mask)
        alive.remove(up)
    assert all((lambda x: x[0]<0 or x[1]<0 or x[0]==x[1])(endpoints(m,s)) for s in alive)
    assert len(faces)-len(alive)==2*len(bases)
    return len(bases),len(alive)


def mod2_betti(faces):
    bydim=defaultdict(list)
    for mask in faces:
        bydim[mask.bit_count()-1].append(mask)
    ranks={}
    for k in sorted(bydim,reverse=True):
        if k<=0:
            continue
        rows={mask:i for i,mask in enumerate(bydim[k-1])}
        piv={}
        for mask in bydim[k]:
            col=0;x=mask
            while x:
                b=x&-x;x-=b
                col^=(1<<rows[mask^b])
            while col:
                r=col.bit_length()-1
                if r in piv:col^=piv[r]
                else:piv[r]=col;break
        ranks[k]=len(piv)
    return {k:len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0)
            for k in bydim if k>=0 and len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0)}


def sign(p):
    return (-1)**sum(p[a]>p[b] for a in range(len(p)) for b in range(a+1,len(p)))


def homology_character(m,perm,reverse,faces):
    # Signed simplicial fixed-simplex Lefschetz trace, including empty face.
    image=[((3-layer) if reverse else layer)*m+perm[i]
           for layer in range(4) for i in range(m)]
    lefschetz=0
    for mask in faces:
        old=[];x=mask
        while x:
            b=x&-x;x-=b
            old.append(b.bit_length()-1)
        new=[image[v] for v in old]
        if set(old)!=set(new):continue
        orientation=(-1)**sum(new[a]>new[b] for a in range(len(new)) for b in range(a+1,len(new)))
        lefschetz+=(-1)**(len(old)-1)*orientation
    return (-1)**m*lefschetz


def main():
    checks=0
    for m in range(2,8):
        faces=enumerated_matching_faces(m)
        structural=structural_faces(m)
        assert faces==structural, (m,len(faces),len(structural))
        betti=mod2_betti(faces)
        assert betti=={0:1,m:m-1},(m,betti)
        pairs,remaining=check_collapse(m,faces)
        assert remaining>0
        if m<=5:
            all_perms=list(permutations(range(m)))
        else:
            all_perms=[tuple(range(m)),tuple(reversed(range(m))),
                       tuple([1,0]+list(range(2,m))),tuple(list(range(1,m))+[0])]
        for perm in all_perms:
            for reverse in (False,True):
                expected=sign(perm)*((-1)**(m*reverse))*(sum(i==perm[i] for i in range(m))-1)
                observed=homology_character(m,perm,reverse,faces)
                assert observed==expected,(m,perm,reverse,expected,observed)
                checks+=1
        print(f'm={m} faces={len(faces)} collapse_pairs={pairs} residual_faces={remaining} '
              f'betti={betti} signed_action_checks={2*len(all_perms)}')
    print(f'REPRODUCIBLE_CHECKS_OK total_signed_action_checks={checks}')

if __name__=='__main__':main()
