"""Finite consistency checks for full one-block zip maps (not an infinite proof)."""
from itertools import product
from collections import Counter
from math import prod


def partitions(n, least=1):
    if n == 0:
        yield ()
    for k in range(least, n + 1):
        for tail in partitions(n - k, k):
            yield (k,) + tail


def profile(tau):
    bins = Counter(tau)
    return tuple(sorted(bins.values()))


def fixed_degree_polynomial(tau):
    bins = Counter(tau)
    return tuple(sorted(Counter({d: d * sum(1 for v in bins.values() if v == d) for d in set(bins.values())}).items()))


def periodic_weight(tau, n, r):
    bins = Counter(tau)
    weighted = 0
    for word in product(range(len(tau)), repeat=n):
        weighted += prod(bins[tau[letter]] ** r for letter in word)
    return weighted


def run():
    tested = 0
    for N in range(1, 7):
        seen = set()
        polys = {}
        for k in range(1, N + 1):
            for tau in product(range(k), repeat=N):
                if set(tau) != set(range(k)):
                    continue
                ps = profile(tau)
                ip = fixed_degree_polynomial(tau)
                if ip in polys:
                    assert polys[ip] == ps
                else:
                    polys[ip] = ps
                seen.add(ps)
                assert sum(d for d in ps) == N
                # Any fixed word determines a unique periodic zip point.
                if N <= 4:
                    for n in range(1, 4):
                        for r in range(3):
                            assert periodic_weight(tau, n, r) == sum(d**(r+1) for d in ps)**n
                tested += 1
        assert seen == set(partitions(N))
        assert len(polys) == len(seen)
    a = (0, 0, 0, 1)
    b = (0, 0, 1, 1)
    assert profile(a) == (1, 3)
    assert profile(b) == (2, 2)
    assert periodic_weight(a, 1, 1) == 10
    assert periodic_weight(b, 1, 1) == 8
    print(f'CHECKS_PASS {tested} surjective maps; N=1..6; periodic n=1..3 for N<=4; weighted r=0..2')

if __name__ == '__main__':
    run()
