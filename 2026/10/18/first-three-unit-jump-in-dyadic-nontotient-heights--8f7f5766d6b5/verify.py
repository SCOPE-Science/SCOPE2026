#!/usr/bin/env python3
"""Verify complete dyadic Nontotient argmax fibers through 2**19."""
from array import array
from math import isqrt
from pathlib import Path
import json

LIMIT = 1 << 19


def phi_by_prime_depletion(limit):
    phi = array('I', range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for n in range(p, limit + 1, p):
                phi[n] -= phi[n] // p
    return phi


def phi_by_smallest_factor(limit):
    spf = array('I', [0]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == 0:
            for n in range(p * p, limit + 1, p):
                if spf[n] == 0:
                    spf[n] = p
    phi = array('I', [0]) * (limit + 1)
    phi[1] = 1
    for n in range(2, limit + 1):
        p = spf[n] or n
        m = n // p
        phi[n] = p * phi[m] if m % p == 0 else (p - 1) * phi[m]
    return phi


def iteration_heights(phi, limit):
    heights = bytearray(limit + 1)
    for n in range(2, limit + 1):
        nxt = n - phi[n]
        assert 1 <= nxt < n
        heights[n] = heights[nxt] + 1
    return heights


def argmax_fibers(heights):
    entries = []
    for k in range(1, 20):
        low, high = 1 << (k - 1), 1 << k
        maximum = max(heights[low + 1:high + 1])
        winners = [n for n in range(low + 1, high + 1)
                   if heights[n] == maximum]
        entries.append({"k": k, "maximum_height": int(maximum),
                        "maximizers": winners})
    return entries


def main():
    phi_a = phi_by_prime_depletion(LIMIT)
    phi_b = phi_by_smallest_factor(LIMIT)
    assert phi_a == phi_b
    heights_a = iteration_heights(phi_a, LIMIT)
    heights_b = iteration_heights(phi_b, LIMIT)
    assert heights_a == heights_b
    entries = argmax_fibers(heights_a)
    certificate = json.loads(Path(__file__).with_name('MAXIMIZERS.json').read_text(encoding='utf8'))
    assert certificate['entries'] == entries
    assert len(entries) == 19
    assert sum(len(e['maximizers']) for e in entries) == 123
    M = [e['maximum_height'] for e in entries]
    assert M == [1, 2, 3, 4, 6, 7, 9, 10, 12, 14, 16, 18,
                 20, 22, 24, 26, 28, 30, 33]
    assert all(M[k] - M[k-1] <= 2 for k in range(1, 18))
    assert M[18] - M[17] == 3
    assert len(entries[17]['maximizers']) == 44
    assert entries[18]['maximizers'] == [462210]
    x, orbit = 462210, [462210]
    while x != 1:
        x -= phi_a[x]
        orbit.append(x)
    assert len(orbit) == 34 and orbit[-1] == 1
    print('VERIFIED', 'complete dyadic argmax fibers k=1..19,',
          sum(len(e['maximizers']) for e in entries), 'maximizers')
    for e in entries:
        print(e['k'], e['maximum_height'], len(e['maximizers']),
              e['maximizers'][0])

if __name__ == '__main__':
    main()
