"""Standalone exhaustive checks for the exact shattering dimensions of proper colorings of paths.
Run: python3 color_path_verifier.py
No external packages required.
"""
from itertools import product, combinations
from functools import lru_cache

def colorings(n,q):
    return [z for z in product(range(q), repeat=n) if all(z[i]!=z[i+1] for i in range(n-1))]

def ldim(F,n,q):
    m=len(F); full=(1<<m)-1
    masks=[sum(1<<j for j,f in enumerate(F) if f[i]==c) for i in range(n) for c in range(q)]
    @lru_cache(None)
    def rec(s):
        if s.bit_count()<2:return 0
        return max((1+min(rec(s & b), rec(s & (full^b))) for b in masks if s&b and s&(full^b)),default=0)
    return rec(full)

def vcdim(F,n,q):
    m=len(F); B=[[int(f[i]==c) for i in range(n) for c in range(q)] for f in F]
    for r in range(min(n,m.bit_length()-1),0,-1):
        for S in combinations(range(n*q),r):
            if any(S[a]//q==S[b]//q for a in range(r) for b in range(a+1,r)):continue
            if len({sum(b[j]<<k for k,j in enumerate(S)) for b in B})==1<<r:return r
    return 0

for n in range(1,8):
    F=colorings(n,3)
    assert len(F)==3*(2**(n-1))
    L=ldim(F,n,3)
    V=vcdim(F,n,3)
    assert (L,V)==(n,n-n//4),(n,L,V)
    print('q=3 n=%d concepts=%d VC=%d LD=%d'%(n,len(F),V,L))
for n in range(1,5):
    F=colorings(n,4)
    assert (ldim(F,n,4),vcdim(F,n,4))==(n,n)
    print('q=4 n=%d concepts=%d VC=%d LD=%d'%(n,len(F),n,n))
for n in range(1,6):
    F=colorings(n,2)
    assert len(F)==2 and ldim(F,n,2)==1 and vcdim(F,n,2)==1
    print('q=2 n=%d VC=1 LD=1'%n)
# Check local 4-position obstruction and each possible 3-block labeling.
C3=colorings(3,3)
assert len({tuple(int(c[i]==(0,1,0)[i]) for i in range(3)) for c in C3})==8
for target in colorings(4,3):
    traces={tuple(int(c[i]==target[i]) for i in range(4)) for c in colorings(4,3)}
    assert len(traces)<16
print('ALL_COLOR_PATH_CHECKS_PASS')
