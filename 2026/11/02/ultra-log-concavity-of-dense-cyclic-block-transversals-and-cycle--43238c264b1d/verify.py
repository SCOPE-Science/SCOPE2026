#!/usr/bin/env python3
"""Exact verifier of the cycle-power domination coefficient identity and ULC tests."""
from math import comb


def formula(n, r):
    q = 2*r + 1
    if n <= q:
        return [0] + [comb(n,k) for k in range(1,n+1)]
    assert q+1 <= n <= 2*q+1
    t = n-q-1
    return [0] + [comb(n,k)-n*comb(t,k-1) if k-1<=t else comb(n,k) for k in range(1,n+1)]


def ulc(d):
    n = len(d)-1
    for k in range(1,n):
        assert d[k]**2 * comb(n,k-1)*comb(n,k+1) >= d[k-1]*d[k+1]*comb(n,k)**2, (n,k,d)


def brute(n,r):
    masks=[]
    for i in range(n):
        mask=0
        for j in range(n):
            if min((j-i)%n,(i-j)%n)<=r:
                mask |=1<<j
        masks.append(mask)
    d=[0]*(n+1)
    for subset in range(1<<n):
        covered=0
        for j in range(n):
            if subset>>j&1:covered|=masks[j]
        if covered==(1<<n)-1:d[subset.bit_count()]+=1
    return d


def brute_hitting(n,q):
    blocks=[]
    for i in range(n):
        mask=0
        for j in range(q):mask |= 1 << ((i+j)%n)
        blocks.append(mask)
    ans=[0]*(n+1)
    for selection in range(1<<n):
        if all(selection & block for block in blocks):
            ans[selection.bit_count()]+=1
    return ans


def hitting_formula(n,q):
    assert q+1 <= n <= 2*q+1
    t=n-q-1
    return [0] + [comb(n,k)-n*comb(t,k-1) if k-1<=t else comb(n,k) for k in range(1,n+1)]


def main():
    transversal_tests=0
    for n in range(2,16):
        for q in range(1,n):
            if n > 2*q+1:continue
            predicted=hitting_formula(n,q)
            measured=brute_hitting(n,q)
            assert predicted==measured,(n,q,predicted,measured)
            ulc(predicted)
            transversal_tests+=1
    tested=0
    for n in range(3,16):
        for r in range(1,n):
            if n>4*r+3:continue
            a,b=formula(n,r),brute(n,r)
            assert a==b,(n,r,a,b)
            ulc(a)
            tested+=1
    extensive=0
    for r in range(1,81):
        for n in range(3,4*r+4):
            a=formula(n,r)
            assert all(v>=0 for v in a)
            ulc(a)
            extensive+=1
    print(f'VERIFY_OK cyclic_hypergraphs={transversal_tests} exhaustive_graphs={tested} exact_parameter_cases={extensive}')
if __name__=='__main__':main()
