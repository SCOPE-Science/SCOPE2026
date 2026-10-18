#!/usr/bin/env python3
"""Exact finite checks for centered Lipschitz potentials of matched-pair metrics."""
from fractions import Fraction as F
from itertools import product
from math import comb


def centered_norm2(entries):
    n=len(entries)
    return sum(x*x for x in entries)-sum(entries)**2/F(n)


def states(t):
    return ((F(0),F(0)),(F(1),F(1)),(F(0),t),(t,F(0)),(F(1)-t,F(1)),(F(1),F(1)-t))


def expected(k,t):
    if k%2==0:
        return F(k,2)
    c0=F(1,2*k)
    c1=t*(1-t)+(1-t)**2/F(2*k)
    return F(k,2)-min(c0,c1)


def expected_contacts(k,t):
    if k%2==0:
        return comb(k,k//2)
    c0=F(1,2*k)
    c1=t*(1-t)+(1-t)**2/F(2*k)
    zero=2*comb(k,(k-1)//2) if c0<=c1 else 0
    one=4*comb(k,(k+1)//2)*((k+1)//2) if c1<=c0 else 0
    return zero+one


def rank(vectors):
    if not vectors: return 0
    a=[list(row) for row in vectors]
    r=0
    cols=len(a[0]); rows=len(a)
    for c in range(cols):
        pivot=next((i for i in range(r,rows) if a[i][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        x=a[r][c]
        for j in range(c,cols): a[r][j]/=x
        for i in range(r+1,rows):
            if a[i][c]:
                x=a[i][c]
                for j in range(c,cols): a[i][j]-=x*a[r][j]
        r+=1
        if r==rows:break
    return r


def verify(k,t,do_rank=False):
    n=2*k
    best=expected(k,t)
    contact=[]
    for assignment in product(states(t),repeat=k):
        f=tuple(x for pair in assignment for x in pair)
        val=centered_norm2(f)
        assert val<=best,(k,t,f,val,best)
        if val==best:
            contact.append(f)
    assert len(contact)==expected_contacts(k,t),(k,t,len(contact),expected_contacts(k,t))
    if do_rank:
        vecs=[[x-sum(f)/n for x in f] for f in contact]
        actual_rank=rank(vecs)
        predicted_rank=n-1 if k%2==1 and t>=F(2*k-2,2*k-1) else k-1
        assert actual_rank==predicted_rank,(k,t,actual_rank,predicted_rank)
    print('PASS',k,str(t),'maximum',str(best),'contacts',len(contact),'normal_rank',rank([[x-sum(f)/n for x in f] for f in contact]) if do_rank else 'not_checked')


def main():
    for k in (2,3,4,5):
        for t in (F(1,5),F(1,2),F(3,4),F(9,10),F(19,20)):
            verify(k,t,True)
    for k in (3,5):
        verify(k,F(2*k-2,2*k-1),True)
    verify(6,F(9,10),False)
    print('ALL EXACT MATCHING-METRIC CHECKS PASSED')

if __name__=='__main__': main()
