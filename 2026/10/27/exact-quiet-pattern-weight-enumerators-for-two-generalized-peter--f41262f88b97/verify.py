#!/usr/bin/env python3
"""Exact closed-neighborhood kernel and weight-enumerator checks for GP(n,k).

Only the Python standard library is required; all arithmetic is integral/binary.
"""
from collections import Counter
from math import gcd

BASE = {
 (1,0): {0:1, 2:1},
 (1,1): {0:1, 4:15, 6:15, 10:1},
 (2,0): {0:1, 2:2, 4:1},
 (2,1): {0:1, 8:15, 10:32, 12:15, 20:1},
 (4,0): {0:1, 4:14, 8:1},
 (4,1): {0:1, 16:55, 20:144, 24:55, 40:1},
}

def poly_mul(a,b):
    r=0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r

def f(k):
    return poly_mul(0b111, (1<<(2*k))|(1<<k)|1) ^ (1<<(k+1))

def graph_rows(n,k):
    assert k in (2,3) and n >= 2*k+1
    adj=[set() for _ in range(2*n)]
    def edge(a,b):
        assert a!=b
        adj[a].add(b); adj[b].add(a)
    for i in range(n):
        edge(i,(i+1)%n)
        edge(i,n+i)
        edge(n+i,n+(i+k)%n)
    assert all(len(s)==3 for s in adj)
    return [sum(1<<j for j in ({i}|adj[i])) for i in range(2*n)]

def nullspace(rows,width):
    rows=rows[:]
    piv=[]; p=0
    for j in range(width):
        sel=next((r for r in range(p,len(rows)) if rows[r]>>j&1),None)
        if sel is None: continue
        rows[p],rows[sel]=rows[sel],rows[p]
        for q in range(len(rows)):
            if q !=p and rows[q]>>j&1: rows[q]^=rows[p]
        piv.append(j); p+=1
    free=[j for j in range(width) if j not in set(piv)]
    vec=[]
    for col in free:
        a=1<<col
        for r,j in enumerate(piv):
            if rows[r]>>col&1: a|=1<<j
        assert all((a&row).bit_count()%2==0 for row in rows)
        vec.append(a)
    return vec

def ker_counter(n,k):
    basis=nullspace(graph_rows(n,k),2*n)
    counts=Counter()
    for mask in range(1<<len(basis)):
        x=0
        for i,b in enumerate(basis):
            if (mask>>i)&1: x ^= b
        counts[x.bit_count()]+=1
    return len(basis),dict(sorted(counts.items()))

def periodic_counter(h,delta):
    m=h*(5 if delta else 1)
    counts=Counter()
    for umask in range(1<<(h-1 if delta else h)):
        u=([0]+[(umask>>i)&1 for i in range(h-1)]) if delta else [(umask>>i)&1 for i in range(h)]
        for vmask in range(32 if delta else 1):
            x=[u[i%h] ^ ((vmask>>(i%5))&1 if delta else 0) for i in range(m)]
            y=[x[i]^x[(i-1)%m]^x[(i+1)%m] for i in range(m)]
            counts[sum(x)+sum(y)]+=1
    return dict(sorted(counts.items()))

def main():
    for k in (2,3):
        expected=poly_mul(poly_mul(1<<(2**(k-1))|1, 0b11111),1)
        assert f(k)==expected, (k,f(k),expected)
    for (h,d),table in BASE.items():
        assert periodic_counter(h,d)==table, (h,d,periodic_counter(h,d),table)
    tested=0
    for k in (2,3):
        for n in range(2*k+1,81):
            h=gcd(n,2**(k-1)); delta=int(n%5==0)
            m=h*(5 if delta else 1)
            dim,cnt=ker_counter(n,k)
            expected={w*(n//m):c for w,c in BASE[h,delta].items()}
            assert dim==h+4*delta,(n,k,dim,h,delta)
            assert cnt==expected,(n,k,cnt,expected)
            tested+=1
    print('VERIFY_OK: polynomial factorization, six base code enumerators, independent GF2 matrix kernels for',tested,'graphs through n=80')

if __name__=='__main__': main()
