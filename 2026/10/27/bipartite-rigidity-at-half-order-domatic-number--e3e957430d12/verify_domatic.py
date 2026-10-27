#!/usr/bin/env python3
"""Independent finite verifier for the domatically perfect bipartite rigidity theorem.

Enumerates all labelled bipartite graphs with total order six or eight, and
cross-checks the exact number of two-vertex domatic partitions of K_m,m minus
any subset of diagonal matching edges, for m=3,4,5.
"""
from itertools import combinations
from math import factorial, comb

def pairs_of_perfect_matchings(vertices):
    if not vertices:
        yield ()
        return
    first=vertices[0]
    for j in range(1,len(vertices)):
        second=vertices[j]
        rem=vertices[1:j]+vertices[j+1:]
        for tail in pairs_of_perfect_matchings(rem):
            yield ((first,second),)+tail

def count_pair_partitions(neighbors):
    n=len(neighbors); full=(1<<n)-1
    valid={}
    for u in range(n):
        for v in range(u+1,n):
            seen = (1<<u)|(1<<v)|neighbors[u]|neighbors[v]
            valid[(u,v)] = seen==full
    return sum(all(valid[tuple(sorted(edge))] for edge in matching)
               for matching in pairs_of_perfect_matchings(tuple(range(n))))

def bipartite_graph(a,b,bits):
    n=a+b; neigh=[0]*n
    for i in range(a):
        for j in range(b):
            if (bits>>(i*b+j))&1:
                neigh[i] |= 1<<(a+j)
                neigh[a+j] |= 1<<i
    return neigh

def covered_by_deleted_matching(a,b,bits):
    if a!=b:return False
    deleted=[(i,j) for i in range(a) for j in range(b) if not(bits>>(i*b+j))&1]
    return len({i for i,j in deleted})==len(deleted) and len({j for i,j in deleted})==len(deleted)

def check_order(m):
    total=0; yes=0; predicted=0
    for a in range(1,m+1):
        b=2*m-a
        for bits in range(1<<(a*b)):
            total+=1
            pred=covered_by_deleted_matching(a,b,bits)
            if pred: predicted+=1
            N=bipartite_graph(a,b,bits)
            # A k-domatic coloring requires every vertex's closed neighbourhood
            # to contain each color, hence minimum degree at least k-1.
            possible=all(deg.bit_count()>=m-1 for deg in N)
            actual=bool(count_pair_partitions(N)) if possible else False
            assert actual==pred, (m,a,b,bits,actual,pred)
            if actual:yes+=1
    print(f'2m={2*m}: {total} labeled bipartite-side graphs tested; domatic-m={yes}, predicted={predicted}')
    assert yes==predicted

for m in (3,4):
    check_order(m)
for m in (3,4,5):
    for t in range(m+1):
        bits=sum(1<<(i*m+j) for i in range(m) for j in range(m) if i!=j or i>=t)
        got=count_pair_partitions(bipartite_graph(m,m,bits))
        want=factorial(m-t)
        assert got==want,(m,t,got,want)
        print(f'm={m}, deleted_matching={t}: domatic partitions={got}')
print('All exhaustive tests passed.')
