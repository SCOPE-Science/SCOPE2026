#!/usr/bin/env python3
"""Exact independent finite verification of generic-poset one-type extrema.

Usage: python verify_second_min_poset_types.py
Uses no third-party libraries. Enumerates every distinct transitive relation
representable with one fixed linear-extension labelling for 2<=n<=6.
"""
from itertools import combinations


def closure(n, selected):
    upper = [0]*n
    for a,b in selected:
        upper[a] |= 1<<b
    for k in range(n):
        for a in range(n):
            if upper[a] & (1<<k):
                upper[a] |= upper[k]
    return upper


def type_count(n, upper):
    size=1<<n
    lower=[0]*n
    for a in range(n):
        for b in range(n):
            if (upper[a]>>b)&1:
                lower[b]|=1<<a
    ideals=[False]*size
    filters=[0]*size
    common=[0]*size
    ideals[0]=True
    filters[0]=1
    common[0]=size-1
    for mask in range(1,size):
        bit=mask&-mask
        i=bit.bit_length()-1
        rem=mask^bit
        ideals[mask]=all(not (lower[j]&~mask) for j in range(n) if mask&(1<<j))
        # Recursive filter test works as closure of each added bit.
        filters[mask]=int(all(not (upper[j]&~mask) for j in range(n) if mask&(1<<j)))
        common[mask]=common[rem]&upper[i]
    subset=filters[:]
    for i in range(n):
        for m in range(size):
            if m&(1<<i):
                subset[m]+=subset[m^(1<<i)]
    return sum(subset[common[mask]] for mask in range(size) if ideals[mask])


def near_chain_or_chain_plus_isolate(n,upper):
    comparable=lambda a,b: bool((upper[a]>>b)&1 or (upper[b]>>a)&1)
    missing=sum(not comparable(a,b) for a,b in combinations(range(n),2))
    if missing==1:
        return True
    for isolated in range(n):
        if all(not comparable(isolated,j) for j in range(n) if j!=isolated):
            rest=[j for j in range(n) if j!=isolated]
            if all(comparable(a,b) for a,b in combinations(rest,2)):
                return True
    return False


def main():
    for n in range(2,7):
        pairs=list(combinations(range(n),2))
        seen=set()
        total=0
        minimum=(n+1)*(n+2)//2
        second=minimum+n-1
        maximum=2**(n+1)-1
        witnesses=0
        for mask in range(1<<len(pairs)):
            selected=[e for i,e in enumerate(pairs) if (mask>>i)&1]
            u=closure(n,selected)
            key=tuple(u)
            if key in seen:
                continue
            seen.add(key)
            total+=1
            t=type_count(n,u)
            chain=all((u[a]>>b)&1 for a,b in pairs)
            antichain=all(x==0 for x in u)
            assert (t==minimum)==chain,('minimum',n,t,selected)
            assert (t==maximum)==antichain,('maximum',n,t,selected)
            expected=near_chain_or_chain_plus_isolate(n,u)
            assert (t==second)==expected,('runner_up',n,t,selected)
            assert minimum<=t<=maximum,('bound',n,t,selected)
            if t==second:witnesses+=1
        print('n=%d distinct_linear_extension_labeled_posets=%d runner_up_representations=%d min=%d second=%d max=%d PASS'%(n,total,witnesses,minimum,second,maximum))
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
