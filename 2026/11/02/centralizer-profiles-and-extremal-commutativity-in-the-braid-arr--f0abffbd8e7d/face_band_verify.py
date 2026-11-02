#!/usr/bin/env python3
"""Independent enumeration of commuting pairs of braid-arrangement faces."""
from itertools import product
from math import comb, factorial


def partitions(n):
    # Enumerate ordered set partitions as surjective words (block ranks).
    if n == 0:
        return [()]
    out = []
    for k in range(1, n + 1):
        for t in product(range(k), repeat=n):
            if set(t) == set(range(k)):
                out.append(t)
    return out


def multiply(a,b):
    if not a:
        return ()
    pairs=sorted(set(zip(a,b)))
    rank={p:i for i,p in enumerate(pairs)}
    return tuple(rank[(a[i], b[i])] for i in range(len(a)))


def bell(n):
    if n==0:return 1
    return len(partitions(n))


def stirling(n,k):
    S=[[0]*(n+1) for _ in range(n+1)]
    S[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):S[i][j]=j*S[i-1][j]+S[i-1][j-1]
    return S[n][k]


def theorem_count(n):
    if n==0:return 1
    return sum(3**(k-1)*factorial(k)*stirling(n,k) for k in range(1,n+1))


def predicted_centralizer(a):
    if not a:return 1
    counts = [a.count(i) for i in range(max(a)+1)]
    return 2**(len(counts)-1) * __import__('math').prod(bell(m) for m in counts)


def main():
    assert multiply((0,0,1),(0,1,0)) != multiply((0,1,0),(0,0,1))
    for n in range(0,6):
        P=partitions(n)
        C=0
        for a in P:
            central=sum(multiply(a,b)==multiply(b,a) for b in P)
            expected=predicted_centralizer(a)
            assert central==expected,(n,a,central,expected)
            C+=central
        goal=theorem_count(n)
        assert C==goal,(n,C,goal)
        print(f'n={n}: elements={len(P)}, commuting ordered pairs={C}, centralizer profiles verified')
    print('VERIFY_OK')

if __name__=='__main__':main()
