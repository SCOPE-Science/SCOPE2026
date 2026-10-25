#!/usr/bin/env python3
"""Reproducible finite checks of rooted higher-dimensional furtherness barcodes."""
from math import comb

def expected(n,root_type):
    if root_type=='atom':
        d={(0,0,None):1}
        for j in range(1,n-1):
            d[(j-1,2**j-1,2**(j+1)-2)]=comb(n-1,j)
        d[(n-2,2**(n-1)-1,None)]=1
        return d
    if root_type=='coatom':
        d={(0,0,None):1}
        for k in range(0,n-2):
            d[(k,2**k,2**(k+1))]=comb(n-2,k)
        d[(n-2,2**(n-2),None)]=1
        return d
    raise ValueError(root_type)

def observed(n,root_type):
    root=1 if root_type=='atom' else ((1<<n)-1)^1
    cells=[i for i in range(1,(1<<n)-1)]
    def w(mask):
        # |U_y \ U_root|; U_z includes nonempty subsets of z
        return 2**mask.bit_count()-2**(mask&root).bit_count()
    cells.sort(key=lambda c:(w(c),c.bit_count(),c))
    ind={c:i for i,c in enumerate(cells)}
    assert all(w(c&~(1<<v))<=w(c) for c in cells for v in range(n) if (c>>v&1) and c&(c-1))
    pivots={}; pairs={}; births={}
    for j,c in enumerate(cells):
        b=set(ind[c^(1<<v)] for v in range(n) if (c>>v&1) and c&(c-1))
        while b:
            pivot=max(b)
            if pivot not in pivots:break
            b^=pivots[pivot]
        if b:
            pivot=max(b)
            pivots[pivot]=b
            pairs[pivot]=j
        else:
            births[j]=(c.bit_count()-1,w(c))
    intervals={}
    for i,(deg,birth) in births.items():
        death=w(cells[pairs[i]]) if i in pairs else None
        if birth==death:continue
        key=(deg,birth,death)
        intervals[key]=intervals.get(key,0)+1
    return intervals

if __name__=='__main__':
    for n in range(3,9):
        for kind in ('atom','coatom'):
            a=expected(n,kind);b=observed(n,kind)
            assert a==b, (n,kind,a,b)
            print(f'n={n} {kind}: {sum(a.values())} intervals in degrees {sorted(set(d for d,_,_ in a))}')
    print('VERIFY_OK')

def direct_order_observed(n,kind):
    """Independent chain-complex construction, without the face-poset shortcut."""
    root=1 if kind=='atom' else (((1<<n)-1)^1)
    vertices=list(range(1,(1<<n)-1))
    chains=[(c,) for c in vertices]
    seen=set(chains)
    for length in range(1,n-1):
        old=[c for c in chains if len(c)==length]
        for chain in old:
            last=chain[-1]
            for b in vertices:
                if b!=last and last&b==last:
                    out=chain+(b,)
                    if out not in seen:
                        seen.add(out);chains.append(out)
    w=lambda s:(2**s.bit_count()-2**(s&root).bit_count())
    chains.sort(key=lambda c:(max(w(v) for v in c),len(c),c))
    ids={c:i for i,c in enumerate(chains)}
    pivots={};pairs={};births={}
    for idx,chain in enumerate(chains):
        boundary=set(ids[chain[:i]+chain[i+1:]] for i in range(len(chain)) if len(chain)>1)
        while boundary and max(boundary) in pivots:
            boundary ^=pivots[max(boundary)]
        if boundary:
            p=max(boundary);pivots[p]=boundary;pairs[p]=idx
        else:
            births[idx]=(len(chain)-1,max(w(s) for s in chain))
    out={}
    for i,(degree,birth) in births.items():
        death=max(w(s) for s in chains[pairs[i]]) if i in pairs else None
        if birth==death:continue
        key=(degree,birth,death);out[key]=out.get(key,0)+1
    return out,len(chains)

if __name__=='__main__':
    for n in range(3,6):
        for kind in ('atom','coatom'):
            bars,cnt=direct_order_observed(n,kind)
            assert bars==expected(n,kind),(n,kind,bars,expected(n,kind))
            print('DIRECT_ORDER_OK',n,kind,cnt)
    print('DIRECT_ORDER_VERIFY_OK')
