#!/usr/bin/env python3
"""Exact finite-state verification of a single-swap subset-coverage formula.

This checker is finite evidence for the transition reduction, initial law,
and stationary entrance flux. Asymptotic assertions require the written proof.
No external Python dependencies are required.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def all_sets(n, k):
    return [frozenset(x) for x in combinations(range(n), k)]


def is_bad(h, targets):
    return any(s <= h for s in targets)


def projected(n, r, targets):
    union = frozenset().union(*targets)
    u = len(union)
    states = [j for k in range(max(0, r + u - n), min(r, u) + 1)
              for j in map(frozenset, combinations(sorted(union), k))
              if not is_bad(j, targets)]
    allowed = set(states)
    q = {j: {} for j in states}
    def add(src, dst, val):
        if dst in allowed and val:
            q[src][dst] = q[src].get(dst, Fraction(0)) + val
    for j in states:
        k = len(j)
        absent = union - j
        outside = n - r - len(absent)
        for x in j:
            base = j - {x}
            add(j, base, Fraction(outside, r * (n-r)))
            for y in absent:
                add(j, base | {y}, Fraction(1, r*(n-r)))
        for_unused = r - k
        add(j, j, Fraction(for_unused * outside, r*(n-r)))
        for y in absent:
            add(j, j | {y}, Fraction(for_unused, r*(n-r)))
    z = Fraction(comb(n, r))
    initial = {j: Fraction(comb(n-u, r-len(j)), z) for j in states}
    return states, q, initial


def complete(n, r, targets):
    states = [h for h in all_sets(n,r) if not is_bad(h, targets)]
    allowed = set(states)
    q = {h: {} for h in states}
    weight = Fraction(1, r * (n-r))
    for h in states:
        for x in h:
            reduced = h - {x}
            for y in range(n):
                if y not in h:
                    nxt = reduced | {y}
                    if nxt in allowed:
                        q[h][nxt] = q[h].get(nxt, Fraction(0)) + weight
    z = Fraction(comb(n, r))
    return states, q, {h: Fraction(1,z) for h in states}


def apply(q, dist):
    out = {}
    for x, mass in dist.items():
        if mass:
            for y, p in q[x].items():
                out[y] = out.get(y, Fraction(0)) + mass*p
    return out


def exact_flux(n,r,targets):
    states = all_sets(n,r)
    entered = 0
    for h in states:
        if is_bad(h, targets):
            continue
        for x in h:
            h0 = h-{x}
            for y in range(n):
                if y not in h and is_bad(h0|{y}, targets):
                    entered += 1
    return Fraction(entered, comb(n,r)*r*(n-r))


def main():
    count = 0
    cases = []
    for n,r in ((6,2),(7,3),(8,3),(8,4),(9,4),(10,4)):
        for targets in (({0,1},),({0,1},{1,2}),({0,1},{2,3})):
            cases.append((n,r,tuple(map(frozenset, targets))))
    for n,r,targets in ((9,4,({0,1,2},)),(10,4,({0,1,2},{1,2,3})),
                          (11,5,({0,1,2},{3,4,5})),(10,5,({0,1,2},{1,2,3}))):
        cases.append((n,r,tuple(map(frozenset, targets))))
    for n,r,target_sets in cases:
        small, qs, ps = projected(n,r,target_sets)
        whole, qf, pf = complete(n,r,target_sets)
        u = frozenset().union(*target_sets)
        def project_full(dist):
            d={}
            for h,v in dist.items():
                j=h & u
                d[j]=d.get(j, Fraction(0))+v
            return d
        assert project_full(pf)==ps
        count+=1
        for t in range(8):
            assert sum(ps.values()) == sum(pf.values()), (n,r,target_sets,t)
            assert ps==project_full(pf), (n,r,target_sets,t)
            count += 2
            ps = apply(qs, ps)
            pf = apply(qf, pf)
        s=len(target_sets[0]); m=comb(n,s)
        baseline = Fraction(comb(r-1,s-1),m)
        flux=exact_flux(n,r,target_sets)
        if len(target_sets)==1:
            assert flux==baseline,(n,r,target_sets,flux,baseline)
        else:
            assert 0<flux<=len(target_sets)*baseline
        count+=1
    print('PASS',count,'exact-rational comparisons across',len(cases),'small-volume target families')
    print('Limits: tests check finite transitions, survival probabilities and stationary entrance flux only.')

if __name__=='__main__':
    main()
