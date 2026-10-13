#!/usr/bin/env python3
from itertools import combinations
from math import comb

def graph(n):
    N=2*n+1; a=[set() for _ in range(N)]
    for v in range(1,N): a[0].add(v); a[v].add(0)
    for i in range(n):
        for j in range(n):
            if i!=j:
                x=1+i; y=1+n+j; a[x].add(y); a[y].add(x)
    return a

def vis(a,M,x,y): return y in a[x] or any(z not in M for z in a[x]&a[y])
def dual(a,M):
    V=set(range(len(a)))
    return all(vis(a,M,x,y) for S in (M,V-M) for x,y in combinations(S,2))
def pred(n,M):
    p=0
    for i in range(n):
        A=1+i; B=1+n+i
        if ((A in M)+(B in M))!=1:return False
        p+=A in M
    return 1<=p<=n-1 and p!=2 and n-p!=2

def main():
    counts={}; subsets=0
    for n in range(2,9):
        a=graph(n); N=len(a); good=[]
        for t in range(1<<(N-1)):
            M={0}|{v for v in range(1,N) if (t>>(v-1))&1}; subsets+=1
            g=dual(a,M); assert g==pred(n,M),(n,M,g,pred(n,M))
            if g:good.append(M)
        exp=sum(comb(n,p) for p in range(1,n) if p!=2 and n-p!=2); assert len(good)==exp
        if n==3: assert not good
        else:
            assert good; M=good[0]; Y=set(range(N))-M; assert dual(a,Y); assert not dual(a,set(range(N)))
        counts[n]=len(good)
    assert counts=={2:2,3:0,4:8,5:10,6:32,7:84,8:198}
    print('ALL CHECKS PASSED; n_range=2..8; hub_containing_subsets=%d; counts=%s'%(subsets,counts))
if __name__=='__main__':main()
