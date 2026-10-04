import itertools
import math
import sys


def column(perm, n):
    v = 0
    for path in range(1 << (n + 1)):
        assignment = 0
        for k, var in enumerate(perm):
            a = (path >> k) & 1
            b = (path >> (k + 1)) & 1
            assignment |= ((a << 1) | b) << (2 * var)
        out = ((path & 1) << 1) | ((path >> n) & 1)
        row = (assignment << 2) | out
        v ^= 1 << row
    return v


def rank_n(n):
    basis = {}
    for perm in itertools.permutations(range(n)):
        x = column(perm, n)
        while x:
            pivot = x.bit_length() - 1
            b = basis.get(pivot)
            if b is None:
                basis[pivot] = x
                break
            x ^= b
    return len(basis)


limit = int(sys.argv[1]) if len(sys.argv) > 1 else 7
for n in range(1, limit + 1):
    r = rank_n(n)
    print(n, r, math.factorial(n) - r)
