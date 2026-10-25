"""Exact finite verification of residue failure patterns for reciprocal-sum recurrences.

Usage: python3 reciprocal_distribution_checker.py
Uses integer arithmetic only; no external libraries.
"""
from collections import defaultdict
from math import gcd


def factor(n):
    factors=[]
    p=2
    while p*p<=n:
        if n%p==0:
            a=0
            while n%p==0:
                n//=p; a+=1
            factors.append((p,a))
        p+=1 if p==2 else 2
    if n>1: factors.append((n,1))
    return factors


def finite_basin(p):
    counts=defaultdict(int)
    for r in range(1,p):
        seen=set()
        x=r
        j=0
        while x not in seen and x!=0:
            seen.add(x)
            x=(x+pow(x,-1,p))%p
            j+=1
        if x==0:
            counts[j]+=1
    assert sum(counts.values())<=p-1
    return dict(counts)


def local_failures(h, x):
    result=set()
    for p,a in factor(h):
        unit=h//p**a
        if x % p**a: # valuation below a
            continue
        s=(x//p**a)%p
        if s==0:
            continue  # valuation greater than a
        r=s*pow(unit,-1,p)%p
        visited=set()
        j=0
        while r and r not in visited:
            visited.add(r)
            r=(r+pow(r,-1,p))%p
            j+=1
        if r==0:
            result.add(j+1)
    return frozenset(result)


def distribution_formula(h):
    D={frozenset():1}
    modulus=1
    for p,a in factor(h):
        local=finite_basin(p)
        q=p**(a+1)
        options={frozenset():q-sum(local.values())}
        options.update({frozenset((j+1,)):b for j,b in local.items()})
        new=defaultdict(int)
        for S,v in D.items():
            for T,w in options.items():
                new[S|T]+=v*w
        D=dict(new)
        modulus*=q
    assert sum(D.values())==modulus
    return modulus,D


def direct_numerators(h,x,limit=7):
    # independently reduce t0=x/h then iterate (u^2+v^2)/(uv)
    u,v=x//gcd(x,h),h//gcd(x,h)
    fails=set()
    for j in range(1,limit+1):
        u,v=u*u+v*v,u*v
        assert gcd(u,v)==1
        if gcd(h,u)>1:
            fails.add(j+1)
    return fails


def verify():
    for h in (1,2,4,5,10,13,17,25,29,65,145):
        L,D=distribution_formula(h)
        # Entire residue period, checking local hit trajectories without CRT.
        observed=defaultdict(int)
        for x in range(1,L+1):
            observed[local_failures(h,x)]+=1
        assert dict(observed)==D,(h,L,D,dict(observed))
        # Verify recurrence numerator computations on samples.
        for x in (1,2,3,4,5,6,7,17,101):
            assert direct_numerators(h,x)==local_failures(h,x),(h,x)
    assert finite_basin(5)=={1:2,2:2}
    assert finite_basin(29)=={1:2,2:4,3:2}
    L,D=distribution_formula(145)
    assert L==21025
    bysize=[sum(v for S,v in D.items() if len(S)==k) for k in (0,1,2)]
    assert bysize==[17493,3512,20],bysize
    print('VERIFY_OK: all listed moduli; CRT finite-basin vs direct residue dynamics and exact recurrence')
    print('h=145: modulus',L, 'counts by number of bad indices',bysize)
    print('h=145: counts by exact failure index set:',sorted((sorted(S),v) for S,v in D.items()))


if __name__=='__main__':
    verify()
