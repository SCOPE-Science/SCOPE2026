"""Finite verification for band cross-sections of the order-preserving transformation monoid.
Uses zero-based point labels; formulas and theorem are stated with one-based labels.
"""
from itertools import combinations,product

def partitions(n):
    for cutset in range(1<<(n-1)):
        cuts=[0]+[i+1 for i in range(n-1) if cutset & (1<<i)]+[n]
        yield tuple(tuple(range(cuts[j],cuts[j+1])) for j in range(len(cuts)-1))

def mul(f,g):
    return tuple(g[f[x]] for x in range(len(f)))

def key(f):
    return tuple(f[i]!=f[i+1] for i in range(len(f)-1))

def canonical(p,r,n):
    f=[None]*n
    for block in p:
        if r in block:v=r
        elif block[-1]<r:v=block[0]
        else:v=block[-1]
        for x in block:f[x]=v
    return tuple(f)

def count_bands_brute(n):
    parts=list(partitions(n))
    choices=[]
    for p in parts:
        cand=[]
        for targets in combinations(range(n),len(p)):
            t=[None]*n
            for block,y in zip(p,targets):
                for x in block:t[x]=y
            t=tuple(t)
            if mul(t,t)==t:cand.append(t)
        choices.append(cand)
    ans=0
    for chosen in product(*choices):
        S=set(chosen)
        if all(mul(a,b) in S for a in chosen for b in chosen):
            ans+=1
    return ans

for n,expected in [(1,1),(2,2),(3,3),(4,2),(5,1),(6,0),(7,0)]:
    part=list(partitions(n))
    roots=[r for r in range(n) if r<=2 and n-1-r<=2]
    assert len(roots)==expected
    for r in roots:
        S={canonical(p,r,n) for p in part}
        assert len(S)==2**(n-1)
        for f in S:
            assert tuple(sorted(f))==f
            assert mul(f,f)==f
            assert f[r]==r
        for a in S:
            for b in S:
                assert mul(a,b) in S
    if n<=4:
        assert count_bands_brute(n)==expected
    print('n=',n,'band R-sections=',expected,'verified roots=',roots)

# Each potential forbidden six-point window has a concrete non-idempotent product.
for n in range(6,16):
    for r in range(n):
        if r+3<n:
            e=list(range(n));e[r+3]=r+2
            h=list(range(n));h[r+1]=h[r+2]=r
            z=mul(tuple(h),tuple(e))  # e after h
            assert z[r+3]==r+2 and mul(z,z)[r+3]==r
        elif r>=3:
            e=list(range(n));e[r-3]=r-2
            h=list(range(n));h[r-1]=h[r-2]=r
            z=mul(tuple(h),tuple(e))
            assert z[r-3]==r-2 and mul(z,z)[r-3]==r
print('VERIFY_OK: n<=5 exhaustive construction and n<=4 section census; six-point obstruction checked n=6..15')
