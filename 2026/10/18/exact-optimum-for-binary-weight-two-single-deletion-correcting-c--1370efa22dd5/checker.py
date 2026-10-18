#!/usr/bin/env python3
"""Finite independent checks for a weight-two single-deletion code formula.

No finite computation is used to justify the all-length upper bound.
"""
from functools import lru_cache
from itertools import combinations


def word(n, a, b):
    return ''.join('1' if i in (a, b) else '0' for i in range(n))


def descendants(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}


def formula(n):
    return n-1-(n+1)//4


def witness(n):
    a = [(i,i+1) for i in range(0,n-1,2)]
    b = [(i,i+3) for i in range(1,n-3,4)]
    return a+b


def brute_optimum(n):
    words = [word(n,a,b) for a,b in combinations(range(n),2)]
    ds = list(map(descendants,words))
    m = len(words)
    adj = [0]*m
    for i in range(m):
        for j in range(i+1,m):
            if ds[i]&ds[j]:
                adj[i] |= 1<<j
                adj[j] |= 1<<i
    @lru_cache(None)
    def independence(mask):
        if not mask:
            return 0
        choices = [i for i in range(m) if mask>>i&1]
        v = max(choices, key=lambda i:(mask&adj[i]).bit_count())
        return max(independence(mask&~(1<<v)),
                   1+independence(mask&~(1<<v)&~adj[v]))
    return independence((1<<m)-1)


def main():
    for n in range(2,97):
        pairs = witness(n)
        assert len(pairs) == formula(n), (n,pairs)
        assert len(set(pairs)) == len(pairs)
        assert all(0<=a<b<n for a,b in pairs)
        ds = [descendants(word(n,*p)) for p in pairs]
        assert all(not (ds[i] & ds[j]) for i in range(len(ds)) for j in range(i+1,len(ds))), n
    print('CONSTRUCTION_CHECK n=2..96: PASS')
    results = [(n,brute_optimum(n),formula(n)) for n in range(2,9)]
    assert all(x==y for _,x,y in results), results
    print('INDEPENDENT_EXACT_OPTIMUM n=2..8:',results)
    for n in range(2,25):
        loops = [(i,i+1) for i in range(n-1)]
        for i in range(n-2):
            assert descendants(word(n,*loops[i])) & descendants(word(n,*loops[i+1]))
        for a,b in combinations(range(n),2):
            d = {x for x in descendants(word(n,a,b)) if x.count('1') == 1}
            assert len(d) == (1 if b==a+1 else 2)
    print('UNARY_SHADOW_AND_ADJACENT_LOOP_TEST n=2..24: PASS')
    print('CHECK_OK')

if __name__=='__main__':
    main()
