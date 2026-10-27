"""Exact checks for binary two-symbol-survivor deletion list codes.

Requires only Python 3.9+ standard library. The infinite claims in the
accompanying proof do not depend on these finite checks.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import ceil

PATTERNS = ('00', '01', '10', '11')


def signature(word):
    """Bit mask of the four distinct length-two subsequences."""
    return sum(1 << i for i, p in enumerate(PATTERNS)
               if any(word[a] == p[0] and word[b] == p[1]
                      for a in range(len(word))
                      for b in range(a + 1, len(word))))


def layers(n):
    assert n >= 3
    low = ['0'*n, '1'*n, '0'*(n-1)+'1', '1'+'0'*(n-1),
           '0'+'1'*(n-1), '1'*(n-1)+'0']
    omit_00 = ['1'*a+'0'+'1'*(n-a-1) for a in range(1,n-1)]
    omit_11 = ['0'*a+'1'+'0'*(n-a-1) for a in range(1,n-1)]
    omit_01 = ['1'*a+'0'*(n-a) for a in range(2,n-1)]
    omit_10 = ['0'*a+'1'*(n-a) for a in range(2,n-1)]
    universal = []
    if n >= 4:
        universal = ['0101'+'0'*(n-4), '1010'+'1'*(n-4)]
    return low, omit_00, omit_11, omit_01, omit_10, universal


def construction(n,L):
    if L == 1:
        return ['0'*n, '1'*n]
    low, a, b, c, d, quad = layers(n)
    if L == 2:
        return [low[j] for j in (0,1,2,5)]
    if L == 3:
        return low
    h, s = divmod(L,3)
    if s == 0:
        assert h >= 2 and n >= max(4,h+1)
        return low + a[:h-1]+b[:h-1]+c[:h-2]+d[:h-2]+quad[:2]
    assert n >= max(3 if L==4 else 4, h+2)
    return low + a[:h]+b[:h]+c[:h-1]+d[:h-1]+quad[:(s==2)]


def capacity_bound(L):
    return min(2*L, (4*L+8)//3)


def threshold(L):
    return 3 if L <= 4 else max(4, ceil(L/3)+1)


def exact_small(n, L):
    """Finite, exact signature-class dynamic programming."""
    counts=Counter(signature(''.join(w)) for w in product('01',repeat=n))
    kinds=sorted(counts)
    @lru_cache(None)
    def dp(k,slots):
        if k == len(kinds):
            return 0
        mask = kinds[k]
        max_count=min(counts[mask],*(slots[j] for j in range(4) if mask & (1<<j)))
        return max(t+dp(k+1,tuple(slots[j]-t*((mask>>j)&1)
                                  for j in range(4))) for t in range(max_count+1))
    return dp(0,(L,)*4)


def run():
    # Independent enumeration of every possible length-two subsequence signature.
    checked_words = 0
    for n in range(3,12):
        counts=Counter(signature(''.join(w)) for w in product('01',repeat=n))
        assert counts[1]==counts[8]==1
        assert sum(counts[m] for m in (3,5,10,12))==4
        assert counts[7]==counts[14]==n-2
        assert counts[11]==counts[13]==max(0,n-3)
        assert counts[15] == (2**n-4*n+4 if n>=4 else 0)
        assert sum(counts.values())==2**n
        checked_words+=2**n
    constructed = 0
    for L in range(1,61):
        for n in range(threshold(L), min(threshold(L)+4,26)):
            words=construction(n,L)
            assert len(words)==len(set(words))==capacity_bound(L)
            loads=[sum(bool(signature(w) & (1<<j)) for w in words) for j in range(4)]
            assert max(loads)<=L, (n,L,loads)
            constructed+=1
    exact_cases=0
    for n in range(3,7):
        for L in range(1,11):
            opt=exact_small(n,L)
            B=capacity_bound(L)
            assert (opt==B)==(n>=threshold(L)), (n,L,opt,B)
            exact_cases+=1
    print('PASS', 'enumerated_words',checked_words,
          'construction_cases',constructed,'exact_DP_cases',exact_cases)


if __name__=='__main__':
    run()
