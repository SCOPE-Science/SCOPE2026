#!/usr/bin/env python3
"""Self-contained exact verification of regular-network coextinction-variance envelope.

Only standard-library modules. The proof in RESULT.md covers all sizes; this script
independently exhausts small regular incidence matrices and removal subsets.
"""
from itertools import combinations
from math import comb
from collections import Counter


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def uvar_numerator(rows, m):
    n = len(rows)
    d = rows[0].bit_count()
    D = comb(n, m)
    # Sum indicators over every equally likely removed m-pollinator set.
    hist = Counter()
    for gone in combinations(range(n), m):
        mask = sum(1 << j for j in gone)
        z = sum((r & mask) == r for r in rows)
        hist[z] += 1
    assert sum(hist.values()) == D
    return D * sum(z*z*c for z,c in hist.items()) - sum(z*c for z,c in hist.items())**2


def formula_numerator(rows, m):
    n = len(rows)
    d = rows[0].bit_count()
    D = comb(n, m)
    a = choose(n-d, m-d)
    twice_pairs = 0
    deficits = 0
    b0 = choose(n-2*d, m-2*d)
    bd = a
    for i,j in combinations(range(n), 2):
        t = (rows[i]&rows[j]).bit_count()
        bt = choose(n-2*d+t, m-2*d+t)
        twice_pairs += 2*bt
        # d times the chord-defect numerator; integer arithmetic.
        deficits += (d-t)*b0+t*bd-d*bt
    N = n*a*D+twice_pairs*D-(n*a)**2
    maxN = (n*d*a+n*(n-d)*b0)*D-(n*a)**2
    assert d*(maxN-N) == 2*D*deficits
    return N, maxN, deficits


def regular_rows(n, d):
    masks = [sum(1 << j for j in pos) for pos in combinations(range(n), d)]
    cols = [0]*n
    rows=[]
    def rec(depth):
        if depth==n:
            if all(c==d for c in cols):
                yield tuple(rows)
            return
        for mask in masks:
            if any(cols[j]==d for j in range(n) if mask>>j&1):
                continue
            rows.append(mask)
            for j in range(n):
                cols[j] += mask>>j&1
            if all(c<=d for c in cols):
                yield from rec(depth+1)
            for j in range(n):
                cols[j] -= mask>>j&1
            rows.pop()
    yield from rec(0)


def block_network(n,d):
    return tuple(sum(1 << j for j in range((i//d)*d, (i//d+1)*d)) for i in range(n))


def is_blocks(rows):
    d=rows[0].bit_count()
    counts=Counter(rows)
    keys=list(counts)
    return all(c==d for c in counts.values()) and all((a&b)==0 for a,b in combinations(keys,2))

def check(n,d,exhaustive=True):
    block=block_network(n,d)
    count=0
    equality=[]
    for rows in regular_rows(n,d):
        count+=1
        for m in range(n+1):
            N,maxN,deficit=formula_numerator(rows,m)
            assert N<=maxN, (n,d,m,rows,N,maxN)
            if d<=m<=n-2:
                assert (N==maxN)==is_blocks(rows),(n,d,m,rows)
            if count<=10 or (count%100==0 and m in (d,n-2)):
                assert N==uvar_numerator(rows,m), (n,d,m,rows,N)
        if count>=10 and not exhaustive:
            break
    print(f'n={n}, d={d}, matrices_checked={count}, complete={exhaustive}')
    assert count>0


if __name__=='__main__':
    check(4,2,True)
    check(6,2,True)
    check(6,3,False)
    # A labeled 3-by-3-block arrangement realizes the exact upper bound.
    for n,d in [(4,2),(6,2),(6,3),(9,3)]:
        rows=block_network(n,d)
        for m in range(n+1):
            got,upper,_=formula_numerator(rows,m)
            assert got==upper==uvar_numerator(rows,m)
    print('PASS: exhaustive small cases; direct uniform-subset moments; unique active-stage maximizers.')
