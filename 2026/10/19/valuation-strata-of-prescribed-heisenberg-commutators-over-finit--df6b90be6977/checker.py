#!/usr/bin/env python3
"""Exact finite-ring checks for the commutator-fiber theorem (standard library)."""
from collections import Counter
from itertools import product


def modular_ring(p, n):
    size = p ** n
    mul = [[(a * b) % size for b in range(size)] for a in range(size)]
    add = [[(a + b) % size for b in range(size)] for a in range(size)]
    neg = [(-a) % size for a in range(size)]
    def val(a):
        if a == 0:
            return n
        i = 0
        while a % p == 0:
            a //= p
            i += 1
        return i
    return (size, p, n, mul, add, neg, val)


def binary_dual_ring():
    # F_2[t]/(t^2), not isomorphic to Z/4.
    mul = [[((a & 1) * (b & 1)) | ((((a & 1) * (b >> 1)) ^ ((a >> 1) * (b & 1))) << 1)
            for b in range(4)] for a in range(4)]
    add = [[a ^ b for b in range(4)] for a in range(4)]
    neg = list(range(4))
    def val(a):
        return 2 if a == 0 else (1 if a == 2 else 0)
    return (4, 2, 2, mul, add, neg, val)


def four_dual_ring():
    # F_4 = F_2[u]/(u^2+u+1), and R = F_4[t]/(t^2).
    def fmul(a, b):
        bits = 0
        for i in range(2):
            for j in range(2):
                if (a >> i) & (b >> j) & 1:
                    bits ^= 1 << (i+j)
        if bits & 4:
            bits ^= 7
        return bits
    def mul_entry(a, b):
        a0, a1 = a & 3, a >> 2
        b0, b1 = b & 3, b >> 2
        return fmul(a0, b0) | ((fmul(a0, b1) ^ fmul(a1, b0)) << 2)
    mul = [[mul_entry(a, b) for b in range(16)] for a in range(16)]
    add = [[a ^ b for b in range(16)] for a in range(16)]
    neg = list(range(16))
    def val(a):
        return 2 if a == 0 else (1 if (a & 3) == 0 else 0)
    return (16, 4, 2, mul, add, neg, val)


def target_count(q, n, m, valuation):
    stop = min(valuation, n-1)
    result = sum((q ** (2*m*(n-s)) - q ** (2*m*(n-s-1)))
                 * q ** ((2*m-1)*n+s) for s in range(stop+1))
    return result + (q ** (2*m*n) if valuation == n else 0)


def check_one(ring, m):
    size, q, n, mul, add, neg, val = ring
    vectors = list(product(range(size), repeat=2*m))
    counts = Counter()
    for v in vectors:
        for w in vectors:
            t = 0
            for i in range(m):
                t = add[t][mul[v[i]][w[m+i]]]
                t = add[t][neg[mul[w[i]][v[m+i]]]]
            counts[t] += 1
    assert sum(counts.values()) == size ** (4*m)
    for t in range(size):
        assert counts[t] == target_count(q, n, m, val(t)), \
            (q, n, m, t, counts[t], target_count(q, n, m, val(t)))
    assert len(set(counts[t] for t in range(1, size))) == n
    print('ring-size', size, 'q', q, 'length', n, 'm', m,
          'fiber-by-valuation', [target_count(q, n, m, s) for s in range(n+1)])
    if m == 1 and size <= 4:
        # Full independent group-word evaluation, including arbitrary centers.
        elems = list(product(range(size), repeat=3))
        def prod(g, h):
            return (add[g[0]][h[0]], add[g[1]][h[1]],
                    add[add[g[2]][h[2]]][mul[g[0]][h[1]]])
        def inverse(g):
            return (neg[g[0]], neg[g[1]],
                    add[neg[g[2]]][mul[g[0]][g[1]]])
        actual = Counter()
        for g in elems:
            for h in elems:
                comm = prod(prod(prod(inverse(g), inverse(h)), g), h)
                assert comm[0] == comm[1] == 0
                actual[comm[2]] += 1
        for t in range(size):
            assert actual[t] == size * size * counts[t]


def main():
    for p, n, m in [(2, 1, 1), (2, 2, 1), (2, 3, 1),
                    (3, 1, 2), (3, 2, 1), (2, 2, 2)]:
        check_one(modular_ring(p, n), m)
    check_one(binary_dual_ring(), 1)
    check_one(four_dual_ring(), 1)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
