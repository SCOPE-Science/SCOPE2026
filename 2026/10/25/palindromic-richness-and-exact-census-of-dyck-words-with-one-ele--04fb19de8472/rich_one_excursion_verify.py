#!/usr/bin/env python3
"""Reproduce palindromic factor formulas for one elevated excursion."""
from itertools import product

def word(a,u,v):
    return '01'*u+'0'+'01'*a+'1'+'01'*v

def pal_count_direct(w):
    seen=set()
    for i in range(len(w)):
        for j in range(i+1,len(w)+1):
            p=w[i:j]
            if p==p[::-1]:seen.add(p)
    return len(seen)

def analytic(a,u,v):
    m0=max(a,u+(u%2==0),v+(v%2==1))
    m1=max(a,u+(u%2==1),v+(v%2==0))
    return m0+m1+min(2*u+1,2*a)+min(2*v+1,2*a)

def count_formula(n):
    if n<2:return 0
    t=(n-1)//3
    return t*(t+1)+(n-t-1)*(n-t)//2+int((n-1)%3==0)

def run():
    checks=0
    for a in range(1,22):
        for u in range(0,22):
            for v in range(0,22):
                w=word(a,u,v)
                actual=pal_count_direct(w)
                formula=analytic(a,u,v)
                assert actual==formula,(a,u,v,actual,formula)
                assert (actual==len(w))==(min(u,v)<a or u==v==a),(a,u,v)
                checks+=1
    for n in range(2,41):
        direct=sum(1 for a in range(1,n) for u in range(n-a) for v in [n-a-1-u] if pal_count_direct(word(a,u,v))==2*n)
        assert direct==count_formula(n),(n,direct,count_formula(n))
    print('RICH_SINGLE_EXCURSION_PASS triples=',checks,'n=2..40')
if __name__=='__main__':run()
