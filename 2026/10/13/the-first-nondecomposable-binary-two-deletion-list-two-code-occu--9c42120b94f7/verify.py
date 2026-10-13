#!/usr/bin/env python3
"""Exact finite verification of a binary two-deletion list-capacity statement.

No floating-point optimization, external data, or third-party packages required.
"""
from itertools import combinations

WITNESSES = {
    (3,1): ['000','111'],
    (3,2): ['000','110','111'],
    (4,1): ['0010','1111'],
    (4,2): ['0000','0001','1101','1110'],
    (5,1): ['00110','11111'],
    (5,2): ['01000','01010','10111','11110'],
    (6,1): ['000000','001110','110001','111111'],
    (6,2): ['000000','001110','010000','010101','110001','111110','111111'],
    (7,1): ['0000000','0000111','0111001','1001010','1111110'],
    (7,2): ['0000000','0000100','0001111','0011110','0101010','1000011','1010101','1110000','1110111','1111000','1111111'],
}
# Integer-weight dual certificates: each y output of length n-2 has weight w_y/d.
# Each x input of length n has nonnegative overage s_x/d.
DUALS = {
    3: (1, [1,0], {7:1}),
    4: (1, [1,0,0,1], {}),
    5: (1, [1,0,0,0,0,0,0,1], {}),
    6: (5, [3,2,0,1,0,0,0,2,2,0,0,0,1,0,2,3],{0:2,63:2}),
    7: (59,[52,7,0,26,7,5,4,26,0,1,2,5,4,1,16,7,7,16,1,4,5,2,1,0,26,4,5,7,26,0,7,52],{0:7,127:7})
}
CAPACITIES = {(2,1):1,(2,2):2, (3,1):2,(3,2):3,(4,1):2,(4,2):4,
              (5,1):2,(5,2):4,(6,1):4,(6,2):7,(7,1):5,(7,2):11}

def shadows(word):
    return {''.join(word[i] for i in places) for places in combinations(range(len(word)),len(word)-2)}

def words(n):
    return [format(j,f'0{n}b') for j in range(2**n)]

def verify():
    for (n,L), m in CAPACITIES.items():
        if n==2:
            assert m==L
            continue
        code=WITNESSES[(n,L)]
        assert len(code)==m and len(set(code))==m
        counts={y:0 for y in words(n-2)}
        for x in code:
            assert len(x)==n and set(x)<={'0','1'}
            for y in shadows(x): counts[y]+=1
        assert max(counts.values())<=L, (n,L,counts)
        denominator,weights,slacks=DUALS[n]
        assert len(weights)==2**(n-2)
        assert all(v>=0 for v in weights) and all(v>=0 for v in slacks.values())
        for j,x in enumerate(words(n)):
            lhs=sum(weights[int(y,2)] for y in shadows(x))+slacks.get(j,0)
            assert lhs>=denominator, (n,x,lhs,denominator)
        numerator=L*sum(weights)+sum(slacks.values())
        assert numerator < (m+1)*denominator, (n,L,numerator,denominator,m)
        print('n=',n,'list=',L,'achieved=',m,'dual=',f'{numerator}/{denominator}', 'checks=',2**n)
    assert all(CAPACITIES[n,2]<=2*CAPACITIES[n,1] for n in range(2,7))
    assert CAPACITIES[7,2]>2*CAPACITIES[7,1]
    print('VERIFY_OK')

if __name__=='__main__': verify()
