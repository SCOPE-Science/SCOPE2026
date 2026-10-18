#!/usr/bin/env python3
"""Exact small-order verifier for rank strata of dyadic Fourier minors.

Arithmetic takes place in Z[X]/(X^(N/2)+1), the cyclotomic
integer ring for primitive Nth roots when N is a power of two.
"""
from itertools import combinations
from random import Random

PERMS=((0,1,2,1),(0,2,1,-1),(1,0,2,-1),
       (1,2,0,1),(2,0,1,1),(2,1,0,-1))

def add_poly(q, exponent, amount, n):
    exponent %= n
    if exponent >= n//2:
        exponent -= n//2
        amount = -amount
    q[exponent] += amount

def minor_zero(rows, cols, n):
    q=[0]*(n//2)
    for a,b,c,sign in PERMS:
        add_poly(q, rows[0]*cols[a]+rows[1]*cols[b]+rows[2]*cols[c], sign, n)
    return not any(q)

def two_minor_zero(ra,rb,ca,cb,n):
    return (ra-rb)*(ca-cb) % n == 0

def exact_rank(rows, cols, n):
    if not minor_zero(rows, cols, n):
        return 3
    for ra,rb in combinations(rows,2):
        for ca,cb in combinations(cols,2):
            if not two_minor_zero(ra,rb,ca,cb,n):
                return 2
    return 1

def valuation(x,n):
    x %= n
    assert x != 0
    return (x & -x).bit_length()-1

def levels(triple,n):
    a,b,c=triple
    lev=sorted([valuation(a-b,n),valuation(a-c,n),valuation(b-c,n)])
    assert lev[0]==lev[1]<lev[2]
    return lev[0],lev[2]

def proposed_rank(rows,cols,n):
    m=n.bit_length()-1
    u,v=levels(rows,n)
    s,t=levels(cols,n)
    if u+s>=m:
        return 1
    if v+s>=m or u+t>=m:
        return 2
    return 3

def count_formula(m):
    n=2**m
    counts={1:0,2:0,3:0}
    B={(u,v):n**3//2**(u+v+3)
       for u in range(m) for v in range(u+1,m)}
    for (u,v),cr in B.items():
        for (s,t),cc in B.items():
            rank=1 if u+s>=m else (2 if v+s>=m or u+t>=m else 3)
            counts[rank] += cr*cc
    assert sum(counts.values()) == (n*(n-1)*(n-2)//6)**2
    return counts

def main():
    rng=Random(1457289)
    verified=0
    for m in (2,3,4):
        n=2**m
        triples=list(combinations(range(n),3))
        tally={1:0,2:0,3:0}
        for rows in triples:
            for cols in triples:
                actual=exact_rank(rows,cols,n)
                predicted=proposed_rank(rows,cols,n)
                if actual!=predicted:
                    raise AssertionError((n,rows,cols,actual,predicted))
                tally[actual]+=1
                verified+=1
        assert tally==count_formula(m),(m,tally,count_formula(m))
        print(f'exhaustive N={n} ranks={tally}')
    for m,samples in ((5,18000),(6,8000)):
        n=2**m
        for _ in range(samples):
            rows=tuple(sorted(rng.sample(range(n),3)))
            cols=tuple(sorted(rng.sample(range(n),3)))
            actual=exact_rank(rows,cols,n)
            predicted=proposed_rank(rows,cols,n)
            if actual!=predicted:
                raise AssertionError((n,rows,cols,actual,predicted))
            verified+=1
        print(f'sampled N={n}: {samples} exact cyclotomic checks')
    assert count_formula(3)[2]==320
    assert count_formula(4)[1]==256
    assert count_formula(4)[2]==26624
    print(f'VERIFY_OK {verified} exact minor-rank comparisons')

if __name__=='__main__':
    main()
