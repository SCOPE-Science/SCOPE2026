#!/usr/bin/env python3
"""Exact tests of new finite-chain FIK modal-profile classification (stdlib only)."""
from itertools import combinations_with_replacement, product
from math import comb, factorial

checks=0

def test(x, msg='assertion'):
    global checks
    checks+=1
    if not x: raise AssertionError(msg)


def count_plane(n,r):
    if r == 0: return 1
    return factorial(n+r-1)*factorial(n+r)//(factorial(n-1)*factorial(n)*factorial(r)*factorial(r+1))


def predicted(n):
    return 1+sum(count_plane(n,r) for r in range(1,n+1))


def profile(rows,n):
    # Box and Diamond on all n+1 upward-closed subsets of chain.
    box=[];dia=[]
    for cut in range(n+1):
        bmask=0;dmask=0
        for i in range(n):
            if any((rows[j] & ((1<<cut)-1)) for j in range(i,n)) == False:
                bmask|=1<<i
            if any((rows[i]>>cut) & (1 << y) for y in range(n-cut)):
                dmask|=1<<i
        box.append(bmask);dia.append(dmask)
        test(all(not(bmask>>i&1) or (bmask>>j&1) for i in range(n) for j in range(i,n)),"box persistence")
        test(all(not(dmask>>i&1) or (dmask>>j&1) for i in range(n) for j in range(i,n)),"diamond persistence")
    return tuple(box),tuple(dia)


def fc(rows,n):
    for z in range(n):
        for x in range(z,n):
            for y in range(n):
                if rows[z] >> y & 1:
                    if not any((rows[x]>>t & 1) for t in range(y,n)):
                        return False
    return True


def invariants(rows,n):
    k=next((i for i,r in enumerate(rows) if r),n)
    m=tuple(row.bit_length()-1 for row in rows[k:])
    if k==n: return k,m,()
    mins=[min(j for j in range(n) if row>>j&1) for row in rows[k:]]
    u=tuple(min(mins[i:]) for i in range(len(mins)))
    return k,m,u


def rep(n,k,m,u):
    rows=[0]*k
    for a,b in zip(m,u): rows.append((1<<a)|(1<<b))
    test(len(rows)==n)
    return tuple(rows)

for n in range(1,5):
    seen={}; fcs=0
    for bits in range(1<<(n*n)):
        rows=tuple((bits>>(n*i)) & ((1<<n)-1) for i in range(n))
        if not fc(rows,n): continue
        fcs+=1
        p=profile(rows,n)
        inv=invariants(rows,n)
        test(all(inv[1][i]<=inv[1][i+1] for i in range(len(inv[1])-1)),"max monotone")
        test(all(inv[2][i]<=inv[2][i+1] for i in range(len(inv[2])-1)),"suffix-min monotone")
        test(all(lo<=hi for lo,hi in zip(inv[2],inv[1])),"min<=max")
        rr=rep(n,*inv)
        test(fc(rr,n),"normal form FC")
        test(invariants(rr,n)==inv,"normal form invariants")
        test(profile(rr,n)==p,"normal form modal behavior")
        if p in seen: test(seen[p]==inv,"profile implies invariants")
        else: seen[p]=inv
    test(len(seen)==predicted(n),f"predicted count n={n}: {len(seen)} != {predicted(n)}")
    print(f"n={n} frames={fcs} modal_profiles={len(seen)} predicted={predicted(n)}")

for n in range(1,7):
    total=0; functional=0
    for r in range(n+1):
        if r==0:
            total+=1;functional+=1;continue
        count=0;func_count=0
        for m in combinations_with_replacement(range(n),r):
            for u in combinations_with_replacement(range(n),r):
                if all(a<=b for a,b in zip(u,m)):
                    count+=1
                    if u==m:func_count+=1
        total+=count;functional+=func_count
        test(count==count_plane(n,r),f"plane product {n},{r}")
        test(func_count==comb(n+r-1,r),f"functional count {n},{r}")
    test(total==predicted(n))
    test(functional==comb(2*n,n))
    print(f"n={n:2} profiles={total} functional={functional} necessarily_binary={total-functional}")
print(f'VERIFY_OK {checks} exact assertions; exhaustive all {sum(2**(n*n) for n in range(1,5))} relations through n=4; independent ordered-pair counts through n=6')
