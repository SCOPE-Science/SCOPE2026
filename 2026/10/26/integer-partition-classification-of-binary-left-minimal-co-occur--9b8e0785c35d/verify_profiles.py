#!/usr/bin/env python3
"""Independent finite checks for binary left-minimal co-occurrence profiles.

No external modules are required. Brute enumeration is deliberately separate
from the run decomposition used in the proof.
"""
from collections import Counter, defaultdict
from itertools import product
from math import factorial, isqrt


def direct_profile(word):
    n = len(word)
    counts = [0] * (n + 1)
    for i in range(n):
        # A left-minimal mixed window starting at i has both symbols,
        # but removing its first symbol loses mixedness.
        for j in range(i + 1, n):
            window = word[i:j+1]
            if len(set(window)) == 2 and len(set(window[1:])) < 2:
                counts[j-i+1] += 1
    return tuple(counts[1:])


def run_profile(word):
    n = len(word)
    lengths = []
    for c in word:
        if lengths and lengths[-1][0] == c:
            lengths[-1] = (c, lengths[-1][1]+1)
        else:
            lengths.append((c, 1))
    ans = [0] * n
    for _, ell in lengths[1:]:
        for width in range(2, min(n, ell+1)+1):
            ans[width-1] += 1
    return tuple(ans)


def partitions_upto(n):
    p = [0] * (n + 1)
    p[0] = 1
    for part in range(1, n+1):
        for s in range(part, n+1):
            p[s] += p[s-part]
    return sum(p)


def partition_fibers(n):
    """Predicted multiset of class sizes from partitions of t <= n-1."""
    if n == 1:
        return Counter({2: 1})
    sizes = Counter({2: 2})  # empty and exceptional singleton (n-1)
    def visit(rem, largest, parts):
        if rem == 0:
            if parts and not (len(parts) == 1 and parts[0] == n-1):
                freq = Counter(parts)
                num = 2 * factorial(len(parts))
                for v in freq.values():
                    num //= factorial(v)
                sizes[num] += 1
            return
        for k in range(min(rem, largest), 0, -1):
            visit(rem-k, k, parts + [k])
    for t in range(1, n):
        visit(t, t, [])
    return sizes


def maximum_d(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    k = (isqrt(8*n-7)-1)//2
    return 1+k


def main():
    words_checked = 0
    for n in range(1, 16):
        fibers = defaultdict(int)
        supports = set()
        for tup in product('01', repeat=n):
            word = ''.join(tup)
            p = direct_profile(word)
            assert p == run_profile(word), (word,p,run_profile(word))
            fibers[p] += 1
            delta = [p[0]] + [p[i]-p[i-1] for i in range(1,n)]
            supports.add(sum(v != 0 for v in delta[1:]))
            words_checked += 1
        assert len(fibers) == partitions_upto(n-1), (n,len(fibers),partitions_upto(n-1))
        assert Counter(fibers.values()) == partition_fibers(n), (n, Counter(fibers.values()), partition_fibers(n))
        assert max(supports) == maximum_d(n), (n,max(supports),maximum_d(n))
        assert sum(fibers.values()) == 2**n
        print(f'n={n}, profiles={len(fibers)}, largest_d={max(supports)}, words={2**n}')
    assert words_checked == (2**16-2)
    print('VERIFY_OK', words_checked)


if __name__ == '__main__':
    main()
