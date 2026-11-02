#!/usr/bin/env python3
"""Independent finite checks for a cyclic-permutation square-subsequence theorem.

Run: python3 verify.py
The mathematical theorem for all sizes is proved separately, not by this enumeration.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def occurrence(target, host):
    iterator = iter(host)
    return all(any(x == a for x in iterator) for a in target)


def predicted_root(root, periods):
    r = sum(root[i] <= root[i-1] for i in range(1, len(root)))
    s = int(root[0] <= root[-1])
    return 1 + 2*r + s <= periods


def subsequence_square_roots(host):
    """Independently enumerate indexed subsequences and deduplicate their roots."""
    out = set()
    for m in range(1, len(host)//2+1):
        for indices in combinations(range(len(host)), 2*m):
            s = tuple(host[j] for j in indices)
            if s[:m] == s[m:]:
                out.add(s[:m])
    return out


def predict_all_square_roots(q, k, maxroot=None):
    host = tuple(i for _ in range(k) for i in range(q))
    maxroot = len(host)//2 if maxroot is None else min(maxroot, len(host)//2)
    out = set()
    # Enumerate distinct subsequences of length <= maxroot rather than q^maxroot roots.
    old = {()}
    for x in host:
        old |= {u + (x,) for u in tuple(old) if len(u) < maxroot}
    for u in old:
        if u and len(u) <= maxroot and predicted_root(u, k):
            out.add(u)
    return out


def profile_by_transfer(q, m):
    """Count rooted square candidates by their unnormalized weak-descent cost."""
    count = Counter()
    for first in range(q):
        dp = {(first, 0):1}
        for _ in range(m-1):
            nxt = defaultdict(int)
            for (last, cost), ways in dp.items():
                for new_last in range(q):
                    nxt[(new_last, cost+2*int(new_last<=last))] += ways
            dp = nxt
        for (last, cost), ways in dp.items():
            count[cost+int(first<=last)] += ways
    assert sum(count.values()) == q**m
    return count


def polys(q):
    """Expansion of H_q(v(1-z²)) and its derivative in z and v."""
    H,Hp=Counter(),Counter()
    for j in range(q):
        for h in range(j+1):
            coef=comb(q,j+1)*comb(j,h)*(-1)**h
            H[(2*h,j)]+=coef
            if j:
                coef2=j*comb(q,j+1)*comb(j-1,h)*(-1)**h if h<j else 0
                if coef2: Hp[(2*h,j-1)]+=coef2
    return H,Hp


def mul(A,B,K,M):
    ans=Counter()
    for (k,m),a in A.items():
        for (l,n),b in B.items():
            if k+l<=K and m+n<=M: ans[(k+l,m+n)]+=a*b
    return {x:v for x,v in ans.items() if v}


def add(*polys):
    ans=Counter()
    for p in polys:ans.update(p)
    return {x:v for x,v in ans.items() if v}


def shift(A,k,m,s=1):
    return {(i+k,j+m):s*a for (i,j),a in A.items()}


def gf_check(q,K=12,M=9):
    F={}
    for m in range(1,M+1):
        costs=profile_by_transfer(q,m)
        for k in range(1,K+1):
            v=sum(a for t,a in costs.items() if t<k)
            if v:F[(k,m)]=v
    H,Hp=polys(q)
    # (1-z)(1-v z² H) F = z² v H + (1-z) z³ v² H'
    one={(0,0):1}
    one_minus_z={(0,0):1,(1,0):-1}
    factor=add(one,shift(H,2,1,-1))
    lhs=mul(mul(one_minus_z,factor,K,M),F,K,M)
    rhs=add(shift(H,2,1),shift(Hp,3,2),shift(Hp,4,2,-1))
    for k in range(K+1):
        for m in range(M+1):
            if lhs.get((k,m),0)!=rhs.get((k,m),0):
                raise AssertionError((q,k,m,lhs.get((k,m),0),rhs.get((k,m),0)))
    return sum(1 for k in range(K+1) for m in range(M+1))


def main():
    cases=((2,7),(3,5),(4,3),(5,3),(6,2),(7,2),(8,2))
    num_cases=num_roots=0
    for q,kmax in cases:
        for k in range(1,kmax+1):
            host=tuple(i for _ in range(k) for i in range(q))
            actual=subsequence_square_roots(host)
            predicted=predict_all_square_roots(q,k)
            if actual!=predicted:
                raise AssertionError((q,k,actual^predicted))
            h=k//2
            mx=max(map(len,actual),default=0)
            assert mx==q*h
            expected_max=(1 if k%2==0 else q) if h else 0
            assert sum(len(u)==mx for u in actual)==expected_max if h else not actual
            num_roots+=len(actual);num_cases+=1
    gf_coeffs=sum(gf_check(q) for q in range(2,8))
    print('VERIFY_OK literal_parameter_cases=%s distinct_square_roots=%s formal_identity_coefficients=%s q=2..8'% (num_cases,num_roots,gf_coeffs))

if __name__=='__main__':main()
