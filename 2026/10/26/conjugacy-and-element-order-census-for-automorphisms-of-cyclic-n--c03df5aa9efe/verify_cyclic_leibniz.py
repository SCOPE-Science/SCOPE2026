#!/usr/bin/env python3
"""Small-field enumeration for order and conjugacy formulas.

Finite fields of sizes 2,3,4,5 are implemented directly. The algebra operations
model 1+t*F_q[t]/(t^n) and scaling of t. No external packages required.
"""
from itertools import product
from collections import Counter
from math import gcd

def field(q):
    if q==4:
        add=lambda x,y:x^y
        def mul(x,y):
            z=0
            while y:
                if y&1: z^=x
                y>>=1
                x<<=1
                if x&4:x^=7 # t^2 + t + 1
            return z
        p=2
    else:
        add=lambda x,y:(x+y)%q
        mul=lambda x,y:(x*y)%q
        p=q
    return add,mul,p

def order(a,mul,q):
    x=1
    for d in range(1,q):
        x=mul(x,a)
        if x==1:return d
    raise AssertionError

def phi(n):return sum(gcd(i,n)==1 for i in range(1,n+1))

def predicted(q,n):
    add,mul,p=field(q)
    dd=[d for d in range(1,q) if (q-1)%d==0]
    cl=sum(phi(d)*sum(phi(e)*q**((n-1)//(d*e//gcd(d,e))) for e in dd) for d in dd)//(q-1)
    hist=Counter()
    for d in dd:
        h=(n-1)//d
        factor=phi(d)*q**(n-1-h)
        Bprev=0
        for r in range(0,20):
            B=q**(h-h//p**r)
            if B>Bprev:hist[d*p**r]+=factor*(B-Bprev)
            Bprev=B
            if p**r>h:break
    return cl,hist

def brute(q,n):
    add,mul,p=field(q)
    pol=list(product(range(q),repeat=n-1))
    G=[(a,u) for a in range(1,q) for u in pol]
    idx={x:i for i,x in enumerate(G)}
    scalepowers={a: [1]+[None]*(n-1) for a in range(1,q)}
    for a in range(1,q):
        for j in range(1,n):scalepowers[a][j]=mul(scalepowers[a][j-1],a)
    def compose(g,h):
        a,u=g;b,v=h
        w=[0]*(n-1)
        for j in range(n-1):
            c=add(u[j],mul(v[j],scalepowers[a][j+1]))
            for i in range(j):
                c=add(c,mul(u[i],mul(v[j-1-i],scalepowers[a][j-i])))
            w[j]=c
        return mul(a,b),tuple(w)
    I=(1,(0,)*(n-1))
    orders=Counter()
    for g in G:
        c=I
        for s in range(1,10000):
            c=compose(c,g)
            if c==I:
                orders[s]+=1
                break
        else:raise AssertionError('element order bound')
    commuting=0
    for i,g in enumerate(G):
        for h in G:
            if compose(g,h)==compose(h,g):commuting+=1
    assert commuting%len(G)==0
    return commuting//len(G), orders

if __name__=='__main__':
    for q,n in [(2,2),(2,3),(2,5),(3,2),(3,3),(3,4),(4,3),(4,4),(5,2),(5,3),(5,4)]:
        ex_cl,ex_hist=predicted(q,n)
        br_cl,br_hist=brute(q,n)
        assert ex_cl==br_cl,(q,n,ex_cl,br_cl)
        assert ex_hist==br_hist,(q,n,ex_hist,br_hist)
        print('q=',q,'n=',n,'group=',(q-1)*q**(n-1),'classes=',ex_cl,'order_hist=',dict(sorted(ex_hist.items())))
    print('CYCLIC_LEIBNIZ_CENSUS_OK')
