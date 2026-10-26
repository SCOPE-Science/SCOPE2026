#!/usr/bin/env python3
"""Exact finite checks for the multipartite metric transportation identity.

Works with Python's standard library. Finite enumeration corroborates but is not
substituted for the unrestricted flow argument in the theorem.
"""
from fractions import Fraction as F
from itertools import product, permutations


def expected(masses, parts, lengths):
    P = sum(max(a, 0) for a in masses)
    if P == 0:
        return F(0)
    overloads = [max(0, sum(abs(masses[j]) for j, k in enumerate(parts) if k == i) - P)
                 for i in range(len(lengths))]
    assert sum(bool(x) for x in overloads) <= 1
    return F(P) + max((lengths[i]-1)*overloads[i] for i in range(len(lengths)))


def brute(masses, parts, lengths):
    supply = [i for i, a in enumerate(masses) for _ in range(max(0, a))]
    demand = [i for i, a in enumerate(masses) for _ in range(max(0, -a))]
    if not supply:
        return F(0)
    values = []
    for pi in set(permutations(demand)):
        cost = sum((lengths[parts[a]] if parts[a]==parts[b] else F(1))
                   for a,b in zip(supply,pi))
        values.append(cost)
    return min(values)


def run():
    configurations = [
        ((2, 2), (F(3,2), F(7,4))),
        ((2, 2, 1), (F(5,4), F(7,4), F(2))),
        ((3, 2, 1), (F(7,4), F(5,4), F(3,2))),
        ((2, 1, 2, 2), (F(5,4), F(2), F(3,2), F(7,4))),
        ((2, 2, 2), (F(2), F(11,8), F(9,8))),
    ]
    cases = 0
    interpolations=0
    for sizes, ts in configurations:
        parts = tuple(i for i, size in enumerate(sizes) for _ in range(size))
        for ms in product((-1, 0, 1), repeat=len(parts)):
            if sum(ms):
                continue
            predicted = expected(ms, parts, ts)
            observed = brute(ms, parts, ts)
            assert observed == predicted, (sizes,ts,ms, observed, predicted)
            qs = tuple(F(3,2) for _ in ts)
            midpoint = tuple((a+b)/2 for a,b in zip(ts,qs))
            assert expected(ms,parts,midpoint) == (predicted+expected(ms,parts,qs))/2
            cases += 1
            interpolations += 1
    print('MULTIPARTITE_TRANSPORT_EXACT_OK cases=%s norm_affinity_checks=%s' % (cases, interpolations))

if __name__=='__main__':
    run()
