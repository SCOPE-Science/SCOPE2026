#!/usr/bin/env python3
"""Exact arithmetic and word-level checks of a restricted universal-cycle formula.
Run: python verify.py (standard library only)."""
from itertools import permutations
from math import factorial
from fractions import Fraction
from collections import defaultdict


def permitted(q):
    result = []
    for a,b,c in permutations(range(q), 3):
        result.extend(((a,b,a,c),(a,b,c,a),(a,b,c,b)))
    return result


def graph(q):
    words = permitted(q)
    vertices = sorted({w[:3] for w in words} | {w[1:] for w in words})
    idx = {v:i for i,v in enumerate(vertices)}
    outgoing = [[] for _ in vertices]
    for i,w in enumerate(words):
        outgoing[idx[w[:3]]].append((idx[w[1:]],i))
    return words, vertices, outgoing


def count_formula(q):
    d=q-2
    assert q>=3
    p=q*(q-1)
    mplus=q*(q-3)//2
    mminus=(q-1)*(q-2)//2
    exponent=p*(q-5)//3
    assert p*(q-5)%3==0
    # Formula via transfer determinant and derivative at zero.
    trees=(Fraction(7,q*(q-1))*Fraction(7)**exponent
           *(14*d*q)**(q-1)*(6*(q-1))**mplus
           *(2*(4*q-5))**mminus)
    assert trees.denominator == 1
    return int(trees)*factorial(q-3)**p, int(trees)


def bareiss_det(A):
    n=len(A)
    B=[row[:] for row in A]
    sign=1
    prev=1
    for k in range(n-1):
        if B[k][k]==0:
            r=next((r for r in range(k+1,n) if B[r][k]!=0),None)
            if r is None:return 0
            B[k],B[r]=B[r],B[k]
            sign=-sign
        pivot=B[k][k]
        for i in range(k+1,n):
            bik=B[i][k]
            for j in range(k+1,n):
                numerator=B[i][j]*pivot-bik*B[k][j]
                assert numerator%prev==0
                B[i][j]=numerator//prev
            B[i][k]=0
        prev=pivot
    return sign*B[-1][-1]


def graph_cofactor(q):
    words,V,adj=graph(q)
    n=len(V)
    L=[[0]*n for _ in range(n)]
    for u,outs in enumerate(adj):
        L[u][u]=len(outs)
        for v,_ in outs:L[u][v]-=1
    return bareiss_det([row[:-1] for row in L[:-1]])


def witness_cycle(q):
    words,V,adj=graph(q)
    n=len(words)
    stacks=[x[:] for x in adj]
    edges=[]
    stack=[(0,None)]
    while stack:
        v,e=stack[-1]
        if stacks[v]:
            u,i=stacks[v].pop()
            stack.append((u,i))
        else:
            stack.pop()
            if e is not None:edges.append(e)
    edges.reverse()
    assert len(edges)==n
    assert sorted(edges)==list(range(n))
    assert all(words[edges[(i+1)%n]][:3]==words[edges[i]][1:] for i in range(n))
    word=[words[i][0] for i in edges]
    factors=[tuple(word[(j+t)%n] for t in range(4)) for j in range(n)]
    assert set(factors)==set(words) and len(set(factors))==n
    return ''.join(map(str,word)) if q<=10 else word


def brute_rooted(q):
    words,V,adj=graph(q)
    E=len(words)
    rootedge=next(i for i,w in enumerate(words) if w==(0,1,0,2))
    u=next(i for i,v in enumerate(V) if v==words[rootedge][:3])
    v=next(i for i,x in enumerate(V) if x==words[rootedge][1:])
    target=(1<<E)-1
    def walk(cur,used):
        if used==target:return int(cur==u)
        return sum(walk(next_v,used|(1<<edge)) for next_v,edge in adj[cur] if not used & (1<<edge))
    return walk(v,1<<rootedge)


def main():
    for q in range(3,7):
        predicted,trees=count_formula(q)
        word=witness_cycle(q)
        if q<=5:
            exact=graph_cofactor(q)
            assert exact==trees,(q,exact,trees)
        if q==3:
            exact_count=brute_rooted(q)
            assert exact_count==predicted==12
        print('q=',q,'windows=',3*q*(q-1)*(q-2),'trees=',trees,
              'cycles=',predicted, 'witness_prefix=',word[:60])
    print('VERIFY_OK')

if __name__=='__main__':main()
