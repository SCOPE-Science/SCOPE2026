#!/usr/bin/env python3
from itertools import combinations


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def closed_neighborhoods(parts):
    part_of=[]
    for i,m in enumerate(parts):
        part_of += [i]*m
    n=len(part_of)
    return part_of, [tuple(u for u in range(n) if u==v or part_of[u]!=part_of[v]) for v in range(n)]


def is_k_tuple(mask, closed, k):
    return all(sum((mask >> u) & 1 for u in nb) >= k for nb in closed)


def is_minimal(mask, closed, k, n):
    if not is_k_tuple(mask, closed, k):
        return False
    for u in range(n):
        if (mask >> u) & 1 and is_k_tuple(mask & ~(1 << u), closed, k):
            return False
    return True

profiles=0
parameter_checks=0
subset_checks=0
minimal_sets=0
construction_checks=0
max_order=10
for n in range(2,max_order+1):
    for parts in partitions(n):
        if len(parts) < 2:
            continue
        profiles += 1
        L=max(parts)
        delta=n-L
        part_of,closed=closed_neighborhoods(parts)
        for k in range(1,delta+2):
            parameter_checks += 1
            max_minimal=-1
            for mask in range(1<<n):
                subset_checks += 1
                if is_minimal(mask,closed,k,n):
                    minimal_sets += 1
                    max_minimal=max(max_minimal,mask.bit_count())
            expected=L+k-1
            assert max_minimal==expected,(parts,k,max_minimal,expected)
            for i,m in enumerate(parts):
                if m != L:
                    continue
                outside=[v for v in range(n) if part_of[v]!=i]
                whole=[v for v in range(n) if part_of[v]==i]
                for T in combinations(outside,k-1):
                    mask=0
                    for v in whole+list(T): mask |= 1<<v
                    construction_checks += 1
                    assert mask.bit_count()==expected
                    assert is_minimal(mask,closed,k,n),(parts,k,i,T)
print(f"VERIFY_OK profiles={profiles} parameter_checks={parameter_checks} subset_checks={subset_checks} minimal_sets={minimal_sets} construction_checks={construction_checks} max_order={max_order}")
