#!/usr/bin/env python3
"""Exact finite checks for connected Ferrers/chain graphs; standard-library only."""
from itertools import product

def graph(a, b):
    m = len(a)
    assert m and m == len(b) and min(a + b) >= 1
    A, B, v = [], [], 0
    for sizes, blocks in ((a, A), (b, B)):
        for s in sizes:
            blocks.append(list(range(v, v+s)))
            v += s
    E = [set() for _ in range(v)]
    for i in range(m):
        for j in range(i+1):
            for x in A[i]:
                for y in B[j]:
                    E[x].add(y)
                    E[y].add(x)
    return E, A, B

def canonical(a,b):
    return min((tuple(a),tuple(b)),(tuple(reversed(b)),tuple(reversed(a))))

def investigate(a,b):
    E,A,B=graph(a,b)
    n=len(E);m=len(a)
    assert all(x not in E[x] for x in range(n))
    assert all(x in E[y] for x in range(n) for y in E[x])
    todo={0};seen=set()
    while todo:
        x=todo.pop()
        if x in seen:continue
        seen.add(x);todo.update(E[x]-seen)
    assert len(seen)==n
    twins={}
    for x in range(n):twins.setdefault(frozenset(E[x]),[]).append(x)
    assert len(twins)==2*m
    classes=list(twins.values())
    inc=lambda x,y: E[x]<E[y]
    rank={x:sum(1 for C in classes if inc(C[0],x)) for x in range(n)}
    for r in range(m):
        CS=[C for C in classes if rank[C[0]]==r]
        assert len(CS)==2
        assert sorted(map(len,CS))==sorted((a[r],b[m-1-r]))
        for C in CS:assert all(rank[x]==r for x in C)
    for x in range(n):
        for y in range(n):
            common=bool(E[x]&E[y]);same=any(x in side and y in side for side in (sum(A,[]),sum(B,[])))
            assert common==same
    return len(classes)

def main():
    tested=0; twinclasses=0
    for m in range(1,4):
        for allsizes in product((1,2,3),repeat=2*m):
            a,b=allsizes[:m],allsizes[m:]
            twinclasses+=investigate(a,b)
            tested+=1
    print('verified_graphs',tested)
    print('verified_total_twin_classes',twinclasses)
    for k in range(2,5):
        for m in range(1,4):
            S=set()
            for zz in product(range(1,k+1),repeat=2*m):
                S.add(canonical(zz[:m],zz[m:]))
            assert len(S)==(k**(2*m)+k**m)//2
            print('burnside',k,m,len(S))
    print('STRUCTURE_PASS')
if __name__=='__main__':main()
