#!/usr/bin/env python3
from itertools import product, combinations
from functools import lru_cache
from math import comb

@lru_cache(None)
def S(n,k):
    if n==k==0:
        return 1
    if n==0 or k==0:
        return 0
    return S(n-1,k-1)+k*S(n-1,k)

def partitions_rgs(n):
    if n==0:
        yield ()
        return
    def rec(seq,m):
        if len(seq)==n:
            yield tuple(seq)
            return
        for x in range(m+2):
            seq.append(x)
            yield from rec(seq,max(m,x))
            seq.pop()
    yield from rec([0],0)

def parity_ok(rgs,bits):
    n=len(rgs)
    cross=[(i,j) for i in range(n) for j in range(i+1,n) if rgs[i]!=rgs[j]]
    orient=dict(zip(cross,bits))  # 1 means smaller index -> larger index
    blocks={}
    for v,c in enumerate(rgs):
        blocks.setdefault(c,[]).append(v)
    B=list(blocks.values())
    for p in range(len(B)):
        for q in range(p+1,len(B)):
            X,Y=B[p],B[q]
            for x,x2 in combinations(X,2):
                for y,y2 in combinations(Y,2):
                    total=0
                    for u in (x,x2):
                        for v in (y,y2):
                            i,j=sorted((u,v))
                            z=orient[(i,j)]
                            total += z if u<v else 1-z
                    if total % 2:
                        return False
    return True

def direct_partition_count(rgs):
    n=len(rgs)
    cross=[(i,j) for i in range(n) for j in range(i+1,n) if rgs[i]!=rgs[j]]
    return sum(parity_ok(rgs,bits) for bits in product((0,1), repeat=len(cross)))

def a(n):
    if n==0:
        return 1
    return sum(S(n,k)*2**((k-1)*n-comb(k,2)) for k in range(1,n+1))

def b(n):
    return sum(S(n,r)*a(r) for r in range(n+1))

direct=[]
for n in range(1,7):
    total=0
    for rgs in partitions_rgs(n):
        k=max(rgs)+1
        got=direct_partition_count(rgs)
        want=2**((k-1)*n-comb(k,2))
        assert got==want,(n,rgs,got,want)
        total+=got
    assert total==a(n)
    direct.append(total)

# Equivalent collision-layer rewrite.
for n in range(1,15):
    lhs=a(n)
    rhs=sum(S(n,n-j)*2**(comb(n,2)-comb(j+1,2)) for j in range(n))
    assert lhs==rhs

A=[a(n) for n in range(11)]
B=[b(n) for n in range(9)]
assert A==[1,1,3,21,313,9585,591841,72906689,17809866625,8598208478977,8188495841984001]
assert B==[1,1,4,31,461,13286,757945,86793311,20019300954]

print('direct_a_n_1_to_6',direct)
print('formula_a_n_0_to_10',A)
print('all_tuple_b_n_0_to_8',B)
print('VERIFY_OK')
