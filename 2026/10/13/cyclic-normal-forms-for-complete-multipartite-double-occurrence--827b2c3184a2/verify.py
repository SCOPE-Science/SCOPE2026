#!/usr/bin/env python3
"""Independent exhaustive checks of cyclic double-occurrence normal forms.
Requires only Python 3 standard library. Scientific definitions only.
"""
from collections import Counter
from itertools import permutations
from math import factorial


def partitions_graph(word, n):
    # Nonedge neighborhoods must be equivalence classes, with loops.
    first = [-1]*n
    second = [-1]*n
    for j, x in enumerate(word):
        if first[x]<0: first[x]=j
        else: second[x]=j
    groups = []
    pending = set(range(n))
    while pending:
        x = min(pending)
        group = {y for y in pending if x==y or not (first[x]<first[y]<second[x]<second[y] or
                   first[y]<first[x]<second[y]<second[x])}
        # For every y in group, its nonneighbors must be exactly group.
        for y in group:
            ys = {z for z in range(n) if y==z or not
                 (first[y]<first[z]<second[y]<second[z] or first[z]<first[y]<second[z]<second[y])}
            if ys!=group:
                return None
        groups.append(frozenset(group))
        pending-=group
    return groups if len(groups)>=2 else None


def is_normal_rotation(word, groups):
    n=len(word)//2
    membership={x:j for j,g in enumerate(groups) for x in g}
    w=word+word
    for shift in range(2*n):
        a=w[shift:shift+n]
        b=w[shift+n:shift+2*n]
        if len(set(a))!=n:
            continue
        blocks=[]
        j=0
        seen=set()
        valid=True
        while j<n:
            g=membership[a[j]]
            if g in seen:
                valid=False
                break
            seen.add(g)
            k=j+1
            while k<n and membership[a[k]]==g:
                k+=1
            if k-j!=len(groups[g]):
                valid=False
                break
            blocks.append(a[j:k]);j=k
        if valid and j==n and list(b)==[x for block in blocks for x in reversed(block)]:
            return True
    return False


def canonical_words(n):
    a=[0];counts=[1]+[0]*(n-1)
    def rec(next_unused):
        if len(a)==2*n:
            yield tuple(a)
            return
        for x in range(next_unused+1):
            if x==n or counts[x]==2: continue
            counts[x]+=1;a.append(x)
            yield from rec(next_unused+(x==next_unused))
            a.pop();counts[x]-=1
    yield from rec(1)


def check_canonical(max_n=7):
    for n in range(2,max_n+1):
        tested=0;valid=0
        for word in canonical_words(n):
            tested+=1
            groups=partitions_graph(word,n)
            if groups is None: continue
            valid+=1
            assert is_normal_rotation(word,groups), (n,word,groups)
        target=1
        for x in range(1,2*n,2): target*=x
        assert tested==target,(n,tested,target)
        print('CANONICAL_OK n={} exhaustive_words={} multipartite_words={}'.format(n,tested,valid))


def count_labeled(parts):
    n=sum(parts)
    membership=[]
    for j,s in enumerate(parts): membership.extend([j]*s)
    letters=tuple(range(n))
    cnt=[0]*n
    word=[]
    valid=0
    def rec():
        nonlocal valid
        if len(word)==2*n:
            first=[-1]*n;second=[-1]*n
            for i,x in enumerate(word):
                if first[x]==-1: first[x]=i
                else: second[x]=i
            for a in range(n):
                for b in range(a+1,n):
                    cross=(first[a]<first[b]<second[a]<second[b] or
                           first[b]<first[a]<second[b]<second[a])
                    if cross != (membership[a]!=membership[b]):return
            valid+=1
            return
        for x in letters:
            if cnt[x]==2:continue
            cnt[x]+=1;word.append(x)
            rec()
            word.pop();cnt[x]-=1
    rec()
    r=len(parts)
    predicted=(factorial(n) if all(s==1 for s in parts) else
               n*factorial(r-1)*__import__('math').prod(factorial(s) for s in parts))
    # For a noncomplete graph: cyclic orbits=(r-1)!prod(s!)/2,
    # hence linear words = 2n times this number.
    if all(s==1 for s in parts):
        predicted=factorial(n)
    assert valid==predicted,(parts,valid,predicted)
    print('LABELED_OK parts={} words={} predicted={}'.format(parts,valid,predicted))

if __name__=='__main__':
    check_canonical(7)
    for parts in ((1,1),(1,2),(2,2),(3,1),(2,2,1),(3,2),(1,1,3),(1,1,1,2)):
        count_labeled(parts)
    print('VERIFY_OK complete_multipartite_cyclic_normal_form')
