#!/usr/bin/env python3
"""Integer-only cross-checks of the even-Betti polynomial identities.

Recomputes the additive Chow decomposition and an unrelated
Stirling expansion, and compares both with the proved differential recurrence.
Finite checks are not a substitute for the general root-interlacing proof.
"""
from math import comb, factorial


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def plus(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, k):
    return trim([k*x for x in a])


def product(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def power(a, n):
    out = [1]
    for _ in range(n):
        out = product(out, a)
    return out


def derivatives(a):
    return trim([i*a[i] for i in range(1,len(a))] or [0])


def compositions_big(s):
    if s == 0:
        yield ()
    for j in range(2, s+1):
        for c in compositions_big(s-j):
            yield (j,) + c


def chow(n, r):
    # Clader--Damiolini--Li--Ramadas Theorem 4.13, each ordered jump >= 2.
    result = power([1,1], n)
    for s in range(2,n+1):
        for js in compositions_big(s):
            if not js:
                continue
            mult = factorial(n) * r**s // (factorial(n-s)*__import__('math').prod(factorial(j) for j in js))
            term = power([1,1], n-s)
            for j in js:
                term = product(term, [0]+[1]*(j-1))
            result = plus(result, scale(term, mult))
    return result


def stirling_table(N):
    a = [[0]*(N+1) for _ in range(N+1)]
    a[0][0] = 1
    for m in range(1,N+1):
        for k in range(1,m+1):
            a[m][k] = k*a[m-1][k] + a[m-1][k-1]
    return a


def stirling_expression(n, r, ST):
    ans = [0]
    for m in range(n+1):
        inner = [0]
        for k in range(m+1):
            inner = plus(inner, scale(power([-1,1], m-k), factorial(k)*ST[m][k]))
        term = product(power([1-r,1], n-m), inner)
        ans = plus(ans, scale(term, comb(n,m)*r**m))
    return ans


def recurrence(N, r):
    seq = [[1], [1,1]]
    for n in range(1,N):
        a = seq[n]
        b = seq[n-1]
        right = plus(product([1, r*n+1], a),
                     scale(product([0,1,-1], derivatives(a)), r))
        right = plus(right, scale(product([0,1], b), r*(r-2)*n))
        seq.append(right)
    return seq[:N+1]


def main():
    N=8
    ST=stirling_table(N)
    count=0
    for r in (2,3,4,5,7,11):
        seq=recurrence(N,r)
        for n, polynomial in enumerate(seq):
            assert polynomial == chow(n,r), ("chow",r,n,polynomial,chow(n,r))
            assert polynomial == stirling_expression(n,r,ST), ("stirling",r,n)
            assert polynomial == polynomial[::-1], ("palindromic",r,n)
            assert len(polynomial) == n+1 and all(x > 0 for x in polynomial), (r,n)
            count += 1
    assert recurrence(4,2)[3] == [1,23,23,1]
    assert recurrence(4,3)[4] == [1,247,897,247,1]
    assert recurrence(5,4)[5] == [1,3109,34154,34154,3109,1]
    print("VERIFY_OK", "r-values=6", "n=0..8", "crosschecked_pairs="+str(count))

if __name__ == '__main__':
    main()
