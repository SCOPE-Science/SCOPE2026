#!/usr/bin/env python3
"""Finite exact checks of reciprocal-JR quality loss for two voters.
Reproducible Python 3, standard library only; finite checks complement the proof.
"""
from fractions import Fraction as F
from itertools import product, combinations
from random import Random


def rjr(W, h, support, k):
    """Direct reciprocal-JR definition for all three nonempty voter coalitions."""
    for S in (1, 2, 3):
        if any(S & mask for mask in (support[c] for c in W)):
            continue
        common = [c for c, mask in enumerate(support) if mask & S == S]
        if common and max(k * S.bit_count() * h[c] >= 2 for c in common):
            return False
    return True


def check_case(h, support, k):
    m = len(h)
    committees = list(combinations(range(m), k))
    quality = lambda W: sum((h[c] for c in W), F(0))
    unrestricted = max(quality(W) for W in committees)
    feasible = [quality(W) for W in committees if rjr(W, h, support, k)]
    assert feasible, ('no feasible rJR committee', k, h, support)
    best = max(feasible)
    limit = F(k*k, k*k-k+2)
    assert unrestricted / best <= limit, ('price violates theorem', k, h, support, unrestricted, best)
    # Exact structural equivalence for two voters: singleton claims suffice.
    for W in committees:
        simple = all(
            any(mask & bit for mask in (support[c] for c in W))
            or not any((support[c] & bit) and (k*h[c] >= 2) for c in range(m))
            for bit in (1,2)
        )
        assert simple == rjr(W,h,support,k)
    return 1


def main():
    count=0
    grid=tuple(F(a,12) for a in (6,9,12))
    for k in (2,3,4):
        for m in (k,k+1):
            for labels in product(range(9), repeat=m):
                h=tuple(grid[t // 3] for t in labels)
                supports=tuple((t % 3)+1 for t in labels)
                count+=check_case(h,supports,k)
    rng=Random(20261025)
    random_checks=0
    for k in range(2,11):
        for _ in range(350):
            m=k+rng.randrange(1,5)
            h=tuple(F(rng.randrange(1,13),12) for _ in range(m))
            support=tuple(rng.randint(1,3) for _ in range(m))
            random_checks+=check_case(h,support,k)
    for k in range(2,51):
        h=tuple([F(1)]*k+[F(2,k)])
        support=tuple([1]*k+[2])
        committees=list(combinations(range(k+1),k))
        q=lambda W:sum((h[c] for c in W),F(0))
        unrestricted=max(map(q,committees))
        best=max(q(W) for W in committees if rjr(W,h,support,k))
        assert unrestricted/best==F(k*k,k*k-k+2)
    assert F(4*4,4*4-4+2)==F(8,7)
    assert all(F(k*k,k*k-k+2)<=F(8,7) for k in range(2,51))
    print('VERIFY_OK exhaustive_instances=%d random_instances=%d tight_witnesses=49' % (count,random_checks))

if __name__=='__main__':main()
