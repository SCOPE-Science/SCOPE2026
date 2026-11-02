#!/usr/bin/env python3
"""Exact probability checker for independent-agent Bernoulli lottery goods.

No third-party dependencies. Run with: python3 check.py
"""
from fractions import Fraction as Q
from itertools import product


def mass(parameters):
    out = [Q(1)]
    for p in parameters:
        nxt = [Q(0)] * (len(out) + 1)
        for j, value in enumerate(out):
            nxt[j] += value * (1 - p)
            nxt[j + 1] += value * p
        out = nxt
    return out


def ex_post_probability(parameters, left_mask):
    left = mass([p for j, p in enumerate(parameters) if left_mask & (1 << j)])
    right = mass([p for j, p in enumerate(parameters) if not (left_mask & (1 << j))])
    a = sum(x * y for i, x in enumerate(left) for j, y in enumerate(right) if i >= j)
    b = sum(x * y for i, x in enumerate(left) for j, y in enumerate(right) if i <= j)
    return a * b


def direct_probability(parameters, left_mask):
    m = len(parameters)
    out = Q(0)
    for bits in product((0, 1), repeat=2*m):
        weight = Q(1)
        for i in range(2):
            for j, p in enumerate(parameters):
                weight *= p if bits[i*m+j] else (1-p)
        u1left = sum(bits[j] for j in range(m) if left_mask & (1 << j))
        u1right = sum(bits[j] for j in range(m) if not(left_mask & (1 << j)))
        u2left = sum(bits[m+j] for j in range(m) if left_mask & (1 << j))
        u2right = sum(bits[m+j] for j in range(m) if not(left_mask & (1 << j)))
        if u1left >= u1right and u2right >= u2left:
            out += weight
    return out


def check():
    p = [Q(7, 20), Q(7, 20), Q(1, 20), Q(13, 20)]
    assert sum(p[:2]) == sum(p[2:]) == Q(7,10)
    all_scores = {mask: ex_post_probability(p, mask) for mask in range(16)}
    assert all_scores[3] == Q(13144772641, 25600000000)
    assert all_scores[7] == Q(13170400347, 25600000000)
    assert all_scores[7] - all_scores[3] == Q(12813853,12800000000)
    assert max(all_scores.values()) == all_scores[7]
    assert {mask for mask, v in all_scores.items() if v == max(all_scores.values())} == {7, 8}
    for mask, value in all_scores.items():
        assert value == direct_probability(p, mask), mask
    # Test cases complement the analytic universal three-good exchange identity.
    for numerator in product(range(5), repeat=3):
        q = [Q(x,4) for x in numerator]
        k = max(range(3), key=lambda j:q[j])
        best = ex_post_probability(q, 1<<k)
        assert best == max(ex_post_probability(q, mask) for mask in range(8))
    print('PASS: 16 independent exact probabilities match 256-outcome enumeration.')
    print('PASS: 125 three-item parameter vectors satisfy the singleton-max rule.')
    print('PASS: ex-ante EF =',all_scores[3],', better alternative =',all_scores[7])
    print('PASS: strict difference =', all_scores[7]-all_scores[3])

if __name__ == '__main__':
    check()
