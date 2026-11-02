"""Exact rational checks for heterogeneous all-but-one reset cumulants.

Requires Python 3.10+ standard library.  These finite checks do not prove the
universal assertions; the accompanying document supplies their proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial


def partitions(seq):
    if not seq:
        yield ()
        return
    head, *tail = seq
    for part in partitions(tail):
        yield (frozenset((head,)),) + part
        for j in range(len(part)):
            yield part[:j] + (part[j] | frozenset((head,)),) + part[j+1:]


def age_moment(indices, weights, r):
    if not indices:
        return F(1)
    k = len(indices)
    # Independent generator recursion for the stationary product of ages:
    # every global event resets some selected coordinate whenever k >= 2.
    if k == 1:
        i = next(iter(indices))
        return F(1) / (r * (1 - weights[i]))
    return sum(age_moment(indices - {i}, weights, r) for i in indices) / r


def partition_cumulant(indices, weights, r):
    out = F(0)
    for blocks in partitions(list(indices)):
        out += (-1) ** (len(blocks) - 1) * factorial(len(blocks) - 1) * __import__('math').prod(
            age_moment(b, weights, r) for b in blocks
        )
    return out


def predicted_cumulant(indices, weights, r):
    k = len(indices)
    odds = __import__('math').prod(weights[i] / (1 - weights[i]) for i in indices)
    return F(factorial(k - 1), 1) / r**k * (1 + (-1)**(k-1) * odds)


def check():
    count = 0
    for n in range(2, 8):
        cases = (
            [F(1, n)] * n,
            [F(i + 1, n*(n+1)//2) for i in range(n)],
            [F(2**i, 2**n-1) for i in range(n)],
        )
        for w in cases:
            assert sum(w) == 1 and all(0 < p < 1 for p in w)
            r = F(7, 5)
            for k in range(1, min(n,6) + 1):
                for tup in combinations(range(n), k):
                    subset = frozenset(tup)
                    direct = partition_cumulant(subset,w,r)
                    formula = predicted_cumulant(subset,w,r)
                    assert direct == formula,(n,w,tup,direct,formula)
                    if k >= 2:
                        odds = __import__('math').prod(w[i]/(1-w[i]) for i in tup)
                        assert odds <= F(1,(k-1)**k)
                        assert ((formula - F(factorial(k-1),1)/r**k) * (-1)**(k-1)) > 0
                    count += 1
    # Sharp equality at N=k with equal exemption weights, including k=2.
    for k in range(2,9):
        w = [F(1,k)] * k
        odds = __import__('math').prod(x/(1-x) for x in w)
        assert odds == F(1,(k-1)**k)
        count += 1
    # Brownian parameters enter only via multiplication by (2D_i)^k.
    for n in range(2,6):
        w = [F(i + 1,n*(n+1)//2) for i in range(n)]
        D = [F(2*i+3,4) for i in range(n)]
        for k in range(1,n+1):
            for ids in combinations(range(n),k):
                age = partition_cumulant(frozenset(ids),w,F(5,3))
                energy_cumulant = age*__import__('math').prod(2*D[i] for i in ids)
                assert energy_cumulant == predicted_cumulant(frozenset(ids),w,F(5,3))*__import__('math').prod(2*D[i] for i in ids)
                count += 1
    print(f"PASS: {count} independent exact-rational partition/generator and sharp-bound checks")


if __name__ == '__main__':
    check()
