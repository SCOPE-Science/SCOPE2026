#!/usr/bin/env python3
"""Exact finite checks for record-count / positive-occupation dependence.

Uses only the standard library. A magnitude-bin family uses independent
J uniform in {0,...,m-1}, independent U uniform on (1, 1.003), and
amplitudes 100^J U; independent symmetric signs are appended.
The sign of every nonzero partial sum is constant on each bin-and-rank
cell. Consequently exact rank enumeration computes the true expectations.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import comb


def empirical_stats(weighted_paths, n):
    rbar = abar = rab = Q(0)
    table = [[Q(0) for _ in range(n)] for _ in range(n)]
    total = Q(0)
    for increments, weight in weighted_paths:
        total += weight
        s = 0
        best = 0
        rec = []
        pos = []
        for x in increments:
            s += x
            rec.append(int(s > best))
            best = max(best, s)
            pos.append(int(s > 0))
        rbar += weight * sum(rec)
        abar += weight * sum(pos)
        rab += weight * sum(rec) * sum(pos)
        for i in range(n):
            for j in range(n):
                table[i][j] += weight * rec[i] * pos[j]
    assert total == 1, total
    return rbar, abar, rab, rab - rbar*abar, table


def enumerate_bins(m, n=3):
    # Integer arithmetic with a rank-dependent representative of U.
    # 100^j*(1000+rank) reflects U uniform (1,1.003), not a point-mass
    # law: on each cell the sign patterns are invariant under all U values.
    signs = list(product((-1, 1), repeat=n))
    ranks = list(permutations(range(1, n+1)))
    weight = Q(1, (m**n) * 2**n * len(ranks))
    for js in product(range(m), repeat=n):
        for rank in ranks:
            amplitudes = [100**j * (1000+rank[i]) for i,j in enumerate(js)]
            for sig in signs:
                yield tuple(sig[i]*amplitudes[i] for i in range(n)), weight


def triangle_prob(m):
    vals = list(enumerate_bins(m,3))
    s = Q(0)
    for xs,weight in vals:
        a,b,c = map(abs, xs)
        s += weight * int(a > b+c)
    return s


def main():
    # Analytical nine-cell joint matrix, with t=P(A>B+C).
    def expected(t):
        return [
            [Q(1,2), Q(3,8), Q(3,8)-t/8],
            [Q(1,4), Q(3,8), Q(5,16)],
            [Q(3,16), Q(11,48), Q(5,16)]
        ]
    checks = 0
    for m in [1,2,3,5,8]:
        t=triangle_prob(m)
        re,ae,rae,cov,table=empirical_stats(enumerate_bins(m,3),3)
        assert re == Q(19,16) and ae==Q(3,2)
        assert rae==Q(35,12)-t/8
        assert cov == Q(109,96)-t/8
        assert table == expected(t), (m,t,table)
        assert 0 <= t < Q(1,3)
        checks += 13
        print('bins',m,'triangle_probability',t,'covariance',cov)
    # For a symmetric continuous law with |X| uniform (0,1),
    # P(A>B+C)= int_0^1 [A^2/2] dA = 1/6.
    assert Q(109,96)-Q(1,6)/8 == Q(107,96)
    checks += 1
    # At n<=2 the covariance is law-independent: exact rank enumeration
    # in two strongly different magnitude-bin models.
    for n,goal in [(1,Q(1,4)),(2,Q(5,8))]:
        for m in [1,5]:
            _,_,_,cov,_=empirical_stats(enumerate_bins(m,n),n)
            assert cov==goal,(n,m,cov,goal)
            checks += 1
    # On bin-separation events with pairwise distinct J values, the
    # uniquely largest amplitude exceeds the sum of the other two.
    for m in [3,5,8]:
        t=triangle_prob(m)
        assert 3*t >= Q(m*(m-1)*(m-2),m**3)
        checks += 1
    print('EXACT_VERIFICATION_OK',checks,'identity_groups')


if __name__=='__main__':
    main()
