#!/usr/bin/env python3
"""Exact checks for prime-support fibers of the Dedekind-psi pseudo-aliquot map."""
from collections import Counter
from itertools import product
from math import prod


def prime_factors(n):
    assert n >= 1
    result = {}
    p = 2
    while p * p <= n:
        if n % p == 0:
            k = 0
            while n % p == 0:
                n //= p
                k += 1
            result[p] = k
        p += 1 if p == 2 else 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def prime_support(n):
    return frozenset(prime_factors(n))


def direct_T(n):
    assert n >= 1
    fac = prime_factors(n)
    # Independent squarefree-divisor sum, not the ratio used by the classifier.
    squarefree_divisors = [1]
    for p in fac:
        squarefree_divisors += [d*p for d in squarefree_divisors[:]]
    return sum(n // d for d in squarefree_divisors if d > 1)


def check_prime(p):
    return p > 1 and prime_factors(p) == {p:1}


def parameterize(word):
    """Return (base exponent vector, common set, base orbit) or None."""
    word = tuple(frozenset(S) for S in word)
    r = len(word)
    assert r >= 1 and all(S and all(check_prime(p) for p in S) for S in word)
    U = frozenset.union(*word)
    K = frozenset.intersection(*word)
    D = [prod(S) for S in word]
    A = [prod(p+1 for p in S)-d for S,d in zip(word,D)]
    if prod(D) != prod(A):
        return None
    Af = [prime_factors(a) for a in A]
    h = [{p:0 for p in U}]
    for i in range(r):
        h.append({p:h[-1][p]+Af[i].get(p,0)-int(p in word[i]) for p in U})
    assert all(h[-1][p] == 0 for p in U)
    e0 = {}
    for p in U:
        if p in K:
            e0[p] = max(1-h[i][p] for i in range(r))
        else:
            absent = [i for i in range(r) if p not in word[i]]
            candidates = {-h[i][p] for i in absent}
            if len(candidates)!=1:
                return None
            e0[p] = next(iter(candidates))
        if any((e0[p]+h[i][p]>0) != (p in word[i]) for i in range(r)):
            return None
    n = prod(p**e for p,e in e0.items())
    seq = [n]
    for i in range(r):
        n2 = direct_T(n)
        seq.append(n2)
        n = n2
    assert seq[-1] == seq[0]
    assert all(prime_support(seq[i]) == word[i] for i in range(r))
    return e0, K, tuple(seq[:-1])


def fiber_count(word, X):
    info = parameterize(word)
    if info is None:
        return 0
    e0, K, seq = info
    base = seq[0]
    if base > X:
        return 0
    k = sorted(K)
    def f(i, acc):
        if i==len(k): return 1
        p=k[i]
        s=0
        while acc <= X:
            s+=f(i+1,acc)
            acc*=p
        return s
    return f(0,base)


def brute_cycles(N):
    observed = Counter()
    sample = {}
    for n in range(2,N+1):
        n1 = direct_T(n)
        if n1 <= 1:
            continue
        n2 = direct_T(n1)
        if n2 == n:
            word = (prime_support(n),prime_support(n1))
            observed[word] += 1
            sample.setdefault(word,n)
    return observed, sample


def test():
    assert prime_support(1) == frozenset()
    fixed=(frozenset([2,3]),)
    assert parameterize(fixed)[2] == (6,)
    assert fiber_count(fixed,10000) == sum(1 for n in range(1,10001) if direct_T(n)==n)
    invalid=(frozenset([2,5]),)
    assert parameterize(invalid) is None
    balanced_but_impossible=(frozenset([2,7]),frozenset([2,3,5]))
    assert parameterize(balanced_but_impossible) is None
    assert (24-14)*(72-30) == 14*30
    first=(frozenset([2,5,7,19]),frozenset([2,5,31]))
    swapped=first[::-1]
    e0,K,seq = parameterize(first)
    assert (seq,K,e0)==((1330,1550),frozenset((2,5)),{2:1,5:1,7:1,19:1,31:0})
    assert parameterize(swapped)[2] == (1550,1330)
    assert fiber_count(first,100000)==sum(1 for a in range(30) for b in range(20) if 1330*2**a*5**b<=100000)
    fixed_doubled=(frozenset([2,3]),frozenset([2,3]))
    assert parameterize(fixed_doubled)[2]==(6,6)
    repeated_pair=first+first
    assert parameterize(repeated_pair)[2]==(1330,1550,1330,1550)
    assert fiber_count(repeated_pair,100000)==fiber_count(first,100000)
    for e in range(5):
        for f in range(5):
            n=1330*2**e*5**f
            assert direct_T(n)==1550*2**e*5**f
            assert direct_T(direct_T(n))==n
    # Independent direct enumeration by n; check every actually occurring support word.
    LIMIT=25000
    observed,samples=brute_cycles(LIMIT)
    for word,cnt in observed.items():
        if word[0] == word[1]:
            assert parameterize((word[0],)) is not None
        base = parameterize(word)
        assert base is not None, (word,samples[word])
        assert cnt == fiber_count(word,LIMIT), (word,cnt,fiber_count(word,LIMIT))
        assert prime_support(base[2][0]) == word[0]
        assert prime_support(base[2][1]) == word[1]
    print('VERIFY_OK',
          'n<=',LIMIT,
          'distinct_rooted_words=',len(observed),
          'rooted_points=',sum(observed.values()),
          'all_fiber_counts=exact',
          'two_cycle_seed=(1330,1550)',
          'fixed_support=(2,3)',
          'higher_exponent_scalings=25')
    print('ROOTED_WORD_COUNTS', sorted((cnt, samples[w]) for w,cnt in observed.items())[-12:])
    print('COUNT_1330_FIBER_100000',fiber_count(first,100000))


if __name__ == '__main__':
    test()
