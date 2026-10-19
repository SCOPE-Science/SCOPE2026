#!/usr/bin/env python3
"""Independent finite checks for the cyclic binary trigram-profile formula.

No external dependencies. The infinite statement follows from the proof, not
from the finite checks. Run: python3 verify.py
"""
from itertools import product
from math import comb

# Polynomial N(z)/D(z), with coefficients in ascending degree.
NUM = [0, 2, -3, 1, -1, 0, 5, -5, 6, -7, 3]


def poly_mul(x, y):
    out = [0] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i+j] += a*b
    return out


def coefficients(limit):
    d = [1]
    for _ in range(5):
        d = poly_mul(d, [1, -1])
    for f in ([1, 1], [1, 0, 1], [1, 1, 1]):
        d = poly_mul(d, f)
    assert d[0] == 1
    f = [0] * (limit + 1)
    for n in range(1, limit + 1):
        f[n] = (NUM[n] if n < len(NUM) else 0) - sum(
            d[j]*f[n-j] for j in range(1, min(n, len(d)-1)+1)
        )
    return f


def cyclic_profile_bits(x, n):
    counts = [0] * 8
    for i in range(n):
        v = 4*((x >> i)&1) + 2*((x >> ((i+1) % n))&1) + ((x >> ((i+2) % n))&1)
        counts[v] += 1
    return tuple(counts)


def word_spectra(n):
    return {cyclic_profile_bits(x, n) for x in range(1 << n)}


def structural_valid(t):
    u,a,c,b,a2,d,b2,v = t  # indices 000,001,010,011,100,101,110,111
    if sum(t) == 0 or a != a2 or b != b2 or a+d != b+c:
        return False
    if a > 0 and b > 0:
        return True
    if a > 0:
        return b == 0 and v == 0
    if b > 0:
        return a == 0 and u == 0
    if c > 0:
        return d == c and u == 0 and v == 0
    return d == 0 and ((u > 0) != (v > 0))


def graph_eulerian(t):
    if not sum(t):
        return False
    edges = [(i >> 1, i & 3) for i in range(8)]
    ins = [0]*4
    outs = [0]*4
    for m,(u,v) in zip(t,edges):
        outs[u]+=m
        ins[v]+=m
    if ins != outs:
        return False
    used = {v for v in range(4) if ins[v]+outs[v] > 0}
    root = next(iter(used))
    def reachable(reverse=False):
        seen = {root}
        stack = [root]
        while stack:
            v = stack.pop()
            for k, (a,b) in enumerate(edges):
                if not t[k]:
                    continue
                src,dst = (b,a) if reverse else (a,b)
                if src == v and dst not in seen:
                    seen.add(dst)
                    stack.append(dst)
        return seen
    return reachable(False) == used and reachable(True) == used


def compositions(total, k):
    if k == 1:
        yield (total,)
        return
    for j in range(total+1):
        for rest in compositions(total-j,k-1):
            yield (j,)+rest


def parametric_count(n):
    # Directly count the disjoint parametrized families from the proof.
    out = 2  # the all-zero and all-one cycles
    if n % 2 == 0:
        out += 1  # the alternating profile
    # three-vertex supports, one directed triangle in either orientation
    for a in range(1, n//3+1):
        for slack in range((n-3*a)//2 + 1):
            out += 2  # remaining loops have exactly one nonnegative value
    # four-vertex supports. For fixed base length, u+v has n-base+1 solutions.
    for a in range(1, n+1):
        for b in range(1, n+1):
            lo = max(0, a-b)
            if a+3*b+2*lo > n:
                continue
            for c in range(lo, (n-a-3*b)//2+1):
                out += n-(a+3*b+2*c)+1
    return out


def main():
    f = coefficients(60)
    brute_total = 0
    for n in range(1, 19):
        words = word_spectra(n)
        assert len(words) == f[n] == parametric_count(n), (n,len(words),f[n],parametric_count(n))
        brute_total += 1 << n
    for n in range(19, 61):
        assert f[n] == parametric_count(n), (n,f[n],parametric_count(n))
    for n in range(1, 12):
        direct = word_spectra(n)
        feasible = set()
        for t in compositions(n,8):
            p = structural_valid(t)
            e = graph_eulerian(t)
            assert p == e, (n,t,p,e)
            if e:
                feasible.add(t)
        assert direct == feasible, (n,len(direct),len(feasible))
    print('CYCLIC_BINARY_TRIGRAM_PASS',
          'complete_word_lengths=1..18',
          'structural_euler_lengths=1..11',
          'parametric_gf_lengths=1..60',
          'direct_words=',brute_total,
          'first_ten=',f[1:11])

if __name__ == '__main__':
    main()
