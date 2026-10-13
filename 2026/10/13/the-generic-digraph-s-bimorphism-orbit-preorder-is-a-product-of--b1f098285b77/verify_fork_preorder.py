#!/usr/bin/env python3
from itertools import product
from math import comb

assertions = 0

def check(cond, msg=''):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(msg)

def leq1(a,b):
    return a == b or a == 0

def leq(x,y):
    return all(leq1(a,b) for a,b in zip(x,y))

def rank(x):
    return sum(a != 0 for a in x)

def covers(x,y):
    return leq(x,y) and rank(y) == rank(x)+1

def mobius_interval(x,y):
    if not leq(x,y):
        return None
    # Every interval is Boolean on coordinates that go 0 -> +/-.
    return (-1) ** (rank(y)-rank(x))

for k in range(1,5):
    N = comb(k,2)
    states = list(product(range(3), repeat=N))
    check(len(states) == 3**N)
    # Mutual reachability collapses exactly to equality.
    for x in states:
        for y in states:
            if leq(x,y) and leq(y,x):
                check(x == y)
    # Rank distribution.
    dist = [0]*(N+1)
    for x in states:
        dist[rank(x)] += 1
    check(dist == [comb(N,r)*2**r for r in range(N+1)])
    # Comparable pairs and covers.
    comp = 0
    cov = 0
    for x in states:
        for y in states:
            if leq(x,y):
                comp += 1
                check(mobius_interval(x,y) == (-1)**(rank(y)-rank(x)))
                if covers(x,y):
                    cov += 1
    check(comp == 5**N)
    expected_cov = 0 if N == 0 else 2*N*3**(N-1)
    check(cov == expected_cov)

def stirling2(n,k):
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i][j] = dp[i-1][j-1] + j*dp[i-1][j]
    return dp[n][k]

s_expected = [1,4,37,913,67060,15284551,10770210577]
c_expected = [1,6,141,16411,9925076,30665089531,477479400037941]
e_expected = [0,2,60,3254,424200,149588432,149514364692]

for n in range(1,8):
    s = sum(stirling2(n,k)*3**comb(k,2) for k in range(1,n+1))
    c = sum(stirling2(n,k)*5**comb(k,2) for k in range(1,n+1))
    e = sum(stirling2(n,k)*(0 if k < 2 else 2*comb(k,2)*3**(comb(k,2)-1)) for k in range(1,n+1))
    check(s == s_expected[n-1])
    check(c == c_expected[n-1])
    check(e == e_expected[n-1])

print('strong_orbits', s_expected)
print('comparable_pairs', c_expected)
print('covers', e_expected)
print('assertions', assertions)
print('VERIFY_OK')
