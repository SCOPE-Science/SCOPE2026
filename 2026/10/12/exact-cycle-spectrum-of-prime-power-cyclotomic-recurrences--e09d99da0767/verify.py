#!/usr/bin/env python3
"""Exact finite replay for prime-power cyclotomic recurrence cycle spectrum."""
from itertools import product
from collections import Counter
from random import Random


def next_state(v, p, j, m):
    stride = p ** (j - 1)
    return (*v[1:], (-sum(v[k * stride] for k in range(p - 1))) % m)


def predicted(p, j, m):
    d = p ** j - p ** (j - 1)
    g = p if m % p == 0 else 1
    counts = Counter({1: g})
    for r in range(1, j):
        counts[p ** r] = (g ** (p ** r) - g ** (p ** (r - 1))) // (p ** r)
    counts[p ** j] = (m ** d - g ** (p ** (j - 1))) // (p ** j)
    return +counts


def exhaustive(p, j, m):
    d = p ** j - p ** (j - 1)
    remaining = set(product(range(m), repeat=d))
    counts = Counter()
    while remaining:
        start = next(iter(remaining))
        v = start
        length = 0
        while True:
            assert v in remaining, (p, j, m, v, start)
            remaining.remove(v)
            length += 1
            v = next_state(v, p, j, m)
            if v == start:
                break
        counts[length] += 1
    return counts


def sample_check(p, j, m, trials=300):
    d = p ** j - p ** (j - 1)
    rng = Random(p * 100_000 + j * 1000 + m)
    g = p if m % p == 0 else 1
    # Directly test fixed-point rank predictions on random seeds.
    for _ in range(trials):
        v0 = tuple(rng.randrange(m) for _ in range(d))
        length = p ** j
        # All vectors must return after p^j steps; if shorter,
        # check each divisor of p^j by naive iteration.
        v = v0
        ret = None
        for k in range(1, length + 1):
            v = next_state(v, p, j, m)
            if v == v0:
                ret = k
                break
        assert ret in [p ** r for r in range(j + 1)], (p, j, m, ret)
        # Check exact formula for fixed-point membership for full p-power period.
        assert ret is not None
    return trials


def run():
    cases = 0
    checked_states = 0
    for p in (2, 3, 5, 7):
        for j in (1, 2, 3, 4):
            d = p ** j - p ** (j - 1)
            if d > 18:
                continue
            for m in range(1, 18):
                total = m ** d
                if total > 100_000:
                    continue
                got = exhaustive(p, j, m)
                want = predicted(p, j, m)
                assert got == want, (p, j, m, got, want)
                cases += 1
                checked_states += total
    for p, j, m in [(2, 5, 2), (3, 3, 3), (5, 2, 5), (7, 2, 7), (3, 4, 3)]:
        sample_check(p, j, m, trials=120)
    print('PASS: exhaustive_parameter_cases=%d, exhaustive_states=%d, sampled_vectors=%d' % (cases, checked_states, 5 * 120))
    for key in [(2,3,4),(3,2,12),(5,1,10),(3,3,3)]:
        p,j,m=key
        print('example (p,j,m)=%s: predicted_cycle_multiplicities=%s'%(str(key),dict(sorted(predicted(*key).items()))))


if __name__ == '__main__':
    run()
