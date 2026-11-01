#!/usr/bin/env python3
"""Exact finite-ring rule-184 traffic convergence census checker.

No external dependencies. All coefficient arithmetic is rational and exact.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def update(x, n):
    mask = (1 << n) - 1
    right = (x >> 1) | ((x & 1) << (n - 1))
    moving = x & (~right & mask)
    return (x & ~moving) | (((moving << 1) | (moving >> (n - 1))) & mask)


def time_to_cycle(x, n):
    seen = {}
    while x not in seen:
        seen[x] = len(seen)
        x = update(x, n)
    return seen[x]


def catalan(m):
    return comb(2 * m, m) // (m + 1)


def coeff_log(n, k, t):
    """n*[u^n z^k]log(1/(1-B_t(u,z)))."""
    atoms = [(1, 0, 1)] + [(2*j, j, catalan(j-1)) for j in range(1, min(t+1,k)+1)]
    current = {(0, 0): 1}
    result = Fraction(0)
    for number_atoms in range(1, n+1):
        next_terms = defaultdict(int)
        for (length, cars), count in current.items():
            for alen, acars, mult in atoms:
                if length+alen <= n and cars+acars <= k:
                    next_terms[length+alen, cars+acars] += count*mult
        current = next_terms
        result += Fraction(current.get((n,k), 0), number_atoms)
        if not current:
            break
    final = n*result
    assert final.denominator == 1
    return final.numerator


def test_local_ballot_preimages():
    checks = 0
    for t in range(0, 6):
        length = 2*t+2
        for initial in range(1 << length):
            enlarged = length + 6
            current = initial
            for _ in range(t):
                current = update(current, enlarged)
            observed = ((current >> t) & 3) == 3
            w = format(initial, f'0{length}b')
            height = 0
            ballot = True
            for bit in w:
                height += 1 if bit == '1' else -1
                ballot &= height > 0
            expected = w.startswith('11') and ballot
            assert observed == expected, (t, w, observed, expected)
            checks += 1
    return checks


def test_census():
    states = 0
    comparisons = 0
    last_step = 0
    for n in range(2, 16):
        actual = defaultdict(int)
        for x in range(1 << n):
            k = x.bit_count()
            t = time_to_cycle(x,n)
            actual[k,t] += 1
            states += 1
        for k in range(n+1):
            m = min(k,n-k)
            for t in range(m):
                expected = coeff_log(n,m,t)
                observed = sum(actual[k,s] for s in range(t+1))
                assert expected == observed, (n,k,t,expected,observed)
                comparisons += 1
            assert not any(tt > max(0,m-1) for kk,tt in actual if kk == k)
            if m >= 2:
                expected_last = n*catalan(m-1)
                actual_last = actual[k,m-1]
                assert actual_last == expected_last, (n,k,expected_last,actual_last)
                last_step += 1
    return states,comparisons,last_step


if __name__ == '__main__':
    checks = test_local_ballot_preimages()
    states, comparisons, last_step = test_census()
    print(f'local_preimage_windows={checks}')
    print(f'full_orbit_states={states}')
    print(f'exact_cdf_comparisons={comparisons}')
    print(f'last_step_catalan_comparisons={last_step}')
    print('TRAFFIC_CATALAN_LOG_VERIFY_OK')
