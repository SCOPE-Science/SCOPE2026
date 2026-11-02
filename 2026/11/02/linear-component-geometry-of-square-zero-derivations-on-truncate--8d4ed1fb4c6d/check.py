#!/usr/bin/env python3
"""Finite-field exhaustive checks of square-zero derivations and component census."""
from itertools import product

def gf_mul(a,b,q):
    if q==2: return a&b
    # GF(4) modulus z^2+z+1; GF(8) modulus z^3+z+1
    mod={4:0b111,8:0b1011}[q]
    res=0
    while b:
        if b&1:res^=a
        b>>=1
        a<<=1
        if a&q:a^=mod
    return res

def polysquarezero(f,q):
    n=len(f)
    if n%2 and f[0]:return False
    # D^2(x) = f*f', check each coefficient directly.
    for degree in range(n):
        value=0
        for i in range(degree+1):
            j=degree-i+1
            if j<n and j%2:
                value^=gf_mul(f[i],f[j],q)
        if value:return False
    return True

def components(n):
    comps=[]
    if n%2==0:
        for j in range(n//4+1):
            zeros=set(range(2*j))
            zeros.update(range(2*j+1,n-2*j,2))
            comps.append(zeros)
    else:
        for j in range(1,(n-1)//4+1):
            zeros=set(range(2*j))
            zeros.update(range(2*j+1,n-2*j+1,2))
            comps.append(zeros)
        comps.append(set(range((n+1)//2)))
    return comps

def main():
    tests=0
    for q,maxn in ((2,12),(4,8),(8,5)):
        for n in range(2,maxn+1):
            comps=components(n)
            m=n//2
            assert len(comps)==n//4+1
            assert all(n-len(S)==m for S in comps), (n,comps)
            # Linear subspace chain: every new component intersects preceding union
            # only in its immediate predecessor hyperplane.
            for j in range(1,len(comps)):
                assert len(comps[j]|comps[j-1])==n-m+1,(n,j)
                for i in range(j-1):
                    assert (comps[j]|comps[j-1]).issubset(comps[j]|comps[i])
            cnt=0
            membership_dist=[0]*(len(comps)+1)
            for f in product(range(q),repeat=n):
                good=polysquarezero(f,q)
                covered=sum(all(f[i]==0 for i in Z) for Z in comps)
                if good!=(covered>0):
                    raise AssertionError((q,n,f,good,covered,comps))
                if good:cnt+=1
                membership_dist[covered]+=1
            expected=(n//4+1)*q**m-(n//4)*q**(m-1)
            assert cnt==expected,(n,q,cnt,expected)
            print(f'n={n:2} q={q:2} components={len(comps)} dimension={m} points={cnt:6} predicted={expected:6} OK')
            tests+=1
    print('SQUARE_ZERO_TRUNCATED_DERIVATION_COMPONENT_CENSUS_OK',tests)

if __name__=='__main__':main()
