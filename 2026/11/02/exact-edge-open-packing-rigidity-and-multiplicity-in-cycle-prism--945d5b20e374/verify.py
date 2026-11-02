#!/usr/bin/env python3
"""Self-contained exact integer checks for edge-open packings of cycle prisms.

An edge-open packing forbids a third graph edge joining DISTINCT endpoints
of two selected edges; it allows several selected edges of an induced star.
Python >=3.8, standard library only.
"""
from itertools import combinations

KINDS = ('T', 'B', 'R')

def prism(n):
    assert n >= 3
    es = {}
    for i in range(n):
        es[('T', i)] = frozenset((('u', i), ('u', (i + 1) % n)))
        es[('B', i)] = frozenset((('v', i), ('v', (i + 1) % n)))
        es[('R', i)] = frozenset((('u', i), ('v', i)))
    return es

def conflict(e, a, b):
    A, B = e[a], e[b]
    return any(g != a and g != b and any(x != y and x in A and y in B for x in endpoints for y in endpoints)
               for g, endpoints in e.items())

def local_triples():
    es = prism(11)
    c = {frozenset((a, b)) for a, b in combinations(es, 2) if conflict(es, a, b)}
    by_offset = [set() for _ in range(3)]
    for d in range(3):
        for x in KINDS:
            for y in KINDS:
                if (x, 0) != (y, d) and frozenset(((x, 0), (y, d))) in c:
                    by_offset[d].add((x, y))
    assert by_offset[0] == {('T','B'), ('B','T')}
    assert by_offset[1] == {('B','T'), ('R','B'), ('R','R'), ('R','T'), ('T','B')}
    assert by_offset[2] == {('B','B'), ('B','R'), ('T','R'), ('T','T')}
    def chosen(mask, column):
        return [(t, column) for j, t in enumerate(KINDS) if (mask >> j) & 1]
    good=[]
    for a in range(8):
        for b in range(8):
            for cc in range(8):
                selected = chosen(a, 0) + chosen(b, 1) + chosen(cc, 2)
                if not any(frozenset((x, y)) in c for x, y in combinations(selected, 2)):
                    good.append((a,b,cc))
    assert len(good)==37
    return good

def matmul(A,B):
    N=len(A)
    cols=list(zip(*B))
    return [[sum(x*y for x,y in zip(row,col)) for col in cols] for row in A]

def matpow(A,k):
    N=len(A)
    p=[[int(i==j) for j in range(N)] for i in range(N)]
    for _ in range(k):
        p=matmul(p,A)
    return p

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def brute(n):
    es=prism(n)
    keys=list(es)
    masks=[0]*len(keys)
    for i,a in enumerate(keys):
        for j,b in enumerate(keys):
            if i!=j and conflict(es,a,b): masks[i] |= 1<<j
    best=-1; count=0
    def dfs(i, selected, weight):
        nonlocal best,count
        if weight+len(keys)-i<best:return
        if i==len(keys):
            if weight>best:best,count=weight,1
            elif weight==best:count+=1
            return
        dfs(i+1,selected,weight)
        if not (masks[i]&selected):dfs(i+1, selected|(1<<i),weight+1)
    dfs(0,0,0)
    return best,count

def formula(n):
    if n==3:return 2,12
    r=n%6
    if r==0:return n,6
    return n-1,(4*n if r in (3,5) else 2*n)

def run():
    triples=local_triples()
    states=sorted({(a,b) for a,b,c in triples}|{(b,c) for a,b,c in triples})
    assert len(states)==17
    idx={s:i for i,s in enumerate(states)}
    phi={s:int(s in ((0,5),(0,6),(1,5),(2,6))) for s in states}
    N=len(states)
    A=[[0]*N for _ in range(N)]
    B=[[0]*N for _ in range(N)]
    for a,b,c in triples:
        u,v=(a,b),(b,c)
        slack=1+phi[v]-phi[u]-c.bit_count()
        assert slack in (0,1), (u,v,slack)
        (A if slack==0 else B)[idx[u]][idx[v]]+=1
    assert sum(sum(row) for row in A)==24
    assert sum(sum(row) for row in B)==13
    assert matpow(A,8)==matpow(A,2)
    assert [trace(matpow(A,n)) for n in range(4,10)]==[0,0,6,0,0,0]
    assert [trace(matmul(matpow(A,n-1),B)) for n in range(4,10)]==[2,4,6,2,2,4]
    for n in range(4,60):
        zero=trace(matpow(A,n))
        single=n*trace(matmul(matpow(A,n-1),B))
        best,count=formula(n)
        assert (zero == count if n%6==0 else zero==0 and single==count), (n,zero,single,count)
        assert best==(n if zero else n-1)
    for n in range(3,9):
        assert brute(n)==formula(n), (n,brute(n),formula(n))
    print('VERIFY_OK states=17 triples=37 tight_arcs=24 slack_one_arcs=13 '
          'A8_eq_A2=True exact_trace_classes=6 direct_brute_n=3..8')

if __name__=='__main__':run()
