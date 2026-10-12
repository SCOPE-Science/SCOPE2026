#!/usr/bin/env python3
"""Independent verification of the double-star independence-polynomial formula.
Uses only the Python standard library. Finite checks do not replace the proof.
"""
from fractions import Fraction
from math import comb


def formula(a,b):
    out=[comb(a+b,k) for k in range(a+b+1)]+[0]
    for m in (a,b):
        for k in range(m+1):
            out[k+1]+=comb(m,k)
    while len(out)>1 and out[-1]==0:
        out.pop()
    return tuple(out)


def brute(a,b):
    n=a+b+2
    adj=[0]*n
    edges=[(0,1)]+[(0,2+i) for i in range(a)]+[(1,2+a+j) for j in range(b)]
    for u,v in edges:
        adj[u]|=1<<v
        adj[v]|=1<<u
    counts=[0]*(n+1)
    for mask in range(1<<n):
        independent=True
        m=mask
        while m:
            bit=m&-m
            u=bit.bit_length()-1
            m-=bit
            if adj[u]&m:
                independent=False
                break
        if independent:
            counts[mask.bit_count()]+=1
    while len(counts)>1 and counts[-1]==0:
        counts.pop()
    return tuple(counts)


def routh_first_column(coeffs):
    """Exact Routh table for positive real-coefficient polynomials."""
    desc=[Fraction(v) for v in coeffs[::-1]]
    assert desc[0]>0
    m=(len(desc)+1)//2
    row0=desc[::2]+[Fraction(0)]*(m-len(desc[::2]))
    row1=desc[1::2]+[Fraction(0)]*(m-len(desc[1::2]))
    table=[row0,row1]
    while len(table)<len(desc):
        a,b=table[-2],table[-1]
        if b[0]==0:
            raise AssertionError('Unexpected Routh zero pivot')
        row=[(b[0]*(a[i+1] if i+1<m else 0)-a[0]*(b[i+1] if i+1<m else 0))/b[0] for i in range(m)]
        table.append(row)
    first=[row[0] for row in table]
    if any(x<=0 for x in first):
        raise AssertionError(f'Failed exact Routh: {coeffs} first={first}')
    return first


def main():
    subsets=0
    profiles=0
    for a in range(9):
        for b in range(9):
            f=formula(a,b)
            assert f==brute(a,b),(a,b,f,brute(a,b))
            profiles+=1
            subsets+=1<<(a+b+2)
    print(f'EXACT_ENUMERATION_PASS profiles={profiles} subsets_examined={subsets} a_b=0..8')
    count=0
    for a in range(16):
        for b in range(16):
            routh_first_column(formula(a,b))
            count+=1
    print(f'EXACT_ROUTH_PASS profiles={count} a_b=0..15 all_first_column_entries_positive')
    print('ALL CHECKS PASSED: proof covers all nonnegative parameters; exhaustive checks are finite.')

if __name__=='__main__':
    main()
