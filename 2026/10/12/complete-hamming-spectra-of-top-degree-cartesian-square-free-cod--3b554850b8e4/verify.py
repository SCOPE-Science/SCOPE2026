#!/usr/bin/env python3
"""Exhaustive evaluation checks for last-degree homogeneous square-free codes."""
from itertools import product
from collections import Counter
from math import comb

def field(q):
    if q in (2,3,5,7):
        return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q
    assert q in (4,8)
    degree = 2 if q==4 else 3
    poly = 0b111 if q==4 else 0b1011
    def mul(a,b):
        c=0
        while b:
            if b&1:c^=a
            b>>=1
            a<<=1
            if a & (1<<degree):a^=poly
        return c
    return lambda a,b:a^b,mul

def predicted(q,m):
    t=q-1
    w={0:0}
    for r in range(1,m+1):
        N0=(t**r+t*((-1)**r))//q
        w[r]= t**m - N0*t**(m-r)+r*t**(m-1)
    counts=Counter({0:1})
    for r in range(1,m+1):counts[w[r]]+=comb(m,r)*t**r
    return w,dict(counts)

def verify(q,m):
    add,mul=field(q)
    allx=list(product(range(q),repeat=m))
    monomial_cols=[]
    for x in allx:
        cols=[]
        for j in range(m):
            p=1
            for i in range(m):
                if i!=j:p=mul(p,x[i])
            cols.append(p)
        monomial_cols.append(cols)
    observed=Counter()
    bysupport={r:set() for r in range(m+1)}
    for coeffs in product(range(q),repeat=m):
        r=sum(a!=0 for a in coeffs)
        wt=0
        for col in monomial_cols:
            v=0
            for a,b in zip(coeffs,col):
                v=add(v,mul(a,b))
            wt+=v!=0
        observed[wt]+=1
        bysupport[r].add(wt)
    w,expected=predicted(q,m)
    assert dict(observed)==expected,(q,m,observed,expected)
    assert all(bysupport[r]=={w[r]} for r in range(m+1))
    assert sum(observed.values())==q**m
    assert (w[1]==w[2] if m>=2 else True)
    if q>2:
        assert all(w[r+1]>w[r] for r in range(2,m))
    print(f'q={q} m={m} {sorted(observed.items())}')

if __name__=='__main__':
    for q, m_values in ((2,[2,3,4,5,6]),(3,[2,3,4,5]),(4,[2,3,4]),(5,[2,3,4]),(7,[2,3]),(8,[2,3])):
        for m in m_values:verify(q,m)
    print('VERIFY_OK')
