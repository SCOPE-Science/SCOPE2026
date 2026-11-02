#!/usr/bin/env python3
"""Finite checks for the rank-two toric positroid enumeration and F3 correspondence."""
from itertools import combinations, product
from collections import Counter
from math import comb

def partitions(m):
    result = [((0,),)]
    for x in range(1, m):
        nxt = []
        for p in result:
            for j in range(len(p)):
                q = list(p)
                q[j] = q[j] + (x,)
                nxt.append(tuple(q))
            nxt.append(p + ((x,),))
        result = nxt
    return result

def cyclic_interval(block, m):
    b = frozenset(block)
    return any(b == frozenset((i+j)%m for j in range(len(b))) for i in range(m))

def toric_histogram(n):
    d = Counter()
    for m in range(2, n+1):
        for c in (2, 3):
            if c <= m:
                d[m+c-4] += comb(n,m)*comb(m,c)
    return d

def expected_histogram(n):
    d=Counter()
    for j in range(n-1):
        d[j] = comb(n,2)*(comb(n-2,j) if 0<=j<=n-2 else 0)
        if n>=3 and 0<=j-2<=n-3:
            d[j] += comb(n,3)*comb(n-3,j-2)
    return d

def rank2_positive_f3_histogram(n):
    hist=Counter()
    seen_supports=set()
    for i,j in combinations(range(n),2):
        left=range(i+1,j)
        right=range(j+1,n)
        for middles in product(range(3),repeat=len(left)):
            for ends in product(product(range(3), repeat=2), repeat=len(right)):
                cols=[(0,0)]*n
                cols[i]=(1,0)
                cols[j]=(0,1)
                for t,a in zip(left,middles):cols[t]=(a,0)
                for t,v in zip(right,ends):cols[t]=v
                def det(a,b):return (a[0]*b[1]-a[1]*b[0])%3
                minors={(a,b):det(cols[a],cols[b]) for a,b in combinations(range(n),2)}
                if 2 in minors.values():
                    continue
                support=frozenset(pair for pair,v in minors.items() if v==1)
                assert support not in seen_supports, (n, support)
                seen_supports.add(support)
                for a,b,c,d in combinations(range(n),4):
                    assert minors[a,b]*minors[c,d]-minors[a,c]*minors[b,d]+minors[a,d]*minors[b,c]==0

                supp=[x for x in cols if x != (0,0)]
                cls={}
                for v in supp:
                    repr_v = (1, (v[1]*pow(v[0],-1,3))%3) if v[0] else (0,1)
                    cls[repr_v]=1
                m=len(supp)
                c=len(cls)
                assert c in (2,3)
                hist[m+c-4]+=1
    return hist

def algebraic_checks():
    for m in range(2,9):
        counts=Counter()
        for p in partitions(m):
            if len(p)>=2 and all(cyclic_interval(block,m) for block in p):
                counts[len(p)]+=1
        for c in range(2,m+1):
            assert counts[c]==comb(m,c),(m,c,counts[c],comb(m,c))
    for n in range(2,11):
        d=toric_histogram(n)
        e=expected_histogram(n)
        assert all(d[j]==e[j] for j in range(n-1))
        assert sum(d.values())==comb(n,2)*2**(n-2)+(comb(n,3)*2**(n-3) if n>=3 else 0)
        total=sum(comb(n,m)*sum(comb(m,c) for c in range(2,m+1)) for m in range(2,n+1))
        assert total==3**n-(n+2)*2**(n-1)
    for n in range(2,8):
        direct=rank2_positive_f3_histogram(n)
        expected=toric_histogram(n)
        assert all(direct[j]==expected[j] for j in range(n-1)),(n,direct,expected)
        print(n, [direct[j] for j in range(n-1)],sum(direct.values()))
    print('VERIFY_OK')
if __name__=='__main__':
    algebraic_checks()
