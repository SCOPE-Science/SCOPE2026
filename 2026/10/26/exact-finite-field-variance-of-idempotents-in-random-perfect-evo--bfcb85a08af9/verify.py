#!/usr/bin/env python3
"""Direct finite checks for the nonzero-idempotent variance identity."""
from itertools import product
from fractions import Fraction

def finite_field(q):
    if q == 4:
        # GF(2)[t]/(t^2+t+1): low and high bits.
        add=lambda a,b:a^b
        def mul(a,b):
            z=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1:
                        z^=1<<(i+j)
            if z&4:z^=0b111
            return z
        return add,mul
    assert q in (2,3,5,7)
    return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q

def rank(matrix, q, add, mul):
    if not matrix:return 0
    rows=[list(r) for r in matrix]
    n=len(rows); m=len(rows[0]); r=0
    for j in range(m):
        piv=next((i for i in range(r,n) if rows[i][j]), None)
        if piv is None:continue
        rows[r],rows[piv]=rows[piv],rows[r]
        inv=next(x for x in range(1,q) if mul(x,rows[r][j])==1)
        rows[r]=[mul(x,inv) for x in rows[r]]
        for i in range(n):
            if i!=r and rows[i][j]:
                c=rows[i][j]
                # subtraction equals addition only in even characteristic
                negc=c if q in (2,4) else q-c
                rows[i]=[add(a,mul(negc,b)) for a,b in zip(rows[i],rows[r])]
        r+=1
        if r==n:break
    return r

def direct(q,n):
    add,mul=finite_field(q)
    vs=list(product(range(q), repeat=n))
    target=vs[1:]
    sq={v:tuple(mul(x,x) for x in v) for v in target}
    hist={}
    total=0
    for vals in product(range(q), repeat=n*n):
        rows=[vals[i*n:(i+1)*n] for i in range(n)]
        if rank(rows,q,add,mul)!=n:continue
        total+=1
        N=0
        for v in target:
            w=sq[v]
            out=tuple(sum((mul(rows[i][j],w[j]) for j in range(n)),0)%q for i in range(n)) if q!=4 else tuple(__import__('functools').reduce(add,(mul(rows[i][j],w[j]) for j in range(n)),0) for i in range(n))
            N += (out==v)
        hist[N]=hist.get(N,0)+1
    mean=Fraction(sum(k*v for k,v in hist.items()),total)
    var=Fraction(sum((k*k)*v for k,v in hist.items()),total)-mean*mean
    if n==1:want=Fraction(0)
    elif q%2==0:want=Fraction(1)
    else:want=Fraction(1)-Fraction((q-1)*((2*q-1)**n-2*q**n+1),2*(q**n-1)*(q**n-q))
    assert mean==1 and var==want,(q,n,total,hist,mean,var,want)
    print('OK',q,n,'invertible',total,'variance',str(var),'distribution',sorted(hist.items()))

if __name__=='__main__':
    for q,n in [(2,1),(3,1),(2,2),(3,2),(4,2),(5,2),(7,2),(2,3),(3,3),(2,4)]:
        direct(q,n)
    print('VERIFY_OK')
