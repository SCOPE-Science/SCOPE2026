#!/usr/bin/env python3
"""Independent exhaustive field-matrix check of idempotent-product rank census."""
from collections import Counter
from itertools import product
from math import prod


def mul_scalar(a, b, q):
    if q != 4:
        return (a * b) % q
    out = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                degree = i + j
                if degree == 2:
                    out ^= 3  # alpha squared = alpha + 1
                else:
                    out ^= 1 << degree
    return out


def add_scalar(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def rank_matrix(a, n, q):
    rows = [list(a[n*i:n*(i+1)]) for i in range(n)]
    r = 0
    for j in range(n):
        piv = next((i for i in range(r,n) if rows[i][j]),None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = next(x for x in range(1,q) if mul_scalar(x,rows[r][j],q)==1)
        rows[r] = [mul_scalar(x,inv,q) for x in rows[r]]
        for i in range(n):
            if i != r and rows[i][j]:
                factor = rows[i][j]
                rows[i] = [add_scalar(x, -mul_scalar(factor,y,q) if q != 4 else mul_scalar(factor,y,q),q)
                           for x,y in zip(rows[i],rows[r])]
        r += 1
    return r


def matmul(a,b,n,q):
    return tuple(sum(mul_scalar(a[n*i+k],b[n*k+j],q) for k in range(n))%q
                 if q!=4 else xor_all(mul_scalar(a[n*i+k],b[n*k+j],q) for k in range(n))
                 for i in range(n) for j in range(n))


def xor_all(seq):
    ret=0
    for v in seq: ret ^= v
    return ret


def qchoose(m,k,q):
    if k<0 or k>m: return 0
    return prod(q**(m-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))


def I(m,r,q):
    if r<0 or r>m:return 0
    return qchoose(m,r,q)*q**(r*(m-r))


def Z(t,k,q):
    return sum(qchoose(k,j,q)*prod(q**t-q**i for i in range(j))*q**(t*(k-j))
               for j in range(min(t,k)+1))


def expected(n,r,s,t,q):
    h=s-t; k=n-r-s+t
    if not (0<=t<=r<=n and 0<=h<=n-r and k>=0):return 0
    return I(n,r,q)*I(r,t,q)*qchoose(n-r,h,q)*q**(h*k+h*(r-t))*Z(t,k,q)


def check(n,q):
    allmat=product(range(q),repeat=n*n)
    idems=[a for a in allmat if matmul(a,a,n,q)==a]
    ranks=[rank_matrix(a,n,q) for a in idems]
    observed=Counter()
    for i,e in enumerate(idems):
        for j,f in enumerate(idems):
            ef=matmul(e,f,n,q)
            if matmul(ef,ef,n,q)==ef:
                observed[(ranks[i],ranks[j],rank_matrix(ef,n,q))]+=1
    predicted={(r,s,t):expected(n,r,s,t,q)
               for r in range(n+1) for s in range(n+1) for t in range(n+1)}
    assert all(observed[key]==v for key,v in predicted.items()), (n,q,[(key,observed[key],v) for key,v in predicted.items() if observed[key]!=v])
    return len(idems),sum(observed.values()),len(observed)


def gf2_rank(m,n):
    rows=[(m>>(i*n))&((1<<n)-1) for i in range(n)]
    r=0
    for col in range(n):
        piv=next((i for i in range(r,n) if rows[i]&(1<<col)),None)
        if piv is None:continue
        rows[r],rows[piv]=rows[piv],rows[r]
        for i in range(n):
            if i!=r and rows[i]&(1<<col):rows[i]^=rows[r]
        r+=1
    return r


def gf2_product(a,b,n):
    mask=(1<<n)-1
    br=[(b>>(i*n))&mask for i in range(n)]
    result=0
    for i in range(n):
        bits=(a>>(i*n))&mask
        out=0
        for k in range(n):
            if bits&(1<<k):out^=br[k]
        result|=out<<(i*n)
    return result


def check_binary_fast(n):
    idems=[m for m in range(1<<(n*n)) if gf2_product(m,m,n)==m]
    ranks=[gf2_rank(m,n) for m in idems]
    observed=Counter()
    for i,e in enumerate(idems):
        for j,f in enumerate(idems):
            ef=gf2_product(e,f,n)
            if gf2_product(ef,ef,n)==ef:
                observed[(ranks[i],ranks[j],gf2_rank(ef,n))]+=1
    assert all(observed[r,s,t]==expected(n,r,s,t,2)
               for r in range(n+1) for s in range(n+1) for t in range(n+1))
    return len(idems),sum(observed.values()),len(observed)


def main():
    trials=[(1,2),(2,2),(3,2),(2,3),(3,3),(2,4),(2,5)]
    for n,q in trials:
        count,total,strata=check(n,q)
        print(f'FIELD_CHECK n={n} q={q} idempotents={count} valid_products={total} strata={strata}')
    count,total,strata=check_binary_fast(4)
    print(f'FIELD_CHECK n=4 q=2 idempotents={count} valid_products={total} strata={strata}')
    for n in range(1,8):
        for q in (2,3,4,5,7):
            for r in range(n+1):
                for s in range(n+1):
                    for t in range(n+1):
                        h=s-t;k=n-r-s+t
                        if not (0<=t<=r<=n and 0<=h<=n-r and k>=0):continue
                        a=expected(n,r,s,t,q)
                        b=I(n,r,q)*I(r,t,q)*I(n-r,h,q)
                        assert a>=b and a%b==0 and a//b==q**(h*(r-t))*Z(t,k,q)
    print('VERIFY_OK_IDEMPOTENT_LINEAR_PRODUCT_RANKS')
if __name__=='__main__':main()
