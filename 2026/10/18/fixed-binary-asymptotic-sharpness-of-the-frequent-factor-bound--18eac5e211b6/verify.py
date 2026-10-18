"""Independent finite checks for frequent-factor counts in periodic de Bruijn words.

Run with Python 3.10+: python verify.py
The arguments in the theorem are proved symbolically; these finite tests are illustrative.
"""
from collections import Counter
from math import floor, log2, sqrt


def debruijn_binary(d):
    """Construct a lexicographically canonical binary de Bruijn cycle of order d."""
    a = [0] * (2 * d + 1)
    out = []
    def db(t, p):
        if t > d:
            if d % p == 0:
                out.extend(a[1:p+1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, 2):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return ''.join(map(str, out))


def frequent_factors(word):
    n = len(word)
    counts = Counter()
    for ell in range(1, (n + 1) // 2 + 1):
        for i in range(n - ell + 1):
            counts[word[i:i+ell]] += 1
    return sum(len(u) < count for u, count in counts.items())


def parameters(n):
    d = floor(log2(n / log2(n)) / 2)
    p = 2**d
    L = (n - p + 1) // (p + 1)
    return d, p, L


def check_case(n):
    d, p, L = parameters(n)
    assert n >= 64 and L >= d
    block = debruijn_binary(d)
    assert len(block) == p
    assert len({(block * 2)[i:i+d] for i in range(p)}) == p
    word = (block * ((n + p - 1)//p))[:n]
    assert len(word) == n
    for ell in range(d, L + 1):
        cyclic = { (block * ((ell+p-1)//p+1))[i:i+ell] for i in range(p) }
        assert len(cyclic) == p, (n,d,p,ell)
        counts = Counter(word[i:i+ell] for i in range(n - ell + 1))
        assert len(counts) == p, (n,d,p,ell)
        assert min(counts.values()) > ell, (n,d,p,ell)
    bound = p * (L - d + 1)
    assert n - bound < 3 * sqrt(n * log2(n)) + 1e-8
    actual = frequent_factors(word)
    assert actual >= bound, (n, actual, bound)
    return d,p,L,bound,actual


def check_fixed_cycle(n,d):
    p=1<<d
    L=(n-p+1)//(p+1)
    assert L>=d
    block=debruijn_binary(d)
    word=(block*((n+p-1)//p))[:n]
    lower=p*(L-d+1)
    actual=frequent_factors(word)
    assert actual>=lower
    for ell in range(d,L+1):
        counts=Counter(word[i:i+ell] for i in range(n-ell+1))
        assert len(counts)==p
        assert min(counts.values())>ell
    return lower,actual


if __name__ == '__main__':
    for n in [64,65,79,101,127,128,191,255,256,257,333,511]:
        d,p,L,lower,actual=check_case(n)
        print(f'n={n:4d} order={d} period={p:3d} L={L:3d} guaranteed={lower:4d} actual={actual:4d}')
    for n,d in [(200,3),(350,4),(1000,5)]:
        lower,actual=check_fixed_cycle(n,d)
        print(f'fixed-order n={n} order={d} guaranteed={lower} actual={actual}')
    for d in range(1, 9):
        b=debruijn_binary(d)
        assert len(b)==(1<<d)
        assert len({(b+b)[i:i+d] for i in range(len(b))})==len(b)
    sampled_n=list(range(64, 20000))+list(range(20000, 1000000, 997))
    for n in sampled_n:
        d,p,L=parameters(n)
        assert L >= d
        assert n-p*(L-d+1) < 3*sqrt(n*log2(n))
    print(f'PASS: 15 direct word counts, 8 de Bruijn order checks, and {len(sampled_n)} numerical parameter checks.')
