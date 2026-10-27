#!/usr/bin/env python3
"""Exact finite checks of the stated ternary polynomial branching formula."""
from collections import Counter

def valuation3(a):
    s=0
    while a%3==0:
        s+=1
        a//=3
    return s,a%3

def verify(k):
    n=3**k
    f=lambda x:(x*x-2)%n
    branch=list(range(2,n,3))
    marked=set()
    cycles=[]
    for x in branch:
        if x in marked:
            continue
        seq=[]
        y=x
        while y not in marked:
            marked.add(y)
            seq.append(y)
            y=f(y)
        assert y==x
        cycles.append(seq)
    assert len(marked)==3**(k-1)
    assert all(f(y) in marked for y in branch)
    assert all(f(z) in marked for z in range(1,n,3))
    assert all(f(x)%3==1 for x in range(0,n,3))
    assert all(f(f(x)) in marked for x in range(0,n,3))
    first=Counter(f(z) for z in range(1,n,3))
    assert all(first[y]==1 for y in branch)
    second=Counter(f(f(x)) for x in range(0,n,3))
    for y in branch:
        if y==2:
            b=3**(k//2)
        else:
            s,u=valuation3(y-2)
            b=2*3**(s//2) if s%2==0 and u==2 else 0
        assert second[y]==b, (k,y,second[y],b)
    for cyc in cycles:
        assert len({second[y] for y in cyc})==1
    for s in range(2,k,2):
        targets=[y for y in branch if y!=2 and valuation3(y-2)==(s,2)]
        assert len(targets)==3**(k-s-1)
        matches=[cyc for cyc in cycles if set(cyc)==set(targets)]
        assert len(matches)==1
        assert all(second[y]==2*3**(s//2) for y in targets)
    rich_cycles=[cyc for cyc in cycles if second[cyc[0]]>0]
    assert len(rich_cycles)==1+(k-1)//2
    return len(cycles)

if __name__=="__main__":
    data=[(k,verify(k)) for k in range(1,9)]
    print("VERIFY_OK",data)
