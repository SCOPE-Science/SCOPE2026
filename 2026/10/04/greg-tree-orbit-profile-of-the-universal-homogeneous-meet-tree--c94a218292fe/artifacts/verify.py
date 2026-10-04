#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from math import factorial

EXPECTED = [1,3,22,262,4336,91984,2381408,72800928,2566606784,102515201984]

@lru_cache(None)
def partitions(items):
    items = tuple(items)
    if not items:
        return ((),)
    first = items[0]
    out = set()
    for p in partitions(items[1:]):
        # new block
        q = tuple(sorted(((first,),) + p))
        out.add(q)
        # insert into existing block
        for j in range(len(p)):
            blocks = [tuple(b) for b in p]
            blocks[j] = tuple(sorted(blocks[j] + (first,)))
            out.add(tuple(sorted(blocks)))
    return tuple(sorted(out))

@lru_cache(None)
def greg(labels):
    labels = tuple(sorted(labels))
    if not labels:
        return frozenset()
    out = set()
    # black root: choose root label, partition remaining labels among child subtrees
    for r in labels:
        rem = tuple(x for x in labels if x != r)
        if not rem:
            out.add(('B', r, ()))
        else:
            for p in partitions(rem):
                child_lists = [greg(block) for block in p]
                combos = [()]
                for choices in child_lists:
                    combos = [c + (v,) for c in combos for v in choices]
                for c in combos:
                    out.add(('B', r, tuple(sorted(c, key=repr))))
    # white root: at least two nonempty child blocks
    for p in partitions(labels):
        if len(p) < 2:
            continue
        child_lists = [greg(block) for block in p]
        combos = [()]
        for choices in child_lists:
            combos = [c + (v,) for c in combos for v in choices]
        for c in combos:
            out.add(('W', tuple(sorted(c, key=repr))))
    return frozenset(out)

def egf_coeffs(N):
    # G=sum c[n] x^n and E=exp(G)=sum e[n] x^n.
    # From 2G+1=(1+x)E, coefficient n>=1 gives
    # c[n] = e[n-1] + (1/n) sum_{k=1}^{n-1} k*c[k]*e[n-k].
    c = [Fraction(0) for _ in range(N+1)]
    e = [Fraction(0) for _ in range(N+1)]
    e[0] = Fraction(1)
    for n in range(1, N+1):
        tail = sum((Fraction(k) * c[k] * e[n-k] for k in range(1,n)), Fraction(0)) / n
        c[n] = e[n-1] + tail
        e[n] = c[n] + tail
    return c, e

def stirling2(n,k):
    dp = [[0]*(k+2) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

def main():
    direct = [len(greg(tuple(range(1,n+1)))) for n in range(1,6)]
    assert direct == EXPECTED[:5], (direct, EXPECTED[:5])
    c,e = egf_coeffs(10)
    seq = [int(c[n]*factorial(n)) for n in range(1,11)]
    assert seq == EXPECTED, (seq, EXPECTED)
    # Verify the functional equation coefficientwise: 2G+1=(1+x)exp(G).
    for n in range(0,11):
        lhs = Fraction(1) if n==0 else 2*c[n]
        rhs = e[n] + (e[n-1] if n>=1 else 0)
        assert lhs == rhs, (n,lhs,rhs)
    b=[]
    for n in range(1,5):
        b.append(sum(stirling2(n,k)*EXPECTED[k-1] for k in range(1,n+1)))
    assert b == [1,4,32,416], b
    print('DIRECT', direct)
    print('EGF', seq)
    print('ALL_TUPLES', b)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
