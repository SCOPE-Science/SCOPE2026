#!/usr/bin/env python3
from itertools import product
from math import comb
from collections import Counter


def build_graph(parts):
    groups=[]; part_of={}; off=0
    for i,n in enumerate(parts):
        vs=list(range(off,off+n)); off += n; groups.append(vs)
        for v in vs: part_of[v]=i
    adj={v:set() for v in range(off)}
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            for u in groups[i]:
                for v in groups[j]:
                    adj[u].add(v); adj[v].add(u)
    return groups, adj


def psd_forces(parts, blue):
    groups,adj=build_graph(parts)
    V=set(adj); blue=set(blue)
    while True:
        white=V-blue
        if not white:
            return True
        rem=set(white); comps=[]
        while rem:
            root=rem.pop(); comp={root}; stack=[root]
            while stack:
                u=stack.pop()
                for v in list(adj[u] & rem):
                    rem.remove(v); comp.add(v); stack.append(v)
            comps.append(comp)
        moved=False
        for comp in comps:
            for u in tuple(blue):
                targets=adj[u] & comp
                if len(targets)==1:
                    blue.add(next(iter(targets))); moved=True; break
            if moved:
                break
        if not moved:
            return False


def criterion(parts, blue):
    groups,_=build_graph(parts)
    w=[sum(v not in blue for v in group) for group in groups]
    positive=[i for i,a in enumerate(w) if a>0]
    if len(positive)<=1:
        return True
    return any(0<w[i]<parts[i] and sum(w[j] for j in range(len(w)) if j!=i)==1
               for i in positive)


def formula_coefficients(parts):
    N=sum(parts); coeff=[0]*(N+1); coeff[N]=1
    for n in parts:
        for k in range(n):
            coeff[N-n+k] += comb(n,k)
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            a,b=parts[i],parts[j]; shift=N-a-b
            for kb in range(1,b):
                coeff[shift+a-1+kb] += a*comb(b,kb)
            for ka in range(1,a):
                coeff[shift+b-1+ka] += b*comb(a,ka)
            if a>=2 and b>=2:
                coeff[shift+a+b-2] -= a*b
    return coeff


def main():
    profiles=subset_checks=criterion_checks=coefficient_checks=minimum_checks=0
    max_order=0
    for r in range(2,5):
        for parts in product(range(1,5), repeat=r):
            N=sum(parts)
            if N>11:
                continue
            profiles += 1; max_order=max(max_order,N)
            brute=Counter()
            for mask in range(1<<N):
                blue={v for v in range(N) if (mask>>v)&1}
                actual=psd_forces(parts,blue)
                predicted=criterion(parts,blue)
                subset_checks += 1; criterion_checks += 1
                assert actual == predicted, (parts,mask,actual,predicted)
                if actual:
                    brute[len(blue)] += 1
            formula=formula_coefficients(parts)
            for k in range(N+1):
                coefficient_checks += 1
                assert brute[k] == formula[k], (parts,k,brute[k],formula[k])
            minimum_checks += 1
            observed=min(brute)
            expected=N-max(parts)
            assert observed == expected, (parts,observed,expected)
    print(f"VERIFY_OK profiles={profiles} subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order={max_order}")

if __name__ == '__main__':
    main()
