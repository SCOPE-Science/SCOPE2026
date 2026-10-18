"""Finite-field checks for square-zero lifts over dual numbers.
All arithmetic is implemented here; no external packages are required.
"""
from itertools import product
from math import prod


def ops(q):
    if q in (2, 3):
        return (lambda x, y: (x+y)%q), (lambda x, y:(x*y)%q), (lambda x: (-x)%q)
    if q == 4:
        def mul(a,b):
            c = 0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1:
                        c ^= 1 << (i+j)
            if c & 4: c ^= 7  # t^2=t+1
            return c
        return (lambda x,y:x^y), mul, (lambda x:x)
    raise ValueError(q)


def mulmat(a,b,n,q):
    add,mul,_=ops(q)
    return tuple(_sumprod(((a[i*n+k],b[k*n+j]) for k in range(n)),add,mul) for i in range(n) for j in range(n))


def _sumprod(pairs,add,mul):
    s=0
    for x,y in pairs:s=add(s,mul(x,y))
    return s


def zero_square(A,n,q):
    return all(x==0 for x in mulmat(A,A,n,q))


def lin_rank(A,n,q):
    add,mul,neg=ops(q)
    cols=[]
    for j in range(n*n):
        E=(0,)*j+(1,)+(0,)*(n*n-j-1)
        U,V=mulmat(A,E,n,q),mulmat(E,A,n,q)
        cols.append(tuple(add(x,y) for x,y in zip(U,V)))
    rows=[[cols[c][r] for c in range(n*n)] for r in range(n*n)]
    rank=0
    for c in range(n*n):
        k=next((k for k in range(rank,n*n) if rows[k][c]!=0),None)
        if k is None:continue
        rows[rank],rows[k]=rows[k],rows[rank]
        inv=next(x for x in range(1,q) if mul(x,rows[rank][c])==1)
        rows[rank]=[mul(inv,x) for x in rows[rank]]
        for k in range(rank+1,n*n):
            factor=rows[k][c]
            if factor:
                rows[k]=[add(x,neg(mul(factor,y))) for x,y in zip(rows[k],rows[rank])]
        rank+=1
    return rank


def gaussian(n,r,q):
    if not 0<=r<=n:return 0
    top=prod(q**(n-i)-1 for i in range(r))
    bot=prod(q**(r-i)-1 for i in range(r))
    return top//bot


def count_rank(n,r,q):
    gl=prod(q**r-q**i for i in range(r))
    return gaussian(n,r,q)*gaussian(n-r,r,q)*gl


def predicted(n,q):
    return sum(count_rank(n,r,q)*q**(n*n-2*r*(n-r)) for r in range(n//2+1))


def verify(q,n):
    rank_count={}
    by_r={}
    total=0
    for A in product(range(q),repeat=n*n):
        if not zero_square(A,n,q): continue
        rank=lin_rank(A,n,q)
        expected_r=next((r for r in range(n//2+1) if rank==2*r*(n-r)),None)
        assert expected_r is not None,(q,n,A,rank)
        rank_count[rank]=rank_count.get(rank,0)+1
        by_r[expected_r]=by_r.get(expected_r,0)+1
        total+=q**(n*n-rank)
    for r in range(n//2+1):
        assert by_r.get(r,0)==count_rank(n,r,q),(q,n,r,by_r.get(r),count_rank(n,r,q))
    assert total==predicted(n,q),(total,predicted(n,q))
    print(f'REDUCTION_OK q={q} n={n}: strata={by_r}, lifts={total}')


def direct(q,n):
    add,mul,_=ops(q)
    count=0
    for A in product(range(q),repeat=n*n):
        if not zero_square(A,n,q):continue
        for B in product(range(q),repeat=n*n):
            U,V=mulmat(A,B,n,q),mulmat(B,A,n,q)
            if all(add(x,y)==0 for x,y in zip(U,V)):
                count+=1
    assert count==predicted(n,q),(count,predicted(n,q))
    print(f'DIRECT_OK q={q} n={n}: total={count}')

if __name__=='__main__':
    for q,n in ((2,2),(3,2),(4,2),(2,3),(3,3),(2,4)):
        verify(q,n)
    for q,n in ((2,2),(3,2),(4,2),(2,3)):
        direct(q,n)
    print('VERIFY_OK')
