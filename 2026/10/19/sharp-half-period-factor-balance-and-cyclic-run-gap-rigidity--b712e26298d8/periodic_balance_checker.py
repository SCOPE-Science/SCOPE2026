#!/usr/bin/env python3
"""Finite corroboration of sharp periodic factor-count imbalance."""
from itertools import product
from math import gcd

def period(w):
    p=len(w)
    return next(d for d in range(1,p+1) if p%d==0 and w == w[:d]*(p//d))

def observed_optimum(block):
    p=len(block)
    long=block*6
    optimum=0
    witness=None
    # Occurrence phases of all factor types up to length p.
    for k in range(1,p+1):
        for v in set(long[i:i+k] for i in range(p)):
            starts={i for i in range(p) if long[i:i+k]==v}
            for m in range(0,p):
                counts=[sum(((i+j)%p in starts) for j in range(m)) for i in range(p)]
                gap=max(counts)-min(counts)
                if gap>optimum:
                    optimum=gap;witness=(v,m,starts)
    return optimum,witness

def independent_optimum(block):
    p=len(block); w=block*12
    best=0
    for length in range(1,2*p+2):
        for patlen in range(1,min(p,length)+1):
            windows=[w[i:i+length] for i in range(p)]
            factors=set(w[i:i+patlen] for i in range(p))
            for pat in factors:
                scores=[sum(t[j:j+patlen]==pat for j in range(length-patlen+1)) for t in windows]
                best=max(best,max(scores)-min(scores))
    return best

def predicted_extremal(block):
    p=len(block); k=p//2
    runs={c:[] for c in set(block)}
    if len(runs)==1:
        return False
    # Start at a cyclic change point to expose all maximal cyclic runs.
    j=next(i for i in range(p) if block[i]!=block[(i-1)%p])
    rotated=block[j:]+block[:j]
    z=0
    while z<p:
        t=z+1
        while t<p and rotated[t]==rotated[z]:t+=1
        runs[rotated[z]].append(t-z)
        z=t
    return any((lambda r:r[0]-(r[1] if len(r)>1 else 0)>=k)(sorted(lengths,reverse=True))
               for lengths in runs.values() if lengths)

def run():
    total=0
    for p in range(2,10):
        for tup in product('01',repeat=p):
            w=''.join(tup)
            if period(w)!=p:continue
            actual,_=observed_optimum(w)
            assert actual<=p//2,(w,p,actual)
            assert (actual==p//2)==predicted_extremal(w),(w,p,actual,predicted_extremal(w))
            total+=1
        for a in range(1,p):
            b=p-a
            w='0'*a+'1'*b
            actual,wi=observed_optimum(w)
            assert actual==p//2,(w,actual,p//2,wi)
            assert independent_optimum(w)==p//2,('direct',w)
    # Primitive ternary small cases with independent direct windows.
    ternary=0
    for p in range(2,8):
        for tup in product('012', repeat=p):
            w=''.join(tup)
            if period(w)!=p:continue
            actual,_=observed_optimum(w)
            assert actual<=p//2
            assert (actual==p//2)==predicted_extremal(w),(w,p,actual,predicted_extremal(w))
            assert independent_optimum(w)==actual,(w,p,actual)
            ternary+=1
    print('binary primitive periods 2..9:',total)
    print('ternary primitive periods 2..7:',ternary)
    print('all binary two-run equality cases periods 2..9:',sum(range(1,9)))
    print('PASS: sharpness classification, independent windows, cyclic-support bounds')
if __name__=='__main__':run()
