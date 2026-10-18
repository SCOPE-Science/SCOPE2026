#!/usr/bin/env python3
"""Direct finite verification of directed sunlet multipath complexes."""
from itertools import product
from collections import Counter

def arcs(n, orient):
    assert n >= 3 and len(orient)==n
    # core vertices 0..n-1; distinct leaves n..2n-1
    es = [(i,(i+1)%n) for i in range(n)]
    es += [(i,n+i) if orient[i] else (n+i,i) for i in range(n)]
    return es

def direct_faces(n, orient):
    es=arcs(n,orient); faces=[]
    for mask in range(1<<(2*n)):
        selected=[es[i] for i in range(2*n) if mask>>i & 1]
        outgoing=[u for u,v in selected]; incoming=[v for u,v in selected]
        if len(set(outgoing))<len(outgoing) or len(set(incoming))<len(incoming):
            continue
        # detect directed cycles by tracing selected successor arcs
        nxt=dict(selected); cyclic=False
        for start in nxt:
            v=start; seen=set()
            while v in nxt:
                if v in seen:
                    cyclic=True; break
                seen.add(v); v=nxt[v]
            if cyclic: break
        if not cyclic: faces.append(mask)
    return faces

def predicted_faces(n, orient):
    k=[int(orient[i])+int(not orient[(i+1)%n]) for i in range(n)]
    allrim=(1<<n)-1
    faces=[]
    for mask in range(1<<(2*n)):
        if mask & allrim == allrim: continue
        ok=True
        for i in range(n):
            if mask>>i & 1:
                if orient[i] and (mask>>(n+i)&1): ok=False
                j=(i+1)%n
                if not orient[j] and (mask>>(n+j)&1): ok=False
        if ok:faces.append(mask)
    return faces

def rank_mod2(vectors):
    pivots={}
    for v in vectors:
        while v:
            k=v.bit_length()-1
            if k in pivots: v^=pivots[k]
            else: pivots[k]=v;break
    return len(pivots)

def bettis(faces):
    # augmented boundary ranks; returns positive ordinary Betti except H0 converted to reduced
    by_dim={}
    for mask in faces:
        if mask:by_dim.setdefault(mask.bit_count()-1,[]).append(mask)
    ranks={}
    for d in sorted(by_dim):
        if d==0:
            ranks[d]=1 if by_dim[d] else 0
            continue
        target={mask:i for i,mask in enumerate(by_dim.get(d-1,[]))}
        cols=[]
        for mask in by_dim[d]:
            x=mask;vec=0
            while x:
                bit=x & -x; x-=bit
                vec^=(1<<target[mask-bit])
            cols.append(vec)
        ranks[d]=rank_mod2(cols)
    bs={}
    for d in by_dim:
        val=len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if val:bs[d]=val
    return bs


def f_polynomial(n, q):
    # multiplication over Z[t], using coefficient lists
    def mul(a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j]+=x*y
        return c
    p=[1]
    for _ in range(q):p=mul(p,[1,1])
    for _ in range(n-2*q):p=mul(p,[1,2])
    for _ in range(q):p=mul(p,[1,3,1])
    p[n]-=1
    return p

def check_mixed_collapse(n, orient, faces):
    assert len(set(orient))==2
    j=next(i for i in range(n) if (not orient[i]) and orient[(i+1)%n])
    apex=1<<j; rim=(1<<n)-1
    live=set(faces)
    lowers=sorted([m for m in faces if (m>>n) and not (m&apex)], key=lambda m:(-m.bit_count(),m))
    for lo in lowers:
        hi=lo|apex
        assert lo in live and hi in live, ('missing matched pair',n,orient,lo,hi)
        assert all((lo | (1<<v)) not in live or v==j for v in range(2*n) if not ((lo>>v)&1)),('nonfree pair',n,orient,lo)
        live.remove(lo);live.remove(hi)
    expected={m for m in range(1<<n) if m != rim}
    assert live==expected,('collapse remainder',n,orient,live^expected)
    return len(lowers)

if __name__=='__main__':
    for n in range(3,7):
        distribution=Counter();patterns=0;collapse_pairs=0
        for orient in product((False,True),repeat=n):
            expected={} if len(set(orient))==1 else {n-2:1}
            a=direct_faces(n,orient)
            b=predicted_faces(n,orient)
            assert a==b, (n,orient,'face-model mismatch')
            bh=bettis(a)
            assert bh==expected,(n,orient,bh,expected)
            distribution[('uniform' if len(set(orient))==1 else 'mixed',tuple(sorted(bh.items())))]+=1
            q=sum((not orient[i]) and orient[(i+1)%n] for i in range(n))
            actual=Counter(m.bit_count() for m in a)
            expected_f=f_polynomial(n,q)
            assert all(actual[d]==expected_f[d] for d in range(len(expected_f))),('f-polynomial',n,orient)
            if q:collapse_pairs+=check_mixed_collapse(n,orient,a)
            patterns+=1
        print(f'n={n}; orientations={patterns}; types={dict(distribution)}; collapse_pairs={collapse_pairs}')
    print('all finite checks passed')
