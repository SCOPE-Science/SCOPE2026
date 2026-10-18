#!/usr/bin/env python3
"""Independent finite-field checks for rank-one nilpotent commuting tuples.

No external packages or files are required. Run: python3 verify_rank_one.py
"""
from functools import lru_cache
from itertools import product


def field(q):
    if q == 4:
        def add(a, b): return a ^ b
        def mul(a, b):
            out = 0
            while b:
                if b & 1: out ^= a
                b >>= 1
                a <<= 1
                if a & 4: a ^= 7  # t^2+t+1
            return out
    else:
        def add(a, b): return (a+b) % q
        def mul(a, b): return (a*b) % q
    return add, mul


def qbinom(n, k, q):
    if k < 0 or k > n: return 0
    # exact division performed once to avoid intermediate fractions
    numer = 1
    denom = 1
    for j in range(k):
        numer *= q**(n-j)-1
        denom *= q**(j+1)-1
    assert numer % denom == 0
    return numer // denom


def formula(n, r, q):
    total = 0
    for d in range(n+1):
        inner = 0
        for t in range(d+1):
            coeff = qbinom(d, t, q) * (-1)**(d-t) * q**((d-t)*(d-t-1)//2)
            one = 1 + (q**t-1)*(q**(n-d)-1)//(q-1)
            inner += coeff*one**r
        total += qbinom(n,d,q)*inner
    return total


def matrices(n, q):
    add, mul = field(q)
    unit = tuple([0]*(n*n))
    unique = {unit}
    vectors = list(product(range(q), repeat=n))
    nonzero = [x for x in vectors if any(x)]
    for u in nonzero:
        for v in nonzero:
            s=0
            for i in range(n): s=add(s,mul(u[i],v[i]))
            if s: continue
            M=tuple(mul(u[i],v[j]) for i in range(n) for j in range(n))
            unique.add(M)
    return sorted(unique)


def product_matrix(A,B,n,add,mul):
    out=[]
    for i in range(n):
        for j in range(n):
            s=0
            for k in range(n): s=add(s,mul(A[i*n+k],B[k*n+j]))
            out.append(s)
    return tuple(out)


def count(n, r, q):
    add,mul=field(q)
    mm=matrices(n,q)
    size=len(mm)
    zero=tuple([0]*(n*n))
    neighbor=[0]*size
    for i,A in enumerate(mm):
        for j,B in enumerate(mm):
            prod=product_matrix(A,B,n,add,mul)
            reverse=product_matrix(B,A,n,add,mul)
            assert (prod==reverse)==(prod==zero and reverse==zero), (n,q,i,j)
            if prod==reverse: neighbor[i]|=1<<j
    @lru_cache(None)
    def recursively(k,mask):
        if k==0: return 1
        out=0
        remaining = mask
        while remaining:
            bit=remaining & -remaining
            i=bit.bit_length()-1
            out+=recursively(k-1, mask & neighbor[i])
            remaining-=bit
        return out
    observed=recursively(r,(1<<size)-1)
    expected=formula(n,r,q)
    assert observed==expected,(n,r,q,observed,expected)
    print('PASS',f'n={n}',f'r={r}',f'q={q}',f'number_of_matrices={size}',f'commuting_tuples={observed}')


def component_count(n,r):
    if n>=2*r: return 1
    return min(r,n-1)-max(n-r,1)+1


def component_dimensions(n,r):
    ds=[r] if n>=2*r else list(range(max(n-r,1), min(r,n-1)+1))
    dims=[d*(n-d)+r*(n-1) for d in ds]
    assert max(dims)==r*(n-1)+(r*(n-r) if n>=2*r else n*n//4)
    return ds,dims


def main():
    for n,r,q in [(2,1,2),(2,2,2),(2,4,2),(3,2,2),(3,3,2),
                  (3,4,2),(4,2,2),(4,3,2),(2,3,3),(3,2,3),
                  (2,3,4),(3,2,4),(2,2,5)]:
        count(n,r,q)
        ds,dims=component_dimensions(n,r)
        assert len(ds)==component_count(n,r)
        print('  component_dimensions', list(zip(ds,dims)))
    for n in range(2,16):
        for r in range(1,16):
            component_dimensions(n,r)
    print('VERIFY_OK_MINIMAL_NILPOTENT_TUPLES')

if __name__=='__main__': main()
