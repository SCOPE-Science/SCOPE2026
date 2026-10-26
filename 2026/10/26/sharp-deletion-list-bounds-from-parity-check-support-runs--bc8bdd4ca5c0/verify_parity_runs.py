#!/usr/bin/env python3
"""Independent finite checks of deletion lists for binary parity-check hyperplanes."""
from collections import defaultdict
from itertools import product


def runs(mask, n):
    spans=[]; i=0
    while i<n:
        if mask>>i&1:
            a=i
            while i<n and (mask>>i&1): i+=1
            spans.append((a,i-1))
        else:i+=1
    return spans


def candidate(y,n,i,b):
    return (y&((1<<i)-1))|(b<<i)|((y>>i)<<(i+1))


def witness(mask,n):
    spans=runs(mask,n); r=len(spans)
    if r==1 and (spans[0][1]-spans[0][0]+1)%2==0:
        a,b=spans[0]; ell=b-a+1
        return ((1<<(ell-2))-1)<<a
    if r%2==1 and all((b-a+1)%2==0 for a,b in spans):
        return None
    t=[0]*r
    if r%2:
        j=next(j for j,(a,b) in enumerate(spans) if (b-a+1)%2)
        t[j]=1
    ybits={}
    for j,(a,b) in enumerate(spans):
        for i in range(a,b):
            assert i not in ybits
            ybits[i]=t[j]
        if a>0:
            assert a-1 not in ybits
            ybits[a-1]=1-t[j]
        if b<n-1:
            assert b not in ybits
            ybits[b]=1-t[j]
    return sum(bit<<i for i,bit in ybits.items())


def list_from_insertions(mask,n,y):
    p={candidate(y,n,i,b) for i in range(n) for b in (0,1)}
    assert len(p)==n+1
    return sum((x&mask).bit_count()%2==0 for x in p)


def lists_via_codewords(mask,n):
    bins=defaultdict(set)
    for x in range(1<<n):
        if (x&mask).bit_count()%2: continue
        for i in range(n):
            y=(x&((1<<i)-1))|((x>>(i+1))<<i)
            bins[y].add(x)
    return [len(bins[y]) for y in range(1<<(n-1))]


def main():
    total=0;applicable=0; exceptional=0;verified_witnesses=0
    for n in range(2,10):
        for h in range(1,1<<n):
            ell=runs(h,n);r=len(ell)
            pred=n-r+1
            if r==1 and (ell[0][1]-ell[0][0]+1)%2==0:pred=n-1
            applicable_case=(r%2==0 or any((b-a+1)%2 for a,b in ell) or r==1)
            values=lists_via_codewords(h,n)
            assert max(values)<=n-r+1,('universal bound',n,h)
            if applicable_case:
                assert max(values)==pred,(n,h,ell,max(values),pred)
                y=witness(h,n)
                assert y is not None and list_from_insertions(h,n,y)==pred,(n,h,ell,y,pred)
                applicable+=1;verified_witnesses+=1
            else:exceptional+=1
            total+=1
        print('EXHAUSTIVE n=%d done'%n)
    # Constructive family checks for all masks (no brute over received words) at longer lengths.
    for n in range(10,15):
        for h in range(1,1<<n):
            ell=runs(h,n);r=len(ell)
            if r%2==0 or any((b-a+1)%2 for a,b in ell) or r==1:
                y=witness(h,n)
                want=n-1 if r==1 and (ell[0][1]-ell[0][0]+1)%2==0 else n-r+1
                assert list_from_insertions(h,n,y)==want,(n,h,ell,y,want)
                verified_witnesses+=1
        print('CONSTRUCTION n=%d done'%n)
    print('EXHAUSTIVE_HYPERPLANES',total,'APPLICABLE',applicable,'EXCEPTIONAL',exceptional)
    print('VERIFIED_EXPLICIT_WITNESSES',verified_witnesses)
    print('PARITY_RUNS_VERIFY_OK')
if __name__=='__main__':main()
