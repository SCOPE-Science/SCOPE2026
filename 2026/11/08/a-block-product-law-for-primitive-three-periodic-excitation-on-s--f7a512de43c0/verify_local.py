#!/usr/bin/env python3
"""Independently count local rooted-cycle extensions via edge-increment DP."""
from itertools import product

def count_dp(length):
    # Fix root phase zero. Every step adds an edge increment in {-1,0,+1}.
    # An interior vertex needs a successor neighbor: left increment -1 or right increment +1.
    d={(k,k%3):1 for k in (-1,0,1)}
    for _ in range(1,length):
        nd={}
        for (prev,s),ways in d.items():
            for k in (-1,0,1):
                if prev!=-1 and k!=1:continue
                key=(k,(s+k)%3)
                nd[key]=nd.get(key,0)+ways
        d=nd
    return sum(ways for (last,s),ways in d.items() if s==0)

def enumerate_bruteforce(length):
    cnt=0
    for rest in product(range(3),repeat=length-1):
        state=(0,)+rest
        if all((state[i]+1)%3 in (state[i-1],state[(i+1)%length]) for i in range(1,length)):
            cnt+=1
    return cnt

for length in range(3,201):
    formula=2*(length//3)+1
    count=count_dp(length)
    assert count==formula,(length,count,formula)
    if length<=10:
        brute=enumerate_bruteforce(length)
        assert brute==formula,(length,brute,formula)
    if length in (3,4,5,6,7,8,9,10,11,12,101,200):print(f'rooted cycle length={length}: count={count}')
print('PASS: 198 cycle lengths with transfer DP, 8 independently enumerated full phase assignments')
