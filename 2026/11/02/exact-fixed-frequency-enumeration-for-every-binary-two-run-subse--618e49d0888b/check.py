#!/usr/bin/env python3
"""Independent exact checks for two-run binary subsequence-frequency formulas."""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def occ(word, a, b):
    # Independent brute-style subsequence DP rather than the zero-before-ones decomposition.
    pat = '0' * a + '1' * b
    dp = [0] * (len(pat) + 1)
    dp[0] = 1
    for c in word:
        for i in range(len(pat)-1, -1, -1):
            if c == pat[i]:
                dp[i+1] += dp[i]
    return dp[-1]


def cores(a, b, k):
    """Unique constrained profiles: q active ones, nondecreasing preceding-zero counts."""
    if k < 1:
        return []
    out = []
    q = b
    while comb(q, b) <= k:
        r = q - b + 1
        def gen(seq, low, rem):
            i = len(seq) + 1
            if i > r:
                if rem == 0:
                    out.append((q, seq[-1], tuple(seq)))
                return
            weight = comb(q-i, b-1)
            t = low
            while weight * comb(t, a) <= rem:
                gen(seq + [t], t, rem - weight * comb(t, a))
                t += 1
        gen([], a, k)
        q += 1
    return out


def predicted(n, a, b, k):
    d = a + b
    return sum(comb(n - q - t + d-1, d-1) for q,t,_ in cores(a,b,k) if n >= q+t)


def verify():
    checks = 0
    for a in range(1, 5):
        for b in range(1, 5):
            for n in range(a+b, 16):
                actual = Counter(occ(''.join(bits), a, b) for bits in product('01', repeat=n))
                for k in range(1, 19):
                    exp = predicted(n,a,b,k)
                    got = actual[k]
                    assert exp == got, (a,b,n,k,exp,got)
                    checks += 1
    print('brute/closed-form profile comparisons:', checks)
    assert cores(2,2,5) == [(3,3,(2,3))]
    for n in range(0,40):
        assert predicted(n,2,2,5) == (comb(n-3,3) if n>=6 else 0)
    print('specific counterexample B_{0011}(n,5) verified through n=39')
    for a,b,k in [(1,1,12),(2,2,5),(2,3,8),(3,2,12),(3,3,15)]:
        pr = cores(a,b,k)
        print(f'a={a} b={b} k={k}: {len(pr)} constrained profiles; leading coefficient {len(pr)}/{(a+b-1)}!')
    print('OK')

if __name__ == '__main__':
    verify()
