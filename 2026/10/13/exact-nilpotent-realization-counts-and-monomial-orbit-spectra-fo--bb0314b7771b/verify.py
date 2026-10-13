#!/usr/bin/env python3
"""Finite-field checks for weighted cyclic matrices with nonzero loops.
Standard library only. Output VERIFY_OK iff independent finite enumerations agree.
"""
import itertools
import math
from collections import Counter


def field(p, modulus=None):
    if modulus is None:
        q = p
        return q, [[(a+b)%p for b in range(q)] for a in range(q)], [[(a*b)%p for b in range(q)] for a in range(q)]
    deg=len(modulus)-1
    q=p**deg
    def coeffs(a):
        v=[]
        for i in range(deg):
            v.append(a%p)
            a//=p
        return v
    def enc(cs):
        return sum(int(c)*p**i for i,c in enumerate(cs))
    add=[[0]*q for _ in range(q)]
    mul=[[0]*q for _ in range(q)]
    for a in range(q):
        ca=coeffs(a)
        for b in range(q):
            cb=coeffs(b)
            add[a][b]=enc([(ca[i]+cb[i])%p for i in range(deg)])
            c=[0]*(2*deg-1)
            for i in range(deg):
                for j in range(deg):
                    c[i+j]=(c[i+j]+ca[i]*cb[j])%p
            for k in range(2*deg-2,deg-1,-1):
                z=c[k]
                for j in range(deg):
                    c[k-deg+j]=(c[k-deg+j]-z*modulus[j])%p
            mul[a][b]=enc(c[:deg])
    return q,add,mul


def neg(a, add):
    for b in range(len(add)):
        if add[a][b]==0: return b
    raise AssertionError


def poly_product_roots(diag, add, mul):
    # Polynomial coefficients in ascending order.
    cs=[1]
    for a in diag:
        aa=neg(a,add)
        nxt=[0]*(len(cs)+1)
        for j,c in enumerate(cs):
            nxt[j]=add[nxt[j]][mul[c][aa]]
            nxt[j+1]=add[nxt[j+1]][c]
        cs=nxt
    return cs


def is_nilpotent_direct(diag, product, add, mul):
    n=len(diag)
    a=[[0]*n for _ in range(n)]
    for i in range(n):
        a[i][i]=diag[i]
        a[i][(i+1)%n]=product if i==n-1 else 1
    eye=[[int(i==j) for j in range(n)] for i in range(n)]
    v=eye
    for power in range(1,n+1):
        v=[[sum_field([mul[v[i][k]][a[k][j]] for k in range(n)],add) for j in range(n)] for i in range(n)]
        if power==n-1: assert any(any(row) for row in v),('not regular',diag,product)
    return not any(any(row) for row in v)


def sum_field(ls,add):
    z=0
    for k in ls: z=add[z][k]
    return z


def mobius(k):
    if k==1: return 1
    z=0
    d=2
    while d*d<=k:
        if k%d==0:
            k//=d
            if k%d==0:return 0
            z+=1
            while k%d==0:k//=d
        d+=1
    if k>1:z+=1
    return -1 if z%2 else 1


def divs(n):
    return [d for d in range(1,n+1) if n%d==0]


def expected(q,p,n):
    h=1
    m=n
    while m%p==0:
        m//=p
        h*=p
    if (q-1)%m: return 0, {}
    count=(q-1)**n//m * math.factorial(n)//math.prod(math.factorial(h) for _ in range(m))
    f={d:math.factorial(d)//math.factorial(h*d//n)**m if h%(n//d)==0 else 0 for d in divs(n)}
    period={d:sum(mobius(d//e)*f[e] for e in divs(d))//d*((q-1)//m) for d in divs(n)}
    return count,{d:k for d,k in period.items() if k}


def run(p,modulus,n):
    q,add,mul=field(p,modulus)
    nonzero=list(range(1,q))
    sols=[]
    for diag in itertools.product(nonzero,repeat=n):
        f=poly_product_roots(diag,add,mul)
        if any(f[j] for j in range(1,n)):continue
        for w in nonzero:
            if f[0]!=w:continue
            assert is_nilpotent_direct(diag,w,add,mul)
            sols.append((diag,w))
    # Each (diagonal, product) admits (q-1)^(n-1) distinct edge assignments.
    actual=len(sols)*(q-1)**(n-1)
    predicted,period=expected(q,p,n)
    assert actual==predicted,('total',p,q,n,actual,predicted)
    orbits={}
    for diag,w in sols:
        key=(min(diag[i:]+diag[:i] for i in range(n)),w)
        orbits[key]=len({diag[i:]+diag[:i] for i in range(n)})
    periods=dict(Counter(orbits.values()))
    assert periods==period,('periods',p,q,n,periods,period)
    assert sum((q-1)**(n-1)*d*amount for d,amount in periods.items())==actual
    print('q=%d n=%d: matrices=%d, orbits_by_period=%s'%(q,n,actual,dict(sorted(periods.items()))))

if __name__=='__main__':
    for p,mod,n in [
        (2,None,3),(2,None,4),(2,None,6),
        (3,None,3),(3,None,4),
    ]:
        run(p,mod,n)
    for p,mod,n in [(2,[1,1,1],3),(2,[1,1,1],4),(2,[1,1,1],6),
                    (5,None,3),(5,None,4),(7,None,3),
                    (3,[1,0,1],3),(3,[1,0,1],4)]:
        run(p,mod,n)
    print('VERIFY_OK')
