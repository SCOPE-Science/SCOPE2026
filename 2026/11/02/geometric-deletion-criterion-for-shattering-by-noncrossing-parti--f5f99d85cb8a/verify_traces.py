#!/usr/bin/env python3
"""Independent direct-trace exhaustive checks for pair equality on noncrossing partitions."""
from itertools import combinations
from math import comb

def partitions(n):
    acc=[((0,),)]
    for v in range(1,n):
        nxt=[]
        for p in acc:
            nxt.append(p+((v,),))
            for i in range(len(p)):
                nxt.append(p[:i]+(p[i]+(v,),)+p[i+1:])
        acc=nxt
    return acc

def is_noncrossing(p,n):
    label=[-1]*n
    for i,b in enumerate(p):
        for x in b:label[x]=i
    for a,b,c,d in combinations(range(n),4):
        if label[a]==label[c] and label[b]==label[d] and label[a]!=label[b]:
            return False
    return True

def counts(n):
    allp=partitions(n)
    pp=[p for p in allp if is_noncrossing(p,n)]
    edges=list(combinations(range(n),2))
    masks=[]
    for a,b in edges:
        mask=0
        for i,p in enumerate(pp):
            labels=[0]*n
            for j,B in enumerate(p):
                for v in B:labels[v]=j
            if labels[a]==labels[b]:mask|=1<<i
        masks.append(mask)
    whole=(1<<len(pp))-1
    ans=[]
    for size in range(n):
        c=0
        for selected in combinations(range(len(edges)),size):
            states=[whole]
            for e in selected:
                true_mask=masks[e]
                new=[]
                for state in states:
                    a=state & true_mask
                    b=state ^ a
                    if not a or not b:
                        new=[];break
                    new.append(a);new.append(b)
                if not new:
                    states=[];break
                states=new
            if states:c+=1
        ans.append(c)
    return len(pp),ans

if __name__=='__main__':
    for n,target in [(4,[1,6,15,12]),(5,[1,10,45,90,55]),(6,[1,15,105,375,588,273]),(7,[1,21,210,1155,3276,3990,1428])]:
        k,v=counts(n)
        assert k==comb(2*n,n)//(n+1),(n,k)
        assert v==target,(n,v,target)
        print('INDEPENDENT_DIRECT_TRACES_PASS',n,'concepts',k,'fvector',v,flush=True)
    print('ALL_INDEPENDENT_TRACES_PASS')
