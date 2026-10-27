#!/usr/bin/env python3
"""Finite diagnostic checks for expansive relations between finite rooted stars.

No external packages. Run: python checker.py
"""
from itertools import product
from collections import Counter
from math import comb


def successors_leq(u, v):
    return u == v or u == 0


def expansive(rows, k, l):
    # Reflexive target order; check both confluence directions directly.
    q = l + 1
    if any(r == 0 for r in rows):
        return False
    for i in range(1, k + 1):
        for a in range(q):
            if rows[0] >> a & 1:
                if not any((rows[i] >> b & 1) and successors_leq(a,b) for b in range(q)):
                    return False
            if rows[i] >> a & 1:
                if not any((rows[0] >> b & 1) and successors_leq(b,a) for b in range(q)):
                    return False
    return True


def normal_form(rows, k, l):
    if any(r == 0 for r in rows):
        return False
    root = rows[0]
    C = root & ~1
    if root & 1:
        return all((r & C) == C for r in rows[1:])
    return bool(C) and all(r == C for r in rows[1:])


def rank_from_rows(rows):
    C = rows[0] & ~1
    c = C.bit_count()
    if rows[0] & 1:
        return c + max(1, *( (r & ~C).bit_count() for r in rows[1:] ))
    return c


def is_order_map(f):
    return all(successors_leq(f[0], f[i]) for i in range(1,len(f)))


def rowgraph(f, k, l):
    return tuple(1 << a for a in f)


def homomorphisms(k, l):
    return [rowgraph(f,k,l) for f in product(range(l+1), repeat=k+1) if is_order_map(f)]


def cover(rows, k, l):
    C = rows[0] & ~1
    c_list = [j for j in range(1,l+1) if C >> j & 1]
    maps=[]
    if not (rows[0] & 1):
        for j in c_list:
            maps.append(tuple([1<<j]*(k+1)))
    else:
        for j in c_list:
            maps.append(tuple([1<<j]*(k+1)))
        extras=[[j for j in range(l+1) if (rows[i] & (1<<j)) and not (C & (1<<j))] for i in range(1,k+1)]
        t=max(1,*(len(E) for E in extras))
        for z in range(t):
            f=[0]
            for i,E in enumerate(extras,1):
                if z < len(E):
                    f.append(E[z])
                else:
                    f.append(next(j for j in range(l+1) if rows[i]>>j & 1))
            maps.append(rowgraph(f,k,l))
    return maps


def cumulative(k,l,r):
    if r<1:
        return 0
    q=l+1
    S=sum(comb(q,j) for j in range(1,min(r,q)+1))**k
    for c in range(1, min(l,r-1)+1):
        z=min(r-c,q-c)
        S+=comb(l,c)*sum(comb(q-c,j) for j in range(z+1))**k
    S+=sum(comb(l,c) for c in range(1,min(l,r)+1))
    return S


def total_count(k,l):
    return (2**(l+1)-1)**k+sum(comb(l,c)*2**(k*(l+1-c)) for c in range(1,l+1))+2**l-1


def exact_minimum_cover(rows, homs):
    # Dynamic-programming exact set cover for small universes, independent of closed formula.
    universe=[(i,j) for i,r in enumerate(rows) for j in range(r.bit_length()) if r>>j & 1]
    full=(1<<len(universe))-1
    masks=[]
    for h in homs:
        if all((a & ~b)==0 for a,b in zip(h,rows)):
            masks.append(sum(1<<e for e,(i,j) in enumerate(universe) if h[i]>>j&1))
    reachable={0:0}
    for m in masks:
        old=list(reachable.items())
        for z,d in old:
            u=z|m
            if u not in reachable or reachable[u]>d+1:
                reachable[u]=d+1
    return reachable.get(full,None)


def run():
    tests=0
    for k in range(1,4):
        for l in range(1,4):
            counts=Counter()
            homs=homomorphisms(k,l)
            assert len(homs)==(l+1)**k+l
            for rows in product(range(1,1<<(l+1)), repeat=k+1):
                ex=expansive(rows,k,l)
                nf=normal_form(rows,k,l)
                assert ex==nf,(k,l,rows,'normal-form')
                tests+=1
                if not ex:continue
                rk=rank_from_rows(rows)
                cnt=cover(rows,k,l)
                assert len(cnt)==rk,(k,l,rows,'rank')
                assert all(all((v&~w)==0 for v,w in zip(h,rows)) for h in cnt)
                assert all(all(x.bit_count()==1 for x in h) for h in cnt)
                assert all(is_order_map(tuple(h_i.bit_length()-1 for h_i in h)) for h in cnt)
                assert tuple(__import__('functools').reduce(lambda a,b:a|b,[h[i] for h in cnt],0) for i in range(k+1))==rows
                counts[rk]+=1
                tests+=5
                if k<=2 and l<=2:
                    minimum=exact_minimum_cover(rows,homs)
                    assert minimum==rk,(k,l,rows,minimum,rk)
                    tests+=1
            assert sum(counts.values())==total_count(k,l)
            assert {r:counts[r] for r in range(1,l+2)}=={r:cumulative(k,l,r)-cumulative(k,l,r-1) for r in range(1,l+2)}
            tests+=2
            print('case',k,l,'total',sum(counts.values()),'rank_counts',dict(sorted(counts.items())))
    # Critical Poisson scaling: for k=10, l=2^10, lambda=1.
    # Exact ratios computed relative to dominant 2^(k(l+1)) without huge big integers.
    import math
    for k in (8,10,12):
        l=2**k
        corr=math.exp(k*math.log1p(-2**(-l-1))) if l<1000 else 1.0
        # Event root present and no leaf, normalized denominator.
        denom=corr+(1+2**(-k))**l-1 + (2**l-1)/2**(k*(l+1)) if l<1000 else corr+(1+2**(-k))**l-1
        p0=corr/denom
        assert abs(p0-math.exp(-1))<0.003
        tests+=1
    print('ALL_CHECKS_OK',tests)

if __name__=='__main__': run()
