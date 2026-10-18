#!/usr/bin/env python3
"""Finite consistency tests for generated neighborhoods of the fixed Box-Diamond bundle.
The infinite ZF/AC implication is proved symbolically in RESULT.md, not here.
"""
from itertools import product


def rooted_orders(n):
    """Transitive partial orders with root 0, compatible with 0<...<n-1."""
    pairs = [(i,j) for i in range(1,n) for j in range(i+1,n)]
    for bits in range(1<<len(pairs)):
        up = [1<<i for i in range(n)]
        up[0] = (1<<n)-1
        for k,(i,j) in enumerate(pairs):
            if (bits>>k)&1:
                up[i] |= 1<<j
        if all((up[i]& (1<<j))==0 or (up[j]& ~up[i])==0
               for i in range(n) for j in range(n)):
            yield tuple(up)


def maximum_chain(up):
    n=len(up)
    memo={}
    def length(i):
        if i in memo: return memo[i]
        memo[i]=1+max((length(j) for j in range(i+1,n)
                       if up[i]&(1<<j)), default=0)
        return memo[i]
    return max(map(length,range(n)))


def nbh_box_diamond(up):
    """Ding--Yang neighborhood for Box Diamond (+): union over all local witnesses."""
    n=len(up)
    certificates={0}
    for u in range(n):
        options=[1<<v for v in range(n) if up[u]&(1<<v)]
        certificates={b|option for b in certificates for option in options}
    return certificates


def check():
    order_count=valuation_count=height_two_count=0
    for n in range(1,6):
        for up in rooted_orders(n):
            order_count+=1
            h=maximum_chain(up)
            certs=nbh_box_diamond(up)
            assert certs
            for p in range(1<<n):
                valuation_count+=1
                semantic=all(bool(up[u]&p) for u in range(n))
                generated=any(c&~p==0 for c in certs)
                assert semantic==generated,(n,up,p)
                if h<=2 and semantic:
                    # At height <=2 every nonroot world is maximal; choose itself.
                    root_witness=next(v for v in range(n) if up[0]&(1<<v) and p&(1<<v))
                    selector=[root_witness]+list(range(1,n))
                    assert all(up[u]&(1<<selector[u]) and p&(1<<selector[u])
                               for u in range(n))
                    height_two_count+=1
    print(f'FINITE_VERIFY_OK rooted_orders={order_count} valuations={valuation_count} height_two_positive={height_two_count}')
    print('Logical limit: every finite family has a selector; this program cannot certify AC over arbitrary sets.')


if __name__=='__main__':
    check()
