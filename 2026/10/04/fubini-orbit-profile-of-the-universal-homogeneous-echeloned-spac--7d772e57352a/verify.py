#!/usr/bin/env python3
from itertools import product
from math import comb, factorial

def stirling2(n,k):
    if n==0: return 1 if k==0 else 0
    if k==0: return 0
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

def fubini(m):
    return sum(factorial(j)*stirling2(m,j) for j in range(m+1))

def brute_weak_orders(m):
    if m==0: return 1
    count=0
    for ranks in product(range(m), repeat=m):
        used=set(ranks)
        if used==set(range(max(ranks)+1)):
            count+=1
    return count

expected_a={1:1,2:1,3:13,4:4683,5:102247563,6:230283190977853}
for n,want in expected_a.items():
    got=fubini(comb(n,2))
    assert got==want,(n,got,want)

for m in range(7):
    got=brute_weak_orders(m)
    want=fubini(m)
    assert got==want,(m,got,want)

expected_b={1:1,2:2,3:17,4:4769,5:102294734}
for n,want in expected_b.items():
    got=sum(stirling2(n,k)*fubini(comb(k,2)) for k in range(1,n+1))
    assert got==want,(n,got,want)

print('VERIFY_OK')
