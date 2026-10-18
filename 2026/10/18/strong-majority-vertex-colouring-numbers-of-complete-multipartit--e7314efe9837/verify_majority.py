#!/usr/bin/env python3
"""Direct finite checks and constructive tests for strong-majority vertex colorings."""
from itertools import product
from functools import lru_cache
from math import comb


def partitions(n, minimum=1):
    if n==0:
        yield ()
        return
    for part in range(minimum,n+1):
        for tail in partitions(n-part,part):
            yield (part,)+tail


def valid(sizes, color_by_part):
    """Directly test the defining condition at each vertex (not the theorem formula)."""
    colors=[c for part in color_by_part for c in part]
    assert len(colors)==sum(sizes)
    base=0
    for size in sizes:
        for _ in range(size):
            neigh=colors[:base]+colors[base+size:]
            if any(neigh.count(c)*2>len(neigh) for c in set(neigh)):
                return False
        base+=size
    return True


def optimal_formula(p):
    if len(p)<2 or sum(p)-max(p)<2:
        raise ValueError('Outside the theorem domain')
    if all(x%2==0 for x in p):return 2
    if sorted(p) in ([1,1,1,1],[1,1,2]):return 4
    return 3


def first_witness(p,k):
    n=sum(p)
    for labels in product(range(k),repeat=n):
        result=[];start=0
        for s in p:
            result.append(labels[start:start+s]);start+=s
        if valid(p,result):return result
    return None


def construction(p):
    """Explicit 2/3/4 coloring, based on pair-augmentation in a single part."""
    p=tuple(p)
    k=optimal_formula(p)
    if k==2:return [[0]*(a//2)+[1]*(a//2) for a in p]
    if k==4:
        counter=0;parts=[]
        for a in p:
            parts.append(list(range(counter,counter+a)));counter+=a
        return parts
    if len(p)==2:
        return [[j%3 for j in range(a)] for a in p]
    core=[1 if a%2 else 2 for a in p]
    if sorted(core) in ([1,1,1,1],[1,1,2]):
        i=next(i for i,(a,b) in enumerate(zip(p,core)) if a>b)
        core[i]+=2
    n=sum(core)
    parts=[[] for _ in core]
    if n==3:
        parts=[[0],[1],[2]]
    elif n==5:
        twos=[i for i,a in enumerate(core) if a==2]
        for i in twos:parts[i]=[0,1]
        remaining=[0]*(2-len(twos))+[1]*(2-len(twos))+[2]
        for i,a in enumerate(core):
            if a==1:parts[i]=[remaining.pop()]
        assert not remaining
    elif n==6 and max(core)>2:
        # Three exceptional parity cores enlarged once.
        if sorted(core)==[1,1,1,3]:
            for i,a in enumerate(core):
                if a==3:parts[i]=[0,1,2]
            remain=iter([0,1,2])
            for i,a in enumerate(core):
                if a==1:parts[i]=[next(remain)]
        elif sorted(core)==[1,2,3]:
            for i,a in enumerate(core):
                parts[i]={1:[0],2:[1,2],3:[0,1,2]}[a]
        elif sorted(core)==[1,1,4]:
            for i,a in enumerate(core):
                if a==4:parts[i]=[0,1,2,2]
            remain=iter([0,1])
            for i,a in enumerate(core):
                if a==1:parts[i]=[next(remain)]
        else:raise AssertionError((p,core))
    elif n==7:
        # Pair parts each receive one of the three copies of color zero.
        for i,a in enumerate(core):
            if a==2:parts[i]=[0]
        assigned=sum(len(a) for a in parts)
        remaining=[0]*(3-assigned)+[1]*2+[2]*2
        for i,a in enumerate(core):
            while len(parts[i])<a:parts[i].append(remaining.pop())
        assert not remaining
    elif n>=8 or n==6:
        remaining=[j%3 for j in range(n)]
        for i,a in enumerate(core):
            parts[i]=remaining[:a]
            remaining=remaining[a:]
        assert not remaining
    else:raise AssertionError((p,core))
    assert valid(core,parts),(core,parts)
    for i,a in enumerate(p):
        while len(parts[i])<a:
            parts[i].extend([0,1])
    assert valid(p,parts),(p,parts)
    return parts


def main():
    small=0;binary_checked=0;trinary_checked=0
    for n in range(3,9):
        for p in partitions(n):
            if len(p)<2 or n-max(p)<2:continue
            ans=optimal_formula(p)
            assert valid(p,construction(p)),('construction',p)
            got2=first_witness(p,2) is not None
            assert got2==(ans==2),(p,2,got2,ans)
            binary_checked+=1
            got3=first_witness(p,3) is not None
            assert got3==(ans<=3),(p,3,got3,ans)
            trinary_checked+=1
            small+=1
    print('EXHAUSTIVE:',small,'unlabeled multipartite types, sizes 3..8;',binary_checked,'2-color tests;',trinary_checked,'3-color tests.')
    count=0
    for n in range(3,26):
        for p in partitions(n):
            if len(p)<2 or n-max(p)<2:continue
            w=construction(p)
            assert valid(p,w),(p,w)
            count+=1
    print('CONSTRUCTIVE:',count,'unlabeled multipartite types, sizes 3..25.')
    # Stress unbalanced large sizes and parity cores, independent direct validation.
    large=[(2,1001),(1,1,1000),(1,2,999),(1,1,1,1000),
           (1,1,2,1001),(1,1,1,1,1000),(100,101,102),(101,103,105,107)]
    for p in large:
        assert valid(p,construction(p)),p
    print('LARGE:',len(large),'stress profiles checked. ALL PASSED')
if __name__=='__main__':main()
