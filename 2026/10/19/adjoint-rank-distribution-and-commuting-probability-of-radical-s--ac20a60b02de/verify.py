#!/usr/bin/env python3
"""Independent adjoint-matrix enumeration for radical-square-zero cyclic path algebras."""
from itertools import product
from math import comb


def field(q):
    if q == 4:
        add = lambda a, b: a ^ b
        def mul(a, b):
            a0, a1 = a & 1, (a >> 1) & 1
            b0, b1 = b & 1, (b >> 1) & 1
            return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1) << 1)
        neg = lambda a: a
    else:
        add = lambda a,b: (a+b)%q
        mul = lambda a,b: (a*b)%q
        neg = lambda a: (-a)%q
    inv = {a:next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}
    return add,mul,neg,inv


def rank(rows, q, f):
    add,mul,neg,inv=f
    r=0
    for c in range(len(rows[0])):
        piv=next((j for j in range(r,len(rows)) if rows[j][c]),None)
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        k=inv[rows[r][c]]
        rows[r]=[mul(k,a) for a in rows[r]]
        for j in range(len(rows)):
            if j==r or not rows[j][c]: continue
            scale=neg(rows[j][c]); rows[j]=[add(a,mul(scale,b)) for a,b in zip(rows[j],rows[r])]
        r+=1
        if r==len(rows): break
    return r


def multiply(x,y,n,q,f):
    add,mul,_,_=f
    out=[0]*(2*n)
    for i in range(n):
        out[i]=mul(x[i],y[i])
        out[n+i]=add(mul(x[i],y[n+i]),mul(x[n+i],y[(i+1)%n]))
    return out


def brute(q,n):
    f=field(q); add,mul,neg,inv=f
    hist=[0]*(n+1)
    basis=[tuple(1 if i==j else 0 for i in range(2*n)) for j in range(2*n)]
    for x in product(range(q),repeat=2*n):
        cols=[]
        for e in basis:
            left=multiply(x,e,n,q,f)
            right=multiply(e,x,n,q,f)
            cols.append([add(a,neg(b)) for a,b in zip(left,right)])
        mat=[[cols[j][i] for j in range(2*n)] for i in range(2*n)]
        hist[rank(mat,q,f)]+=1
    return hist


def expected(q,n):
    h=[0]*(n+1)
    for k in range(n+1):
        h[k]=comb(n,k)*(q*q-1)**k+(q-1)*comb(n,k)*(-1)**k
    h[n-1]+=q*(q-1)**n
    h[n]-=q*(q-1)**n
    return h


def main():
    for q,n in ((2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(4,3),(5,2)):
        a=brute(q,n); b=expected(q,n)
        assert a==b,(q,n,a,b)
        assert sum(a)==q**(2*n)
        print(f'q={q},n={n}: {a} / OK')
    print('VERIFY_OK')

if __name__=='__main__': main()
