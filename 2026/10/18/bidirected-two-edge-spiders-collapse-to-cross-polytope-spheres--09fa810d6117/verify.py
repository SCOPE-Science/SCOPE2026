#!/usr/bin/env python3
"""Finite certificate for the bidirected two-edge spider multipath collapse.
Uses no third-party modules. This file is research/reproducibility material.
"""
from collections import deque, Counter
from math import factorial


def sign_of_permutation(p):
    inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inversions % 2 else 1


def verify(n):
    # Vertex labels: root 0, intermediates 1..n, leaves n+1..2n.
    # Arc order per arm: A_i=root->mid; B_i=mid->root;
    # C_i=mid->leaf; D_i=leaf->mid.
    arcs=[]
    for i in range(n):
        m=1+i; w=1+n+i
        arcs.extend([(0,m),(m,0),(m,w),(w,m)])
    size=len(arcs)
    clash=[0]*size
    for i,(u,v) in enumerate(arcs):
        for j,(x,y) in enumerate(arcs):
            if i!=j and (u==x or v==y or (u==y and v==x)):
                clash[i] |= 1<<j
    faces=[]
    def rec(pos,mask):
        if pos==size:
            faces.append(mask)
            return
        rec(pos+1,mask)
        if not (clash[pos]&mask):
            rec(pos+1,mask|(1<<pos))
    rec(0,0)
    face_set=set(faces)
    assert len(face_set)==len(faces)
    # Independent symbolic enumeration by the number of selected center arcs.
    # Polynomial coefficients of (1+2t)^n + 2nt(1+t)(1+2t)^(n-1)
    # + n(n-1)t^2(1+t)^2(1+2t)^(n-2).
    from math import comb
    poly=[0]*(4*n+1)
    for k in range(n+1):
        poly[k]+=comb(n,k)*2**k
    for k in range(n):
        for j in (0,1):
            poly[1+k+j]+=2*n*comb(n-1,k)*2**k
    if n>=2:
        for k in range(n-1):
            for j,coef in enumerate((1,2,1)):
                poly[2+k+j]+=n*(n-1)*comb(n-2,k)*2**k*coef
    actual=Counter(mask.bit_count() for mask in faces)
    assert all(actual[k]==poly[k] for k in range(len(poly)))
    assert sum(poly)==3**n+4*n*3**(n-1)+(4*n*(n-1)*3**(n-2) if n>=2 else 0)
    # Confirm exclusion of directed cycles (the underlying graph is a tree;
    # all possible directed cycles have length two).
    for mask in faces:
        selected=[arcs[i] for i in range(size) if mask>>i&1]
        for u,v in selected:
            assert (v,u) not in selected
        for v in range(2*n+1):
            assert sum(u==v for u,w in selected)<=1
            assert sum(w==v for u,w in selected)<=1

    inner_mask=sum((1<<(4*i))|(1<<(4*i+1)) for i in range(n))
    B={mask for mask in faces if not mask&inner_mask}
    assert len(B)==3**n  # join of n two-vertex sets, augmented face included
    pairs={}
    for mask in faces:
        inside=mask&inner_mask
        if not inside:
            continue
        # First center arc determines a compatible outer arc: A_i->C_i, B_i->D_i.
        pivot=(inside&-inside).bit_length()-1
        target=pivot+2
        assert target<size
        assert not ((mask^ (1<<target)) & (clash[target]) if mask>>target&1 else mask&clash[target])
        if mask>>target&1:
            continue
        upper=mask|(1<<target)
        assert upper in face_set
        assert upper not in pairs
        pairs[mask]=upper
    expected=(len(faces)-len(B))//2
    assert len(pairs)==expected
    matched=set(pairs)|set(pairs.values())
    assert len(matched)==2*expected and matched==face_set-B
    # Exhaustive directed Hasse diagram: matched covers point up,
    # every other cover points down.
    indeg={mask:0 for mask in faces}
    out={mask:[] for mask in faces}
    edge_count=0
    for upper in faces:
        s=upper
        while s:
            bit=s&-s
            lower=upper^bit
            assert lower in face_set
            if pairs.get(lower)==upper:
                frm,to=lower,upper
            else:
                frm,to=upper,lower
            out[frm].append(to)
            indeg[to]+=1
            edge_count+=1
            s^=bit
    q=deque(mask for mask in faces if indeg[mask]==0)
    seen=0
    while q:
        mask=q.popleft();seen+=1
        for other in out[mask]:
            indeg[other]-=1
            if indeg[other]==0:q.append(other)
    assert seen==len(faces), (n,seen,len(faces))
    # Explicit integral fundamental cycle on the outer join.
    # Each top simplex chooses one outer arc per arm.
    z={}
    for x in range(1<<n):
        vs=[4*i+(3 if x>>i&1 else 2) for i in range(n)]
        assert len(set(vs))==n
        mask=sum(1<<v for v in vs)
        assert mask in B
        z[tuple(vs)]=(-1)**x.bit_count()
    bd=Counter()
    for tup,coeff in z.items():
        for j in range(n):
            face=tup[:j]+tup[j+1:]
            bd[face]+=coeff*((-1)**j)
    assert all(v==0 for v in bd.values())
    # Check branch transposition and the global arc reversal on this cycle.
    if n>=2:
        perm=tuple([1,0]+list(range(2,n)))
        acted=Counter()
        for tup,coeff in z.items():
            tw=[4*perm[v//4]+v%4 for v in tup]
            parity=sign_of_permutation(tw)
            acted[tuple(sorted(tw))]+=parity*coeff
        assert all(acted[k]==-z[k] for k in z)
    if n>=3:
        perm=tuple([1,2,0]+list(range(3,n)))
        acted=Counter()
        for tup,coeff in z.items():
            tw=[4*perm[v//4]+v%4 for v in tup]
            parity=sign_of_permutation(tw)
            acted[tuple(sorted(tw))]+=parity*coeff
        assert all(acted[k]==z[k] for k in z)
    acted=Counter()
    for tup,coeff in z.items():
        tw=[v^1 for v in tup]  # outer arc C_i <-> D_i
        acted[tuple(tw)]+=coeff
    assert all(acted[k]==(-1)**n*z[k] for k in z)
    print(f'n={n} faces_including_empty={len(faces)} B={len(B)} matched_pairs={len(pairs)} covers={edge_count} topo_sorted={seen} sphere_dimension={n-1} parity_branch={-1 if n>=2 else 'NA'} parity_reversal={(-1)**n}')


if __name__=='__main__':
    for n in range(1,8):
        verify(n)
    print('VERIFY_OK n=1..7; all faces, cover orientations, cycles, and symmetry checks')
