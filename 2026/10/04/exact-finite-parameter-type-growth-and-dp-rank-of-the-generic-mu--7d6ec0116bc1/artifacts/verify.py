#!/usr/bin/env python3
import itertools, math

def partitions(seq):
    seq=list(seq)
    if not seq:
        yield []
        return
    first=seq[0]
    for rest in partitions(seq[1:]):
        yield [{first}]+[set(b) for b in rest]
        for i in range(len(rest)):
            nr=[set(b) for b in rest]
            nr[i].add(first)
            yield nr

def falling(m,t):
    z=1
    for j in range(t): z*=m-j
    return z

def rising_m1(m,s):
    z=1
    for j in range(1,s+1): z*=m+j
    return z

def stirling2(r,b):
    dp=[[0]*(b+2) for _ in range(r+1)]
    dp[0][0]=1
    for i in range(1,r+1):
        for j in range(1,min(i,b)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[r][b]

def closed(n,r,m):
    total=0
    for b in range(1,r+1):
        for t in range(b+1):
            total += stirling2(r,b)*math.comb(b,t)*falling(m,t)*(rising_m1(m,b-t)**n)
    return total

def direct(n,r,m):
    # Direct finite-diagram enumeration. For each equality partition, explicitly
    # choose which blocks are pinned to which parameters and explicitly enumerate
    # every order extension of the remaining labeled blocks.
    total=0
    for pi in partitions(range(r)):
        # canonicalize blocks only to avoid duplicate recursive representations
        blocks=sorted((tuple(sorted(b)) for b in pi), key=lambda z:z[0])
        b=len(blocks)
        for t in range(0,b+1):
            for chosen in itertools.combinations(range(b),t):
                for params in itertools.permutations(range(m),t):
                    pinned=dict(zip(chosen,params))
                    new=[j for j in range(b) if j not in pinned]
                    # Per order, enumerate all shuffles of the fixed A-chain with
                    # the distinct new blocks; this is exactly the finite diagram.
                    one=0
                    symbols=[('A',a) for a in range(m)]+[('X',j) for j in new]
                    for perm in itertools.permutations(symbols):
                        apos=[next(k for k,z in enumerate(perm) if z==('A',a)) for a in range(m)]
                        if apos==sorted(apos): one+=1
                    total += one**n
    return total

for n in (1,2,3):
    for r in (1,2,3):
        for m in (0,1,2):
            a=closed(n,r,m)
            b=direct(n,r,m)
            assert a==b,(n,r,m,a,b)
assert [closed(1,1,m) for m in range(5)] == [1,3,5,7,9]
assert [closed(2,1,m) for m in range(4)] == [1,5,11,19]
assert [closed(2,2,m) for m in range(3)] == [5,49,193]
print('VERIFY_OK')
