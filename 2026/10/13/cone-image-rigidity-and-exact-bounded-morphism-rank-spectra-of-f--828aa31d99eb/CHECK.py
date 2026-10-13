#!/usr/bin/env python3
"""Exact rank spectra for bounded morphisms of regular finite rooted trees.

Independent small-instance brute force compared with the structural recurrence.
Only the Python standard library is needed.
"""
from itertools import product
from math import factorial
from collections import Counter

def R_table(d, h):
    R = [[0] * (h + 1) for _ in range(h + 1)]
    for H in range(h + 1):
        R[H][0] = 1
    for H in range(1, h + 1):
        for K in range(1, H + 1):
            A = R[H - 1][K] if K <= H - 1 else 0
            B = sum(d ** j * R[H - 1][K - j] for j in range(1, K + 1))
            R[H][K] = (A + B) ** d - B ** d + factorial(d) * R[H - 1][K - 1] ** d
    return R

def polys(d, h):
    R = R_table(d,h)
    N = lambda K: sum(d ** j for j in range(K + 1))
    end, idem = Counter(),Counter()
    for k in range(h + 1):
        K = h - k
        end[N(K)] += d ** k * R[h][K]
        ct = d ** k
        for t in range(1,k + 1):
            Hs = h - t
            S = sum(d ** j * R[Hs][K - j]
                    for j in range(max(0,K-Hs),K+1))
            ct *= S ** (d - 1)
        idem[N(K)] += ct
    return end,idem,R

def brute(d,h):
    verts = [()]
    for k in range(1,h+1):
        verts.extend(product(range(d),repeat=k))
    n=len(verts)
    cones=[tuple(j for j,y in enumerate(verts) if y[:len(x)]==x) for x in verts]
    target=[set(c) for c in cones]
    rank,idem=Counter(),Counter()
    ntested=0
    for a in product(range(n),repeat=n):
        ntested+=1
        if any({a[j] for j in cone}!=target[a[i]] for i,cone in enumerate(cones)):
            continue
        card=len(set(a));rank[card]+=1
        if all(a[a[i]]==a[i] for i in range(n)):idem[card]+=1
    return rank,idem,ntested

def main():
    assert polys(2,0)[0] == {1:1}
    c=0
    for d,h in [(2,0),(2,1),(2,2),(3,0),(3,1),(4,1)]:
        e,i,R=polys(d,h)
        be,bi,checks=brute(d,h)
        assert be == e, (d,h,e,be)
        assert bi == i, (d,h,i,bi)
        print(f'd={d} h={h}: endomorphism rank={dict(sorted(e.items()))}; idempotent rank={dict(sorted(i.items()))}; candidates={checks}')
        c += checks
    for d in range(2,6):
        for h in range(1,5):
            e,i,R=polys(d,h)
            assert e[sum(d**j for j in range(h+1))] == factorial(d)**((d**h-1)//(d-1))
            assert i[sum(d**j for j in range(h+1))] == 1
            assert e[1]==i[1]==d**h
            assert sum(e.values()) >= sum(i.values())
    print('VERIFY_OK independent brute',c,'function tables; 16 rank-structure cross-checks')

if __name__=='__main__':main()
