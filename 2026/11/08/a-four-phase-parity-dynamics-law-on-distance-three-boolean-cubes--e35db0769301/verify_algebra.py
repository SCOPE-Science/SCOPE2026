#!/usr/bin/env python3
"""Independent squarefree-monomial basis calculations and dynamic checks."""
from itertools import combinations
from random import Random

def elementary(n,deg):
    return sum(1<<sum(1<<i for i in comb) for comb in combinations(range(n),deg))

def polynomial_multiply(a,b,n):
    ans=0
    while a:
        ia=(a&-a).bit_length()-1
        x=b
        while x:
            ib=(x&-x).bit_length()-1
            if not ia&ib:
                ans^=1<<(ia|ib)
            x&=x-1
        a&=a-1
    return ans

def group_to_squarefree(a,n):
    # x_i=1+y_i: group basis delta_S corresponds to prod_{i in S}(1+y_i)
    ret=0
    while a:
        mask=(a&-a).bit_length()-1
        sub=mask
        while True:
            ret^=1<<sub
            if sub==0:break
            sub=(sub-1)&mask
        a&=a-1
    return ret

rng=Random(20261101)
for n in range(3,12):
    m=(1<<n)
    multiplier=0
    for comb in combinations(range(n),3):
        mask=sum(1<<i for i in comb)
        sub=mask
        while True:
            multiplier^=1<<sub
            if sub==0:break
            sub=(sub-1)&mask
    e=[elementary(n,j) for j in range(4)]
    assert multiplier == [e[1]^e[3],e[2]^e[3],e[3],1^e[1]^e[2]^e[3]][n%4]
    assert polynomial_multiply(multiplier,multiplier,n)==(1 if n%4==3 else 0)
    for _ in range(20):
        x=rng.getrandbits(m)
        # Independent group convolution first, then basis transform
        grp=0
        for tri in combinations(range(n),3):
            mask=sum(1<<i for i in tri)
            for v in range(1<<n):
                if (x>>v)&1: grp^=1<<(v^mask)
        a=group_to_squarefree(x,n)
        b=group_to_squarefree(grp,n)
        assert polynomial_multiply(a,multiplier,n)==b,(n,x)
    print('n=',n,'polynomial',str([i for i in range(4) if (multiplier>>((1<<i)-1)) & 1]),'basis identity and 20 random state checks PASS')
print('PASS independent group-to-squarefree conjugacy')
