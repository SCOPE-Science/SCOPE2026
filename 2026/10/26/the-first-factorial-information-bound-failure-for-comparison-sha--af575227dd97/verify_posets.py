"""Independent exact shattering test using partial orders and linear extensions.

Usage: python verify_posets.py

No permutation bitsets or shattering certificates are used. A state is a transitively
closed strict partial order, encoded as predecessor masks. Each adaptive answer
extends that order; a depth-d split exists precisely when both extended posets
support depth d-1. Every such state has exactly its linear extensions as concepts.
"""
import itertools
import math
from functools import lru_cache

def closure(p):
    n=len(p); p=list(p)
    changed=True
    while changed:
        changed=False
        for i in range(n):
            x=p[i]
            for j in range(n):
                if x & (1<<j):x |= p[j]
            if x!=p[i]:p[i]=x;changed=True
    return tuple(p)

def extend(p,a,b):
    # Enforce a earlier than b. Return None if inconsistent.
    q=list(p);q[b]|=1<<a;q=closure(q)
    if any(q[i]&(1<<i) for i in range(len(q))):return None
    return q

def profile(n):
    pair_indices=list(itertools.combinations(range(n),2))
    base=tuple([0]*n)
    full=(1<<n)-1
    @lru_cache(None)
    def extension_count(p):
        @lru_cache(None)
        def orders(chosen):
            if chosen==full:return 1
            return sum(orders(chosen|(1<<i)) for i in range(n)
                       if not (chosen & (1<<i)) and not (p[i] & ~chosen))
        return orders(0)
    @lru_cache(None)
    def supports(p,d):
        if d==0:return True
        if extension_count(p) < (1<<d):return False
        for a,b in pair_indices:
            if p[a] & (1<<b) or p[b] & (1<<a):continue
            x=extend(p,a,b); y=extend(p,b,a)
            assert x is not None and y is not None
            if extension_count(x)<(1<<(d-1)) or extension_count(y)<(1<<(d-1)):
                continue
            if supports(x,d-1) and supports(y,d-1):return True
        return False
    limit=math.factorial(n).bit_length()-1
    dim=next(d for d in range(limit,-1,-1) if supports(base,d))
    assert extension_count(base)==math.factorial(n)
    if n==7:
        first=extend(base,0,1)
        assert extension_count(first)==math.factorial(n)//2
        assert not supports(first,11)
        assert supports(first,10)
        assert supports(base,11)
        assert not supports(base,12)
        print(f'POSET n=7 ordered_root_depth11=False poset_states={supports.cache_info().currsize} extension_states={extension_count.cache_info().currsize}')
    return dim

def main():
    expected=[0,1,2,4,6,9,11]
    for n,d in enumerate(expected,1):
        actual=profile(n);assert actual==d,(n,actual,d)
        print(f'POSET n={n} permutations={math.factorial(n)} ldim={actual}')
    print('POSET_ALL_CHECKS_PASS')

if __name__=='__main__': main()
