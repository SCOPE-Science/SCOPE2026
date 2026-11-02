#!/usr/bin/env python3
"""Exact small-case cross-checks for multiset high-deletion plateaus.

Run with Python >= 3.9: python verify.py. No third-party packages required.
This independently generates all multiplicity vectors and compatible cliques.
The infinite theorems are proved symbolically, not inferred from these checks.
"""
from itertools import combinations

def vectors(q,n):
    if q == 1:
        yield (n,)
        return
    for c in range(n+1):
        for tail in vectors(q-1,n-c):
            yield (c,)+tail

def overlap(x,y):
    return sum(min(a,b) for a,b in zip(x,y))

def compatible(x,y,k):
    return overlap(x,y) < k

def all_cliques_of_size(q,k,n,choose):
    v=list(vectors(q,n))
    N=len(v)
    upper=[0]*N
    for i in range(N):
        for j in range(i+1,N):
            if compatible(v[i],v[j],k):
                upper[i]|=1<<j
    def recur(candidates,needed):
        if needed==0: return 1
        if candidates.bit_count()<needed: return 0
        total=0
        while candidates.bit_count()>=needed:
            low=candidates&-candidates
            idx=low.bit_length()-1
            candidates^=low
            total+=recur(candidates & upper[idx],needed-1)
        return total
    return recur((1<<N)-1,choose)

def pure(q,n):
    return [tuple(n if i==j else 0 for i in range(q)) for j in range(q)]

def light(q,k):
    return (k-1,)*q

def lower_boundary(q,k):
    h=k-1
    if q%2:
        r=(q-1)//2
        a=[h if i<=r else 0 for i in range(q)]
        b=[h if i==0 or i>r else 0 for i in range(q)]
    else:
        r=q//2
        s=h//2
        a=[h if i<r else 0 for i in range(q)]
        b=[0 if i<r else h for i in range(q)]
        a[r]=s
        b[0]=s
    n=sum(a)
    assert n==sum(b)==((q+1)*h)//2
    return pure(q,n)+[tuple(a),tuple(b)]

def top_boundary(q,k):
    h=k-1
    n=q*h
    return pure(q,n)+[light(q,k)]

def penult_boundary(q,k,deficit,target):
    h=k-1;n=q*h-1
    a=[h]*q;a[deficit]=h-1
    C=pure(q,n)
    C[deficit]=tuple(n if j==deficit else 0 for j in range(q)) if target==deficit else tuple((n-1 if j==deficit else 1 if j==target else 0) for j in range(q))
    return C+[tuple(a)]

def test_code(C,k):
    return len(C)==len(set(C)) and all(compatible(x,y,k) for x,y in combinations(C,2))

def main():
    for q,k in [(3,4),(3,5),(4,4),(4,5),(5,4),(2,4)]:
        h=k-1;n0=((q+1)*h)//2
        C0=lower_boundary(q,k)
        assert test_code(C0,k)
        assert len(C0)==q+2
        Ct=top_boundary(q,k)
        assert test_code(Ct,k)
        cp=[]
        for d in range(q):
            for t in range(q):
                C=penult_boundary(q,k,d,t)
                assert test_code(C,k)
                cp.append(frozenset(C))
        assert len(set(cp))==q*q
        print(f'construction q={q} k={k}: n0={n0}, boundary size={len(C0)}, top length={q*h}, penultimate {len(set(cp))} distinct size-{q+1} codes verified')
    for q,k,n in [(3,4,6),(3,4,7),(3,4,8),(3,4,9),(3,5,8),(3,5,10),(3,5,11),(3,5,12),(2,4,5),(2,4,6)]:
        m1=all_cliques_of_size(q,k,n,q+1)
        m2=all_cliques_of_size(q,k,n,q+2)
        print(f'exhaustive q={q} k={k} n={n}: {q+1}-word codes={m1}, {q+2}-word codes={m2}')
        h=k-1
        if n==q*h:assert m1==1 and m2==0
        if n==q*h-1 and (q-1)*(k-1)>2:assert m1==q*q and m2==0
        if (q+1)*h<2*n<=2*q*h:assert m2==0 and m1>0
    print('ALL VERIFICATION CHECKS PASSED')
if __name__=='__main__':main()
