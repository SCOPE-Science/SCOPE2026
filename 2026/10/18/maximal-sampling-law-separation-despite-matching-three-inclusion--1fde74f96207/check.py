"""Finite exact checks of a three-wise balanced affine-hyperplane sampling construction.
No finite enumeration is used as a proof of its asymptotic central limit theorem.
"""
from itertools import combinations
from collections import Counter
from math import comb
from fractions import Fraction


def parity(i):
    return i.bit_count() % 2


def construction(m):
    d, N = 2*m, 1 << (2*m)
    Q = lambda x: sum(((x >> (2*j)) & 1) * ((x >> (2*j+1)) & 1) for j in range(m)) % 2
    y = [(-1)**Q(x) for x in range(N)]
    expected_mean_sum = 1 << m
    assert sum(y) == expected_mean_sum
    assert sum(t*t for t in y) == N
    for a in range(N):
        W = sum(y[x] * (-1)**parity(a & x) for x in range(N))
        assert W == (1 << m)*(-1)**Q(a), (m,a,W)
    blocks = [[x for x in range(N) if parity(a & x)==b]
              for a in range(1,N) for b in (0,1)]
    assert len(blocks) == 2*(N-1)
    assert all(len(B)==N//2 for B in blocks)
    Uvals = Counter()
    for B in blocks:
        raw = sum(y[x] for x in B)
        # Standardized score is 2/sqrt(N) * (raw - sqrt(N)/2)
        # store the numerator 2*raw-sqrt(N) instead.
        Uvals[2*raw-(1<<m)] += 1
    assert Uvals == {-(1<<m):N-1, (1<<m):N-1}, (m,Uvals)
    if m == 2:
        for t in (1,2,3):
            predicted = Fraction(comb(N//2,t),comb(N,t))
            for sub in combinations(range(N),t):
                observed = Fraction(sum(set(sub).issubset(B) for B in map(set,blocks)),len(blocks))
                assert observed == predicted, (t,sub,observed,predicted)
    # Compare common finite-population variance exactly.
    S2 = Fraction(sum((N*y[x]-(1<<m))**2 for x in range(N)), N*N*(N-1))
    assert S2 == 1
    v_srs = Fraction(N//2*(N-N//2),N)*S2
    assert v_srs == Fraction(N,4)
    print('m=',m,'N=',N,'blocks=',len(blocks),'exact checks passed')

for m in (2,3,4):
    construction(m)
print('ALL EXACT CHECKS PASSED')
