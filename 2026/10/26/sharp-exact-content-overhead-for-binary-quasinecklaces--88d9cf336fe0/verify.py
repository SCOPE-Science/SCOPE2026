#!/usr/bin/env python3
"""Independent finite checks of binary quasinecklace composition counts.
All operations use integer arithmetic and exhaustive tests for small words.
"""
from itertools import product
from math import comb, gcd

def is_quasinecklace(w):
    if not w: return False
    a = min(w)
    if w == (a,)*len(w): return True
    if w[-1]==a: return False
    run=0; ell=0
    for c in w:
        if c==a:
            run+=1
            ell=max(ell,run)
        else: run=0
    if w[:ell]!=(a,)*ell:return False
    after=w[ell]
    for i in range(1,len(w)-ell):
        if w[i:i+ell]==(a,)*ell and w[i+ell]<after:return False
    return True

def is_necklace(w):
    return all(w<=w[k:]+w[:k] for k in range(1,len(w)))

def quasi_formula(z,r):
    if z==0 or r==0: return 1
    ans=0
    for ell in range(1,z+1):
        rem=z-ell
        # weak compositions into r-1 slots, each <=ell
        dp=[1]+[0]*rem
        for _ in range(r-1):
            q=[0]*(rem+1)
            for k,a in enumerate(dp):
                for j in range(min(ell,rem-k)+1):q[k+j]+=a
            dp=q
        ans+=dp[rem]
    return ans

def phi(d):
    x=d; ans=d;p=2
    while p*p<=x:
        if x%p==0:
            while x%p==0:x//=p
            ans-=ans//p
        p+=1
    if x>1:ans-=ans//x
    return ans

def necklace_formula(z,r):
    n=z+r
    return sum(phi(d)*comb(n//d,z//d) for d in range(1,gcd(z,r)+1) if z%d==0 and r%d==0)//n

if __name__=='__main__':
    tests=0
    for n in range(1,16):
        qc=[0]*(n+1);nc=[0]*(n+1)
        for w in product((0,1),repeat=n):
            z=w.count(0)
            qc[z]+=is_quasinecklace(w)
            nc[z]+=is_necklace(w)
        for z in range(n+1):
            r=n-z
            exp_q=quasi_formula(z,r)
            exp_n=necklace_formula(z,r)
            assert (qc[z],nc[z])==(exp_q,exp_n),(n,z,r,qc[z],exp_q,nc[z],exp_n)
            tests+=1
    print('ALL_LENGTHS_THROUGH_15_OK',tests)
    for z in range(1,8):
        r=3000
        q=quasi_formula(z,r)
        nn=necklace_formula(z,r)
        ratio=q/nn
        print('FIXED_Z',z,'R',r,'RATIO',f'{ratio:.9f}')
        assert abs(ratio-z)<0.1
    orbit_checks=0
    for n in range(2,15):
        seen=set()
        for w in product((0,1),repeat=n):
            if min(w)==max(w):continue
            orbit={w[k:]+w[:k] for k in range(n)}
            key=min(orbit)
            if key in seen:continue
            seen.add(key)
            p=next(d for d in range(1,n+1) if n%d==0 and w==w[:d]*(n//d))
            root=w[:p]
            starts=[i for i in range(p) if root[i]==0 and root[(i-1)%p]==1]
            lengths=[]
            for i in starts:
                j=0
                while root[(i+j)%p]==0:j+=1
                lengths.append(j)
            predicted=lengths.count(max(lengths))
            actual=sum(is_quasinecklace(v) for v in orbit)
            assert predicted==actual,(n,w,p,predicted,actual)
            orbit_checks+=1
    print('CYCLIC_ORBIT_COUNTS_OK',orbit_checks)
    print('VERIFY_OK')
