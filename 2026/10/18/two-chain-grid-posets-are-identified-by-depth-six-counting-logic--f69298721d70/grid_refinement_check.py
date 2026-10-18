#!/usr/bin/env python3
"""Finite cross-check for four-round counting refinement of products of chains.
No external dependencies; an independently recomputed canonical signature at each round.
"""
from collections import defaultdict


def check(m,n):
    points=[(i,j) for i in range(1,m+1) for j in range(1,n+1)]
    N=len(points)
    colors=[0]*N
    classes_by_round=[]
    for round_no in range(1,5):
        keys=[]
        for x,(i,j) in enumerate(points):
            tally=defaultdict(int)
            for y,(k,l) in enumerate(points):
                relation=0 if x==y else (1 if i<=k and j<=l else (2 if k<=i and l<=j else 3))
                tally[(relation,colors[y])]+=1
            keys.append((colors[x],tuple(sorted(tally.items()))))
        mapping={signature:index for index,signature in enumerate(sorted(set(keys)))}
        colors=[mapping[key] for key in keys]
        part=defaultdict(list)
        for pt,c in zip(points,colors):part[c].append(pt)
        classes_by_round.append(sorted(tuple(sorted(v)) for v in part.values()))
    expected=sorted(tuple(sorted({(i,j),(j,i)} & set(points))) for i in range(1,m+1) for j in range(1,n+1) if i<=j) if m==n else sorted((p,) for p in points)
    assert classes_by_round[-1]==expected,(m,n,classes_by_round[-1],expected)
    assert len(classes_by_round)==4
    return len(classes_by_round[0]),len(classes_by_round[-1])

if __name__=='__main__':
    count=0
    for m in range(2,16):
        for n in range(m,16):
            first,final=check(m,n)
            count+=1
    for m,n in [(2,22),(2,35),(3,29),(4,19),(7,17),(12,15),(17,17),(20,21)]:
        check(m,n)
        count+=1
    print(f'PASS four-round orbit classes for {count} rectangles, including all 2<=m<=n<=15')
