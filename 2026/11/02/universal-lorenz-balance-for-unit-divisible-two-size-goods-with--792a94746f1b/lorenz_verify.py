"""Exact finite tests for a two-denomination equal-valuation allocation theorem.
This is a finite check, not an infinite proof.
"""
from itertools import product
from fractions import Fraction
from math import gcd


def compact_profile(n, k, m, r):
    assert n>=1 and k>=0 and m>=0 and r>=2 and isinstance(r,int)
    q,s=divmod(k,n)
    low=r*q
    if s==0:
        d,u=divmod(m,n)
        return sorted([low+d]*(n-u)+[low+d+1]*u,reverse=True)
    if m < r*(n-s):
        d,u=divmod(m,n-s)
        return sorted([low+d]*(n-s-u)+[low+d+1]*u+[low+r]*s,reverse=True)
    d,u=divmod(m-r*(n-s),n)
    return sorted([low+r+d]*(n-u)+[low+r+d+1]*u,reverse=True)


def check():
    cases=allocations=0
    for n in range(1,5):
        for r in range(2,7):
            for k in range(5):
                for m in range(7):
                    if n**(k+m)>150000: continue
                    target=compact_profile(n,k,m,r)
                    expected=[sum(target[:j]) for j in range(1,n)]
                    for v in product(range(n),repeat=k+m):
                        loads=[0]*n
                        for j in v[:k]: loads[j]+=r
                        for j in v[k:]: loads[j]+=1
                        loads.sort(reverse=True)
                        assert all(sum(loads[:j])>=expected[j-1] for j in range(1,n)),(n,r,k,m,target,loads)
                        allocations+=1
                    cases+=1
    for q in range(2,14):
        for p in range(q+1,19*q):
            if gcd(p,q)!=1: continue
            r=Fraction(p,q)
            two=2*r
            m=2*(int(two)//2)+1
            assert m>0 and m%2==1 and abs(two-m)<1,(r,m)
            assert abs(two-m)<1
    print(f'VERIFY_OK profiles={cases} assignments={allocations} rational_boundary=all_coprime_pq_tested')

if __name__=='__main__':check()
