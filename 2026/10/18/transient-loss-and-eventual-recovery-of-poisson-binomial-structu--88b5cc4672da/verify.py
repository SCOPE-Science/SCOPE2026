"""Exact-rational checks for finite-alphabet strict upper-record counts.

Uses only the Python standard library. The universal arguments are proved
in RESULT.md; finite checks validate the stated certificates.
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial


def pgf_enumerate(weights, n):
    p = tuple(F(x, sum(weights)) for x in weights)
    counts = [F(0)] * (min(len(p) - 1, n - 1) + 1)
    for seq in product(range(len(p)), repeat=n):
        prob = F(1)
        for i in seq:
            prob *= p[i]
        k = 0
        maximum = seq[0]
        for i in seq[1:]:
            if i > maximum:
                k += 1
                maximum = i
        counts[k] += prob
    assert sum(counts) == 1
    return counts


def pgf_dp(weights, n):
    p = tuple(F(x, sum(weights)) for x in weights)
    d = len(p)
    state = [[F(0)] * d for _ in range(d)]
    for i in range(d):
        state[i][0] = p[i]
    for _ in range(n - 1):
        nxt = [[F(0)] * d for _ in range(d)]
        for i in range(d):
            for k in range(d):
                if not state[i][k]:
                    continue
                for j in range(d):
                    kk = k + (j > i)
                    nxt[max(i, j)][kk] += state[i][k] * p[j]
        state = nxt
    return [sum(state[i][k] for i in range(d)) for k in range(d)]


def disc_cubic(a, b, c, d):
    return 18*a*b*c*d - 4*b**3*d + b*b*c*c - 4*a*c**3 - 27*a*a*d*d


def pb_limit(weights):
    p = tuple(F(x, sum(weights)) for x in weights)
    q = [p[i] / sum(p[i:]) for i in range(len(p)-1)]
    v = [F(1)]
    for x in q:
        out = [F(0)] * (len(v)+1)
        for j, y in enumerate(v):
            out[j] += y*(1-x)
            out[j+1] += y*x
        v = out
    return q, v


def exact_size_biased_permutation(weights):
    p = [F(x, sum(weights)) for x in weights]
    d = len(p)
    law = [F(0)]*d
    for order in permutations(range(d)):
        mass = F(1)
        remaining = F(1)
        for i in order:
            mass *= p[i] / remaining
            remaining -= p[i]
        k, mx = 0, order[0]
        for j in order[1:]:
            if j > mx:
                k += 1
                mx = j
        law[k] += mass
    return law


def run():
    five = pgf_enumerate((1, 1, 1, 1, 8), 3)
    assert five == [F(197, 288), F(247, 864), F(13, 432)]
    assert five[1]**2 - 4 * five[0]*five[2] == F(-455, 746496)
    four = pgf_enumerate((1, 1, 1, 5), 4)
    assert four == [F(649, 1024), F(1309, 4096), F(93, 2048), F(5, 4096)]
    assert disc_cubic(four[3], four[2], four[1], four[0]) == F(-61127, 274877906944)
    num = 0
    for weights in ((1, 1, 1, 5), (1, 1, 1, 1, 8), (1, 2, 3), (2, 1, 4, 3)):
        d = len(weights)
        q, limit = pb_limit(weights)
        assert len(q) == d - 1 and len(set(q)) == d - 1
        assert exact_size_biased_permutation(weights) == limit
        for n in range(1, 13):
            coeff = pgf_dp(weights, n)
            assert sum(coeff) == 1
            assert sum(abs(coeff[j]-limit[j]) for j in range(d))/2 <= F(1 - F(weights[-1],sum(weights))) ** n
            if n <= 4:
                brute = pgf_enumerate(weights,n)
                assert coeff[:len(brute)] == brute
            num += 1
    assert pgf_dp((1, 1, 1, 1, 8), 3)[:3] == five
    assert pgf_dp((1, 1, 1, 5), 4)[:4] == four
    print('PASS: two exact nonreal-root certificates, size-biased law identities,', num, 'exact DP/TV checks, finite enumeration.')

if __name__ == '__main__':
    run()
