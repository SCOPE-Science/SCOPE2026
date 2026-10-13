#!/usr/bin/env python3
"""Exact integer verification of a cyclic adjacent-pair pooling construction."""

def columns(m):
    n=(1<<m)-1
    return [i if (i%2==0) else (1 if i%4==1 else 0) for i in range(n)]

def verify(m):
    assert isinstance(m,int) and m>=2
    n=(1<<m)-1
    x=columns(m)
    y=[x[i]|x[(i+1)%n] for i in range(n)]
    assert sorted(y)==list(range(1,n+1))
    pools=[[i for i,v in enumerate(x) if (v>>j)&1] for j in range(m)]
    assert all(len(p)==1<<(m-2) for p in pools)
    assert all(all(((i+1)%n) not in set(p) for i in p) for p in pools)
    total=sum(v.bit_count() for v in x)
    assert total==m*(1<<(m-2))
    for j in range(m):
        assert sum((z>>j)&1 for z in y)==(1<<(m-1))
    return n,total

if __name__=='__main__':
    for m in range(2,14):
        n,w=verify(m)
        print(f'm={m} n={n} incidence={w} distinct_outcomes={n} balanced=yes')
    print('VERIFY_OK')
