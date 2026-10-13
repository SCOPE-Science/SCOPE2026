#!/usr/bin/env python3
from itertools import combinations
from collections import Counter


def rank(vs, m):
    basis = [0]*m
    r=0
    for x in vs:
        y=x
        while y:
            p=y.bit_length()-1
            if basis[p]:
                y ^= basis[p]
            else:
                basis[p]=y
                r+=1
                break
    return r


def span(vs):
    out={0}
    for v in vs:
        out |= {x^v for x in list(out)}
    return frozenset(out)


def subspaces(m,r):
    if r==0:
        return [frozenset({0})]
    nz=list(range(1,1<<m))
    seen=set()
    for comb in combinations(nz,r):
        if rank(comb,m)==r:
            seen.add(span(comb))
    return sorted(seen, key=lambda S: tuple(sorted(S)))


def gauss2(n,r):
    if r<0 or r>n: return 0
    num=den=1
    for i in range(r):
        num *= (2**(n-i)-1)
        den *= (2**(r-i)-1)
    return num//den


def generator_columns(m,np,npp):
    # simplex block: all nonzero column vectors of F_2^m
    cols=list(range(1,1<<m))
    # first appended block has row1=row2=1: functional a1+a2
    f12=(1<<0)|(1<<1)
    cols += [f12]*npp
    # second appended block has only row1=1: functional a1
    cols += [1]*(np-npp)
    return cols


def support_size(U, cols):
    # coordinate with column c is active iff some coefficient vector u in U has u.c=1
    return sum(any((u & c).bit_count() & 1 for u in U) for c in cols)


def formula_counts(m,r,np,npp):
    B=(1<<m)-(1<<(m-r))
    a=gauss2(m-2,r)
    b=gauss2(m-1,r)-a
    d=gauss2(m,r)-2*gauss2(m-1,r)+a
    raw=[(B,a),(B+npp,b),(B+np-npp,b),(B+np,d)]
    out=Counter()
    for s,c in raw:
        out[s]+=c
    return dict(sorted((s,c) for s,c in out.items() if c))


def expected_dr(m,r,np,npp):
    if r<=m-2:
        return (1<<m)-(1<<(m-r))
    if r==m-1:
        return (1<<m)-2+min(npp,np-npp)
    return (1<<m)-1+np


def check(m,np,npp):
    assert m>=3 and np>npp>0 and np%2==0 and npp%2==0 and np%4==2
    cols=generator_columns(m,np,npp)
    print(f"case m={m}, nprime={np}, ndoubleprime={npp}, length={len(cols)}")
    for r in range(1,m+1):
        ss=Counter(support_size(U,cols) for U in subspaces(m,r))
        expected=formula_counts(m,r,np,npp)
        got=dict(sorted(ss.items()))
        assert got==expected, (m,r,got,expected)
        dr=min(got)
        assert dr==expected_dr(m,r,np,npp), (m,r,dr,expected_dr(m,r,np,npp))
        assert sum(got.values())==gauss2(m,r)
        print(f"r={r}: spectrum={got}; d_r={dr}")
    # r=1 support counts are exactly the nonzero codeword weight distribution.
    one=Counter(support_size(U,cols) for U in subspaces(m,1))
    print("nonzero weight distribution:", dict(sorted(one.items())))

check(3,6,2)
check(4,10,4)
print("VERIFY_OK")
