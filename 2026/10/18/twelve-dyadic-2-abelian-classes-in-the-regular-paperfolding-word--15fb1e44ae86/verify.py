#!/usr/bin/env python3
"""Reproduce the dyadic 2-abelian profile theorem for regular paperfolding factors.

The mathematical proof is given in RESULT.md. This program checks its finite
base case, uniform witnesses, structural identities and representative lengths.
"""
from collections import Counter


def bit(i):
    assert i >= 1
    while i % 2 == 0:
        i //= 2
    return int(i % 4 == 1)


def word(t, n):
    return [bit(i) for i in range(t, t+n)]


def signature(w):
    return (sum(w)-len(w)//2, w[0], w[-1])


def full_2abelian(w):
    return (w[0], w[-1], sum(w),
            tuple(sum((w[i], w[i+1]) == (a, b) for i in range(len(w)-1))
                  for a in (0, 1) for b in (0, 1)))


def expected_start(j, n, offset):
    return (j-1)*(n//2)+offset


def run():
    assert tuple(bit(i) for i in range(1, 17)) == (1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1)
    for k in range(3, 13):
        n = 2**k
        max_t = 16*n
        p = [0] + [bit(i) for i in range(1, max_t+n+1)]
        one_prefix = [0]*(len(p)+1)
        trans_prefix = [0]*(len(p)+1)
        for i in range(1,len(p)):
            one_prefix[i+1] = one_prefix[i] + p[i]
            if i+1 < len(p):
                trans_prefix[i+1] = trans_prefix[i] + (p[i] != p[i+1])
        seen, full = set(), set()
        for t in range(1,max_t+1):
            K=one_prefix[t+n]-one_prefix[t]
            T=trans_prefix[t+n-1]-trans_prefix[t]
            a,b=p[t],p[t+n-1]
            sig=(K-n//2,a,b)
            seen.add(sig)
            j=(t+n//2-1)//(n//2)
            assert K == n//2-1+p[j]+p[j+1], (k,t)
            assert T == (n//2 if a==b else n//2-1), (k,t)
            assert sig[0] in (-1,0,1)
            if k<=7 or t%(n//2)==0:
                w=p[t:t+n]
                assert signature(w)==sig
                full.add(full_2abelian(w))
        assert len(seen)==12, (k,len(seen))
        assert seen == {(q,a,b) for q in (-1,0,1) for a in (0,1) for b in (0,1)}
        if k<=7: assert len(full)==12
        if k >= 4:
            js = {1:1,0:3,-1:11}
            for q,j in js.items():
                for offset,(a,b) in ((2,(1,1)),(3,(0,1)),(4,(1,0)),(7,(0,0))):
                    w=word(expected_start(j,n,offset),n)
                    assert signature(w) == (q,a,b), (k,j,offset)
        print('n=%d profiles=12, recursion/transition identities verified' % n)
    # Full finite base case k=3: explicit locations for all twelve triples.
    table = {
      (-1,0,0):23,(-1,0,1):22,(-1,1,0):21,(-1,1,1):42,
      (0,0,0):7,(0,0,1):6,(0,1,0):5,(0,1,1):9,
      (1,0,0):15,(1,0,1):3,(1,1,0):4,(1,1,1):1,
    }
    for sig,t in table.items():
        assert signature(word(t,8)) == sig, (sig,t)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
