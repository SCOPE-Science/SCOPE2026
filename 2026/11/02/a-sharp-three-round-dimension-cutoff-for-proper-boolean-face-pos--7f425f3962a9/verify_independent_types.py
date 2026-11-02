#!/usr/bin/env python3
"""Direct bitset recursive 3-move types; independent of Venn-cell enumerator."""
from functools import lru_cache

def calculate(n, depth=3):
    full=(1<<n)-1
    elements=range(1,full)
    # Under coordinate permutations one selected subset is characterized by cardinality.
    @lru_cache(None)
    def ext_pair(x,y):
        relxy=atomic(x,y)
        return (relxy, frozenset((atomic(x,z),atomic(y,z)) for z in elements))
    def atomic(a,b):
        if a==b: return 0
        if a & b == a: return 1
        if a & b == b: return 2
        return 3
    return frozenset(frozenset(ext_pair((1<<k)-1,y) for y in elements)
                     for k in range(1,n))

def main():
    types={}
    for n in range(2,10):
        t=calculate(n)
        match=[m for m,oth in types.items() if oth==t]
        assert match == ([8] if n==9 else []),(n,match)
        types[n]=t
        print(f'direct rank3: n={n} vertices={(1<<n)-2} pointed_types={len(t)} equivalent_previous={match}')
    assert len({t for t in types.values()})==7
    print('DIRECT_CLASSIFICATION PASS distinct=7 stable_at=8; all 2..9 checked')
if __name__=='__main__':main()
