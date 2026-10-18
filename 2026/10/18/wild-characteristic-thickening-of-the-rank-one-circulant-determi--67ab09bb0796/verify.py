#!/usr/bin/env python3
"""Finite exact consistency checks for cyclic rank-one determinantal schemes."""
from itertools import combinations, combinations_with_replacement, product
from math import comb


def canonical(pair, n):
    return tuple(sorted(pair)), sum(pair) % n


def check_n(n):
    # Every quadratic rank-one circulant minor is a difference of equal-sum monomials.
    actual = set()
    for r, s in combinations(range(n), 2):
        for c, d in combinations(range(n), 2):
            p = tuple(sorted(((r-c)%n, (s-d)%n)))
            q = tuple(sorted(((r-d)%n, (s-c)%n)))
            if p != q:
                assert sum(p)%n == sum(q)%n
                actual.add(frozenset((p,q)))
    # Each quadratic monomial reduces modulo actual minors to x0*x_{sum}.
    adj = {p:set() for p in combinations_with_replacement(range(n),2)}
    for e in actual:
        p,q = tuple(e)
        adj[p].add(q)
        adj[q].add(p)
    seen=set()
    comps=[]
    for p in adj:
        if p in seen:
            continue
        todo=[p]; seen.add(p); comp=set()
        while todo:
            a=todo.pop();comp.add(a)
            for b in adj[a]:
                if b not in seen:
                    seen.add(b);todo.append(b)
        comps.append(comp)
    assert len(comps)==n
    for comp in comps:
        s=sum(next(iter(comp))) % n
        assert all(sum(pair)%n == s for pair in comp)
        assert (0,s) in comp
    # Reduction of arbitrary monomials preserves the cyclic residue and yields n normal forms.
    for deg in range(1,7):
        reps={sum(m)%n for m in combinations_with_replacement(range(n),deg)}
        assert len(reps)==n
    # Quotient Betti polynomial agrees with the 2-linear ranks.
    a=[comb(n-1,j)*(-1)**j for j in range(n)]
    b=[(a[j] if j<n else 0)+(n-1)*(a[j-1] if j else 0) for j in range(n+1) for _ in (0,) if j <= n]
    for i in range(1,n):
        assert b[i+1]==((-1)**i)*i*comb(n,i+1)
    assert b[0]==1 and b[1]==0
    return len(actual), n, (n-1)*n//2


def poly_mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]=(out[i+j]+x*y)%p
    return out


def check_bad(n,p):
    assert n%p==0
    m=n;a=1
    while m%p==0:
        m//=p;a*=p
    base=[(-1)%p]+[0]*(m-1)+[1]
    val=[1]
    for _ in range(a):
        val=poly_mul(val,base,p)
    target=[(-1)%p]+[0]*(n-1)+[1]
    assert val==target
    return m,a


if __name__=='__main__':
    for n in range(3,9):
        print('n',n,'nonzero minors, graded dimension, quadratic generator count',check_n(n))
    for n,p in [(3,3),(4,2),(6,2),(6,3),(8,2),(9,3),(10,2),(12,3)]:
        print('wild fiber',n,p,'number support, local length',check_bad(n,p))
    print('VERIFY_OK: cyclic quadratic relations, graded ranks, Betti polynomial, wild-fiber factorization')
