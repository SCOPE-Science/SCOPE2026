#!/usr/bin/env python3
"""Standalone checks for minimal absent subsequences of alternating binary words.
No external packages are needed.
"""
from itertools import product
from collections import Counter


def sub(v,w):
    p=0
    for c in w:
        if p<len(v) and c==v[p]:
            p+=1
    return p==len(v)

def is_mas(v,w):
    return not sub(v,w) and all(sub(v[:i]+v[i+1:], w) for i in range(len(v)))

def criterion(v,m):
    if len(v)<2:return False
    first_one=int(v[0]=='1')
    eq=sum(v[i]==v[i+1] for i in range(len(v)-1))
    cost=len(v)+first_one+eq
    if v.startswith('01') or '010' in v or '101' in v:return False
    return cost==2*m+1 or (cost==2*m+2 and v[-2]==v[-1])

def polynomial_add(*ps):
    out=Counter()
    for p in ps:
        out.update(p)
    return {k:v for k,v in out.items() if v}

def shift(p,k):return {i+k:v for i,v in p.items()}

def scale(p,c):return {i:c*v for i,v in p.items()}

def polys(m):
    # Extracted by formal power-series coefficient comparison, no symbolic library.
    p={0:{},1:{2:3},2:{3:4,4:1},3:{4:5,5:4}}
    for j in range(4,m+1):
        p[j]=polynomial_add(scale(shift(p[j-1],1),2),scale(shift(p[j-2],2),-1),shift(p[j-3],4))
    return p

def run_tests():
    tab=polys(30)
    totals=[3,5,9,16,28,49,86,151,265,465,816,1432]
    assert [sum(tab[m].values()) for m in range(1,13)]==totals
    # Direct definition versus structural characterization, exhaustive by m and length.
    for m in range(1,9):
        w='01'*m
        observed=Counter()
        for length in range(1,2*m+2):
            for v in map(''.join,product('01',repeat=length)):
                actual=is_mas(v,w)
                predicted=criterion(v,m)
                if actual!=predicted:
                    raise AssertionError(('criterion mismatch',m,v,actual,predicted))
                if actual: observed[length]+=1
        assert dict(observed)==tab[m], ('coefficient mismatch',m,dict(observed),tab[m])
        assert observed[m+1]==m+2
        assert max(observed)==(4*(m+1))//3
        print(m,dict(sorted(observed.items())))
    # A distinct check that the cost formula exactly characterizes embedding.
    for m in range(1,7):
        w='01'*m
        for length in range(1,2*m+2):
            for v in map(''.join,product('01',repeat=length)):
                f=length+int(v[0]=='1')+sum(v[i]==v[i+1] for i in range(length-1))
                assert sub(v,w)==(f<=2*m), (m,v,f)
    print('VERIFY_OK')

if __name__=='__main__':run_tests()
