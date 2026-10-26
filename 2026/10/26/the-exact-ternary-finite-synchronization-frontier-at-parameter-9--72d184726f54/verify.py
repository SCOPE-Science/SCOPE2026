#!/usr/bin/env python3
"""Exhaustive isomorphism-reduced finite ternary synchronization-string census."""
from functools import lru_cache

@lru_cache(maxsize=250000)
def lcs(a,b):
    previous = [0] * (len(b)+1)
    for x in a:
        current=[0]
        for j,y in enumerate(b,1):
            current.append(previous[j-1]+1 if x==y else max(current[-1],previous[j]))
        previous=current
    return previous[-1]

def good_last(w):
    n=len(w)
    for j in range(1,n):
        right=w[j:]
        for i in range(j):
            if 20*lcs(w[i:j],right)>=9*(n-i):
                return False
    return True

def run():
    candidates=[(0,)]
    counts=[1]
    for length in range(2,34):
        ext=[]
        for prefix in candidates:
            for symbol in range(min(2, max(prefix)+1)+1):
                test=prefix+(symbol,)
                if good_last(test): ext.append(test)
        candidates=ext
        counts.append(len(ext))
        if length==32: survivors=[''.join(map(str,w)) for w in ext]
        print(length,len(ext))
    print('length-32 patterns (up to alphabet bijection):')
    for s in survivors:print(s)
    print('length 32:',len(survivors),'length 33:',counts[-1])
    assert counts==[1,1,2,3,5,7,10,13,18,24,27,33,36,41,39,40,44,50,57,46,50,34,30,29,27,26,26,13,11,12,11,10,0]
    assert len(survivors)==10 and not candidates
    assert len(set(survivors))==10
if __name__=='__main__':run()

# Independent insertion/deletion-distance cross-check, not used in enumeration.
def edit_insdel(a,b):
    prev=list(range(len(b)+1))
    for i,c in enumerate(a,1):
        row=[i]
        for j,d in enumerate(b,1):
            row.append(prev[j-1] if c==d else 1+min(prev[j],row[j-1]))
        prev=row
    return prev[-1]

def independent_check():
    leaves=[]
    frontier=[(0,)]
    for n in range(2,33):
        frontier=[w+(a,) for w in frontier for a in range(min(2,max(w)+1)+1) if good_last(w+(a,))]
        if n==32:leaves=frontier[:]
    checks=0
    for w in leaves:
        for k in range(2,33):
            for j in range(1,k):
                for i in range(j):
                    checks+=1
                    if 10*edit_insdel(w[i:j],w[j:k]) <= k-i:
                        raise AssertionError('Direct distance violation',w,i,j,k)
    print('independent full-word edit-distance tests:',checks)
    # Completely independent enumeration of all labeled ternary words at length 8.
    from itertools import product
    count=0
    for w in product(range(3), repeat=8):
        if all(10*edit_insdel(w[i:j],w[j:k]) > k-i
               for k in range(2,9) for j in range(1,k) for i in range(j)):
            count+=1
    print('independent labeled length-eight count:',count)
    assert count==13*6
if __name__=='__main__': independent_check()
