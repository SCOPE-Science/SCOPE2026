#!/usr/bin/env python3
"""Independent finite checks for clique-bouquet clique-avoidance homotopy and symmetry characters.
Run with Python 3; no third-party libraries required.
"""
from itertools import product, permutations, combinations
from math import comb
from collections import defaultdict


def valid(mask, blockbits, apex, t):
    v = int(bool(mask & (1 << apex)))
    return all((mask & b).bit_count() + v <= t-1 for b in blockbits)


def faces_by_dimension(sizes, t):
    n = 1 + sum(sizes)
    apex = n - 1
    blockbits=[]
    st=0
    for a in sizes:
        blockbits.append(((1<<a)-1)<<st)
        st+=a
    block_index={j:i for i,b in enumerate(blockbits) for j in range(n-1) if b>>j&1}
    def adjacent(u,v):
        return u==apex or v==apex or block_index[u]==block_index[v]
    prohibited=[]
    for vs in combinations(range(n),t):
        if all(adjacent(u,v) for u,v in combinations(vs,2)):
            prohibited.append(sum(1<<i for i in vs))
    fs=defaultdict(list)
    for mask in range(1, 1<<n):
        by_graph=not any((mask & forbidden)==forbidden for forbidden in prohibited)
        by_quota=valid(mask,blockbits,apex,t)
        assert by_graph==by_quota,(n,sizes,t,mask)
        if by_graph:
            fs[mask.bit_count()-1].append(mask)
    return fs


def rank_mod2(cols):
    pivots={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in pivots:
                x^=pivots[p]
            else:
                pivots[p]=x
                break
    return len(pivots)


def betti_mod2(fs):
    dims=sorted(fs)
    count={d:len(fs[d]) for d in dims}
    ranks={}
    for d in dims:
        if d==0:continue
        rows={f:i for i,f in enumerate(fs[d-1])}
        columns=[]
        for f in fs[d]:
            x=0
            for j in range(f.bit_length()):
                if f>>j&1:
                    x ^= 1<<rows[f^(1<<j)]
            columns.append(x)
        ranks[d]=rank_mod2(columns)
    raw={d:count[d]-ranks.get(d,0)-ranks.get(d+1,0) for d in dims}
    raw[0]-=1
    return {k:v for k,v in raw.items() if v}


def expected(sizes,t):
    r=len(sizes)
    top=1
    bottom=1
    for a in sizes:
        top*=comb(a-1,t-1)
        bottom*=comb(a-1,t-2)
    return {d:m for d,m in ((r*(t-1)-1,top),(r*(t-2),bottom)) if m}


def cycle_lengths(p):
    seen=set();lens=[]
    for i in range(len(p)):
        if i in seen:continue
        j=i; ell=0
        while j not in seen:
            seen.add(j);ell+=1;j=p[j]
        lens.append(ell)
    return lens


def exterior_augmentation_trace(p,k):
    if k >= len(p):
        return 0
    # det(I+z p | U) = prod_cycles (1-(-z)^length)/(1+z)
    poly=[1]+[0]*len(p)
    for ell in cycle_lengths(p):
        coef=(-1)**(ell+1)
        nxt=[0]*len(poly)
        for i,c in enumerate(poly):
            nxt[i]+=c
            if i+ell<len(nxt):nxt[i+ell]+=coef*c
        poly=nxt
    out=[0]*len(poly)
    for i,c in enumerate(poly):out[i]=c-(out[i-1] if i else 0)
    return out[k]


def permutation_sign_on_face(old_indices,new_indices):
    inds={x:i for i,x in enumerate(old_indices)}
    dest=[inds[x] for x in new_indices]
    inv=sum(dest[i]>dest[j] for i in range(len(dest)) for j in range(i+1,len(dest)))
    return -1 if inv%2 else 1


def signed_lefschetz(fs,perm):
    total=0
    for d,flist in fs.items():
        for mask in flist:
            old=[i for i in range(len(perm)) if mask>>i&1]
            targets=[perm[i] for i in old]
            if sorted(targets)!=old:continue
            total+=(-1)**d*permutation_sign_on_face(old,targets)
    return total


def predicted_lefschetz(sizes,t,group_perms):
    r=len(sizes)
    top=1; bottom=1
    for p in group_perms:
        top*=exterior_augmentation_trace(p,t-1)
        bottom*=exterior_augmentation_trace(p,t-2)
    dtop=r*(t-1)-1
    dlow=r*(t-2)
    return 1+(-1)**dtop*top+(-1)**dlow*bottom


def full_perm(sizes,group_perms):
    out=[];start=0
    for a,p in zip(sizes,group_perms):
        assert len(p)==a
        out.extend(start+i for i in p)
        start+=a
    out.append(start)
    return tuple(out)


def main():
    cases=[
        ((2,2),3),((2,3),3),((3,3),3),((4,3),3),((5,2),3),
        ((3,3,3),3),((2,3,3),3),((2,2,4),3),((2,2,2,2),3),
        ((3,3),4),((3,4),4),((4,4),4),((5,3),4),((3,3,3),4),
        ((4,4),5),((4,5),5),((5,5),5),
        ((1,3),3),((2,1,4),3),((2,4),4),
        ((1,2,3),4),((3,5),5),((2,2,2),4),
    ]
    face_total=0; char_total=0
    for sizes,t in cases:
        fs=faces_by_dimension(sizes,t)
        nfaces=sum(len(a) for a in fs.values())
        face_total+=nfaces
        observed=betti_mod2(fs)
        want=expected(sizes,t)
        assert observed==want, (sizes,t,nfaces,observed,want)
        groups=[]
        for a in sizes:
            ident=tuple(range(a))
            swap=tuple((1 if i==0 else (0 if i==1 else i)) for i in range(a)) if a>=2 else ident
            cyclic=tuple((i+1)%a for i in range(a))
            groups.append(list(dict.fromkeys([ident,swap,cyclic])))
        for perms in product(*groups):
            actual=signed_lefschetz(fs,full_perm(sizes,perms))
            expect=predicted_lefschetz(sizes,t,perms)
            assert actual==expect, (sizes,t,perms,actual,expect)
            char_total+=1
        print(f"PASS r={len(sizes)} t={t} sizes={sizes} faces={nfaces} reduced_Betti={observed}")
    print(f"PASS CASES={len(cases)} FACES={face_total} SIGNED_LEFSCHETZ={char_total}")
    print("VERIFY_OK")

if __name__=='__main__': main()
