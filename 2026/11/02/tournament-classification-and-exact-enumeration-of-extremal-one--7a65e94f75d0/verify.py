#!/usr/bin/env python3
"""Exact finite tests for ternary trifferent codes with one occurrence of symbol 2.
Standalone, standard library only; no external data or solver.
"""
from itertools import combinations, product

def triple_separates(a,b,c):
    return any({x,y,z}=={0,1,2} for x,y,z in zip(a,b,c))

def trifferent(words):
    return all(triple_separates(*triple) for triple in combinations(words,3))

def unordered_pairs_at(n,i):
    js=[j for j in range(n) if j!=i]
    out=[]
    for bits in product((0,1),repeat=n-1):
        if bits[0]!=0: continue # choose one of each complementary pair
        a=[0]*n;b=[0]*n
        a[i]=b[i]=2
        for j,x in zip(js,bits): a[j]=x;b[j]=1-x
        out.append((tuple(a),tuple(b)))
    return out

def tournament_code(n,edges):
    e={(i,j):val for (i,j),val in edges.items()}
    a=[[0]*n for _ in range(n)]
    for i in range(n):
        a[i][i]=2
        for j in range(n):
            if i!=j:
                a[i][j]=e[(min(i,j),max(i,j))] if i<j else 1-e[(j,i)]
    return tuple(tuple(a[i]) for i in range(n))+tuple(tuple(2 if i==j else 1-a[i][j] for j in range(n)) for i in range(n))

for n in range(2,6):
    choices=[unordered_pairs_at(n,i) for i in range(n)]
    seen=set()
    count=0
    for selected in product(*choices):
        words=tuple(w for pair in selected for w in pair)
        if trifferent(words):
            count+=1
            seen.add(frozenset(words))
    predicted=1<<(n*(n-1)//2-1)
    assert count==predicted,(n,count,predicted)
    assert len(seen)==count
    edges_list=list(combinations(range(n),2))
    from_tournaments=set()
    for bits in product((0,1),repeat=len(edges_list)):
        words=tournament_code(n,dict(zip(edges_list,bits)))
        assert trifferent(words)
        from_tournaments.add(frozenset(words))
    assert seen==from_tournaments
    print('n=%d expected_and_verified_labeled_maxima=%d tournaments=%d'%(n,count,2**len(edges_list)))
print('TRIFFERENT_ONE2_TOURNAMENT_CLASSIFICATION_OK')
