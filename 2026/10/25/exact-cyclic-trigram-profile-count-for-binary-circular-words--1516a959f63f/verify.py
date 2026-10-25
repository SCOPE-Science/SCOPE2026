#!/usr/bin/env python3
"""Independent finite checks for cyclic binary trigram profiles.

No external libraries; direct source-word enumeration and a separate flow
parameterization are compared as sets of 8-component integer vectors.
"""
from itertools import product
from collections import Counter

TRIPLES = tuple(''.join(p) for p in product('01', repeat=3))


def direct_profiles(n):
    result = set()
    for bits in product('01', repeat=n):
        vector = [0] * 8
        for i in range(n):
            j = int(bits[i]) * 4 + int(bits[(i+1) % n]) * 2 + int(bits[(i+2) % n])
            vector[j] += 1
        result.add(tuple(vector))
    return result


def from_parameters(n):
    vectors = set()
    # Counts 001 and 100 = t; 011 and 110 = u.
    # Counts 010=(t-u)_+ + j; 101=(u-t)_+ + j.
    for t in range(n + 1):
        for u in range(n + 1):
            core = 3 * max(t, u) + min(t, u)
            if core > n:
                continue
            for j in range((n-core) // 2 + 1):
                remainder = n - core - 2*j
                for a in range(remainder + 1):
                    h = remainder - a
                    if t and u:
                        valid = True
                    elif t:
                        valid = h == 0
                    elif u:
                        valid = a == 0
                    elif j:
                        valid = (a == 0 and h == 0)
                    else:
                        valid = ((a == 0) != (h == 0))
                    if not valid:
                        continue
                    c = max(t-u, 0) + j
                    f = max(u-t, 0) + j
                    vectors.add((a, t, c, u, t, f, u, h))
    return vectors


def generating_function_coeff(n):
    # Disjoint cases in the four-vertex de Bruijn flow graph.
    ans = 2 + (n % 2 == 0)  # constant and alternating profiles
    # Exactly one of t,u is positive.
    for t in range(1, n//3 + 1):
        for j in range((n-3*t)//2 + 1):
            ans += 2
    # Both t,u positive; a+h is determined by length.
    for t in range(1, n + 1):
        for u in range(1, n + 1):
            core = 3*max(t,u) + min(t,u)
            if core > n:
                continue
            for j in range((n-core)//2 + 1):
                ans += n-core-2*j+1
    return ans


def run():
    checks = []
    for n in range(1, 17):
        raw = direct_profiles(n)
        pred = from_parameters(n)
        a = generating_function_coeff(n)
        assert raw == pred, (n, 'vector_set_mismatch', len(raw), len(pred))
        assert len(raw) == a, (n, 'count_mismatch', len(raw), a)
        checks.append(a)
    # Independent spot checks at larger lengths by flow vectors, not 2^n words.
    for n in (20, 24, 30):
        assert len(from_parameters(n)) == generating_function_coeff(n)
    # z^n GF coefficient for n=1..16 must be the following list.
    assert checks == [2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271], checks
    print('VERIFY_OK')
    print('distinct_cyclic_3gram_profiles_n1_to16=' + ','.join(map(str, checks)))
    print('parameter_checks_n20_24_30=OK')

if __name__ == '__main__':
    run()
