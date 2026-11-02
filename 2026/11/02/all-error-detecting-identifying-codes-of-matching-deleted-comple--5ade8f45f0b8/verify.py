#!/usr/bin/env python3
"""Independent finite verification of the error-detecting identifying-code census.

For a complete bipartite graph with a prescribed matching removed, each
candidate set is tested directly against every closed neighborhood. The
claimed formula is evaluated separately from its structural classification.
"""
from collections import Counter
from math import comb


def candidate_polynomial(a, b, t):
    p, q = a-t, b-t
    if p < 0 or q < 0 or p > 1 or q > 1:
        return {}
    if p == q == 0:
        if t >= 5:
            return {2*t: 1, 2*t-1: 2*t, 2*t-2: t*(t-1)}
        if t == 4:
            return {8: 1, 7: 8}
        return {}
    if p+q == 1:
        if t >= 4:
            return {2*t+1:1, 2*t:t}
        if t == 3:
            return {7:1}
        return {}
    if p == q == 1 and t >= 3:
        return {2*t+2:1}
    return {}


def neighborhoods(a, b, t):
    # The first a vertices form the left side. The final b vertices
    # form the right side. The deleted edges are (i,a+i), 0<=i<t.
    ret=[]
    for i in range(a):
        bits=1<<i
        for j in range(b):
            if not (i<t and j==i):
                bits|=1<<(a+j)
        ret.append(bits)
    for j in range(b):
        bits=1<<(a+j)
        for i in range(a):
            if not (i<t and i==j):
                bits|=1<<i
        ret.append(bits)
    return ret


def graph_check(a,b,t,S):
    code=[N&S for N in neighborhoods(a,b,t)]
    if any(i.bit_count()<2 for i in code):
        return False
    for u in range(a+b):
        for v in range(u+1,a+b):
            if (code[u]&~code[v]).bit_count()<2 and (code[v]&~code[u]).bit_count()<2:
                return False
    return True


def brute(a,b,t):
    counts=Counter()
    for S in range(1<<(a+b)):
        if graph_check(a,b,t,S):
            counts[S.bit_count()]+=1
    return dict(counts)


def build_sets(a,b,t):
    p,q=a-t,b-t
    if p>1 or q>1:
        return []
    V=set(range(a+b))
    candidates=[]
    def add(omit):
        candidates.append(sum(1<<i for i in V-set(omit)))
    if p==q==0:
        if t>=4:
            add([])
            for i in range(t):
                add([i]);add([a+i])
        if t>=5:
            for i in range(t):
                for j in range(t):
                    if i!=j:add([i,a+j])
    elif p+q==1 and t>=3:
        add([])
        if t>=4:
            if p==1:
                for i in range(t):add([i])
            else:
                for i in range(t):add([a+i])
    elif p==q==1 and t>=3:
        add([])
    return candidates


def run():
    cases=0
    for a in range(2,8):
        for b in range(2,8):
            if a+b>13:
                continue
            for t in range(min(a,b)+1):
                expected=candidate_polynomial(a,b,t)
                found=brute(a,b,t)
                assert found==expected,(a,b,t,found,expected)
                represented=build_sets(a,b,t)
                assert len(represented)==len(set(represented)),(a,b,t)
                assert Counter(S.bit_count() for S in represented)==Counter(expected), (a,b,t,'structures')
                assert all(graph_check(a,b,t,S) for S in represented), (a,b,t,'witness')
                cases+=1
    large=0
    for t in (4,5,6,7,9,12,20,50):
        for p,q in ((0,0),(1,0),(0,1),(1,1)):
            a,b=t+p,t+q
            expected=candidate_polynomial(a,b,t)
            represented=build_sets(a,b,t)
            assert Counter(S.bit_count() for S in represented)==Counter(expected),(a,b,t,'count')
            assert all(graph_check(a,b,t,S) for S in represented),(a,b,t,'large witness')
            large+=1
    print(f'VERIFY_OK: {cases} full exhaustive parameter cases; {large} larger witness families')

if __name__ == '__main__':run()
