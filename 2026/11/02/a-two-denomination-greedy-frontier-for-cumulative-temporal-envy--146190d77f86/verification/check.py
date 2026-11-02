#!/usr/bin/env python3
"""Exact independent enumeration for sequential cumulative maximum envy claims."""
from itertools import product

def greedy_cost(weights, n):
    loads=[0]*n; ds=[]
    for w in weights:
        j=min(range(n), key=lambda i: loads[i])
        loads[j]+=w
        ds.append(max(loads)-min(loads))
    return sum(ds),ds

def exhaustive_cost(weights,n):
    best=None;bestpath=None;cnt=0
    for choices in product(range(n),repeat=len(weights)):
        loads=[0]*n;cost=0
        for x,w in zip(choices,weights):
            loads[x]+=w
            cost+=max(loads)-min(loads)
        cnt+=1
        if best is None or cost<best:
            best=cost;bestpath=choices
    return best,bestpath,cnt

if __name__=='__main__':
    cases=0; assignments=0
    for n in [2]:
        for m in range(1,11):
            for a in product((1,2),repeat=m):
                gc,_=greedy_cost(a,n);opt,_,ct=exhaustive_cost(a,n)
                assert gc==opt,(n,m,a,gc,opt)
                cases+=1;assignments+=ct
    for m in range(1,4):
        for a in product((1,2),repeat=m):
            gc,_=greedy_cost(a,3);opt,_,ct=exhaustive_cost(a,3)
            assert gc==opt,(m,a,gc,opt)
            cases+=1;assignments+=ct
    for n,weights,expected in [
        (3,(1,2,1,2),(6,5)),
        (2,(1,1,3,1),(6,4)),
        (2,(1,1,2,0),(5,3))]:
        gc,ds=greedy_cost(weights,n);opt,path,ct=exhaustive_cost(weights,n)
        assert (gc,opt)==expected,(n,weights,gc,opt)
        print('WITNESS',n,weights,'greedy_curve',ds,'greedy',gc,'optimal',opt,'witness_assignment',path)
        cases+=1; assignments+=ct
    print('VERIFY_OK cases=%d assignments=%d'%(cases,assignments))
