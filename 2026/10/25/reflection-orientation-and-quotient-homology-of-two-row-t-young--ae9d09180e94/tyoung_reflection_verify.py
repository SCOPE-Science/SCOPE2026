#!/usr/bin/env python3
"""Standalone exact verifier for reflected two-row t-Young complexes.
Requires only Python 3.9+ standard library. No external files or network.
The finite calculations are tests, not the proof for all parameters.
"""
from itertools import product


def facets_by_columns(length, width):
    # Bottom row in column j has label j; top row has label width+j.
    out = set()
    for choices in product((0, 1), repeat=length):
        seq = [j + (width if choices[j-1] else 0) for j in range(1,length+1)]
        if all(a < b for a,b in zip(seq,seq[1:])):
            out.add(sum(1 << (x-1) for x in seq))
    return out


def facets_by_windows(length, width):
    n = length + width
    universe = (1 << n)-1
    return {universe ^ (((1 << width)-1)<<k) for k in range(length+1)}


def faces(facets):
    out = {0}
    for mask in facets:
        subs = mask
        while True:
            out.add(subs)
            if subs == 0:
                break
            subs = (subs-1)&mask
    return out


def reflect(mask,n):
    ans=0
    for i in range(n):
        if mask & (1<<i): ans |= 1<<(n-1-i)
    return ans


def reversal_sign(mask,n):
    a=[n-1-i for i in range(n) if mask&(1<<i)]
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))


def f2_rank(vectors):
    pivots={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in pivots:v ^= pivots[p]
            else:
                pivots[p]=v
                break
    return len(pivots)


def bettis_mod2(allfaces):
    by_size={}
    for f in allfaces:
        by_size.setdefault(f.bit_count(),[]).append(f)
    for k in by_size:by_size[k].sort()
    ranks={}
    for k in range(1,max(by_size)+1):
        rows={f:j for j,f in enumerate(by_size[k-1])}
        cols=[]
        for f in by_size.get(k,[]):
            boundary=0
            for i in range(f.bit_length()):
                if f&(1<<i):boundary ^= 1<<rows[f^(1<<i)]
            cols.append(boundary)
        ranks[k]=f2_rank(cols)
    return {k-1:len(arr)-ranks.get(k,0)-ranks.get(k+1,0)
            for k,arr in by_size.items() if k>0 and len(arr)-ranks.get(k,0)-ranks.get(k+1,0)}


def direct_lefschetz(allfaces,n):
    total=0
    for f in allfaces:
        if reflect(f,n)==f:
            # Including empty set, sign on empty is +1 and contribution is -1.
            total+=(-1)**(f.bit_count()-1)*reversal_sign(f,n) if f else -1
    return total


def half_word_weight(n,t):
    h=(n+1)//2
    total=0
    for bits in product((0,1),repeat=h):
        full=bits+ (bits[::-1] if n%2==0 else bits[-2::-1])
        if not any(all(full[j:j+t]) for j in range(n-t+1)):
            total+=(-1)**sum(bits)
    return total


def exact_coefficient(n,t):
    h=(n+1)//2
    c=(t-1)//2 if n%2==0 else t//2
    q,r=divmod(h,t+1)
    if r==0:return (-1)**((t+1)*q)
    if r==c+1:return (-1)**(c+(t+1)*q)
    return 0


def predicted_bettis(length,t):
    q,r=divmod(length,t+1)
    return ({2*q+r-1:1} if r in (0,1) else {})


def predicted_trace(length,t):
    q,r=divmod(length,t+1)
    return (-1)**(q+r) if r in (0,1) else 0


def main():
    a=b=c=d=0
    for t in range(1,9):
        for length in range(1,13-t):
            n=length+t
            assert facets_by_columns(length,t)==facets_by_windows(length,t),(length,t)
            a+=1
            ff=faces(facets_by_windows(length,t))
            assert bettis_mod2(ff)==predicted_bettis(length,t),(length,t,bettis_mod2(ff))
            b+=1
            tr=direct_lefschetz(ff,n)
            if tr:
                q,r=divmod(length,t+1)
                assert r in (0,1)
                assert tr==(-1)**(2*q+r-1)*predicted_trace(length,t)
            else:assert predicted_trace(length,t)==0
            c+=1
    for t in range(1,16):
        for n in range(t+1,26):
            assert half_word_weight(n,t)==exact_coefficient(n,t),(n,t)
            d+=1
    e=0
    for t in range(1,151):
        for length in range(1,451):
            n=t+length
            f=exact_coefficient(n,t)
            lefs=(-1)**(n+n//2)*f
            q,r=divmod(length,t+1)
            if r in (0,1):
                assert lefs==(-1)**(2*q+r-1)*predicted_trace(length,t),(n,t,lefs)
            else:assert lefs==0,(n,t,lefs)
            e+=1
    print('PASS: facet derivations',a,'mod-2 complete homology',b,
          'signed chain Lefschetz',c,'independent palindrome enumerations',d,
          'symbolic parameter substitutions',e)

if __name__=='__main__':main()
