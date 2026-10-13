#!/usr/bin/env python3
"""Exact consistency checks for the affine-weight Mobius recurrence and factorization formula."""
from math import comb


def omega_factor(n):
    exps=[]; p=2
    while p*p <= n:
        if n%p==0:
            k=0
            while n%p==0:
                k+=1; n//=p
            exps.append(k)
        p+=1 if p==2 else 2
    if n>1: exps.append(1)
    return exps


def ordered_squarefree_count(exps,r):
    # Inclusion-exclusion removes empty positions from r labelled bins.
    ans=0
    for j in range(r+1):
        ways=1
        for e in exps:
            ways*=comb(j,e) if j>=e else 0
        ans+=(-1)**(r-j)*comb(r,j)*ways
    return ans


def formula(n,c):
    if n==1: return 1
    exps=omega_factor(n); k=sum(exps)
    return (-1)**k*sum(ordered_squarefree_count(exps,r)*(c-1)**(r-1) for r in range(1,k+1))


def direct_floor(N,c):
    out=[0]*(N+1); out[1]=1
    for n in range(2,N+1):
        out[n]=1-n-sum(out[d]*(1+c*(n//d-1)) for d in range(2,n))
    return out


def direct_divisor(N,c):
    out=[0]*(N+1); out[1]=1
    for n in range(2,N+1):
        out[n]=-1-c*sum(out[d] for d in range(2,n) if n%d==0)
    return out


def main():
    total=0; boundary=0
    for c in (1,2,3,4,7):
        floor=direct_floor(300,c)
        div=direct_divisor(300,c)
        for n in range(1,301):
            expected=formula(n,c)
            assert floor[n]==div[n]==expected,(c,n,floor[n],div[n],expected)
            if n>1 and c>=3: assert (floor[n]==-1)==(len(omega_factor(n))==1 and omega_factor(n)[0]==1)
            if n>1 and c>=2: assert floor[n]*(-1)**sum(omega_factor(n))>0
            total+=1
    for n in range(2,2001):
        es=omega_factor(n); k=sum(es); E=max(es)
        counts=[ordered_squarefree_count(es,r) for r in range(1,k+1)]
        assert all(a>=0 for a in counts)
        assert all(counts[r-1]==0 for r in range(1,E))
        assert counts[E-1]==__import__('math').prod(comb(E,e) for e in es)
        assert counts[k-1]==__import__('math').factorial(k)//__import__('math').prod(__import__('math').factorial(e) for e in es)
        boundary+=1
    assert direct_floor(12,2)[8]==-1
    assert direct_floor(40,1)[30]==-1
    print(f'VERIFY_OK direct_floor_divisor_factorization={total} factor_count_boundaries={boundary} c=2_n=8=-1 c=1_n=30=-1')

if __name__=='__main__':main()
