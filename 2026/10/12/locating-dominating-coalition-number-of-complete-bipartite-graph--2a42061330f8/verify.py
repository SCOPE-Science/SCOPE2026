#!/usr/bin/env python3
"""Finite stress checks for the complete-bipartite LDC classification."""
from itertools import combinations


def is_ld(m, n, D):
    A = set(range(m))
    B = set(range(m, m+n))
    D = set(D)
    for v in (A | B) - D:
        N = B if v in A else A
        if not (N & D):
            return False
    traces = []
    for v in (A | B) - D:
        N = B if v in A else A
        traces.append(frozenset(N & D))
    return len(traces) == len(set(traces))


def predicted_ld(m, n, D):
    A = set(range(m)); B = set(range(m, m+n)); D = set(D)
    a = len(D & A); b = len(D & B)
    if a and b:
        return (m-a <= 1) and (n-b <= 1)
    if D == A:
        return n == 1
    if D == B:
        return m == 1
    return False


def partitions(N):
    blocks = []
    def rec(x):
        if x == N:
            yield tuple(tuple(b) for b in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(x)
            yield from rec(x+1)
            blocks[j].pop()
        blocks.append([x])
        yield from rec(x+1)
        blocks.pop()
    yield from rec(0)


def is_ldc_partition(m, n, P):
    blocks = [set(x) for x in P]
    if any(is_ld(m,n,X) for X in blocks):
        return False
    for i, X in enumerate(blocks):
        if not any(i != j and is_ld(m,n,X | Y) for j,Y in enumerate(blocks)):
            return False
    return True


def predicted_cl(m,n):
    if (m,n)==(1,1): return None
    if (m,n)==(2,2): return 4
    return 3

subset_checks=0
for m in range(1,9):
    for n in range(1,9):
        N=m+n
        for mask in range(1<<N):
            D=[v for v in range(N) if mask>>v & 1]
            assert is_ld(m,n,D)==predicted_ld(m,n,D),(m,n,D)
            subset_checks += 1

partition_cases=0
partition_candidates=0
for m in range(1,5):
    for n in range(m,8):
        if m+n>9:
            continue
        best=None
        for P in partitions(m+n):
            partition_candidates += 1
            if is_ldc_partition(m,n,P):
                best=max(best or 0,len(P))
        assert best==predicted_cl(m,n),(m,n,best,predicted_cl(m,n))
        partition_cases += 1

print(f"ALL CHECKS PASSED; subset_checks={subset_checks}; partition_parameter_cases={partition_cases}; partition_candidates={partition_candidates}; subset_range=1<=m,n<=8; partition_range=1<=m<=n<=7,m+n<=9")
