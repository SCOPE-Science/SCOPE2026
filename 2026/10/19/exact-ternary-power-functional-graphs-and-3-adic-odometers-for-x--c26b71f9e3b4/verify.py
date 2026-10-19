#!/usr/bin/env python3
"""Exact finite enumeration independently checking the stated quadratic-map graph laws."""
from collections import Counter

for n in range(1, 9):
    modulus = 3 ** n
    image = [(x * x + x) % modulus for x in range(modulus)]
    visited = set()
    cycles = Counter()
    for start in range(0, modulus, 3):
        if start in visited:
            continue
        orbit = []
        at = start
        while at not in orbit:
            if at in visited or at % 3:
                raise AssertionError(('periodic basin', n, start, at))
            orbit.append(at)
            at = image[at]
        assert at == start
        visited.update(orbit)
        cycles[len(orbit)] += 1
    assert len(visited) == modulus // 3
    expected_cycles = Counter({1: 3 ** (n // 2)})
    for t in range(1, (n - 1) // 2 + 1):
        expected_cycles[3 ** (n - 2 * t)] += 2 * 3 ** (t - 1)
    assert cycles == expected_cycles, (n, cycles, expected_cycles)
    assert all(image[x] in visited for x in range(2, modulus, 3))
    assert all(image[x] % 3 == 2 and image[image[x]] in visited
               for x in range(1, modulus, 3))
    assert len(set(image[x] for x in range(2, modulus, 3))) == modulus // 3
    children = Counter()
    for u in range(2, modulus, 3):
        count = sum(image[v] == u for v in range(1, modulus, 3))
        children[count] += 1
    predicted = Counter({3 ** (n // 2): 1})
    for r in range(1, (n - 1) // 2 + 1):
        predicted[2 * 3 ** r] += 3 ** (n - 2 * r - 1)
    if sum(predicted.values()) < modulus // 3:
        predicted[0] += modulus // 3 - sum(predicted.values())
    assert children == predicted, (n, children, predicted)
    assert sum(k * v for k, v in children.items()) == modulus // 3

# Independently test the displacement valuation lemma at finite but large precision.
modulus = 3 ** 22
for x in (3, 6, 9, 12, 18, 27, 45, 81):
    t = 0
    y = x
    while y % 3 == 0:
        y //= 3
        t += 1
    for k in range(5):
        at = x
        for _ in range(3 ** k):
            at = (at + at * at) % modulus
        delta = (at - x) % modulus
        if 2 * t + k < 22:
            z = delta
            val = 0
            while z % 3 == 0:
                z //= 3
                val += 1
            assert val == 2 * t + k, (x, k, val)
print('VERIFY_OK')
