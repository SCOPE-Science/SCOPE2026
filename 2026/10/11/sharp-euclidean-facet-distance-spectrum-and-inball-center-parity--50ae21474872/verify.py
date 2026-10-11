#!/usr/bin/env python3
"""Exact finite checks of a fan-graph symmetric edge polytope theorem."""
from collections import Counter
from fractions import Fraction
from itertools import product

def tight_vertex(x):
    m=len(x)
    if any(abs(x[i]-x[i+1])>1 for i in range(m-1)):
        return False
    return all(v!=0 or (i>0 and x[i-1]!=0) or (i+1<m and x[i+1]!=0)
               for i,v in enumerate(x))

def transfer(m):
    # States: +, -, satisfied 0, unsatisfied 0.
    dp={(0,(1,0,0)):1,(1,(0,1,0)):1,(3,(0,0,1)):1}
    edges={0:[(0,(1,0,0)),(2,(0,0,1))],
           1:[(1,(0,1,0)),(2,(0,0,1))],
           2:[(0,(1,0,0)),(1,(0,1,0)),(3,(0,0,1))],
           3:[(0,(1,0,0)),(1,(0,1,0))]}
    for _ in range(1,m):
        nex=Counter()
        for (state,exps),count in dp.items():
            for dest,delta in edges[state]:
                new=tuple(a+b for a,b in zip(exps,delta))
                nex[(dest,new)]+=count
        dp=nex
    hist=Counter()
    for (state,exps),count in dp.items():
        if state!=3: hist[exps]+=count
    return hist

def norm(x):
    m=len(x)
    s=sum(x)
    return Fraction(sum(v*v for v in x))-Fraction(s*s,m+1)

def rational_rank(matrix):
    if not matrix:return 0
    a=[[Fraction(q) for q in row] for row in matrix]
    h=len(a);w=len(a[0]);rank=0
    for col in range(w):
        pivot=next((i for i in range(rank,h) if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        z=a[rank][col]
        a[rank]=[t/z for t in a[rank]]
        for i in range(h):
            if i!=rank and a[i][col]:
                q=a[i][col]
                a[i]=[t-q*v for t,v in zip(a[i],a[rank])]
        rank+=1
        if rank==h:break
    return rank

def main():
    count=0
    for m in range(2,11):
        words=[x for x in product((-1,0,1),repeat=m) if tight_vertex(x)]
        brute=Counter((x.count(1),x.count(-1),x.count(0)) for x in words)
        assert brute==transfer(m),(m,'transfer unequal')
        values=[norm(x) for x in words]
        best=max(values)
        N=m+1
        if m==2:
            assert best==Fraction(2,3) and len([v for v in values if v==best])==6
        else:
            expect=Fraction(m-1)-Fraction(0 if m%2 else 1,N)
            assert best==expect,(m,best,expect)
            chosen=[x for x,v in zip(words,values) if v==best]
            assert len(chosen)==(2 if m%2 else 4)
            full_vectors=[]
            for x in chosen:
                s=sum(x)
                full_vectors.append([-s]+[N*v-s for v in x])
            rank=rational_rank(full_vectors)
            assert rank==(1 if m%2 else 2),(m,rank)
            assert m-rank==(m-1 if m%2 else m-2)
        count+=len(words)
    print('PASS: vertex tight graphs, full facet-distance multiplicity transfer matrix,')
    print('      squared polar norms, contact counts and ranks for m=2..10;')
    print('      checked',count,'exact polar vertices, no approximate arithmetic.')

if __name__=='__main__':main()
