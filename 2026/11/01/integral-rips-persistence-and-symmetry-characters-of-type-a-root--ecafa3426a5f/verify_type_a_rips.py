#!/usr/bin/env python3
"""Finite checks for Euclidean Rips complexes on type-A root sets.
All indexing and computations are exact integers/modulo two; no network or packages.
The proof for every n is mathematical, not inferred from this finite test.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial


def faces(n, stage):
    # Stages 1 and 2: row/column cliques, and source-target cut cliques.
    verts=[(i,j) for i in range(n) for j in range(n) if i!=j]
    maximal=[]
    if stage==1:
        maximal.extend(tuple(k for k,v in enumerate(verts) if v[0]==i) for i in range(n))
        maximal.extend(tuple(k for k,v in enumerate(verts) if v[1]==i) for i in range(n))
    elif stage==2:
        for mask in range(1,(1<<n)-1):
            maximal.append(tuple(k for k,(i,j) in enumerate(verts)
                                 if (mask & (1<<i)) and not(mask & (1<<j))))
    else:
        raise ValueError(stage)
    fs={frozenset()}
    for f in maximal:
        for q in range(1,len(f)+1):
            fs.update(map(frozenset,combinations(f,q)))
    return verts, [sorted((tuple(sorted(f)) for f in fs if len(f)==q+1))
                   for q in range(max(map(len,fs)))]


def rank2(cols):
    pivots={}
    for col in cols:
        x=col
        while x:
            p=x.bit_length()-1
            if p in pivots:x^=pivots[p]
            else:
                pivots[p]=x
                break
    return len(pivots)


def betti2(bydim):
    ranks=[0]*(len(bydim)+1)
    for q in range(1,len(bydim)):
        lower={v:i for i,v in enumerate(bydim[q-1])}
        cols=[]
        for face in bydim[q]:
            val=0
            for k in range(q+1):val^=1<<lower[face[:k]+face[k+1:]]
            cols.append(val)
        ranks[q]=rank2(cols)
    b=[len(bydim[q])-ranks[q]-ranks[q+1] for q in range(len(bydim))]
    return b, ranks


def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1


def face_trace(verts, bydim, p):
    index={v:i for i,v in enumerate(verts)}
    perm=[index[p[i],p[j]] for i,j in verts]
    answer=0
    for q,fs in enumerate(bydim):
        for f in fs:
            im=[perm[v] for v in f]
            if sorted(im)!=list(f):continue
            sign=parity([f.index(v) for v in im])
            answer+=(-1)**q * sign
    return answer


def verify(n, with_char):
    print('n=',n,'ordered-roots=',n*(n-1),'unordered-antipodes=',comb(n,2))
    roots=[(i,j) for i in range(n) for j in range(n) if i!=j]
    dist=set()
    for a,b in combinations(roots,2):
        v=sum(((a[0]==k)-(a[1]==k)-(b[0]==k)+(b[1]==k))**2 for k in range(n))
        dist.add(v)
    assert dist=={2,4,6,8},dist
    print('squared_distances=',sorted(dist))
    for stage in (1,2):
        verts, fs=faces(n,stage)
        b,r=betti2(fs)
        target= [0]*len(b)
        if stage==1:
            target[1]=n*n-3*n+1
        else:
            target[n-2]=1
        assert b==[1]+target[1:],(stage,b,target)
        print('stage=',stage,'fvector=',[len(c) for c in fs],
              'boundary_ranks_F2=',r[1:len(fs)],'Betti_F2=',b)
        if with_char:
            for p in permutations(range(n)):
                f=sum(p[i]==i for i in range(n))
                L=face_trace(verts,fs,p)
                expected=(1-(f*f-3*f+1)) if stage==1 else 1+(-1)**(n-2)*parity(p)
                assert L==expected,(stage,p,L,expected)
            print('stage=',stage,'equivariant_Lefschetz_checks=',factorial(n))
    assert comb(n,2)>n-2
    print('stage_3=join_of',comb(n,2),'zero_spheres; sphere_dimension=',comb(n,2)-1)
    print('stage_3_character=sign_power',n-1)

if __name__=='__main__':
    for n in (4,5,6): verify(n,n<=5)
    print('TYPE_A_RIPS_CHECKS_OK')
