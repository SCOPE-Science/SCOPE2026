#!/usr/bin/env python3
"""Exact low-weight graph flip search on three classical cubic graphs."""
from itertools import combinations
from collections import Counter

def petersen():
    pts=list(combinations(range(5),2))
    return list(range(10)), [(i,j) for i in range(10) for j in range(i+1,10) if not(set(pts[i])&set(pts[j]))]

def heawood():
    return list(range(14)), [(p,7+k) for k in range(7) for p in {(k+d)%7 for d in (0,1,3)}]

def dodecahedron():
    return list(range(20)), [(i,(i+1)%10) for i in range(10)]+[(i,10+i) for i in range(10)]+[(10+i,10+(i+2)%10) for i in range(10)]

def run(name,gen,expected):
    V,E=gen(); E=[tuple(sorted(e)) for e in E]; assert len(set(E))==len(E)
    assert all(sum(v in e for e in E)==3 for v in V)
    m=len(E); neighbor=[0]*m
    for i,e in enumerate(E):
        for j,f in enumerate(E):
            if i!=j and (set(e)&set(f)):neighbor[i] |= 1<<j
    assert all(x.bit_count()==4 for x in neighbor)
    winners=[]; best=99
    for k in range(1,6):
        for C in combinations(range(m),k):
            mask=sum(1<<x for x in C)
            # Direct local operation: supports on chosen vertices plus odd neighborhood outside.
            extra=sum(1 for j in range(m) if not(mask>>j&1) and (neighbor[j]&mask).bit_count()%2)
            weight=k+extra
            if weight<best:best=weight; winners=[C]
            elif weight==best:winners.append(C)
    assert best==5,(name,best)
    sizes=Counter(map(len,winners))
    assert dict(sizes)==expected,(name,sizes,expected)
    print(name,'|E|',m,'min_support',best,'witnesses',len(winners),'support_sizes',dict(sizes))

if __name__=='__main__':
    run('Petersen',petersen,{1:15,5:18})
    run('Heawood',heawood,{1:21})
    run('Dodecahedral',dodecahedron,{1:30,5:12})
    print('DIRECT_LINEGRAPH_FLIP_PASS')
