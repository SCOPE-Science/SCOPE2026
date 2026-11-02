#!/usr/bin/env python3
"""Independent exact extension-support census for finite level-homogeneous rooted trees.
Only standard-library Python is required.
"""
from itertools import product
from collections import defaultdict


def vertices(branch):
    nodes=[()]
    frontier=[()]
    for b in branch:
        frontier=[x+(i,) for x in frontier for i in range(b)]
        nodes+=frontier
    return nodes


def meet_depth(x,y):
    i=0
    while i<min(len(x),len(y)) and x[i]==y[i]: i+=1
    return i


def signature(items, k):
    if k==2:
        # Only order and equality are atomic in the pure strict-ancestor language.
        return tuple(len(x) for x in items)+tuple((0 if x==y else 1 if x==y[:len(x)] else 2 if y==x[:len(y)] else 3)
            for i,x in enumerate(items) for y in items[i+1:])
    return tuple(len(x) for x in items)+tuple(meet_depth(x,y) for i,x in enumerate(items) for y in items[i+1:])


def support(branch,k):
    V=vertices(branch)
    ans=defaultdict(set)
    for anchors in product(V,repeat=k-1):
        key=signature(anchors,k)
        ans[key].update(signature(anchors+(v,),k) for v in V)
    return {k:frozenset(v) for k,v in ans.items()}


def first_branch(b):
    return next((i for i,v in enumerate(b) if v>=2),len(b))


def test(h,domain,k):
    branches=list(product(domain,repeat=h))
    tables={b:support(b,k) for b in branches}
    for a in branches:
        for b in branches:
            predicted= (first_branch(a)==first_branch(b)) if k==2 else (tuple(min(k,x) for x in a)==tuple(min(k,y) for y in b))
            observed=tables[a]==tables[b]
            if predicted!=observed:
                raise AssertionError((h,k,a,b,predicted,observed))
    types=len({frozenset((a,b) for a,b in table.items()) for table in tables.values()})
    return len(branches), types


def main():
    for h,domain,k in [(0,[1],2),(1,[1,2,3,4],2),(2,[1,2,3,4],2),(3,[1,2,3],2),
                       (1,[1,2,3,4],3),(2,[1,2,3,4],3),(3,[1,2,3],3)]:
        cnt,ty=test(h,domain,k)
        print(f'PASS support h={h} k={k} profiles={cnt} distinct_types={ty}')
    for a,b,want in [((3,1),(4,1),False),((4,1),(5,1),True),((3,3),(3,4),False),((4,2),(5,2),True)]:
        observed=support(a,4)==support(b,4)
        assert observed==want,(a,b,observed,want)
        print(f'PASS support k=4 {a} versus {b}; equivalent={observed}')
    print('PASS all pairwise equivalence comparisons')

if __name__=='__main__': main()
