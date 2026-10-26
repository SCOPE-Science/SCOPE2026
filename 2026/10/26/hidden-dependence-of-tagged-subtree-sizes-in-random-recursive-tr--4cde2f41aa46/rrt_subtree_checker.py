"""Exact finite checks for two tagged fringe-subtree sizes in random recursive trees.
The unrestricted theorem uses a Pólya urn argument, not this finite enumeration.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial


def exact_statistics(n):
    total = factorial(n-1)
    pairs = [(i,j) for i in range(1,n) for j in range(i+1,n+1)]
    sums = {(i,j,a):[0,0,0,0] for i,j in pairs for a in (0,1)}
    maximum = {(i,j):[0,0] for i,j in pairs}
    for choices in product(*(range(1,t) for t in range(2,n+1))):
        parent = [0,0]+list(choices)
        sizes = [1]*(n+1)
        for v in range(n,1,-1):
            sizes[parent[v]]+=sizes[v]
        for i,j in pairs:
            u=j
            while u>i:
                u=parent[u]
            a=int(u==i)
            x,y=sizes[i],sizes[j]
            row=sums[(i,j,a)]
            row[0]+=1;row[1]+=x;row[2]+=y;row[3]+=x*y
            if x==n-i+1:
                r=maximum[(i,j)];r[0]+=1;r[1]+=y
    def cv(r):
        c,sx,sy,sxy=r
        return Q(sxy,c)-Q(sx,c)*Q(sy,c) if c else None
    checks=0
    for i,j in pairs:
        neg,pos=sums[(i,j,0)],sums[(i,j,1)]
        assert neg[0]+pos[0]==total;checks+=1
        assert Q(pos[0],total)==Q(1,i);checks+=1
        sx=neg[1]+pos[1];sy=neg[2]+pos[2];sxy=neg[3]+pos[3]
        assert Q(sx,total)==Q(n,i) and Q(sy,total)==Q(n,j);checks+=2
        assert Q(sxy,total)==Q(sx*sy,total*total);checks+=1
        if i>1 and j<n:
            assert cv(pos)==Q(n*(n-j)*(i-1),(i+1)*j*(j+1));checks+=1
            assert cv(neg)==-Q(n*(n-j),(i+1)*j*(j+1));checks+=1
            assert cv(pos)>0 and cv(neg)<0;checks+=2
            ct,val=maximum[(i,j)]
            assert ct>0 and Q(val,ct)==Q(n-i+1,j-i+1)
            assert Q(val,ct)>Q(n,j);checks+=2
        else:
            if pos[0]:assert cv(pos)==0;checks+=1
            if neg[0]:assert cv(neg)==0;checks+=1
    return len(pairs),checks

if __name__=='__main__':
    nchecks=0
    for n in range(3,10):
        pairs,checks=exact_statistics(n)
        nchecks+=checks
        print(f'n={n}: {pairs} pairs, {checks} exact assertions PASS')
    print(f'TOTAL {nchecks} exact assertions PASS (all increasing-parent trees through n=9).')
