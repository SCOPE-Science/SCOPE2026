"""Exact coefficient arithmetic and independent exhaustive checks for crown graphs.
Run with Python 3.9+; uses only the standard library.
"""
from itertools import product
from collections import Counter
from math import comb


def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return c

def scale(a,k):return [k*v for v in a]

def sub(a,b):return add(a,scale(b,-1))

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def power(a,n):
    c=[1]
    for _ in range(n):c=mul(c,a)
    return c

def shift(a,k):return [0]*k+a

def polynomial(n):
    assert n>=2
    ones=[1]
    Q=sub(power([1,1],n-1),ones)
    def F(k):
        if not k:return [0]
        return sub(sub(power([1,1,1],k),power([1,1],k)),
                   scale(shift(power([1,1],k-1),2),k))
    U=sub(sub(power([0,1,1],n),shift([1],n)),scale(shift([1],n+1),n))
    V=sub(sub(power([1,1],n),ones),[0,n])
    p=mul(F(n),F(n))
    p=add(p,scale(shift(mul(Q,sub(F(n),F(n-1))),2),2*n))
    p=add(p,scale(mul(U,V),2))
    p=add(p,scale(shift(mul(Q,Q),4),n))
    p=add(p,scale(shift(power([1,1],2*n-4),6),n*(n-1)))
    p=add(p,scale(shift(Q,n+2),2*n))
    p=add(p,shift([1],2*n))
    assert all(v>=0 for v in p)
    return p


def direct(n):
    N=2*n
    neighbors=[[n+j if v<n else j for j in range(n) if j!=v%n] for v in range(N)]
    hist=Counter()
    for a in product((0,1,2),repeat=N):
        good=True
        for i in range(N):
            if a[i]==0:
                good=any(a[j]==2 for j in neighbors[i])
            else:
                good=any(a[j]>0 for j in neighbors[i])
            if not good:break
        if good:hist[sum(a)]+=1
    return hist


def minimum_count(n):
    if n==2:return 4,1
    if n==3:return 6,31
    return 6,n*n*(n-1)


def main():
    total=0
    for n in range(2,7):
        p=polynomial(n)
        brute=direct(n)
        exp={i:v for i,v in enumerate(p) if v}
        assert exp==dict(brute),(n,exp,brute)
        mn=min(exp)
        assert (mn,exp[mn])==minimum_count(n)
        assert p[-1]==1
        total+=3**(2*n)
        print('n=%s PASS: all %s labelings, full polynomial; min_weight=%s min_functions=%s total_valid=%s'
              %(n,3**(2*n),mn,exp[mn],sum(exp.values())))
    for n in range(7,31):
        p=polynomial(n)
        mn=next(i for i,v in enumerate(p) if v)
        assert (mn,p[mn])==minimum_count(n)
        assert p[-1]==1 and len(p)==4*n+1
    print('PASS: %s independently enumerated labelings; polynomial arithmetic through n=30.'%total)

if __name__=='__main__':main()
