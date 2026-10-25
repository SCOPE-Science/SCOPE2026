#!/usr/bin/env python3
"""Independent finite verification of the two-row matched-clique sub-quorum theorem.

Public mathematical data only. Python >=3.9, standard library.
"""
from itertools import combinations
from math import comb, factorial

def predicted(n):
    return sum(comb(n,2*a)*comb(n-2*a,2*b)*comb(2*a,a)*comb(2*b,b)//4
               for a in range(1,n//2+1) for b in range(1,(n-2*a)//2+1))

def valid(v,n):
    # 0 represents an uncoloured vertex; remaining positive integers are colors.
    for p,c in enumerate(v):
        if not c: continue
        row,col=divmod(p,n)
        same=sum(v[row*n+j]==c for j in range(n))
        rowcount=sum(v[row*n+j]!=0 for j in range(n))
        other=v[(1-row)*n+col]
        same+=int(other==c)
        total=rowcount+int(other!=0)
        if 2*same<total:return False
    return True

def shape(v,n):
    top=v[:n];bottom=v[n:]
    if len(set(top)-{0})!=2 or len(set(bottom)-{0})!=2:return False
    if (set(top)-{0}) & (set(bottom)-{0}):return False
    I={i for i,c in enumerate(top) if c};J={i for i,c in enumerate(bottom) if c}
    if I&J or len(I)%2 or len(J)%2:return False
    return all(top.count(c)==len(I)//2 for c in set(top)-{0}) and all(bottom.count(c)==len(J)//2 for c in set(bottom)-{0})

def check(n):
    N=2*n;v=[0]*N
    best=0;count=0;good=0;examined=0
    def rec(p,maxcolor):
        nonlocal best,count,good,examined
        if p==N:
            examined+=1
            if not valid(v,n):return
            if maxcolor>best:best=maxcolor;count=0;good=0
            if maxcolor==best:
                count+=1
                if shape(v,n):good+=1
            return
        v[p]=0;rec(p+1,maxcolor)
        for c in range(1,maxcolor+2):
            v[p]=c;rec(p+1,max(maxcolor,c))
    rec(0,0)
    expected=min(n,4)
    assert best==expected,(n,best,expected)
    if n>=4:
        assert count==predicted(n),(n,count,predicted(n))
        assert good==count,(n,good,count)
    print('n=%d all_partitions=%d optimum=%d optimal_unlabelled=%d classified=%d' % (n,examined,best,count,good),flush=True)

for n in range(2,6):check(n)
for n in range(4,13):
    num=predicted(n)
    assert num>0
    print('n=%d formula_count=%d' %(n,num))
print('VERIFY_OK')
