#!/usr/bin/env python3
"""Independent finite tests of the maximal-code defect coefficient theorem.

The all-permutation branch decodes Lehmer codes, tests consecutive 321
avoidance on the actual permutation, and computes maximality in the full
coordinatewise order by a multidimensional upper-zeta transform.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def formula(n):
    c = Counter()
    for d in range(n - 1):
        u = n - 2 - d
        e = (2*d - n + 2) % 3
        v_num = 2*d - n + 2 - e
        if u >= 0 and v_num >= 0:
            v = v_num // 3
            c[d] = comb(2, e) * comb(u + v, v)
    return +c


def direct(n):
    radices = list(range(n, 0, -1))
    size = factorial(n)
    valid = bytearray(size)
    for index, p in enumerate(product(*(range(a) for a in radices))):
        remaining = list(range(1, n+1))
        perm = [remaining.pop(d) for d in p]
        if all(not (perm[i] > perm[i+1] > perm[i+2]) for i in range(n-2)):
            valid[index] = 1
    # Each entry g[p] will count admissible codes q satisfying q >= p.
    g = list(valid)
    stride = 1
    for radix in reversed(radices):
        width = stride * radix
        for begin in range(0, size, width):
            for j in range(radix-2, -1, -1):
                this = begin + j*stride
                following = this + stride
                for offset in range(stride):
                    g[this+offset] += g[following+offset]
        stride = width
    assert stride == size
    out = Counter()
    for index, p in enumerate(product(*(range(a) for a in radices))):
        if valid[index] and g[index] == 1:
            out[comb(n,2)-sum(p)] += 1
    return +out


def by_blocks(n):
    c = Counter()
    def visit(blocks, remaining):
        if remaining in (1,2):
            c[sum(comb(t,2) for t in blocks) + comb(remaining,2)] += 1
        for b in (2,3):
            if remaining-b>=1:
                visit(blocks+[b],remaining-b)
    for start in (1,2):
        if start<n:
            visit([start],n-start)
    return +c


def unimodal(seq):
    p = max(range(len(seq)),key=lambda i:seq[i]); return all(seq[i]<=seq[i+1] for i in range(p)) and all(seq[i]>=seq[i+1] for i in range(p,len(seq)-1))

if __name__ == '__main__':
    for n in range(2,10):
        a = formula(n)
        b = direct(n)
        assert a == b, (n,a,b)
        print(f'exact_poset_crosscheck n={n} total={sum(a.values())} polynomial={sorted(a.items())}')
    for n in range(2,29):
        assert formula(n)==by_blocks(n), n
    for n in range(2,121):
        c=formula(n)
        assert sum(c.values()) == (1 if n==2 else 2 if n==3 else sum(formula(n-2).values())+sum(formula(n-3).values()) if n>=5 else 2), n
        expect = (n <= 10 or n == 12)
        assert unimodal(list(c.values())) == expect, n
    print('ALL CHECKS PASSED; independent_full_lehmer_posets_n=2..9; total_all_codes='+str(sum(factorial(n) for n in range(2,10)))+'; block_compositions_n=2..28; coefficient_and_unimodality_n=2..120')
